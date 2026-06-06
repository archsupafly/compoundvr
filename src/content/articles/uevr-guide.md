---
title: "UEVR: Play Unreal Engine Games in VR"
description: "Praydog's UEVR injects full 6DOF VR with stereoscopic rendering, motion controls, and roomscale into nearly any Unreal Engine 4 or 5 game. It's free, it's open source, and it's the single most important tool in the flat-to-VR community. Here's how to get it working, which games to start with, and what to expect."
pubDate: 2026-06-06
lastVerified: 2026-06-06
author: Richard
category: guide
heroImage: /images/articles/uevr-guide-hero.jpg
tags:
  - uevr
  - unreal-engine
  - mods
  - PCVR
  - guide
  - praydog
  - flat-to-vr
---

# UEVR: Play Unreal Engine Games in VR

UEVR doesn't ask permission from the game. It reaches into Unreal Engine's own rendering pipeline and turns on the stereo view that Epic built but never exposed. The result: full 6DOF VR with stereoscopic depth, head tracking, and optional motion controls in hundreds of flat games that were never designed for it.

That's the pitch. The reality is more complicated — but more impressive than you might expect.

## What UEVR Actually Is

UEVR (Universal Unreal Engine VR) is an open-source injection mod created by Praydog. It targets Unreal Engine 4.8 through 5.4, which covers the vast majority of UE games released in the last decade. It's free. It's actively maintained. And it leverages the engine's own stereo rendering system rather than bolting on a fake 3D effect.

This is the critical distinction from injection drivers like VorpX. UEVR isn't approximating depth with Z-buffer tricks. It's activating the native stereoscopic rendering pipeline that Unreal Engine already contains — the same pipeline Epic uses for their own VR projects. When it works, you're getting real, engine-level VR rendering, not an approximation.

**What UEVR provides:**

- **Stereoscopic 3D** via native UE stereo rendering — real depth, not simulated
- **Full 6DOF head tracking** — move and look freely in 3D space
- **Optional motion controls** — 3DOF controller aiming in many games, with UObject inspector for attaching controllers to in-game objects
- **Optional roomscale movement** — player character moves with your physical position
- **Automatic UI projection** — most in-game UI gets reprojected into 3D space
- **Per-game configurations** — save and share settings for individual titles
- **Plugin system** — Lua scripting, C++ plugins, and Blueprint support for community-authored enhancements
- **OpenXR and OpenVR support** — works with Quest, Index, Vive, Pimax, and other headsets

**What UEVR does NOT provide:**

- **Native VR gameplay** — the game still thinks you're using a gamepad. No VR-specific interactions, no hand physics, no grabbed objects
- **Guaranteed stability** — this is injection into software that wasn't designed for it. Crashes happen
- **Performance optimization** — you're rendering twice. On hardware that may already be struggling
- **Comfort features by default** — no vignette, no teleport, no comfort options unless you configure them or a community plugin adds them

## Requirements

Before you install anything, make sure you have:

- **A PCVR-capable headset** connected via Link, Air Link, Virtual Desktop, or SteamVR (Quest 2/3/Pro, Valve Index, HTC Vive, Bigscreen Beyond, Pimax, HP Reverb G2, etc.)
- **A gaming PC** that can handle rendering the game twice at headset resolution
- **.NET 6.0 SDK** installed — UEVR's frontend requires it. [Download from Microsoft](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) (x64 installer, top-left of the table)
- **The target game** running on your PC, launched and waiting at the main menu or in-game

UEVR works with DX11 and DX12 games. It does not work with Vulkan-only titles.

## How to Set Up UEVR

### Step 1: Download UEVR

