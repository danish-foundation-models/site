"""Build the publications pages from several sources (all files live in publications/).

1. Fetch works for each DFM member from OpenAlex into openalex_publications.bib. If the fetch
   fails, the existing file is kept.
2. Add papers listed on members' ORCID records that OpenAlex lacks, filled in from Semantic Scholar
   (orcid_publications.bib).
3. Merge in the hand-written overrides.bib, apply the exclude list, de-duplicate (a published version
   beats its preprint) and write the finished list to en/docs/publications.bib (served for download)
   and the pages en/docs/publications.md and da/docs/publications.md.

Set OPENALEX_API_KEY and SEMANTIC_SCHOLAR_API_KEY for higher rate limits (both optional).
"""

import html
import json
import os
import re
import unicodedata
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import bibtexparser
import yaml
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "publications" / "config.yml"
PEOPLE = ROOT / "data" / "people.yml"
BIB = ROOT / "publications" / "openalex_publications.bib"  # raw OpenAlex results
OVERRIDES = ROOT / "publications" / "overrides.bib"  # hand-written entries
COMBINED = ROOT / "en" / "docs" / "publications.bib"  # the finished list, served for download
S2_BIB = ROOT / "publications" / "semanticscholar_publications.bib"  # papers from members' verified Semantic Scholar profiles
ORCID_BIB = ROOT / "publications" / "orcid_publications.bib"  # papers found via ORCID / Semantic Scholar but not in OpenAlex
API = "https://api.openalex.org/works"
SELECT = ",".join(
    [
        "id",
        "doi",
        "title",
        "publication_year",
        "publication_date",
        "type",
        "authorships",
        "primary_location",
        "best_oa_location",
        "locations",
    ]
)

TEXT = {
    "en": {
        "title": "Publications",
        "updated": "Last updated",
        "about": "About this list",
        "stat_papers": "papers since {since_long}",
        "click": "Click to filter",
        "stat_peer": "peer-reviewed publications",
        "stat_astar": "papers at A* venues",
        "tip_papers": "Everything our members have published since {since_long}, including preprints that have not yet been peer reviewed.",
        "tip_peer": "Papers published in a journal or at a conference after peer review. Preprints (for example on arXiv) that have not been reviewed yet are not counted.",
        "tip_astar": "Peer-reviewed papers at top-tier venues (A* in the CORE conference ranking), for example ACL, EMNLP, NeurIPS, ICML and ICLR. Workshops and Findings volumes are not counted.",
        "info": (
            "This list is fetched automatically every day from "
            '<a href="https://openalex.org">OpenAlex</a>, members\' ORCID records and Semantic Scholar, '
            "so it can miss published work or contain mistakes. "
            'Download it as <a href="https://foundationmodels.dk/publications.bib">BibTeX</a>.'
        ),
    },
    "da": {
        "title": "Publikationer",
        "updated": "Senest opdateret",
        "about": "Om denne liste",
        "stat_papers": "artikler siden {since_long}",
        "click": "Klik for at filtrere",
        "stat_peer": "peer-reviewede publikationer",
        "stat_astar": "artikler på A*-konferencer",
        "tip_papers": "Alt, vores medlemmer har publiceret siden {since_long}, inklusive preprints, der endnu ikke er peer-reviewede.",
        "tip_peer": "Artikler udgivet i et tidsskrift eller på en konference efter peer review. Preprints (fx på arXiv), der endnu ikke er gennemgået, tælles ikke med.",
        "tip_astar": "Peer-reviewede artikler på topkonferencer (A* i CORE-rangeringen), fx ACL, EMNLP, NeurIPS, ICML og ICLR. Workshops og Findings-bind tælles ikke med.",
        "info": (
            "Listen hentes automatisk hver dag fra "
            '<a href="https://openalex.org">OpenAlex</a>, medlemmernes ORCID-profiler og Semantic Scholar, '
            "og kan derfor mangle udgivet arbejde eller indeholde fejl. "
            'Hent den som <a href="https://foundationmodels.dk/publications.bib">BibTeX</a>.'
        ),
    },
}


# Venues counted as A* (CORE ranking). The patterns live in publications/config.yml
# (`a_star_venues`) and are matched case-insensitively against the venue name.
A_STAR: list[re.Pattern] = []
A_STAR_NOT: list[re.Pattern] = []  # title patterns for things that are not main-track papers


def is_a_star(entry: dict) -> bool:
    venue = entry.get("journal") or entry.get("booktitle") or ""
    return (
        not is_preprint(entry)
        and any(p.search(venue) for p in A_STAR)
        and not any(p.search(entry.get("title") or "") for p in A_STAR_NOT)
    )


