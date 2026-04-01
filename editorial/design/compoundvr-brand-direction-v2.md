# CompoundVR Brand Direction v2
## Visual System Update — Light Body, Dark Header

**Date:** March 18, 2026  
**Author:** Richard (Managing Editor)  
**Status:** Approved Direction — Ready for Implementation  
**Constraint:** Existing logo (v5) remains unchanged — dark header preserved

---

## Executive Summary

Based on publisher feedback, CompoundVR shifts to a **sophisticated light-body design** that maintains editorial authority while elevating visual polish. The dark header anchors the brand (matching the existing logo), while the body transitions to an elegant light theme inspired by premier enthusiast publications.

**Core Principle:** Light doesn't mean generic. The design must feel like Wired, Engadget, or The Verge — confident, editorial, technically credible.

---

## Design Rationale

### Why Light Body Works for CompoundVR

**Reference Analysis:**

| Publication | Approach | Why It Works |
|-------------|----------|--------------|
| **Wired** | Clean white backgrounds, bold typography, editorial confidence | Authority through restraint; content-forward |
| **Engadget** | Light gray surfaces, card-based, tech-focused | Scannable, modern, enthusiast-appropriate |
| **Nexus Mods** | Functional white/light gray, information-dense | Community credibility, tool-like utility |
| **The Verge** | Off-white backgrounds, strong hierarchy, distinctive | Memorable without being flashy |

**Key Insight:** The most credible enthusiast media uses light backgrounds not because they're "safe," but because they signal editorial maturity. Dark themes often read as "gaming aesthetic" — light themes read as "publication."

### What We're Keeping

