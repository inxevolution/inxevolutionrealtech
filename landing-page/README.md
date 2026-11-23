# In X Evolution — Real Technology Landing Page

Standalone, responsive landing page for the In X Evolution Real Technology area.

## Structure

```text
landing-page/
├── index.html
├── README.md
└── assets/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── main.js
    └── images/
        └── favicon.svg
```

## Local preview

From the repository root, run:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/landing-page/` in a browser.

No package installation, build step, backend or third-party JavaScript dependency is required.

## Features

- Responsive desktop, tablet and mobile layouts.
- Semantic page structure, skip link and keyboard focus styles.
- Accessible mobile navigation with Escape-to-close behaviour.
- Reduced-motion preference support.
- Lightweight scroll-reveal effects with an Intersection Observer fallback.
- Search/social metadata and a standalone SVG favicon.
- Dedicated open-source section linking to the repository's license.

## License

The repository root contains **The Unlicense**. Read the exact license text in [../LICENSE](../LICENSE) or visit [unlicense.org](https://unlicense.org/).

The Unlicense dedicates the covered software to the public domain to the extent recognised by applicable law and provides the software "AS IS", without warranties or liability. Do not assume that third-party assets, trademarks, brand names, external services or separately licensed materials are covered by the repository license; verify their terms independently.

## Content status

The page describes proposed capabilities and strategic direction. It does not claim that every service is currently available, that a corporate structure has been legally established, or that regulated services are authorised.

## Deployment

The files are static and can be hosted through GitHub Pages or another static host. Public hosting, a custom domain, analytics and contact-form processing are not configured by this directory.