Get the latest stable release from [github.com/praydog/UEVR/releases](https://github.com/praydog/UEVR/releases). Extract the ZIP to a folder on your PC. You'll find `UEVRInjector.exe` — that's your entry point.

If you want bleeding-edge fixes, the [nightly builds](https://github.com/praydog/UEVR-nightly/releases/latest) are also available. Use stable unless a specific fix you need is only in nightly.

### Step 2: Launch Your Game

Start the Unreal Engine game you want to play in VR. Get it to the main menu or into gameplay — UEVR needs the game's rendering pipeline to be active before injection.

### Step 3: Inject UEVR

1. Launch `UEVRInjector.exe`
2. Select your VR runtime: **OpenVR** (SteamVR) or **OpenXR** (direct, often lower latency)
3. Find your game in the process dropdown
4. If the game has existing VR plugins (some UE games ship dormant VR support), check "Nullify existing VR plugins" — this prevents conflicts
5. Click **Inject**

If the game doesn't appear in the dropdown, try running UEVRInjector as administrator.

### Step 4: Configure Rendering Mode

After injection, press **Insert** (or L3+R3 on a gamepad) to open UEVR's in-game menu. The most important setting is the rendering mode:

- **Native Stereo** — Uses UE's built-in stereo rendering. Best visual quality and performance when it works. Temporal effects (TAA, DLSS, FSR2) work correctly. Try this first.
- **Synchronized Sequential** — Renders both eyes on the same engine tick but sequentially. Fixes many graphical bugs that Native Stereo introduces. Temporal effects will show ghosting/doubling. Turn off motion blur. This is your second option if Native Stereo has issues.
- **AFR (Alternating Frame Rendering)** — Renders each eye on separate frames. Causes eye desync and nausea. Use only if the other two modes are unplayable.

**Always start with Native Stereo.** Switch to Sync Sequential only if you see rendering bugs.

### Step 5: Adjust and Play

From the in-game menu:

- **Camera offset** — Hold RT + left stick to adjust your position relative to the game character
- **Recenter view** — RT + Y
- **Reset standing origin** — RT + X
- **World scale** — Adjust if the world feels too large or too small
- **Snap turn** — Enable for comfort if using roomscale

Save your configuration per game. UEVR stores settings automatically.

## The Three Rendering Modes, Explained Properly

This is where most new UEVR users get confused, so let's be precise.

### Native Stereo

The engine renders both eyes in a single frame using its built-in stereo pipeline. This is real stereoscopic rendering — the same path Epic uses for their own VR projects. When it works, it's the best: no ghosting, correct temporal effects, DLSS/FSR2 compatibility.

Native Stereo can crash or produce graphical artifacts on games where the rendering pipeline wasn't designed to run twice in one frame. Some post-processing effects, certain particle systems, and some engine-level workarounds break under stereo rendering.

### Synchronized Sequential (Sync Sequential)

Both eyes are rendered sequentially within the same engine tick — the game world doesn't advance between eyes, so there's no temporal mismatch. This fixes most Native Stereo rendering bugs.

The trade-off: temporal anti-aliasing (TAA) and motion blur produce ghosting because the engine applies temporal accumulation per-eye but the accumulation history wasn't designed for sequential stereo. **Turn off motion blur.** TAA ghosting is usually tolerable but noticeable.

Sync Sequential has two sub-modes:
- **Skip Draw** — Skips the viewport draw on the next tick. Usually the better option, but particle effects may play at incorrect speed
- **Skip Tick** — Skips the entire engine tick. Fixes particle timing but can introduce other bugs

### AFR (Alternating Frame Rendering)

Each eye renders on a separate frame with the game world advancing time between them. This means your left eye sees the world at time T and your right eye sees it at time T+1/refresh. The result is a constant temporal mismatch between eyes that produces eye strain and nausea in most people.

**Use AFR only as a last resort.** It works for some games where neither Native Stereo nor Sync Sequential is stable, but it's not comfortable for extended play.

## Which Games Work Well

UEVR has been tested with over 600 Unreal Engine titles. "Works" spans a spectrum from "nearly native VR" to "technically runs but don't bother." Here's how to think about it:

### Games That Work Exceptionally Well

These titles have strong community profiles, stable rendering, and meaningful motion control support:

- **Atomic Heart** — First-person UE5 game. Native Stereo works well. Community plugin adds motion controls. One of the showcase UEVR titles.
- **Hellblade: Senua's Sacrifice** — Dark, atmospheric third-person game that gains intensity in VR. Native Stereo stable.
- **Stray** — Third-person cat game. Simple locomotion translates well. Community profile recommended.
- **Sifu** — Third-person martial arts. Motion control plugins exist. Performance-heavy.
- **High on Life** — First-person shooter. Good candidate for motion controls. UE5 with some shader complexity.
- **RoboCop: Rogue City** — First-person with gunplay that benefits from VR aiming. UE5.
- **The Finals** — Fast-paced FPS. Works with Sync Sequential. Performance demands are high.

### Games That Work with Effort

These require specific settings, community profiles, or acceptable compromises:

- **Cyberpunk 2077** (UE5 next-gen update) — Works but performance-intensive. DLSS recommended. Some UI scaling needed.
- **Elden Ring** — Third-person, works with Sync Sequential. No motion controls. The scale of the world in VR is impressive but combat is still gamepad-based.
- **Jedi Survivor** — UE5 with performance issues even on flat. Expect heavy compromise on visual settings.
- **Remnant 2** — Third-person shooter. Sync Sequential recommended. Community profile available.
- **Fortnite** — UE5. Works but anti-cheat may conflict. Frequent updates can break compatibility.

### Games That Are Difficult or Not Recommended

- **Games with aggressive anti-cheat** (Fortnite, Valorant on Vanguard) — May detect injection and block it
- **Games using custom render pipelines** — May have rendering bugs in all modes
- **Extremely performance-heavy UE5 titles** — Nanite and Lumen are demanding in flat; in stereo they may require aggressive quality reduction
- **Online multiplayer games with EAC/BattlEye** — Injection mods can trigger bans. Check community reports before trying

### The Best Way to Find Compatibility

Check these resources before committing time to a game:

- [UEVR Profiles](https://uevr-profiles.com/) — Community-maintained per-game configuration profiles
- [Flat2VR Discord](https://flat2vr.com/) — The central community for flat-to-VR modding, with UEVR-specific channels
- [Steam Curator: UEVR Compatibility](https://store.steampowered.com/curator/44946997-UEVR-Compatibility/) — Compatibility ratings for Steam games
- [UEVR GitHub Issues](https://github.com/praydog/UEVR/issues) — Check for known bugs with specific games

## Motion Controls: The UObject Inspector

UEVR's most ambitious feature is the UObject Inspector — a tool that lets you attach VR motion controllers to any object in the game world. This isn't native VR hand tracking. It's closer to puppeteering.

Here's how it works:

1. Open the UObject Inspector from UEVR's in-game menu
2. Select an in-game object (a weapon, a hand, a flashlight)
3. Attach it to your VR controller
4. The object now tracks your controller's position and rotation

The results vary wildly. Some games have clean object hierarchies that respond well to attachment. Others have animation-driven systems that fight the controller input. Community plugins and Lua scripts can bridge some of these gaps, but this is advanced configuration territory, not plug-and-play.

For games where motion controls work well, the UObject Inspector transforms the experience from "flat game on a headset" to something approaching native VR. For games where it doesn't, you're still playing with a gamepad — but now in stereoscopic 3D with head tracking, which is still a meaningful upgrade.

## Performance: The Reality Check

You're asking your GPU to render the game twice at headset resolution. Here's what that means in practice:

**If the game runs at 90fps on your monitor** — Expect 45-60fps in VR with similar settings. You may need to reduce visual quality.

**If the game barely holds 60fps on your monitor** — It will not be playable in VR without significant quality reduction.

**Practical performance tips:**

- **Use DLSS or FSR2** — These work with Native Stereo and massively improve performance
- **Turn off DLSS Frame Generation** — It causes crashes with UEVR
- **Turn off motion blur** — It produces ghosting in Sync Sequential and doesn't look right in VR
- **Reduce shadow quality first** — Shadows are expensive in stereo and the visual downgrade is minimal in VR
- **Disable volumetric effects** if performance is tight — Fog and volumetric lighting double in cost with stereo rendering
- **Disable hardware-accelerated GPU scheduling** in Windows Graphics settings if you experience stuttering
- **Use OpenXR runtime** instead of OpenVR/SteamVR when possible — it skips the SteamVR overhead layer

A GPU equivalent to an RTX 3070 or better is the realistic minimum for most UE4 games. UE5 titles with Nanite and Lumen may require an RTX 4070 or above for acceptable VR performance.

## Common Problems and Fixes

### Game doesn't appear in UEVR dropdown
Run UEVRInjector as administrator. Some games run at elevated privilege levels and won't be visible otherwise.

### Black screen after injection
Try switching rendering modes. Start with Sync Sequential if Native Stereo produces a black screen. Check that HDR is disabled — UEVR doesn't handle HDR well and games will appear darker than normal if it's on.

### Crashes on injection
- Disable overlays: Rivatuner, ASUS Armoury Crate, Razer Synapse, Overwolf — these hook into the rendering pipeline and conflict with UEVR
- Try the game without any other mods or injectors running
- Check the UEVR GitHub issues for your specific game

### VR headset not detected
Make sure your headset is connected and SteamVR or your OpenXR runtime is running before launching UEVR. UEVR needs an active VR session to inject into.

### Motion controls not working
Not all games support motion controls out of the box. Check [UEVR Profiles](https://uevr-profiles.com/) for a community-made profile that may include controller mappings. The UObject Inspector requires manual configuration for most games.

### Double vision / ghosting
Switch from Native Stereo to Sync Sequential. Turn off motion blur. If you're using TAA, try switching to a different anti-aliasing mode in the game settings.

## The Plugin Ecosystem

UEVR's extensibility is where it separates from every other flat-to-VR tool:

- **Lua scripting** — Full access to UE's reflection system. Hook any UFunction, read and write properties, build custom ImGui interfaces. Scripts can persist settings and communicate with each other.
- **C++ plugins** — Native plugins with callbacks for present, device reset, engine tick, stereo view offset, and XInput state. For modders who need maximum performance and low-level access.
- **Blueprint support** — Add VR features through UE's visual scripting without writing code.

Community plugins exist for specific games that add first-person cameras, motion control schemes, weapon handling, and VR comfort options. The [Flat2VR Discord](https://flat2vr.com/) is the primary hub for finding and sharing these.

## UEVR vs. Other Flat-to-VR Tools

| Feature | UEVR | VorpX | REFramework VR | UUVR |
|---------|------|-------|----------------|------|
| **Price** | Free | $40 | Free | Free |
| **Engine scope** | UE 4.8–5.4 | Any DX9–DX12 | RE Engine only | Unity 5.x+ |
| **Rendering** | Native stereo | Z-buffer / Geometry 3D | Native stereo | Native stereo |
| **Motion controls** | Optional via UObject | Mapped gamepad | Full (game-specific) | Optional |
| **Head tracking** | Full 6DOF | Full 6DOF | Full 6DOF | Full 6DOF |
| **Open source** | Yes | No | Yes | Yes |
| **Community profiles** | Yes | Yes (built-in) | Limited | Growing |
| **Plugin system** | Lua, C++, Blueprint | No | Lua | Limited |

UEVR's main advantage: it uses the engine's own stereo rendering, which produces true stereoscopic depth. VorpX's Z-buffer mode is an approximation. The trade-off is scope — UEVR only works with Unreal Engine games, while VorpX works with nearly anything.

## When to Use UEVR vs. When Not To

**Use UEVR when:**

- You want to play a specific UE4/UE5 game in VR and it doesn't have native VR support
- You have a VR-capable PC and a headset
- You're willing to spend 15-30 minutes configuring settings per game
- You understand that this is injection — not a native port — and bugs are expected

**Don't use UEVR when:**

- The game already has native VR support (use the native version)
- You expect plug-and-play perfection (configuration is required)
- You're playing a competitive multiplayer game with anti-cheat (risk of bans)
- Your PC can barely run the game flat (stereo rendering doubles the GPU load)

## Getting Started: The First-Timer's Checklist

1. **Install .NET 6.0 SDK** — Required for UEVR's frontend
2. **Download UEVR** from [github.com/praydog/UEVR/releases](https://github.com/praydog/UEVR/releases)
3. **Choose a well-supported game** — Atomic Heart, Stray, or Hellblade are safe first picks
4. **Launch the game first**, then UEVRInjector.exe
5. **Select your game** in the process dropdown, choose OpenXR runtime
6. **Inject** — wait for the VR display to activate
7. **Press Insert** for the in-game menu
8. **Start with Native Stereo** — switch to Sync Sequential if you see rendering bugs
9. **Turn off motion blur** in the game's settings
10. **Save your configuration** — UEVR auto-saves per game
11. **Check [UEVR Profiles](https://uevr-profiles.com/)** for community configurations specific to your game

UEVR is the most important tool in the flat-to-VR ecosystem. It's not perfect — it's not a native VR port, it requires configuration, and some games won't work well no matter what you do. But for the games it does work with, the experience of standing inside a world that was never designed for you to enter is worth the effort.

The community is active, the tool is free, and the code is open. Start with a game you already own. The worst case is you spend twenty minutes learning something about Unreal Engine's rendering pipeline. The best case is you find a new way to play a game you love.