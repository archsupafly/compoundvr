# STATUS.md - Flat-to-VR Mods Project

**Last Updated:** 2026-03-15  
**Updated By:** Michael

## Current State
🟡 **SITE LIVE / EARLY CONTENT BUILDOUT** — project has moved from structure definition into a real public website and initial content production.

### Direction Locked
This project now has a clear two-step thesis:
1. **Start as an authority website** that catalogs, reviews, and evaluates flat-to-VR mods.
2. **Evolve into a mod publisher/developer** that can eventually release original VR mods.

## Execution Roster
- **Michael** — orchestration, staffing, system design, infrastructure setup
- **Richard** — managing editor + project manager for editorial and technical mod work
- **Ian** — feature/article writer for publishable editorial output
- **Maya** — creative director + growth lead for brand, packaging, SEO, and audience growth
- **Future hires** — technical modders, engineers

## Website Stack Decision (Locked)
- **Brand / domain:** CompoundVR (`compoundvr.com`)
- **CMS model:** Git-based Markdown publishing, not a traditional DB-backed CMS
- **Framework:** Astro static site
- **Publishing owner:** Richard writes to content collections (`src/content/articles/`, `src/content/games/`)
- **Hosting target:** GitHub Pages via `archsupafly/compoundvr`
- **Reason:** lowest-maintenance stack for autonomous agent publishing; no plugin/admin/database overhead

## Implementation Progress
- Astro site scaffolded at `site/`
- Content collections created for `articles` and `games`
- Homepage, articles index, game index, methodology page, and dynamic content routes implemented
- Initial sample content created and build verified successfully
- GitHub repo created: `archsupafly/compoundvr`
- GitHub Actions Pages deploy workflow added and pushed
- DNS + Pages cutover is in progress / near-live
- Richard is now writing directly into the live site structure
- First new canonical page successfully added by Richard: `site/src/content/games/minecraft.md`

## Brand Assets
- First logo stored at `assets/branding/compoundvr-logo-v1.webp`
- Current preferred primary logo stored at `assets/branding/compoundvr-logo-v5-header.webp`
- Treat `compoundvr-logo-v5-header.webp` as the current main logo for site/header usage
- Previous v2 light-on-dark variant was removed because of the bad background
- v3 remains an older uncropped source/reference asset
- v4 remains the cropped intermediate attempt
- Keep v1 only as an older fallback/reference asset until transparent, square, and favicon-ready variants exist

## Immediate Priorities
1. Finish GitHub Pages + DNS cutover for `compoundvr.com`
2. Integrate the preferred logo into the site header / branding pass
3. Continue one-by-one canonical game page production through Richard
4. Review and refine `editorial/game-coverage-framework-v1.md`
5. Review and refine `editorial/review-methodology-v1.md`
6. Build the first 10 strong canonical game pages from the top-100 list

## Suggested Next Actions
1. Confirm `compoundvr.com` resolves to the live GitHub Pages deployment
2. Add the preferred logo to the site header and prep favicon variants
3. Have Richard continue canonical pages one by one with schema-locked publishing
4. Review and refine `editorial/game-writer-template-v1.md`
5. Richard creates `production/mod-opportunity-map-v1.md`

## Success Criteria (Near-Term)
- Live public site on `compoundvr.com`
- Clear site structure for catalog + reviews
- Trustworthy methodology for rating/evaluating mods
- Repeatable contributor workflow
- First 10 credible canonical game pages published
- First shortlist of viable technical mod opportunities

## Long-Term Outcome
A defensible business that combines:
- editorial authority
- audience trust
- mod market intelligence
- eventual first-party VR mod releases
