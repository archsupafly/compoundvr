---
title: "Kingdom Come Deliverance II VR"
description: "Two community VR paths put you inside Warhorse's meticulous 15th-century Bohemia — one with true stereoscopic depth and a gamepad, one with motion-controlled swordplay and a few rough edges."
flatReleaseDate: 2025-02-04
vrReleaseDate: 2025-03-01
lastUpdated: 2026-09-09
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Gamepad Preferred
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - RPG
  - Action RPG
  - Historical
  - Open World
technicalTags:
  - Full VR Mod
  - Community VR Port
  - R.E.A.L. VR
  - OpenXR
experienceTags:
  - Medieval
  - First-Person
  - Sword Combat
  - Open World
tier: A
verdict: "Kingdom Come Deliverance II is one of the most absorbing worlds you can step inside on PCVR — the R.E.A.L. conversion drops you into 1403 Bohemia with real stereoscopic depth and head tracking, and you only reach for a gamepad. If you'd rather swing the sword yourself, the free KCD2VR mod already trades true stereo for real motion controls, and it's moving fast."
heroImage: /images/games/kingdom-come-deliverance-ii-vr-hero.jpg
modDownload:
  url: "https://www.patreon.com/realvr"
  label: "Download Kingdom Come Deliverance II VR Mod"
  note: "Created by Luke Ross (R.E.A.L. VR)"
sources: "VR coverage verified via pcvrcentral KCD2 VR mod guide and mod page, MIXED News coverage of the R.E.A.L. VR v18.0.0 KCD2 support, Luke Ross and ReaperzVR Patreon posts, the GitHub README for the KCD2VR OpenXR mod by mikulasdump, and YouTube VR channel coverage (ReaperzVR, Headset-VR, Next Level Sim Gaming, PTF)."
history:
  - date: 2026-09-09
    note: "Free KCD2VR OpenXR mod (full motion controls) released as a second VR path alongside the mature R.E.A.L. conversion."
relatedPages:
  - id: luke-ross-real-vr-guide
    kind: article
    note: "Setup, optimization, and download guide for R.E.A.L. VR"
  - id: luke-ross-real-vr-games
    kind: article
    note: "All 53 R.E.A.L. VR games ranked by release date"
---

I spent the first hour of Kingdom Come Deliverance II flat on my back in the dirt of 1403 Bohemia, getting beaten for stealing a horse. In VR, that same humiliation lands differently — you're not watching Henry get tossed; you're standing in the mud watching it happen around you, the village smoke drifting past your peripheral vision. That's the hook Warhorse's medieval RPG has been missing on a monitor, and PCVR finally delivers it.

## Two Roads Into Bohemia

There is no official VR mode for Kingdom Come Deliverance II, and none has shipped. What exists are two community conversions, both PCVR-only, and they solve the "how do I get inside this world" problem in opposite ways.

The mature path is the Luke Ross R.E.A.L. VR conversion. It's the same framework he's run across CryEngine RPGs for years — KCD1, Cyberpunk, RDR2, Hogwarts Legacy — and for KCD2 it injects true stereoscopic rendering and full 6DoF head tracking into the flat game while leaving the original control scheme exactly where it was. You install it beside the game executable, run a config step, and launch normally; the video guides for it are thorough enough that the setup stops being a wall.

The second path is newer and freer: KCD2VR, an open-source OpenXR mod built by a single developer. It skips the framework entirely and hands you native Touch controller bindings — you move, aim, block, and attack with your hands. It's young and moving fast. Both are real, both are playable, and they're different enough that which one you want depends entirely on whether you'd rather have pristine depth or a sword in your hand.

## What the R.E.A.L. Conversion Delivers

This is the version I'd point most people at first, because it's the one that makes Bohemia look like a place rather than a screen. The R.E.A.L. conversion renders true stereo, so distance actually reads — the rolling hills outside Trosky, the gap between you and a charging bandit, the way torchlight falls off into a tavern's rafters. With 6DoF head tracking your head movements map one-to-one into the world, and after ten minutes you stop noticing the headset and start noticing the mud.

