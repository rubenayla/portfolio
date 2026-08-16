<!-- read in full — kept under 150 lines -->
# Tasks

## TODO

### Site structure
- [ ] **Check whether the LinkedIn profile links `rubenayla.xyz/build-journey`** (About section,
  Featured cards, or the contact/website field) and repoint it to
  `rubenayla.xyz/projects/kart/`. The move on 2026-08-16 covered every reference on disk; the
  LinkedIn profile is the one surface that can only be checked by logging in. The old URL still
  redirects, so this is tidying, not a breakage.
- [ ] **Retire the `/build-journey/` redirect in `mkdocs.yml`** once the applications that printed
  that URL are stale — roughly 2027, or whenever the Duatic thread (applied 2026-08-14) is closed.
  Deleting the `redirects` plugin block is the whole job.

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
- [ ] Add favicon
- [ ] Optimize meta descriptions per page
- [ ] Create profiles on high-DR sites linking back (see partle/.agents/posts/profile-bios.md)

### Future
- [ ] Consider blog section
- [ ] Project status badges (Completed, Ongoing, Prototype)

## In Progress