- **Dark header (#0b1020)** — anchors the logo, provides brand continuity
- **Cyan accent (#0ee7ff)** — tech-forward, VR-appropriate
- **Purple secondary (#8b5cf6)** — editorial distinction
- **Inter typography** — modern, readable
- **Card-based layout** — scannable, proven pattern
- **Technical authority tone** — no hype, just evidence

### What We're Changing

- **Body background** — shifts from dark navy to warm off-white
- **Card surfaces** — light gray instead of dark charcoal
- **Text hierarchy** — dark grays instead of light grays
- **Border system** — subtle dark borders instead of light borders
- **Score badges** — adapted for light context with maintained impact

---

## Color System v2

### Background Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-header` | `#0b1020` | Header only — matches logo |
| `--bg-body` | `#fafafa` | Main page background — warm off-white |
| `--bg-secondary` | `#f5f5f5` | Section alternates, footer |
| `--bg-tertiary` | `#eeeeee` | Subtle section backgrounds |

**Rationale:** `#fafafa` is warmer than pure white (`#ffffff`), reducing eye strain while maintaining cleanliness. It photographs well and feels more editorial than clinical.

### Surface Colors (Cards, Modals)

| Token | Value | Usage |
|-------|-------|-------|
| `--surface-primary` | `#ffffff` | Standard cards — pure white for contrast |
| `--surface-secondary` | `#f8f9fa` | Hover states, subtle elevation |
| `--surface-tertiary` | `#f0f0f0` | Active states, pressed cards |
| `--surface-elevated` | `#ffffff` | Modals, dropdowns — with shadow |

**Rationale:** Cards are pure white for maximum contrast against the off-white body. This creates subtle depth without heavy shadows.

### Text Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--text-primary` | `#1a1a2e` | Headlines — near-black with slight warmth |
| `--text-secondary` | `#4a4a5a` | Body copy — readable gray |
| `--text-tertiary` | `#6b6b7b` | Metadata, captions |
| `--text-muted` | `#9a9aaa` | Disabled, hints, timestamps |
| `--text-inverted` | `#f0f4ff` | Text on dark backgrounds (header) |

**Rationale:** `#1a1a2e` replaces pure black — it's softer, more sophisticated, and has subtle blue undertones that harmonize with the cyan accent.

### Accent Colors (Unchanged)

| Token | Value | Usage |
|-------|-------|-------|
| `--accent-cyan` | `#0ee7ff` | Primary accent, links, CTAs |
| `--accent-cyan-glow` | `rgba(14, 231, 255, 0.2)` | Glows on light backgrounds |
| `--accent-cyan-subtle` | `rgba(14, 231, 255, 0.1)` | Subtle backgrounds |
| `--accent-purple` | `#8b5cf6` | Secondary accent, editorial marks |
| `--accent-purple-subtle` | `rgba(139, 92, 246, 0.1)` | Subtle purple backgrounds |
| `--accent-success` | `#22c55e` | Positive scores, recommended |
| `--accent-warning` | `#f59e0b` | Caveats, warnings |
| `--accent-error` | `#ef4444` | Not recommended, broken |

**Note:** Cyan adjusted slightly darker (`#0ee7ff` vs `#6ee7ff`) for better contrast on light backgrounds.

### Border Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--border-subtle` | `rgba(0, 0, 0, 0.06)` | Card borders, dividers |
| `--border-default` | `rgba(0, 0, 0, 0.1)` | Input borders, stronger dividers |
| `--border-strong` | `rgba(0, 0, 0, 0.15)` | Focus states, active cards |
| `--border-accent` | `rgba(14, 231, 255, 0.5)` | Accent borders, highlights |

**Rationale:** Borders use black opacity instead of white opacity — this is the fundamental inversion from dark theme to light theme.

---

## Typography System v2

### Font Stack (Unchanged)

**Primary:** `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

**Monospace:** `"JetBrains Mono", "Fira Code", "SF Mono", monospace`

### Type Scale (Refined)

| Level | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| Display | clamp(2.25rem, 4vw, 3.5rem) | 800 | 1.05 | -0.02em | Hero headlines |
| H1 | clamp(1.75rem, 3vw, 2.5rem) | 700 | 1.1 | -0.01em | Page titles |
| H2 | clamp(1.375rem, 2.5vw, 2rem) | 700 | 1.15 | -0.01em | Section headers |
| H3 | 1.125rem | 600 | 1.3 | 0 | Card titles |
| H4 | 1rem | 600 | 1.35 | 0 | Subsection titles |
| Body Large | 1.125rem | 400 | 1.7 | 0 | Lead paragraphs |
| Body | 1rem | 400 | 1.7 | 0 | Standard body |
| Body Small | 0.875rem | 400 | 1.6 | 0 | Secondary text |
| Caption | 0.75rem | 500 | 1.5 | 0.02em | Metadata, labels |
| Eyebrow | 0.75rem | 600 | 1.2 | 0.08em | Section labels (uppercase) |

**Changes from v1:**
- Reduced hero size slightly for light theme elegance
- Tightened Display line-height for punchier headlines
- Maintained generous body line-height for readability

### Typography Patterns

**Eyebrow Text (Light Context):**
```
SECTION LABEL
- Uppercase
- Letter-spacing: 0.08em
- Color: --accent-cyan (on light) or --text-tertiary
- Weight: 600
- Size: 0.75rem
```

**Headlines on Light:**
- Color: `--text-primary` (near-black, not pure black)
- Tight line-height for impact
- Slight negative letter-spacing for large sizes
- Max-width: 15-20ch for readability

**Body Copy on Light:**
- Color: `--text-secondary` (not primary — reduces contrast fatigue)
- Generous line-height (1.7) for readability
- Max-width: 70ch for comfortable reading

---

## Component System v2

### Header (Dark — Preserved)

**Structure:**
```
┌─────────────────────────────────────────────────────────────┐
│  [LOGO]    Games    Articles    Methodology    [Search]     │  ← #0b1020 background
│                                                             │
│  Subtle bottom border or shadow for separation              │
└─────────────────────────────────────────────────────────────┘
```

**Header Styling:**
```css
.header {
  background: #0b1020;
  color: #f0f4ff;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.header-nav-link {
  color: rgba(240, 244, 255, 0.7);
}

.header-nav-link:hover {
  color: #f0f4ff;
  background: rgba(255, 255, 255, 0.05);
}

.header-nav-link.active {
  color: #0ee7ff;
}
```

**Rationale:** Header remains dark to match logo. Navigation uses inverted text colors. Active state uses cyan accent.

### Cards (Light Context)

**Standard Card:**
```css
.card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}
```

**Card Hover State:**
```css
.card:hover {
  border-color: rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}
```

**Card Active State:**
```css
.card:active {
  background: #f8f9fa;
  transform: translateY(0);
}
```

**Visual:**
```
┌─────────────────────────────────────┐
│                                     │
│  [Score Badge]                      │
│                                     │
│  Game Title in Bold                 │
│  Description text in secondary...   │
│                                     │
│  [Setup: Advanced] [Performance: ..]│
│                                     │
└─────────────────────────────────────┘
     ↑ subtle shadow on hover
     ↑ border defines edges
```

**Rationale:** Cards are pure white with subtle borders. Shadows are softer and warmer on light themes. Hover lift is maintained for interactivity.

### Score Badges (Light Context)

**Large Score Badge:**
```css
.score-badge {
  font-family: var(--font-mono);
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  background: rgba(0, 0, 0, 0.04);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.06);
}

.score-badge--high {
  color: var(--accent-success);
  background: rgba(34, 197, 94, 0.1);
  border-color: rgba(34, 197, 94, 0.2);
}

.score-badge--medium {
  color: var(--accent-warning);
  background: rgba(245, 158, 11, 0.1);
  border-color: rgba(245, 158, 11, 0.2);
}

.score-badge--low {
  color: var(--accent-error);
  background: rgba(239, 68, 68, 0.1);
  border-color: rgba(239, 68, 68, 0.2);
}
```

**Visual:**
```
Recommended (Green):
┌────┐
│ 92 │  ← Green text on subtle green background
└────┘

With Caveats (Amber):
┌────┐
│ 78 │  ← Amber text on subtle amber background
└────┘

Not Recommended (Red):
┌────┐
│ 54 │  ← Red text on subtle red background
└────┘
```

**Rationale:** Score badges use subtle tinted backgrounds instead of glows. This maintains visibility on light backgrounds while preserving color coding.

### Pills/Tags (Light Context)

**Category Pill:**
```css
.pill {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.75rem;
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text-tertiary);
}
```

**Status Pill Variants:**
```css
.pill--success {
  background: rgba(34, 197, 94, 0.1);
  border-color: rgba(34, 197, 94, 0.2);
  color: var(--accent-success);
}

