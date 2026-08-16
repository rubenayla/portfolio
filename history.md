<!-- consult selectively — grep, never read in full -->
# History

Dated log of decisions and changes, oldest-first, at topic level. Grep by topic (e.g. "kart page", "build journey") rather than reading in full.

## Kart page → Build Journey layout

### 2026-07-01 — Inlined the Build Journey into the kart overview page
Reworked the bottom of `docs/projects/kart.md` after the user questioned whether the image gallery was pulling its weight.

Decisions made this session:
- **Dropped the `## Gallery` section.** It was six decontextualised build photos (`full-kart`, `chassis-arrival`, `zed2-mount`, `steering-planetary`, `battery-pack`, `kart-medulla-pcb`) that just previewed the same images already told with story in the Build Journey. The two videos (autoplay hero + autonomous-run clip) already carry the visual proof for a fast skimmer, so the gallery was redundant.
- **Removed the bottom "Continue to the Build Journey" button** and instead render the whole journey inline. The user wanted zero-friction: scroll from the overview straight into the story with no click. A click is only avoidable if both live on the *same rendered page*, so this is a merge, not a link.
- **Implementation = build-time include, not a copy.** Enabled `pymdownx.snippets` (`base_path: docs`, `check_paths: true`) in `mkdocs.yml` and pull the journey in with `--8<-- "build-journey/index.md"` at the bottom of the kart page. `docs/build-journey/index.md` stays the single source of truth — the weekly-append workflow is untouched.
- **Kept the standalone `/build-journey/` page.** AGENTS.md declares the per-post anchors (`/build-journey/#motor`, etc.) as stable URLs, so the page must keep building even though it's now also embedded on the kart page. Accepted tradeoff: the journey HTML renders on both `/projects/kart/` and `/build-journey/` (duplicate rendered output). For a personal portfolio the SEO cost is negligible and it's the price of preserving the stable anchors.
- **Top button repointed** from `../build-journey/index.md` to the in-page `#build-journey` anchor, so it scrolls down to the inlined journey instead of navigating away.

Why "lazy loading" wasn't the real lever: all 19 journey images already carry `loading=lazy`, so inlining the journey doesn't hurt load time — the browser still only fetches images on scroll. The decision was UX (one page vs two), not performance.

Deferred (resolved 2026-07-02, see below).

Commit `45c8794`. GitHub Pages deploy succeeded.

### 2026-07-02 — Resolved the deferred items; re-added the photos as a collapsed section
- **Kept the standalone "Build Journey" nav entry.** User: the inline copy on the kart overview exists only to hook the viewer; the journey is *conceptually a sub-part* and belongs as its own standalone page. So the nav stays as-is — inline hook on the overview, canonical standalone page in the nav.
- **Re-added the six build photos as a collapsed `??? note "Build photos"` section** (Material `pymdownx.details`), placed where the old `## Gallery` was (between the autonomous-run video and `## Links`). Collapsed by default, no nav entry and no button/link pointing to it — visible to anyone curious, invisible weight otherwise. This resolves the earlier "orphaned images" question: the six `docs/images/kart/` files are in use again, not deleted.

## tasks.md location

### 2026-07-16 — Consolidated tasks.md to the repo root; retired `.agents/tasks.md`
`.agents/tasks.md` was moved to `tasks.md` at the repo root with `git mv`, so the file's history follows it. `.agents/tasks.md` no longer exists in this repo and must not be recreated — the rule is one `tasks.md` per repo, at the root.

Rationale: tasks are the project's tasks regardless of who does them. Two files named `tasks.md` only produce duplicates and stale entries, because whichever one the current session isn't reading quietly goes out of date.

`AGENTS.md`'s "Agent Files" list now points at the root `tasks.md`.

