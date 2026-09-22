# Danish Foundation Models — Site

This repository contains the source for [foundationmodels.dk](https://foundationmodels.dk), built with [Zensical](https://zensical.org/).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)

If you don't have `uv` installed, running `make install` will install it automatically.

## Getting started

Install dependencies:

```bash
make install
```

Build both languages and serve them at `http://127.0.0.1:8000`:

```bash
make serve
```

Serve a single language with live reload:

```bash
make serve-en
make serve-da
```

Note that `make serve-da` does not show images, as the Danish site shares its assets with the English site through symlinks, which Zensical does not follow. `make build` copies them in.

## Build

Build the static site into `site/`:

```bash
make build
```

## Structure

```
en/docs/            # English site content (Markdown)
  index.md          # Front page
  news/             # News/blog posts
  _static/          # Images, CSS, logos
    home.css/js     # Front page: hero, latest-news banner (read from news/index.html)
    map/            # Collaboration map; edit NODES in dfm-map.js to add or move collaborators
da/docs/            # Danish site content; _static and news/images are symlinks to en/docs
overrides/          # Theme overrides
zensical.toml       # English configuration (built into site/)
zensical.da.toml    # Danish configuration (built into site/da/)
```

The two languages are built as separate projects and linked through the language selector (`extra.alternate`).

## Adding a news post

Create a new Markdown file in both `en/docs/news/posts/` and `da/docs/news/posts/` with the following frontmatter:

```markdown
---
draft: false
date: YYYY-MM-DD
tags:
  - Model Release   # or: Paper, News, Behind the Scenes
---

# Post title

Intro paragraph (shown in the post listing).

<!-- more -->

Full post content here.
```

## References

- [Zensical documentation](https://zensical.org/docs/)
- [Zensical blog setup](https://zensical.org/docs/setup/blog/)
- [Zensical language setup](https://zensical.org/docs/setup/language/)
