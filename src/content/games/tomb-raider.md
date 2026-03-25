---
title: "Tomb Raider (1996) in VR"
description: "A polished OpenXR source port that transforms the 1996 classic into an immersive VR experience. Feature-complete, free, and built by Team Beef using the OpenLara engine. A-tier flat-to-VR adaptation with multiple view modes and full motion controls."
lastVerified: 2026-03-25
featured: false
routeType: "Full VR Mod"
platforms: ['PCVR', 'Quest']
recommendation: Recommended
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - Action-Adventure
  - Platformer
  - Puzzle
technicalTags:
  - OpenLara
  - OpenXR
  - Source Port
experienceTags:
  - Nostalgia
  - Multiple View Modes
  - Classic Game
score: 90
tier: A
verdict: "An exceptional flat-to-VR source port that respects the original while delivering a genuinely new way to experience a classic. Feature-complete, free, and polished by a trusted team. Platforming friction in first-person mode is the primary caveat—treat this as a third-person game with first-person exploration segments."
heroImage: /images/games/tomb-raider-vr-hero.jpg
---

# Tomb Raider (1996) — VR Review
**A Flat-to-VR Assessment**

---

## Executive Summary

| Category | Verdict |
|----------|---------|
| **Overall Rating** | Recommended with caveats |
| **VR Implementation** | Excellent adaptation via OpenLara engine |
| **Setup Complexity** | Moderate — requires file extraction, but tools provided |
| **Comfort** | Moderate concern — 1996 camera DNA creates platforming friction |
| **Playability** | Good in third-person; challenging in first-person VR |

Tomb Raider in VR is a fascinating case study: a nearly 30-year-old game transformed into a genuinely immersive experience that both showcases VR's potential and highlights the fundamental limits of retrofitting games never designed for first-person immersion. **BeefRaiderXR** by Team Beef delivers a polished, feature-rich port that VR enthusiasts and Tomb Raider fans should experience—provided they understand what they're getting into.

**Tier Verdict: A-Tier** — This is a polished, feature-complete source port from a respected team, offered free of charge. The OpenXR implementation is native and well-executed, with multiple view modes, full motion controls, and cross-platform support. The only marks against it are inherent to the source material (1996 tank controls, grid-based platforming) rather than the VR adaptation itself.

---

## The VR Route

**Type:** OpenXR Source Port (not a traditional mod or injection driver)

**Port:** BeefRaiderXR  
**Developer:** Team Beef (led by Simon "Dr. Beef" Brown)  
**Engine Base:** OpenLara (open-source Tomb Raider engine recreation by XProger)  
**Distribution:** Free via SideQuest (Quest/Pico) / GitHub (PCVR)  
**Release Date:** September 30, 2024 (v1.0)  
**Price:** Free (requires owned copy of original game files)

BeefRaiderXR is **not a traditional mod** in the injection-driver sense, nor is it a runtime wrapper. It is a complete **OpenXR source port** of Tomb Raider 1 using the OpenLara engine, which recreates the original game's logic while adding modern rendering, framerate flexibility, and VR-native features. This is closer to GZDoom or QuakeSpasm than to a wrapper-based VR mod.

**Supported Platforms:**
- Meta Quest 1/2/3/3S (standalone)
- Pico 4 (standalone)
- PCVR via OpenXR (Index, Vive, Rift S, WMR, etc.)

---

## Setup Complexity & Current State

### The Good News
Team Beef has streamlined what could have been a nightmare process. The team provides a purpose-built extraction tool called **"Beef Raider Extraction Tool"** (SauronDesktop.exe) that automates most of the complexity.

**Setup Steps:**
1. Install BeefRaiderXR from SideQuest (Quest/Pico) or download from GitHub (PCVR)
2. Own either **Tomb Raider Classic (1996)** from Steam/GOG **OR** **Tomb Raider I-III Remastered (2024)**
3. Run the extraction tool to automatically detect and extract required game files (.phd level data, audio tracks, FMVs)
4. Transfer files to headset (Quest/Pico) or point PC version to extracted folder
5. Launch and select OpenXR runtime (Meta for Air Link; Steam for Virtual Desktop/Steam Link)

**Included Demo:** The SideQuest release includes the official TR1 demo, allowing immediate testing before committing to the full game file extraction.

