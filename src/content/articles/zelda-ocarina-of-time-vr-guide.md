---
title: 'Zelda: Ocarina of Time VR Setup Guide (Ship of Harkinian + CitraVR)'
description: 'How to play Ocarina of Time in VR: Ship of Harkinian on PC for full 6DoF and motion controls, or CitraVR on Quest for the 3DS version. Setup steps, fixes, and what to expect.'
pubDate: 2026-11-05
lastUpdated: 2026-11-05
author: Ian
category: guide
heroImage: /images/articles/zelda-ocarina-of-time-vr-guide-hero.jpg
tags: ['zelda', 'ocarina-of-time', 'ship-of-harkinian', 'citravr', 'quest', 'vr-setup', 'emulation']
relatedPages:
  - id: legend-of-zelda-ocarina-of-time
    kind: game
    note: "Our Ocarina of Time VR review and hands-on impressions."
faq:
  - q: "Can you play Ocarina of Time in VR?"
    a: "Yes. Ship of Harkinian VR runs the N64 game on a PC VR headset with 6DoF and motion controls. CitraVR runs Ocarina of Time 3D on a standalone Meta Quest."
  - q: "What is the best way to play Ocarina of Time in VR?"
    a: "Use Ship of Harkinian VR if you have a VR-ready Windows PC and an OpenVR headset. Use CitraVR on Quest only if you do not have a PC VR setup."
  - q: "Is Ship of Harkinian VR available on Quest?"
    a: "The main Shipwright/Ship of Harkinian VR setup covered here is for Windows PC VR. Standalone Quest ports exist as separate community projects, but they are experimental and outside this guide."
  - q: "Do I need a ROM to play Ocarina of Time in VR?"
    a: "Yes. You must supply your own legally dumped copy of the game. Ship of Harkinian uses an N64 Ocarina of Time ROM, and CitraVR uses an Ocarina of Time 3D dump."
  - q: "How do I fix a black screen or crashes in Ship of Harkinian VR?"
    a: "Set the renderer to DirectX 11, not OpenGL. Launch SteamVR before the VR build, confirm your ROM is compatible, and use a recent release from the same VR fork."
---

# Zelda: Ocarina of Time VR Setup Guide (Ship of Harkinian + CitraVR)

Want to play *The Legend of Zelda: Ocarina of Time* in VR? Use **Ship of Harkinian VR** on a PC if you can. It runs the N64 game with 6DoF head tracking and motion controls. If you only have a standalone Quest, **CitraVR** runs *Ocarina of Time 3D* (the 3DS remake) on the headset without a PC.

