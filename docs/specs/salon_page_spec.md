# Inquiry Institute — Codex Spec  
## Implement `/programs/salon/`

### PURPOSE
Add a new Programs subpage explaining the Feminine Salon, including seasonal salons, the Salon Box, the Salon Circle subscription, and online participation.

---

## PAGE LOCATION
`/programs/salon/`

This is a public-facing page linked under **Programs**.

---

## CONTENT SECTIONS (REQUIRED)
1. **Hero Section**  
   - Title: *“The Feminine Salon”*  
   - Subtitle: *“Where intellect softens into beauty.”*  
   - Visual: candlelight / floral motif

2. **What Is a Salon?**  
   Public explanation of feminine inquiry.

3. **Seasonal Salons**  
   With section headings:
   - Candlemas → Beltane
   - Beltane → Lammas
   - Lammas → Samhain
   - Samhain → Candlemas

4. **Featured Salon (Candlemas Salon: The First Softness)**  
   Theme, roles, ritual flow, seasonal tone.

5. **Online Participation**  
   Lighting, candle, ribbon, pacing, camera guidelines.

6. **Salon Box**  
   Short product description + link to `/programs/salon/box/`.

7. **Salon Circle Subscription**  
   Tier list + links:
   - Basic  
   - Luxe  
   - Patron

8. **The Salon Code**  
   10-point feminine code.

---

## DESIGN REQUIREMENTS
- Palette: **pearl, blush, ivory, soft gold**  
- Typography: **Playfair Display**, **Garamond**, or similar  
- Imagery: soft edges, feminine, candlelight  
- Icons: moon, flower, ribbon, candle  
- Avoid harsh lines or dark blocks  
- Gentle spacing + large margins  

---

## LEFT ICON → PROJECT STATUS SLIDE PANEL (REQUIRED)
On the left edge of the page, there are two icons. **The latter (second) icon** must open a **slide-in panel from the left** that gives stakeholders quick context about this page and its implementation initiative.

### Trigger
- **Icon**: the second/“latter” left-side icon (recommend an **info** / **sparkle** / **scroll** glyph).
- **Interaction**: click/tap toggles the panel.

### Motion & layout
- **Animation**: slide in from the left over ~200–300ms; slide out on close.
- **Width**:
  - Desktop: ~360–420px (or ~30% of viewport, whichever is smaller).
  - Mobile: full-height, near full-width (leave ~12–24px gutter if desired).
- **Overlay**: dim the main page behind the panel; clicking the dimmed area closes it.
- **Accessibility**:
  - Focus moves into panel on open; focus trap while open.
  - Close via **Esc** and via a visible close control.
  - Appropriate ARIA for a modal/drawer.

### Panel contents (in this order)
1. **What this page should do**
   - 3–7 bullets describing intended user outcomes and key sections/CTAs.
2. **Estimated cost to get there**
   - A single **range** (e.g., “$X–$Y”) plus a brief breakdown (design, copy, build, integrations).
   - Include a note for assumptions/unknowns (e.g., “store + calendar integration scope pending”).
3. **How the initiative is doing**
   - **Status**: Not started / In progress / Blocked / Done
   - **Confidence**: Low / Medium / High
   - **Progress**: % complete (or milestone-based)
   - **Milestones**: 3–6 checkpoints with dates/owners if known
   - **Risks/Deps**: short list (e.g., assets, store integration, calendar integration)
   - **Last updated**: date stamp

### Data source: OpenCollective (required for initiative text)
The **initiative text** shown in this panel (especially “Estimated cost to get there” and “How the initiative is doing”) must be sourced from **OpenCollective**, so non-engineers can update it without deploying code.

- **Source-of-truth**: an OpenCollective **Update** post (longform text) dedicated to this initiative.
- **Selection rule** (pick one; recommended is the slug rule):
  - **Recommended**: fetch the Update by a known **slug** (e.g. `salon-page-initiative`).
  - Alternative: fetch the most recent Update that contains a specific tag/marker in the title (e.g. `[Initiative] Salon Page`).
- **Rendering**:
  - Render the Update body as **sanitized HTML/Markdown** (no unsafe HTML injection).
  - Preserve headings and lists so the content can map cleanly onto the three required panel sections.
- **Fallback**:
  - If OpenCollective is unavailable, show the “Suggested default values” below plus a small note: “Initiative panel is temporarily unavailable.”

### Suggested Update template (OpenCollective post body)
Maintain the Update body using these headings (so the UI can render it verbatim, or optionally parse into sub-sections):
- `## What this page should do`
- `## Estimated cost to get there`
- `## How the initiative is doing`

### Implementation notes (for the website repo)
- Use the OpenCollective **GraphQL API** to fetch the Update content server-side.
- Configure via environment variables:
  - `OPENCOLLECTIVE_COLLECTIVE_SLUG` (e.g. `inquiry-institute`)
  - `OPENCOLLECTIVE_INITIATIVE_UPDATE_SLUG` (e.g. `salon-page-initiative`)
  - `OPENCOLLECTIVE_API_TOKEN` (optional; only if needed for private/unlisted content)
- Add caching (e.g., 5–30 minutes) to avoid rate limits and keep page loads fast.

### Suggested default values (fill in during implementation)
- **What this page should do**: explain Feminine Salon; link to seasonal pages; explain online participation; link to Box and Circle.
- **Estimated cost**: TBD by Codex after confirming store + calendar integration requirements.
- **Initiative status**: Not started; progress 0%; last updated at time of first implementation PR.

---

## ROUTES & SUBPAGES TO PREPARE
- `/programs/salon/candlemas/`  
- `/programs/salon/beltane/`  
- `/programs/salon/lammas/`  
- `/programs/salon/samhain/`  
- `/programs/salon/box/`  
- `/programs/salon/circle/`

(These can be skeleton pages for now.)

---

## ASSETS NEEDED
- Hero image (candle or petals)  
- Seasonal illustrations  
- Box photos (placeholders OK)  
- Icon set (moon, candle, flower, ribbon)  
- Typography set (serif)

---

## GO-LIVE CHECKLIST
- [ ] Page in nav under **Programs**  
- [ ] Hero section renders properly  
- [ ] Seasonal blocks lay out correctly  
- [ ] Box and Circle links working  
- [ ] Mobile responsive  
- [ ] Store integration for Box + Subscription  
- [ ] Calendar integration for Salon events  

---

## SUMMARY
This spec defines everything Codex needs to implement the Salon page and prepare for the larger Salon subsystem (seasonal pages, boxes, subscriptions).
