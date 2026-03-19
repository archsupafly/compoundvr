# Tier Rating System

**Purpose:** This document defines how CompoundVR rates flat-to-VR experiences. It applies to ALL route types: native VR, official hybrids, community mods, and injection drivers.

---

## The Core Question

**Tiers answer one question:** "Is this worth my Saturday afternoon compared to ANY VR option?"

A VR gamer deciding between:
- Half-Life: Alyx (native VR)
- MotherVR (community mod)
- Project CARS VR (official hybrid)
- Dishonored via VorpX (injection driver)

...should be able to compare them on the same scale. The tier system is the great equalizer.

---

## Tier Ratings: S/A/B/C/D/F

| Tier | Meaning | What It Takes |
|------|---------|---------------|
| **S** | Essential — one of the best VR experiences available | Both game quality AND VR implementation must be exceptional |
| **A** | Excellent — highly recommended, minor caveats | Great game + great VR implementation |
| **B** | Good — worth playing, notable limitations | Great game + decent VR, OR decent game + great VR |
| **C** | Average — only for enthusiasts | Great game + weak VR, OR weak game + great VR |
| **D** | Below Average — significant problems | Not recommended except for die-hards |
| **F** | Not Recommended | Fundamental issues that prevent enjoyment |

---

## Dual-Factor Scoring

Every verdict includes two scores that combine into the overall tier:

### Game Quality
- **How good is the underlying game?**
- Independent of VR implementation
- A great game is a great game, whether flat or VR

### VR Implementation Quality
- **How good is the VR experience?**
- Motion controls, hand presence, comfort options, UI adaptation, performance
- Native VR, mods, and injection drivers all compete on this scale

**Key principle:** A great VR implementation can elevate a mediocre game. A terrible VR implementation can drag down a great game.

---

## Examples

| Game | Game Quality | VR Implementation | Overall Tier | Why |
|------|--------------|-------------------|--------------|-----|
| Half-Life: Alyx | A | A+ | **S** | Exceptional game, exceptional VR — the benchmark |
| Half-Life 2 VR Mod | A- | A | **A** | Great game, excellent mod with motion controls |
| MotherVR (Alien: Isolation) | A | B+ | **A** | Great game, solid mod |
| Doom 3 BFG VR | B+ | A- | **A** | Good game, excellent mod, historical significance |
| Project CARS VR | B+ | D | **C** | Good game, incomplete VR (menus require monitor) |
| Ethan Carter VR | A- | D+ | **B** | Great game, dated VR implementation, delisted |
| Dishonored via VorpX | A- | D | **C+** | Great game, terrible VR (injection driver) |

---

## Route Type Awareness

The tier scale is absolute, but route type matters for context:

### Official Hybrid / Native VR
- Developer-made VR support
- Expected: complete implementation, comfort options, VR UI
- A "B" implementation here means something different than a "B" mod

### Full VR Mod
- Community-made with motion controls, rebuilt systems
- Expected: varying quality, ongoing development
- A "B" mod might have rough edges but be genuinely impressive for community work

### Injection Driver
- VorpX/Geo3D stereoscopic injection, no motion controls
- Expected: 3D depth, head tracking, NO hand presence
- A "D" implementation is honest — injection drivers cannot provide what mods can
- Great games with injection drivers can still be C-tier experiences (worth playing if you understand the limitations)

---

## What Injection Drivers CAN and CANNOT Do

For injection driver articles, always explain:

**CAN provide:**
- Stereoscopic 3D (depth perception)
- Head tracking (look around naturally)
- Sometimes automatic calibration (DirectVR, etc.)
- A way to experience flat games "in VR"

**CANNOT provide:**
- Motion controls
- Hand presence
- VR-optimized UI
- Comfort features (teleport, vignette, etc.)
- A transformed experience

The verdict should note: "This is injection driver quality, not port quality."

---

## Verdict Template

Every article verdict follows this format:

```
## The Verdict

**Tier: [LETTER]**

**Game Quality: [LETTER]**
[1-2 sentences explaining why]

**VR Implementation Quality: [LETTER]**
[1-2 sentences explaining why]

[Paragraph summarizing the overall experience and whether it's worth your time]
```

---

## Notes

- Tiers are NOT relative to category. An injection driver doesn't get a "B+ for injection drivers" — it gets an absolute rating.
- The tier answers: "Should I play this instead of something else?"
- Great game + terrible VR = mid-tier experience. You'd be better off playing a B-tier native VR game.
- Great VR + terrible game = mid-tier experience. The VR can't save a bad game.
- S/A tier requires BOTH to be excellent.
- **Multiplatform games:** Briefly mention platform differences (Quest vs PSVR vs PCVR) if relevant, but don't make it the focus unless versions are radically different.

---

## Platforms Field

Every game includes a `platforms` field indicating VR platforms:

- PCVR (SteamVR, Rift, Vive, Index, etc.)
- PSVR (PlayStation VR, PS4)
- PSVR2 (PlayStation VR2, PS5)
- Quest (Meta Quest standalone)
- Pico
- Rift (original Oculus Rift)
- Rift S
- Index (Valve Index)
- Vive (HTC Vive)
- Windows Mixed Reality

Most games will be `['PCVR']`. Multiplatform games list all available platforms.

**Editorial guidance for multiplatform:**
- Don't spend significant article space on platform differences unless versions are radically different
- Brief mention of visual/audio/control differences is useful
- Typical hierarchy: Quest ≤ PSVR ≤ PCVR (but not always — check for each game)
- If versions are extremely different (e.g., Resident Evil 7), consider separate articles