This guide covers setup for both, the common problems, and what each one actually feels like to play. For impressions and context, read our [Ocarina of Time VR review](/games/legend-of-zelda-ocarina-of-time/). If Hyrule hooks you, our [Majora's Mask](/games/the-legend-of-zelda-majoras-mask/) page covers the sequel.

## Before you start

You must supply your own legally dumped copy of the game. Neither project ships copyrighted assets.

### Ship of Harkinian VR (PC)
- A legally dumped *Ocarina of Time* (N64) ROM. Check compatibility at ship.equipment or compare the ROM's SHA-1 to the project's supported hashes.
- A Windows PC with a discrete GPU.
- A VR headset with SteamVR/OpenVR support (Quest via Link, Air Link, or Virtual Desktop, Valve Index, or another OpenVR headset).
- SteamVR installed and running.

### CitraVR (Meta Quest standalone)
- A Meta Quest 2, Quest Pro, Quest 3, or Quest 3S.
- A legally dumped *Ocarina of Time 3D* ROM (`.cia` or `.3ds`). This is the 2011 3DS remake, not the N64 original.
- No PC required for play.

## Ship of Harkinian VR setup (PC)

Ship of Harkinian is an open-source PC port of *Ocarina of Time* built on the libultraship framework. The VR version is a separate community fork (often called Shipwright-VR) that adds OpenVR support on top of the port.

You get 6DoF head tracking and motion controls. You can swing the sword, raise the shield, and aim with your hands. Menus and some interactions still rely on standard inputs, but combat and looking around feel far closer to VR than emulation hacks ever did.

### Install steps

1. **Verify your ROM.** Check it at ship.equipment or compare the SHA-1 to the supported hashes. If the hash is wrong, the port will reject it. *Success:* the checker reports a supported version.
2. **Download the base Ship of Harkinian** from the project's GitHub Releases (Windows: `soh.exe`). Launch it once and point it at your ROM so it generates the required `.otr` data. *Success:* the desktop port loads and finishes OTR generation.
3. **Install the VR fork** from a single fork's GitHub Releases (for example, ShinyWindow/Shipwright-VR or poregon/Shipwright-VR). Extract it into the same folder as `soh.exe` so it can read the generated data, then launch the VR executable from that release. *Success:* the VR build starts in your headset.
4. **Set the renderer to DirectX 11.** OpenGL does not work for the VR fork. In `shipofharkinian.json`, set `gfxbackend` to the DirectX 11 option. *Success:* the game renders in stereo with head tracking.
5. **Start SteamVR first, then launch the VR build.** *Success:* you reach the title screen in-headset.

### Controls

Sword swings with your dominant hand, shield with the other, and bow aiming uses motion. Start in a safe area like Kokiri Forest and adjust swing sensitivity if the sword triggers too easily.

### Known issues

- **Black screen or no VR output:** usually OpenGL. Switch to DirectX 11.
- **Headset not detected or tracking problems:** start SteamVR before launching, confirm the headset is active, and recalibrate your play space in SteamVR if needed.
- **Sword swings firing constantly:** lower the swing sensitivity in the fork's settings.
- **Fork drift:** releases and compatibility change. Use one fork consistently and check its current release notes/community channels before troubleshooting.

### Save and quit

Save in-game through normal save points. Ship of Harkinian also supports save-state hotkeys (commonly F5 save, F6 cycle slot, F7 load). To quit, exit the VR build or close it through SteamVR; your saves persist on disk.

## CitraVR setup (Quest)

CitraVR is a native OpenXR port of the Citra 3DS emulator for Meta Quest. It runs on the headset and shows 3DS games on a large virtual screen. You play *Ocarina of Time 3D*, the 2011 Grezzo remake, not the N64 original.

CitraVR is the fallback when you don't have a PC VR setup. It is convenient, but it does not give you motion-controlled sword swings. You play with Quest controllers mapped to 3DS inputs.

### Install steps

1. **Install CitraVR on your Quest.** Use SideQuest or the available Quest listing, with Developer Mode enabled if required. *Success:* CitraVR opens to its game list.
2. **Add your *Ocarina of Time 3D* dump** (`.cia` or `.3ds`). *Success:* the game appears as a launchable title.
3. **Launch the game and adjust the virtual screen.** Set size and distance for readability. *Success:* the game runs with stable audio and image.

### Controls and expectations

OoT 3D uses 3DS-style inputs. Map the circle pad, buttons, and touch interactions to your Quest controllers. The touch inventory is less natural than native VR UI, so expect some menu friction.

### Known issues

- **Shader stutter:** brief hitches can happen the first time you enter an area as shaders compile.
- **Soft text or image:** raise CitraVR's resolution/atlas settings before changing other options.
- **Audio dropouts:** quit to the game list and relaunch the title.
- **Busy scenes feel rough:** lower per-game resolution scaling. Keep CitraVR updated (Azahar-core builds improved performance and accuracy).

### Save and quit

Save through *Ocarina of Time 3D*'s normal in-game save points. CitraVR stores that save data on its virtual SD card. To quit, save first, then open the Quest menu and return to Home.

## Performance and stability: what to expect

There are no reliable, universal "best settings" numbers for every headset and PC here. Focus on stability first.

- **Ship of Harkinian VR:** the N64-era geometry is light, but VR renders two views and depends on the DirectX 11/OpenVR path. A discrete GPU helps. If you get stutter or crashes, confirm DirectX 11, close background apps, and keep SteamVR and the VR fork updated.
- **CitraVR:** *Ocarina of Time 3D* is a light 3DS workload for modern Quest hardware. Expect occasional shader compilation hitches on first area entry. If performance drops, lower per-game resolution scaling.

Comfort depends on your tolerance for first-person movement and screen presentation. Take breaks, start with short sessions, and adjust movement/camera habits before long dungeon runs.

## Mods

Keep mods separate by platform. Mixing Ship of Harkinian files with CitraVR files breaks installs.

### Ship of Harkinian mods
Ship of Harkinian loads custom assets as `.otr` archives in the `mods` folder. Common options include HD texture packs, quality-of-life tweaks, randomizer content, custom music, and model swaps (where supported by the port/fork).

### CitraVR mods
CitraVR uses 3DS emulator-style custom textures and cheats for *Ocarina of Time 3D*. It does not use Ship of Harkinian `.otr` mods.

## Troubleshooting checklist

- **Black screen (Ship of Harkinian VR):** DirectX 11 renderer, not OpenGL.
- **No headset/tracking (Ship of Harkinian VR):** SteamVR running first; headset active; recalibrate play space.
- **Over-sensitive sword swings:** lower motion/swing sensitivity.
- **CitraVR stutter in new areas:** normal shader compilation; let it settle.
- **CitraVR blurry text:** raise atlas/resolution settings.
- **ROM not accepted:** re-check the dump and SHA-1/compatibility.

## Which one should you use?

If you have a VR-ready Windows PC, use **Ship of Harkinian VR**. It is the best way to play *Ocarina of Time* in VR because you get the full N64 game with 6DoF and motion controls.

If you only have a Quest, use **CitraVR**. It gets you into *Ocarina of Time 3D* quickly, but treat it as a fallback: fixed-screen emulation with controller mapping, not the same VR experience.

## Next step

Once you’re in Hyrule, read our [Ocarina of Time VR review](/games/legend-of-zelda-ocarina-of-time/) for hands-on impressions, strengths, and where each version still feels rough around the edges.
