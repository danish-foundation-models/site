"""Build the publications pages from OpenAlex via a BibTeX file.

1. Fetch works for each DFM member (publications/config.yml) and write them to
   en/docs/publications.bib. If the fetch fails, the existing .bib is kept.
2. Render the citation list from the .bib (applying the exclude list and
   de-duplicating) into en/docs/publications.md and da/docs/publications.md.

Set OPENALEX_API_KEY for a higher rate limit (optional).
"""

import html
import json
import os
import re
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
BIB = ROOT / "en" / "docs" / "publications.bib"
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
            'Generated automatically every day from <a href="https://openalex.org">OpenAlex</a> '
            "and covers papers by our members. "
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
            'Genereres automatisk hver dag fra <a href="https://openalex.org">OpenAlex</a> '
            "og dækker artikler af DFM-medlemmer siden {since}. "
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
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


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


def person_ids(work: dict, people: list[dict]) -> list[str]:
    """Ids (from data/people.yml) of the DFM members who wrote a work, matched by OpenAlex id, ORCID or name."""
    found = []
    for p in people:
        if p.get("left") and str(work.get("publication_date") or "") > str(p["left"]):
            continue
        ids, orcid = set(p.get("openalex") or []), str(p.get("orcid") or "")
        names = {norm(p["name"]), *(norm(n) for n in p.get("aliases") or [])}
        for a in work.get("authorships", []):
            author = a["author"]
            if (
                short_id(author.get("id") or "") in ids
                or (orcid and (author.get("orcid") or "").endswith(orcid))
                or (ids and norm(author["display_name"]) in names)  # name match only for people with OpenAlex ids
            ):
                found.append(p["id"])
                break
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
            if short_id(a["author"].get("id") or "") in member_ids or norm(a["author"]["display_name"]) in member_names
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


def write_bib(entries: list[dict], updated: str) -> None:
    db = BibDatabase()
    db.entries = entries
    db.comments = [f"last_updated = {{{updated}}}"]
    writer = BibTexWriter()
    writer.indent = "  "
    BIB.write_text(bibtexparser.dumps(db, writer))


def read_bib() -> tuple[list[dict], str]:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True, ignore_nonstandard_types=False)
    db = bibtexparser.loads(BIB.read_text(), parser)
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


def authors_line(entry: dict) -> str:
    members = set((entry.get("dfm_members") or "").split(" and "))
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
        f'<p class="pub__authors">{authors_line(e)}</p>'
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


def main() -> int:
    config = yaml.safe_load(CONFIG.read_text())
    A_STAR[:] = [re.compile(p, re.I) for p in config.get("a_star_venues") or []]
    A_STAR_NOT[:] = [re.compile(p, re.I) for p in config.get("a_star_exclude_titles") or []]
    people = yaml.safe_load(PEOPLE.read_text())["people"]
    config["authors"] = [p for p in people if p.get("openalex")]
    config["people"] = people
    try:
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
    except Exception as err:  # keep the last good .bib
        print(f"Fetch failed ({err}); keeping existing {BIB.name}", file=sys.stderr)
        if not BIB.exists():
            return 1

    entries, updated = read_bib()
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
    for e in entries:
        title = norm(e.get("title"))
        if not title or excluded(e, exclude):
            continue
        if title not in best or (is_preprint(e), -date_key(e)) < (is_preprint(best[title]), -date_key(best[title])):
            best[title] = e  # published beats preprint; between equals, the newer wins
    for e in entries:  # a published version inherits the preprint's Hugging Face page
        twin = best.get(norm(e.get("title")))
        if twin is not None and e.get("huggingface") and not twin.get("huggingface"):
            twin["huggingface"] = e["huggingface"]
    kept = sorted(best.values(), key=lambda e: e.get("date", ""), reverse=True)

    for lang in ("en", "da"):
        path = ROOT / lang / "docs" / "publications.md"
        path.write_text(render(kept, lang, str(config["since"]), updated, config["people"]))
    print(f"Wrote {len(kept)} publications")
    return 0


if __name__ == "__main__":
    sys.exit(main())
