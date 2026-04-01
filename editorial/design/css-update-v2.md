# CompoundVR CSS Update v2
## Specific CSS Changes for Light Body Implementation

**Date:** March 18, 2026  
**Author:** Richard (Managing Editor)  
**Status:** Developer Implementation Guide  
**Scope:** Global styles, components, and theme variables

---

## Overview

This document provides the exact CSS changes needed to implement the v2 brand direction. Changes are organized by file/section and marked as **NEW**, **MODIFY**, or **DELETE**.

---

## 1. CSS Custom Properties (Root Variables)

### File: `styles.css` or `variables.css`

**REPLACE the entire color system:**

```css
:root {
  /* ========================================
     COLOR SYSTEM v2 — Light Body, Dark Header
     ======================================== */
  
  /* Background Colors */
  --bg-header: #0b1020;           /* Dark header — matches logo */
  --bg-body: #fafafa;             /* Warm off-white main background */
  --bg-secondary: #f5f5f5;        /* Section alternates */
  --bg-tertiary: #eeeeee;         /* Subtle section backgrounds */
  
  /* Surface Colors (Cards, Modals) */
  --surface-primary: #ffffff;     /* Standard cards */
  --surface-secondary: #f8f9fa;   /* Hover states */
  --surface-tertiary: #f0f0f0;   /* Active states */
  --surface-elevated: #ffffff;    /* Modals, dropdowns */
  
  /* Text Colors — Light Context */
  --text-primary: #1a1a2e;        /* Headlines — near-black */
  --text-secondary: #4a4a5a;      /* Body copy */
  --text-tertiary: #6b6b7b;       /* Metadata, captions */
  --text-muted: #9a9aaa;          /* Disabled, hints */
  
  /* Text Colors — Dark Context (Header) */
  --text-inverted: #f0f4ff;       /* Text on dark backgrounds */
  --text-inverted-secondary: rgba(240, 244, 255, 0.7);
  --text-inverted-tertiary: rgba(240, 244, 255, 0.5);
  
  /* Accent Colors */
  --accent-cyan: #0ee7ff;         /* Primary accent — slightly darker for light */
  --accent-cyan-glow: rgba(14, 231, 255, 0.2);
  --accent-cyan-subtle: rgba(14, 231, 255, 0.1);
  --accent-purple: #8b5cf6;
  --accent-purple-subtle: rgba(139, 92, 246, 0.1);
  --accent-success: #22c55e;
  --accent-warning: #f59e0b;
  --accent-error: #ef4444;
  
  /* Border Colors — Light Context */
  --border-subtle: rgba(0, 0, 0, 0.06);
  --border-default: rgba(0, 0, 0, 0.1);
  --border-strong: rgba(0, 0, 0, 0.15);
  --border-accent: rgba(14, 231, 255, 0.5);
  
  /* Border Colors — Dark Context (Header) */
  --border-inverted: rgba(255, 255, 255, 0.06);
  --border-inverted-default: rgba(255, 255, 255, 0.1);
  
  /* Typography */
  --font-sans: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "SF Mono", monospace;
  
  /* Spacing (Unchanged) */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  
  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-base: 0.2s ease;
  
  /* Shadows — Light Context */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-xl: 0 8px 24px rgba(0, 0, 0, 0.12);
  
  /* Shadows — Dark Context (Header) */
  --shadow-inverted: 0 2px 8px rgba(0, 0, 0, 0.3);
}
```

---

## 2. Global Styles

### File: `styles.css` or `global.css`

**MODIFY body styles:**

```css
/* ========================================
   GLOBAL STYLES
   ======================================== */

/* Body — Light Theme */
body {
  background: var(--bg-body);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Remove dark theme body gradient if present */
/* DELETE: body::before pseudo-element with dark gradients */

/* Selection Color */
::selection {
  background: var(--accent-cyan-subtle);
  color: var(--text-primary);
}
```

**MODIFY typography defaults:**

