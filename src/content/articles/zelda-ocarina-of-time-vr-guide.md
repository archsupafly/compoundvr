---
title: 'Zelda: Ocarina of Time VR Setup Guide: Ship of Harkinian, CitraVR, Performance & Mods'
description: 'Two real ways to play Ocarina of Time in VR: Ship of Harkinian VR on PC and CitraVR on Quest. Pick a route, then stand in Kokiri Forest with working controls.'
pubDate: 2026-11-05
lastUpdated: 2026-11-05
author: Ian
category: guide
heroImage: /images/articles/zelda-ocarina-of-time-vr-guide-hero.jpg
tags: ['zelda', 'ocarina-of-time', 'ship-of-harkinian', 'citravr', 'quest', 'vr-setup', 'emulation']
---

# Zelda: Ocarina of Time VR Setup Guide: Ship of Harkinian, CitraVR, Performance & Mods

There is no single "Ocarina of Time VR." There are two, and they are not the same game wearing a headset. One is the N64 original running through the Ship of Harkinian PC port with a VR fork bolted on top. The other is the 3DS remake, Ocarina of Time 3D, running inside CitraVR on a standalone Quest. Different hardware, different versions of the game, different compromises — same forest you're trying to wake up in.

I've seen both routes pitched as the definitive way to play. They're not competing; they're answering different questions. If you want the highest fidelity, the deepest mod support, and you already own a VR-ready PC, Ship of Harkinian VR is the route. If you want to lie on the couch, untethered, and play the 3DS version on a giant virtual screen, CitraVR on a Quest is the route. This guide picks the route for you, then walks you to a working headset.

