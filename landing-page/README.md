# In X Evolution — Landing Page

Standalone static landing page for the In X Evolution project.

## Structure

```text
landing-page/
├── index.html
├── README.md
└── assets/
    ├── css/
    │   └── styles.css
    └── js/
        └── main.js
```

## Preview locally

Open `index.html` in a modern browser. No build step, package installation or backend is required.

For a local HTTP preview, run from the repository root:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/landing-page/`.

## Deployment

This is static HTML, CSS and JavaScript. It can be deployed using GitHub Pages or another static host. Hosting, custom domain, analytics, forms and external services are not configured by this folder.

## Content and claims

The page deliberately describes the portfolio as proposed and the project as being in strategy/discovery. Do not publish claims that products, services, legal entities, partnerships or regulated permissions exist unless verified and approved.

## Accessibility and maintenance

- Semantic landmarks and headings.
- Skip-to-content link and visible keyboard focus.
- Mobile navigation with an accessible expanded state.
- Reduced-motion preference respected.
- CSS and JavaScript separated from HTML.
- No third-party runtime dependencies.