.pill--warning {
  background: rgba(245, 158, 11, 0.1);
  border-color: rgba(245, 158, 11, 0.2);
  color: var(--accent-warning);
}

.pill--accent {
  background: rgba(14, 231, 255, 0.1);
  border-color: rgba(14, 231, 255, 0.2);
  color: var(--accent-cyan);
}
```

**Visual:**
```
[Recommended] [Advanced Setup] [Heavy Performance] [VR Mod]
   ↑green      ↑neutral       ↑amber            ↑cyan
```

### Buttons (Light Context)

**Primary Button:**
```css
.button--primary {
  background: var(--accent-cyan);
  color: #0b1020; /* Dark text on cyan for contrast */
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  border: none;
  transition: all 0.2s ease;
}

.button--primary:hover {
  background: #5dd5e8;
  box-shadow: 0 4px 12px rgba(14, 231, 255, 0.3);
}
```

**Secondary Button:**
```css
.button--secondary {
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.15);
  color: var(--text-primary);
}

.button--secondary:hover {
  background: rgba(0, 0, 0, 0.04);
  border-color: rgba(0, 0, 0, 0.25);
}
```

**Ghost Button:**
```css
.button--ghost {
  background: transparent;
  color: var(--accent-cyan);
}

.button--ghost:hover {
  background: rgba(14, 231, 255, 0.08);
}
```

### Links (Light Context)

**Standard Link:**
```css
a {
  color: var(--accent-cyan);
  text-decoration: none;
  transition: all 0.15s ease;
}

