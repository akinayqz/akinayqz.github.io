## Development

Hugo site using the [rewired](https://github.com/RigleGit/rewired) theme (git submodule in `themes/rewired`).

- Run locally: `hugo server` (http://localhost:1313)
- Production build: `hugo --gc --minify`
- After cloning: `git submodule update --init --recursive`

Don't edit `themes/rewired` directly. Override theme files from the site root instead (same path under `layouts/` or `assets/`):

- `assets/css/cactus.css`: Cactus "white"/"dark" colour palettes, the theme toggle, and home hero tweaks (tagline "|" drawn as a full-height border)
- `layouts/_partials/head/css.html`: theme CSS bundle + syntax/cactus CSS, rewrites Rewired's hard-coded rgba tints to colour variables
- `layouts/_partials/head/js.html` + `assets/js/theme-toggle.js`: light/dark switching
- `layouts/_partials/nav.html`: adds the toggle button
- `layouts/home.html` + `layouts/_partials/home/*.html`: home sections below the intro are listed (and ordered) by `params.homeSections` in `hugo.toml`; each partial skips itself when empty. `home.html` also adds the photo "terminal window" to the hero (`params.photo` in `hugo.toml`, image under `assets/`); styles at the bottom of `cactus.css`. Shows the text-art portrait from `data/portrait.json` (regenerate with `python3 scripts/portrait.py assets/images/me.jpg`), or a tinted photo if that file is absent
- `layouts/_partials/nav.html` also hides menu links to sections with no pages yet (the blog until the first post); a section can opt out with `alwaysInMenu: true` in its `_index.md`
- `layouts/_partials/project-card.html`: the project card from the theme's `/projects/` page, reused on the home page (`params.projectsHomeCount`, default 4). If the theme changes its card markup, update this copy to match
- Publications: entries live in `data/publications.yaml` (newest first; `selected: true` puts one on the home page). Rendered by `layouts/_partials/publication/row.html` on the home page and `layouts/publications/section.html`; styles in `assets/css/publications.css`; options under `[params.publications]` in `hugo.toml`
- `assets/css/syntax.css`: generated with `hugo gen chromastyles` (dracula for dark, github for light)

Deployed to GitHub Pages by `.github/workflows/deploy.yml` on push to `main`.
