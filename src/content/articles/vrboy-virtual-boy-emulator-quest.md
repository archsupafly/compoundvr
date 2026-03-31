---
title: "VRboy: Virtual Boy on Quest"
description: "The Virtual Boy was Nintendo's failed 1995 VR console—a red monochrome nightmare that caused headaches and sold fewer than 800,000 units. VRboy is a free, open-source emulator that finally does justice to the hardware's promise: proper stereoscopic VR on Meta Quest headsets."
pubDate: 2026-03-31
author: Richard
category: guide
tags:
  - VRboy
  - Virtual Boy
  - emulator
  - Quest
  - retro
  - OpenXR
featured: false
heroImage: /images/articles/vrboy-virtual-boy-hero.jpg
---

# VRboy: Virtual Boy Finally Gets the VR Experience It Promised

VRboy is a free, open-source Virtual Boy emulator built specifically for Meta Quest headsets. It transforms Nintendo's infamous 1995 failure into a proper VR experience—stereoscopic 3D, 6DOF positioning, and none of the physical discomfort that doomed the original hardware.

**What you get:** Authentic Virtual Boy emulation with OpenXR stereo rendering, two viewing modes (world-anchored and head-locked), and calibration tools for screen size and depth convergence.

**What you need to know:** Requires sideloading on Quest. You must supply your own legally obtained Virtual Boy ROMs. Only 22 games were ever released for the platform.

---

## The Virtual Boy Legacy

Nintendo's Virtual Boy launched in 1995 as the company's first 3D console—and arguably the first consumer VR headset. It failed spectacularly:

- **Sold fewer than 800,000 units** before discontinuation in late 1996
- **Caused headaches and neck strain** due to its heavy, awkward visor design
- **Red monochrome display** limited visual fidelity
- **Only 22 games released** in its brief lifespan

The hardware had genuine innovation—true stereoscopic 3D via parallax barriers—but the execution was flawed. Players had to lean into a stationary stand. The weight distribution was poor. Games ran at lower framerates to achieve the 3D effect.

VRboy solves the hardware problems while preserving the software library. What was a physical endurance test becomes a proper room-scale VR experience.

---

## How VRboy Works

VRboy uses the **Beetle VB (mednafen/libretro)** emulation core—the same battle-tested core used in RetroArch—wrapped in a native Android OpenXR application designed specifically for Quest headsets.

### Core Architecture

| Component | Technology |
|-----------|-------------|
| Emulation Core | Beetle VB (mednafen/libretro) |
| Rendering | OpenXR stereo renderer with GLES fallback |
| Audio | AAudio output |
| Input | Quest controller mapping to Virtual Boy controls |
| Platform | Native Android (Quest 2+) |

The OpenXR integration is genuine stereo rendering—it's not simply displaying a flat image in VR. The emulator presents separate left and right eye views with proper separation, which is exactly what the Virtual Boy hardware was designed to do but couldn't achieve comfortably.

---

## View Modes

VRboy offers two viewing modes:

### Anchored Mode (Default)

The Virtual Boy display is fixed in world space with full 6DOF movement:
- Walk around the "screen" like it's a physical object in your room
- Grip + stick movement for strafe, forward/back, look adjustment
- Up/down movement for examining from different heights
- World-fixed positioning means the display stays in place as you move

This is how the Virtual Boy always should have worked. The original hardware trapped you in an uncomfortable lean; VRboy lets you treat each game as a display you can approach from any angle.

### Classic Mode (Head-Locked)

The display follows your head like a traditional TV-in-VR experience. This mirrors what you'd get from flat emulation, but with the added benefit of the Virtual Boy's native stereoscopic depth.

---

## Controls

### Basic Input

| Quest Input | Virtual Boy Action |
|-------------|-------------------|
| A | VB A button |
| B | VB B button |
| Y | Start |
| X | Select |
| L1/R1 + Triggers | VB L/R (shoulder buttons) |
| Left Stick / D-pad | Movement |
| R3 | Toggle info window |
| L3 | Open ROM picker (when info window hidden) |

### Anchored Mode Navigation

| Input | Effect |
|-------|--------|
| B (while info window visible) | Toggle Classic ↔ Anchored |
| Hold Grip + Left Stick | Move (strafe/forward/back) |
| Hold Grip + Right Stick | Look yaw/pitch |
| Hold Grip + R/L Trigger | Move up/down |
| Hold Grip + A | Reset walkthrough transform |
| L3 + R3 together | Reset + recenter world anchor |

### Calibration (Info Window Visible)

| Input | Effect |
|-------|--------|
| Hold L + R | Enter calibration mode |
| Up/Down | Increase/decrease screen size |
| Left/Right | Adjust stereo convergence (Classic mode only) |
| A | Reset calibration to defaults |

