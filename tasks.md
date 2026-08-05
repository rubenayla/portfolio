<!-- read in full — kept under 150 lines -->
# Tasks

## TODO

### Domain Migration
- [ ] Add CNAME file (`docs/CNAME` with `rubenayla.xyz`) to repo
- [ ] Configure Cloudflare DNS: CNAME `rubenayla.xyz` -> `rubenayla.github.io`
- [ ] Set custom domain in GitHub Pages settings
- [ ] Verify HTTPS works after migration
- [ ] Set up redirect from old `rubenayla.github.io/portfolio/` to `rubenayla.xyz`

### Content Updates
- [ ] Add project images for Driverless Kart (action shots, team, hardware)
- [ ] Add project images for Cyberwheel (renders, prototype, assembly)
- [ ] Add images for other projects (steering, electronics, PCBs)
- [ ] Add profile photo to About page
- [ ] Add specific metrics/results to project pages
- [ ] Update CV PDFs with latest version

### SEO & Backlinks
- [ ] Add Open Graph meta tags for social sharing (`og:title`/`og:description`/`og:image` per page, plus `twitter:card`). Without these, LinkedIn/X build a bare card from the `<title>` alone — no description, no image. Confirmed 2026-08-05 while adding LinkedIn Featured cards: had to set every card's title/description/thumbnail by hand. MkDocs Material supports this via a `meta` plugin or per-page front matter + an `overrides/main.html` block.
- [ ] Add favicon
- [ ] Optimize meta descriptions per page
- [ ] Create profiles on high-DR sites linking back (see partle/.agents/posts/profile-bios.md)

### Future
- [ ] Consider blog section
- [ ] Project status badges (Completed, Ongoing, Prototype)

## In Progress

## Done
- [2026-04-06] **Update Partle project page** — rewrote with current stack, real numbers, MCP, SSR, scraping details
- [2026-04-06] **Update mkdocs.yml site_url** — changed to rubenayla.xyz
