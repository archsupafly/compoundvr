# Site Architecture v1

**Owner:** Richard  
**Date:** 2026-03-14  
**Purpose:** Define the information architecture, page types, taxonomy, and internal-linking model for a flat-to-VR mods authority site.

---

## 1. Strategic Goal

The site should be structured to do four jobs at once:

1. help readers quickly find the best VR route for a game
2. build search traffic around high-intent queries
3. create reusable taxonomy for comparisons, lists, and updates
4. generate market intelligence useful for future first-party mod decisions

If the architecture is weak, the site becomes a pile of articles.
If the architecture is strong, it becomes a usable product.

---

## 2. Core Site Model

The site should not be organized like a generic gaming blog.
It should be organized like a **decision database with editorial judgment layered on top**.

That means the primary unit is:

> **the canonical game page**

Everything else supports, compares, updates, or organizes those pages.

---

## 3. Primary Page Types

## 3.1 Canonical Game Page
This is the most important template on the site.

Purpose:
- answer whether and how a game works in VR
- capture structured metadata
- serve as the updateable evergreen page
- act as the SEO pillar for that title

Examples:
- "Cyberpunk 2077 in VR: Is It Worth Playing?"
- "Ready or Not in VR: UEVR, Mod Options, and Verdict"

Must include:
- verdict box
- classification
- setup info
- experience evaluation
- recommendation
- tags/metadata
- last verified date

## 3.2 Setup Guide
Purpose:
- explain installation and configuration in more detail for high-friction titles

Examples:
- "How to Install the Resident Evil 2 VR Mod"
- "How to Use UEVR With [Game]"

Use only when the setup burden justifies a dedicated page.

## 3.3 Troubleshooting / Performance Guide
Purpose:
- capture recurring user pain points
- target practical long-tail search traffic
- reduce bounce and improve trust

Examples:
- "[Game] VR Mod Not Working: Common Fixes"
- "Best Settings for [Game] in UEVR"

## 3.4 Comparison Page
Purpose:
- compare multiple games, mods, or VR routes using structured site data

Examples:
- "Best UEVR Games Right Now"
- "Official Hybrid VR Games vs VR Mods"
- "Best Flat-to-VR Horror Games"

These pages are strong traffic and monetization assets if built on real taxonomy.

## 3.5 News / Update Page
Purpose:
- cover meaningful updates that materially affect recommendation quality

Examples:
- major mod release
- framework compatibility leap
- official patch that breaks support
- feature expansion such as new motion controls

Do not produce low-value churn.
Only publish when the update changes the decision landscape.

## 3.6 Hub / Category Page
Purpose:
- aggregate pages by useful reader intent
- rank for broader thematic terms
- improve navigation and internal linking

Examples:
- UEVR Games
- Official VR Games from Flat Series
- Best Flat-to-VR Shooters
- Beginner-Friendly VR Mods

---

## 4. Taxonomy Model

The taxonomy should support reader utility first, SEO second, and editorial consistency throughout.

## 4.1 Primary taxonomy dimensions
Every game page should be classified on these axes:

### A. VR Route Type
- Official Hybrid
- Official Standalone VR Version
- Full VR Mod
- Framework-Based

### B. Recommendation State
- Recommended
- Recommended with Caveats
- Enthusiasts/Tinkerers Only
- Wait for Updates
- Not Recommended

### C. Playability State
- Fully Playable
- Mostly Playable
- Partially Playable
- Experimental
- Broken

### D. Setup Burden
- Beginner Friendly
- Moderate Setup
- Advanced Setup
- Expert Only

### E. Input Style
- Full Motion Controls
- Partial Motion Controls
- Gamepad Preferred
- KBM Required
- Mixed Input

### F. Comfort Profile
- Comfortable
- Moderate Intensity
- Intense
- Highly Variable

### G. Performance Profile
- Efficient
- Moderate Demand
- Heavy Demand
- Inconsistent / Unpredictable

### H. Support Status
- Active
- Recently Updated
- Stable but Quiet
- Uncertain
- Abandoned
- Broken by Update

---

## 4.2 Secondary taxonomy dimensions
These improve browsing, comparisons, and editorial packaging.

### Genre tags
- Shooter
- Horror
- Racing
- RPG
- Action
- Survival
- Sim
- Platformer
- Strategy
- Open World
- Stealth
- Soulslike

### Perspective tags
- First Person
- Third Person
- Mixed Perspective
- Cockpit
- Isometric/Other

### Experience tags
- Good First VR Mod
- Best-in-Class Candidate
- Hardcore Enthusiast Pick
- Third-Person in VR
- Performance Heavy
- Comfort Intense
- Seated Friendly
- Roomscale Friendly

### Technical tags
- UEVR
- Unreal Engine
- Unity
- Praydog Ecosystem
- Injector-Based
- Native VR Mode
- Separate VR App

These tags should be selective. Taxonomy bloat kills clarity.

---

## 5. Canonical URL / Content Hierarchy Recommendation

Recommended structure:

- `/games/[slug]/` → canonical game page
- `/guides/[slug]/` → setup/troubleshooting/performance guides
- `/compare/[slug]/` → comparison pages
- `/updates/[slug]/` → meaningful news/update items
- `/tags/[taxonomy-term]/` or curated hub pages → aggregation pages

Examples:
- `/games/cyberpunk-2077-vr/`
- `/guides/install-resident-evil-2-vr-mod/`
- `/compare/best-uevr-games/`
- `/updates/uevr-update-improves-[game]/`

The canonical game page should remain the center of gravity.

