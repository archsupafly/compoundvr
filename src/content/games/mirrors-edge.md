---
title: "Mirror's Edge VR"
description: "DICE's rooftop parkour classic finally has a dedicated VR mod with tracked hands, arm-swing locomotion, and native stereo — but it's alpha, VDXR-only, and not for fragile stomachs."
lastUpdated: 2026-09-19
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Beginner Friendly
inputStyle: Full Motion Controls
comfort: Intense
performance: Moderate Demand
supportStatus: Active
genres:
  - Action
  - Platformer
technicalTags:
  - Geometry 3D
  - Positional Tracking
  - Motion Controls
  - 6DOF
  - OpenXR
experienceTags:
  - Parkour
  - Rooftops
  - Fast Movement
  - Vertigo
tier: B
verdict: "The strongest VR route Mirror's Edge has ever had, and one of the few flat games that genuinely becomes physical in VR — arm-swing locomotion turns the rooftops into full-body parkour. It remains a niche proposition: the project is alpha, it runs only through Virtual Desktop's VDXR runtime, and it does nothing to soften Mirror's Edge's punishing comfort design. Worth it if you have strong VR legs and patience for an unfinished build; not for newcomers."
flatReleaseDate: 2009-01-13
vrReleaseDate: 2009-01-13
heroImage: /images/games/mirrors-edge-vr-hero.jpg
modDownload:
  url: https://github.com/letsgosportsteam/mirrors-edge-vr-mod/releases
  label: Download Mirror's Edge VR Mod
  note: Created by LetsGoSportsTeam
history:
  - date: 2026-09-19
    note: Dedicated VR mod reached v0.2.2-alpha, adding motion controls, 6DOF tracking, and tracked hands, pistols, and parkour over the previous VorpX route.
sources: "Research conducted via the LetsGoSportsTeam/mirrors-edge-vr-mod GitHub repository and README, YouTube VR gameplay footage (Beardo Benjo, NotAGameAddict, CaptainsRath, LetsGoSportsTeam), Flat2VR Discord community knowledge, Reddit community reports (r/mirrorsedge, r/vive), and VorpX official forums and documentation for the legacy injection-driver route. No direct testing performed."
---

The first time you look down from a rooftop in Mirror's Edge in VR, your body rebels. The city falls away in layers of white concrete and arterial red, and some primitive part of your brain insists that you are actually standing on the edge of a building. That moment — the lurch in your stomach, the instinct to step back — is the entire pitch. Mirror's Edge was always about height and momentum and clean lines, and in stereoscopic 3D those qualities become physical in a way the flat screen never managed.

## What the Mirror's Edge VR Mod Actually Is

The way to get there changed. A dedicated VR mod by LetsGoSportsTeam now replaces the old injection-driver route as the default answer. It is still alpha — four GitHub releases, all tagged prerelease, three open issues and zero closed — but it already delivers native stereo, 6DOF head tracking, motion controllers, and a set of motion interactions the README describes as tracked hands, pistols, and parkour. Hardware coverage is limited and those motion interactions are explicitly experimental, which is the honest frame for everything that follows. This is a genuinely capable project under active development, not a finished product.

## How to Install the Mirror's Edge VR Mod

Setup is unusually light. The release zip contains three files — `d3d9.dll`, `openxr_loader.dll`, and `mevr.ini` — that drop into the game's `Binaries` folder next to `MirrorsEdge.exe`. No INI editing is required out of the box. The hard requirement is the runtime: this build supports Virtual Desktop with VDXR, and the README says plainly that SteamVR and Meta Link/Air Link are not supported by the mod's current 32-bit OpenXR path. A reader on SteamVR or Link cannot use this mod today. There is an open GitHub issue asking whether SteamVR support is coming, and it has not been answered yet.

## Mirror's Edge VR Setup Problems and Fixes

There are a few real gotchas to know before you start. PhysX must be disabled in the game's settings; if a chapter load freezes, that is the first thing to check. The mod needs the x86 Microsoft Visual C++ 2015–2022 Redistributable — the x64 package alone is not enough. Resolution defaults to Auto and may need a relaunch to catch the headset size, and if stereo still fails after a level loads, F6 rescans. None of this is hidden; the README documents all of it. The point is that "light setup" does not mean "zero troubleshooting."

