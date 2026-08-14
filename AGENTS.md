<!-- read in full — kept under 150 lines -->
# portfolio — Agent Guide

Recruiter-facing portfolio for Rubén Jiménez Mejías — engineering projects, writing (essays), and CV. Static site built with MkDocs Material, hosted on GitHub Pages.

Personal notes / opinionated standards live in a **separate** site: repo `rubenayla/notes` → https://notes.rubenayla.xyz/. The split is intentional. Keep this portfolio's **primary** recruiter surfaces (top nav, hero, page bodies) free of links to notes so the hiring skim stays clean. The one intentional exception is a single unobtrusive **footer** social icon ("Notes", `fontawesome/solid/book` → notes.rubenayla.xyz): subtle enough that skimming recruiters skip it, while engaged engineers who dig into the footer find the depth (a positive signal). Don't add prominent portfolio → notes links beyond that footer icon. Anything personal/scratch/standards belongs in `notes`, not here.

## Quick Reference
- Live: https://rubenayla.xyz/
- Repo: https://github.com/rubenayla/portfolio (renamed from `ruben` 2026-06-07; was `portfolio` before a May 2026 rename to `ruben`, now reverted on the portfolio/notes split)
- Stack: MkDocs Material (Python), deployed via GitHub Pages
- Domain: rubenayla.xyz (Cloudflare DNS)

## Structure
```
docs/
  index.md          — homepage
  about.md          — personal bio, links, CV
  projects/         — one .md per project
  images/           — project images organized by subfolder
  files/            — CV PDFs, downloadable files
mkdocs.yml          — site config, nav, theme
```

## Local Development
Do NOT use `mkdocs serve` — it has path prefix issues. Instead:
```bash
uv run mkdocs build && python3 -m http.server 8005 --directory site
```
Then visit http://localhost:8005/. Kill stale processes with `lsof -ti:8005 | xargs kill -9`.

## Agent Files
- `tasks.md` (repo root) — task board (TODO / In Progress / Done), holding only live (open)
  work. One `tasks.md` per repo, always at the root — there is no `.agents/tasks.md`.
  **Done items do not stay on the board.** When an item closes, move it — with its date and
  closing note, verbatim — to `tasks/done-archive.md`, the only other task file, which holds
  nothing actionable. Exception: a `- [x]` that is a step of a task still open stays on the
  board; only a whole finished task moves. Same convention as the partle and kart-medulla
  repos.
- `.agents/notes.md` — project notes, decisions, context
- `.agents/error-log.md` — mistake log

## Conventions
- No emojis in content (user preference)
- Keep descriptions technical and concise
- Images go in `docs/images/{project-name}/`
- Downloadable files go in `docs/files/`
- Videos in `docs/videos/`, self-hosted as MP4 and embedded with raw `<video>` tags. Hero/loop MP4 = `kart-hero.mp4`. (YouTube embedding is allowed but not required — there is no "demos must go on YouTube" rule.)

## Gotchas
- **Raw HTML `<video src>` / `<iframe src>` relative paths are NOT rewritten by mkdocs** like markdown links are. A page at `/projects/kart/` (directory URL) referencing `../videos/X.mp4` resolves to `/projects/videos/X.mp4` (404). Use `../../videos/X.mp4` to reach `/videos/X.mp4`. Markdown image/link syntax does get rewritten — only raw HTML tags hit this.

