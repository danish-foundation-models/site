"""Generate the People pages and the news author lists from data/people.yml.

Writes en/docs/people.md, da/docs/people.md, en/docs/news/.authors.yml and
da/docs/news/.authors.yml. Do not edit those files by hand; edit data/people.yml.
"""

import html
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PEOPLE = ROOT / "data" / "people.yml"

# (field in people.yml, label, URL template); icons are drawn in extra.css. Shown in this order.
SOCIALS = [
    ("website", "Website", "{}"),
    ("github", "GitHub", "https://github.com/{}"),
    ("huggingface", "Hugging Face", "https://huggingface.co/{}"),
    ("orcid", "ORCID", "https://orcid.org/{}"),
    ("linkedin", "LinkedIn", "{}"),
    ("bluesky", "Bluesky", "https://bsky.app/profile/{}"),
]

TEXT = {
    "en": {"title": "People", "portrait": "Portrait", "filtered": "Filtered by", "clear": "Clear filter",
           "one": "person", "many": "people", "click": "Click to filter", "alumni": "Alumni"},
    "da": {"title": "Mennesker", "portrait": "Portræt", "filtered": "Filtreret på", "clear": "Ryd filter",
           "one": "person", "many": "personer", "click": "Klik for at filtrere", "alumni": "Tidligere medlemmer"},
}

# Click a tag to filter the cards by it (state lives in the URL hash, e.g. #tag=Evaluation).
SCRIPT = """<script>
(function () {
  var grid = document.querySelector(".people-page");
  if (!grid) return;
  var alumniHead = grid.querySelector(".people-alumni");
  var bar = document.querySelector(".people-filter");
  var label = bar.querySelector(".people-filter__tag");
  var count = bar.querySelector(".people-filter__count");
  var cards = [].slice.call(grid.querySelectorAll(".person-card"));
  var UNITS = %(units)s;
  function apply(tag, scroll) {
    var n = 0;
    cards.forEach(function (c) {
      var show = !tag || c.getAttribute("data-tags").split("|").indexOf(tag) !== -1;
      c.hidden = !show;
      if (show) n++;
    });
    if (alumniHead) alumniHead.hidden = !grid.querySelector(".people-alumni ~ .people-grid .person-card:not([hidden])");
    [].forEach.call(grid.querySelectorAll("[data-tag]"), function (b) {
      b.classList.toggle("is-active", !!tag && b.getAttribute("data-tag") === tag);
    });
    bar.classList.toggle("is-active", !!tag);
    label.textContent = tag || "";
    count.textContent = tag ? n + " " + (n === 1 ? UNITS[0] : UNITS[1]) : "";
    try { history.replaceState(null, "", tag ? "#tag=" + encodeURIComponent(tag) : location.pathname + location.search); } catch (e) {}
    if (tag && scroll) bar.scrollIntoView({ behavior: "smooth", block: "center" });
  }
  grid.addEventListener("click", function (e) {
    var b = e.target.closest("[data-tag]");
    if (!b) return;
    var t = b.getAttribute("data-tag");
    apply(label.textContent === t ? "" : t, true);
  });
  bar.querySelector(".people-filter__clear").addEventListener("click", function () { apply("", false); });
  var m = /^#tag=(.+)$/.exec(location.hash);
  if (m) { try { apply(decodeURIComponent(m[1]), false); } catch (e) {} }
})();
</script>
"""


def load() -> list[dict]:
    people = yaml.safe_load(PEOPLE.read_text())["people"]
    return sorted(people, key=lambda p: (p["tier"], p["name"]))  # by tier, then by name


def card(p: dict, lang: str) -> str:
    t = TEXT[lang]
    tags = "".join(
        f'<button type="button" class="tag" data-tag="{html.escape(x)}" title="{t["click"]}">{html.escape(x)}</button>'
        for x in p.get("tags", {}).get(lang, [])
    )
    items = []
    for field, label, url in SOCIALS:
        if p.get(field):
            href = html.escape(url.format(p[field]))
            items.append(f'<a class="social social--{field}" href="{href}" aria-label="{label}" title="{label}"></a>')
    link_row = f'<p class="person-links">{"".join(items)}</p>\n' if items else ""
    portrait = ""
    if p.get("portrait", {}).get(lang):
        portrait = f'<p class="person-portrait"><a href="{html.escape(p["portrait"][lang])}">{t["portrait"]} →</a></p>\n'
    position = f'<p class="position">{html.escape(p["position"][lang])}</p>\n' if p.get("position") else ""
    tag_row = f'<div class="tags">{tags}</div>\n' if tags else ""
    data_tags = html.escape("|".join([*p.get("tags", {}).get(lang, []), p["affiliation"][lang]]))
    affiliation = html.escape(p["affiliation"][lang])
    return (
        f'<div class="person-card" data-tags="{data_tags}">\n'
        f'<img src="./_static/people/{p["image"]}" alt="{html.escape(p["name"])}">\n'
        f'<h3>{html.escape(p["name"])}</h3>\n'
        + link_row
        + position
        + f'<p class="affiliation"><button type="button" class="affiliation-filter" data-tag="{affiliation}" '
        + f'title="{t["click"]}">{affiliation}</button></p>\n'
        + tag_row
        + portrait
        + "</div>\n"
    )


def main() -> None:
    people = load()
    for lang in ("en", "da"):
        t = TEXT[lang]
        shown = [p for p in people if p.get("show", True) is not False]
        body = "".join(card(p, lang) for p in shown if not p.get("alumni"))
        alumni = "".join(card(p, lang) for p in shown if p.get("alumni"))
        alumni_html = (
            f'<h2 class="people-alumni">{t["alumni"]}</h2>\n<div class="people-grid">\n{alumni}</div>\n' if alumni else ""
        )
        bar = (
            f'<div class="people-filter">'
            f'<p class="people-filter__active">{t["filtered"]} <strong class="people-filter__tag"></strong> '
            f'<span class="people-filter__count"></span> '
            f'<button type="button" class="people-filter__clear">{t["clear"]} ✕</button></p></div>\n'
        )
        script = SCRIPT % {"units": json.dumps([t["one"], t["many"]])}
        (ROOT / lang / "docs" / "people.md").write_text(
            f'# {t["title"]}\n\n{bar}\n<div class="people-page">\n<div class="people-grid">\n{body}</div>\n{alumni_html}</div>\n\n{script}'
        )
        authors = {}
        for p in people:
            if p.get("news_author", True) is False:
                continue
            entry = {
                "name": p["name"],
                "description": ", ".join(x for x in (p.get("position", {}).get(lang), p["affiliation"][lang]) if x),
                "avatar": f'_static/people/{p["image"]}',
            }
            if p.get("url"):
                entry["url"] = p["url"]
            authors[p["id"]] = entry
        (ROOT / lang / "docs" / "news" / ".authors.yml").write_text(
            "# Generated by scripts/build_people.py from data/people.yml. Do not edit by hand.\n"
            + yaml.safe_dump({"authors": authors}, allow_unicode=True, sort_keys=False)
        )
    print(f"Wrote {len(people)} people")


if __name__ == "__main__":
    main()
