# Ian Brief Template

Use this template for all Ian article briefs. Copy and customize for each game.

---

# Ian Brief: [Game Name]

**Game:** [Game Name]  
**Route Type:** [Official Hybrid | Official Standalone VR Version | Full VR Mod | Framework-Based | Injection Driver]  
**Platforms:** [PCVR | PSVR | PSVR2 | Quest | Pico | etc.]  
**Due:** Article + YAML frontmatter

---

## What Ian Needs to Know

### Route Type Context
[Explain what this route type means. Be factual, not editorial.]

- **Official Hybrid:** Developer-added VR support to an existing game. May be incomplete or delisted.
- **Official Standalone VR Version:** Native VR port, designed for VR, sold as VR product.
- **Full VR Mod:** Community-made mod with motion controls, rebuilt systems, ongoing development.
- **Framework-Based:** Universal VR profiles via REFramework, UEVR, etc. Variable quality per-game.
- **Injection Driver:** VorpX/Geo3D stereoscopic injection. No motion controls, no hand presence.

### [Game-Specific Context]
[Factual background: what the game is, when it released, who made it, what the VR implementation is. No opinions about quality — just facts.]

### Multiplatform Note (if applicable)
[If the game is on multiple platforms, briefly note: which platforms, what differences to research, keep comparison brief in article.]

---

## Research Sources

**Preferred sources (in order):**
1. **YouTube VR channels:** Beardo Benjo, Gamertag VR, Ian from Eurogamer, Paradise's Decay, Headset VR, Nathie, VR Grid
2. **Flat2VR Discord** — community knowledge, mod status, setup notes
3. **Reddit** — r/vive, r/oculus, r/psvr, r/psvr2, game-specific subreddits
4. **Internet/media coverage** — reviews, articles, developer notes
5. **Training data** — may be outdated, verify against current sources

### Key Research Points
[Specific things to verify for this game. Bullet points.]

---

## Article Requirements

### Must Include
1. [What the game is — brief, assume reader may not know]
2. [The VR implementation — how it works]
3. [Key features or differences — if relevant]
4. [Brief platform comparison if multiplatform — one paragraph or section]
5. The verdict with tier ratings

### Must NOT Include
- Community quotes or forum references
- "Tested vs community" framing
- Specific setup steps (keep evergreen, preserves paid guide monetization path)
- Hardware-specific performance numbers
- Version numbers (keep evergreen)

### Verdict Format
```
**Game Quality: [LETTER]**
[1-2 sentences explaining why]

**VR Implementation Quality: [LETTER]**
[1-2 sentences explaining why]

**Overall Tier: [LETTER]**
[1-2 sentences summarizing the experience]
```

### YAML Frontmatter
```yaml
---
title: "[Game Name] VR"
description: "[Compelling one-sentence description]"
lastVerified: YYYY-MM-DD
featured: false
routeType: [Official Hybrid | Official Standalone VR Version | Full VR Mod | Framework-Based | Injection Driver]
platforms: ['PCVR', ...other platforms if applicable]
recommendation: [Recommended | Recommended with Caveats | Enthusiasts/Tinkerers Only | Wait for Updates | Not Recommended]
playability: [Fully Playable | Mostly Playable | Partially Playable | Experimental | Broken]
setupBurden: [Beginner Friendly | Moderate Setup | Advanced Setup | Expert Only]
inputStyle: [Full Motion Controls | Partial Motion Controls | Gamepad Preferred | KBM Required | Mixed Input]
comfort: [Comfortable | Moderate Intensity | Intense | Highly Variable]
performance: [Efficient | Moderate Demand | Heavy Demand | Inconsistent / Unpredictable]
supportStatus: [Active | Recently Updated | Stable but Quiet | Uncertain | Abandoned | Broken by Update]
genres:
  - [Genre 1]
  - [Genre 2]
technicalTags:
  - [Tag 1]
  - [Tag 2]
experienceTags:
  - [Tag 1]
  - [Tag 2]
tier: [S/A/B/C/D/F]
verdict: "[Summary verdict]"
heroImage: /images/games/[game-slug]-vr-hero.jpg
---
```

---

## Output

Write the complete article in the drafts folder:
`/editorial/drafts/[game-slug]-feature-draft.md`

Include full article body plus YAML frontmatter.

---

## Editorial Process

1. **Ian writes first draft** — no editorial opinions from Richard in brief
2. **Richard reviews** — then we debate tier, angle, and editorial position
3. **Final draft** — after editorial feedback loop
4. **Publish** — after final approval