```css
/* Typography — Light Context */
h1, h2, h3, h4, h5, h6 {
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.2;
}

p {
  color: var(--text-secondary);
  max-width: 70ch;
}

/* Links — Light Context */
a {
  color: var(--accent-cyan);
  text-decoration: none;
  transition: var(--transition-fast);
}

a:hover {
  color: #0bc8d8; /* Slightly darker cyan */
  text-decoration: underline;
}

a:focus-visible {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}
```

---

## 3. Header Component

### File: `header.css` or component styles

**MODIFY header styles:**

```css
/* ========================================
   HEADER — Dark (Preserved from Logo)
   ======================================== */

.header {
  background: var(--bg-header);
  color: var(--text-inverted);
  border-bottom: 1px solid var(--border-inverted);
  position: sticky;
  top: 0;
  z-index: 100;
  /* Optional: subtle shadow for depth */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.header-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-4);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

/* Logo */
.header-logo {
  height: 48px; /* Adjust based on logo dimensions */
  width: auto;
}

/* Navigation — Dark Context */
.header-nav {
  display: flex;
  gap: var(--space-2);
}

.header-nav-link {
  color: var(--text-inverted-secondary);
  font-weight: 500;
  font-size: 0.9rem;
  padding: var(--space-2) var(--space-3);
  border-radius: 6px;
  transition: var(--transition-fast);
}

.header-nav-link:hover {
  color: var(--text-inverted);
  background: rgba(255, 255, 255, 0.05);
  text-decoration: none;
}

.header-nav-link.active {
  color: var(--accent-cyan);
  background: rgba(14, 231, 255, 0.1);
}

.header-nav-link:focus-visible {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}
```

---

## 4. Card Component

### File: `card.css` or component styles

**REPLACE card styles:**

```css
/* ========================================
   CARD — Light Context
   ======================================== */

.card {
  background: var(--surface-primary);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: var(--space-6);
  transition: all var(--transition-base);
  box-shadow: var(--shadow-sm);
}

.card:hover {
  border-color: var(--border-default);
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card:active {
  background: var(--surface-secondary);
  transform: translateY(0);
}

.card:focus-within {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}

/* Card Title */
.card-title {
  color: var(--text-primary);
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: var(--space-2);
}

/* Card Description */
.card-description {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: var(--space-4);
}

/* Card Meta */
.card-meta {
  color: var(--text-tertiary);
  font-size: 0.875rem;
  display: flex;
  gap: var(--space-4);
  align-items: center;
}

/* Card Variants */

.card--featured {
  padding: var(--space-8);
  border-radius: 16px;
}

.card--compact {
  padding: var(--space-4);
}

.card--interactive {
  cursor: pointer;
}

.card--interactive:hover {
  border-color: var(--border-strong);
}
```

---

## 5. Score Badge Component

### File: `score.css` or component styles

**REPLACE score badge styles:**

```css
/* ========================================
   SCORE BADGE — Light Context
   ======================================== */

.score-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 700;
  border-radius: 8px;
  border: 1px solid var(--border-subtle);
  background: rgba(0, 0, 0, 0.04);
  color: var(--text-primary);
}

/* Sizes */
.score-badge--large {
  font-size: 2rem;
  padding: var(--space-3) var(--space-5);
  min-width: 80px;
}

.score-badge--medium {
  font-size: 1.5rem;
  padding: var(--space-2) var(--space-4);
  min-width: 60px;
}

.score-badge--small {
  font-size: 1rem;
  padding: var(--space-1) var(--space-3);
}

/* Score Variants — Color Coded */

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

/* Score Label */
.score-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: var(--space-1);
}

/* Score Container (Badge + Label) */
.score-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
}
```

---

## 6. Pill/Tag Component

### File: `pill.css` or component styles

**REPLACE pill styles:**

