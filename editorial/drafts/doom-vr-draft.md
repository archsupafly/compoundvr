# Doom (1993) VR Review

**Route Type:** Framework-Based / Source Port VR  
**Platforms:** Quest (QuestZDoom), PCVR (gzdoom-VR)  
**Last Verified:** 2026-03-23  
**Evidence:** [Verified] — Compiled from official documentation, community reports, and independent video reviews

---

## Overview

Doom in VR is not a single mod but a category. The 1993 classic that defined the first-person shooter has been ported to VR through community source ports built on the GZDoom/LZDoom engine family. Two primary routes exist: **QuestZDoom** for standalone Quest headsets, and **gzdoom-VR** for PCVR.

This review evaluates the VR framework as a way to experience Doom, Doom II, Final Doom, Hexen, and Heretic—not the underlying games themselves. The question is whether these source ports deliver a credible, playable VR experience worth the setup effort.

---

## The Routes

### QuestZDoom (Quest Standalone)

Developed by Dr. Beef's team (the same group behind Quest ports of Half-Life, Quake, and other classics), QuestZDoom brings the full GZDoom engine to Quest headsets without requiring a PC connection [QuestZDoom.com]. It includes the QuestZDoom Launcher by BaggyG, which handles mod discovery and installation entirely within the headset [QuestZDoom.com, UploadVR].

### gzdoom-VR (PCVR)

A VR fork of GZDoom built on OpenVR, supporting SteamVR-compatible headsets. Developed and tested primarily on Quest via Virtual Desktop, it should work with any OpenVR setup [GitHub/hh79/gzdoomvr]. It offers similar 6DoF weapon handling and mod support, but requires a PC capable of running both Doom and the VR overhead.

---

## Setup Friction

**Score: 3/5** — Manageable but requires attention

QuestZDoom requires sideloading via SideQuest—installing two APKs (the engine and the launcher), accepting permissions, and transferring WAD files if you want to play commercial games [QuestZDoom.com]. The launcher simplifies mod installation, but first-time users face:

- SideQuest installation and headset connection
- Permission dialogs for storage access
- Manual WAD file transfer for owned games (or FreeDoom for free content)
- Understanding load order for mods

The PC route requires compiling or obtaining the VR fork build, understanding OpenVR controller bindings, and managing mod files manually [GitHub/hh79/gzdoomvr]. Neither path is frictionless, but both are documented and achievable for users comfortable with basic modding.

---

## VR Implementation Quality

**Score: 4/5** — Strong implementation with some limitations

Both ports deliver convincing 6DoF VR:

- **Head tracking** is native and smooth
- **Stereoscopy** and world scale work well for Doom's blocky aesthetic
- **Weapon handling** uses tracked dominant-hand controllers with two-handed grip support (off-hand grip stabilizes weapons) [QuestZDoom.com]
- **Haptic feedback** is implemented for weapon fire
- **VR weapon packs** replace flat sprites with 3D models, solving the "cardboard cutout" problem [UploadVR]

The sprite-based enemies and items remain 2D billboards, which is jarring in VR but historically accurate and moddable. The implementation is functional rather than transformative—this is Doom *in* VR, not Doom *reimagined* for VR.

---

## Playability / Completeness

**Score: 5/5** — Fully playable end-to-end

This is a complete engine port, not a demo. Users can play:

- Doom (Ultimate Doom)
- Doom II
- Final Doom
- Hexen
- Heretic
- Thousands of community WADs and mods

The QuestZDoom Launcher categorizes mods by type (Core Games, Map Packs, Gameplay Mods, Weapons, Textures/Sounds) and includes curated recommendations [QuestZDoom.com]. Save/load works. The automap is accessible. Cheats are available if desired.

There are no known progression blockers specific to VR—if a WAD works in GZDoom, it generally works in QuestZDoom [QuestZDoom.com, community reports].

---

## Controls / Input Quality

**Score: 4/5** — Good with minor awkwardness

Default bindings follow VR FPS conventions [QuestZDoom.com, GitHub/hh79/gzdoomvr]:

| Action | Mapping |
|--------|---------|
| Movement | Off-hand thumbstick (smooth or teleport) |
| Turning | Dominant thumbstick (snap or smooth) |
| Fire | Dominant trigger |
| Open door/use | A button (dominant) |
| Jump | B button (dominant) |
| Run | Off-hand trigger |
| Two-hand weapon | Off-hand grip |
| Menu | Menu button (off-hand) |

