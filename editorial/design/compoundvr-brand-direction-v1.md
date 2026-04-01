# CompoundVR Brand Direction v1
## Visual System & Design Language Proposal

**Date:** March 18, 2026  
**Author:** Richard (Managing Editor)  
**Status:** Proposal for review  
**Constraint:** Existing logo (v5) remains unchanged

---

## Executive Summary

CompoundVR needs a visual system that communicates **editorial authority and technical credibility** to a skeptical enthusiast audience. Based on research into VR media and modern gaming publications (2024-2025), this proposal moves the brand toward **sophisticated restraint** — a system that feels engineered rather than decorated.

**Core Principle:** The design should make the content feel trustworthy, not make the site feel "designed."

---

## Current State Assessment

### What's Working
- Dark navy background (#0b1020) — sophisticated, not harsh
- Cyan accent (#6ee7ff) — appropriate for tech/VR space
- Purple secondary (#8b5cf6) — adds editorial distinction
- Inter typography — modern, readable, appropriate
- Card-based layout — scannable, modern
- 1120px max-width — good readability

### What's Missing/Needs Refinement
- **No distinct visual hierarchy** — everything feels same-weight
- **Surface system lacks depth** — cards feel flat
- **Typography scale needs tuning** — hero text too large, body too small
- **Interaction states underdeveloped** — hover, focus, active not defined
- **Component patterns inconsistent** — pills, tags, scores need system
- **Mobile navigation feels cramped** — needs rethinking
- **No dark theme sophistication** — missing layered surface system

---

## Brand Positioning

### What CompoundVR Is
- **Decision database** — helps users choose whether to pursue a VR mod
- **Technical authority** — honest about setup complexity and performance
- **Evergreen resource** — canonical game pages, not just news cycle

### What CompoundVR Is Not
- **Tech hype machine** — no vaporware, no overstated claims
- **Generic gaming blog** — depth over breadth
- **Community forum** — editorial voice, not crowd-sourced

### Personality Traits
- **Confident** — knows what it's talking about
- **Honest** — upfront about limitations and caveats
- **Precise** — specific language, specific data
- **Restrained** — no visual noise, no decoration for decoration's sake

---

## Visual System

### Color System

#### Core Palette

**Backgrounds:**
| Token | Value | Usage |
|-------|-------|-------|
| `--bg-primary` | `#0b1020` | Main page background |
| `--bg-secondary` | `#0f1528` | Elevated sections, footer |
| `--bg-tertiary` | `#131a30` | Card backgrounds, containers |

**Surfaces (Cards, Modals, Overlays):**
| Token | Value | Usage |
|-------|-------|-------|
| `--surface-primary` | `#151d38` | Standard cards |
| `--surface-secondary` | `#1a2342` | Hover states, elevated cards |
| `--surface-tertiary` | `#1e284c` | Active states, focused cards |

**Text Colors:**
| Token | Value | Usage |
|-------|-------|-------|
| `--text-primary` | `#f0f4ff` | Headlines, important text |
| `--text-secondary` | `#c5cce6` | Body copy |
| `--text-tertiary` | `#8b92b8` | Metadata, captions |
| `--text-muted` | `#5a6280` | Disabled, hints |

**Accent Colors:**
| Token | Value | Usage |
|-------|-------|-------|
| `--accent-cyan` | `#6ee7ff` | Primary accent, links, CTAs |
| `--accent-cyan-glow` | `rgba(110, 231, 255, 0.15)` | Subtle glows, borders |
| `--accent-purple` | `#8b5cf6` | Secondary accent, editorial marks |
| `--accent-purple-glow` | `rgba(139, 92, 246, 0.15)` | Subtle glows |
| `--accent-success` | `#4ade80` | Positive scores, recommended |
| `--accent-warning` | `#fbbf24` | Caveats, warnings |
| `--accent-error` | `#f87171` | Not recommended, broken |

**Borders:**
| Token | Value | Usage |
|-------|-------|-------|
| `--border-subtle` | `rgba(255, 255, 255, 0.06)` | Card borders |
| `--border-default` | `rgba(255, 255, 255, 0.1)` | Input borders, dividers |
| `--border-strong` | `rgba(255, 255, 255, 0.15)` | Focus states, active cards |

#### Color Usage Guidelines

**Primary Accent (Cyan):**
- Links and interactive elements
- Primary CTAs
- Active navigation states
- Score highlights for top-tier content
- Use sparingly — 5-10% of UI surface maximum

**Secondary Accent (Purple):**
- Editorial badges ("Editor's Pick", "Essential")
- Category labels
- Blockquote borders
- Alternative to cyan for variety

**Semantic Colors:**
- **Green:** Scores 85+, "Recommended", "Fully Playable"
- **Yellow:** Scores 70-84, "Recommended with Caveats", "Moderate"
- **Red:** Scores <70, "Not Recommended", "Broken"

**Surface Layering:**
Background → Cards → Elevated Cards → Modals/Overlays
Each level 2-4% lighter than the previous

---

### Typography System

#### Font Stack

**Primary:** `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

**Monospace (for technical data):** `"JetBrains Mono", "Fira Code", "SF Mono", monospace`

**Rationale:** Inter is already in use and appropriate. Adding JetBrains Mono for technical metadata (scores, specs, compatibility data) adds subtle differentiation and credibility.

#### Type Scale

| Level | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| Display | clamp(2.5rem, 5vw, 4rem) | 800 | 1.05 | -0.02em | Hero headlines |
| H1 | clamp(2rem, 4vw, 3rem) | 700 | 1.1 | -0.01em | Page titles |
| H2 | clamp(1.5rem, 3vw, 2.25rem) | 700 | 1.15 | -0.01em | Section headers |
| H3 | 1.25rem | 600 | 1.3 | 0 | Card titles |
| H4 | 1.125rem | 600 | 1.35 | 0 | Subsection titles |
| Body Large | 1.125rem | 400 | 1.7 | 0 | Lead paragraphs |
| Body | 1rem | 400 | 1.7 | 0 | Standard body |
| Body Small | 0.875rem | 400 | 1.6 | 0 | Secondary text |
| Caption | 0.75rem | 500 | 1.5 | 0.02em | Metadata, labels |
| Eyebrow | 0.75rem | 600 | 1.2 | 0.08em | Section labels (uppercase) |

#### Typography Patterns

**Eyebrow Text:**
```
Section Label
- Uppercase
- Small caps spacing (letter-spacing: 0.08em)
- Cyan or purple accent color
- Weight: 600
```

**Headlines:**
- Tight line-height (1.05-1.15) for impact
- Slight negative letter-spacing for large sizes
- Max-width constraint (15-20ch) for readability

**Body Copy:**
- Generous line-height (1.7) for readability
- Max-width: 70ch for comfortable reading
- Color: text-secondary (not pure white)

**Technical Data:**
- Monospace font
- Tabular numbers (font-variant-numeric: tabular-nums)
- Slightly smaller size (0.9em)

---

### Layout System

#### Grid & Spacing

**Container:**
- Max-width: 1280px (increased from 1120px for better content density)
- Padding: 1rem mobile, 2rem desktop
- Centered with auto margins

**Grid:**
- CSS Grid with auto-fit
- Gap: 1.5rem (increased from 1rem for breathing room)
- Card min-width: 320px for readability

**Spacing Scale:**
| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 0.25rem | Tight gaps |
| `--space-2` | 0.5rem | Inline spacing |
| `--space-3` | 0.75rem | Component internal |
| `--space-4` | 1rem | Standard gap |
| `--space-5` | 1.25rem | Card padding |
| `--space-6` | 1.5rem | Section gaps |
| `--space-8` | 2rem | Large gaps |
| `--space-10` | 2.5rem | Section padding |
| `--space-12` | 3rem | Major sections |
| `--space-16` | 4rem | Hero spacing |

#### Breakpoints

| Name | Width | Changes |
|------|-------|---------|
| Mobile | < 640px | Single column, stacked nav, reduced typography |
| Tablet | 640px - 1024px | Two-column grid, adjusted spacing |
| Desktop | 1024px - 1280px | Full layout, three-column grid |
| Large | > 1280px | Max container width, generous whitespace |

---

### Component System

#### Cards

**Standard Card:**
```css
background: var(--surface-primary);
border: 1px solid var(--border-subtle);
border-radius: 16px;
padding: 1.5rem;
transition: all 0.2s ease;
```

**Card Hover State:**
```css
background: var(--surface-secondary);
border-color: var(--border-default);
transform: translateY(-2px);
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
```

**Card Variants:**
- **Featured:** Larger padding (2rem), subtle gradient overlay
- **Compact:** Reduced padding (1rem), smaller typography
- **Interactive:** Full click target, cursor pointer, hover lift

#### Buttons

**Primary Button:**
```css
background: var(--accent-cyan);
color: var(--bg-primary);
padding: 0.75rem 1.5rem;
border-radius: 8px;
font-weight: 600;
transition: all 0.2s ease;
```

**Button Hover:**
```css
background: #8eedff; /* slightly lighter */
box-shadow: 0 0 20px var(--accent-cyan-glow);
```

**Secondary Button:**
```css
background: transparent;
border: 1px solid var(--border-default);
color: var(--text-primary);
```

**Ghost Button:**
```css
background: transparent;
color: var(--accent-cyan);
padding: 0.5rem 1rem;
```

#### Pills/Tags

**Category Pill:**
```css
display: inline-flex;
align-items: center;
padding: 0.35rem 0.75rem;
background: var(--surface-secondary);
border: 1px solid var(--border-subtle);
border-radius: 999px;
font-size: 0.75rem;
font-weight: 500;
color: var(--text-tertiary);
```

**Status Pill (Score):**
```css
/* Variant: recommended */
background: rgba(74, 222, 128, 0.1);
border-color: rgba(74, 222, 128, 0.3);
color: var(--accent-success);

/* Variant: caveat */
background: rgba(251, 191, 36, 0.1);
border-color: rgba(251, 191, 36, 0.3);
color: var(--accent-warning);
```

#### Score Display

**Large Score Badge:**
```css
font-family: var(--font-mono);
font-size: 2.5rem;
font-weight: 700;
color: var(--accent-cyan);
text-shadow: 0 0 30px var(--accent-cyan-glow);
```

**Score with Label:**
```
[Score: 92]  — Large, prominent
Excellent    — Label below, muted
```

#### Navigation

**Desktop Navigation:**
- Sticky header with `backdrop-filter: blur(20px)`
- Background: `rgba(11, 16, 32, 0.85)`
- Border-bottom: `1px solid var(--border-subtle)`
- Height: 72px

**Navigation Links:**
```css
color: var(--text-tertiary);
font-weight: 500;
font-size: 0.9rem;
padding: 0.5rem 0.75rem;
border-radius: 6px;
transition: all 0.15s ease;
```

**Nav Link Hover:**
```css
color: var(--text-primary);
background: var(--surface-primary);
```

**Nav Link Active:**
```css
color: var(--accent-cyan);
background: rgba(110, 231, 255, 0.1);
```

**Mobile Navigation:**
- Full-width logo centered above nav
- Horizontal scroll or hamburger menu
- Touch targets minimum 44px
- Simplified navigation items

#### Metadata Display

**Article Meta:**
```
Author Name · Category · Date · Read time
```
- Color: var(--text-tertiary)
- Separator: middle dot (·)
- Font size: 0.875rem

**Game Meta (Structured):**
```
[Setup: Advanced] [Performance: Heavy] [Status: Active]
```
- Pills with icons (optional)
- Color-coded by severity

---

### Interaction Design

#### Hover States
- All interactive elements have visible hover states
- Cards lift slightly (translateY: -2px)
- Links brighten or underline
- Buttons glow subtly
- Transition timing: 0.2s ease

#### Focus States
- Visible focus rings for accessibility
- Color: var(--accent-cyan)
- Offset: 2px
- All interactive elements focusable

#### Active States
- Cards: slightly depressed or color shift
- Buttons: scale(0.98) for tactile feedback
- Navigation: background highlight

#### Loading States
- Skeleton screens for content loading
- Pulsing gradient animation
- Preserve layout to prevent shift

---

## Specific Changes to Current Site

### 1. Global Styles Update

**Current issues:**
- Hero text too large (clamp(2.4rem, 5vw, 4.5rem))
- Pure gradient background on body
- Surface colors not layered

**Proposed changes:**
```css
/* New background approach */
body {
  background: var(--bg-primary);
  color: var(--text-secondary);
}

/* Add subtle texture/gradient */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: 
    radial-gradient(ellipse at 50% 0%, rgba(110, 231, 255, 0.03) 0%, transparent 50%),
    radial-gradient(ellipse at 100% 100%, rgba(139, 92, 246, 0.02) 0%, transparent 40%);
  pointer-events: none;
  z-index: -1;
}
```

### 2. Header/Navigation Redesign

**Current:** Logo height 104px, nav below on mobile
**Proposed:**
- Reduce logo height to 64px desktop, 48px mobile
- Keep sticky behavior
- Add backdrop blur for depth
- Mobile: horizontal nav with scroll, not stacked

### 3. Hero Section Refinement

**Current:** Very large headline, eyebrow text
**Proposed:**
- Reduce headline size to clamp(2.5rem, 5vw, 4rem)
- Add subtle gradient text effect for headline
- Increase lead paragraph max-width and size
- Better spacing hierarchy

### 4. Card System Overhaul

**Current:** Basic card with border
**Proposed:**
- Layered surface system
- Hover lift effect
- Consistent padding (1.5rem)
- Metadata in structured format
- Score badges with visual hierarchy

### 5. Typography Refinements

**Changes:**
- Reduce hero headline size
- Increase body line-height to 1.7
- Add monospace font for technical data
- Standardize eyebrow text pattern

### 6. Score/Verdict Display

**New Component:**
- Large score badge with color coding
- Verdict prominently displayed
- Recommendation status clearly marked
- Link to methodology

### 7. Game Metadata Display

**New Pattern:**
- Structured grid of key attributes
- Icon + label for quick scanning
- Color-coded severity (setup, performance, comfort)
- Collapsible technical details

### 8. Footer Enhancement

**Proposed:**
- Multiple columns on desktop
- Navigation links
- Social/secondary links
- Copyright and attribution

---

## Mood & Style Direction

### Visual Metaphor

**Concept: "The Technical Manual"**

CompoundVR should feel like a well-designed technical reference — something an engineer would use, not something a marketer would create. The aesthetic is:

- **Precise:** Everything aligned, measured, intentional
- **Layered:** Surfaces at different depths, clear hierarchy
- **Illuminated:** Strategic use of accent colors like indicator lights
- **Trustworthy:** No tricks, no hiding, everything accounted for

### Comparison to References

**Like Rock Paper Shotgun:** Distinctive personality, editorial confidence
**Unlike Polygon:** Not magazine-art-directed, more utilitarian
**Like The Verge:** Bold typography, confident layout
**Unlike Eurogamer:** Cleaner, less cluttered
**Like Wired:** Editorial authority
**Unlike UploadVR:** More distinctive visual identity

### Emotional Response

User should feel:
- **Confident:** "These people know what they're talking about"
- **Informed:** "I can find what I need quickly"
- **Respected:** "They don't waste my time with fluff"
- **Trust:** "They'll tell me if something is broken"

---

## Implementation Priorities

### Phase 1: Foundation (High Impact)
1. Update color system with layered surfaces
2. Refine typography scale
3. Redesign card component with hover states
4. Update navigation (header + mobile)

### Phase 2: Components (Medium Impact)
1. Score/verdict display component
2. Game metadata grid
3. Pill/tag system
4. Button styles

### Phase 3: Polish (Lower Impact)
1. Animation refinements
2. Footer redesign
3. Loading states
4. Accessibility improvements

---

## Technical Notes

### CSS Custom Properties

All values should use CSS custom properties for maintainability:

```css
:root {
  /* Colors */
  --bg-primary: #0b1020;
  --bg-secondary: #0f1528;
  --surface-primary: #151d38;
  --surface-secondary: #1a2342;
  --text-primary: #f0f4ff;
  --text-secondary: #c5cce6;
  --text-tertiary: #8b92b8;
  --accent-cyan: #6ee7ff;
  --accent-purple: #8b5cf6;
  
  /* Typography */
  --font-sans: Inter, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
  
  /* Spacing */
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  
  /* Borders */
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-default: rgba(255, 255, 255, 0.1);
  
  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-base: 0.2s ease;
}
```

### Performance Considerations

- Use `will-change` sparingly on animated elements
- Prefer transform/opacity for animations
- Lazy load images below fold
- Use system fonts as fallbacks

### Accessibility Requirements

- WCAG AA contrast ratios (4.5:1 for text)
- Focus visible on all interactive elements
- Reduced motion support via `prefers-reduced-motion`
- Semantic HTML throughout
- Alt text for all images

---

## Appendix: Mood Board Concepts

### Color Relationships
```
Background (#0b1020)
    ↓ 2% lighter
Surface Primary (#151d38) — Cards
    ↓ 3% lighter  
Surface Secondary (#1a2342) — Hover
    ↓ 4% lighter
Surface Tertiary (#1e284c) — Active

Accents:
    Cyan (#6ee7ff) — Links, CTAs, highlights
    Purple (#8b5cf6) — Editorial, secondary
    Green (#4ade80) — Success, recommended
    Yellow (#fbbf24) — Warning, caveats
    Red (#f87171) — Error, not recommended
```

### Typography Hierarchy
```
DISPLAY (Large, tight)
    ↓
H1 (Bold, authoritative)
    ↓
H2 (Section headers)
    ↓
H3 (Card titles)
    ↓
Body Large (Lead text)
    ↓
Body (Standard reading)
    ↓
Caption (Metadata)
    ↓
Eyebrow (Uppercase, spaced)
```

### Card Interaction Flow
```
Default: Surface Primary, subtle border
    ↓ Hover
Surface Secondary, border lightens, lifts 2px, shadow appears
    ↓ Active
Surface Tertiary, slight scale down
    ↓ Focus
Cyan outline ring
```

---

## Conclusion

This brand direction moves CompoundVR toward a visual system that:

1. **Respects the audience** — no hype, no visual noise
2. **Supports the content** — design serves information
3. **Builds trust** — consistency, honesty, precision
4. **Scales well** — system that grows with content
5. **Feels distinctive** — not generic, not following trends

The existing logo (v5) anchors the brand. Everything around it should amplify its authority, not compete for attention.

**Next step:** Review and approve this direction, then implement Phase 1 changes.
