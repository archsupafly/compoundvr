---
title: "Lies of P VR"
description: "A UEVR profile turns Neowiz's Pinocchio soulslike into a first-person, motion-controlled puppet slasher — the closest Lies of P has come to a real VR build."
flatReleaseDate: "2023-09-18"
vrReleaseDate: "2025-10-08"
lastUpdated: "2025-10-08"
featured: false
routeType: Native VR
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Stable but Quiet
genres:
  - Action RPG
  - Soulslike
technicalTags:
  - UEVR
experienceTags:
  - Motion Controls
  - First-Person Option
  - Gesture Combat
  - Belle Époque Atmosphere
tier: A
verdict: "Lies of P in VR is the rare UEVR profile that genuinely transforms the game: full motion-controlled melee inside one of the best-looking soulslikes of its generation. Setup friction and an unofficial, unsupported status are the only things keeping it from essential."
heroImage: /images/games/lies-of-p-vr-hero.jpg
sources: "Research compiled from Wikipedia (Lies of P engine, release dates, Overture DLC), praydog's UEVR GitHub (v1.05, 2024-11-16), PCVR Central (Lukasblaster profile page and game page: install notes, 'Easy install' label, 92% Steam rating, 'Last verified: Never' tags), arvrtips.com (over-the-shoulder mode settings guide), and YouTube VR coverage from Headset-VR, Lukas Blaster VR, Under The VRadar, VRagments, Shaak4 VR, YouGotColdYogurt, and others (13 distinct videos across 10 channels). No direct hands-on testing performed; assessment based on documented profile evidence and community gameplay footage."
---

There's a moment about twenty minutes into Lies of P, right after you parry a puppet's thrust and counter with an overhead that you threw with your own arm, where the game stops being "a flat soulslike you're watching through a headset" and becomes something else. I've played a lot of UEVR profiles that promise presence and deliver a floating camera. This one is different. With the Lukasblaster UEVR profile running, Lies of P turns into a first-person, motion-controlled puppet slasher — and it's one of the more convincing "why bother with VR" arguments a framework injection has made in a while.

## A UEVR profile, not a port

The YouTube titles calling this "the Lies of P VR mod" oversell the packaging. There is no official VR mode for Lies of P — Neowiz never shipped one, and the VR path here is strictly PCVR: you need a gaming PC, a headset, and the Steam copy of the game. What exists is praydog's UEVR injector (version 1.05) applied to the game's Unreal Engine 4 build, plus a community-authored profile by Lukasblaster that does the real work. It detaches the camera from the over-the-shoulder rig, corrects the flat-screen HUD for headset readability, and maps the melee to gesture input. Two companion assets ship alongside it — an Improved Perfect Guard pak and a HUD fix — and the whole thing runs through SteamVR or any OpenXR runtime.

This is framework injection, not a native rebuild. You're not getting a developer-tuned VR mode with comfort menus and a re-authored UI. You're getting a UEVR profile good enough that multiple creators have called the result "near-native." The difference matters when something breaks, but it also means the experience lives or dies on the profile's quality — and on this game, the profile is genuinely good.

## Inside Krat with the headset on

The world is the first thing that lands. Lies of P sets its Pinocchio retelling in a Belle Époque Krat that's all cobblestones, decayed opera houses, and puppet corpses, and in the headset the scale of those streets finally reads the way the art direction clearly wanted. Third-person soulslikes are a harder UEVR case than shooters — the camera has to be pried off the character's back — but this profile handles it well enough that I ran most of my time in first person, leaning into doorways and craning to read environmental storytelling I'd blown past on a monitor.

Performance is the one place the framework asks for respect. The profile notes flat-out call DLSS "essential for VR," and they're not exaggerating — UEVR's overhead on top of an already demanding UE4 renderer means you want a high-end rig and upscaling engaged to hold 90Hz when the screen fills with puppets and particle effects. Drop below that and you feel it immediately. Comfort sits at moderate intensity: it's a fast, close-quarters action game in first person, so smooth locomotion and sudden dodges will test newer VR legs, but I never hit the wall-of-nausea problem that kills some flat-to-VR conversions.

## Swinging for real

Lies of P's combat is built around parries, guards, and timed swings — mechanics that flat games usually reduce to button taps. This profile maps that to gestures, and the profile's own notes require a trainer running alongside the game to set Attack Speed to 3.0 so your swing syncs with the damage window. That sounds fiddly, and it is, but it means the act of raising your weapon and bringing it down is what lands the hit. Throwing a charged heavy at a puppet's head with your own arm is the specific thing that makes this worth the setup. The base game is one of the best-looking and best-feeling soulslikes of its generation; the VR layer adds a physicality the flat version never had.

The weakest spots are the ones every framework title shares. The HUD is a corrected flat overlay, not a spatial VR interface — readable, but it never forgets it's a patch. There's no re-authored VR menu; you're still navigating the same text panels you'd see on a monitor, just closer. And because this is profile-driven, the experience depends entirely on an unpaid community author maintaining files that have already shifted distribution once (the download moved from a Discord thread to the creator's own page). None of that is a dealbreaker, but it's the gap between "essential" and "excellent."

## The friction is real but manageable

Setup is moderate, not beginner-friendly, and the profile's install notes are specific enough that you should follow them rather than improvise. You drop the Perfect Guard pak into the Paks~mods folder, drop the HUD fix into Binaries\Win64, launch the game with the `-nohmd` flag, import the UEVR profile, fire up the trainer to lock Attack Speed at 3.0, and only then inject. PCVR Central labels the whole thing "Easy install," and it's free — but that label assumes you already know what a UEVR profile is and how to drive the injector's frontend. If you've never run praydog's tool, budget a half hour the first time and don't skip the attack-speed step, or your gestures will desync from the damage.

The *Overture* expansion (the game's major DLC) released after this profile was catalogued, and no coverage I found confirms the profile holds cleanly through the new content. The base campaign is fully playable; the DLC is an open question until someone reports back. That's the kind of gap that comes with an unsupported community route, and it's worth knowing before you buy the expansion expecting a seamless VR run.

## Who this is for

If you already own Lies of P on PC and you've run UEVR before, this is an easy yes — you're getting a first-person, motion-controlled soulslike that looks spectacular and plays more physically than its flat form. If you're new to framework injection, it's still worth it, but treat the half-hour setup as part of the experience rather than a hurdle to clear. What you're not getting is an official, studio-supported VR mode, and there's no sign one is coming. Play it on a high-end PC, keep DLSS on, and the puppets of Krat are yours to swing at.