```css
/* ========================================
   PILL / TAG — Light Context
   ======================================== */

.pill {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: 0.35rem 0.75rem;
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid var(--border-subtle);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text-tertiary);
  white-space: nowrap;
}

/* Pill Variants */

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

.pill--error {
  background: rgba(239, 68, 68, 0.1);
  border-color: rgba(239, 68, 68, 0.2);
  color: var(--accent-error);
}

.pill--accent {
  background: var(--accent-cyan-subtle);
  border-color: rgba(14, 231, 255, 0.2);
  color: #0bc8d8; /* Darker cyan for text */
}

.pill--purple {
  background: var(--accent-purple-subtle);
  border-color: rgba(139, 92, 246, 0.2);
  color: var(--accent-purple);
}

/* Pill with Icon */
.pill-icon {
  width: 12px;
  height: 12px;
  opacity: 0.8;
}
```

---

## 7. Button Component

### File: `button.css` or component styles

**REPLACE button styles:**

```css
/* ========================================
   BUTTON — Light Context
   ======================================== */

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all var(--transition-base);
  text-decoration: none;
}

.button:focus-visible {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}

/* Primary Button */
.button--primary {
  background: var(--accent-cyan);
  color: #0b1020; /* Dark text for contrast */
}

.button--primary:hover {
  background: #5dd5e8;
  box-shadow: 0 4px 12px rgba(14, 231, 255, 0.3);
  text-decoration: none;
}

.button--primary:active {
  background: #4cc5d8;
  transform: scale(0.98);
}

/* Secondary Button */
.button--secondary {
  background: transparent;
  border: 1px solid var(--border-default);
  color: var(--text-primary);
}

.button--secondary:hover {
  background: rgba(0, 0, 0, 0.04);
  border-color: var(--border-strong);
  text-decoration: none;
}

.button--secondary:active {
  background: rgba(0, 0, 0, 0.08);
}

/* Ghost Button */
.button--ghost {
  background: transparent;
  color: var(--accent-cyan);
  padding: var(--space-2) var(--space-3);
}

.button--ghost:hover {
  background: var(--accent-cyan-subtle);
  text-decoration: none;
}

/* Button Sizes */
.button--small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.button--large {
  padding: 1rem 2rem;
  font-size: 1rem;
}

/* Button with Icon */
.button-icon {
  width: 16px;
  height: 16px;
}
```

---

## 8. Section Styles

### File: `sections.css` or component styles

**ADD section background alternation:**

```css
/* ========================================
   SECTIONS — Light Context with Alternation
   ======================================== */

.section {
  padding: var(--space-12) 0;
}

.section--alt {
  background: var(--bg-secondary);
}

.section--dark {
  background: var(--bg-header);
  color: var(--text-inverted);
}

.section--dark h2,
.section--dark h3 {
  color: var(--text-inverted);
}

.section--dark p {
  color: var(--text-inverted-secondary);
}

/* Container */
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-4);
}

@media (min-width: 640px) {
  .container {
    padding: 0 var(--space-8);
  }
}
```

---

## 9. Hero Section

### File: `hero.css` or component styles

**MODIFY hero styles:**

```css
/* ========================================
   HERO — Light Context
   ======================================== */

.hero {
  padding: var(--space-16) 0;
  background: var(--bg-body);
  text-align: center;
}

.hero-eyebrow {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-cyan);
  margin-bottom: var(--space-4);
}

.hero-title {
  font-size: clamp(2.25rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  margin-bottom: var(--space-6);
  max-width: 20ch;
  margin-left: auto;
  margin-right: auto;
}

.hero-description {
  font-size: 1.125rem;
  color: var(--text-secondary);
  max-width: 60ch;
  margin: 0 auto var(--space-8);
  line-height: 1.7;
}

.hero-ctas {
  display: flex;
  gap: var(--space-4);
  justify-content: center;
  flex-wrap: wrap;
}
```

---

## 10. Footer

### File: `footer.css` or component styles

**OPTION A: Light Footer (Recommended)**

