# Game Writer Template v2

**Owner:** Richard  
**Date:** 2026-03-19  
**Purpose:** Standardize what a writer must submit for every flat-game-with-VR coverage page.

---

## 1. Use Case

Use this template for any game page covering:
- **Official Hybrid:** Developer-added VR support to an existing game (may be incomplete or delisted)
- **Official Standalone VR Version:** Native VR port, designed for VR, sold as VR product
- **Full VR Mod:** Community-made mod with motion controls, rebuilt systems
- **Framework-Based:** Universal VR profiles via REFramework, UEVR, etc.
- **Injection Driver:** VorpX/Geo3D stereoscopic injection, no motion controls

This is the default template for a game's canonical page.

---

## 2. Writer Submission Package

Every assignment must include:

1. Completed article draft with YAML frontmatter
2. Verdict with tier ratings (Game Quality + VR Implementation Quality + Overall)
3. Testing notes (if directly tested)
4. Source log

If any item is missing, the article is incomplete.

---

## 3. Article Structure

### Title
`[Game Name] in VR: [Compelling Subtitle]`

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

## 4. Article Body

### Opening
Lead with what matters: what the game is, what VR route exists, and whether it's worth playing. Don't bury the answer.

### What This VR Route Actually Is
Explain:
- Route type (official hybrid, mod, injection driver, etc.)
- What it provides and doesn't provide
- Who maintains it
- Whether support is active or abandoned

For injection drivers specifically:
- Explain they provide stereoscopic 3D + head tracking only
- No motion controls, no hand presence, no VR UI
- Set honest expectations

### How It Plays
Break down:
- Controls (motion controls? gamepad? keyboard?)
- Comfort (locomotion type, motion sickness risk)
- Performance (broad categories: potato/mid-range/super computer)
- Stability (crashes, bugs, update fragility)

### What Works Well
Honest assessment of strengths. Be specific.

### What Doesn't Work
Honest assessment of weaknesses. Be specific.

### Platform Differences (if multiplatform)
If the game is on multiple VR platforms (PCVR, PSVR, Quest, etc.):
- Brief comparison of visual/audio/control differences
- One paragraph or section — don't make it the focus
- Typical hierarchy: Quest ≤ PSVR ≤ PCVR (but verify for each game)

### Who This Is For
Segment the audience:
- Good for: [specific groups]
- Not for: [specific groups]

### The Verdict

**Use this exact format:**

```
## The Verdict

**Tier: [LETTER]**

**Game Quality: [LETTER]**
[1-2 sentences explaining why — absolute rating, not relative to category]

**VR Implementation Quality: [LETTER]**
[1-2 sentences explaining why — absolute rating, not "good for a mod" or "good for injection"]

**Overall Tier: [LETTER]**
[1-2 sentences summarizing the experience]
```

**Tier Ratings:**
- **S:** Essential — both game and VR implementation are exceptional
- **A:** Excellent — highly recommended, minor caveats
- **B:** Good — worth playing, notable limitations
- **C:** Average — only for enthusiasts
- **D:** Below average — significant problems
- **F:** Not recommended — fundamental issues

**Critical:** Tiers are absolute, not relative. An injection driver doesn't get "B+ for injection drivers" — it gets an absolute rating against ALL VR experiences. A gamer deciding between this and native VR should compare on the same scale.

---

## 5. Evergreen Language Requirements

**Do NOT include:**
- Community quotes or forum references
- "Tested vs community" framing
- Specific hardware requirements ("RTX 3080 recommended")
- Specific version numbers (updates change them)
- Detailed setup steps (preserves paid guide monetization path)
- "As of [date]" or time-bound language

**DO include:**
- Broad performance categories (potato/mid-range/super computer)
- Evergreen descriptions of quality
- What the VR route provides and doesn't provide
- Honest assessment of who should bother

---

## 6. Research Sources

**Preferred sources (in order):**
1. **YouTube VR channels:** Beardo Benjo, Gamertag VR, Ian from Eurogamer, Paradise's Decay, Headset VR, Nathie, VR Grid
2. **Flat2VR Discord** — community knowledge, mod status, setup notes
3. **Reddit** — r/vive, r/oculus, r/psvr, r/psvr2, game-specific subreddits
4. **Internet/media coverage** — reviews, articles, developer notes
5. **Training data** — may be outdated, verify against current sources

**Document sources in your notes, but do NOT quote community members or forums in the article.**

---

## 7. Testing Notes (if directly tested)

- Date tested:
- Headset used:
- Runtime/platform:
- Controller/input method:
- Game version/build:
- Time spent testing:
- Main content tested:
- What worked reliably:
- What partially worked:
- What failed:
- Major caveats:
- What was not tested:

**Rule:** If you did not test it, do not imply that you did. AI authorship is acknowledged implicitly — no need to claim direct testing.

---

## 8. Source Log

Document for editor review:
- Which YouTube channels you referenced
- Which Discord communities you checked
- Which Reddit threads informed understanding
- Which articles/docs you consulted
- Which claims come from training data vs. current sources

---

## 9. Editorial Standards

### Must Include
1. Clear verdict with tier ratings
2. What the VR route actually provides
3. Honest assessment of strengths and weaknesses
4. Who should and shouldn't play it

### Must NOT Include
1. Community quotes or "as Reddit user X said"
2. "Tested vs community" framing
3. Specific hardware requirements
4. Version numbers
5. Setup steps (link to guides instead)
6. Hype or marketing language

### Tone
- Direct, skeptical, calm
- Specific, not generic
- Honest about tradeoffs
- Decision-grade, not enthusiasm

---

## 10. Writer Checklist

Before submission, confirm:

- [ ] I stated the tier clearly with both Game Quality and VR Implementation ratings
- [ ] I explained what the VR route provides and doesn't provide
- [ ] I used evergreen language (no version numbers, specific hardware, or dates)
- [ ] I did NOT quote community members or forums
- [ ] I identified who should and shouldn't play this
- [ ] I gave an honest recommendation, not vague positivity
- [ ] I filled in all YAML frontmatter fields
- [ ] I documented my sources for editor review

---

## 11. Editor Rejection Triggers

Editors should bounce the draft back if:
- Tier ratings are missing or use relative framing ("B+ for an injection driver")
- The article quotes community members or forums
- Setup steps are included (link to guides instead)
- Hardware requirements are too specific
- The verdict is vague or hides the actual recommendation
- The piece reads like generic game coverage with VR words bolted on
- Evergreen language is violated (version numbers, specific dates, "as of")

---

## 12. Reference Documents

- `/editorial/tier-rating-system.md` — Tier definitions and dual-factor scoring
- `/editorial/review-methodology-v1.md` — Editorial standards
- `/editorial/brief-template.md` — Assignment parameters for Ian

---

## 13. Bottom Line

A writer's job is to submit a decision-grade package that helps a reader understand:

1. **Is this VR route real and usable?**
2. **Is it worth my time compared to other VR options?**
3. **Who should bother and who shouldn't?**

The tier system exists to answer question #2 on a single scale — whether native VR, mod, or injection driver, they all compete for the same Saturday afternoon.