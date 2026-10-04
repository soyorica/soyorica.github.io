# QUALITY_CHECK

## Evaluation criteria

The criteria were fixed before implementation in `DESIGN_SYSTEM.md`. This file records the final pass.

### Manual review

- [x] Home identifies Soyorica and DaVinci Resolve / Fusion without relying on a generic slogan.
- [x] No gradient blobs, glass cards, oversized sentence hero, or decorative 3D effects.
- [x] Product status is explicit: HairSway on sale, MathMotionGraph coming soon, Lite free.
- [x] Product pages link to manuals; manuals link to install/support; BOOTH is reachable from global navigation.
- [x] Basic usage and parameter reference are separate sections in each manual.
- [x] Installation paths have dedicated copy buttons.
- [x] Japanese is the root language; English has independent `/en/` URLs.
- [x] Mobile layout changes from split rows to single-column reading order.
- [x] Motion is limited and `prefers-reduced-motion` is supported.
- [x] The content remains readable with JavaScript disabled.

### Release decision

PASS — suitable as a first public implementation. Store/download URLs that were not supplied are intentionally not invented.

### Automated checks

- HTML pages checked: 20
- Broken internal links / missing local images: 0
- SEO metadata errors (title / description / canonical / hreflang): 0
- Duplicate title / description warnings: 0
- Contrast ratios: body text on white 15.44:1; muted text on paper 5.20:1; navy on white 12.62:1

The automated checker is included as `tools/check_site.py`.
