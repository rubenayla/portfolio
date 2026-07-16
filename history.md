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
