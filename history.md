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

Deferred (not done, awaiting user decision):
- Whether to drop the "Build Journey" nav sub-entry now that the content is inline on the overview.
- Whether to delete the six now-orphaned gallery images under `docs/images/kart/`.

Commit `45c8794`. GitHub Pages deploy succeeded.