Stale `.agents/tasks.md` paths in append-only records were deliberately left as written — they were accurate on the date they were logged, and rewriting them would falsify the record. This covers `.agents/error-log.md` and the note in `.agents/notes.md` that references `~/repos/dv-hardware/.agents/tasks.md` (a different repo's board, not this one).

## The `/build-journey/` URL is wrong, and it is already in a sent job application

### 2026-08-16 — Named for its first occupant, then locked in by outreach
The build journey lives at `https://rubenayla.xyz/build-journey/`. Every entry on it is about the
driverless kart, and always has been. Rubén flagged the URL as wrong: he will build many things over
the years, and a top-level `/build-journey/` claims to cover all of them while holding one project.
`kart-build-journey/` would at least have been honest; the correct place is under the project,
`/projects/kart/build-journey/`.

This was not a case of the page's meaning changing after the fact. The page was named for the first
thing that went into it. When `c2c028d` created it, the mental model was "the page where my weekly
LinkedIn posts go" — a posting campaign belongs to a person, not a project, so top-level looked
right. Nobody asked what the page would be called once a second project existed. That question had
one obvious answer available on day one.

Two later commits made it harder to fix rather than easier. `7ee7531` collapsed the journey into one
scrolling page and `AGENTS.md` declared the per-post anchors (`/build-journey/#motor`, `#battery`,
and the rest) stable public URLs — turning the address into a promise. Then `45c8794` inlined the
whole journey into the kart page with a `pymdownx.snippets` include, because the kart page should
obviously carry its own build log. At that point the content existed in two rendered places and the
standalone page was kept alive only to honour the anchor promise. The cheap move was to duplicate
and leave the address alone.

**The URL is now load-bearing outside this repo.** A grep of `~/vault` found it in outreach:

- `future/applications/Duatic/cover_letter.md:7` — "Build journey: rubenayla.xyz/build-journey".
  This application was **sent on 2026-08-14** (`future/applications/Duatic/Duatic.md`), so a real
  recruiter holds this link.
- `future/applications/AutoStore/cover_letter.md:27` — same link, drafted, not sent as of this date.
- `future/preferences.md:125` — a standing instruction for how to order artifact links in job
  applications names `rubenayla.xyz/build-journey` as the second link for any kart-related role, so
  every future application will reproduce it until that line is updated.

Checked and clean: no published LinkedIn post text under `~/ruben-files/videos/kart/linkedin/posts/`
links to it (those link to `um-driverless.github.io/kart-docs/`), and the CV one-pager at
`~/vault/paperwork/cv/project-sheet/onepager.html` points at the kart-docs build journey, not this
one. Rubén's LinkedIn profile itself was not checked and may carry the link.

**Consequence for any fix:** the address cannot simply disappear. Moving the page requires a
redirect from `/build-journey/` that a recruiter clicking a months-old PDF still lands on. The site
is GitHub Pages with a custom domain, so there is no server-side redirect available — it needs the
`mkdocs-redirects` plugin, which is not currently installed (`mkdocs.yml` has no `plugins:` block
and `pyproject.toml` lists only `mkdocs-material`). Whether that plugin's generated redirect carries
the URL fragment through is untested, so `/build-journey/#motor` surviving the move is an open
question, not an assumption.

**Rule this repeats:** name a file or a URL for the job it does, not for the first thing that goes
into it. A name chosen for a temporary meaning gets frozen by whatever starts depending on it —
here, a stability rule written into `AGENTS.md` and then a cover letter mailed to a company.

### 2026-08-16 — Moved it: `/projects/kart/build-journey/`, old URL redirects
Nested rather than flat. `/projects/kart-build-journey/` was considered and rejected: `/projects/`
means one project per entry, so a flat `kart-build-journey` would put something that is not a
project into that list, and the hyphen would be faking the hierarchy that a slash expresses for
real. Nesting also extends to `/projects/partle/build-journey/` without inventing a convention.

`docs/projects/kart.md` → `docs/projects/kart/index.md` (same URL, `/projects/kart/`), and
`docs/build-journey/index.md` → `docs/projects/kart/build-journey.md`.

**Asset paths had to become root-absolute.** The journey file is rendered at two URL depths — as its
own page at `/projects/kart/build-journey/` and snippet-included into `/projects/kart/` — so no
single `../` count works for both. All `../images/...` became `/images/...`, and the kart page's own
assets followed for consistency. The videos were already absolute: commit `978d18b` had hit exactly
this problem once before and fixed only the videos. `mkdocs build` now prints an INFO line per
absolute link suggesting a relative one; that suggestion is wrong for a site served from the apex
domain, and the lines are expected noise.

**The old URL is a redirect, not a copy.** Added `mkdocs-redirects` (`uv add`; CI runs `uv sync`, so
it installs itself) with one entry mapping `build-journey/index.md` to the new page. The plugin's
generated stub carries the fragment across in JavaScript —
`location.href = url + (anchor ? "#" + anchor : "")` — so deep links survive. Verified in a headless
browser rather than assumed: `/build-journey/#motor` ends at `/projects/kart/build-journey/#motor`.
The `redirect_maps` entry carries a comment saying it is obsolete, why it is kept (the Duatic cover
letter), and when to delete it.

Checked with all 26 images and 9 videos loaded on `/projects/kart/` (details blocks forced open,
since the six build photos sit in a collapsed `??? note` and lazy-load) and all 20 on
`/projects/kart/build-journey/`. No broken assets.

**Outreach fixed at the source.** `~/vault/future/preferences.md` was the file generating the bad
link — it instructed every application to link `rubenayla.xyz/build-journey`. It now names
`rubenayla.xyz/projects/kart/` and carries an explicit line never to use the old URL again. The
unsent AutoStore cover letter had both links as separate bullets; the build-journey bullet was
dropped rather than repointed, since the journey renders inline at the bottom of the kart page and
one link covers both. The Duatic letter is already sent and was left alone — it is a record.
`~/ruben-files/videos/kart/linkedin/AGENTS.md` step 10, which drives the weekly post mirror, now
points at the new file path.

Still open, on `tasks.md`: the LinkedIn profile may link the old URL and can only be checked by
logging in, and the redirect itself should be deleted once the sent applications go stale.
