# CompoundVR Style Tile Concepts
## Visual Reference Guide

**Date:** March 18, 2026  
**Purpose:** Descriptive mood board for brand direction implementation

---

## Overview

Since image generation is unavailable, this document describes the visual concepts in detail that would typically be represented in a mood board or style tile. These descriptions can guide implementation and serve as reference for future visual asset creation.

---

## Style Tile A: "The Technical Manual"

### Concept
Clean, precise, engineered. Like a well-designed spec sheet or technical documentation. Everything has a purpose. No decoration.

### Visual Description

**Color Palette:**
- Deep navy background (#0b1020) — like a monitor in a dark room
- Cards in slightly elevated charcoal (#151d38)
- Cyan accent (#6ee7ff) — like an LED status indicator
- Text in soft white (#f0f4ff) — not harsh, comfortable to read
- Subtle borders (6% white opacity) — barely visible separators

**Textures/Materials:**
- Matte surfaces — no gloss, no reflections
- Subtle noise/grain at 2-3% opacity for depth
- Clean edges, no rounded corners on major containers
- Card corners: 12-16px radius (substantial but not bubbly)

**Typography Mood:**
- Inter font, tight tracking on headlines
- Monospace for data — like reading system specs
- Clear hierarchy: you know instantly what's a headline vs. body
- Generous line-height — breathing room for reading

**Imagery Treatment:**
- Game screenshots with consistent treatment
- Subtle darkening gradient on images
- No borders on images — let them bleed to card edges
- Optional: slight desaturation for cohesive look

**Layout Principles:**
- Generous whitespace — content needs room to breathe
- Strong grid alignment — everything snaps to columns
- Asymmetric balance — not rigidly centered
- Z-depth through layering, not shadows

**Reference Touchpoints:**
- Minimalist engineering documentation
- High-end audio equipment interfaces
- Flight instrument panels (clean, precise)
- Contemporary technical publications

---

## Style Tile B: "The Editorial Authority"

### Concept
Confident editorial presence. Bold but not loud. Authority without arrogance.

### Visual Description

**Color Palette:**
- Same deep navy base
- Purple accent (#8b5cf6) plays larger role
- Gradient accents on featured cards — subtle purple-to-cyan
- Text hierarchy through color (primary, secondary, muted)
- Success states in green glow

**Textures/Materials:**
- Subtle gradients on hero sections
- Cards have depth through layer differences
- Hover states have "lift" with soft shadows
- Glass-morphism on header (backdrop blur)

**Typography Mood:**
- Bold headlines with tight leading
- Display weight used for hero headlines (800 weight)
- Italics for pull quotes and emphasis
- Author bylines prominent — personality matters

**Imagery Treatment:**
- Large hero images with gradient overlays
- Featured cards have image + text balance
- Screenshots captioned with technical context
- Thumbnail grids for related content

**Layout Principles:**
- Editorial weighting — featured content gets prominence
- Breaking the grid occasionally for emphasis
- Content zones clearly defined
- Reading paths clearly guided

**Reference Touchpoints:**
- The Verge (bold typography)
- Wired (editorial sophistication)
- High-end gaming publications
- Contemporary digital magazines

---

## Style Tile C: "The Tool Interface"

### Concept
Functional first. Like a professional tool or dashboard. Information density without clutter.

### Visual Description

**Color Palette:**
- Darker background — almost black (#080c18)
- Surface layers more distinct
- Status colors prominent (green/yellow/red for scores)
- Accent cyan for interactive elements
- Data visualization friendly

**Textures/Materials:**
- Flat design with layered elevation
- Borders define hierarchy (visible but subtle)
- No gradients — solid colors only
- Grid lines optional for data-heavy sections

**Typography Mood:**
- Monospace for scores and technical data
- Sans-serif for everything else
- Tabular numbers aligned
- Compact but readable

**Imagery Treatment:**
- Thumbnail-first approach
- Screenshots in consistent aspect ratio
- Optional: play button overlays for video
- Gallery grids for multiple images

**Layout Principles:**
- Data table aesthetics for game listings
- Filter/sort controls prominent
- Comparison layouts side-by-side
- Information density optimized for scanning

**Reference Touchpoints:**
- GitHub interface
- Developer documentation sites
- Dashboard UIs
- Technical comparison tools

---

## Recommended Direction: Hybrid A + B

### The "Technical Authority" Approach

**Primary Character:** Style Tile A (Technical Manual)
- Clean, precise, no decoration
- Respect for the content
- Trust through restraint

**Secondary Character:** Style Tile B (Editorial Authority)
- Bold when needed (hero sections)
- Editorial personality
- Authoritative voice

**Rejects:** Style Tile C (Tool Interface)
- Too utilitarian for editorial content
- Good for future "mod tools" but not main site

---

## Component-Specific Concepts

### Navigation Bar

**Concept:** Floating command bar
- Sticky on scroll
- Backdrop blur (glass effect)
- Logo prominent but not overwhelming
- Links subtle until hover

**Visual:**
```
[LOGO]    Games  Articles  Methodology    [Search icon]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         ↑ subtle border
    blur backdrop
```

### Game Cards

**Concept:** Information-dense but scannable
- Large click target
- Score prominently displayed
- Verdict as pull quote
- Metadata in pill format

**Visual:**
```
┌─────────────────────────────┐
│  [Score: 92]                │
│                             │
│  Game Title                 │
│  Two-line description...    │
│                             │
│  [Setup: Beginner] [Perf: ..]│
│  Recommended · FPS · Action │
└─────────────────────────────┘
```

### Score Badge Variations

**Recommended (Green glow):**
```
    ╭──────╮
    │  92  │  ← Cyan or white, high contrast
    ╰──────╯
   Excellent
```

**Caution (Yellow glow):**
```
    ╭──────╮
    │  78  │  ← Yellow/amber
    ╰──────╯
   With Caveats
```

**Not Recommended (Red/gray):**
```
    ╭──────╮
    │  54  │  ← Muted, less glow
    ╰──────╯
   Wait for Updates
```

### Hero Section

**Concept:** Statement of purpose
- Large but not overwhelming headline
- Subtle gradient text effect
- Clear value proposition
- Trust badges below (methodology, editorial standards)

**Visual:**
```
    AUTHORITY SITE FOR FLAT-TO-VR PLAYERS
    ═══════════════════════════════════════
    
    Find the best path to play
    flat games in VR.
    
    [Description paragraph]
    
    [Pill] [Pill] [Pill]
```

### Metadata Pills

**Concept:** Quick-scan information
- Consistent sizing
- Icon + text where appropriate
- Color-coded by severity
- Rounded (pill shape)

**Visual:**
```
[🟢 Recommended] [⚙️ Advanced Setup] [💻 Heavy Demand]
```

---

## Color Application Guide

### When to Use Cyan (#6ee7ff)
- Primary CTAs
- Links
- Active navigation states
- Highest scores (90+)
- Brand moments (logo, hero)
- Interactive feedback

### When to Use Purple (#8b5cf6)
- Secondary CTAs
- Editorial badges ("Editor's Pick")
- Category labels
- Blockquotes
- Alternative to cyan for variety

### When to Use Green/Yellow/Red
- Scores/status only
- Semantic meaning (recommended/caution/error)
- Never for decoration
- Never for primary brand moments

### Background Layers
- **Primary (#0b1020):** Page background
- **Secondary (#0f1528):** Section backgrounds, footer
- **Surface Primary (#151d38):** Cards, containers
- **Surface Secondary (#1a2342):** Hover states, elevated

---

## Typography Application

### Display/Hero Text
- Size: 40-64px (responsive)
- Weight: 800 (Extra Bold)
- Use: Homepage headline, major page titles
- Treatment: Optional subtle gradient text

### Headline H1
- Size: 32-48px (responsive)
- Weight: 700 (Bold)
- Use: Page titles, major section headers
- Treatment: Solid color, tight line-height

### Headline H2
- Size: 24-36px (responsive)
- Weight: 700 (Bold)
- Use: Section headers
- Treatment: Often paired with eyebrow text

### Headline H3 (Card Titles)
- Size: 20px
- Weight: 600 (Semi-bold)
- Use: Card titles, subsection headers
- Treatment: Single line with truncation

### Body Text
- Size: 16-18px
- Weight: 400 (Regular)
- Line-height: 1.7
- Use: Article content, descriptions
- Treatment: Max-width 70ch for readability

### Caption/Meta
- Size: 12-14px
- Weight: 400-500
- Use: Dates, authors, metadata
- Treatment: Muted color

---

## Animation Concepts

### Page Load
- Fade in from opacity 0
- Slight translateY (10px → 0)
- Stagger cards by 50ms each
- Duration: 300ms
- Easing: ease-out

### Card Hover
- Transform: translateY(-2px)
- Shadow: appears/grows
- Border: lightens
- Background: shifts to surface-secondary
- Duration: 200ms
- Easing: ease

### Button Hover
- Background: lightens 10%
- Box-shadow: glow appears (accent color at 15% opacity)
- Transform: scale(1.02) — subtle
- Duration: 150ms

### Link Hover
- Color: brightens
- Text-decoration: underline appears
- Optional: slight translateX for arrow icons
- Duration: 150ms

### Scroll Behavior
- Smooth scroll for anchor links
- Header: backdrop blur increases on scroll
- Cards: optional parallax on hero images

---

## Responsive Behavior

### Desktop (>1024px)
- Full layout with generous whitespace
- Multi-column grids
- Expanded navigation
- Large hero text

### Tablet (640-1024px)
- Reduced spacing
- Two-column grids
- Collapsed navigation (hamburger or horizontal scroll)
- Adjusted hero size

### Mobile (<640px)
- Single column
- Stacked header (logo above nav)
- Reduced padding
- Touch-optimized targets (44px minimum)
- Collapsible sections

---

## Implementation Reference

### CSS Structure
```css
/* Tokens */
:root {
  /* Colors */
  --color-bg-primary: #0b1020;
  --color-bg-secondary: #0f1528;
  --color-surface-primary: #151d38;
  /* etc. */
  
  /* Typography */
  --font-sans: Inter, system-ui, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-4: 1rem;
  /* etc. */
}

/* Components */
.card { /* ... */ }
.card:hover { /* ... */ }

.button { /* ... */ }
.button--primary { /* ... */ }

.score-badge { /* ... */ }
.score-badge--high { /* ... */ }
```

### Component Checklist
- [ ] Color system with CSS variables
- [ ] Typography scale
- [ ] Card component with variants
- [ ] Button component with variants
- [ ] Pill/tag component
- [ ] Score badge component
- [ ] Navigation header
- [ ] Footer
- [ ] Hero section
- [ ] Content grid
- [ ] Article layout
- [ ] Game detail page layout

---

## Final Notes

This style tile represents a direction that balances:

1. **Technical credibility** — clean, precise, engineered
2. **Editorial authority** — confident, distinctive, trustworthy
3. **User respect** — no visual noise, information-forward

The existing CompoundVR logo (v5) anchors this system. The design should amplify its authority without competing for attention.

**Remember:** Design is finished not when there's nothing more to add, but when there's nothing left to remove.
