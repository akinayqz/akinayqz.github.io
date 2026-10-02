## Development

Hugo site using the [rewired](https://github.com/RigleGit/rewired) theme (git submodule in `themes/rewired`).

- Run locally: `hugo server` (http://localhost:1313)
- Production build: `hugo --gc --minify`
- After cloning: `git submodule update --init --recursive`

Don't edit `themes/rewired` directly. Override theme files from the site root instead (same path under `layouts/` or `assets/`):

- `assets/css/cactus.css`: Cactus "white"/"dark" colour palettes and the theme toggle styles
- `layouts/_partials/head/css.html`: theme CSS bundle + syntax/cactus CSS, rewrites Rewired's hard-coded rgba tints to colour variables
- `layouts/_partials/head/js.html` + `assets/js/theme-toggle.js`: light/dark switching
- `layouts/_partials/nav.html`: adds the toggle button
- `layouts/home.html`: adds the photo "terminal window" to the hero (`params.photo` in `hugo.toml`, image under `assets/`); styles at the bottom of `cactus.css`. Shows the text-art portrait from `data/portrait.json` (regenerate with `python3 scripts/portrait.py assets/images/me.jpg`), or a tinted photo if that file is absent
- `assets/css/syntax.css`: generated with `hugo gen chromastyles` (dracula for dark, github for light)

Deployed to GitHub Pages by `.github/workflows/deploy.yml` on push to `main`.
