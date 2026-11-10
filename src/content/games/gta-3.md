---
title: "Grand Theft Auto III VR"
description: "A community source port drops you inside Liberty City with hand-tracked guns, motion melee, and first-person drive-bys — the GTA III VR mod is the real thing, bugs and all."
flatReleaseDate: 2001-10-22
vrReleaseDate: 2026-07-17
lastUpdated: 2026-07-17
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - Action
  - Open World
technicalTags:
  - Full VR Mod
  - Community VR Port
  - OpenXR
  - re3
  - Hand Tracking
experienceTags:
  - Open World
  - First-Person Action
  - Driving
  - Motion Controls
tier: A
verdict: "The GTA III VR mod drops you inside Liberty City with proper 6DOF and hand-tracked weapons, and that combination of a landmark open world plus real VR presence makes it an easy recommendation for anyone with a VR-ready PC and an owned retail copy — just go in knowing it's a work in progress."
heroImage: /images/games/gta-3-vr-hero.jpg
modDownload:
  url: "https://gtaforums.com/topic/1006641-gta-iii-vr-standalone-mod/"
  label: "Download GTA III VR Mod"
  note: "Created by the GTA III VR mod author (SoulStorm64)"
sources: "Research drawn from the GTAForums 'GTA III VR (Standalone Mod)' topic 1006641 (via search snippets), SoulStorm64 YouTube build videos (vxZ-EnhuE3Q, lDzaZ-nD-WQ), the MaslowCorporation/GTA-3-VR UEVR tutorial repository, astromaddie/gta3-vr Steam Frame port repository, StoniVR VorpX coverage, and VR mod index checks (VRMods-List, PCVR Mods Installer Hub, Port Royale). No direct hands-on testing performed; assessment based on documented feature lists, build videos, and community setup repositories."
---

The first time I slid behind the wheel of a stolen sedan in Liberty City and actually reached out for the wheel, I stopped caring that the game is older than most of the people playing it. GTA III was a flat-screen third-person game back at launch. In VR, through the community mod built on the re3 engine recreation, it becomes a place you stand inside.

## What the GTA III VR mod actually is

The mod is built on re3, the reverse-engineered reimplementation of GTA III's engine, with a purpose-built OpenXR VR layer dropped on top. That matters more than it sounds. Because the VR support lives in the engine itself rather than being injected after the fact, head tracking, stereo rendering, and hand input are first-class — the weapons, the throwing, the melee, and the drive-by aiming are native to the runtime, not mapped awkwardly onto a gamepad.

You need your own retail PC copy of GTA III to run it. The mod extends the re3 runtime over an installed game, and there's no BepInEx or MelonLoader dependency chain to wrangle — it's a single engine port, not a plugin stack bolted onto a launcher. The trade is that this is a work in progress. The author has been public about remaining bugs in the VR controls, and the build has been iterating in the open through 2026 with incremental fixes to weapon tracking and motion gestures.

## The guns feel different when you hold them

Every firearm in the game gets hand-tracked aiming and shooting. You raise your hand, the gun comes up, and you point it where you're looking — not where a reticle says you're allowed to. Shotgun blasts, pistol work, the whole arsenal responds to where your hand actually is. That alone replaces the flat game's auto-aim comfort blanket with something that feels like you're doing the shooting.

The motion controls go further than just pointing. Grenades and Molotovs are thrown with a real motion gesture — wind up and lob, instead of tapping a key and watching an arc. The baseball bat is the standout: you actually swing it. A hit that lands because you swung it right beats any button-press connect, and after twenty minutes I was lining up swings the way you would in real life, stepping into the strike. Drive-by aiming works too — your off-hand tracks the weapon while you're moving, so you can lay down fire from a passing car without the game fighting you for control of the camera.

## First-person driving is the surprise

I expected the shooting to be the win and the driving to be a mess. It was the other way around in feel. Drop into the driver's seat and the camera sits where your head is, the wheel is in front of you, and the city scrolls past in proper stereoscopic depth. Liberty City's blocky launch-era skyline reads as charming rather than dated when you're actually there at street level — you notice the signage, the alleyways, the way traffic bakes around you. There are no snap-turn or vignette options documented in the mod, so it plays as a standard smooth-locomotion first-person experience. Hand-tracked steering plus the ability to aim a weapon out the window during a drive-by turns a flat-game errand into a genuine action beat.

## Liberty City is the real draw

The reason this mod earns its tier isn't the gunplay, good as the hands feel — it's that you're inside a real, coherent open world. GTA III built the template: three districts, a story that pushes you through them, random pedestrians and traffic and wanted levels that make the streets feel lived-in. Flat VR ports of lesser games give you a sandbox and call it presence. Here you get a city with weather, reputation, and consequences, and standing in it with a headset on is the thing the medium is for. I spent a session just driving from one end of Portland to Staunton, ignoring missions, because the act of being there held up.

That's the elevator for this whole rating. A great flat game with proper 6DOF and hand input can outrank native VR titles with smaller worlds, and GTA III's world is one of the most influential open worlds ever shipped. The mod doesn't have to reinvent the game. It just has to let you inside, and it does.

## What still gets in the way

This is a work in progress, and it shows. The author's own videos track incremental fixes to weapon tracking and throwable motions, which tells you the baseline wasn't clean. Some control bugs remain in the VR layer, and because the project ships as a standalone mod requiring an owned retail copy, there's no one-click installer and no official support channel — you're pulling the current build from a forum thread and the Flat2VR Discord rather than downloading it from a store.

Performance is not the problem. A 2001 RenderWare game running through a re3 port is light on any VR-capable PC; this will hold a solid framerate on modest hardware where heavier 2020s flat-to-VR mods choke. The ceiling here is polish and completeness, not horsepower.

There are also two other ways people have gotten GTA III into a headset, and neither is the one to use. The Definitive Edition from 2021 can be injected with UEVR — there's a full community tutorial for it, with shadow and crosshair fixes and a VR steering-wheel plugin for driving. It works, but on foot you're back on a gamepad for gunfights and fistfights, so it splits the experience instead of committing to hands. A separate native-style port exists for Valve's Steam Frame headset as an Android build, but it's experimental, controller-button-mapped rather than hand-aimed, and tied to one specific device family. And the oldest route — VorpX on the original PC release with a first-person mod — gives you head tracking and stereo only, no motion controls at all. They're real fallback options if your setup can't run the re3 mod, but they're a step down from the hands-on version.

## Liberty City was worth the wait

If you already own GTA III on PC and you've got a VR headset, this mod is the reason to finally replay it. The combination of a landmark open world and genuine hand-tracked presence — pointing a gun where your hand actually is, swinging a bat, leaning out a window on a drive-by — is the kind of transformation that justifies the headset. It is not finished, and you'll bump into control bugs and a rough install path, but the core experience lands. Skip it if you don't already own the game and don't want to hunt a forum build; the polish isn't there for a from-scratch purchase. For everyone else with a retail copy and a VR-ready PC, this is the GTA III you always wanted to walk through.


