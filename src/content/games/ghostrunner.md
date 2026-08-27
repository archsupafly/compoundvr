---
title: "Ghostrunner VR"
description: "Wall-running through a cyberpunk tower at 60mph with a sword in your hand — if your stomach can handle it."
flatReleaseDate: 2020-10-27
vrReleaseDate: 2024-01-01
lastVerified: 2024-01-01
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR']
recommendation: Enthusiasts/Tinkerers Only
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Mixed Input
comfort: Intense
performance: Heavy Demand
supportStatus: Active
genres:
  - Action
  - Platformer
  - Cyberpunk
technicalTags:
  - UE4
  - UEVR
  - Community Profile
  - Wall-Running
experienceTags:
  - Fast-Paced
  - Motion Sickness Risk
  - High Adrenaline
  - One-Hit Death
tier: C
verdict: "Ghostrunner's parkour flow state is electrifying in VR, but the speed that makes it great in flat makes it punishing in a headset. Only for Ghostrunner fans with iron stomachs — everyone else should play the flat version."
heroImage: /images/games/ghostrunner-vr-hero.jpg
sources: "Research conducted via Steam store page (https://store.steampowered.com/app/1139900/Ghostrunner/), Wikipedia (https://en.wikipedia.org/wiki/Ghostrunner), UEVR GitHub repository (https://github.com/praydog/UEVR), CYB3R-JUNKI3 Ghostrunner-VR GitHub profile (https://github.com/CYB3R-JUNKI3/Ghostrunner-VR), PCVR Central CJ117 profile page (https://pcvrcentral.com/mods/ghostrunner-uevr-cj117), VorpX forum threads, Flat2VR YouTube channel (https://www.youtube.com/watch?v=TN3ngZmlNSw), Luke Ross Patreon and press coverage (Road to VR, PC Gamer, FRVR), and BlueSkyDefender Depth3D GitHub (https://github.com/BlueSkyDefender/Depth3D)."
---

Here's the thing about Ghostrunner in VR: the first time you wall-run across a chasm, kill a guy mid-air, land on a narrow beam, and slow time to deflect a bullet back at someone — all in about three seconds — you'll understand why anyone bothered with this mod. The second time you do it, you'll understand why most people don't.

Ghostrunner is a first-person cyberpunk parkour slasher where both you and every enemy die in one hit. Wall-run, dash, slide, grapple, deflect bullets with Sensory Boost slow-mo. The flat version is already a rhythm game disguised as an action game — memorize the path, execute the sequence, restart in two seconds when you mistime the jump. It's sublime. It's also the worst possible candidate for motion sickness.

No official VR mode exists. No PSVR2 version. No Quest port. 505 Games never shipped one, and Flat2VR Studios — the team licensing official VR ports of flatscreen games — hasn't announced one. What you get instead is a constellation of community options, all built on the same Unreal Engine 4 bones. The best one, UEVR, is free. The worst one might still be worth trying if you've already bought VorpX. And there's a whole legal drama involving Luke Ross, DMCA takedowns, and publisher 505 Games that's worth knowing about even if you never touch the mod.

## The UEVR route is the one you want

Praydog's UEVR framework is a free, open-source tool that injects VR support into any Unreal Engine 4 or 5 game. Ghostrunner runs on UE4. The math works out. UEVR's public beta dropped in early January 2024, and Ghostrunner was confirmed working within weeks — a Steam discussion thread from January 17, 2024, already had players talking about how well it ran.

The baseline experience uses CJ117's community profile (released April 2024): head-aiming, scale fixes for the sword and hands, adjusted camera positioning. You aim by looking. It works. The sword is visible, the movement is there, you can play the game. But it's not the ideal way to play Ghostrunner — head-aiming in a game where you need to spin 180 degrees and deflect a bullet while wall-running is fighting the design.

The real leap came in March 2025, when CYB3R-JUNKI3 published the "Ghostrunner-VR" profile with a full 6DOF motion controller fix. This is the version that makes the game sing. The sword attaches to your right controller. Melee triggers when you swing in any direction and stop pointing at the target. Sprint maps to the right stick. Movement orientation locks to the left controller. The player character is hidden so you don't see a floating torso, but your arms appear during cutscenes and montages. Head and controller movement work freely in menus, cutscenes, and dialogue.

Setup takes about twenty minutes once you know what you're doing: install UEVR, launch the game, inject via the frontend, import the profile, tweak the in-game settings through the Insert key or L3+R3. Performance tuning is necessary — dual-eye rendering at 90fps demands a mid-range to high-end PC. But it works. The motion controls work. And when everything clicks, this is one of the most intense VR experiences available.

The catch is stability. CYB3R-JUNKI3's own README notes that some cameras are still attached to the right controller during certain sequences. It's a WIP. Most of the time you won't notice.偶尔 you'll hit a cutscene where the camera latches onto your hand and everything goes sideways.

## VorpX: the distant second

If you already own VorpX, Ghostrunner works in Geometry 3D mode. Community reports from the game's launch week confirm it — "works really well everywhere but cyberspace," one user noted, recommending immersive screen mode with edgepeek always on for motion sickness minimizing.

