---
title: "UUVR: Universal VR for Unity Games"
description: "Raicuparta's UUVR adds stereoscopic 3D and head tracking to Unity games through Rai Pal. It's simpler than UEVR and more limited — but what it does, it does cleanly. Here's what it covers, what it doesn't, and how to get started."
pubDate: 2026-06-13
lastVerified: 2025-07-03
author: Richard
category: guide
heroImage: /images/articles/uuvr-guide-hero.jpg
tags:
  - uuvr
  - unity
  - mods
  - PCVR
  - guide
  - raicuparta
  - rai-pal
  - flat-to-vr
---

# UUVR: Universal VR for Unity Games

If UEVR is the sledgehammer of flat-to-VR modding — powerful, complex, capable of extraordinary results when you know what you're doing — then UUVR is the precision instrument. It does one thing and it does it well: adding stereoscopic 3D and head tracking to Unity games. No motion controls. No UObject puppeteering. No plugin system. Just clean, engine-level VR viewing.

That simplicity is the point. UUVR (Universal Unity VR) is created by Raicuparta, the same developer behind UEVR and Rai Pal. Where UEVR targets Unreal Engine's vast landscape and tries to give you as much VR functionality as possible, UUVR targets Unity's equally vast library and gives you exactly the part that matters most: seeing the game world in true stereoscopic depth.

## What UUVR Actually Is

UUVR is a free, open-source injection mod (GPL-3.0 licensed) that hooks into Unity's rendering pipeline to produce stereoscopic output and track head movement. It's distributed through Rai Pal, Raicuparta's universal mod manager, and activated in-game with a single keypress.

The key word is "viewing." UUVR gives you:

- **Stereoscopic 3D rendering** — Each eye gets a proper perspective-correct view, producing genuine depth perception. This is real stereo rendering, not a Z-buffer approximation
- **Full 6DOF head tracking** — Your head movement maps to the in-game camera. Lean forward to look around corners. Duck to see under objects. The camera goes where you go
- **UI repositioning and scaling** — v0.4.0 added settings for UI position, scale, shader, and render queue. Game HUDs and menus can be moved into comfortable viewing positions in 3D space
- **Component and object disabling** — v0.4.0 also added the ability to disable specific Unity components or deactivate objects, which can fix rendering conflicts in some games
- **OpenXR and OpenVR support** — Works with Quest, Index, Vive, Pimax, and any headset your runtime supports

What UUVR does NOT give you:

- **Motion controls** — The game still expects gamepad input. Your hands are on a controller, not in VR
- **Free camera movement** — You can't fly around freely. Your head controls the view offset from the game's camera position
- **First-person camera** — Third-person games stay third-person. UUVR doesn't reposition the camera to the character's eyes
- **VR-specific interactions** — No grabbing, no pointing, no hand physics. The game's input system is untouched
- **Plugin or scripting system** — No Lua, no C++ plugins, no Blueprint. UUVR has no extensibility layer

If you're coming from UEVR expecting feature parity, recalibrate. UUVR is a viewing tool, not a VR transformation engine.

## How UUVR Works Technically

Unity games (specifically those built on IL2CPP or Mono scripting backends) expose a rendering pipeline that UUVR hooks into at runtime. The injection process works differently depending on the game's scripting backend:

### IL2CPP Backend (Modern)

Most Unity games released after 2018 use IL2CPP, which compiles C# code to C++ ahead of time for performance and obfuscation. UUVR's IL2CPP injection:

1. Attaches to the game process via DLL injection
2. Patches into the camera rendering system at the native level
3. Creates a second camera for the stereoscopic eye
4. Routes head tracking data from OpenXR/OpenVR to the camera transform

This is the backend where UUVR works best. Most modern Unity games use IL2CPP.

### Mono Backend (Legacy)

Older Unity games use the Mono runtime, which keeps C# as managed code. UUVR supports Mono injection as well, though compatibility can be spottier depending on the specific Unity version and how the game was compiled.

### Important Limitation

UUVR supports Unity metadata versions 23 through 29. Games built with newer Unity versions that produce metadata version 31 or higher will throw a `FormatException` on injection. This is a known limitation tracked in the project's GitHub issues. If your game uses a Unity version that's too new, UUVR simply won't inject. There's no workaround short of waiting for UUVR to add support.

## Requirements

Before you install anything:

- **A PCVR-capable headset** — Quest 2/3/Pro via Link/Air Link/Virtual Desktop, Valve Index, HTC Vive, Bigscreen Beyond, Pimax, HP Reverb G2, or any OpenXR-compatible headset
- **A gaming PC** — UUVR renders the game twice. The same stereo rendering performance math applies as with UEVR
- **Rai Pal** — UUVR is distributed and managed through Raicuparta's mod manager. This is the primary installation method. A manual installation path exists for advanced users (via the GitHub releases page), but Rai Pal handles version management and game detection automatically
- **A Unity game** running on your PC

