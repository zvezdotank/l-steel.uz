# Implementation guide — building the site with this system

Written for a coding agent (Claude Code). Everything below is grounded in the real lizhong-steelstructure.com screenshots; do not invent new colors, fonts or component variants.

## Setup

1. Copy this whole folder into the project (e.g. `design-system/`).
2. Link the single entry stylesheet on every page: `<link rel="stylesheet" href="/design-system/styles.css">`. It `@import`s the tokens, base resets and component classes, and pulls Inter from Google Fonts.
3. Take every color, size and spacing value from the CSS variables — never hard-code a hex or px the tokens already carry.

## Tokens you will use most

| Purpose | Token |
| --- | --- |
| Brand blue (header, buttons, active states) | `--color-primary-500` |
| Hover / pressed blue | `--color-primary-600` / `--color-primary-700` |
| Footer + sticky toolbar navy | `--color-primary-900` |
| Sparing orange highlight | `--color-accent-500` |
| Body text / muted text | `--color-text` / `--color-text-muted` |
| Page background / alt band | `--color-bg` / `--color-bg-alt` |
| Borders | `--color-border` |
| Spacing | `--space-1` … `--space-10` (4 → 128px) |
| Radius | `--radius-sm` (2px), `--radius-md` (4px) |
| Type | `--text-h1` … `--text-h4`, `--text-body`, `--text-body-sm`, `--text-caption` |

## Component classes (plain HTML, no JS needed)

- `.btn` + `.btn-primary` / `.btn-accent` / `.btn-secondary` / `.btn-ghost` / `.btn-block` — solid fill, centered plain-case label, near-square corners.
- `.card` (+ `.card-bordered`, `.card-elev`) with `.card-media`, `.card-eyebrow`, `.card-title`, `.card-body` — photo-led product/news card. Default has no border and no shadow.
- `.tag` + `.tag-primary` / `.tag-accent` / `.tag-neutral` / `.tag-outline`.
- `.field` + `label` + `.input` / `.textarea` / `.select`.
- `.nav` + `.nav-links` (`.active` on the current item) — white header bar with the brand lockup left, links right.
- `.table` — technical spec tables.
- `.section-heading` (with `.label` + `.chevron`) — the centered uppercase section divider with a blue chevron below it, used for "Hot Products", "About Us", "News", "Contact Us".
- `.toolbar` + `.toolbar-item` — the dark navy Inquiry / Whatsapp / Email / Top bar pinned mid-page on listing pages.
- `.footer` + `.footer-qr` / `.footer-social` / `.footer-list` / `.footer-bottom` — navy footer.
- `.hr` — 2px section rule.

React equivalents of all of the above live in `components/*/` (`Button`, `Card`, `Tag`, `Input`, `Navbar`, `Table`, `StickyToolbar`, `Footer`), each with a `.d.ts` props contract and a `.prompt.md` usage note. Use these if the build is React; use the CSS classes directly if it's static HTML or a template engine.

## Site structure to build

Nav (every page): HOME · ABOUT US · PRODUCT · FACTORY · NEWS · CONTACT, plus a "Quote Now" action. Footer on every page.

1. **Home** — full-bleed photo hero with the headline "Lizhong Steel Structure/Production and Processing" and the varieties/specifications/delivery line; directly below, a flush row of solid category buttons (Conventional Steel Structure Building, Public Steel Structure Building, Steel Components, Glass Curtain Wall Exquisite Steel, Hot Rolled Finished Profiles); then "HOT PRODUCTS" as a `.section-heading` over a photo card grid; then "ABOUT US" intro; "CONTACT US" band (email + WhatsApp); "NEWS" list of dated headlines.
2. **About Us** — page title "Lizhong Steel Structure (Shandong) Co., Ltd." with the chevron accent, company/team/capacity prose, ISO 9001 / 45001 / 14001 as `.tag-outline`, then a "HONOR" grid of certificate images.
3. **Products** — breadcrumb ("Home page > Products"), full-width blue "All categories" bar, 2–3 column photo card grid, sticky toolbar, numbered pagination with the current page in `--color-primary-500`.
4. **Product detail** — hero image, title, spec `.table`, inquiry CTA.
5. **Factory** — photo-led capability sections (workshop m², equipment list).
6. **News** — dated list, then article pages.
7. **Contact** — email, WhatsApp/Tel, QR codes, and the inquiry form (`.field` + `.input` + `.textarea` + `.btn-primary`).

`ui_kits/website/` is a working click-through of Home / About / Products / Contact — read it as the reference implementation.

## Rules

- Buttons: solid fill, centered label, plain case. Not uppercase, not letter-spaced.
- Blue carries almost everything; orange appears at most once per page as a highlight.
- Cards are plain white with the photo flush to the top edge — no borders, no shadows by default.
- Corners are near-square (2–4px), never pill-shaped.
- Hover/pressed states step one/two down the primary ramp; keyboard focus is a 2px `--color-primary-500` outline. Never leave browser defaults.
- Photography is full-color industrial/site photography — do not grayscale or tint it.

## Missing assets (ask the client before shipping)

- The real logo file — `Navbar`'s "W LIZHONG / STEEL STRUCTURE" lockup is a type reconstruction from a screenshot.
- Real social and toolbar icons — currently line-SVG and monogram placeholders.
- Product/factory photography and the certificate images for the Honor grid.
