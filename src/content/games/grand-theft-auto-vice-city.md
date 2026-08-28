---
title: "Grand Theft Auto: Vice City VR"
description: "A full 6DOF VR conversion of Rockstar's 1986 Miami classic finally puts you on the streets of Vice City with your own hands — driving, shooting, and causing chaos from inside the headset."
flatReleaseDate: "2002-10-29"
vrReleaseDate: "2026-07-22"
lastVerified: "2026-08-22"
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Active
genres:
  - Action-Adventure
  - Open World
technicalTags:
  - Full VR Mod
  - OpenXR
  - 6DOF
  - reVC
  - Standalone Quest Port
  - UEVR
experienceTags:
  - Third-Person
  - Open World
  - Motion Controls
  - Driving
  - Classic Game
tier: A
verdict: "The Vice City VR mod turns a 2002 masterpiece into a real room-scale 6DOF experience — walking, driving, and shooting 1986 Miami with your own hands. It's an alpha with genuine rough edges, but if you have a PCVR headset and a legal copy of the game, this is the way to play Vice City now."
heroImage: /images/games/grand-theft-auto-vice-city-vr-hero.jpg
sources: "Vice City VR mod and standalone Quest port GitHub repositories; reVC open-source engine project; Flat2VR Discord community discussion; UEVR/Praydog project and releases; vorpX supported-games listing; PPSSPP VR documentation; Wikipedia (Grand Theft Auto: Vice City and The Definitive Edition); media coverage via ixbt.games, Sportskeeda, and pcvrcentral listings."
---

I bought Vice City again last month — not because I needed another copy, but because a solo modder finally did what Rockstar never bothered to. The Vice City VR mod drops you straight into 1986 Miami with tracked hands, a working pistol, and a convertible that responds to your actual grip on the wheel. The first time I pulled out of an Ocean Beach parking lot and the windscreen swung up to fill my view, I forgot I was playing a game that shipped before half this headset's owners were born.

## What you're actually installing

This isn't a profile bolted onto the flat game. It's a native VR rebuild of the 2003 PC release, built on the reVC reverse-engineered engine, running through OpenXR with stereoscopic 6DOF. You point it at a legal copy of the original game, drop the mod files next to it, set your OpenXR runtime, and launch reVC.exe. That's the whole setup — no patching the original binary, no dependency hell. The mod ships no game data, so you do need to own Vice City proper, but once it's in place it boots into a VR welcome card the moment Tommy takes his first step.

It's an alpha, and the developer is moving fast — the campaign has already been finished start to finish by players, and recent builds added hand tracking, immersive vehicle steering, and a traffic-density system that lets you crank pedestrians and cars from half to triple the normal count. Bugs exist, and the README is honest that mission-specific or runtime-specific issues may still bite. But this is a living project, not a one-week wonder.

## Standing inside the world

The thing that hooked me isn't the shooting — it's the scale. Vice City was always a postcard of a city, but flat screens flatten it. In the headset, the neon of Washington Beach actually wraps around you, and the draw distance finally reads like a real horizon instead of a painted backdrop. Walking up to a building and craning your neck to find the rooftop sniper nest is a small thrill the original never delivered.

Combat is where the hands earn their keep. You draw with a grip, dual-wield by grabbing a second piece, and stash weapons on holsters that follow your view. Pistols get physical scopes you raise to your eye; melee swings connect from where your hand actually is, not a button press. Reloading is an optional physical motion on supported firearms, and the calibration per weapon actually holds once you set it. Drive-bys work — you lean out the window and fire with the other hand on the wheel.

Vehicles are the standout. Cars take one-handed physical steering, and bikes let you twist the right controller like a throttle or just hold the trigger to accelerate. The HUD can sit on your wrist in stereo if you want it, or stay head-locked if you don't. Snap and smooth turning, body-relative or head-directed movement, and a horizon lock for the motorcycles keep the fast third-person driving manageable rather than nauseating.

## The rough edges are real

This is an alpha of a 23-year-old game rewritten for VR, so the cracks show. Occlusion culling — the trick that hides geometry behind buildings — occasionally pops an eye or clips a wall; there's a toggle, but you shouldn't need it. The optional modern asset packs look fantastic and will happily crush a mid-range GPU, especially the vehicle and vegetation upgrades, so most players will run the classic models and only mix in modern textures where it matters. Some controller combinations, particularly a few SteamVR setups, still want a custom binding pass before everything lines up. And because the base game is third-person, your viewpoint is always over Tommy's shoulder — that's the design, not a failure, but it means you're inhabiting a character, not a floating camera.

None of that stopped me from sinking a weekend into it. The bones are that good.

## The other ways in

If you already own the Definitive Edition remaster, UEVR will inject Vice City's UE4 build into a headset. It's head-tracking and gamepad only — you're watching Tommy from behind inside a headset, not reaching for the wheel. Fine as a curiosity if the remaster is already in your library, but it's a lesser thing than the mod, and unlike the San Andreas DE it never got a dedicated 6DOF motion-control plugin.

The old VorpX profile is the fallback of last resort: stereoscopic 3D and head tracking, none of the hands. You'd register Vice City against the San Andreas profile and hope for the best. It works in the limited sense that any third-person game works through VorpX, but it's a TV in a headset, not Vice City in VR. Phone-streaming apps from the mid-2010s are the same story with worse latency — skip them.

For Quest owners, there's a standalone port built on the same engine, but it's a source kit, not a store download. You run a build script on a PC, it assembles the APK and pulls your game data across, and you sideload it yourself. High effort, no PC in the loop once it's on the headset, and early reports say it runs clean with full touch controls. There's no PSP, GameCube, or Xbox emulator angle here either — Vice City never shipped on those systems, so the usual emulator-VR tricks don't apply.

## Who this is for

If you have a PCVR headset and a legal copy of the 2003 game, the Vice City VR mod is the definitive way to play it — a world that was already worth living in, now something you stand inside. The Quest kit is worth the build effort if you'd rather not tether, but the PC path is where the project is moving fastest. Either way, this is the GTA VR we were promised two console generations ago, and it finally showed up.
