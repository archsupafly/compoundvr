---
title: "Max Payne VR"
description: "evilSheep's free PCVR beta mod brings the original Max Payne into roomscale VR with tracked hands, dual wielding, manual reloads, and bullet time."
flatReleaseDate: 2001-07-25
vrReleaseDate: 2026-11-14
lastUpdated: 2026-11-16
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - Action
  - Shooter
  - Noir
technicalTags:
  - Full VR Mod
  - Tracked Hands
  - Roomscale
  - Bullet Time
  - SteamVR
experienceTags:
  - Bullet Time
  - Physical Weapon Handling
  - Dual Wielding
  - Noir Story
tier: A
verdict: "evilSheep's Max Payne 1 VR mod is a hands-on PCVR beta for the 2001 classic — tracked guns, physical reloads, and bullet time deliver the fantasy, with beta rough edges included."
heroImage: /images/games/max-payne-vr-hero.jpg
modDownload:
  url: "https://github.com/evilSheep/max-payne-1-vr/releases"
  label: "Download Max Payne VR Mod"
  note: "Created by evilSheep (beta). Requires a Steam copy of Max Payne v1.05."
history:
  - date: 2026-11-14
    note: "evilSheep releases Max Payne 1 VR as a public PCVR beta with tracked hands and motion controls."
  - date: 2026-11-16
    note: "Corrected mod links and article details to reference Max Payne 1 VR (evilSheep/max-payne-1-vr), not Max Payne 2 VR."
sources: "evilSheep Max Payne 1 VR GitHub repository and README (https://github.com/evilSheep/max-payne-1-vr), release notes, and documented mod features/requirements."
relatedPages:
  - id: max-payne-2
    kind: game
    note: "evilSheep's separate Max Payne 2 VR mod with its own install and release track."
---

Max Payne's bullet-time shootouts were built for a flat screen in 2001. evilSheep's **Max Payne 1 VR** mod — a free PCVR beta — puts that noir slow-motion fantasy in your hands, with tracked weapons, physical reloads, and roomscale movement in the original game.

This page covers the mod for the original *Max Payne* (2001), not [*Max Payne 2: The Fall of Max Payne*](/games/max-payne-2/), which has its own separate VR conversion and release track.

## What it is

Max Payne never had an official VR mode. evilSheep's mod is a full PCVR conversion for the Steam version of the original game: stereoscopic VR with head tracking, motion controls, roomscale movement, and a visible body that follows your head and hands. It is currently a **beta**, so expect rough edges and check the project's releases/issues for the latest fixes.

- **Mod:** [evilSheep/max-payne-1-vr](https://github.com/evilSheep/max-payne-1-vr) ([releases](https://github.com/evilSheep/max-payne-1-vr/releases))
- **Requires:** Your own installed Steam copy of *Max Payne* (version 1.05), Windows 10/11, SteamVR, and a PC-connected headset with two tracked controllers. Development testing used PSVR2 and Quest 3 through Virtual Desktop. This is not a standalone Quest application.
- **Optional:** The "25th Anniversary Remaster" 4K texture pack by andrew22 (included with permission), which needs about 4 GB of free disk space and a bundled 4 GB memory patch.

## Guns, reloads, and bullet time

The mod is built around physical interaction rather than a flat control scheme. You get independent aiming and dual wielding, with pistol holsters on your lower chest and a shoulder holster for long guns. Reloads are manual — magazine, slide, pump, and shell handling depending on the weapon — and painkillers are a physical action: grab a bottle from your upper chest and bring it to your mouth. Grenades and Molotovs sit on your left shoulder and are thrown by hand.

Bullet time and shoot-dodges carry into VR alongside punches, gun melee, enemy disarming, and grabbing/throwing ragdolls. A body you hold up can stop enemy bullets. The mod also includes a physical rifle scope with an eye-lock setting (on by default), optional gore effects that can be turned off, gun spinning, an optional weapon wheel, stick actions for jumping/crouching/bullet time, a wrist HUD and weapon ammo displays, and a virtual screen for menus and cutscenes.

## Setup and caveats

Installation is handled by a one-click installer: install the game through Steam, run it once, then close it; download and extract the release ZIP (and the optional 4K texture parts into the same folder if you want them); run **Install Max Payne VR.cmd** and choose **Install**. Start SteamVR, then launch Max Payne from Steam. Open **Options > VR Settings** in-game to configure the experience.

A few practical notes from the mod's documentation:

- **SteamVR menu stuck in front:** If Steam shows Max Payne in Desktop Game Theatre, disable **Use Desktop Game Theatre while SteamVR is active** for Max Payne in Steam > Library > Properties > General.
- **After verifying game files:** Steam restores its original `maxpayne.exe` without the 4 GB patch. Rerun the installer and press **Install**.
- **4K textures:** Optional. Without the texture ZIPs, the installer keeps the original textures; unpacking the textures can take a few minutes.
- **Beta status:** Compatibility and bugs vary by headset/PC setup. The project's GitHub issues page is the place for versioned reports (include mod version, headset, connection method, level, reproduction steps, and `maxpaynevr.log` copied after the issue occurs).

For the sequel's separate VR conversion by the same author, see [Max Payne 2 VR](/games/max-payne-2/).