## Motion Controls and Gameplay

What you get for that effort is a much more physical Mirror's Edge. The default control scheme uses arm-swing locomotion for running, raising both hands above your head to jump, physically crouching to slide, and gripping ledges or pipes hand-over-hand to climb. Pistols — the Colt1911 and Glock18c — follow either hand with controller aiming, picked up by looking at one within two meters and squeezing the grip. Punching and disarms are mapped to grip-based gestures. A long press of Y opens a VR settings panel for recentering, turning style, frame cap, resolution, UI size, and comfort toggles. Arm-swing running and motion hands are both on by default.

## What "Tracked Hands" Actually Means

The crucial clarification: when the README says "tracked hands," it means the controllers are tracked as hands, not that you can play with bare hands. The mod author's own trailer title calls it "Full Hand Tracking Showcase," but the README contradicts that. It is Touch controller tracking. Calling it anything else would be misleading.

## How Mirror's Edge VR Plays

Once it is running, the experience is still dominated by the same qualities that made the injection-driver profile compelling. The sun-bleached rooftops, saturated reds and blues, and clean geometric world read instantly in a headset. Judging jump distances is more intuitive with true stereoscopic vision. The sense of speed and verticality is amplified by the depth. But now it is also a fitness experience. Arm-swinging across those rooftops for any length of time is exhausting in the way CaptainsRath's "IS EXHAUSTING" framing suggests. The game does not hold back on sustained sprinting, and your arms will remind you of that.

## Comfort, Camera Snapping, and Frame Rate

The comfort problems are still the same ones that made the original VR route punishing. Mirror's Edge was built without any consideration for VR comfort, and the mod does not rewrite the game. Ledge grabs snap the camera. The hard-landing roll yanks your view through a rotation. Sliding down ramps delivers sustained vestibular conflict. Cutscenes seize the camera entirely. The default frame cap is 72 FPS, and the README recommends capping at a rate your PC can hold that matches or evenly divides your headset refresh — 60 FPS on a 120 Hz headset, for instance. A high-end PC helps, but no hardware fixes the core design. This is not a game for newcomers to VR.

## Mirror's Edge VR vs VorpX (and Why Not Catalyst)

If the mod does not work for your setup, the legacy VorpX route still exists. It gives true Geometry 3D, positional head tracking, and automatic FOV adjustment through DirectVR scanning, but it remains keyboard-and-mouse-or-gamepad play with no motion controls. The original's FOV can be finicky; if the DirectVR scan misses, the view feels zoomed-in and claustrophobic, and you may need to push the horizontal FOV toward 112 degrees. For most people in 2026, the mod is the better first attempt.

A brief word on the sequel: Mirror's Edge Catalyst does not share the original's good fortune. The VorpX profile for Catalyst relies on Z-Normal reconstruction rather than Geometry 3D, which produces a weaker stereo effect that degrades further on nearby objects. Head tracking is handled through mouse emulation with visible latency, making precise platforming harder rather than easier. The mod itself requires the original game rather than Catalyst. If you are looking for parkour in VR, stick to the 2008 release.

## Who Should Play Mirror's Edge VR

So who is this for? If you have strong VR legs, a tolerance for alpha software, a Virtual Desktop setup with VDXR, and any affection for first-person platforming, this is now the obvious way to play Mirror's Edge in a headset. The motion controls remove the old input ceiling, and the physicality of arm-swing locomotion makes the rooftops feel less like a visual spectacle and more like a full-body activity. The alpha status and VDXR lock-in are real caveats, not footnotes. The lack of closed issues and limited hardware coverage mean your mileage may vary, and you should expect to tinker.

If you are prone to motion sickness, if you run SteamVR or Link as your primary PCVR path, if you want a plug-and-play experience with no configuration, or if you expect bare-hand tracking, this is not your game. The comfort is intense, the runtime requirement is narrow, and the project is unfinished. But for the right player, the trade is worth it. Those rooftops are still there, waiting, and in a headset they feel higher — and more exhausting — than ever.