VENUE_FIXES = [  # OpenAlex's own names for some venues read like catalogue entries
    (re.compile(r"^Proceedings of the conference - Association for Computational Linguistics\. Meeting$"),
     "Annual Meeting of the Association for Computational Linguistics (ACL)"),
]


def tidy_venue(name: str) -> str:
    for pattern, replacement in VENUE_FIXES:
        name = pattern.sub(replacement, name)
    return name


def is_preprint(entry: dict) -> bool:
    if entry.get("peer_override"):
        return False
    venue = (entry.get("journal") or entry.get("booktitle") or "").lower()
    if entry.get("oa_type") == "preprint":
        return True
    return not venue or any(w in venue for w in ("arxiv", "preprint", "osf", "ssrn"))


SOURCE_RANK = {"overrides": 0, "openalex": 1, "semanticscholar": 2, "orcid": 3}


def priority(entry: dict) -> tuple:
    """Lower wins when two entries have the same title: hand-written overrides first, then a published
    version over a preprint, then the newer one, then OpenAlex over ORCID."""
    source = entry.get("source", "openalex")
    return (source != "overrides", is_preprint(entry), -date_key(entry), SOURCE_RANK.get(source, 9))


def date_key(entry: dict) -> int:
    return int((entry.get("date") or "0").replace("-", ""))


def long_date(iso: str, lang: str) -> str:
    year, month, day = (int(x) for x in iso.split("-"))
    months = {
        "en": "January February March April May June July August September October November December",
        "da": "januar februar marts april maj juni juli august september oktober november december",
    }[lang].split()
    return f"{day}. {months[month - 1]} {year}" if lang == "da" else f"{day} {months[month - 1]} {year}"


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")  # S³ -> S3, é -> e
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def short_id(value: str) -> str:
    return value.rsplit("/", 1)[-1]


def norm_doi(value: str) -> str:
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", value or "").lower()


def get(params: dict) -> dict:
    key = os.environ.get("OPENALEX_API_KEY")
    if key:
        params = {**params, "api_key": key}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                return json.load(resp)
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")


def full_authorships(work: dict) -> list[dict]:
    """The list endpoint cuts long author lists at 100; the single-work endpoint has them all."""
    params = {"select": "authorships"}
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    url = f"{API}/{short_id(work['id'])}?{urllib.parse.urlencode(params)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                return json.load(resp)["authorships"]
        except Exception:
            if attempt == 3:
                return work["authorships"]
            time.sleep(2 * (attempt + 1))
    return work["authorships"]


def fetch_all(filter_: str) -> list[dict]:
    works, cursor = [], "*"
    while cursor:
        data = get({"filter": filter_, "select": SELECT, "per-page": 200, "cursor": cursor})
        works += data["results"]
        cursor = data["meta"].get("next_cursor")
        time.sleep(0.2)
    return works


def fetch(config: dict) -> list[dict]:
    """Return raw works, each tagged with the DFM members who authored them."""
    by_id: dict[str, dict] = {}
    for person in config["authors"]:
        ids = "|".join(person["openalex"])
        start = max(str(config["since"]), str(person.get("hired") or ""))  # never before `since`
        filter_ = f"author.id:{ids},from_publication_date:{start}"
        if person.get("left"):  # alumni: nothing published after they left
            filter_ += f",to_publication_date:{person['left']}"
        if person.get("exclude_types"):  # e.g. book-chapter, only for this person's profile
            filter_ += ",type:" + "|".join(f"!{t}" for t in person["exclude_types"])
        for work in fetch_all(filter_):
            entry = by_id.setdefault(work["id"], {**work, "members": []})
            if person["name"] not in entry["members"]:
                entry["members"].append(person["name"])
    for ref in config.get("always_include", []):
        filter_ = f"doi:https://doi.org/{ref.lower()}" if ref.startswith("10.") else f"openalex:{ref}"
        for work in fetch_all(filter_):
            by_id.setdefault(work["id"], {**work, "members": []})
    works = list(by_id.values())
    for work in works:
        if len(work.get("authorships", [])) >= 100:  # the list endpoint stops at 100 authors
            work["authorships"] = full_authorships(work)
            time.sleep(0.2)
    return works


def excluded(work: dict, exclude: list[str]) -> bool:
    keys = {norm(work.get("title")), short_id(work["id"]).lower(), norm_doi(work.get("doi"))}
    return any(
        norm_doi(e).lower() in keys or short_id(str(e)).lower() in keys or norm(str(e)) in keys
        for e in exclude
    )


ARXIV_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf)/|10\.48550/arxiv\.)(\d{4}\.\d{4,5})", re.I)


def arxiv_id(work: dict) -> str:
    """The arXiv id of a work (or of its preprint version), if OpenAlex knows one."""
    urls = [work.get("doi") or ""]
    for loc in work.get("locations") or []:
        urls += [loc.get("landing_page_url") or "", loc.get("pdf_url") or ""]
    for url in urls:
        m = ARXIV_RE.search(url)
        if m:
            return m.group(1)
    return ""