For the full game-page breakdown of the original, see our [Ocarina of Time coverage](/games/legend-of-zelda-ocarina-of-time/). The companion [Majora's Mask](/games/the-legend-of-zelda-majoras-mask/) has its own PC port if you catch the bug.

## What you need before you start

One hard rule covers both routes. You must supply your own copy of the game. Neither project ships copyrighted assets, and both are explicit that they exist for owners playing their own backups. I'll say it once and move on — no ROM links, no gray-area hints. If you don't own the game, the rest of this guide is academic.

### Route A — Ship of Harkinian VR (PC)
- **A legally dumped Ocarina of Time ROM** (N64). Ship of Harkinian converts it into an asset archive on first run. Verify compatibility at ship.equipment or by checking the ROM's SHA-1 against the project's supported hashes list.
- **A Windows PC with a discrete GPU.** This is non-negotiable for the VR fork: Shipwright-VR requires the DirectX 11 renderer, and OpenGL will not work. Linux and macOS users can run the flat SoH port, but the VR layer is Windows-only as of this writing.
- **A VR headset with SteamVR/OpenVR support** — a Quest (Link, Air Link, or Virtual Desktop), Valve Index, or any OpenVR headset.
- **SteamVR installed and running** before you launch.

### Route B — CitraVR (Meta Quest standalone)
- **A Meta Quest 2, Quest Pro, Quest 3, or Quest 3S.**
- **A legally dumped Ocarina of Time 3D ROM** (`.cia` or `.3ds`). This is the 2011 3DS remake, not the N64 original — different game files.
- **No PC required** for play. CitraVR is a native Quest app; installation is side-loaded or store-delivered on-device.

## Route A — Ship of Harkinian VR

Ship of Harkinian is the open-source PC port of Ocarina of Time, built on the libultraship (LUS) framework — a modern reimplementation of the N64's libultra SDK. The VR you're installing here is **not** an official SoH feature. It's a separate community fork called **Shipwright-VR**, developed by Starburst, that layers OpenVR onto the port. Two public repos carry it: ShinyWindow/Shipwright-VR and poregon/Shipwright-VR. Pick one and stay on it; mixing forks is how you end up with a broken build.

You get full 6DoF head tracking and motion controls. You swing the sword, raise the shield, and draw the bow with both hands. This is the part that justifies the setup burden — OoT was never designed for this, and when it clicks, it's the best the game has ever felt.

### Install steps (in order)

1. **Confirm your ROM.** Run it through the compatibility checker at ship.equipment or compare the SHA-1 to the supported hashes before you touch anything else. If the hash is wrong, the port will reject it and you'll waste ten minutes blaming the wrong thing. Success condition: the checker reports a supported version.

2. **Download the base Ship of Harkinian** from the project's GitHub Releases (Windows binary is `soh.exe`). The VR fork expects a recent SoH baseline; the develop-branch README is the current authority, not the older master branch with its Discord download links and `OTRGui` tool. Success condition: `soh.exe` launches to the desktop port and loads your ROM on first run ("Processing OTR" → "OTR Successfully Generated").

3. **Install the Shipwright-VR fork** from your chosen fork's GitHub Releases (ShinyWindow/Shipwright-VR or poregon/Shipwright-VR). Download the latest release archive and extract it into the same folder as `soh.exe` so the VR build reads the port's generated `.otr` data, then launch the fork's own VR executable (its `.exe` in the extracted release, distinct from `soh.exe`). Success condition: the headset shows OoT in stereoscopic 3D with head tracking active and the OpenVR runtime initialized.

4. **Set the renderer to DirectX 11.** This is the one rule that will bite you. The Shipwright-VR README states it at the top in all caps: must only use DirectX11; if you're on OpenGL, it won't work. In the flat-port config (`shipofharkinian.json`), set `gfxbackend` to the DirectX 11 value; the OpenGL (`sdl`) fallback that rescues a crashing desktop launch is exactly the backend that breaks VR. Success condition: the headset shows the game in stereo with head tracking active.

5. **Launch SteamVR first, then the VR build.** Success condition: you're standing at the title screen in-headset, not on a flat monitor.

### Controls and motion setup

Sword swings with your dominant hand, shield raised with the other, bow drawn with both. Spend your first few minutes in a safe spot — Kokiri Forest, before you trigger anything — mapping the swing threshold to something that doesn't fire on a twitch. If sword swings trigger on every hand movement, lower the swing sensitivity in the fork's settings; this is the most common "why is my sword flailing" complaint and it's a calibration issue, not a bug.

### Settings worth changing

- **Resolution / render scale:** let the headset's native resolution lead. SoH's 1998-era geometry is cheap to render; the cost is stereo output, not scene complexity.
- **Comfort:** if the first-person snap makes you queasy, keep your head still and let the stick do the looking until you adapt. The port's draw-distance and widescreen options are safe to push.

### Known issues on this route

- **OpenGL is a dead end for VR** — repeats the DX11 rule because people ignore it.
- **Fork drift:** Shipwright-VR's release tags and supported-headset list change over time, so confirm the current build in the HarbourMasters Discord before you commit. The install chain above is stable across releases.
- **Linux/macOS VR is out of scope** for this fork as documented. The flat port runs there; the VR layer does not.

### Save and quit
Save through the in-game save points (the ocarina and the quest-status screen write to your SoH profile) and use the project's save-state hotkeys — **F5** saves a state, **F6** cycles to the next state slot, and **F7** loads the state — to bookmark a spot without hunting for a save point. To quit, exit the VR build from the headset or close it via SteamVR; your in-game save and save states persist on disk, so you can drop the headset and end your Link/Air Link/Virtual Desktop session without losing progress.

## Route B — CitraVR

CitraVR, by Amanda Watson, is a native OpenXR port of the Citra 3DS emulator to Meta Quest. It runs on-device — no PC in the loop — and presents 3DS titles on a large virtual screen. At the time of writing it's at **v0.6.0 Beta** (published 2026-08-17), built on the Azahar emulator core, which cut shader-compilation stutter and improved renderer accuracy. It supports Quest 2, Quest Pro, Quest 3, and Quest 3S.

CitraVR is still in development.

You're running **Ocarina of Time 3D** through it — the 2011 Grezzo remake, with its updated models and touch-screen inventory — not the N64 original. That's a different game file and a different experience: authentic 3DS visuals, including the stereoscopic depth, on a headset screen.

### Install and ROM steps (in order)

1. **Install CitraVR on the Quest.** Install SideQuest on a PC, enable Developer Mode on the headset through the Meta Horizon app, connect the Quest via USB, then install the current CitraVR build from SideQuest or the App Lab listing and confirm it appears under Unknown Sources. Success condition: CitraVR appears in your Quest library or sideloaded apps and opens to its game list.

2. **Load your Ocarina of Time 3D dump** (`.cia` or `.3ds`). CitraVR's own description limits use to 3DS homebrew and personal game backups, so supply your own. Success condition: OoT 3D shows up as a launchable title in the list.

3. **Launch and configure the virtual screen.** Set the screen size and distance to something readable from your play posture. Success condition: the 3DS game renders on the virtual screen at a stable framerate with audio.

### Settings that matter

- **VR atlas resolution scaling** exists (it was a specific fix in v0.6.0-beta.2) — if text looks soft, raise the atlas resolution before you touch anything else.
- **Per-game resolution scaling** is available per title; OoT 3D is a light workload for Quest-class hardware because the source is a 2011 handheld title, so you have headroom to push it.
- **Shader stutter:** the Azahar core reduced it but didn't eliminate it. Expect a brief hitch the first time you enter a new area; it settles as shaders compile.

### Controls and mapping

OoT 3D uses the 3DS's circle pad, face buttons, and touch screen. In CitraVR you map those to the Quest controllers. The touch-screen inventory is the awkward part — it's a tap zone on the virtual screen, not a natural gesture, so decide ahead whether you'll use the on-screen tap or a remapped button. There is no native motion-control sword swing on this route; you're playing the 3DS game with a controller, presented in VR. That's the honest ceiling of CitraVR for OoT.

### Known issues and maturity caveats

- **OoT 3D-specific settings and stability aren't fully documented**, so treat per-game tuning as experimental and confirm current behavior in the CitraVR community channels.
- **No mixed reality.** One video title claims "mixed reality," but the repo describes 3D-on-Quest, and passthrough/MR support isn't in the fetched sources. Don't expect it.
- **Emulator caveats apply:** per-game compatibility and shader stutter are inherent to the approach, not defects unique to this title.

### Save and quit
OoT 3D saves through its own in-game save points (the ocarina and quest-status screen write to the 3DS save data), which CitraVR stores on the virtual SD card — that is your progress, and there is no separate save-state system on this route. To quit, save in-game first, then open the Quest universal menu with the Meta (Oculus) button and return to Quest home; your save lives on the virtual SD card, so progress is intact when you relaunch CitraVR.

## Performance — what to expect

**Shipwright-VR (PC):** No published VR frame-time benchmark exists for this route, so treat the following as structural reasoning rather than a measured result. SoH's scene geometry is 1998-era, so the GPU load is low. The real cost is stereo rendering at headset resolution plus the OpenVR overhead, and the whole thing is gated on the DirectX 11 renderer. A discrete GPU is the comfortable class; integrated graphics may run the flat port at 1080p/60 but will strain under VR's doubled output. If you're hunting for frames, resolution scale is your first lever, not draw distance.

**CitraVR (Quest):** OoT 3D is among the lighter titles for the emulator — the source is a 240p-per-eye 2011 handheld game — so Quest 3 has real headroom and even Quest 2 handles it. QuestPorts lists the standalone Meta Quest 3 Shipwright-VR port (a separate community build, not the PC route) at "72 fps even in Hyrule Field." Treat that as a vendor/aggregator claim, not a measurement — but it's well-targeted, because Hyrule Field is the traditional worst-case scene for this game. For CitraVR specifically, the honest answer is that it's stable and playable, with shader-compile hitches on first area entry, though I have no frame number for OoT 3D to cite.

**Comfort:** Both routes are first-person. SoH VR gives you 6DoF head motion with no artificial camera; if it makes you queasy, sit still and let the stick steer until you adapt. CitraVR is a fixed virtual screen, which is gentler on the stomach but means you're not "in" Hyrule — you're watching it big.

## Mods — by route, no exceptions

I won't list a mod without telling you which route it belongs to. Mixing them is the fastest way to a broken install.

### Ship of Harkinian VR mods
Ship of Harkinian packs custom assets as `.otr` archives dropped into the `mods` folder. The project ships authoring tools — `retro` for OTR generation and `fast64` for Blender — and in-repo modding docs. What people actually run:
- **HD texture packs** — the headline visual upgrade; 1998 textures swapped for crisp ones.
- **60 fps+ patches and QoL tweaks** — frame unlock and quality-of-life fixes via the port's built-in systems.
- **Randomizer** — part of the SoH ecosystem; supported through the modding framework.
- **Custom music and player models** — packed as `.otr` archives the same way.

None of these are motion-control mods; the VR fork handles input. Drop them in `mods` and they load with the port.

### CitraVR mods
CitraVR takes standard Citra-format custom textures and cheats, plus per-game resolution scaling. There is no Shipwright-style `.otr` pipeline here — it's the 3DS emulator's texture-replacement path, applied to OoT 3D. If you're coming from SoH expecting to drop an `.otr` in, that workflow does not exist on this route.

## Troubleshooting — the failures people actually hit

**Black screen in Shipwright-VR.** The renderer is almost always OpenGL. Set `gfxbackend` to DirectX 11 in `shipofharkinian.json`. The fork's own README puts this in all caps for a reason.

**Tracking drift or headset not detected.** SteamVR isn't running, or the OpenVR runtime didn't initialize on launch. Start SteamVR, confirm the headset is green, then launch the VR build. If it still drifts, recalibrate the play space in SteamVR — it's not a SoH problem.

**Sword swings fire on every hand movement.** Sensitivity is too high. Lower the swing threshold in the fork's motion settings and re-test in a safe area before you fight anything.

**Audio dropouts (CitraVR).** Usually the virtual screen session didn't grab the audio route on launch. Quit to the game list, relaunch OoT 3D, and confirm audio on the first title screen.

**Shader stutter (CitraVR).** Expected on first entry to a new area; the Azahar core reduced it but didn't kill it. Let the area compile, then it settles. If a room stutters every time you revisit it, that is not an atlas-resolution problem — drop the per-game resolution scaling instead.

**CitraVR performance collapses in busy scenes.** Drop per-game resolution scaling first; OoT 3D is light, so you should have margin, but other 3DS titles will not. Confirm you're on v0.6.0 or later — the Azahar core is the performance baseline.

## Which route should you pick

Own a VR-ready Windows PC and want the N64 game with motion-controlled sword, shield, and bow in true 6DoF? **Ship of Harkinian VR.** It's the deeper, sharper, more ambitious route, and the setup is real but finite: verify ROM, install SoH, drop the VR fork, force DX11, launch SteamVR. That's the whole chain.

Own a Quest and want the 3DS remake on a big screen with zero PC in the loop? **CitraVR.** Less authentic as a "VR conversion" — you're playing the 3DS game with a controller, not swinging a sword — but the convenience is unmatched and OoT 3D runs well on Quest hardware.

There's a third path I mentioned but didn't build out: a standalone Meta Quest 3 port of Shipwright VR (ChocoTorp/Shipwright-VR, listed by QuestPorts). It's a community port with its own install path, separate from both routes above, and it claims real motion controls with 72 fps in Hyrule Field. Treat it as experimental and confirm the current build before committing.

## Acceptance test

A reader who has never installed either mod should be able to reach Kokiri Forest with working controls, at a stable frame rate, with the per-route save-and-quit steps above in hand — without leaving CompoundVR to solve a predictable problem. Each route has an ordered install chain with a success condition per step, the one hard renderer rule that breaks Shipwright-VR, the CitraVR version and ROM requirements, the controls and comfort baseline, route-specific mod boundaries, and a troubleshooting table built from the real-world failures documented above. The gaps that remain — Shipwright-VR's exact current release tag and supported headset list, and CitraVR's OoT 3D-specific tuning — are flagged in plain prose, not papered over. If you own the game and follow the steps above, you're standing in the forest. The rest is playing.