```css
/* ========================================
   FOOTER — Light Context
   ======================================== */

.footer {
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-subtle);
  padding: var(--space-12) 0 var(--space-8);
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-8);
  margin-bottom: var(--space-8);
}

.footer-column h4 {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-4);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.footer-link {
  display: block;
  color: var(--text-tertiary);
  font-size: 0.875rem;
  padding: var(--space-1) 0;
}

.footer-link:hover {
  color: var(--text-secondary);
}

.footer-bottom {
  border-top: 1px solid var(--border-subtle);
  padding-top: var(--space-6);
  text-align: center;
  color: var(--text-muted);
  font-size: 0.875rem;
}
```

**OPTION B: Dark Footer (Alternative)**

```css
.footer {
  background: var(--bg-header);
  color: var(--text-inverted-secondary);
}

.footer h4 {
  color: var(--text-inverted);
}

.footer-link {
  color: var(--text-inverted-tertiary);
}

.footer-link:hover {
  color: var(--text-inverted);
}
```

---

## 11. Form Elements

### File: `forms.css` or component styles

**MODIFY form styles:**

```css
/* ========================================
   FORMS — Light Context
   ======================================== */

.input,
.textarea,
.select {
  width: 100%;
  padding: 0.75rem 1rem;
  background: var(--surface-primary);
  border: 1px solid var(--border-default);
  border-radius: 8px;
  font-size: 1rem;
  color: var(--text-primary);
  transition: all var(--transition-fast);
}

.input::placeholder,
.textarea::placeholder {
  color: var(--text-muted);
}

.input:hover,
.textarea:hover,
.select:hover {
  border-color: var(--border-strong);
}

.input:focus,
.textarea:focus,
.select:focus {
  outline: none;
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 3px var(--accent-cyan-subtle);
}

.label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.label-required::after {
  content: '*';
  color: var(--accent-error);
  margin-left: var(--space-1);
}
```

---

## 12. Code Blocks

### File: `code.css` or component styles

**ADD code block styles:**

```css
/* ========================================
   CODE — Light Context
   ======================================== */

pre {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: var(--space-4);
  overflow-x: auto;
  margin: var(--space-6) 0;
}

code {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  color: var(--text-primary);
}

/* Inline code */
:not(pre) > code {
  background: rgba(0, 0, 0, 0.04);
  padding: 0.2em 0.4em;
  border-radius: 4px;
  font-size: 0.9em;
}
```

---

## 13. Utility Classes

### File: `utilities.css`

**ADD/UPDATE utility classes:**

```css
/* ========================================
   UTILITY CLASSES
   ======================================== */

/* Text Colors */
.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-tertiary { color: var(--text-tertiary); }
.text-muted { color: var(--text-muted); }
.text-inverted { color: var(--text-inverted); }
.text-accent { color: var(--accent-cyan); }
.text-success { color: var(--accent-success); }
.text-warning { color: var(--accent-warning); }
.text-error { color: var(--accent-error); }

/* Background Colors */
.bg-body { background: var(--bg-body); }
.bg-secondary { background: var(--bg-secondary); }
.bg-header { background: var(--bg-header); }
.bg-surface { background: var(--surface-primary); }

/* Border Colors */
.border-subtle { border-color: var(--border-subtle); }
.border-default { border-color: var(--border-default); }
.border-strong { border-color: var(--border-strong); }

/* Shadows */
.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow-md { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }
```

---

## 14. Responsive Adjustments

### File: `responsive.css` or media queries

**UPDATE responsive styles:**

```css
/* ========================================
   RESPONSIVE — Light Context
   ======================================== */

/* Mobile Adjustments */
@media (max-width: 639px) {
  .header-container {
    height: 64px;
  }
  
  .header-logo {
    height: 36px;
  }
  
  .card {
    padding: var(--space-4);
  }
  
  .hero {
    padding: var(--space-10) 0;
  }
  
  .hero-title {
    font-size: 2rem;
  }
}

/* Tablet */
@media (min-width: 640px) and (max-width: 1023px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

## 15. Dark Mode Support (Optional)

### File: `dark-mode.css` (if supporting both themes)

**ADD dark mode media query:**

```css
/* ========================================
   DARK MODE (Optional — System Preference)
   ======================================== */

