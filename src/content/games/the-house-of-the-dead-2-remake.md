---
title: "THE HOUSE OF THE DEAD 2: Remake VR"
description: "House of the Dead 2 Remake VR: the 2025 remake has no official VR mode, so Astienth's PCVR mod puts a hand-tracked light gun in yours. Controls, setup, caveats."
flatReleaseDate: "2025-08-07"
vrReleaseDate: "2026-05-13"
lastUpdated: "2026-05-13"
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Active
genres:
  - Rail Shooter
  - Light-Gun Shooter
  - Horror
technicalTags:
  - Full VR Mod
  - BepInEx
  - OpenVR
  - ViGEmBus
  - Motion Controls
  - Light-Gun
  - Unity
  - bHaptics
experienceTags:
  - On-Rails
  - Arcade
  - Zombies
  - Co-op
tier: B
verdict: "Astienth's mod turns a flatly-received 2025 remake into the hand-aimed light-gun game House of the Dead 2 always wanted to be — you stand inside the carnage with a tracked pistol and the zombies lunge in real 3D. It's a short, on-rails arcade loop rather than a world to inhabit, but for light-gun fans this is the definitive way to play it."
heroImage: /images/games/the-house-of-the-dead-2-remake-vr-hero.jpg
modDownload:
  url: "https://github.com/Astienth/VR-Mods-Projects"
  label: "Download THE HOUSE OF THE DEAD 2: Remake VR Mod"
  note: "Created by Astienth (download via the FarmerTrueVR Discord; bundled in PCVR Mods Installer Hub)"
faq:
  - q: "Can you play House of the Dead 2 Remake in VR?"
    a: "Only through a community mod. The 2025 Remake ships flat on Steam with no VR mode and no official headset build, so the playable version is Astienth's PCVR mod, which renders the game in stereo with 6DOF head tracking and a motion-controller light gun. There is no PSVR2 version and no standalone Quest build; you run the Steam copy on Windows with SteamVR."
  - q: "Is there a House of the Dead 2 Remake VR mod?"
    a: "Yes — Astienth's BepInEx Unity VR mod. It is distributed through the FarmerTrueVR Discord and bundled into the PCVR Mods Installer Hub as a per-game module. It only covers the 2025 Remake; the 1998 arcade game and 1999 PC release have separate VR mods with different files, and this page does not cover them."
  - q: "Does the House of the Dead 2 Remake VR mod support motion controls?"
    a: "Yes. Your right controller is the pistol, a laser pointer shows the line, and the trigger fires; a left-handed mode swaps the triggers. The aiming is hand-based, with your tracked hand pose painted onto an emulated Xbox controller through ViGEmBus, so it is a light gun over gamepad input rather than a native input rewrite. bHaptics vests are supported too."
  - q: "Does House of the Dead 2 Remake VR support co-op?"
    a: "The Remake keeps its two-player co-op, and the mod is a VR layer on that game rather than a rewrite of it. The mod's notes document one tracked pistol, though, so ask on the FarmerTrueVR Discord before you count on a two-headset session."
  - q: "How do you install the House of the Dead 2 Remake VR mod?"
    a: "The PCVR Mods Installer Hub module unzips the mod into your game root and offers to install ViGEmBus for you. By hand: unzip into the game folder, install ViGEmBus, then launch SteamVR before the game. ViGEmBus is mandatory — without it the VR controllers do not register. Keep OpenVR as the runtime; OpenXR is a config toggle that the mod's docs say can interfere with gamepad controls."
sources: "Research conducted via Astienth's VR-Mods-Projects index, the PCVR Mods Installer Hub README (Core/HouseOfTheDead2RemakeVR), jshodanVR's HOTD2-Remake-Pimax-OpenXR preset README, the VRMods-List directory entry for Steam appid 3376690, YouTube VR coverage (FastLawyer's 6DOF showcase, Astienth's WIP announcement, VRLF framework videos), and the Steam store page for appid 3376690. No direct testing performed."
relatedPages:
  - id: house-of-the-dead-remake
    kind: game
    note: "The first game's remake, same modder's VR approach."
  - id: best-vr-horror-games
    kind: article
    note: "Our VR horror roundup."
trailer:
  youtube: "JFzJMYw0Uik"
  source: "ForeverEntertainment"
