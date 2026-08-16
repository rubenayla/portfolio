# portfolio — Rubén Jiménez Mejías

**Live site: <https://rubenayla.xyz/>**

Recruiter-facing portfolio built with MkDocs Material — engineering projects, writing, and CV. (Personal notes / opinionated standards live separately at <https://notes.rubenayla.xyz/>, repo `rubenayla/notes`, and are linked only from an unobtrusive footer icon — kept out of the primary recruiter surfaces, not hidden entirely.) Three main sections:

1. **Homepage (`docs/index.md`)** — CV-style landing: who I am, what I work on, and direct links to LinkedIn, GitHub, and the resume PDFs (EN + ES). This is what someone lands on from a job application or LinkedIn click — it should answer "who is this person, and where do I find their CV?" in one screen.
2. **Project tabs** — one tab per substantial project (driverless kart, Partle, Cyberwheel, investment analysis, …). Each is a self-contained write-up under `docs/projects/`. A project with more than one page gets a folder — the kart is `docs/projects/kart/` with `index.md` plus `build-journey.md`.
3. **Writing tab** — essays. Lives under `docs/writing/`. Same status as a project tab: a section of the site, not a sub-page of something else.

Top-level nav tabs are defined in `mkdocs.yml` under `nav:`.

## Local Development

```bash
git clone https://github.com/rubenayla/portfolio.git
cd portfolio
uv sync
uv run mkdocs serve
```

Visit `http://127.0.0.1:8000`.

## Deployment

Auto-deploys to GitHub Pages via GitHub Actions on push to `main`. The custom domain (`rubenayla.xyz`) is wired through `docs/CNAME`.

### Setup GitHub Pages

1. Repository Settings → Pages
2. Build and deployment source: "GitHub Actions"
3. Push to `main` to trigger

## Structure

```
portfolio/
├─ docs/
│  ├─ index.md               # CV-style homepage (LinkedIn, GitHub, CV PDFs, project grid)
│  ├─ about.md               # Longer-form about page
│  ├─ files/                 # CV PDFs and other downloadable files
│  ├─ images/                # Site images
│  ├─ videos/                # Project videos (hero clips, demos)
│  ├─ projects/              # One markdown file per project tab
│  ├─ build-journey/         # Multi-page project write-up (driverless kart)
│  └─ writing/               # Essays (healthcare, …)
├─ mkdocs.yml                # Site config + nav (tabs)
├─ pyproject.toml
└─ .github/workflows/        # GitHub Actions deploy
```

## Adding Content

### A new project tab

1. Create `docs/projects/<name>.md`
2. Add it under `nav:` in `mkdocs.yml`
3. Optionally feature it on the homepage (`docs/index.md`)

### A new essay

1. Create `docs/writing/<topic>.md` (or a folder if it's multi-page)
2. Add it under the `Writing:` section in `nav:` in `mkdocs.yml`, nested under `Essays:`

### Images

Place in `docs/images/` and reference relatively:

```markdown
![Alt text](../images/your-image.jpg)
```

## License

MIT.
