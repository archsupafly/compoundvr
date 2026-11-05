---
title: 'Zelda: Ocarina of Time VR Setup Guide (Ship of Harkinian + CitraVR)'
description: 'How to play Ocarina of Time in VR: Ship of Harkinian on PC for full 6DoF and motion controls, or CitraVR on Quest. Step-by-step setup, key settings, fixes, and workarounds.'
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
    a: "Yes. Ship of Harkinian VR runs the N64 version on a PC VR headset with 6DoF and motion controls. CitraVR runs Ocarina of Time 3D on a standalone Meta Quest."
  - q: "What is the best way to play Ocarina of Time in VR?"
    a: "Use Ship of Harkinian VR if you have a VR-ready Windows PC and an OpenVR headset. Use CitraVR only if you need a Quest-only fallback."
  - q: "How do I fix pre-rendered backgrounds blocking my view in Ship of Harkinian VR?"
    a: "Install 3D background mods (such as the Djipi 3DS Experience background files), then in Enhancements > Graphics disable 2D pre-rendered backgrounds and fixed camera, and restart the game."
  - q: "Why is my shield not blocking in Ship of Harkinian VR?"
    a: "Turn Physical Combat on, then increase the shield width sliders in the Physical Combat settings. If you play as Child Link, the Hylian Shield may not behave correctly with physical combat; the Fireproof Deku Shield cheat is a practical workaround."
  - q: "What if Ship of Harkinian VR shows a black screen, upside-down world, or missing HUD on Quest?"
    a: "For black screens, use DirectX 11 and start SteamVR first. For Quest connection issues, check your OpenXR runtime and streaming app setup. HUD visibility and upside-down rendering can depend on the VR build and connection method, so test Virtual Desktop/Meta Link/Steam Link and keep the VR fork updated."
---

# Zelda: Ocarina of Time VR Setup Guide (Ship of Harkinian + CitraVR)

Want to play *The Legend of Zelda: Ocarina of Time* in VR? Use **Ship of Harkinian VR** on a Windows PC if you can. It runs the N64 game in a headset with 6DoF tracking and motion controls. If you only have a standalone Quest, **CitraVR** runs *Ocarina of Time 3D* (the 3DS remake) without a PC.

This guide focuses on getting Ship of Harkinian VR working well: install, first-run settings, controls, common Quest/PC VR problems, and the workarounds players actually hit in temples and boss fights. For impressions and context, read our [Ocarina of Time VR review](/games/legend-of-zelda-ocarina-of-time/).

## Before you start

You must supply your own legally dumped copy of the game. Neither project ships copyrighted assets.