### The Caveats
- Requires Windows PC for file extraction (even for standalone Quest users)
- .NET 7.0 runtime may need installation
- Must own legitimate copy of original game—no files are bundled
- Audio track conversion is a separate step (though the tool handles this)

### Current State
As of v1.0 (September 2024), the port is **feature-complete and stable**. Team Beef spent approximately 8 months in development, with early access available to Patreon supporters. The public release has polished controls, proper left-handed support, and all advertised features functional.

---

## Controls & Input Methods

BeefRaiderXR offers **four distinct view/control modes**, accessible via the right thumbstick:

### 1. First-Person VR Mode
- **Immersion level:** Maximum
- **Controls:** 6DoF motion controls with VR-native input
- **Features:** Full body/arms IK, head tracking, motion-controlled aiming
- **Best for:** Exploration, combat, atmospheric immersion

### 2. Third-Person VR Mode
- **Immersion level:** High
- **Controls:** Classic tank controls adapted for VR (directional relative to camera)
- **Features:** Camera positioned behind Lara, world scale maintained
- **Best for:** Platforming sections, comfort, classic feel

### 3. Top-Down Diorama Mode
- **Immersion level:** Moderate
- **Controls:** Standard tank controls
- **Features:** Miniature "dollhouse" view of levels, passthrough support
- **Best for:** Puzzle solving, strategic view, novelty

### 4. Mixed Reality Mode (Quest/Pico only)
- **Immersion level:** Variable
- **Features:** Projects the game world into your physical space
- **Best for:** Showing off, unique perspective

### Control Scheme Deep Dive
Team Beef faced the fundamental challenge of adapting **tank controls**—where Lara moves relative to her own facing direction, not the camera—to VR's expectation of camera-relative movement.

**Their solution:** Modified directional pad controls with 6DoF extensions:
- Left stick: Movement (tank-style: up=forward relative to Lara)
- Right stick: Camera/look (in third-person), view mode toggle (click)
- Motion controllers: Aiming weapons (first-person), menu interaction
- Button mapping: Contextual action, jump, draw weapon, roll

**The reality:** Even "modern" VR-adapted controls retain DNA from 1996. Lara still moves on a grid-based system with momentum and animation-driven traversal. This is not a smooth analog modern platformer—it's a 1996 game wearing VR clothes.

Team Beef provides a comprehensive button mapping guide (linked in their documentation) covering special moves like the swan dive, handstand, and ledge-shimmy.

---

## Comfort Considerations

### The Core Problem
Tomb Raider (1996) was built around **fixed camera angles** and **tank controls**. The camera served as a framing device, not an immersive viewport. Moving this to first-person VR creates fundamental tensions:

**Platforming Challenges:**
- The original game expects you to see Lara's body for jump distance estimation
- Precision platforming (a staple of Tomb Raider) becomes guesswork in first-person
- The "run-up" system (holding jump while running for longer leaps) isn't intuitive in VR

**Motion Considerations:**
- No snap/smooth locomotion toggle—the original game only had tank movement
- Head bobbing is present and reportedly cannot be disabled (a significant comfort issue for some)
- No comfort vignette options
- Rapid camera switches when entering/exiting water or triggering events

**Mitigations Provided:**
- Instant toggle between first and third-person (right stick click)
- Third-person mode is genuinely comfortable and solves most platforming issues
- Diorama mode eliminates motion concerns entirely
- High framerate (up to 144fps supported by OpenLara engine) reduces motion sickness

### Verdict on Comfort
**Moderate risk.** Players sensitive to artificial locomotion or head bobbing should expect some discomfort in first-person mode. The ability to instantly switch to third-person for difficult sections is essential—this isn't a bug workaround, it's the intended way to play. Treat first-person as "exploration mode" and third-person as "platforming mode."

---

## Performance Demands

**Verdict: Negligible.**

A game from 1996 runs effortlessly on modern VR hardware:

- **Quest 1/2:** Runs smoothly at 72/90Hz
- **Quest 3:** Crisp rendering, ample headroom for supersampling
- **PCVR:** Can push 120Hz/144Hz easily
- **Resolution:** Supports up to 4K internal resolution (overkill but available)