---

## 6. Content Tiering System

Not every game deserves the same editorial investment.

## Tier 1 — Full Coverage
Use for:
- high-demand games
- obvious SEO value
- strong affiliate/commercial potential
- major community attention
- major strategic authority value

Deliver:
- canonical game page
- setup guide
- troubleshooting/performance guide if needed
- update coverage when warranted
- inclusion in comparison hubs

## Tier 2 — Standard Coverage
Use for:
- moderate demand
- good niche value
- meaningful reader usefulness

Deliver:
- canonical game page
- one guide only if setup complexity justifies it
- occasional inclusion in comparison pages

## Tier 3 — Catalog Coverage
Use for:
- low-demand or long-tail titles
- low commercial value but some completeness value

Deliver:
- concise canonical page with verdict, metadata, tags, and update notes
- no supporting pages unless traction appears

This protects the business from overinvesting in low-return pages.

---

## 7. Internal Linking Model

Internal linking should be systemized, not improvised.

Every canonical game page should link to:
- relevant setup guide(s)
- troubleshooting/performance guide(s) if they exist
- category hubs for its VR route type
- genre hubs where relevant
- comparison pages featuring it
- adjacent alternatives when genuinely helpful

Every guide should link back to:
- the canonical game page
- relevant framework or category hub
- related troubleshooting/setup content

Every comparison page should link to:
- all included canonical game pages
- relevant hubs and related comparisons

This creates a strong topical cluster and improves user navigation.

---

## 8. Front-End Filtering Recommendations

The site should eventually allow filtering by:
- VR route type
- recommendation level
- setup difficulty
- playability state
- motion controls support
- comfort intensity
- performance demand
- genre
- engine/framework
- support/update status

This is part of what makes the site feel useful rather than merely editorial.

---

## 9. Homepage and Navigation Recommendations

The homepage should not behave like a generic news feed.

Recommended homepage blocks:
- Featured: Best VR routes worth playing now
- Recently Verified / Recently Updated
- Beginner-Friendly Picks
- Best by category (Shooter / Horror / Racing / etc.)
- UEVR Highlights
- Official Hybrid VR Highlights
- Latest meaningful updates
- Search/filter entry point

Primary nav recommendation:
- Games
- Guides
- Best Of / Compare
- UEVR
- Official VR
- VR Mods
- Updates

This structure supports both new visitors and repeat utility traffic.

---

## 10. SEO Architecture Principles

The site should be built around search intent clusters, not random post ideas.

## 10.1 High-intent page clusters
### Per-game intent
- [Game] VR mod
- [Game] in VR
- does [Game] support VR
- [Game] UEVR
- [Game] VR review

### Setup intent
- how to install [Game] VR mod
- [Game] UEVR settings
- [Game] VR mod not working

### Comparison intent
- best UEVR games
- best flat-to-VR games
- best VR mods for [genre]
- official hybrid VR games worth playing

## 10.2 Evergreen over churn
Prioritize pages with long-lived user utility.
Update posts should exist to support the evergreen pages, not replace them.

## 10.3 Snippet-friendly design
Canonical game pages should:
- answer the core question early
- use structured verdict sections
- include FAQ only when useful
- expose freshness via last verified date

---

## 11. Business / Monetization Alignment

A strong site architecture supports monetization without turning coverage into sludge.

## 11.1 Affiliate opportunities
High-intent pages can support affiliate placements for:
- VR headsets
- router/network gear for streaming setups
- GPUs/PC components
- controller accessories
- cables/battery solutions

These placements make the most sense on:
- setup guides
- performance guides
- beginner-friendly recommendation hubs
- high-traffic game pages

## 11.2 Sponsorship potential
Possible only if editorial integrity remains obvious.
The site needs visible methodology and honest caveats first.

## 11.3 Newsletter / owned audience capture
Natural capture points:
- game update alerts
- framework compatibility updates
- "best new VR routes" digests

## 11.4 Product intelligence
The taxonomy should also reveal:
- which genres perform best in VR
- which games create the most reader interest
- which technical routes are too fragile
- where first-party mod opportunity may exist later

This is strategically valuable.

---

## 12. Recommended Editorial Workflow Around the Architecture

1. select target game
2. assign content tier
3. create canonical game page first
4. complete metadata and taxonomy fields
5. determine whether supporting guide(s) are justified
6. place game into appropriate hubs/comparison candidates
7. flag update watch channels

This prevents random article production detached from the site's information model.

---

## 13. Suggested Initial Build Order

For launch or early-stage buildout, prioritize:

### Phase 1
- canonical game pages for highest-value targets
- essential taxonomy
- route-type hubs (Official VR / VR Mods / UEVR)
- basic compare pages

### Phase 2
- setup guides for high-friction winners
- troubleshooting/performance guides for high-traffic titles
- genre hubs and best-of pages

### Phase 3
- more advanced filtering
- systematic update coverage
- richer comparison tooling
- newsletter/product integrations

---

## 14. What Success Looks Like

A successful site architecture means:
- users can answer practical VR questions quickly
- writers can produce repeatable, structured coverage
- editors can compare titles consistently
- search traffic compounds around utility pages
- monetization can attach to high-intent surfaces without corrupting trust
- the company learns which opportunities matter most

---

## 15. Bottom Line

The site should be built as:

> **an evergreen decision engine for flat-to-VR games, with game pages as the canonical unit and taxonomy strong enough to power guides, comparisons, search traffic, and future business intelligence.**

That is a much stronger business than a blog-shaped pile of VR content.
