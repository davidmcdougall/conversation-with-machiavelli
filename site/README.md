The build output, published to GitHub Pages by `.github/workflows/pages.yml`.
Regenerate with `scripts/build.py --all`; never edit by hand.

Pages share `style.css`; `404.html`, `sitemap.xml` and `robots.txt` are
generated with them. The content-only pages used as Claude artifacts are
written to `build/artifact-input/`, which is not committed or published.

Versioned, not frozen. Publish v0.3, be wrong, fix it, publish v0.4, and date
every page.