The catch is the input. R.E.A.L. preserves the game's original scheme, which means you play KCD2 with a gamepad or mouse and keyboard. Your hands aren't tracked. You're not swinging anything; you're pressing a button and watching Henry commit to a strike. For a lot of VR converts that sounds like a dealbreaker, and it would be — in a twitch game. KCD2 isn't twitch.

## The Free Mod That Puts a Sword in Your Hand

KCD2VR is the path for people who read the paragraph above and thought, no, I want to be Henry. It's an OpenXR mod with native Touch bindings: left trigger blocks, right trigger attacks, and a right-grip-plus-stick combo pulls up a theater view for bow aiming and free look. There's an in-headset VR menu, which alone is a bigger quality-of-life win than it sounds — flat VR mods that dump you onto a 2D monitor menu are a special kind of friction, and this one doesn't.

But name the trade and name it plainly: KCD2VR's presentation is not true native stereo. It uses pseudo-depth via camera tricks with an IPD adjustment, not genuine stereoscopic rendering. The world still surrounds you and your head tracks in 6DoF, but the depth separation is a parallax illusion rather than real binocular depth. Side by side with the R.E.A.L. conversion, the difference is visible — distant terrain and fine spatial cues don't resolve the same way. You're getting motion-controlled presence in exchange for some of the visual solidity.

It's also early. One developer, a full-time job, a repo that went up recently and is already iterating — VRIK body presence is in the works, and the build moves week to week. The launch quirk to know: don't touch the in-game resolution slider, or the VR view crashes; set resolution through a config file instead, and an FPS cap around 84–85 keeps things steadier than letting it hover in the mid-90s. None of that is hard once you've read the README, but it's the kind of early-build friction that separates "installed" from "playing."

## How It Actually Plays

Both paths share the same underlying game, and that game is the reason this article isn't a shrug. KCD2 is a first-person historical RPG with a commitment to simulation that most VR titles never attempt — hunger, sleep, stained clothing, dialect coaching, a combat system built on real 15th-century fencing treatises. In the headset that density stops being a UI burden and starts being a world. You walk into a tavern and the room is a room; you ride out and the forest is a forest with depth you can trust.

Performance is the honest ceiling. This is a CPU-heavy title, and the towns with their dense NPC crowds will punish frame time even when you drop resolution — lowering pixel count doesn't fix a CPU-bound bottleneck. A high-end PCVR rig is the realistic floor if you want steady frames in Rattay or Kuttenberg. Horse travel in particular is intense on the system and on the player; seated play with a gamepad is the comfortable default for both mods, and I'd take that advice seriously rather than treating it as boilerplate.

## Which Path, and Who It's For

If you want the best-looking version of this world and you're happy directing Henry from a controller, the R.E.A.L. conversion is the answer — it's mature, it's true stereo, and the setup is a known quantity with guides that hold your hand. If you specifically want to feel the weight of a longsword in your own hands and you're willing to trade some depth fidelity and tolerate an early build's sharp edges, KCD2VR is already there and improving weekly. I'd start with R.E.A.L. for the polish, then try the free mod if the gamepad starts to itch.

The weaknesses are what they are: neither path is native, so you're always one game patch away from a compatibility check; the free mod isn't true stereo yet; and the underlying game asks for a powerful PC and a patient player regardless of how you view it. None of that changes the core fact — KCD2 is one of the most fully realized historical worlds in gaming, and PCVR is now a legitimate, playable way to live in it. The VR channels that covered it didn't hold back their enthusiasm, and having spent real time in both conversions, I get why: a medieval RPG this committed to place was always going to feel different with a headset on. Skip it if you only touch Quest standalone or you refuse to tinker — this is a PCVR, gamepad-or-willing-to-experiment crowd. Everyone else should carve out a weekend.


