---
title: "REFramework VR: Resident Evil and Beyond in VR"
description: "Praydog's REFramework turns Capcom's RE Engine into a VR platform. Full stereoscopic 6DOF VR with motion controls for Resident Evil 2, 3, 4, 7, 8, and 9 — plus Devil May Cry 5, Monster Hunter, and every other RE Engine game. Free, open source, and the most polished flat-to-VR mod in existence. Here's how to set it up, what each game plays like, and what to expect."
pubDate: 2026-06-20
lastVerified: 2026-06-20
author: Richard
category: guide
heroImage: /images/articles/reframework-vr-guide-hero.jpg
tags:
  - reframework
  - resident-evil
  - praydog
  - mods
  - PCVR
  - guide
  - flat-to-vr
  - re-engine
  - capcom
---

# REFramework VR: Resident Evil and Beyond in VR

REFramework doesn't inject VR into a game. It injects VR into an engine.

Capcom's RE Engine powers every major Capcom release since 2017 — Resident Evil 2 through 9, Devil May Cry 5, Monster Hunter Rise and Wilds, Street Fighter 6, Dragon's Dogma 2. REFramework, created by Praydog (the same developer behind UEVR), hooks into the RE Engine's own rendering and input systems and turns on VR that was never meant to exist. The result is full stereoscopic 6DOF VR with motion controls across six Resident Evil games and counting — the most polished flat-to-VR experience in the community modding scene.

This is not VorpX approximating depth from a Z-buffer. This is not a side-by-side 3D shader. REFramework activates real stereoscopic rendering through the engine's DX11 and DX12 pipelines. When it works, you're getting engine-level VR that rivals official conversions — and in some cases, surpasses them.

## What REFramework Actually Is

REFramework is an open-source modding framework for RE Engine games. VR is one of its features, but the framework also provides mod loading, Lua and C# scripting, a native C++ plugin API, an object explorer, behavior tree editing, free camera, first-person mode, FOV sliders, ultrawide fixes, and more.

For VR purposes, REFramework provides:

- **Stereoscopic 3D rendering** through the RE Engine's native DX11/DX12 pipeline — real depth, not simulated
- **Full 6DOF head tracking** — look around freely, lean, peek, and move your head independently of the character
- **Motion controller support** for RE2, RE3, RE7, RE8, and RE9 — hand-tracked weapon aiming, two-hand grip, physical interactions
- **Roomscale movement** — your physical position maps to the game world
- **Comfort options** — decoupled camera pitch, vignette toggle, world scale adjustment, snap turn scripts
- **First-person mode** for RE2 and RE3 — full camera override from third person to first
- **OpenVR and OpenXR support** — works with Quest, Index, Vive, Pimax, Bigscreen Beyond, and other PCVR headsets
- **Alternative Eye Rendering (AER)** — optional rendering mode that can improve performance on weaker hardware

What REFramework does NOT provide:

- **VR-native gameplay design** — the games still think you're using a gamepad. No VR-specific interactions exist beyond what motion control mods add
- **Perfect cutscene rendering** — cutscenes were designed for fixed cameras. Characters may disappear, textures may flicker, geometry may be missing when you look around during cinematic sequences
- **Guaranteed stability** — this is a mod hooking into software that wasn't built for VR. Crashes and glitches happen
- **Scope functionality** — scopes and visors do not render correctly in VR. This is a known REFramework limitation across all supported games

## Supported Games

REFramework's monolithic DLL works across every supported RE Engine game. The same `dinput8.dll` detects the game at runtime and loads the correct configuration. Here's the full list:

### Resident Evil Series