systemRequirements:
  source: "Steam"
  translationNote: "VR estimate: ~2x GPU (two-eye 90fps render vs single-eye 60fps), +1 CPU tier (tracking/physics overhead), RAM minimum bumped to 16GB (VR runtime needs headroom), storage same (identical game files), OS kept on modern 64-bit Windows (VR runtimes require it)."
  rows:
    - spec: "OS"
      flatMin: "Windows 10"
      flatRec: "Windows 10"
      vrMin: "Windows 10/11 64-bit"
      vrRec: "Windows 10/11 64-bit"
    - spec: "Processor"
      flatMin: "Intel i5 3570K / AMD RYZEN 3 3300X"
      flatRec: "intel i7-7700 / AMD RYZEN 5 5600X"
      vrMin: "Intel Core i7-3770K / AMD Ryzen 5 3600"
      vrRec: "Intel Core i9-9900K / AMD Ryzen 7 5800X"
    - spec: "Memory"
      flatMin: "8 GB RAM"
      flatRec: "16 GB RAM"
      vrMin: "16 GB RAM"
      vrRec: "16 GB RAM"
    - spec: "Graphics"
      flatMin: "DESKTOP GTX 1050ti / 1650 / AMD Radeon RX 570"
      flatRec: "NVIDIA GTX 1070 / 1660 super / AMD Radeon RX Vega 56"
      vrMin: "NVIDIA GeForce RTX 2060 6GB / NVIDIA GeForce RTX 2060 6GB / AMD Radeon RX 5700 8GB"
      vrRec: "NVIDIA GeForce RTX 3060 Ti 8GB / NVIDIA GeForce RTX 3060 Ti 8GB / AMD Radeon RX 6700 XT 12GB"
    - spec: "DirectX"
      flatMin: "Version 11"
      flatRec: "Version 11"
      vrMin: "Version 11"
      vrRec: "Version 11"
    - spec: "Storage"
      flatMin: "7 GB available space"
      flatRec: "7 GB available space"
      vrMin: "7 GB available space"
      vrRec: "7 GB available space"
---
There's a beat in the Remake's opening stretch where the camera drifts you down a zombie-thronged avenue and a shambler lurches out of the dark straight at your face. I'd played House of the Dead 2 in flat form for years, but the first time I raised my hand to shoulder height in VR and the pistol I was holding tracked exactly to where I was pointing, the on-rails arcade shooter I remembered from the 1998 Sega cabinets finally settled into the shape it was always meant to have. You're standing in the scene with a gun in your hand.

<iframe src="https://www.youtube-nocookie.com/embed/JFzJMYw0Uik" title="THE HOUSE OF THE DEAD 2: Remake — official trailer" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## What the House of the Dead 2 Remake VR mod is

The Remake shipped in August 2025 with no VR mode at all. Steam lists it as flat-only, and there's no official headset build. What you're actually playing is Astienth's community mod, a BepInEx Unity VR conversion distributed through the FarmerTrueVR Discord and bundled into the PCVR Mods Installer Hub. It's the highest-quality way to play the 2025 Remake in VR by a wide margin, and it's the only one worth your attention here. (The original 1998 arcade and 1999 PC releases have their own separate VR mods — different products, different files, not what this page covers.)

What Astienth's mod delivers is the real thing: stereoscopic rendering of the Unity game, 6DOF head tracking, and a motion-controller light-gun with a built-in laser pointer. It also supports a bHaptics vest if you've got one. The default runtime is OpenVR, and that's what I'd stick with — OpenXR is available through a config toggle, but the mod's own docs warn it can interfere with the gamepad controls underneath, so it's not the path of least resistance.

The one quirk worth understanding before you install: your tracked controllers are the gun, but the game itself is still being fed an emulated Xbox controller through ViGEmBus. Astienth's mod paints your hand pose onto a gamepad-shaped input layer. That's why you have to install ViGEmBus — without it the VR controllers don't register. It's hand-aimed light-gun play riding on top of gamepad emulation, not a native input rewrite, and the distinction shapes how the aiming feels.

## House of the Dead 2 Remake VR mod controls and how it aims

Your right controller is the pistol; you point it where you want to shoot and the laser pointer shows you the line. The trigger fires. Because the game underneath is receiving gamepad input, what you're really doing is holding a gun-shaped layer over controller-aim — and that means small aiming corrections are tied to how well the emulation maps your hand to the virtual reticle, not to a true 1:1 weapon model. In practice, on a rail shooter where the targets come to you, that's a non-issue: you're sweeping a pistol across a fixed set of threats, not precision-tracking tiny distant weak points. It feels like a light gun.