def on_huggingface(arxiv: str) -> bool | None:
    """True/False if huggingface.co/papers/<arxiv> exists; None if the lookup failed."""
    try:
        with urllib.request.urlopen(f"https://huggingface.co/api/papers/{arxiv}", timeout=30):
            return True
    except urllib.error.HTTPError as err:
        return False if err.code == 404 else None
    except Exception:
        return None


def clean(text: str) -> str:
    """Make text safe inside a BibTeX {...} value."""
    return re.sub(r"[{}\\]", "", text or "").strip()


def matches(person: dict, author: dict) -> bool:
    """Whether an OpenAlex author is this member: by OpenAlex id, ORCID or (with OpenAlex ids) name."""
    ids, orcid = set(person.get("openalex") or []), str(person.get("orcid") or "")
    names = {norm(person["name"]), *(norm(n) for n in person.get("aliases") or [])}
    return bool(
        short_id(author.get("id") or "") in ids
        or (orcid and (author.get("orcid") or "").endswith(orcid))
        or (ids and norm(author["display_name"]) in names)  # name match only for people with OpenAlex ids
    )


def person_ids(work: dict, people: list[dict]) -> list[str]:
    """Ids (from data/people.yml) of the DFM members who wrote a work, matched by OpenAlex id, ORCID or name."""
    found = []
    for p in people:
        if p.get("left") and str(work.get("publication_date") or "") > str(p["left"]):
            continue
        if any(matches(p, a["author"]) for a in work.get("authorships", [])):
            found.append(p["id"])
    return found


def to_entry(work: dict, member_ids: set[str], member_names: set[str], people: list[dict]) -> dict:
    authorships = work.get("authorships", [])
    loc = work.get("primary_location") or {}
    source = clean(((loc.get("source") or {}).get("display_name")) or "")
    source = re.sub(r"^arXiv\b.*", "arXiv", source)  # drop "(Cornell University)"
    source = re.sub(r"^SocArXiv\b.*", "SocArXiv", source)  # drop "(OSF Preprints)"
    doi = norm_doi(work.get("doi"))
    if not source:  # preprint servers that OpenAlex lists without a venue
        source = (
            "SocArXiv" if doi.startswith("10.31235/")
            else "arXiv" if doi.startswith("10.48550/")
            else "ACL Anthology" if doi.startswith("10.18653/")
            else ""
        )
    kind = {"article": "article", "proceedings-article": "inproceedings"}.get(work.get("type"), "misc")
    entry = {
        "ID": short_id(work["id"]),
        "ENTRYTYPE": kind,
        "title": clean(work.get("title")),
        "author": " and ".join(clean(a["author"]["display_name"]) for a in authorships),
        "oa_type": work.get("type") or "",
        "arxiv": arxiv_id(work),
        "year": str(work.get("publication_year") or ""),
        "date": work.get("publication_date") or "",
        "url": clean(link(work)),
        "dfm_people": " and ".join(person_ids(work, people)),
        "dfm_members": " and ".join(
            clean(a["author"]["display_name"])
            for a in authorships
            if short_id(a["author"].get("id") or "") in member_ids
            or norm(a["author"]["display_name"]) in member_names
            or any(matches(p, a["author"]) for p in people)
        ),
    }
    if source:
        entry["booktitle" if kind == "inproceedings" else "journal"] = source
    if work.get("doi"):
        entry["doi"] = norm_doi(work["doi"])
    return entry


def link(work: dict) -> str:
    if work.get("doi"):
        return work["doi"]
    for loc in (work.get("best_oa_location"), work.get("primary_location")):
        if loc and (loc.get("landing_page_url") or loc.get("pdf_url")):
            return loc.get("landing_page_url") or loc["pdf_url"]
    return work["id"]


def write_bib(entries: list[dict], updated: str, path: Path | None = None) -> None:
    db = BibDatabase()
    db.entries = entries
    db.comments = [f"last_updated = {{{updated}}}"]
    writer = BibTexWriter()
    writer.indent = "  "
    (path or BIB).write_text(bibtexparser.dumps(db, writer))


def read_bib(path: Path | None = None) -> tuple[list[dict], str]:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True, ignore_nonstandard_types=False)
    db = bibtexparser.loads((path or BIB).read_text(), parser)
    updated = ""
    for comment in db.comments:
        m = re.search(r"last_updated\s*=\s*\{([^}]*)\}", comment)
        if m:
            updated = m.group(1)
    return db.entries, updated


def excluded(entry: dict, exclude: list[str]) -> bool:
    keys = {norm(entry.get("title")), entry["ID"].lower(), norm_doi(entry.get("doi"))}
    return any(
        norm_doi(e) in keys or short_id(e).lower() in keys or norm(e) in keys for e in exclude
    )