## Related repos / sources
- **kart-docs (team repo)**: `/Users/rubenayla/repos/kart-docs` — MkDocs Material, public team technical reference. Same framework as this portfolio. URL: https://um-driverless.github.io/kart-docs/
- **kart LinkedIn campaign source**: `~/ruben-files/videos/kart/linkedin/` (Drive-synced) — canonical source for the weekly LinkedIn posts that feed the portfolio's Build Journey. Each post is a folder under `posts/<YYYY-MM-DD>_<slug>/` containing `post.md` (literal LinkedIn body), `README.md`, `history.md`, and media files. `published.md` is the durable archive of what's gone live. See that folder's own `AGENTS.md` for the full system.
- **kart raw-media pool**: `~/ruben-files/videos/kart/01_main/` — every photo and video the kart project has ever curated lives here with `YYYY-MM-DD_what_it_is.ext` filenames. Canonical metadata is `01_main/INDEX.md` (Reserved / Used / Tagged tables — chosen deliberately over per-file sidecars, see that folder's history). **Always search this pool before asking the user to re-export anything from Google Photos / cloud / phone.** The portfolio's `docs/videos/` is the deployment surface; `01_main/` is upstream. Recipe for matching a clip the user references by Photos screenshot: `ffprobe` duration + resolution against the pool, then `open` the 1–2 likeliest candidates for visual confirmation — never declare a match on metadata alone (`sec7` had the right dimensions and wrong content; see `.agents/error-log.md`).

## Build Journey
- **Single-page scroll**: all posts live in `docs/build-journey/index.md` as sequential `## <title> { #<anchor> }` sections, oldest first. No per-post pages — older split layouts have been removed. Each section has a stable URL via its anchor (e.g. `/build-journey/#motor`).
- **Per-post anatomy inside the index**:
  ```markdown
  ## <Editorial title> { #<anchor-slug> }

  *<YYYY-MM-DD> · [Original on LinkedIn →](<URL from published.md>)*

  <post body — see migration rules below>

  ![alt](../images/build-journey/<YYYY-MM-DD>-<slug>/<file>){ loading=lazy }
  ```
- **Adding a newly-published post** (triggered by step 11 of the LinkedIn campaign's `AGENTS.md` at-publish workflow):
  1. Confirm the post is in the LinkedIn folder's `published.md` (not just `posts/`).
  2. Append a new `## ... { #anchor }` section before the closing `*That's the latest post...*` stanza.
  3. Update the "Jump to:" line at the top to include the new anchor.
  4. Copy referenced images/thumbnails into `docs/images/build-journey/<YYYY-MM-DD>-<slug>/`.
  5. Strip LinkedIn-only cruft from `post.md`: trailing hashtag block, `@Ü Motorsport...` team-tag line, the docs-URL line if it duplicates an inline link.
  6. Restore `**bold**` / `*italic*` markdown that was flattened for LinkedIn (use `README.md` if it documents intended emphasis).
  7. All images get `{ loading=lazy }` — page weight grows with each post.
  8. Local build only; do not commit/push until user reviews (status promotions are user-only).
- **Mini-entries (decided 2026-08-07)**: the page also carries small dated entries for build moments too minor for a LinkedIn post (a part arriving, a quick board fix) — the page is the build log, not only a post mirror. Same `## <title> { #<anchor> }` anatomy, date line with **no LinkedIn link** (that's what marks a mini), one photo + a few sentences, inserted chronologically among the posts, anchor added to "Jump to:". Source of truth is the kart-docs build journey (`~/repos/kart-docs/docs/build-journey/index.md`) — mirror minis both ways so the two pages stay equivalent.
- **Future page split**: when the page gets unwieldy (~30+ posts, or load-time becomes noticeable), split by year — `index.md` becomes the latest, prior years move to `2026.md`, etc. Anchors per post are stable within each page.

## Video assets — validated-only rule
- For kart Story/Build-Journey embeds and YouTube uploads, source candidate videos from LinkedIn `published.md` (`Media used:` lines with `.mp4`) — never from `ls docs/videos/`. The raw repo MP4s are unvetted (some lack audio, some are weak clips); LinkedIn-published = user-validated.
- If no published videos exist yet, say so and wait — do not substitute repo MP4s.
- Exception: `kart-hero.mp4` (silent autoplay loop on the home page) is allowed to stay self-hosted regardless.
- YouTube URLs for kart videos are tracked in `.agents/youtube-urls.md`.
- **Per-video sidecar metadata**: each `docs/videos/<name>.mp4` has a sibling `docs/videos/<name>.md` with frontmatter (date, length, resolution, source, `human_rating` and `ai_rating` on 0.0–1.0, status) and a short prose body. Sidecars are excluded from the rendered site via `exclude_docs: videos/*.md` in `mkdocs.yml`. Grep for ratings: `grep -E 'human_rating|ai_rating' docs/videos/*.md`. Ratings are the explicit override path when a non-LinkedIn clip is picked for a portfolio page — check the sidecar before deploying or retiring a video.