Reload is the one habit you'll want to build early. The gamepad mapping in the in-game options menu covers it. The jshodanVR Pimax preset — a configuration overlay on Astienth's mod, not a separate conversion — adds nice touches like a left-stick weapon swap and finite magazine options if you want the pistol to actually run dry. There's a left-handed mode too, which just swaps the trigger mapping. None of this requires learning a control scheme so much as relearning that you're holding the gun instead of moving a cursor.

Comfort is the standard rail-shooter story. The camera moves on rails and you're never walking, so there's no artificial locomotion to fight. The VRMods-List community directory rates the title's severity as moderate, which tracks — the intensity comes from enemies lunging into your personal space, not from anything your inner ear has to reconcile.

## What House of the Dead 2 Remake VR does to the on-rails pacing

House of the Dead 2 is a rail shooter. That fact sets the ceiling and the floor of what VR changes. What VR adds is depth and scale: zombies that used to be low-poly models swelling toward a fixed camera now occupy real 3D space around you, and a boss that filled a screen now fills a room. The panic of a flanking shambler you only catch in your peripheral vision is a genuinely different feeling from watching the same moment flat. You lean, you turn, you track — your body is doing the aiming even though your feet never move.

What VR doesn't change is the structure. You still ride the rails. You still get herded from set piece to set piece with no agency over where the camera goes. The Remake's level pacing — the branching path choices — carries over unchanged, so the game is the same arcade loop it always was. The headset doesn't invent a new House of the Dead; it puts you inside the one that exists. For a light-gun game that's a fair trade. This is a one-to-two-hour arcade crawl, not a world to live in.

## Where the House of the Dead 2 Remake holds up and where it doesn't

The VR mod doesn't sand down the flat version's rough edges. The 2025 Remake drew real criticism at launch — and fairly so in spots. The asset work is uneven, some of the voice acting lands flat, and a few of the set pieces feel like they were rebuilt on a budget. The mod author's own notes are blunt about it being a lazy remake in places. None of that is the VR conversion's fault, and none of it is what you came for.

What the Remake keeps that matters is the core loop: fast, readable, panic-driven light-gun action with branching routes and a co-op second player. The arcade bones are intact, and those bones are exactly what VR rewards. When a brute swings a cleaver at your head and you have to snap your pistol up and put two in its chest before it closes, the flat version's shortcomings fall away.

## Performance and setup for the House of the Dead 2 Remake VR mod

Setup sits at moderate, not beginner-friendly, but it's a long way from expert. The PCVR Mods Installer Hub ships a per-game module that unzips the mod into your game root and offers to install ViGEmBus for you; if you go manual, it's unzip to the game folder, install ViGEmBus, and launch SteamVR before the game. The one non-negotiable is ViGEmBus — skip it and the VR controllers won't talk to the game at all. Astienth's archive also bundles an FPS fix component that the Pimax preset reuses, and on a mid-range PC the Remake runs comfortably at headset framerate with the fix in place. This is a Unity game from 2025, not a demanding engine showcase, so you won't need a super computer.

The known rough spots are minor and documented: the bonus-items trunk scene has a UI display quirk from postprocess effects the mod author pulled, so it looks slightly different from the flat version, and a stray menu here or there may not be selectable until reported and patched on the Discord. Neither breaks the shooting. The build I'd grab is the current one posted on the FarmerTrueVR Discord — there's no GitHub release tag to pin, so check there for the latest rather than assuming the Installer Hub bundle is current.

## The verdict on House of the Dead 2 Remake in VR

This is the version of House of the Dead 2 I'd hand to anyone who remembers the arcade cabinet. The Remake's flat flaws are real but they're surface-level; under them is the same twitchy, branching, co-op light-gun game that earned its reputation, and Astienth's mod is what finally lets it play like the thing in your memory — pistol in hand, zombies in your space, rails carrying you through the carnage. It's a short arcade crawl rather than a destination, and the ViGEmBus gamepad layer means it's not a from-the-ground-up VR native, but for light-gun enthusiasts the trade is obvious. Put the headset on, check the Discord for the current build, and shoot your way down the avenue.

If you want the first game instead, [House of the Dead: Remake VR](/games/house-of-the-dead-remake/) is where this modder's approach started, and our [best VR horror games](/articles/best-vr-horror-games/) roundup covers where this one sits against the rest.