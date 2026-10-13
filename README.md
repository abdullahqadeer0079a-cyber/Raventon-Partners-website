# Raventon Partners – Agency Website

A multi-page website for a performance marketing agency offering **Google Ads**, **Meta Ads**, **PPC management**, **lead generation** and **landing pages & CRO**.

## Pages
- Home, About Us, Services (+ one detail page per service), Blog (+ articles), Contact
- Privacy Policy, Terms & Conditions, 404

## Features
- Responsive design with an app-style mobile experience (bottom tab bar, swipeable carousels, collapsible footer)
- Corporate visual identity: Oxford navy + brass, Source Serif 4 headings over IBM Plex Sans, squared geometry and hairline rules
- Layered dashboard/phone hero scene with restrained motion (no gradients, blobs or cursor effects)
- Scroll reveal, stagger and a subtle hover lift powered by [Motion](https://motion.dev) (respects `prefers-reduced-motion`)
- No build tools needed to view the site – it is plain HTML, CSS and JavaScript

## Run locally
```bash
python -m http.server 8000
# open http://localhost:8000
```

## Editing content
Page content lives in `build.py`. After editing it, regenerate the pages:
```bash
python build.py
```
Styles and scripts are in `assets/`. Design tokens (colours, fonts, radius, shadow) live in the `:root` block at the top of `assets/style.css`.

## Notes
- `next-reference/Reveal.tsx` is a TypeScript/Next.js version of the reveal component, for a future port. It is not used by the static site.
- Company details, testimonials, clients and statistics are placeholders.
- Motion is loaded from the jsDelivr CDN, so an internet connection is needed for the animations.
