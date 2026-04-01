# CompoundVR Homepage Card Design v1
## Visual Design Specification — Game Cards & Homepage Layout

**Date:** March 22, 2026
**Author:** Maya (Design System)
**Status:** Draft — For Implementation

---

## Executive Summary

The current homepage shows only 2-3 featured games with minimal card metadata. This specification redesigns the CardGrid component to display more games, hero images, tier badges, route type pills, and platform icons — matching the editorial authority established in the brand direction while creating scannable, information-dense cards that respect the "technical authority" aesthetic.

---

## Current Issues

| Issue | Current State | Required State |
|-------|---------------|----------------|
| Game count | Shows 2-3 featured games only | Show 12-16 games, scrollable sections |
| Images | No hero images on cards | Prominent hero image as card visual anchor |
| Tier | Not displayed on cards | Prominent tier badge (S/A/B/C/D/F) |
| Route Type | Text only in meta | Distinctive pill badge |
| Platforms | Not displayed | Icon row showing PCVR, Quest, PSVR, etc. |
| Layout | 2-column grid | 3-4 column responsive grid |
| Hierarchy | Flat card content | Visual hierarchy: image → tier → title → metadata |

---

## Homepage Layout Design

### Section Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HEADER (Dark #0b1020)                                                       │
│  [Logo]    Games    Articles    Methodology                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  HERO SECTION (#fafafa)                                                      │
│  ─────────────────────                                                        │
│  "Find the best path to play flat games in VR"                              │
│  Brief value prop, 2-3 feature pills                                        │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TIER-S FEATURE SECTION (#fafafa or subtle gradient)                         │
│  ─────────────────────────────────                                            │
│  1-2 S-tier games, large feature card treatment                              │
│  Editorial spotlight if applicable                                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ALL VR ROUTES SECTION (#fafafa)                                             │
│  ───────────────────────────────                                             │
│  Filter bar: [All] [Official Hybrid] [Full VR Mod] [Framework] etc.          │
│  Grid of 12-16 game cards                                                    │
│  "View All Games →" CTA                                                      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EDITORIAL SECTION (#f5f5f5 — alternate)                                      │
│  ─────────────────────────────────                                            │
│  Latest articles, reviews, guides                                            │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  FOOTER (#f5f5f5)                                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Grid Behavior

| Breakpoint | Cards per Row | Card Width |
|------------|---------------|------------|
| Mobile (< 640px) | 1 | 100% |
| Tablet (640-1024px) | 2 | 50% |
| Desktop (1024-1440px) | 3 | 33.33% |
| Large (1440px+) | 4 | 25% |

---

## Game Card Component Design

### Card Anatomy

```
┌──────────────────────────────────────────────────┐
│ ┌────────────────────────────────────────────┐ │
│ │                                              │ │
│ │           HERO IMAGE                         │ │
│ │    (16:9 or 4:3 aspect ratio)               │ │
│ │                                              │ │
│ │  ┌────┐ ┌─────────────┐                     │ │
│ │  │ S  │ │ Full VR Mod │  ← Overlay badges   │ │
│ │  └────┘ └─────────────┘                     │ │
│ │                                              │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│  Half-Life 2 in VR                              │  ← Title (h3)
│                                                  │
│  The Half-Life 2 VR Mod Is a Time Machine...   │  ← Verdict excerpt
│                                                  │
│  ┌────┐ ┌──────────┐ ┌─────────────┐            │
│  │PCVR│ │ Beginner │ │ Recommended │            │  ← Metadata pills
│  └────┘ └──────────┘ └─────────────┘            │
│                                                  │
│  Platform Icons: [PCVR] [Quest] [PSVR]           │  ← Platform row
│                                                  │
└──────────────────────────────────────────────────┘
```

### Visual Hierarchy (Top to Bottom)

1. **Hero Image** — Primary visual anchor, creates emotional connection
2. **Tier Badge** — Top-left overlay, high-visibility ranking
3. **Route Type Pill** — Top-right overlay, categorization
4. **Title** — Bold, scannable game name
5. **Verdict/Description** — Brief editorial summary
6. **Metadata Pills** — Setup burden, playability, recommendation
7. **Platform Icons** — At-a-glance platform support

---

## Component Specifications

### Hero Image Container

```css
.game-card__image-container {
  position: relative;
  aspect-ratio: 16 / 9; /* or 4/3 for more vertical cards */
  overflow: hidden;
  border-radius: 8px 8px 0 0;
  background: var(--bg-tertiary); /* #eeeeee — loading state */
}

.game-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.game-card:hover .game-card__image {
  transform: scale(1.02); /* Subtle zoom on hover */
}
```

### Tier Badge (Overlay)

```css
.tier-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  font-family: var(--font-mono);
  font-size: 1.25rem;
  font-weight: 700;
  padding: 0.35rem 0.65rem;
  border-radius: 6px;
  text-shadow: 0 0 20px currentColor;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

/* Tier Colors (from brand system) */
.tier--s {
  color: #f0c674;
  background: rgba(240, 198, 116, 0.15);
  border: 1px solid rgba(240, 198, 116, 0.4);
}

.tier--a {
  color: var(--accent-success);
  background: rgba(34, 197, 94, 0.15);
  border: 1px solid rgba(34, 197, 94, 0.4);
}

.tier--b {
  color: var(--accent-cyan);
  background: rgba(14, 231, 255, 0.15);
  border: 1px solid rgba(14, 231, 255, 0.4);
}

.tier--c {
  color: var(--accent-warning);
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.4);
}

.tier--d {
  color: #f97316;
  background: rgba(249, 115, 22, 0.15);
  border: 1px solid rgba(249, 115, 22, 0.4);
}

.tier--f {
  color: var(--accent-error);
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.4);
}
```

### Route Type Pill (Overlay)

```css
.route-type-pill {
  position: absolute;
  top: 12px;
  right: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.75);
  color: #ffffff;
  backdrop-filter: blur(4px);
}

/* Route Type Variants */
.route-type--official {
  background: rgba(139, 92, 246, 0.85); /* Purple for official */
}

.route-type--full-mod {
  background: rgba(14, 231, 255, 0.85); /* Cyan for community mods */
}

.route-type--framework {
  background: rgba(34, 197, 94, 0.85); /* Green for framework-based */
}

.route-type--driver {
  background: rgba(245, 158, 11, 0.85); /* Amber for injection drivers */
}
```

### Card Body

```css
.game-card {
  background: var(--surface-primary); /* #ffffff */
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.2s ease;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.game-card:hover {
  border-color: var(--border-default);
  box-shadow: var(--shadow-lg);
  transform: translateY(-3px);
}

.game-card__body {
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.game-card__title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.3;
  margin: 0;
}

.game-card__title a {
  color: inherit;
  text-decoration: none;
}

.game-card__title a:hover {
  color: var(--accent-cyan);
}

.game-card__description {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* Limit to 2 lines */
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

### Metadata Pills Row

```css
.game-card__metadata {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: auto; /* Push to bottom of card */
}

.metadata-pill {
  font-size: 0.7rem;
  font-weight: 500;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  background: var(--bg-secondary);
  color: var(--text-tertiary);
  border: 1px solid var(--border-subtle);
}

/* Metadata Variants */
.metadata-pill--setup-beginner {
  background: rgba(34, 197, 94, 0.1);
  color: var(--accent-success);
  border-color: rgba(34, 197, 94, 0.2);
}

.metadata-pill--setup-moderate {
  background: rgba(14, 231, 255, 0.1);
  color: var(--accent-cyan);
  border-color: rgba(14, 231, 255, 0.2);
}

.metadata-pill--setup-advanced {
  background: rgba(245, 158, 11, 0.1);
  color: var(--accent-warning);
  border-color: rgba(245, 158, 11, 0.2);
}

.metadata-pill--setup-expert {
  background: rgba(239, 68, 68, 0.1);
  color: var(--accent-error);
  border-color: rgba(239, 68, 68, 0.2);
}

.metadata-pill--recommended {
  background: rgba(34, 197, 94, 0.1);
  color: var(--accent-success);
  border-color: rgba(34, 197, 94, 0.2);
}

.metadata-pill--caveats {
  background: rgba(245, 158, 11, 0.1);
  color: var(--accent-warning);
  border-color: rgba(245, 158, 11, 0.2);
}

.metadata-pill--not-recommended {
  background: rgba(239, 68, 68, 0.1);
  color: var(--accent-error);
  border-color: rgba(239, 68, 68, 0.2);
}
```

### Platform Icons Row

```css
.game-card__platforms {
  display: flex;
  gap: 0.35rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--border-subtle);
  margin-top: 0.5rem;
}

.platform-icon {
  width: 24px;
  height: 24px;
  opacity: 0.6;
  transition: opacity 0.15s ease;
}

.platform-icon:hover {
  opacity: 1;
}

.platform-icon--active {
  opacity: 1;
}

.platform-icon--inactive {
  opacity: 0.25;
  filter: grayscale(100%);
}
```

---

## Platform Icons

### Icon Set Needed

| Platform | Icon Suggestion | Notes |
|----------|-----------------|-------|
| PCVR | VR headset silhouette | Generic VR icon |
| Quest | Meta Quest outline | Quest-specific |
| PSVR | PlayStation logo | Sony platform |
| PSVR2 | PlayStation logo variant | PS5 VR |
| Rift | Oculus/Rift outline | Legacy Oculus |
| Index | Valve Index silhouette | PCVR-specific |
| Vive | HTC Vive outline | PCVR-specific |
| Pico | Pico logo | Standalone |

### SVG Implementation

```html
<!-- Example platform icons row -->
<div class="game-card__platforms">
  <img src="/icons/platform-pcvr.svg" alt="PCVR" class="platform-icon platform-icon--active" />
  <img src="/icons/platform-quest.svg" alt="Quest" class="platform-icon platform-icon--active" />
  <img src="/icons/platform-psvr.svg" alt="PSVR" class="platform-icon platform-icon--inactive" />
</div>
```

---

## Image Handling Strategy

### Hero Image Requirements

| Aspect | Specification |
|--------|---------------|
| Aspect Ratio | 16:9 (recommended) or 4:3 |
| Resolution | Minimum 800x450, optimal 1920x1080 |
| Format | WebP preferred, JPEG fallback |
| File Size | Target < 200KB per image |
| Loading | Lazy-load below fold, priority for above-fold |

### Placeholder Strategy

When no hero image exists:
1. Show subtle gradient background (matching brand colors)
2. Game title overlaid in bold
3. "No image available" subtle indicator

```css
.game-card__image--placeholder {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-secondary));
  display: flex;
  align-items: center;
  justify-content: center;
}

.game-card__image--placeholder::before {
  content: attr(data-title);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-muted);
  text-align: center;
  padding: 1rem;
}
```

---

## Homepage Data Flow

### Current (Broken)

```javascript
// index.astro
const featuredGames = games.filter((g) => g.data.featured).slice(0, 3);
```

### Recommended

```javascript
// index.astro
const allGames = games.sort((a, b) => {
  // Sort by tier first (S > A > B > C > D > F)
  const tierOrder = { 'S': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5 };
  const tierDiff = (tierOrder[a.data.tier] ?? 5) - (tierOrder[b.data.tier] ?? 5);
  if (tierDiff !== 0) return tierDiff;
  // Then by recommendation
  return b.data.score - a.data.score;
});

// Section: S-tier spotlight (1-2 games)
const spotlightGames = allGames.filter(g => g.data.tier === 'S').slice(0, 2);

// Section: All games grid (12-16 games)
const displayGames = allGames.slice(0, 16);
```

---

## CardGrid Component Rewrite

### Updated Props Interface

```typescript
interface GameCard {
  href: string;
  title: string;
  description: string;
  heroImage?: string;
  tier?: 'S' | 'A' | 'B' | 'C' | 'D' | 'F';
  routeType: string;
  platforms: string[];
  recommendation: string;
  setupBurden: string;
}

interface Props {
  items: GameCard[];
  columns?: 2 | 3 | 4;
  showImages?: boolean;
  showTier?: boolean;
  showRouteType?: boolean;
  showPlatforms?: boolean;
}
```

### Component Structure

```astro
---
// CardGrid.astro
interface GameCard {
  href: string;
  title: string;
  description: string;
  heroImage?: string;
  tier?: 'S' | 'A' | 'B' | 'C' | 'D' | 'F';
  routeType: string;
  platforms: string[];
  recommendation: string;
  setupBurden: string;
}

const { items, columns = 3, showImages = true, showTier = true, showRouteType = true, showPlatforms = true } = Astro.props;
---

<div class={`grid grid-${columns}`}>
  {items.map((game) => (
    <a class="game-card" href={game.href}>
      {showImages && (
        <div class="game-card__image-container">
          {game.heroImage ? (
            <img 
              src={game.heroImage} 
              alt={game.title}
              class="game-card__image"
              loading="lazy"
            />
          ) : (
            <div class="game-card__image--placeholder" data-title={game.title}></div>
          )}
          
          {showTier && game.tier && (
            <span class={`tier-badge tier--${game.tier.toLowerCase()}`}>
              {game.tier}
            </span>
          )}
          
          {showRouteType && (
            <span class="route-type-pill">
              {game.routeType}
            </span>
          )}
        </div>
      )}
      
      <div class="game-card__body">
        <h3 class="game-card__title">{game.title}</h3>
        <p class="game-card__description">{game.description}</p>
        
        <div class="game-card__metadata">
          <span class={`metadata-pill metadata-pill--recommendation-${game.recommendation.toLowerCase()}`}>
            {game.recommendation}
          </span>
          <span class={`metadata-pill metadata-pill--setup-${game.setupBurden.toLowerCase()}`}>
            {game.setupBurden}
          </span>
        </div>
        
        {showPlatforms && game.platforms.length > 0 && (
          <div class="game-card__platforms">
            {game.platforms.map(platform => (
              <img 
                src={`/icons/platform-${platform.toLowerCase()}.svg`}
                alt={platform}
                class="platform-icon platform-icon--active"
              />
            ))}
          </div>
        )}
      </div>
    </a>
  ))}
</div>
```

---

## Responsive Considerations

### Mobile (< 640px)

- Cards stack vertically (1 per row)
- Hero image aspect ratio shifts to 4:3 (taller)
- Tier and route type badges remain visible
- Metadata pills wrap naturally
- Platform icons scale to 20px

### Tablet (640-1024px)

- 2 cards per row
- Hero image 16:9
- Full metadata visible

### Desktop (1024px+)

- 3-4 cards per row
- Full hover states
- Platform icons interactive

---

## Animation & Interaction

### Hover State

```css
.game-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.game-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
  border-color: var(--border-default);
}

