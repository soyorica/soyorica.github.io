# Soyorica official website

Static, dependency-free website for GitHub Pages.

## Deploy

Copy the contents of this folder to the root of `soyorica/soyorica.github.io` and push to the default branch used by GitHub Pages. Because the repository name is `soyorica.github.io`, the site is designed for the domain root (`https://soyorica.github.io/`).

## Key files

- `DESIGN_SYSTEM.md` — references, design rules, SEO/accessibility rules
- `WIREFRAME.md` / `wireframe.html` — black-and-white information architecture used before visual styling
- `assets/site.css` — visual system
- `assets/site.js` — mobile navigation and copy-path buttons only
- `products/`, `docs/`, `install/`, `faq/` — Japanese pages
- `en/` — English equivalents
- `sitemap.xml`, `robots.txt` — crawl support

## Product status reflected in this build

- HairSway: on sale. Direct BOOTH item link is enabled.
- MathMotionGraph: full version marked as coming soon.
- MathMotionGraph Lite: marked as free; no download URL is invented because none was supplied.

## Updating product availability

When MathMotionGraph is released, replace the coming-soon text and add the confirmed store/download URLs in the product pages. If the Lite distribution URL becomes available, add it as a real CTA rather than a disabled placeholder.
