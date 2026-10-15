---
title: "Aliens versus Predator VR"
description: "A 1999 sci-fi horror classic rebuilt in OpenXR, where the Alien finally climbs walls with your arms and the Marine's motion tracker pings behind your shoulder."
flatReleaseDate: 1999-01-01
vrReleaseDate: 2026-05-25
lastUpdated: 2026-09-27
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - First-Person Shooter
  - Sci-Fi Horror
technicalTags:
  - Full VR Mod
  - OpenXR
  - Source Port
  - Motion Controls
experienceTags:
  - Motion Controls
  - Three-Species Campaign
  - Standalone Quest
  - Melee Combat
tier: B
verdict: "Bassquake's OpenXR rebuild of Aliens versus Predator (1999) is the real thing: per-species motion controls, standalone Quest support, and atmosphere that finally surrounds you. The setup asks for your own Gold Edition files and a little patience."
heroImage: /images/games/aliens-versus-predator-vr-hero.jpg
modDownload:
  url: "https://github.com/Bassquake/Aliens-Versus-Predator-VR/releases"
  label: "Download Aliens versus Predator VR Mod"
  note: "Created by Bassquake"
sources: "Research drawn from the Bassquake GitHub repository for the Aliens Versus Predator (1999) OpenXR source port (atsb/NakedAVP), the VRMods-List index, YouTube VR coverage from TheGeekCrabb, CleXor, Valentin Kozin, Bassquake, YouGotColdYogurt, and For The Love Of Games, and the Flat2VR Discord for peer setup notes."
history:
  - date: 2026-09-27
    note: "The port reaches v1.0 — the first complete release of the OpenXR rebuild."
  - date: 2026-06-24
    note: "Bassquake publishes the first public build of the OpenXR source port of Aliens Versus Predator (1999)."
---

I spent a stupid amount of time this week crawling across a bulkhead as the Alien, claws out, the Marine's motion tracker squealing somewhere below me. That tracker ping lands behind your right shoulder; your body reads it before your ears do. That's the version of Aliens versus Predator I wanted for twenty years, and it finally exists as a community port rather than a studio's afterthought.

This page is about the 1999 original — the one everyone calls AvP Classic — and the OpenXR port Bassquake built from the atsb/NakedAVP source project. It is not about the 2001 sequel (that's a separate game on a separate page) and not about the 2010 reboot, which has only a weaker injection profile elsewhere. One game. One port. One reason to put the headset on.

## What the port actually is

There is no official VR version of Aliens versus Predator (1999). What we have instead is, in the important ways, better than a lazy studio port: a from-scratch VR rebuild of the 1999 game using OpenXR, with motion controls, standalone Quest builds, and PCVR support. The modder going by Bassquake took the atsb/NakedAVP source port and recompiled it around a real VR renderer.

That matters because the 1999 game was built on an engine that treated the camera as a gun with a face. Rebuilding it for tracked controllers and stereo vision is not a wrapper job. The port handles six-degrees-of-freedom head tracking, per-specity controller mapping, and a standalone Quest build that runs at 120Hz. It is actively maintained, with a steady run of releases since the first public build. This is a living project, not a one-and-done upload that rots.

The port ships no game assets. You supply the Gold Edition of the 1999 game yourself, lowercase the filenames with the supplied script, and drop them in. On Quest you sideload the APK; on PCVR you run an installer batch. Budget half an hour if you've modded a game before, longer if this is your first sideload. That friction is the cost of playing a 1999 PC cult classic inside a modern headset.

## Marine weapon grip and motion-tracker dread

The Marine campaign is where the port's VR identity snaps into focus. You hold the pulse rifle or smart-gun with a weapon grip you can disable if it fights your reload timing. The HUD, world scale, and crosshair are adjustable, which matters when a flat game's UI was never drawn to live two inches from your face.

The real star is the motion tracker. In the flat game it was a beeping rectangle at the bottom of the screen. In VR it sits on your wrist, pings behind your shoulder, and turns every corridor into a spatial puzzle. You learn to read direction from sound placement. You learn that silence can be worse than a full sweep. The 1999 game was always about darkness and audio — dripping vents, "they're inside the walls" dread, the click of unseen claws — and in VR that dread finally surrounds you. You're the person hearing the clicks close in.

Comfort options are there: snap and smooth turning, blinders if you want them, adjustable locomotion. The atmosphere does the rest. This is a tense game, not a nauseating one, and the port keeps it that way.

## Alien swipes, Predator swipes, and hold-to-climb

The port's most impressive work is the species-specific motion controls. Pick the Alien or Predator and you are no longer operating a gun — you are operating a body.

As the Alien, you swipe the controllers to claw and tail-strike, and the attack range is tunable so you're not whiffing at air. Climbing is handled with a hold-to-climb option, which lets you scuttle up walls and across ceilings without tapping a button like a rhythm game. Ceiling traversal in VR is disorienting in the best way: the floor becomes a hatch, the Marine squad becomes prey on a map below you, and your own arms are the thing doing the killing.

The Predator plays similarly — controller swipes for melee, wrist-mounted gear, the same vertical freedom — but with the added satisfaction of the cloak and the wrist-computer interface. Both species turn the flat game's melee into something physical. It's not Beat Saber clean, and it doesn't need to be; it's messy, fast, and properly predatory.

## 120Hz on Quest and the Gold Edition catch

The standalone Quest build is the headline feature. A 1999 PC game running at 120Hz inside a wireless headset is a neat trick, and the port pulls it off cleanly enough that performance is not the reason to hesitate. The engine is lightweight by modern standards, so even the standalone Snapdragon can push it without reprojection drama.

The catch is the asset supply. The port needs the Gold Edition specifically; the standard version's language file crashes the build. You also have to lowercase every filename with the included script, and on Quest you sideload the resulting APK. None of this is hard, but none of it is a store page either. PCVR is simpler — installer batch, point it at your files, you're in — but the Gold Edition requirement still stands.

If that sounds like too much friction, it probably is. This is an enthusiast port for an enthusiast game. The reward is a 1999 sci-fi horror classic rebuilt around your body instead of a mouse and keyboard.

## Where the port still shows its age

The port is real, active, and in many ways remarkable, but an A rating demands a level of polish and evidence this release does not have. It is a 1999 game with a community port, no studio QA, and no pile of VR-specific reviews to lean on. Rough edges ship: the setup assumes you can handle a script and a sideload, the UI scaling is functional rather than elegant, and the melee tuning asks for a few minutes of adjustment before it feels right.

This is not a warning to stay away. The port punches above its weight, but it is still a fan rebuild of a twenty-six-year-old game. Buy it expecting a polished remaster and you will be disappointed. Buy it expecting the best version of AvP Classic ever made and you will get exactly that.

If you grew up on this game, or you're a sci-fi horror person who's never touched it, this is the way in. Build your own Alien and go crawl the vents.
