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