def authors_line(entry: dict, by_id: dict[str, dict]) -> str:
    members = set((entry.get("dfm_members") or "").split(" and "))
    for i in (entry.get("dfm_people") or "").split(" and "):  # members matched by ORCID/alias too
        if i in by_id:
            p = by_id[i]
            members |= {p["name"], *(p.get("aliases") or [])}
    names = [n for n in entry.get("author", "").split(" and ") if n]
    flagged = [(n, n in members) for n in names]
    if len(flagged) > 12:  # keep long author lists short, but never hide a DFM member
        flagged = [f for i, f in enumerate(flagged) if i < 10 or i == len(flagged) - 1 or f[1]]
        flagged.insert(10, ("…", False))
    return ", ".join(
        f"<strong>{html.escape(n)}</strong>" if is_member else html.escape(n) for n, is_member in flagged
    )


MAX_PORTRAITS = 4  # more members than this collapse into a "+N" badge


def portraits(e: dict, by_id: dict[str, dict]) -> str:
    people = [by_id[i] for i in (e.get("dfm_people") or "").split(" and ") if i in by_id]
    shown, rest = people[:MAX_PORTRAITS], people[MAX_PORTRAITS:]
    imgs = "".join(
        f'<img class="pub__person" src="./_static/people/{p["image"]}" alt="{html.escape(p["name"])}" '
        f'title="{html.escape(p["name"])}" loading="lazy">'
        for p in shown
    )
    if rest:
        names = html.escape(", ".join(p["name"] for p in rest))
        imgs += f'<span class="pub__person pub__person--more" title="{names}">+{len(rest)}</span>'
    return f'<span class="pub__people">{imgs}</span>' if imgs else ""


def item(e: dict, by_id: dict[str, dict]) -> str:
    url = e.get("url") or f"https://doi.org/{e['doi']}"
    venue = e.get("journal") or e.get("booktitle") or ""
    classes = "pub__venue" + (" pub__venue--preprint" if is_preprint(e) else "")
    return (
        f'<li class="pub" data-peer="{int(not is_preprint(e))}" data-astar="{int(is_a_star(e))}">'
        '<div class="pub__body">'
        f'<a class="pub__title" href="{html.escape(url)}">{html.escape(e["title"])}</a>'
        f'<p class="pub__authors">{authors_line(e, by_id)}</p>'
        + (
            '<p class="pub__meta">'
            + (f'<span class="{classes}">{html.escape(venue)}</span>' if venue else "")
            + (
                f'<a class="pub__link" href="https://huggingface.co/papers/{e["huggingface"]}">Hugging Face ↗</a>'
                if e.get("huggingface")
                else ""
            )
            + "</p>"
            if venue or e.get("huggingface")
            else ""
        )
        + "</div>"
        + portraits(e, by_id)
        + "</li>"
    )


def stat(number: int, label: str, tip: str, key: str, click: str) -> str:
    return (
        f'<div class="pub-stat" data-filter="{key}">'
        f'<button type="button" class="pub-stat__btn" title="{click}"><strong>{number}</strong>'
        f"<span>{html.escape(label)}</span></button>"
        '<span class="info-tip">'
        f'<button type="button" class="info-tip__button" aria-label="{html.escape(label)}">i</button>'
        f'<span class="info-tip__bubble" role="tooltip">{html.escape(tip)}</span>'
        "</span></div>"
    )


# Click a headline number to filter the list (state lives in the URL hash, e.g. #show=peer).
FILTER_SCRIPT = """<script>
(function () {
  var stats = document.querySelector(".pub-stats");
  if (!stats) return;
  var items = [].slice.call(document.querySelectorAll(".pub"));
  var lists = [].slice.call(document.querySelectorAll(".pub-list"));
  function apply(mode) {
    items.forEach(function (li) {
      li.hidden = (mode === "peer" && li.getAttribute("data-peer") !== "1") ||
                  (mode === "astar" && li.getAttribute("data-astar") !== "1");
    });
    lists.forEach(function (ul) {
      var empty = !ul.querySelector(".pub:not([hidden])");
      ul.hidden = empty;
      var h = ul.previousElementSibling;
      while (h && h.tagName !== "H2") h = h.previousElementSibling;
      if (h) {
        h.hidden = empty;
        var link = document.querySelector('.md-sidebar--secondary a[href="#' + h.id + '"]');
        if (link && link.parentElement) link.parentElement.hidden = empty;
      }
    });
    [].forEach.call(stats.querySelectorAll(".pub-stat"), function (s) {
      var on = s.getAttribute("data-filter") === mode;
      s.classList.toggle("is-active", on && mode !== "all");
      s.querySelector(".pub-stat__btn").setAttribute("aria-pressed", on ? "true" : "false");
    });
    try { history.replaceState(null, "", mode === "all" ? location.pathname + location.search : "#show=" + mode); } catch (e) {}
  }
  stats.addEventListener("click", function (e) {
    var b = e.target.closest(".pub-stat__btn");
    if (!b) return;
    var mode = b.parentElement.getAttribute("data-filter");
    var current = (stats.querySelector(".pub-stat.is-active") || {}).dataset;
    apply(current && current.filter === mode ? "all" : mode);
  });
  var m = /^#show=(peer|astar)$/.exec(location.hash);
  if (m) apply(m[1]);
})();
</script>
"""


