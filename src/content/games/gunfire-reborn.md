---
title: "Gunfire Reborn VR"
description: "A dedicated community mod turns Gunfire Reborn's frantic roguelite gunplay into a full motion-control VR shooter — aim with your hands, loot with your squad, die a lot."
flatReleaseDate: 2020-05-22
vrReleaseDate: 2023-08-15
lastUpdated: 2023-08-15
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Stable but Quiet
genres:
  - Roguelite
  - First-Person Shooter
  - Action RPG
technicalTags:
  - Full VR Mod
  - BepInEx
  - Motion Controls
  - 6DOF
  - Co-op
experienceTags:
  - Roguelite
  - Co-op
  - Fast-Paced
  - Build Variety
tier: A
verdict: "Gunfire Reborn's VR mod is the closest thing the game has to a native headset edition — full motion controls, decoupled aim, and a roguelite loop that's better on your feet. The setup friction and version drift are real, but if you own it on Steam, this is an easy yes."
heroImage: /images/games/gunfire-reborn-vr-hero.jpg
modDownload:
  url: "https://github.com/xPrinny/GunfireRebornVRMod/releases"
  label: "Download Gunfire Reborn VR Mod"
  note: "Created by xPrinny (Astienth fork maintains updates)"
sources: "GunfireRebornVRMod by xPrinny (GitHub) and the Astienth fork releases, PCVR Central mod listings, Nexus Mods, the PCVR Mods Installer Hub README, the r/GunfireReborn mod-release thread, and VR gameplay coverage from Eurogamer's Ian's VR Corner, Gamertag VR, SteveKnows, and Laserfights."
---

I've died in Gunfire Reborn more times than I care to count. In the headset, a pistol literally in my hand, those deaths hit different — every clean headshot is mine, every stupid flank is on me. The flat game was already a slick, stylized roguelite shooter; this VR mod doesn't just port it, it puts the gun in your grip and lets you lean around cover like you mean it.

## What you're actually installing

There's no official VR mode here. Gunfire Reborn shipped as a flat PC roguelite and never got first-party headset support. What you get instead is a dedicated community mod — GunfireRebornVRMod, built by xPrinny and kept alive through forks like Astienth's — that hooks into the Unity game through BepInEx and switches on a real VR renderer. This is not an injector drawing a flat picture on a floating screen. It's a proper 6DOF rebuild: you aim with your hands, your body turns independently from your head, and the HUD lives on your wrists instead of the corners of a monitor.

Getting there is the catch. You need a Steam copy of the game (the Game Pass build is an outdated version that won't run it), SteamVR installed, the mod files dropped into the game folder, and a `-vrmode OpenVR` launch flag. The live Steam build drifts ahead of what the mod expects, so the installer community pins a specific depot build into its own folder and launches from there — first run needs a close-and-relaunch so BepInEx initializes, plus a manual bypass of the DLC screen. None of it is hard if you've modded a Unity game before, but it's a real afternoon, not a toggle in settings.

## Inside the run

Here's the part that matters: once you're in, this plays like a VR shooter that happens to have a roguelite wrapped around it. Aiming is two-handed and decoupled — you can hold a sightline on a turret while your body strafes the other way, which sounds minor until you're clearing a room and realize you've been doing it without thinking. The wrist HUD is the detail I didn't know I needed: your map sits on the back of your left hand, your copper and essence on the right, and you check them with a glance like a watch instead of pausing to read a sidebar. Grenades and specials are button-triggered rather than physically thrown, a small concession that never broke my flow.

The gunplay is where the mod earns its keep. Gunfire Reborn has always been about weapon variety and build synergy — elemental scrolls, hero abilities, absurd damage stacking — and in VR that loot loop lands harder because you're the one slinging it. Picking up a new weapon and immediately wrist-flicking it onto a target feels native in a way flat FPS conversions rarely do. The stylized low-poly art keeps the performance load light enough that even a mid-range PC holds frame rate without drama. It's snap-turn only with no teleport and the pace is quick, but that's standard for VR shooters and never pulled me out of the fight.

## The hands are the upgrade

The headline is full motion control, and it's not a gimmick. Decoupled aim, 6DOF tracking, two-hand weapon handling — this is the gap between "a game with VR bolted on" and "a shooter that assumes you have hands." The build variety from the base game does real work here too: every run hands you a different weapon mix and scroll set, so the loop doesn't go stale the way bare roguelites can. And it's co-op — you can drop into a squad with flatscreen players, so your friends don't need the mod or a headset to run with you. Honest caveat: there's no networked VR avatar, so nobody else sees your hand movements. To them you're a voice and a gun.

## The tax you pay

Setup is the obvious one, and it isn't a one-time cost. Because the live game updates faster than the mod tracks, you're partly at the mercy of community-pinned builds and fork maintenance — when a patch lands and your pinned version falls behind, you wait for the mod side to catch up. That's the price of playing a modded live game. The lack of physical throwing for grenades and specials is a minor flatness, and there's no standalone or native Quest build: the Quest and Pico clips you'll see are PCVR streamed over Virtual Desktop, not a port. You need a PC and a Steam copy. If you're standalone-only, this isn't your entry point — grab the Steam version first.

## The call

Gunfire Reborn was already a sharp, replayable roguelite with gunplay that rewards experimentation. The VR mod doesn't dilute that — it puts you inside it, hands first, and the result feels closer to a native headset edition than most community projects attempt. The friction is real and the maintenance tax is annoying, but the in-headset experience is genuinely good and genuinely fun. If you own it on Steam and you've got a PCVR rig, install it. If you're on Game Pass or standalone only, the Steam version is the gate.