The OpenLara engine modernizes the renderer with:
- 60fps+ support (original was locked 30fps)
- Improved lighting and colored lighting effects
- Self-shadowing on character models
- Enhanced water effects
- Wet skin shaders after exiting water

**Storage Requirements:** Minimal. Original game is ~500MB; the extracted files are similar.

**Battery Life (Quest):** Excellent. Low GPU/CPU utilization means extended play sessions without thermal throttling or battery drain.

---

## Community Consensus

### The Praise
- **"Game-changing"** — UploadVR calls it "a game-changing way to experience one of the most treasured third-person platformers"
- **Atmosphere:** Players consistently praise how atmospheric the original becomes in VR, despite (or because of) the retro graphics
- **Mixed Reality:** The MR mode, while simple to implement technically, is a crowd-pleaser for showing VR to newcomers
- **IK/Body presence:** Seeing Lara's arms and body animated in first-person adds surprising presence
- **Value:** Free port of a beloved classic with substantial enhancements

### The Criticisms
- **Control learning curve:** Even VR-adapted tank controls take getting used to
- **Head bobbing:** A recurring complaint; some players find it immersion-breaking or uncomfortable
- **Platforming in first-person:** "Rough around the edges" — UploadVR's early preview noted this is still true in the final release
- **Diorama mode limitations:** Some areas don't render correctly until approached
- **Full game setup:** The file extraction process, while streamlined, is still more complex than App Lab/Store purchases

### The Consensus
Tomb Raider VR via BeefRaiderXR is **legitimately special** for fans of the original, but it's not a game to convert VR skeptics. The platforming friction is real, the controls take adjustment, and the 1996 DNA is unmistakable. That said, for players who can adapt—or who primarily play in third-person mode—it's a novel and worthwhile experience that breathes surprising new life into a classic.

The community recognizes this as a **passion project done right**—not a rushed mod, but a carefully crafted port from a team with a track record (Doom 3 VR, Quake VR, etc.) of delivering quality work.

---

## Final Assessment

### Should You Play This?

**Absolutely if:**
- You have nostalgia for Tomb Raider 1
- You enjoy VR "archaeology"—experiencing classics in new ways
- You own either the original or remaster (making this essentially free)
- You can adapt to tank controls or don't mind switching views for platforming

**Consider carefully if:**
- You're sensitive to head bobbing or artificial locomotion
- You expect modern platforming feel (smooth analog movement, intuitive physics)
- You want a polished, friction-free experience (this requires setup and patience)

**Skip if:**
- You've never played Tomb Raider and have no nostalgia buffer
- You need modern comfort options (vignettes, teleport movement, etc.)
- You expect the remaster's updated graphics (this uses original 1996 assets)

### The Bottom Line
BeefRaiderXR is a **triumph of VR porting**—a polished, feature-rich source port that demonstrates what skilled developers can achieve with open-source tools and passion. It's not perfect: the 1996 game's DNA creates inherent friction that no amount of VR adaptation can fully resolve. But for those willing to meet it on its terms, Tomb Raider in VR is a unique and rewarding experience that justifies the effort.

**Recommendation:** Install the demo first. If you can tolerate the tank controls and head bobbing, extract your full game files. Play primarily in third-person for platforming, switch to first-person for exploration and combat. Expect to consult the button mapping guide. And prepare to see a familiar classic through entirely new eyes.

---

## Resources

- **Download:** [SideQuest](https://sidequestvr.com/app/38086/beef-raider-xr-tomb-raider-in-vr) (Quest/Pico) / [GitHub](https://github.com/Team-Beef-Studios/BeefRaiderXR) (PCVR)
- **Extraction Tool:** Included in GitHub releases
- **Team Beef Patreon:** https://www.patreon.com/teambeef
- **OpenLara Engine:** https://github.com/XProger/OpenLara
- **Button Mapping Guide:** [Google Drive](https://drive.google.com/file/d/1VrrJEc0EelIkZ7lWpISFeJrxr8ME8LWU/view)

---

*Review methodology: This assessment is based on community reports, published hands-on impressions from UploadVR and MIXED, official documentation, and analysis of the technical implementation. Flat-to-VR mods are evaluated on: VR implementation quality, setup friction, control adaptation, comfort considerations, performance, and overall value proposition.*

*Last updated: March 2025*