def render(entries: list[dict], lang: str, since: str, updated: str, people: list[dict]) -> str:
    by_id = {p["id"]: p for p in people}
    t = TEXT[lang]
    n_peer = sum(not is_preprint(e) for e in entries)
    icon = "i"  # drawn as a circle with CSS, see extra.css
    out = [
        f"# {t['title']}\n",
        f'<p class="pub-updated">{t["updated"]}: {updated} '
        '<span class="info-tip">'
        f'<button type="button" class="info-tip__button" aria-label="{t["about"]}">{icon}</button>'
        f'<span class="info-tip__bubble" role="tooltip">{t["info"].format(since=since)}</span>'
        "</span></p>\n",
        '<div class="pub-stats">'
        + stat(len(entries), t["stat_papers"].format(since_long=long_date(since, lang)), t["tip_papers"].format(since_long=long_date(since, lang)), "all", t["click"])
        + stat(n_peer, t["stat_peer"], t["tip_peer"], "peer", t["click"])
        + stat(sum(is_a_star(e) for e in entries), t["stat_astar"], t["tip_astar"], "astar", t["click"])
        + "</div>\n",
    ]
    groups: dict[str, list[dict]] = {}
    for e in entries:
        groups.setdefault(e["year"], []).append(e)
    for n, (year, items) in enumerate(groups.items()):
        out.append(f"\n## {year}\n")
        out.append('<ul class="pub-list">\n' + "\n".join(item(e, by_id) for e in items) + "\n</ul>\n")
    out.append(FILTER_SCRIPT)
    return "\n".join(out) + "\n"


S2_API = "https://api.semanticscholar.org/graph/v1/paper/"
S2_AUTHOR = "https://api.semanticscholar.org/graph/v1/author"
BUDGET = 600  # seconds each of the ORCID and Semantic Scholar steps may take
ORCID_TYPES = {"journal-article", "conference-paper", "preprint", "working-paper", "report", "book-chapter", "book"}


def is_volume(title: str) -> bool:
    """Whole proceedings volumes (front matter) are not papers."""
    return bool(re.match(r"^\s*proceedings of\b", title, re.I))