All buttons are remappable. The dominant-hand grip enables secondary functions (alt-fire, weapon change, etc.). Teleport locomotion is available for comfort [QuestZDoom.com].

The main limitation: Doom's original weapon designs (no iron sights) make precise aiming harder than modern VR shooters. Community mods add laser sights and VR-specific weapon packs to address this [QuestZDoom.com, GitHub/hh79/gzdoomvr].

---

## Comfort

**Score: 4/5** — Moderate intensity but well-contained

Classic Doom is fast. The VR ports respect that speed, which can be intense:

- **Smooth locomotion** at Doom's pace causes vection for sensitive users
- **Snap turn** available (recommended)
- **Teleport** option exists but slows the game significantly
- **No forced camera movement**—cutscenes and intermissions are handled traditionally

The ports include comfort options (vignette settings via GZDoom engine), but the experience remains fundamentally intense due to the source material. This is manageable for experienced VR users; newcomers may need teleport mode initially.

---

## Performance Efficiency

**Score: 3/5** — Moderate issues or substantial tuning required

**Vanilla Doom:** Runs fine on Quest and modest PCs [QuestZDoom.com].

**Modded Doom:** Performance varies dramatically. The GZDoom engine is resource-hungry, and heavy mods (Brutal Doom, high-resolution texture packs, complex gameplay mods) can cause significant frame drops during busy scenes [QuestZDoom.com].

**Quest-specific tuning:**
- Recommended: Set supersampling to 0.9
- Force 60Hz refresh rate for stability [QuestZDoom.com]

**PCVR:** Performance depends on GPU. The OpenVR overhead adds demand on top of GZDoom's already variable requirements.

Users should expect to tune settings and mod loadouts for their hardware.

---

## Stability / Reliability

**Score: 4/5** — Mostly stable with occasional issues

QuestZDoom is mature software from an established porting team. The launcher occasionally requires a trigger click before viewing mod information [QuestZDoom.com]. No widespread reports of crashes or save corruption in community sources.

Stability degrades with heavy mod loads—this is engine limitation, not port-specific breakage. The ports benefit from years of GZDoom testing and Doom community debugging.

---

## Final Scores

| Category | Score |
|----------|-------|
| Setup Friction | 3/5 |
| VR Implementation Quality | 4/5 |
| Playability / Completeness | 5/5 |
| Controls / Input Quality | 4/5 |
| Comfort | 4/5 |
| Performance Efficiency | 3/5 |
| Stability / Reliability | 4/5 |

**Internal Composite Score (weighted):** 3.95/5

---

## Recommendation: **Recommended with Caveats**

Doom in VR is one of the most complete framework experiences available for classic PC gaming. The combination of full game compatibility, extensive mod support, and competent VR controls makes it a genuinely worthwhile way to revisit (or discover) the foundational FPS.

**Caveats:**
- Requires comfort with sideloading and file management
- Performance demands rise quickly with mods
- The 2D sprite aesthetic is authentic but dated
- Fast movement may challenge VR newcomers

**Best for:** VR enthusiasts who want to experience a piece of gaming history with full motion controls; Doom mod veterans curious about their library in VR; anyone seeking a content-rich standalone Quest experience.

**Skip if:** You need native iron sights and modern VR shooting conventions without mods; you want guaranteed smooth performance regardless of mod choices; setup complexity is a dealbreaker.

---

## Evidence Sources

- [QuestZDoom.com] — Official documentation, feature list, installation guide, performance notes
- [UploadVR] — "Playing The Original DOOM In VR On Quest Is A Bloody Blast" (March 2023)
- [GitHub/hh79/gzdoomvr] — PCVR fork documentation, controller bindings, tested mods
- [Community Reports] — Reddit r/QuestZDoom, DoomWorld forums (general consensus)

**Evidence Limitations:** This review is compiled from official documentation and community reports. Direct testing with specific headset hardware was not performed. Performance and comfort assessments represent aggregated user experience, not individual verification.

---

## Related Coverage

- How to install QuestZDoom: [Setup Guide]
- Best Doom VR mods and WADs: [Recommendations]
- Comparison: QuestZDoom vs. PC VR source ports: [Framework Comparison]