---

## Supported Games

The Virtual Boy library is small—only 22 games were released. Notable titles include:

- **Wario Land** — The platformer that demonstrates the system's potential
- **Red Alarm** — Wireframe flight combat, the 3D showcase title
- **Mario Clash** — An arcade-style action game
- **Mario's Tennis** — Sports title with actual depth perception
- **Teleroboxer** — First-person boxing, benefits from VR perspective
- **Galactic Pinball** — Standard pinball with enhanced depth

The emulator supports any properly formatted `.vb` or `.vboy` ROM file. Filename conventions are arbitrary—VRboy doesn't require specific naming.

---

## Setup Requirements

### What You Need

- Meta Quest 2, 3, or Pro (Quest 1 is not supported)
- Developer mode enabled for sideloading
- Virtual Boy ROMs (legally obtained)
- Basic familiarity with ADB (Android Debug Bridge) or a sideloading tool like SideQuest

### Installation

The installation process requires sideloading the APK:

1. Download the latest release APK from the VRboy GitHub releases page
2. Enable developer mode on your Quest headset
3. Install via SideQuest, ADB, or your preferred sideloading method:
   ```
   adb install -r vrboy-1.0.2-release.apk
   ```
4. Launch from your Quest's App Library (Unknown Sources section)

### Adding ROMs

Two methods:

**In-App Picker (Recommended):**
- Press L3 to open Android's file picker
- Select your `.vb` or `.vboy` ROM file
- Any filename works—no specific naming requirements

**ADB Push Fallback:**
```
adb push "Wario Land.vb" /sdcard/Download/test.vb
```

VRboy automatically probes fallback paths on startup.

---

## Technical Details

### Build Requirements (For Developers)

- JDK 17
- Android SDK Platform 35
- NDK 26.1.10909125
- CMake 3.22.1

The project uses Git submodules for the Beetle VB core. Clone with:
```
git clone --recurse-submodules https://github.com/Keitark/VRboy.git
```

### Development Status

VRboy reached stable status with v1.0.2 (February 2026). The project is actively maintained with ongoing development focused on:

- Save states + per-ROM configuration
- CI/CD for automated builds
- Release distribution workflow

---

## The Verdict

**Tier: B+**

**Game Quality: C+**

The Virtual Boy library is historically significant but limited. Wario Land and Red Alarm demonstrate genuine creativity with stereoscopic 3D, but the small catalog (22 games) and dated gameplay mechanics show why the platform failed. These are curiosities, not must-play experiences.

**VR Implementation Quality: A-**

VRboy delivers exactly what the Virtual Boy hardware promised but couldn't achieve: comfortable, proper stereoscopic 3D. The OpenXR integration is native, not a wrapper. 6DOF movement in Anchored mode transforms the experience—you can examine the depth layers of each scene rather than being trapped in the original visor's fixed position. Calibration tools for screen size and convergence add genuine value. This is how emulators should handle VR-native platforms.

**Overall:** Recommended for emulation enthusiasts and retro historians who want to experience the Virtual Boy as Nintendo intended. The software library is too small and its titles too dated for mainstream recommendation, but VRboy itself is a genuinely impressive piece of emulation engineering that rescues a failed platform from obsolescence.

---

## Comparison to Alternatives

| Option | Platform | Experience | Price |
|--------|----------|------------|-------|
| VRboy | Quest native | True stereoscopic VR, 6DOF, proper OpenXR | Free |
| Mednafen/RetroArch | Desktop | Flat emulation, requires display | Free |
| Original Hardware | Physical | Authentic experience, physical discomfort | $150-300+ used |

VRboy is the only Virtual Boy emulator offering native VR integration. Mednafen and RetroArch can run Virtual Boy games, but you're viewing them on a 2D screen—defeating the entire purpose of the platform's stereoscopic design.

---

## Technical Summary

| Aspect | Details |
|--------|---------|
| **Price** | Free, open-source (MIT for project code, GPL-2.0 for Beetle VB core) |
| **Platform** | Meta Quest 2, 3, Pro (OpenXR) |
| **Core** | Beetle VB (mednafen/libretro) |
| **Display Modes** | Anchored (6DOF world-fixed), Classic (head-locked) |
| **Color Palette** | Red monochrome (authentic to hardware) |
| **Input** | Quest controller mapped to VB controls |
| **ROM Support** | .vb, .vboy (any filename) |
| **Development Status** | Stable (v1.0.2, Feb 2026), active |

---

## Resources

- **GitHub:** https://github.com/Keitark/VRboy
- **Releases:** https://github.com/Keitark/VRboy/releases
- **Issues/Feedback:** https://github.com/Keitark/VRboy/issues

**Last Verified:** March 2026