.game-card:hover .game-card__image {
  transform: scale(1.02);
}

.game-card:hover .game-card__title a {
  color: var(--accent-cyan);
}
```

### Focus State (Accessibility)

```css
.game-card:focus-within {
  outline: 2px solid var(--accent-cyan);
  outline-offset: 2px;
}
```

### Loading State

```css
.game-card__image {
  background: var(--bg-tertiary);
}

.game-card__image.is-loading {
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

---

## Implementation Priorities

### Phase 1: Foundation (Critical)

1. Update CardGrid component to accept hero images
2. Add tier badge overlay
3. Add route type pill overlay
4. Update homepage to show more games (remove featured filter)

### Phase 2: Enhancement (High)

1. Create platform icon set (SVG)
2. Add platform icons row to cards
3. Update homepage layout with section structure
4. Add lazy-loading for images

### Phase 3: Polish (Medium)

1. Add hover animations
2. Create placeholder state for missing images
3. Add filtering UI for route types
4. Implement sorting by tier

---

## File Changes Required

### Files to Modify

| File | Changes |
|------|---------|
| `src/pages/index.astro` | Update game query, add section structure |
| `src/components/CardGrid.astro` | Complete rewrite with image support |
| `src/layouts/Layout.astro` | Add platform icon styles if needed |

### Files to Create

| File | Purpose |
|------|---------|
| `public/icons/platform-pcvr.svg` | PCVR icon |
| `public/icons/platform-quest.svg` | Quest icon |
| `public/icons/platform-psvr.svg` | PSVR icon |
| `public/icons/platform-psvr2.svg` | PSVR2 icon |
| `public/icons/platform-rift.svg` | Rift icon |
| `public/icons/platform-index.svg` | Index icon |
| `public/icons/platform-vive.svg` | Vive icon |
| `public/icons/platform-pico.svg` | Pico icon |

---

## Visual Reference

### Card Layout Wireframe

```
┌─────────────────────────────────┐
│ ┌─────────────────────────────┐ │
│ │        HERO IMAGE           │ │
│ │                             │ │
│ │  ┌────┐          ┌────────┐ │ │
│ │  │ A  │          │ Full VR │ │ │
│ │  └────┘          │ Mod     │ │ │
│ │                  └────────┘ │ │
│ └─────────────────────────────┘ │
│                                 │
│  Half-Life 2 in VR              │
│                                 │
│  The Half-Life 2 VR Mod Is...   │
│                                 │
│  ┌──────────┐ ┌──────────────┐ │
│  │ Beginner │ │ Recommended  │ │
│  └──────────┘ └──────────────┘ │
│                                 │
│  [PCVR] [Quest]                 │
│                                 │
└─────────────────────────────────┘
```

### Grid Layout Wireframe

```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Card 1     │ │   Card 2     │ │   Card 3     │
│   Tier S     │ │   Tier A     │ │   Tier A     │
└──────────────┘ └──────────────┘ └──────────────┘

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Card 4     │ │   Card 5     │ │   Card 6     │
│   Tier B     │ │   Tier B     │ │   Tier C     │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## Summary

This design transforms the CompoundVR homepage from a minimal featured-game showcase into an information-dense, scannable catalog that:

1. **Shows more games** — 12-16 visible instead of 2-3
2. **Displays hero images** — Visual anchor for each game
3. **Prominently features tier badges** — S/A/B/C/D/F ranking visible at glance
4. **Shows route type** — Official Hybrid, Full VR Mod, etc.
5. **Includes platform support** — At-a-glance platform icons
6. **Maintains brand consistency** — Light body, dark header, cyan/purple accents
7. **Editorial authority** — Clean, technical, not decorative
8. **Mobile-responsive** — Adapts to all screen sizes

The result matches the brand direction's "technical authority" aesthetic while providing the scannability and information density that reference sites like UploadVR, Rock Paper Shotgun, and Eurogamer achieve.