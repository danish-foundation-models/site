# Danish Foundation Models — Site

This repository contains the source for [foundationmodels.dk](https://foundationmodels.dk), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)

If you don't have `uv` installed, running `make install` will install it automatically.

## Getting started

Install dependencies:

```bash
make install
```

Serve locally with live reload:

```bash
make serve
```

The site will be available at `http://127.0.0.1:8000`.

## Build

Build the static site into `site/`:

```bash
make build
```

## Structure

```
docs/           # Site content (Markdown)
  index.md      # Front page
  news/         # News/blog posts
  _static/      # Images, CSS, logos
overrides/      # MkDocs theme overrides
mkdocs.yml      # MkDocs configuration
```

## Adding a news post

Create a new Markdown file in `docs/news/posts/` with the following frontmatter:

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

- [MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/)