def http_json(url: str, headers: dict | None = None, retries: int = 4, body: dict | None = None):
    for attempt in range(retries):
        try:
            payload = json.dumps(body).encode() if body is not None else None
            req = urllib.request.Request(
                url, data=payload, headers={"Accept": "application/json", "Content-Type": "application/json", **(headers or {})}
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            time.sleep(3 * (attempt + 1))  # 429 and friends: back off
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def orcid_works(orcid: str) -> list[dict]:
    """A person's works as they list them on their ORCID record."""
    data = http_json(f"https://pub.orcid.org/v3.0/{orcid}/works") or {}
    works = []
    for group in data.get("group", []):
        summary = (group.get("work-summary") or [{}])[0]
        ids = {i["external-id-type"]: i["external-id-value"] for i in group.get("external-ids", {}).get("external-id", [])}
        year = ((summary.get("publication-date") or {}).get("year") or {}).get("value")
        works.append(
            {
                "title": ((summary.get("title") or {}).get("title") or {}).get("value") or "",
                "year": int(year) if year else 0,
                "type": summary.get("type") or "",
                "doi": norm_doi(ids.get("doi")) if ids.get("doi") else "",
                "arxiv": re.sub(r"^arxiv:", "", ids.get("arxiv", ""), flags=re.I),
                "journal": summary.get("journal-title", {}) and (summary["journal-title"] or {}).get("value") or "",
            }
        )
    return works


def semantic_scholar(doi: str, arxiv: str) -> dict | None:
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    ref = f"DOI:{doi}" if doi else f"ARXIV:{arxiv}"
    fields = "title,year,publicationDate,venue,externalIds,authors.name"
    data = http_json(f"{S2_API}{urllib.parse.quote(ref, safe=':')}?fields={fields}", {"x-api-key": key} if key else None)
    time.sleep(0.3 if key else 1.2)
    return data


def discover(config: dict, known: list[dict]) -> list[dict]:
    """Papers listed on members' ORCID records that OpenAlex did not give us, filled in from Semantic Scholar."""
    since = str(config["since"])
    have_title = {norm(e.get("title")) for e in known}
    have_doi = {norm_doi(e.get("doi")) for e in known if e.get("doi")}
    have_arxiv = {e["arxiv"] for e in known if e.get("arxiv")}
    people = config["people"]
    found: dict[str, dict] = {}
    for p in people:
        if not p.get("orcid"):
            continue
        for w in orcid_works(str(p["orcid"])):
            if w["type"] not in ORCID_TYPES or w["year"] < int(since[:4]) or not w["title"] or is_volume(w["title"]):
                continue
            if p.get("left") and w["year"] > int(str(p["left"])[:4]):
                continue
            if w["type"] in (p.get("exclude_types") or []):
                continue
            if (w["doi"] and w["doi"] in have_doi) or (w["arxiv"] and w["arxiv"] in have_arxiv) or norm(w["title"]) in have_title:
                continue
            item = found.setdefault(w["doi"] or w["arxiv"] or norm(w["title"]), {**w, "owners": []})
            item["owners"].append(p["id"])
    entries = []
    started = time.time()
    for key, w in found.items():
        if time.time() - started > BUDGET:  # keep the run bounded; the rest is picked up tomorrow
            break
        s2 = semantic_scholar(w["doi"], w["arxiv"]) if (w["doi"] or w["arxiv"]) else None
        title = (s2 or {}).get("title") or w["title"]
        date = (s2 or {}).get("publicationDate") or f"{w['year']}-01-01"
        if date < since:
            continue
        names = [a["name"] for a in (s2 or {}).get("authors", []) if a.get("name")]
        venue = clean((s2 or {}).get("venue") or w["journal"])
        if not venue and w["arxiv"]:
            venue = "arXiv"
        works = {"authorships": [{"author": {"display_name": n, "id": None}} for n in names]}
        owners = list(dict.fromkeys(w["owners"] + person_ids(works, people)))
        by_id = {p["id"]: p for p in people}
        e = {
            "ID": "ext-" + re.sub(r"[^a-z0-9]+", "-", norm(title))[:40].strip("-"),
            "ENTRYTYPE": "inproceedings" if w["type"] == "conference-paper" else "article",
            "title": clean(title),
            "author": " and ".join(clean(n) for n in names) or " and ".join(by_id[i]["name"] for i in owners),
            "oa_type": "preprint" if w["type"] == "preprint" or venue.lower() == "arxiv" else w["type"],
            "arxiv": w["arxiv"] or ((s2 or {}).get("externalIds") or {}).get("ArXiv", ""),
            "year": date[:4],
            "date": date,
            "url": f"https://doi.org/{w['doi']}" if w["doi"] else f"https://arxiv.org/abs/{w['arxiv']}",
            "dfm_people": " and ".join(owners),
            "dfm_members": " and ".join(by_id[i]["name"] for i in owners),
        }
        if venue:
            e["booktitle" if e["ENTRYTYPE"] == "inproceedings" else "journal"] = venue
        if w["doi"]:
            e["doi"] = w["doi"]
        entries.append(e)
    return entries


def s2_headers() -> dict | None:
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    return {"x-api-key": key} if key else None


def s2_author_ids(people: list[dict], known: list[dict]) -> dict[str, set[str]]:
    """Semantic Scholar author ids per member, learned from papers we already know are theirs: on each such
    paper the author whose name matches the member is their profile (Semantic Scholar often splits one person
    into several profiles, so there can be more than one). Ids can also be given in people.yml."""
    by_id = {p["id"]: p for p in people}
    names = {
        p["id"]: {norm(p["name"]), *(norm(n) for n in p.get("aliases") or [])} for p in people
    }
    ids: dict[str, set[str]] = {p["id"]: set(map(str, p.get("semanticscholar") or [])) if isinstance(p.get("semanticscholar"), list)
                                else ({str(p["semanticscholar"])} if p.get("semanticscholar") else set()) for p in people}
    papers = []  # (reference for Semantic Scholar, members on it)
    for e in known:
        owners = [i for i in (e.get("dfm_people") or "").split(" and ") if i in by_id]
        if not owners:
            continue
        ref = f"DOI:{e['doi']}" if e.get("doi") else (f"ARXIV:{e['arxiv']}" if e.get("arxiv") else "")
        if ref:
            papers.append((ref, owners))
    seen: dict[tuple[str, str], int] = {}
    started = time.time()
    for i in range(0, len(papers), 200):
        if time.time() - started > BUDGET:
            break
        chunk = papers[i : i + 200]
        data = http_json(
            f"{S2_API}batch?fields=authors.authorId,authors.name",
            s2_headers(),
            body={"ids": [ref for ref, _ in chunk]},
        )
        time.sleep(0.3 if s2_headers() else 1.2)
        for (ref, owners), paper in zip(chunk, data or []):
            for author in (paper or {}).get("authors", []):
                for o in owners:
                    if author.get("authorId") and norm(author.get("name")) in names[o]:
                        seen[(o, author["authorId"])] = seen.get((o, author["authorId"]), 0) + 1
    for (o, author), n in seen.items():
        if n >= 2:  # a single match could be a namesake; two known papers make the profile theirs
            ids[o].add(author)
    return ids


def s2_discover(config: dict, known: list[dict]) -> list[dict]:
    """Recent papers on members' verified Semantic Scholar profiles that the other sources lack."""
    since = str(config["since"])
    have_title = {norm(e.get("title")) for e in known}
    have_doi = {norm_doi(e.get("doi")) for e in known if e.get("doi")}
    have_arxiv = {e["arxiv"] for e in known if e.get("arxiv")}
    people = config["people"]
    by_id = {p["id"]: p for p in people}
    found: dict[str, dict] = {}
    started = time.time()
    author_ids = s2_author_ids(people, known)
    for p in people:
        if time.time() - started > BUDGET:
            break
        fields = "title,year,publicationDate,venue,externalIds,authors.name,publicationTypes"
        papers: list[dict] = []
        for author in sorted(author_ids.get(p["id"], ())):
            data = http_json(f"{S2_AUTHOR}/{author}/papers?fields={fields}&limit=1000", s2_headers())
            time.sleep(0.3 if s2_headers() else 1.2)
            papers += (data or {}).get("data", [])
        for w in papers:
            ext = w.get("externalIds") or {}
            doi, arxiv = norm_doi(ext.get("DOI")) if ext.get("DOI") else "", ext.get("ArXiv") or ""
            date = w.get("publicationDate") or (f"{w['year']}-01-01" if w.get("year") else "")
            if not w.get("title") or not date or date < since or is_volume(w["title"]):
                continue
            if p.get("left") and date > str(p["left"]):
                continue
            if (doi and doi in have_doi) or (arxiv and arxiv in have_arxiv) or norm(w["title"]) in have_title:
                continue
            item = found.setdefault(doi or arxiv or norm(w["title"]), {"w": w, "doi": doi, "arxiv": arxiv, "date": date, "owners": []})
            item["owners"].append(p["id"])
    entries = []
    for item in found.values():
        w = item["w"]
        names = [a["name"] for a in w.get("authors", []) if a.get("name")]
        venue = clean(w.get("venue") or "")
        if not venue and item["arxiv"]:
            venue = "arXiv"
        works = {"authorships": [{"author": {"display_name": n, "id": None}} for n in names]}
        owners = list(dict.fromkeys(item["owners"] + person_ids(works, people)))
        kinds = w.get("publicationTypes") or []
        e = {
            "ID": "s2-" + re.sub(r"[^a-z0-9]+", "-", norm(w["title"]))[:40].strip("-"),
            "ENTRYTYPE": "inproceedings" if "Conference" in kinds else "article",
            "title": clean(w["title"]),
            "author": " and ".join(clean(n) for n in names),
            "oa_type": "preprint" if venue.lower() in ("arxiv", "arxiv.org") else ("conference-paper" if "Conference" in kinds else "article"),
            "arxiv": item["arxiv"],
            "year": item["date"][:4],
            "date": item["date"],
            "url": f"https://doi.org/{item['doi']}" if item["doi"] else f"https://arxiv.org/abs/{item['arxiv']}",
            "dfm_people": " and ".join(owners),
            "dfm_members": " and ".join(by_id[i]["name"] for i in owners),
        }
        if not (item["doi"] or item["arxiv"]):
            e["url"] = f"https://www.semanticscholar.org/paper/{w['paperId']}" if w.get("paperId") else ""
        if venue:
            e["booktitle" if e["ENTRYTYPE"] == "inproceedings" else "journal"] = venue
        if item["doi"]:
            e["doi"] = item["doi"]
        entries.append(e)
    return entries


def manual_entries(config: dict, people: list[dict]) -> list[dict]:
    """Hand-written papers from publications/overrides.bib (for papers the other sources miss)."""
    if not OVERRIDES.exists():
        return []
    by_id = {p["id"]: p for p in people}
    out = []
    for e in read_bib(OVERRIDES)[0]:
        names = [n.strip() for n in (e.get("author") or "").split(" and ") if n.strip()]
        works = {"authorships": [{"author": {"display_name": n, "id": None}} for n in names]}
        matched = person_ids(works, people)
        arxiv = e.get("arxiv", "")
        e.setdefault("date", f"{e.get('year', '')}-01-01")
        e["year"] = e["date"][:4]
        e["oa_type"] = e.get("oa_type") or "conference-paper"
        e["dfm_people"] = " and ".join(matched)
        e["dfm_members"] = " and ".join(by_id[i]["name"] for i in matched)
        if arxiv and not e.get("huggingface") and on_huggingface(arxiv):
            e["huggingface"] = arxiv
        out.append(e)
    return out


def main() -> int:
    config = yaml.safe_load(CONFIG.read_text())
    A_STAR[:] = [re.compile(p, re.I) for p in config.get("a_star_venues") or []]
    A_STAR_NOT[:] = [re.compile(p, re.I) for p in config.get("a_star_exclude_titles") or []]
    people = yaml.safe_load(PEOPLE.read_text())["people"]
    config["authors"] = [p for p in people if p.get("openalex")]
    config["people"] = people
    try:
        if os.environ.get("PUBLICATIONS_RENDER_ONLY"):  # re-render from the saved .bib files, no network
            raise RuntimeError("render only")
        works = fetch(config)
        member_ids = {i for p in config["authors"] for i in p["openalex"]}
        member_names = {norm(p["name"]) for p in config["authors"]}
        people = config["people"]
        entries = [to_entry(w, member_ids, member_names, people) for w in works]
        previous = {e["arxiv"]: e.get("huggingface") for e in read_bib()[0] if e.get("arxiv")} if BIB.exists() else {}
        for e in entries:
            if not e["arxiv"]:
                continue
            found = on_huggingface(e["arxiv"])
            if found is None:  # lookup failed: keep what we knew
                found = bool(previous.get(e["arxiv"]))
            if found:
                e["huggingface"] = e["arxiv"]
            time.sleep(0.1)
        write_bib(entries, time.strftime("%Y-%m-%d", time.gmtime()))
        today = time.strftime("%Y-%m-%d", time.gmtime())
        orcid_entries: list[dict] = []
        try:  # extra sources; a failure here never loses the OpenAlex list
            orcid_entries = discover(config, entries)
            write_bib(orcid_entries, today, ORCID_BIB)
        except Exception as err:
            print(f"ORCID step failed ({err}); keeping {ORCID_BIB.name}", file=sys.stderr)
        try:
            write_bib(s2_discover(config, entries + orcid_entries), today, S2_BIB)
        except Exception as err:
            print(f"Semantic Scholar step failed ({err}); keeping {S2_BIB.name}", file=sys.stderr)
    except Exception as err:  # keep the last good .bib
        if not os.environ.get("PUBLICATIONS_RENDER_ONLY"):
            print(f"Fetch failed ({err}); keeping existing {BIB.name}", file=sys.stderr)
        if not BIB.exists():
            return 1

    entries, updated = read_bib()
    for e in entries:
        e["source"] = "openalex"
    for path, source in ((S2_BIB, "semanticscholar"), (ORCID_BIB, "orcid")):
        if path.exists():
            entries += [{**e, "source": source} for e in read_bib(path)[0]]
    entries += [{**e, "source": "overrides"} for e in manual_entries(config, config["people"])]
    for e in entries:
        for field in ("journal", "booktitle"):
            if e.get(field):
                e[field] = tidy_venue(e[field])
    exclude = [str(e) for e in config.get("exclude") or []]
    overrides = [str(e) for e in config.get("always_peer_reviewed") or []]
    for e in entries:
        e["peer_override"] = excluded(e, overrides) if overrides else False

    # When a preprint and its published version are both listed, keep the published one.
    best: dict[str, dict] = {}
    all_titles = sorted({norm(e.get("title")) for e in entries if e.get("title")}, key=len, reverse=True)

    def canonical(title: str) -> str:
        """A shortened title ("Follow the Path") is the same paper as its full title ("Follow the Path: ...")."""
        if len(title) >= 7:
            for longer in all_titles:  # only at a word boundary ("include" is not a prefix of "including")
                if longer != title and longer.startswith(title + " "):
                    return longer
        return title

    for e in entries:
        title = canonical(norm(e.get("title")))
        if not title or excluded(e, exclude):
            continue
        if title not in best or priority(e) < priority(best[title]):
            best[title] = e
    for e in entries:  # a published version inherits the preprint's Hugging Face page
        twin = best.get(canonical(norm(e.get("title"))))
        if twin is not None and e.get("huggingface") and not twin.get("huggingface"):
            twin["huggingface"] = e["huggingface"]
    kept = sorted(best.values(), key=lambda e: e.get("date", ""), reverse=True)

    write_bib([{k: v for k, v in e.items() if k != "peer_override"} for e in kept], updated, COMBINED)
    for lang in ("en", "da"):
        path = ROOT / lang / "docs" / "publications.md"
        path.write_text(render(kept, lang, str(config["since"]), updated, config["people"]))
    print(f"Wrote {len(kept)} publications")
    return 0


if __name__ == "__main__":
    sys.exit(main())
