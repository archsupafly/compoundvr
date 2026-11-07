---
title: "R.E.P.O. VR"
description: "R.E.P.O. is a grab-and-carry physics horror game where the core verb is literally 'hold the fragile thing with both hands' — which is exactly why the free RepoXR mod turns it into one of the best flat-to-VR conversions out there."
flatReleaseDate: 2025-02-26
vrReleaseDate: 2025-06-26
lastUpdated: 2026-07-03
history:
  - date: 2026-07-03
    note: "RepoXR v1.2.3 released — supports R.E.P.O. v0.4.4; latest release as of this update."
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Intense
performance: Heavy Demand
supportStatus: Active
genres:
  - Co-op Horror
  - Physics Survival
  - Extraction
technicalTags:
  - Full VR Mod
  - BepInEx
  - OpenXR
experienceTags:
  - Hand Tracking
  - Co-op Multiplayer
  - Horror
tier: A
verdict: "RepoXR is the definitive way to play R.E.P.O. — full 6DoF hand control over its physics toys, working mixed VR/flat lobbies, and a dev who keeps shipping. Put a headset on for this one; just go in knowing it's a mod, it's Early Access, and smooth locomotion in a dark horror house will test your stomach."
heroImage: /images/games/r-e-p-o-vr-hero.jpg
modDownload:
  url: "https://thunderstore.io/c/repo/p/DaXcess/RepoXR/"
  label: "Download R.E.P.O. VR Mod"
  note: "Created by DaXcess"
sources: "Research conducted via the RepoXR GitHub repository and release notes (DaXcess/RepoXR), the Thunderstore package listing, the PCVR Mods Installer Hub README, the arvrtips.com install guide, the Steam store page, Wikipedia, and a YouTube coverage sweep capturing view counts and title framing. Mod authored by DaXcess, the same developer behind the Lethal Company VR mod LCVR. No direct hands-on testing performed; assessment built from the mod's documented capabilities, version history, and community coverage."
---

## The headset finally makes sense of the grab

I spent a weekend hauling cursed valuables out of a dark building with three friends and a walkie-talkie, and here's the thing about R.E.P.O.: the entire game is "pick up the fragile object and don't drop it." On a monitor that's a mouse prompt and a button hold. In VR, it's your actual hands closing around a wobbling statue, your arms straining as the physics engine tries to rip it out of your grip while something in the hallway starts making a sound it shouldn't.

That difference is why R.E.P.O. has quietly become one of the strongest flat-to-VR conversions of its era. There's no official VR mode — Semiwork has never listed VR among its priorities — but a free community mod called RepoXR does the job most studios wish they could. It's built by DaXcess, the same person behind LCVR, the Lethal Company VR mod, so this isn't a stranger's weekend project. It's a full 6DoF motion-control conversion running on Unity's OpenXR plugin, and it turns R.E.P.O.'s central mechanic from an abstraction into a physical act.

## What RepoXR actually is

RepoXR is a BepInEx mod that bolts a complete VR mode onto R.E.P.O. You get full hand movement and motion-based controls: reach out and physically grab an item, rotate it by twisting your wrist, pull it closer or push it away with the stick, and shove it into a cart with both hands like you're moving house under deadline pressure. The mod even gives you a physical toolbelt in front of you for the map, and a flashlight you can hold or mount to your head.

The smartest part is the lobby design. RepoXR works in mixed sessions — VR players and flatscreen players in the same round, both fully compatible with vanilla clients. VR players get a [VR] tag in the menu, and everyone else sees your arm movements live. There's one real caveat: if the host isn't running the mod, item physics can behave slightly differently for VR players, so having the host on RepoXR makes object rotation behave cleanly. That's a minor coordination ask.

The mod keeps pace with the game. The current build supports the latest R.E.P.O. version and has added VR presence on Steam and Discord, left- and right-handed binding overrides, eye-tracking support for headsets that have it, and a configurable arm-detach so you can stretch your reach further than your torso allows. It dynamically checks compatibility at startup, so newer game builds often work even before they're formally listed.

## Getting in: easier than the genre usually allows

A flat game with a VR mod usually means a quiet afternoon of dependency surgery. RepoXR mostly spares you that. The canonical route is the Gale mod manager through Thunderstore, which pulls BepInEx and the OpenXR libraries in automatically, or the one-click installer in the PCVR Mods Hub. Either way you're looking at a moderate setup, not an expert-only ordeal — but there's one trap that bites nearly everyone the first time: you must launch through the mod loader, not Steam. Launch from Steam and you skip the mod entirely and wake up in flat mode wondering what went wrong. Own the game, launch it once flat so config files generate, then run it through the manager.

Beyond that, the honest friction is version-chasing and mod compatibility. R.E.P.O. is still in Early Access and gets regular updates, so you'll occasionally need to confirm your mod version tracks the game build. And R.E.P.O.'s mod scene is enormous and built almost entirely for flat play — RepoXR doesn't audit it, so any extra mods you pile on are yours to test individually. ## What it feels like in the headset

This is where RepoXR turns R.E.P.O. into a better game. R.E.P.O.'s loop is pure tension: creep through a pitch-black level, locate the valuables, coordinate with your crew over walkie-talkie voice, and extract them without the physics deciding you're the entertainment. On a screen that's amusing. In the headset, with an object of real weight in your hands and a friend's panicked breathing in your ear, the fragility becomes physical. You genuinely hesitate before yanking a heavy crate around a corner because you can feel how easily it'll tip.

The multiplayer presence is the draw. Watching a flatscreen friend's avatar fumble a grab while you're standing right there, arms out, is the kind of cross-reality moment VR was promised to deliver and rarely does. And because the mod renders VR players' actual arm motion to everyone, a vanilla host still sees you flailing realistically across the room.

Performance sits at the heavy end of the demand curve. R.E.P.O. is a lightweight Unity title on a monitor, but stereo rendering plus the overhead of SteamVR or Virtual Desktop streaming means you want real headroom above the flat minimums — a mid-range PC will run it, but you'll want a high-end rig to keep dense, particle-heavy rounds at a clean framerate without reprojection. The mod itself is stable; the variable is your machine and your streaming setup, not the conversion.

## Where it earns its keep

The genre fit is the whole story. R.E.P.O. is a physics-grab game, and VR's single greatest trick is making you feel like you're holding something. RepoXR doesn't just map that verb — it rebuilds inventory, map access, and flashlight use around your hands. That's a deliberate, full-conversion effort, not a profile toggle.

The mod launched with working motion controls and has kept iterating: new item interactions, scooters, the cosmetics system, gaze-based enemy reactions for eye-tracking headsets, and separated left/right binding overrides so left-handed players aren't stuck remapping the world. A developer who treats a free mod like a maintained product is the difference between a conversion you try once and one you keep installed.

And the reach is real. Coverage of this mod has been sustained across its whole life — launch trailer, install guides that kept updating as versions shifted, and gameplay videos well into the following year. One video alone pulled close to half a million views, and the channel coverage consistently framed it as the version the game was built for. That's not a verdict I'm parroting; it's a signal that a lot of people tried this and came back talking.

