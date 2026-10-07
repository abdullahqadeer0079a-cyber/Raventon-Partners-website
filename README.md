# Zenvora Digital – Agency Website

A multi-page marketing website for a digital agency offering **Web Development**, **Mobile App Development** and **UI/UX Design**.

## Pages
- Home, About Us, Services (+ one detail page per service), Blog (+ articles), Contact
- Privacy Policy, Terms & Conditions, 404

## Features
- Responsive design with an app-style mobile experience (bottom tab bar, swipeable carousels, collapsible footer)
- Animated hero (layered dashboard/phone scene, particle background, typed headline)
- Scroll reveal, stagger and hover lift powered by [Motion](https://motion.dev) (respects `prefers-reduced-motion`)
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
Styles and scripts are in `assets/`.

## Notes
- `next-reference/Reveal.tsx` is a TypeScript/Next.js version of the reveal component, for a future port. It is not used by the static site.
- Company details, testimonials, clients and statistics are placeholders.
- Motion is loaded from the jsDelivr CDN, so an internet connection is needed for the animations.