## How to Set Up UUVR

### Step 1: Install Rai Pal

Download Rai Pal from [github.com/Raicuparta/rai-pal/releases](https://github.com/Raicuparta/rai-pal/releases). It's available for Windows and Linux. The Windows version is a single executable — no installer needed.

Rai Pal automatically scans your system for installed games from:
- **Steam** — both installed and owned games
- **GOG** — both installed and owned games
- **Epic Games Store** — both installed and owned games
- **Itch.io** — both installed and owned games
- **Xbox PC** — installed games marked as moddable

For games from other sources (humble Bundle, standalone installs, etc.), use the "Add Game" button or drag the game's executable directly onto the Rai Pal window.

### Step 2: Find Your Game

Rai Pal detects the game engine and Unity version for installed games automatically. Look for games marked as Unity in the installed games tab. If your game doesn't appear, add it manually.

### Step 3: Install UUVR Through Rai Pal

1. Select your game in Rai Pal
2. Find UUVR in the available mods list
3. Click Install — Rai Pal downloads the correct version and sets up the injection
4. Rai Pal also manages updates. When a new UUVR version is released, Rai Pal will prompt you to update

This is the recommended path. Manual installation via the GitHub releases ZIP is possible but requires you to extract files to Rai Pal's mods folder and manage versions yourself. For most users, Rai Pal is the way.

### Step 4: Launch and Activate

1. Start your game normally
2. Press **F3** to activate UUVR — the VR view should appear in your headset
3. Press **F5** to toggle the in-game UI overlay in VR (added in v0.3.2)
4. If the VR view doesn't activate, check that your headset is connected and your OpenXR/OpenVR runtime is running before launching the game

That's it. No configuration step. No injector to select processes. No rendering mode to choose. UUVR activates the stereo view and starts head tracking.

### Step 5: Adjust Settings (v0.4.0+)

The v0.4.0 release (July 2025) added in-game settings accessible through the overlay:

- **UI Position** — Move the game's HUD and menus to a comfortable position in 3D space
- **UI Scale** — Resize UI elements for VR viewing
- **UI Shader** — Change how UI is rendered in the stereo view
- **UI Render Queue** — Adjust rendering order to fix UI appearing behind world geometry
- **Components to Disable** — Turn off specific Unity components that conflict with VR rendering
- **Objects to Deactivate** — Remove specific game objects that cause rendering issues

These settings are per-game and persist across sessions.

## The UUVR vs. UEVR Comparison

Since both tools come from the same developer and serve similar communities, the comparison is inevitable and important.

| Feature | UUVR | UEVR |
|---------|------|------|
| **Target engine** | Unity | Unreal Engine 4.8–5.4 |
| **Price** | Free | Free |
| **Open source** | Yes (GPL-3.0) | Yes |
| **Stereoscopic 3D** | Yes — engine-level | Yes — engine-level |
| **Head tracking** | Yes — 6DOF | Yes — 6DOF |
| **Motion controls** | No | Optional via UObject Inspector |
| **Free camera** | No | Optional |
| **Roomscale movement** | No | Optional |
| **Plugin system** | No | Lua, C++, Blueprint |
| **Configuration depth** | Basic (v0.4.0+) | Extensive per-game settings |
| **Community profiles** | Growing | Mature (600+ games) |
| **Installation** | Rai Pal (recommended) or manual | Manual injector |
| **Maturity** | Early (v0.4.0, July 2025) | Mature (v1.0+, years of development) |

The fundamental difference: UEVR tries to give you as close to native VR as injection can achieve. UUVR gives you the VR view and nothing else. For some games and some players, that's exactly enough.

## When UUVR Is the Right Tool

**Use UUVR when:**

- You want to experience a Unity game's world in stereoscopic 3D with head tracking
- The game is third-person and you want to view it from a VR perspective without motion controls
- You want a quick, simple setup — press F3, see in VR, done
- The game doesn't have native VR support and you don't need controller interaction
- You're using Rai Pal already for UEVR and want a unified mod management experience

**Don't use UUVR when:**

- You need motion controls — UUVR doesn't provide them
- You want first-person camera positioning — UUVR preserves the game's camera perspective
- You're playing a game that already has native VR support
- You need per-game deep configuration — UUVR's settings are still basic
- Your game uses a Unity version with metadata version 31+ — UUVR will fail to inject

## Games That Work Well With UUVR

UUVR's compatibility is broader in theory (Unity games are everywhere) but narrower in practice than UEVR's. Because UUVR only provides viewing, the games that shine are ones where simply *being there* adds significant value.

### Games Where UUVR Excels

**Atmospheric exploration games** gain the most from stereoscopic viewing:
- **Outer Wilds** — The solar system in true 3D is breathtaking. Seeing planets loom overhead with genuine depth perception transforms the exploration experience
- **Subnautica** — Already has experimental VR, but UUVR provides a cleaner stereo view for the base game
- **Firewatch** — The Wyoming wilderness in stereoscopic depth is gorgeous. Third-person view works naturally
- **Dredge** — Fishing and ocean horror in 3D. The fog and lighting effects gain real atmosphere
- **DARQ** — Has official VR, but UUVR can work with the flat version for comparison
- **Stray** — Also works with UEVR, but the Unity version gains genuine presence in VR

**Strategy and management games** where spatial awareness helps:
- **Cities: Skylines** — Overhead city view with depth makes density and zoning more readable
- **RimWorld** — 2D colony sim gains surprising depth from stereo rendering
- **Survival: Fountain of Youth** — Has active community UUVR discussion; exploration benefits from 3D

**Slow-paced third-person games** where the environment matters more than reflexes:
- **Death Stranding** (PC version) — The landscape and weather systems are stunning in stereoscopic 3D
- **Firewatch** — Worth mentioning twice. The art direction was made for VR viewing

### Games Where UUVR Struggles

- **Fast-paced first-person shooters** — Without motion controls, you're still using a gamepad. VR viewing alone doesn't transform FPS gameplay
- **UI-heavy games** — Even with v0.4.0's UI settings, some games have UI that doesn't adapt well to VR viewing
- **Online multiplayer games with anti-cheat** — Same risk as UEVR. Injection can trigger bans
- **Games on very new Unity versions** — Metadata version 31+ games will fail to inject

### Finding Compatible Games

- **Rai Pal's game detection** — Shows which of your installed games are Unity and what version they're running
- **[Flat2VR Discord](https://flat2vr.com/)** — UUVR-specific channels with compatibility reports
- **[UUVR GitHub Issues](https://github.com/Raicuparta/uuvr/issues)** — Search for your game to see known problems
- **[Rai Pal's compatibility data](https://github.com/Raicuparta/rai-pal)** — Engine detection helps predict which games might work

## Performance Considerations

The same stereo rendering math applies here as with any flat-to-VR tool: you're rendering the game twice. UUVR is lighter than UEVR (no plugin system, no UObject inspector, no per-game configuration overhead), but the GPU cost of stereo rendering is unavoidable.

**Practical guidance:**

- **If the game runs at 90fps flat** — Expect 45-60fps in VR. Reduce shadow quality and volumetric effects
- **If the game barely holds 60fps flat** — It will not be playable in VR without aggressive quality reduction
- **UUVR has less per-frame overhead than UEVR** — No stereo mode selection, no plugin callbacks, no UObject inspection. The performance delta between flat and VR should be smaller than with UEVR on equivalent hardware
- **Disable in-game anti-aliasing if you're using OpenXR's own AA** — Double AA tanks performance
- **Turn off motion blur** — It produces ghosting in stereo viewing

A GPU equivalent to an RTX 3060 or better is the realistic minimum for most Unity games in UUVR. Simpler 2D or low-poly titles will run on less.

## Common Problems and Fixes

### Game doesn't appear in Rai Pal
Use the "Add Game" button or drag the executable onto the Rai Pal window. Not all game stores are fully supported for automatic detection.

### F3 doesn't activate VR view
- Make sure your headset is connected and your OpenXR/OpenVR runtime is active before launching the game
- Check that UUVR was installed through Rai Pal for the correct game — it needs to match the specific executable
- Try running Rai Pal as administrator if the game runs at elevated privileges

### Black screen after activation (Quest 3 users)
This is a known issue tracked in GitHub issue #37. The Mono Modern injection path can produce black screens on Quest 3 via Link/Air Link. Try switching to the IL2CPP injection path if available, or use Virtual Desktop as an alternative connection method.

### "Unsupported metadata version" error
Your game uses a Unity version that produces metadata version 31 or higher, which UUVR doesn't support yet. There's no workaround. Check the GitHub issues to see if support for your version is in progress.

### BepInEx crashes after installing UUVR
Known issue (GitHub #35). UUVR's IL2CPP Modern injection can conflict with BepInEx. If you need both, try the Mono injection path or remove BepInEx temporarily.

### UI is too close or too small in VR
v0.4.0's UI position, scale, and shader settings address this. Press F5 to access the overlay and adjust. Settings persist per game.

## The Rai Pal Ecosystem

UUVR can't be fully understood without understanding Rai Pal, because Rai Pal is how most people interact with it.

Rai Pal (v0.18.1 as of April 2026) is Raicuparta's universal mod manager. It's a desktop application that:

- **Auto-discovers your games** from Steam, GOG, Epic, Itch.io, and Xbox PC
- **Detects game engines and versions** — knows if a game is Unity, what version, and which scripting backend (IL2CPP or Mono)
- **Manages UUVR and UEVR installations** — download, install, update, and launch mods for specific games
- **Provides a unified interface** — one app for both major flat-to-VR injection tools

Rai Pal is the recommended (and effectively required) way to install and manage UUVR. The GitHub releases page has a manual download, but Rai Pal handles version management, game detection, and mod activation automatically. If you're using UEVR already, you already have Rai Pal. UUVR lives in the same ecosystem.

The integration is meaningful: Rai Pal knows which of your games are Unity, what version they're running, and which injection path to use. This eliminates the guesswork that makes injection tools intimidating for new users.

## UUVR vs. VRGIN

Unity has another flat-to-VR injection tool: VRGIN (VR Generic Injection Framework), which powers VR mods for games like Firewatch, Dear Esther, and DARQ. The comparison matters.

**VRGIN** is a per-game framework. Each game that uses it gets a custom-tailored VR implementation — motion controls, camera adjustments, UI repositioning, all configured for that specific title. VRGIN mods are essentially game-specific VR ports built on a shared framework.

**UUVR** is a universal injector. It applies the same stereo rendering and head tracking to every Unity game, with no per-game customization beyond v0.4.0's basic UI settings. This means wider compatibility but much less depth.

The trade-off is straightforward:
- If a game has a dedicated VRGIN mod, use that. It will always produce a better result than UUVR for that specific game
- If a game has no dedicated VR mod, UUVR is the only option for seeing it in VR
- VRGIN mods exist for maybe a dozen Unity games. UUVR works with hundreds

## The Current State (June 2026)

UUVR is at v0.4.0 (released July 2025). It's early software with active development:

**What works reliably:**
- Stereoscopic 3D rendering in IL2CPP Unity games
- Head tracking across major OpenXR/OpenVR headsets
- Basic per-game UI adjustment settings (v0.4.0)
- Installation and management through Rai Pal

**What's still developing:**
- Mono backend compatibility (spottier than IL2CPP)
- Metadata version 31+ support (not yet available)
- Per-game profile sharing (no community profile system yet, unlike UEVR)
- Standalone operation without Rai Pal (feature requested, not yet implemented — GitHub issue #46)

**What's unlikely to change:**
- No motion controls planned — UUVR's architecture is viewing-only
- No free camera or roomscale — same architectural constraint
- No plugin system — the simplicity is a design choice

## Getting Started: The First-Timer's Checklist

1. **Install Rai Pal** from [github.com/Raicuparta/rai-pal/releases](https://github.com/Raicuparta/rai-pal/releases)
2. **Let it scan your library** — it will find Unity games automatically from Steam, GOG, Epic, and Itch
3. **Select a game** and install UUVR through Rai Pal's mod interface
4. **Launch the game** through Rai Pal or normally
5. **Press F3** while in-game to activate VR
6. **Put on your headset** — you should see the game in stereoscopic 3D
7. **Press F5** to access UI settings if the HUD needs adjustment (v0.4.0+)
8. **Play with a gamepad** — this is a viewing experience, not a VR interaction experience
9. **Adjust settings per game** — UI position and scale persist automatically

## The Bottom Line

UUVR does less than UEVR. It's not trying to do more. It gives Unity games stereoscopic depth and head tracking — two features that transform how a game *looks* without touching how it *plays*. For atmospheric games, exploration games, and anything where being *inside* the world matters more than interacting with it, that's enough.

The integration with Rai Pal makes it the most accessible flat-to-VR tool available. One install, one keypress, you're in VR. No configuration menus, no rendering mode selection, no per-game setup. For a tool at v0.4.0, that simplicity is both its strength and its ceiling.

If you want to *play* a game in VR with motion controls and VR-specific interactions, UEVR or a game-specific mod is the right tool. If you want to *see* a game in VR — to stand inside its world and look around with your own eyes — UUVR delivers that experience with minimum friction.

The tool is free, the code is open, and Raicuparta's track record with UEVR suggests the foundation is solid. Start with a game you already own. The worst case is ten minutes of setup for a new perspective on a familiar world.