@media (prefers-color-scheme: dark) {
  :root {
    /* Revert to dark theme colors */
    --bg-body: #0b1020;
    --bg-secondary: #0f1528;
    --surface-primary: #151d38;
    --surface-secondary: #1a2342;
    --text-primary: #f0f4ff;
    --text-secondary: #c5cce6;
    --text-tertiary: #8b92b8;
    --border-subtle: rgba(255, 255, 255, 0.06);
    --border-default: rgba(255, 255, 255, 0.1);
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
    --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.2);
  }
}
```

**Note:** This is optional. The v2 direction is light-body-first.

---

## Implementation Checklist

### Phase 1: Variables & Global
- [ ] Replace CSS custom properties
- [ ] Update body background and text colors
- [ ] Update link styles
- [ ] Update selection color

### Phase 2: Layout
- [ ] Update header styles (keep dark)
- [ ] Update section backgrounds
- [ ] Update container padding if needed

### Phase 3: Components
- [ ] Update card component
- [ ] Update score badges
- [ ] Update pills/tags
- [ ] Update buttons
- [ ] Update forms

### Phase 4: Content
- [ ] Update hero section
- [ ] Update footer
- [ ] Update code blocks
- [ ] Update any custom components

### Phase 5: Polish
- [ ] Add utility classes
- [ ] Update responsive styles
- [ ] Test hover/focus states
- [ ] Verify contrast ratios

---

## Testing Checklist

### Visual
- [ ] Header remains dark with logo
- [ ] Body is warm off-white (`#fafafa`)
- [ ] Cards are pure white with subtle borders
- [ ] Text is dark gray, not pure black
- [ ] Links are cyan and underlined on hover
- [ ] Score badges have tinted backgrounds
- [ ] Pills have appropriate contrast

### Interaction
- [ ] Card hover lifts and shows shadow
- [ ] Button hover shows appropriate feedback
- [ ] Focus states are visible
- [ ] Active states provide tactile feedback

### Responsive
- [ ] Mobile layout works
- [ ] Tablet layout works
- [ ] Desktop layout works
- [ ] Touch targets are 44px minimum

### Accessibility
- [ ] WCAG AA contrast ratios met
- [ ] Focus indicators visible
- [ ] Reduced motion respected
- [ ] Screen reader tested

---

## Quick Reference: Color Mapping

| Old (Dark) | New (Light Body) |
|------------|------------------|
| `#0b1020` body | `#fafafa` body |
| `#0b1020` header | `#0b1020` header (unchanged) |
| `#151d38` cards | `#ffffff` cards |
| `#c5cce6` body text | `#4a4a5a` body text |
| `#f0f4ff` headlines | `#1a1a2e` headlines |
| `rgba(255,255,255,0.06)` borders | `rgba(0,0,0,0.06)` borders |
| Glow effects on scores | Tinted backgrounds on scores |
| Dark shadows | Soft, diffuse shadows |

---

## Notes for Developer

1. **Header is the exception** — it stays dark to match the logo. All other components shift to light theme.

2. **Border opacity** — This is the key change. Dark theme uses `rgba(255,255,255,0.06)`; light theme uses `rgba(0,0,0,0.06)`.

3. **Score badges** — Remove glow effects. Use subtle tinted backgrounds instead (`rgba(color, 0.1)`).

4. **Shadows** — Light theme shadows are softer and more diffuse. Use `0 4px 12px rgba(0,0,0,0.08)` instead of `0 8px 24px rgba(0,0,0,0.2)`.

5. **Cyan accent** — Adjusted from `#6ee7ff` to `#0ee7ff` for better contrast on white.

6. **Test the transition** — The header-to-body transition should be clean. Consider a subtle shadow on the header for separation.

---

**Questions?** Refer to `/design/compoundvr-brand-direction-v2.md` for full rationale and design principles.
