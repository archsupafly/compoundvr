---
title: "Diablo II: Resurrected VR"
description: "A community mod drops Diablo II: Resurrected into first-person VR with motion-controlled sword swings, aimed spells, and belt potions you physically grab — and it's wilder than it sounds."
flatReleaseDate: 2021-09-23
vrReleaseDate: 2026-10-04
lastUpdated: 2026-10-17
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Active
genres:
  - Action RPG
  - Dungeon Crawler
  - Hack and Slash
technicalTags:
  - Full VR Mod
  - Motion Controls
  - First-Person
  - OpenXR
experienceTags:
  - Loot Grind
  - Sanctuary
  - Action RPG
tier: A
verdict: "An exceptional ARPG reborn as a first-person VR loot hunt with real motion controls — but the headline first-person mode is still experimental and the mod is offline-only. Put the headset on if you love Diablo and don't mind living on the bleeding edge."
heroImage: /images/games/diablo-ii-resurrected-vr-hero.jpg
modDownload:
  url: "https://github.com/bearstonem/d2r-pcvr/releases"
  label: "Download Diablo II: Resurrected VR Mod"
  note: "Created by bearstonem (D2R VR Unleashed), built on natpoh/BodyWalkVR's D2R VR base"
history:
  - date: 2026-10-17
    note: "D2R VR Unleashed reaches v0.3.17 with bow skills, mercenary potions, and world fixes; daily release cadence through October 2026."
sources: "Assessment based on the documented capabilities of the D2R VR (natpoh/BodyWalkVR) and D2R VR Unleashed (bearstonem) GitHub repositories and release APIs, the PCVR Mods Installer Hub entry, BodyWalkVR's mod page, and launch-week coverage from diabloz.net, vr.org, diablobytes, Notebookcheck, DSOGaming, Rhykker, MrLlamaSC, PCVR Gamer, and Monkeylashes."
---

## Diablo II Was Never Meant to Be First-Person

I've killed Diablo's minions thousands of times — clicked, tabbed, watched my necromancer raise skeletons from a god's-eye view. I never once expected to stand in the Blood Moor with a sword in my actual hand, swing it at a fallen, and watch the corpse drop in stereo. That's the pitch of the Diablo II: Resurrected VR mod, and it is exactly as unhinged as it sounds. A remaster built for clicking on a monitor is now, somehow, a first-person action-RPG you play with your body.

## What the Diablo II VR Mod Puts in Your Headset

This isn't an official Blizzard mode — there isn't one, and nobody's announced one. It's a community Full VR Mod, and the lineage matters because it tells you who's maintaining what. The base project, D2R VR from BodyWalkVR, is a D2RLoader plugin plus a ReShade depth effect that hijacks the remaster's real 3D geometry (the 2021 remake's actual models are what make stereo VR possible at all) and pipes the picture into a headset viewer. On top of that, a faster-moving fork called D2R VR Unleashed builds directly on the base and is where the first-person work is happening fastest — it has shipped multiple releases in the days this mod has been public.

The mod gives you four ways to look at Sanctuary, cycled with the F-keys. F1 is an overhead view rendered in true stereo — the classic Diablo camera, but with depth. F2 is a free third-person camera you steer with your head. F3 drops the whole game onto your floor as a tabletop diorama you can lean over in room-scale, which works cleanly with passthrough. And F4 is the headline: an experimental first-person view with tracked arms, your weapon in your hands.

Getting in requires an owned copy of the game, the loader, the plugin, a ReShade effect, and an active headset runtime. There's a bundled installer and a PCVR Mods Installer Hub entry that wrap most of it, but you'll still flip VSync off and cap the framerate at 180 (each eye renders in turn) and set a few graphics options before it's happy. It's a PCVR mod: the game runs on Windows and streams to a Quest 3 over Virtual Desktop or Steam Link, but there's no native Quest or console build, and you won't find it on a store page.

## Standing in Sanctuary with a Sword in Your Hand

Here's the part that surprised me. The first-person mode isn't a reskin — the mod reads your controllers through native OpenXR and maps real gestures to combat. You swing your weapon and the blade you're holding picks its target by touch. You throw with your hand and draw a bow with both. You reach your right hand over your shoulder and grip to swap weapon sets. Life and mana sit on your wrists; a skill wheel and settings panel hang in the headset. Belt potions aren't a hotkey — you physically grab one and drink it.

That's the core of why this works as VR and not just as a flat game wearing a headset. Diablo's combat is fundamentally about positioning, cooldowns, and resource management, and the mod turns those abstractions into things your body does. Aiming a spell down your hand, loosing a physical javelin, pulling a healing potion off your belt mid-fight — none of that exists in the clicked version, and all of it is the reason to put the headset on.

The body calibration is real too: you set your height and arm span so your in-game arms line up with your real ones, and per-hand haptics are adjustable. When a swing connects, you feel it.

## Where It Falls Apart

Now the honest catch, because there's always one with a mod this young. The first-person view is self-labeled a preview by its own authors, and they're right to label it. The weapon calibration isn't finished — how a given weapon sits in your hands and where it actually aims can be off for a lot of them. Diablo's entire combat math was built for click-to-attack targeting, not for a blade that hits what it touches, so you'll get melee-range and target-picking quirks the mod is still wrestling with. It plays, it's fun, and it is not a finished way to play the game.

The second catch is harder to wave away: this is offline single-player only. Both mods warn that injecting into the game while online risks a Blizzard account ban, so the co-op and ladder play that define Diablo for a lot of people are off the table entirely here. You're hunting Sanctuary solo. For an ARPG whose social loot-sharing is half the appeal, that's a real scope limit, not a footnote.

And the version churn is genuinely fast. The Unleashed fork has shipped multiple releases in a single week, each adding combat, bow skills, mercenary potions, and world fixes. That's great for momentum and rough for anyone writing the mod down as a fixed thing — grab the latest release, confirm the current version on the Flat2VR Discord, and expect the experience you install next month to be ahead of the one described here.