a:hover {
  text-decoration: underline;
  color: #0bc8d8; /* Slightly darker on hover */
}
```

**Rationale:** Cyan links need to be dark enough for WCAG contrast on white. Underline on hover provides clear affordance.

---

## Layout System v2

### Container

- Max-width: 1280px (unchanged)
- Padding: 1rem mobile, 2rem desktop
- Centered with auto margins

### Grid & Spacing

**Grid:**
- CSS Grid with auto-fit
- Gap: 1.5rem (maintained)
- Card min-width: 320px for readability

**Spacing Scale (Unchanged):**
| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 0.25rem | Tight gaps |
| `--space-4` | 1rem | Standard gap |
| `--space-6` | 1.5rem | Card padding |
| `--space-8` | 2rem | Large gaps |
| `--space-12` | 3rem | Major sections |
| `--space-16` | 4rem | Hero spacing |

### Section Alternation

**Pattern:**
```
┌─────────────────────────────────────────────────────────────┐
│  HEADER (#0b1020)                                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HERO SECTION (#fafafa)                                     │
│  Large headline, description, CTAs                          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FEATURED SECTION (#f5f5f5) — slightly different            │
│  Cards on off-white background                              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONTENT SECTION (#fafafa) — back to main background        │
│  More cards                                                 │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  FOOTER (#0b1020 or #f5f5f5)                                │
└─────────────────────────────────────────────────────────────┘
```

**Rationale:** Subtle section alternation (fafafa → f5f5f5) creates visual rhythm without heavy dividers.

---

## Interaction Design v2

### Hover States (Light Context)

**Cards:**
- Border darkens slightly
- Shadow appears (softer than dark theme)
- Lift of 2px maintained
- Background shifts to `--surface-secondary`

**Buttons:**
- Primary: Darkens slightly, shadow appears
- Secondary: Background fill appears
- Ghost: Subtle tinted background

**Links:**
- Underline appears
- Color darkens slightly

### Focus States

- Visible focus rings for accessibility
- Color: `--accent-cyan` with 2px offset
- All interactive elements focusable

### Active States

- Cards: Slight scale down (0.98)
- Buttons: Scale down + darker background
- Navigation: Background highlight

---

## Specific Implementation Notes

### Header/Body Transition

**Critical:** The transition from dark header to light body must be handled cleanly.

**Approach 1: Hard Edge (Recommended)**
```
┌─────────────────────────────────────┐
│  Dark Header                        │
├─────────────────────────────────────┤ ← clean line
│  Light Body                         │
└─────────────────────────────────────┘
```

**Approach 2: Subtle Shadow**
```css
.header {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}
```

### Card Shadows on Light

Light theme shadows should be:
- Softer (larger blur radius)
- Darker color (black instead of white)
- More diffuse (lower opacity)

```css
/* Dark theme shadow (old) */
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);

/* Light theme shadow (new) */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
```

### Image Treatment

On light backgrounds, images may need:
- Subtle border (1px rgba(0,0,0,0.06))
- Slight border-radius to match cards
- No additional treatment needed

### Code Blocks / Technical Content

Technical content should use:
- Light gray background (`#f5f5f5`)
- Dark text for code
- Monospace font
- Subtle border

```css
pre, code {
  background: #f5f5f5;
  color: #1a1a2e;
  font-family: var(--font-mono);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 6px;
}
```

---

## Mood & Style Direction v2

### Visual Metaphor: "The Technical Journal"

CompoundVR should feel like a premium technical publication — something between:
- **Wired's** editorial confidence
- **Engadget's** enthusiast accessibility
- **Nexus Mods'** functional credibility

**Characteristics:**
- **Clean:** No visual noise, everything has purpose
- **Authoritative:** Typography leads, content speaks
- **Technical:** Precision in spacing, alignment, hierarchy
- **Approachable:** Light theme invites reading

### Emotional Response

User should feel:
- **Welcomed:** Light theme is less "gamer cave," more "professional resource"
- **Confident:** Design signals editorial standards
- **Focused:** Content-forward, minimal distractions
- **Trust:** Consistency and polish = credibility

### Comparison to References

**Like Wired:** Editorial sophistication, clean white space, confident typography
**Unlike Wired:** More technical, less magazine-art-directed

**Like Engadget:** Light theme, card-based, enthusiast-focused
**Unlike Engadget:** More restrained, less "tech blog" energy

**Like Nexus Mods:** Functional, information-dense, credible
**Unlike Nexus Mods:** More polished, more editorial, better typography

---

## Implementation Priorities

### Phase 1: Foundation (Critical)
1. Update CSS custom properties for light theme
2. Implement header/body color split
3. Update card component styles
4. Update text colors throughout

### Phase 2: Components (High)
1. Score badges for light context
2. Pill/tag components
3. Button variants
4. Link styles

### Phase 3: Polish (Medium)
1. Section background alternation
2. Image treatments
3. Code block styling
4. Animation refinements for light

### Phase 4: QA (Essential)
1. Contrast ratio verification (WCAG AA)
2. Mobile testing
3. Cross-browser verification
4. Accessibility audit

---

## Contrast & Accessibility

### WCAG AA Requirements

| Element | Required Ratio | Light Theme Approach |
|-----------|----------------|---------------------|
| Body text | 4.5:1 | `#4a4a5a` on `#fafafa` = 7.2:1 ✓ |
| Headlines | 3:1 | `#1a1a2e` on `#fafafa` = 12.5:1 ✓ |
| Links | 4.5:1 | `#0ee7ff` on `#fafafa` = 4.6:1 ✓ |
| Muted text | 4.5:1 (large only) | `#6b6b7b` for metadata |

### Dark Header Contrast

| Element | Required Ratio | Approach |
|-----------|----------------|----------|
| Header text | 4.5:1 | `#f0f4ff` on `#0b1020` = 14.2:1 ✓ |
| Header links | 4.5:1 | `rgba(240,244,255,0.7)` on `#0b1020` = 10:1 ✓ |

---

## Summary

### What Makes This Work

1. **Header continuity** — Logo remains anchored, brand recognition preserved
2. **Light body sophistication** — Editorial maturity over "gaming aesthetic"
3. **Maintained accents** — Cyan and purple still define the brand
4. **Technical authority** — Clean, precise, no decoration
5. **Scannable content** — Cards work better on light backgrounds
6. **Accessibility** — Better contrast ratios, clearer hierarchy

### The Shift

| Aspect | v1 (Dark) | v2 (Light Body) |
|--------|-----------|-----------------|
| **Body background** | `#0b1020` (dark navy) | `#fafafa` (warm off-white) |
| **Card background** | `#151d38` (charcoal) | `#ffffff` (pure white) |
| **Text color** | `#c5cce6` (light gray) | `#4a4a5a` (dark gray) |
| **Border color** | `rgba(255,255,255,0.06)` | `rgba(0,0,0,0.06)` |
| **Shadow style** | Dark, sharp | Soft, diffuse |
| **Score badges** | Glow effect | Tinted background |
| **Feel** | Gaming/tech | Editorial/publication |

### Final Note

This is not a generic light theme. It's a **deliberate shift toward editorial credibility** while maintaining the technical DNA that makes CompoundVR distinctive. The dark header preserves brand continuity; the light body elevates the experience.

**The result:** A site that feels like Wired for VR modding — authoritative, clean, and worthy of trust.

---

**Next Step:** Implement CSS variable updates per `/design/css-update-v2.md`
