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
- [x] Add Open Graph meta tags for social sharing — done 2026-08-05 (see Done section).
- [ ] Add favicon
- [ ] Optimize meta descriptions per page
- [ ] Create profiles on high-DR sites linking back (see partle/.agents/posts/profile-bios.md)

### Future
- [ ] Consider blog section
- [ ] Project status badges (Completed, Ongoing, Prototype)

## In Progress

## Done
- [2026-08-05] **Add OpenGraph + Twitter Card meta tags** — `overrides/main.html` emits `og:`/`twitter:` tags on every page; per-page `description`/`image`/`og_title` come from YAML front matter, with `images/kart/full-kart.jpg` as the default image. Links shared to LinkedIn/X/etc. now render a chosen image and blurb instead of a bare title-only card. Verified live on rubenayla.xyz.
- [2026-04-06] **Update Partle project page** — rewrote with current stack, real numbers, MCP, SSR, scraping details
- [2026-04-06] **Update mkdocs.yml site_url** — changed to rubenayla.xyz
