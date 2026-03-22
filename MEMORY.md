# CompoundVR Project Memory

**Project:** Flat-to-VR Mods / CompoundVR  
**Managing Editor:** Richard  
**Last Updated:** March 18, 2026

---

## Key Project Documents

### Editorial System
- `/editorial/review-methodology-v1.md` — How we evaluate flat-to-VR mods
- `/editorial/game-coverage-framework-v1.md` — Content taxonomy and page types
- `/editorial/site-architecture-v1.md` — Site structure and content organization

### Brand & Design
- `/design/research-vr-media-design-2025.md` — Competitive analysis of VR/gaming media
- `/design/compoundvr-brand-direction-v1.md` — **Authoritative visual system specification**
  - Color system with layered surfaces
  - Typography (Inter + JetBrains Mono)
  - Component patterns (cards, buttons, pills, scores)
  - Interaction design
  - Implementation phases

### Team Structure
- `/TEAM.md` — Single source of truth for team composition and roles

### Assets
- `/assets/branding/` — Logo versions (v1-v6), approved: v5 for header
- `/assets/images/` — Article hero images

---

## Design System (Summary)

**Core Principle:** Technical Authority — engineered, not decorated

**Color Palette:**
- Background: `#0b1020` (deep navy)
- Surfaces: Layered system (`#151d38`, `#1a2342`, `#1e284c`)
- Text: `#f0f4ff` (primary), `#c5cce6` (secondary), `#8b92b8` (tertiary)
- Accents: Cyan `#6ee7ff`, Purple `#8b5cf6`
- Semantic: Green success, Yellow warning, Red error

**Typography:**
- Primary: Inter, system-ui
- Monospace: JetBrains Mono (for technical data)
- Scale: Clamp-based responsive sizing

**Key Components:**
- Cards: Hover lift, subtle shadows, 16px radius
- Pills: Rounded, color-coded by status
- Scores: Large monospace, color-coded, with glow effect
- Navigation: Sticky, backdrop blur, reduced logo height

**Implementation Priority:**
1. Color system + typography refinements
2. Card components + hover states
3. Score/verdict display
4. Animation + accessibility polish

---

## Active Work

**Published:**
- Half-Life 2 VR mod article (live on site)

**In Progress:**
- Brand system implementation (Phase 1)

**Next Up:**
- Additional game coverage per content opportunity map

---

## Editorial Standards (for Ian Article Briefs)

### Research Sources (Priority Order)
1. **YouTube reviewers** — Beardo Benjo, Gamertag, Ian from Euro Gamer, paradises decay, headset-vr, nathie, vrgrid
2. **Flat2VR Discord** — strongest community source alongside Reddit
3. **Reddit** — r/virtualreality, r/oculus, r/Vive, game-specific subs
4. **GitHub releases** — version history, but don't prompt specific versions upfront

### Content Rules
- **Evergreen focus** — don't prompt specific version numbers in briefs; let Ian research current state
- **No "tested vs community" labeling** — Ian is an AI, he hasn't tested anything
- **No community quotes** — looks amateurish
- **Developer quotes only** — and only if super relevant, must be cited
- **No specific hardware requirements** — VR mods are notoriously hard on machines; use broad categories: "potato," "mid-range," "super computer"
- **Setup mentions** — can note ease/difficulty broadly, but no specifics (DLL drops, file paths, etc.) — paid setup guides are a future monetization path

### Verdict System
- **Tier rankings: S, A, B, C, D, F** — no percentage scores
- **Tiers are ABSOLUTE, not relative to category** — A B+ injection driver game competes with B+ native VR and B+ mods for your time
- **The question tiers answer:** "Is this worth my Saturday afternoon compared to ANY VR option?"
- **Dual-factor scoring:**
  - How great the game is to play in VR (implementation quality)
  - How great the game is overall (game quality)
- **S/A tier** requires both: awesome game + awesome VR implementation
- **Mid tier (B/C):** One great, one decent — still worth playing with caveats
- **Low tier (D/F):** Not worth the time, regardless of whether it's native, modded, or injected
- **Implementation type note in verdict** — helpful context ("injection driver" or "mod"), but doesn't change the tier

### Route Types (for Schema)
- **Official Hybrid** — Developer-made VR support (Ethan Carter, Project CARS)
- **Full VR Mod** — Community mod with motion controls, rebuilt systems (MotherVR, HL2VR, Fully Possessed)
- **Injection Driver** — VorpX/Geo3D stereoscopic injection, no motion controls (Dishonored via VorpX)
- **Official Standalone VR Version** — Game released as VR-native (Skyrim VR, Fallout 4 VR)
- **Framework-Based** — UEVR/REFramework universal profiles (Elden Ring, RE2 via Praydog)

