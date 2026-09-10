---
title: "BioShock Infinite VR"
description: "A community mod finally drops you into Columbia with real motion controls — pistol in one hand, a Vigor in the other — but Infinite itself is early access."
flatReleaseDate: 2013-03-26
vrReleaseDate: 2026-08-13
lastVerified: 2026-08-13
routeType: Multi-Route Coverage
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Intense
performance: Moderate Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Action-Adventure
technicalTags:
  - Full VR Mod
  - Injection Driver
  - VorpX
experienceTags:
  - 6DOF
  - Motion Controls
  - Atmospheric
  - Story-Driven
tier: B
verdict: "The bioshock-trilogy-vr mod turns Infinite into a real VR shooter — you're in Columbia with a gun in one hand and power in the other. It's a genuine 'yes, put the headset on' for fans, but only the early game is proven and there are rough edges, so go in knowing it's early access."
heroImage: /images/games/bioshock-infinite-vr-hero.jpg
sources: "Research compiled from the bioshock-trilogy-vr GitHub repository (VR-Stereo-Hub/bioshock-trilogy-vr), its STATUS.md and release notes, the VorpX community settings guide for BioShock Infinite, the VorpX supported-games list, the interleave-vr VorpX setup PDF, the UEVR GitHub page, and Wikipedia for release and engine facts."
---

I've played BioShock Infinite four times on a monitor. The first ten minutes in VR — standing on that railing as Columbia opens up below and ahead — is the only time it's ever felt like a place instead of a cutscene.

There's a new community mod, bioshock-trilogy-vr, that does what no official port ever did: it puts you inside Infinite with real 6DOF head tracking and motion controllers. You hold a pistol in your right hand and cast Vigors with your left. Columbia isn't a screen anymore; it's air under your boots.

This is a Full VR mod, not an injection driver. That distinction matters more than usual here, because the other way to get Infinite into a headset — VorpX — gives you stereoscopic 3D and head tracking but no hands, no presence, no VR UI. The mod is the real thing. And right now, for Infinite specifically, it's early access.

## What you're actually getting

The mod hooks the original, non-remastered Steam version of Infinite — not BioShock: The Collection, which only remastered 1 and 2 anyway. You drop a few DLLs into the game's Win32 folder, set the resolution to something near-square (the mod sizes its eye render target from the backbuffer, and headset panels aren't 16:9), and launch through Steam. VR starts on its own.

Once you're in, it's proper VR. Head tracking is 6DOF. Your right hand is the weapon — every gun keeps its own aim calibration, so the laser actually lines up where you're pointing. Your left hand throws Vigors: Murder of Crows, Devil's Kiss, the works. Movement is body-follows-head, which means you walk where you look. The HUD — health, EVE, ammo — sits on a floating panel you can actually read instead of squinting at a flat overlay.

There's an in-headset tuning overlay for world scale, IPD, and FOV, and it persists. That's a small thing that matters: you can dial the game to your face without ever taking the headset off.

## How it plays

The early game is the proof. Standing on the railing of the floating city, then the gunfight on the airship, then the first Vigor — it lands. Throwing a fireball from your left palm while you line up a headshot with your right is the kind of two-handed VR nonsense that justifies the hardware, and the per-weapon aim profiles mean the pistol, the shotgun, the crank gun all feel like they're in your hand rather than bolted to your view.

It runs on Quest 3 through Virtual Desktop as the primary, best-tested lane, with a 32-bit OpenXR runtime and a SteamVR shim pulling Index, Vive, and WMR headsets in too — though I'd still call Quest 3 over Virtual Desktop the safe bet until the others get more miles. Comfort runs intense on the Sky-Line rail sequences and heavy combat, with smooth locomotion and no teleport or vignette to lean on. On the performance side, a 2013 Unreal Engine 3 title rendering stereo at near-square resolution wants a mid-range PC but isn't a furnace — the early city held frame pace without drama on tested hardware.

## The rough edges

Here's the honest catch. The mod added Infinite in a recent build and labels it "early access — start through early city tested." Everything past the first stretch of Columbia is built on the same engine hooking that already runs BioShock 1 and 2 as fully tuned, playable VR, so the bones are sound. But "tested" and "shipped" aren't the same word, and you're an early traveler past the part they've confirmed.

There's also a broken crosshair-hide feature: per-weapon crosshairs spawned after the opening sweep never get found, so they sit on screen the whole time. It's a visual annoyance, not a blocker, but it's there.

Setup has teeth if you're careless. The mod's injection DLL conflicts with other BioShock 1 head-tracking mods, and OBS Studio has been known to interfere with the 32-bit OpenXR runtime — close it before you launch. And you must own the original Steam Infinite; the remastered Collection version won't hook.

## The other option

If you'd rather not drop DLLs, VorpX will get Infinite into a headset with G3D stereoscopic 3D and head tracking. Community setup guides exist and people call it "quite impressive" in VR. But it's an injection driver: no motion controls, no hands, keyboard or gamepad only, and the UI is a flat overlay floating in space. It's a fine way to look at Columbia in 3D. It is not a way to be in it.

## Should you dive in?

If you already own Infinite on Steam and you've got a Quest 3 with Virtual Desktop — or any OpenXR or SteamVR headset and some patience — the mod is a genuine yes. You're in Columbia with a gun and a Vigor, and the opening hours are the best the game has ever felt. Treat the later chapters as a frontier: the engine work is proven on BioShock 1 and 2, but Infinite past the early city is where you're the tester.

If you've never played Infinite at all, play the flat version first and decide if the world is worth the setup. If you're already a fan, this is the way Columbia was supposed to feel — just don't expect the whole campaign to be battle-tested yet.