That last part is telling. Even the least immersive VR option for this game needs a comfort crutch. VorpX gives you stereoscopic 3D and head tracking. No motion controls, no hand presence, no VR UI. It's a TV strapped to your face with depth. For a game built on precision platforming and timing, that's a real limitation. You're watching yourself play rather than playing.

There are also documented menu and game freeze issues. It's functional, but "functional" isn't the same as "recommended" when UEVR is free and provides genuine 6DOF.

## The Luke Ross saga

Luke Ross's R.E.A.L. VR framework included a Ghostrunner conversion — AER (Alternating Eye Rendering) with Geometric 3D, FullVR mode enabled. It was paywalled behind his $10/month Patreon. For a while, it was one of the few ways to play Ghostrunner in VR at all.

Then 505 Games DMCA'd it. In January 2026, the publisher issued a takedown specifically for the Ghostrunner conversion — the second strike after CD Projekt's Cyberpunk 2077 DMCA earlier that month. Ross pulled all his mods, then re-released the suite free in March 2026, excluding Cyberpunk 2077 and any titles "possibly in violation of DMCA claims." Whether the Ghostrunner config is currently distributed is ambiguous.

It's a strange situation. A publisher actively preventing people from playing its own game in VR, at a time when no official VR version exists. The R.E.A.L. mod used AER, which is less demanding than UEVR's dual-eye rendering but also less convincing. Even before the DMCA, UEVR was the better option. The legal drama is more interesting than the mod itself.

## The elephant in the room

Let me be honest: I got motion sick.

Ghostrunner is a game built on speed. Wall-running, dashing, sliding, grapple swings — the camera moves constantly and rapidly. In flat mode, your brain handles it. In VR, with the headset tracking every micro-movement, it's a vestibular assault. The Sensory Boost slow-mo helps. CYB3R-JUNKI3's MR vignette option helps. Short sessions help. But there's no teleport option — the entire movement system is designed around momentum, and momentum is the enemy of VR comfort.

This isn't a game you can play for two hours straight in a headset. It's a fifteen-minute burst, a break, another fifteen minutes. The flow state is real and incredible — when you nail a sequence, the physical sensation of being inside that movement is something flat Ghostrunner can't match. But the cost is your equilibrium.

If you have strong VR legs and love Ghostrunner's mechanical precision, this is a genuinely remarkable way to experience it. If you get motion sick from smooth locomotion in any game, this isn't the one to test your limits.

## Performance and practicality

This is a Heavy Demand experience. UEVR's dual-eye rendering roughly doubles the GPU load, and Ghostrunner's fast camera movements need consistent high frame rates to avoid judder. A mid-range PC can get it running, but you'll be adjusting settings. High-end hardware is the comfortable zone. The game's cyberpunk environments — neon-lit corridors, holographic projections, metallic surfaces — actually look striking in VR when the resolution holds up.

VorpX is lighter on resources since it's not doing full dual-eye rendering, but the visual tradeoff isn't worth the performance gain. If your PC can run Ghostrunner flat, it can probably run it via VorpX. If you want the full UEVR experience with motion controls, budget for a higher-end GPU.

## What's actually good

When the UEVR profile clicks — sword in your right hand, wall-run across a gap, swing to kill the guy on the other side, land, deflect, keep moving — there's nothing else like it in VR. The physicality of melee combat with motion controls transforms what was already one of the best-feeling melee systems in gaming. The scale of Dharma Tower's architecture is breathtaking. The instant respawn loop, which can feel punishing in flat mode, actually works in VR because you're never far from the next attempt.

The community profiles are actively maintained and genuinely thoughtful. CYB3R-JUNKI3's work isn't just "inject VR and hope" — it's a considered conversion with specific fixes for camera attachment, scale, cutscene handling, and input mapping.

## What doesn't work

The motion sickness ceiling is real and non-negotiable. Some cameras still attach to the right controller in cutscenes. The flat-screen UI floats in space without VR adaptation. You can't pause and read menus comfortably in the headset. And the base game's difficulty — one-hit death, frequent restarts — means you're doing the same fast sequence over and over, which compounds the vestibular stress.

There's also the legal uncertainty around the R.E.A.L. mod. If you were hoping for a simpler, AER-based alternative to UEVR, the DMCA situation makes that option unreliable.

## The bottom line

Ghostrunner in VR is a C-tier experience: genuinely excellent for the few who can handle it, genuinely punishing for everyone else. The UEVR route with CYB3R-JUNKI3's 6DOF profile is the definitive way to play it in VR — it's free, it's well-built, and it delivers the game's mechanical brilliance in a way flat mode can't. But the speed and motion that make Ghostrunner great are the same things that make VR Ghostrunner a challenge — and the motion sickness ceiling stops most players before the flow state ever clicks. This is only for Ghostrunner fans with strong VR legs who want the most extreme version of the game. If you're looking for a comfortable way to experience Dharma Tower, play the flat version — it's still a fantastic game, and you won't need a fan pointed at your face.

For the right player, with the right hardware and the right stomach, Ghostrunner in VR is one of the most electrifying things you can do in a headset. Just don't say I didn't warn you about the wall-running.