### Content Type Awareness
When briefing Ian, specify which type we're covering:
- **Native VR / Official Hybrid**: Focus on how complete the implementation is, what's missing
- **Full VR Mod**: Focus on mod quality, motion controls, ongoing development
- **Injection Driver**: Must explain what injection drivers CAN and CANNOT provide:
  - CAN: Stereoscopic 3D, head tracking, sometimes auto-calibration
  - CANNOT: Motion controls, hand presence, VR-optimized UI, comfort features
  - Verdict should note "this is injection driver quality, not port quality"

## Content Technical Notes

### YAML Frontmatter (Game Content Files)
- **Always quote values with colons** — Game titles like "Alien: Isolation" break YAML parsing because colons are key-value separators. Use `title: "Alien: Isolation in VR"` not `title: Alien: Isolation in VR`
- **Quote long descriptions** — Multi-sentence descriptions may contain special characters. Safer to quote.
- **Quote verdicts** — Verdicts often contain em-dashes and special punctuation. Always quote.

### Site Deployment Workflow
- **Always verify build succeeds** — After git push, check GitHub Actions status
- **Run `npm run build` locally before pushing** — Catch YAML/content errors early
- **If build fails:** Fix locally if simple (YAML quoting, syntax), commit and push fix
- **If build fails and can't fix:** Report to user with error details
- **Verify deployment** — Check live URL after deployment completes

## Key Decisions

- **Logo:** v5 approved and in use
- **Theme:** Dark, sophisticated, layered surfaces
- **Content Model:** Canonical game pages with structured metadata
- **Agent Workflow:** Archangel → Michael → Richard/Ian/Maya → Ship

---

## Reference

**Site:** https://compoundvr.com  
**Repo:** github.com/archsupafly/compoundvr  
**Deploy:** GitHub Pages (auto via Actions)

---

## Agent Workflow

### Game Article End-to-End Workflow

**Step 1: Ian Brief**
- Create brief at `/editorial/briefs/[game-slug]-brief.md`
- Brief contains: game context, route type, platforms, research focus, output path
- NO editorial opinions in brief (facts and format only)
- Spawn Ian to write first draft

**Step 2: Richard Reviews First Draft**
- Wait for Ian's first draft to complete
- Review for: evergreen language, tier accuracy, YAML schema compliance, route type correctness
- Give targeted editorial feedback to Ian for revision

**Step 3: Maya Hero Image (AFTER Ian's first draft)**
- Spawn Maya with hero image instructions AFTER Ian's first draft is complete
- Use image generation skill (currently: need to verify which skill works)
- Prompt should match CompoundVR brand colors and game aesthetic
- Maya needs article context from Ian's draft to create appropriate image

**Step 4: Ian Final Draft**
- Ian returns revised draft incorporating editorial feedback
- Verify all changes applied correctly

**Step 5: Richard Publishes**
- Copy hero image to `/site/public/images/games/[game-slug]-vr-hero.jpg`
- Copy final draft to `/site/src/content/games/[game-slug].md`
- Run `npm run build` to verify
- Git commit and push

**CRITICAL:** Steps 2 and 3 are SEQUENTIAL, not parallel. Maya needs Ian's article context. Ian writes first, then Maya generates image.

### Image Generation Note

Maya needs access to an image generation tool. Currently checking:
- `openai-image-gen` skill requires `OPENAI_API_KEY` env var
- `gemini` CLI needs to be installed
- Verify which tool is available before spawning Maya

### Article Types

- **Game Page:** `/site/src/content/games/` — full review with tier rating
- **Software/Tool Article:** `/site/src/content/articles/` — guide format, no tier rating

### Key Files

- Briefs: `/editorial/briefs/`
- Drafts: `/editorial/drafts/`
- Game Content: `/site/src/content/games/`
- Article Content: `/site/src/content/articles/`
- Hero Images: `/site/public/images/games/`

---

## In Progress

**Team Fortress 2 VR Article**
- Brief created: `/editorial/briefs/team-fortress-2-vr-brief.md`
- First draft complete: `/editorial/drafts/team-fortress-2-vr-feature-draft.md`
- Editorial review done, route type fixed to `Multi-Route Coverage`
- **BLOCKED:** Need image generation tool to work for Maya
- **NEXT:** Verify image generation capability, generate hero image, publish
