# CompoundVR Project Memory

**Project:** Flat-to-VR Mods / CompoundVR  
**Managing Editor:** Richard  
**Last Updated:** March 29, 2026

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
- Tetris Effect: Connected VR (S-tier, March 29)
- Space Pirate Trainer VR (A-tier, March 25)
- DuckStation VR software article (March 25)
- The Legend of Zelda VR (A-tier, March 29)

**In Progress:**
- Brand system implementation (Phase 1)

**Next Up:**
- Additional game coverage per content opportunity map

---

## Key Decisions

- **Logo:** v5 approved and in use
- **Theme:** Dark, sophisticated, layered surfaces
- **Content Model:** Canonical game pages with structured metadata
- **Agent Workflow:** Archangel → Michael → Richard/Ian/Maya → Ship
- **Release Date Tracking (added 2026-03-29):** Two fields on game cards:
  - `flatReleaseDate` — Original flat game release (use franchise origin for games like Tetris, Zelda)
  - `vrReleaseDate` — When VR support became available
  - Native VR games only use vrReleaseDate (no flatReleaseDate)
  - Display format: "Month DD, YYYY" (human-readable)
- **Metadata cards removed (2026-03-29):** Recommendation (redundant with tier), Playability (inferred), Support (too hard to keep accurate)

---

## Editorial Standards (for Ian Article Briefs)

### Research Sources (Priority Order)
1. **YouTube reviewers** — Beardo Benjo, Gamertag, Ian from Euro Gamer, paradises decay, headset-vr, nathie, vrgrid
2. **Flat2VR Discord** — strongest community source alongside Reddit
3. **Reddit** — r/virtualreality, r/oculus, r/Vive, game-specific subs
4. **GitHub releases** — version history, but don't prompt specific versions upfront

### Content Rules
- **Evergreen focus** — don't prompt specific version numbers in briefs; let Ian research current state
- **No route type in briefs** — Ian researches and discovers whether it's injection driver, mod, official hybrid, etc. Never give him the answer
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

### Release Date Fields (Added 2026-03-29)
- **`flatReleaseDate`** — Original flat game release date (YYYY-MM-DD)
- **`vrReleaseDate`** — Date VR support became available (YYYY-MM-DD)
- **Native VR games** — Only use `vrReleaseDate`, leave `flatReleaseDate` empty (e.g., Space Pirate Trainer, SUPERHOT VR)
- **Framework/Injection** — `vrReleaseDate` is when the tool/framework made it viable
- **Both fields are optional** — The template only displays them if present

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

**CRITICAL: Maya MUST use `gemini-image-simple` workspace skill for image generation.**

This is a **workspace skill** at `/home/archangel/.openclaw/workspace/skills/gemini-image-simple/`. It uses Google's Nano Banana Pro (Gemini 3 Pro Image).

**Correct invocation (Maya must do this):**
1. Read SKILL.md: `/home/archangel/.openclaw/workspace/skills/gemini-image-simple/SKILL.md`
2. Call via exec: `python3 /home/archangel/.openclaw/workspace/skills/gemini-image-simple/scripts/generate.py "prompt" output.png`

**Correct spawn format (DO NOT DEVIATE):**
```
Generate a hero image for the game [GAME NAME].

Use gemini-image-simple. Reference the CompoundVR brand guide at /design/compoundvr-brand-direction-v1.md for visual direction.

Save to: [full path]

Return the file path when done.
```

**Model:** `ollama/kimi-k2.5:cloud` (specify explicitly in spawn)

**Mandatory elements:**
1. "Use gemini-image-simple" — triggers Maya to look for this workspace skill
2. "Reference the CompoundVR brand guide" — Maya needs design direction
3. Explicit save path

**Critical:**
- Do NOT include narrative context or visual direction — Maya reads the brand guide herself
- If Maya mentions OpenAI or local generation, REJECT and respawn
- Always verify output is valid JPEG with recognizable content

**Hero Image Output Requirements:**
- Format: JPG (convert PNG with PIL if needed)
- Aspect ratio: 16:9 (cinematic wide)
- Dimensions: 1280x720 minimum
- File size: 100-300KB web-optimized (optimize with PIL if larger)

**Retro Game Aesthetic:**
- For older games (1990s, early 2000s), add "retro/older game aesthetic" to spawn task

### Article Types

- **Game Page:** `/site/src/content/games/` — full review with tier rating
- **Software/Tool Article:** `/site/src/content/articles/` — guide format, no tier rating
- **Native VR Games:** Use same tier system as flat-to-VR; routeType is "Official Standalone VR Version"

### Key Files

- Briefs: `/editorial/briefs/`
- Drafts: `/editorial/drafts/`
- Game Content: `/site/src/content/games/`
- Article Content: `/site/src/content/articles/`
- Hero Images: `/site/public/images/games/` (or `/articles/` for software)

---

## Recently Published

**Tetris Effect: Connected VR** — Published 2026-03-29
- S-tier verdict: Essential VR experience, audiovisual immersion masterpiece
- Native VR: PSVR, PSVR2, Quest, PCVR with first-party support
- PSVR2 is premium experience (headset haptics, eye tracking, 120fps)
- Live at: https://compoundvr.com/games/tetris-effect

**Space Pirate Trainer VR** — Published 2026-03-25
- A-tier verdict: Foundational VR wave shooter, mechanically polished
- Native VR: HTC Vive launch title (April 2016), Quest DX Edition adds multiplayer
- Very comfortable — no artificial locomotion
- Live at: https://compoundvr.com/games/space-pirate-trainer

**DuckStation VR** — Published 2026-03-25 (Software Article)
- NOT true VR — stereoscopic 3D wrapper via geo-11
- No head tracking, no motion controls, just 3D depth on virtual screen
- Recommendation: Enthusiasts Only
- Live at: https://compoundvr.com/articles/duckstation-vr
