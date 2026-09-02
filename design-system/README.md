# Lizhong Steel Structure — Design System

## Context

Lizhong Steel Structure (Shandong) Co., Ltd., based in Jinan Laiwu District, China, is a design/manufacturing/construction integrated service provider for steel structures: conventional and public steel structure buildings, steel components (box columns, crane beams), glass curtain wall steel profiles, and hot-rolled finished profiles. It holds ISO 9001, ISO 45001 and ISO 14001 certification, runs multiple production workshops in Jinan (incl. a 40,000㎡ base), and exports worldwide. Built on the real site at **https://www.lizhong-steelstructure.com/**: page text pulled via search-engine cache (the live site couldn't be fetched directly from this environment), plus three user-supplied screenshots (homepage, About, Products) that this system's colors, type and layout are drawn from directly.

## Content fundamentals

- Third-person corporate voice, translated-from-Chinese English; matter-of-fact and technical rather than persuasive.
- Leads with certifications and hard capacity numbers (workshop m², headcount by role, laser-cutter wattage) as credibility signals.
- No emoji, no casual tone. Sentences are declarative and specification-oriented ("Compared with hot-rolled I-beams, hot-rolled H-beams can save 15% to 30% of steel").
- Contact info (email, WhatsApp) is surfaced repeatedly — nav CTA, mid-page, footer — not tucked into one place.
- Section dividers ("About Us", "Hot Products", "News", "Contact Us") are short, centered, all-caps labels.

## Visual foundations

- **Color** — a single strong brand blue (`--color-primary-*`) carries the header, product-category buttons, active pagination and CTA states; the same hue's darkest step doubles as the near-navy footer/sticky-toolbar background. Orange (`--color-accent-*`) appears only once, on a single product-category button — used sparingly, not as the main CTA color. Neutral grays for muted text, breadcrumbs, borders.
- **Type** — a plain sans (no condensed/display face) for both headings and body; substituted with Inter (Google Fonts) since no webfont files were retrievable.
- **Layout** — full-width photo hero under the nav, a row of solid-color category buttons directly below it, then a plain grid of photo-led product cards. Breadcrumbs above list pages. A dark sticky action bar (Inquiry / Whatsapp / Email / Top) floats mid-page on product listings.
- **Radius** — small and functional; buttons/cards read essentially square.
- **Cards** — plain white, no border, photo full-bleed at the top edge, title + muted description below; no shadow by default.
- **Buttons** — solid color fill, centered label, normal case (not uppercase/letter-spaced).
- **Footer** — dark navy: contact block, WhatsApp/WeChat QR codes side by side, a row of circular social icons (Facebook/Instagram/YouTube/TikTok), a bulleted product list, and a thin copyright bar.
- **Motion** — none observed; kept to simple 150ms hover/focus transitions on interactive elements only.

## Iconography

The real site's icons (toolbar glyphs, social icons) weren't recoverable as assets. `StickyToolbar` uses simple line-icon SVGs (chat bubble, phone, envelope, chevron-up) as reasonable stand-ins; `Footer`'s social row uses neutral letter-monogram placeholders rather than the real Facebook/Instagram/YouTube/TikTok marks. Swap both for real assets/icon set when available.

## Logo

**No logo file is available** — only a screenshot. `Navbar`'s brand mark (blue "W" square + "LIZHONG / STEEL STRUCTURE" wordmark) is a type-based reconstruction of what's visible in the screenshot, not the real vector logo. Replace with the actual file when you have it.

## Contents

- `styles.css` — entry point (imports tokens, base resets, components.css)
- `tokens/` — colors, typography, spacing
- `base.css`, `components.css` — resets and shared component classes
- `guidelines/` — foundation specimen cards (Colors, Type, Spacing, Brand)
- `components/` — Button, Tag, Card, Input (forms), Navbar, Table, StickyToolbar, Footer — each with `.jsx` + `.d.ts` + `.prompt.md` + a `.card.html` demo
- `ui_kits/website/` — click-through recreation of Home / About / Product / Contact, with the shared Navbar + Footer
- `guidelines/implementation.md` — **build guide for Claude Code**: setup, token/class reference, page-by-page site structure, styling rules
- `SKILL.md` — Claude Code-compatible skill wrapper

## Open items

1. **Real logo file** — send it and I'll swap out the reconstructed wordmark.
2. **Real icon/social assets** — Facebook/Instagram/YouTube/TikTok icons and the toolbar glyphs are placeholders.
3. **Product photography** — cards in the UI kit render without images; send a few product/factory photos to drop in.
4. Colors/type are read directly off the screenshots you provided but are still eyeballed, not sampled pixel-exact — flag anything that looks off.