### Ship of Harkinian VR (PC)
- A legally dumped *Ocarina of Time* (N64) ROM. Check compatibility at [ship.equipment](https://ship.equipment) or compare the ROM SHA-1 to the supported hashes for your build.
- A Windows PC with a discrete GPU.
- A VR headset with SteamVR/OpenVR support (Quest via Link, Air Link, Virtual Desktop, or Steam Link; Valve Index; or another OpenVR headset).
- SteamVR installed. For Quest PC VR streaming, make sure your chosen OpenXR/runtime setup matches the streaming app you use.

### CitraVR (Meta Quest standalone)
- A Meta Quest 2, Quest Pro, Quest 3, or Quest 3S.
- A legally dumped *Ocarina of Time 3D* dump (`.cia` or `.3ds`). This is the 3DS remake, not the N64 original.

## Ship of Harkinian VR setup (PC)

Ship of Harkinian is an open-source PC port of *Ocarina of Time*. The VR build most players use is a community fork (often called Shipwright-VR) that adds OpenVR/VR features on top of the port. Features, menu names, and bugs can vary by fork and release, so use one fork consistently.

### Install

1. **Use a simple install path.** A short path like `C:\Games\OoT VR` can avoid startup/path issues.
2. **Verify your ROM first.** Confirm the dump is compatible before troubleshooting anything else. NTSC 1.0/1.2 dumps are commonly used by players; use the version your fork supports.
3. **Install the base Ship of Harkinian.** Launch the desktop build once, point it at your ROM, and let it generate the required `.otr` data.
4. **Install the VR fork/build.** Extract the VR release into the same folder so it can read the generated data, then launch the VR executable from that release.
5. **Enable VR in the game settings.** Press `Esc` to open the Ship of Harkinian menu, go to **VR Settings > General**, and turn VR on.
6. **Use DirectX 11.** The VR fork needs DirectX 11. OpenGL will not work for VR. If you see a black screen or no headset output, check `shipofharkinian.json` and set the graphics backend to DirectX 11.
7. **Start SteamVR before the VR build.** Launch SteamVR (or your PC VR streaming path), confirm the headset is active, then start the VR executable.

### Opening the settings menu in VR

The Ship of Harkinian menu is opened with `Esc` on your keyboard. If you are wearing a headset, lift the headset enough to see your monitor, click the game window, then press `Esc`. This is where you change VR controls, HUD, graphics, enhancements, cheats, and developer tools.

## First-time settings that make the game playable

### Fix pre-rendered backgrounds (Castle Town and similar areas)

Without 3D background mods, pre-rendered backgrounds can block your view in VR. The common fix is to use 3D background files (for example, the Djipi 3DS Experience background `.otr` files) and disable the old 2D backgrounds:

1. Put the required background mod files in your `mods` folder.
2. Open **Enhancements > Graphics**.
3. Disable **2D pre-rendered backgrounds** and **fixed camera** (menu wording can vary by build).
4. Restart the game.

If you want the original OoT look with HD textures, you can combine the Reloaded HD texture pack with only the 3D background files from the 3DS background mod. Do not mix full texture/background packs that overlap, or textures can look wrong.

### HD textures

Drop the texture pack file into the `mods` folder, enable alternate/custom assets in **Enhancements > Graphics/Mods**, and restart if needed. Some builds let you toggle custom textures during play.

### HUD, comfort, and controls

Useful first-pass settings (names may differ slightly by fork):

- **HUD:** set the HUD to floating or attached to a hand in **VR Settings > HUD & Menus**. If you cannot see the HUD, try a different attachment mode and test your streaming method (Virtual Desktop/Meta Link/Steam Link).
- **Turning:** smooth turning is faster; snap turning can feel steadier for some players.
- **Lock-on:** enable lock-on if your build supports it. It helps with strafing and combat.
- **Body:** hiding Link’s body can reduce visual clutter in first-person VR.
- **Ocarina mapping:** map C-buttons to inputs you can hit reliably. Many players prefer mapping C-buttons to left-stick directions.

## VR controls and features (Ship of Harkinian VR)

Recent VR forks have added features that change how the game plays. Availability depends on the build you install.

- **Physical combat:** when enabled, sword swings and shield blocking use hand motion/geometry instead of only button timing. You can toggle it in **VR Settings > Physical Combat**.
- **Shield tuning:** if enemies hit through your shield, increase the shield width sliders (top/bottom) in Physical Combat settings.
- **Item/weapon selection:** some builds include an item selector wheel (often compared to *Half-Life: Alyx*). Hold the selector input, flick to an item, and release. In some configurations the trigger uses the currently held item.
- **Held objects above your head:** bombs, rocks, Cuccos, chest items, and similar objects can sit in your face. Raise your hands higher to lift them out of view.
- **Third-person VR:** if first-person is uncomfortable or a puzzle is easier in third-person, some builds let you toggle third-person in **VR Settings > General**.

## CitraVR setup (Quest fallback)

CitraVR is a native Quest emulator for 3DS games. It runs *Ocarina of Time 3D* on a virtual screen with controller mapping. It is quick to set up, but it is not the same as Ship of Harkinian VR’s motion-controlled N64 experience.

1. Install CitraVR on your Quest (SideQuest/App Lab flow may vary).
2. Add your legally dumped *Ocarina of Time 3D* file (`.cia` or `.3ds`).
3. Launch the game and adjust the virtual screen size/distance.
4. Map 3DS controls to Quest controllers. The touch inventory is usable but less natural than native VR UI.

CitraVR caveats: expect shader compilation hitches on first area entry, lower resolution scaling if performance dips, and treat it as a fallback for players without PC VR.

## Mods

Keep mods separate by platform.

- **Ship of Harkinian:** uses `.otr`/custom asset files in the `mods` folder. Common picks are 3D background fixes, HD textures, quality-of-life tweaks, randomizer support, and cosmetic packs supported by your build.
- **CitraVR:** uses 3DS emulator texture/cheat workflows for *Ocarina of Time 3D*. It does not use Ship of Harkinian `.otr` mods.

## Troubleshooting and workarounds

Some issues depend on the VR fork, headset, and streaming method. If a workaround requires toggling settings, save first.

### PC VR / Quest streaming
- **Black screen or VR won’t start:** confirm DirectX 11 (not OpenGL), start SteamVR before the VR build, and test with a known-good ROM.
- **Quest can’t connect or VR won’t enable:** verify your OpenXR runtime and streaming app settings. For Virtual Desktop users, make sure SteamVR is the active OpenXR runtime in the relevant apps and disable conflicting Meta compatibility layers.
- **Upside-down world (reported by Quest users):** try a different streaming path. Some users have had better results with Steam Link than with Meta’s PC link setup.
- **HUD missing:** try changing HUD attachment (floating/hand). If it still does not appear, test another streaming method and check for a newer VR fork release.
- **Audio dropouts (CitraVR):** relaunch the game from the CitraVR game list.

### Combat and movement
- **Shield not blocking:** enable Physical Combat and increase shield width sliders. During magic-reflect fights, move the shield out of the sword’s path when needed.
- **Child Link Hylian Shield issues:** with physical combat, the Hylian Shield may not behave as expected. A common workaround is to use the Deku Shield and enable the *Fireproof Deku Shield* cheat.
- **Sword swings trigger too easily:** lower swing sensitivity.
- **Can’t climb walls/ledges:** approach from a slightly different angle and try again. This is a known rough edge in VR forks; use cheats only as a last resort.
- **Stuck in crawl tunnels (Child Link):** back out and re-enter instead of restarting.
- **Boomerang aiming feels off:** use lock-on/strafe positioning, or check your build’s current boomerang controls. Hand-aiming behavior may differ by version.

### Temple and boss workarounds
- **No spin attack with Physical Combat:** some builds don’t map a motion spin attack. Temporarily turn Physical Combat off, perform the spin attack with the mapped button, then turn Physical Combat back on.
- **Gate switches (Water Temple / Ganon’s Castle):** use the same spin-attack workaround.
- **Forest Temple Poe block puzzle:** in first-person VR the blocks can be hard to see. Temporarily switch to third-person VR or disable VR to solve the puzzle, then switch back.
- **Phantom Ganon / Ganondorf magic tennis:** if reflected magic dissipates, your shield may be intercepting it. Move the shield aside and hit the projectile with the sword.
- **Water Temple Dark Link:** some players report Dark Link taking control of movement. If you cannot progress, try third-person VR or temporarily disabling VR first. As a last resort, use the save editor/dev tools in your build to grant the required items/keys and continue; treat save editing as a fallback, not the default path.
- **Water Temple hookshot ledges:** hook from farther back and try slight directional input as you travel to the ledge.
- **Spirit Temple Twinrova (first phase):** if physical shield blocking doesn’t reflect the elemental attack correctly, temporarily turn Physical Combat off and use lock-on. The second phase may work better with Physical Combat back on.
- **Ganon’s Castle fire room pillar:** if the thrown pillar glitches in place, temporarily disable VR, complete the throw in flatscreen, then re-enable VR.
- **Ganondorf’s 4-point magic charge:** a direct Light Arrow hit can stop it; you can also evade and respond to the follow-up attack.
- **Freezing after opening chests/getting keys:** if you enabled *Assignable Shields, Tunics and Boots*, try turning that option off. It has been reported to cause freezes in some areas.

## Which one should you use?

If you have a VR-ready Windows PC, use **Ship of Harkinian VR**. It’s the best way to play *Ocarina of Time* in VR: the N64 game, in-headset, with 6DoF and motion controls.

If you only have a Quest, use **CitraVR**. It gets you playing *Ocarina of Time 3D* quickly, but it’s a fallback, not a replacement for Ship of Harkinian VR.

## Next step

After setup, read our [Ocarina of Time VR review](/games/legend-of-zelda-ocarina-of-time/) for hands-on impressions. If you get stuck on a specific fork/build issue, check that fork’s release notes and community channels for the latest fix.