| Game | VR Support | Motion Controls | Notes |
|------|-----------|----------------|-------|
| **Resident Evil 2 (2019)** | Full 6DOF | Yes | First-person mode, manual flashlight, IK body |
| **Resident Evil 3 (2020)** | Full 6DOF | Yes | First-person mode, manual flashlight, IK body |
| **Resident Evil 4 (2023)** | Full 6DOF | Via RE4VR addon (Talemann) | First-person via mod, no native IK |
| **Resident Evil 7: Biohazard** | Full 6DOF | Yes | Already first-person — most natural VR conversion |
| **Resident Evil Village (2021)** | Full 6DOF | Yes | IK body, body part toggles |
| **Resident Evil Requiem (2026)** | Full 6DOF | Via RE9VR addon (Talemann) | Manual reloading, holsters with haptics, first VR mod with built-in manual reload |

### Other RE Engine Games

| Game | VR Support | Motion Controls | Notes |
|------|-----------|----------------|-------|
| **Devil May Cry 5** | Full 6DOF | No | Generic VR, some UI issues |
| **Monster Hunter Rise** | Full 6DOF | No | Generic VR, audio positioning issues |
| **Monster Hunter Wilds** | Full 6DOF | No | Generic VR |
| **Monster Hunter Stories 3** | Full 6DOF | No | Generic VR |
| **Street Fighter 6** | Full 6DOF | No | Generic VR |
| **Dragon's Dogma 2** | Full 6DOF | No | Generic VR |
| **Ghosts 'n Goblins Resurrection** | Full 6DOF | No | Uses RE8 build |
| **Apollo Justice: Ace Attorney Trilogy** | Full 6DOF | No | Uses DD2 build |
| **Kunitsu-Gami: Path of the Goddess** | Full 6DOF | No | Uses DD2 build |
| **Onimusha 2: Samurai's Destiny** | Full 6DOF | No | Uses MHWilds build |

The Resident Evil games are the headline act. Everything else works at the 6DOF level — you get stereo rendering and head tracking — but without motion controls or game-specific VR adaptations, they're more "watch in 3D" than "play in VR."

## Requirements

Before installing, make sure you have:

- **A PCVR-capable headset** connected via Link, Air Link, Virtual Desktop, or SteamVR (Quest 2/3/Pro, Valve Index, HTC Vive, Bigscreen Beyond, Pimax, HP Reverb G2, etc.)
- **A gaming PC** that can handle rendering the game twice at headset resolution. RE Engine games are visually demanding — RE9 in particular needs serious GPU horsepower
- **SteamVR** installed (or an OpenXR runtime if you're switching to OpenXR)
- **The target game** installed on PC (Steam version recommended)

REFramework supports both DX11 and DX12. Some games work better on one than the other — see the troubleshooting section.

## How to Set Up REFramework VR

### Step 1: Download REFramework

Get the latest stable release from [github.com/praydog/REFramework/releases](https://github.com/praydog/REFramework/releases). For bleeding-edge fixes and improved TAA/performance, check the [nightly builds](https://github.com/praydog/REFramework-nightly/releases/) or the [pd-upscaler builds](https://github.com/praydog/REFramework/actions) (GitHub account required for Actions builds).

The pd-upscaler builds are particularly important — they fix TAA completely and add optional DLSS, FSR2, and XeSS support. These will eventually merge into stable, but for now they're separate.

### Step 2: Extract to Your Game Folder

Extract the entire ZIP file into your game's install directory. For example:

```
G:\SteamLibrary\steamapps\common\RESIDENT EVIL 2 BIOHAZARD RE2\
```

The key file is `dinput8.dll` — this is the hook that REFramework uses to load before the game's own DLLs. The ZIP also includes `openvr_api.dll` and `openxr_loader.dll` for VR runtime support.

### Step 3: Configure In-Game Settings

Before launching in VR, adjust these in-game settings:

- **Display Mode:** Windowed (not Borderless Windowed — borderless causes aspect ratio issues in VR)
- **Screen Resolution:** Set to your desired render resolution (the headset resolution takes over once VR is active)
- **Refresh Rate:** Match your headset's refresh rate (72Hz, 90Hz, 120Hz)
- **Frame Rate:** Match refresh rate
- **FidelityFX Super Resolution:** Off (let REFramework or your headset handle supersampling)
- **HDR:** Off (HDR causes rainbow visual issues and black screens in VR — this is non-negotiable)

### Step 4: Launch the Game

Start the game normally through Steam. REFramework loads automatically. If SteamVR is running, VR mode activates on launch.

If the game opens in SteamVR Theater Mode instead of true VR: go to SteamVR Settings → Dashboard → turn off "Present Non-VR Applications on Theater Screen Upon Launch."

### Step 5: Open the REFramework Menu

**With motion controllers (OpenVR):** Aim at the palm of your left hand with your head and right hand. Don't press anything — the wrist menu overlay appears automatically.

**On desktop:** Press the **Insert** key. This opens the desktop version of the menu. Useful for initial setup before putting on the headset.

**Via config file:** Settings can also be changed in `re2_fw_config.txt` (or the equivalent for your game) in the game's install folder. This is the fallback if the menu won't open.

### Step 6: Configure VR Settings

In the REFramework menu under the **VR** tab, set:

- **Enable VR:** On
- **Decoupled Camera Pitch:** On (prevents vertical camera movement that causes motion sickness)
- **Vignette:** Off (or on if you're sensitive to motion — your call)
- **World Scale:** Adjust to taste. Default is usually fine, but some games feel better at slightly different scales
- **Render method:** Try both OpenVR and OpenXR to see which performs better (see below)

### Step 7: Motion Controls (RE2/RE3/RE7/RE8)

For games with native motion control support, your VR controllers are automatically mapped:

- **Right hand:** Weapon aiming and firing (hold right grip to aim, right trigger to fire)
- **Left hand:** Two-hand grip (bring left hand near right hand to stabilize weapons)
- **Left joystick:** Smooth locomotion
- **Right joystick:** Smooth turning
- **Weapon switching:** Left trigger + joystick (on supported controllers), or d-pad bindings
- **Map:** Hold controller behind your head/over your shoulder and press the inventory button (RE2/RE3 gesture)

If controls don't work, unplug any gamepad — gamepads conflict with VR controls. Not all controllers have proper default bindings; you may need to manually bind them through SteamVR's controller binding interface.

## OpenVR vs OpenXR

REFramework defaults to OpenVR (SteamVR). Switching to OpenXR can improve performance significantly on some systems — the most notable gains are in DX12 games.

**To switch to OpenXR:**

1. Delete `openvr_api.dll` from your game folder
2. Make sure `openxr_loader.dll` is present (it comes with the REFramework ZIP)
3. Set your OpenXR runtime to your headset's native runtime (Oculus OpenXR for Quest, etc.) — not SteamVR's OpenXR layer, unless you're using Virtual Desktop

**OpenXR trade-offs:**

- No wrist overlay menu (you'll need to use the Insert key on desktop or the config file)
- Less expressive controller binding options
- Not all headsets have a dedicated OpenXR runtime

If you're using a Quest headset with Virtual Desktop or Air Link, try OpenXR with the Oculus runtime first. If you're on a Valve Index or a headset that runs through SteamVR natively, OpenVR may be fine.

## Game-by-Game Guide

### Resident Evil 2 (2019)

RE2 is the flagship REFramework VR experience. Third-person by default, with an optional first-person mode that completely overrides the camera.

**What works well:**
- Motion controls with IK body — you see your arms, hands, and weapon
- First-person mode transforms the game into a proper VR horror experience
- Raccoon City Police Department in VR is genuinely terrifying
- Manual flashlight adds to immersion

**Known issues:**
- Softlock can occur in the Birkin fight if it goes on too long — disable FirstPerson if this happens, then re-enable
- Cutscenes show the flaws of fixed-camera design — characters disappear, geometry is missing
- The game's vignette is aggressive by default — turn it off in the REFramework menu for a better VR experience

**Recommended settings:** First-person mode on, decoupled pitch on, vignette off, motion controls on.

### Resident Evil 3 (2020)

RE3 plays almost identically to RE2 in VR — same engine, same control scheme, same motion control support. The tighter, more action-focused campaign translates well.

**What works well:**
- Same excellent motion control implementation as RE2
- First-person mode available
- Nemesis encounters are intense in VR

**Known issues:**
- Same cutscene issues as RE2
- Shorter campaign means less VR content overall

### Resident Evil 4 (2023)

RE4 is the most complex REFramework VR case. Base REFramework provides 6DOF VR but no motion controls — those come from the **RE4VR addon mod** by Talemann, available on [Nexus Mods](https://www.nexusmods.com/residentevil42023/mods/5682).

**What works well:**
- RE4VR addon provides full first-person motion controls
- Manual reloading via the Immersion Enhancer mod (left grip near your hip to simulate reloading)
- Separate Ways DLC is playable
- Community QoL scripts improve two-hand aiming, recoil, haptics, and scope handling

**Known issues:**
- No native IK — only hands are visible, no arms or body
- Map is difficult to view and partially unusable (REFramework issue, not mod-specific)
- Minecart and jetski sections are glitchy in VR
- Thermal scope doesn't work properly — workaround mods available
- Mounted gun in Chapter 15 can't aim up/down — disable decoupled pitch to get past this section
- Keyboard/mouse prompts appear in-game and menus
- Chainsaw demo does not work with REFramework

**Recommended setup:** Install REFramework, then RE4VR addon, then QoL scripts from the community. Use the auto-installer from [biohazardvr.com](https://www.biohazardvr.com/re4) if available — it bundles the essential improvements.

### Resident Evil 7: Biohazard

RE7 is the most natural VR conversion in the RE Engine lineup. The game is already first-person — REFramework simply adds stereoscopic 3D, head tracking, and motion controls to an experience that was already designed from the ground up as a first-person horror game.

**What works well:**
- First-person by design — no camera mode switching needed
- Motion controls with hand-tracked aiming
- The Baker plantation in VR is one of the scariest experiences in gaming
- Atmosphere and lighting translate beautifully to stereo rendering

**Known issues:**
- Some scripted sequences take camera control back temporarily
- Cutscene issues are less severe than in RE2/RE3 since the game is already first-person

**Recommended settings:** Motion controls on, decoupled pitch on, vignette off (unless you want maximum horror dread). This is the game to start with if you're new to REFramework VR.

### Resident Evil Village (2021)

RE8 builds on RE7's first-person foundation but adds more varied environments — from villages to castles to factories. Motion controls are fully supported with IK body.

**What works well:**
- First-person with IK body — see your arms, hands, and body
- Body parts can be selectively disabled in the REFramework menu if they get in the way
- Castle Dimitrescu in VR is spectacular
- The scale of the environments shines in stereo 3D

**Known issues:**
- Startup crashes and stutters (killing enemies, taking damage) — REFramework includes built-in fixes for these
- Same scope/visor limitations as other games

**Recommended settings:** Motion controls on, disable body parts that clip, decoupled pitch on.

### Resident Evil Requiem (2026)

RE9 is the newest addition and the most feature-complete REFramework VR experience thanks to the **RE9VR addon mod** by Talemann. Released alongside the game in February 2026, it's the first REFramework VR mod with built-in manual reloading and holsters.

**What works well:**
- Full motion controls via RE9VR addon
- Manual reloading — hold left grip near your left hip to pull out a magazine, insert it into the gun, then rack the slide
- Three holsters with haptic feedback
- First-person mode (switchable in game settings)
- Dual protagonist switching between Grace Ashcroft and Leon Kennedy
- Costumes can be changed via Bonus Settings in the main menu

**Known issues:**
- Low-res texture bug — REFramework's default rendering causes textures to degrade over time. Fix: use PureDark's AFW Rendering or Ashok0's High Res Texture Pack
- Blood analyser and computer screens render as black in VR — known REFramework issue. Workaround: play these sections in flatscreen, or use PureDark's AFW Rendering fix
- Scopes and visors do not work
- Film grain is always on with no in-game toggle — RE9VR mod disables it automatically, or use a separate Nexus mod
- Carrying someone requires right stick movement (no HMD movement during that section)

**Recommended setup:** Install REFramework, then RE9VR addon. Consider PureDark's AFW Rendering for the texture and black screen fixes. This is currently the most impressive REFramework VR experience — but also the most demanding on hardware.

## Performance Optimization

RE Engine games are visually rich. Rendering them twice at headset resolution requires serious hardware. Here's how to get the best performance:

### Use pd-upscaler Builds

The pd-upscaler builds of REFramework completely fix TAA and add support for DLSS, FSR2, and XeSS upscaling. This is the single biggest performance improvement available. Get them from the [GitHub Actions page](https://github.com/praydog/REFramework/actions) (requires a GitHub account).

### Try OpenXR

Switching from OpenVR to OpenXR can improve performance, especially in DX12 games. Delete `openvr_api.dll` and use `openxr_loader.dll` with your headset's native runtime.

### Disable Hardware-Accelerated GPU Scheduling

If you're getting extremely low frame rates, disable HAGS in Windows Settings → System → Display → Graphics → Change default graphics settings.

### Use Alternative Eye Rendering (AER)

AER renders one eye per frame instead of both simultaneously, effectively halving the render load at the cost of a slight flicker. Enable it in the REFramework VR menu. The trade-off is worth it if you're struggling to hit framerate.

### Adjust SteamVR Supersampling

Set the game to windowed mode — the game will render at your headset's resolution. Use SteamVR's supersampling slider to lower or raise the effective resolution. Lowering supersampling is a direct performance lever.

### Disable Conflicting Software

- Disable overlay software (Discord overlay, FPS counters, etc.)
- Disable SteamVR Theater Mode
- Remove any DLSS/FSR/XeSS DLLs and PDPerfPlugin.dll if you're getting visual artifacts
- Unplug extra monitors if HDR is causing rainbow issues

## Troubleshooting

### Game appears on a big screen instead of in VR

SteamVR Theater Mode is intercepting the game. Go to SteamVR Settings → Dashboard → turn off "Present Non-VR Applications on Theater Screen Upon Launch."

### Rainbow visual artifacts

You have an HDR monitor and HDR is being forced. Disable HDR in Windows, set the game to windowed mode, or temporarily unplug the monitor.

### Game looks squished with black bars

Turn off Borderless Windowed mode. Use regular Windowed mode instead.

### Motion sickness

Enable Decoupled Camera Pitch in the REFramework VR menu. This stops vertical camera movement. You can also edit `re2_fw_config.txt` (or equivalent) and set `VR_DecoupledPitch=true`. Consider downloading snap turn scripts from [biohazardvr.com](https://www.biohazardvr.com/) for each game.

### Controllers not working

Unplug any gamepad — gamepads conflict with VR controls. If bindings are wrong, set up custom bindings through SteamVR. The community recommends the HoriZon shared bindings profile, which adds floor changes, quick weapons, quick map, and first/third person toggling.

### Black screen on launch

Delete `config.ini` in the game folder to reset all settings to defaults.

### Crashes

Check `re2_framework_log.txt` and `reframework_crash.dmp` in the game folder. Report bugs on the [GitHub Issues page](https://github.com/praydog/REFramework/issues). Try switching between DX11 and DX12. Try the old pre-RT beta builds for RE2/RE3/RE7 (available in Steam under the game's properties → Betas tab).

## The RE4VR and RE9VR Addon Mods

Base REFramework provides 6DOF VR for all supported games, but motion controls are only built-in for RE2, RE3, RE7, and RE8. For RE4 and RE9, you need addon mods created by **Talemann**:

- **RE4VR** ([Nexus Mods](https://www.nexusmods.com/residentevil42023/mods/5682)): Full first-person motion controls for Resident Evil 4 Remake. Includes controller presets for Index and Oculus. Version 1.1.1 adds weapon drag fixes, camera smoothing, and improved hand behavior.

- **RE9VR** ([Nexus Mods](https://www.nexusmods.com/residentevilrequiem/mods/1017)): Full motion controls for Resident Evil Requiem, including manual reloading, three holsters with haptics, snap turn built-in, film grain disabling, and first-person camera. The most feature-complete REFramework VR addon.

These mods are community contributions that build on REFramework's scripting and plugin API. They demonstrate the framework's extensibility — Praydog built the foundation, and other modders add game-specific VR features on top.

## REFramework vs UEVR: What's the Difference?

Both are Praydog projects. Both inject VR into flat games. The approach is completely different:

| | REFramework | UEVR |
|---|---|---|
| **Engine** | RE Engine (Capcom) | Unreal Engine 4/5 |
| **Method** | Native engine hook | Stereo injection via UE's own pipeline |
| **Motion controls** | Built-in for RE2/3/7/8, addon for RE4/RE9 | Optional, game-specific |
| **Game-specific features** | First-person mode, flashlight, IK body, body part toggles | Generic 6DOF + optional motion via plugins |
| **Stability** | More polished — RE Engine is a single, well-understood target | More variable — hundreds of UE games, each different |
| **Supported games** | ~14 RE Engine titles | Hundreds of UE4/UE5 games |

REFramework is the more refined tool because it targets a single engine from a single developer (Capcom) with predictable architecture. UEVR is the more ambitious tool because it targets an entire commercial engine used by thousands of games. Both are essential to the flat-to-VR community.

## Why REFramework Matters

REFramework represents something rare in VR modding: a tool that's been refined to the point where the results compete with official VR conversions. Capcom's own PSVR2 versions of RE4 and RE8 exist — and the PCVR versions through REFramework hold up favorably, offering better graphics (on capable hardware), more customization, and access to games like RE2, RE3, RE7, and RE9 that have no official VR version at all.

The motion control implementation for the Resident Evil series is particularly impressive. Hand-tracked weapon aiming, two-hand grip stabilization, manual reloading (in RE9), and physical holster interactions transform these from "flat game in 3D" to genuine VR experiences. RE7 in VR is arguably the best horror experience on any VR platform — official or modded.

The framework is free, open source, actively maintained, and has a thriving community. The [biohazardvr.com](https://www.biohazardvr.com/) community site provides comprehensive setup guides, troubleshooting, QoL scripts, and auto-installers for every supported game.

If you have a PCVR headset and a gaming PC, REFramework is not optional. It's essential.

## Links

- **REFramework GitHub:** [github.com/praydog/REFramework](https://github.com/praydog/REFramework)
- **Nightly builds:** [github.com/praydog/REFramework-nightly/releases](https://github.com/praydog/REFramework-nightly/releases/)
- **pd-upscaler builds:** [github.com/praydog/REFramework/actions](https://github.com/praydog/REFramework/actions)
- **Official site:** [reframework.praydog.com](https://reframework.praydog.com/)
- **VR Troubleshooting:** [cursey.github.io/reframework-book](https://cursey.github.io/reframework-book/troubleshooting/VR-Troubleshooting.html)
- **Community guide (biohazardvr.com):** [biohazardvr.com](https://www.biohazardvr.com/)
- **RE4VR addon:** [Nexus Mods](https://www.nexusmods.com/residentevil42023/mods/5682)
- **RE9VR addon:** [Nexus Mods](https://www.nexusmods.com/residentevilrequiem/mods/1017)