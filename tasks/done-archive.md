<!-- reference — read only when you need the history of a shipped item -->
# Done archive — completed work items

Closed items moved out of the root `tasks.md` on 2026-08-10, following the same
convention as the partle and kart-medulla repos. Nothing here is actionable: the root
board carries only live work, while the reasoning behind finished things stays findable.

The board is `tasks.md` at the repo root — the only task board in this repo.

## Closed items pulled off the board

- [x] Add Open Graph meta tags for social sharing — done 2026-08-05 (see Done section).

## Done
- [2026-08-05] **Add OpenGraph + Twitter Card meta tags** — `overrides/main.html` emits `og:`/`twitter:` tags on every page; per-page `description`/`image`/`og_title` come from YAML front matter, with `images/kart/full-kart.jpg` as the default image. Links shared to LinkedIn/X/etc. now render a chosen image and blurb instead of a bare title-only card. Verified live on rubenayla.xyz.
- [2026-04-06] **Update Partle project page** — rewrote with current stack, real numbers, MCP, SSR, scraping details
- [2026-04-06] **Update mkdocs.yml site_url** — changed to rubenayla.xyz
