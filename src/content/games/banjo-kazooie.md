---
title: "Banjo-Kazooie VR"
description: "Banjo-Kazooie rebuilt as a native OpenXR VR mod on the Lighthouse PC port — nine N64 worlds you can finally stand inside, with motion controls and four view modes."
flatReleaseDate: 1998-06-29
vrReleaseDate: 2026-08-10
lastUpdated: 2026-08-10
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Stable but Quiet
genres:
  - 3D Platformer
  - Collectathon
technicalTags:
  - Full VR Mod
  - Community VR Port
  - OpenXR
  - N64
experienceTags:
  - Motion Controls
  - Multiple View Modes
  - Retro
  - Nostalgia
tier: B
verdict: "A genuine 6DOF rebuild of a 1998 classic that lets you inhabit its worlds rather than watch them, but comfort tooling is still a work in progress. For Banjo fans with a PCVR headset it is the best way to revisit Spiral Mountain; for everyone else it is a charming novelty with rough edges."
heroImage: /images/games/banjo-kazooie-vr-hero.jpg
modDownload:
  url: "https://github.com/RaYRoD-TV/MVRH"
  label: "Download Banjo-Kazooie VR Mod"
  note: "Created by RaYRoD"
sources: "PCVR Mods Installer Hub (Core/BanjoKazooieVR installer README), RaYRoD Multiverse VR Hub repository and rayrodtv.com, Harbour Masters Lighthouse PC port, VRMods-List index, and legaiaflame gameplay showcase footage."
---

I've replayed Banjo-Kazooie more times than I'll admit — first on the N64, later on Xbox 360 at a smooth 60fps. But the version that finally made me sit up in the headset is the one RaYRoD bolted VR onto, built on Harbour Masters' Lighthouse PC port. For the first time I'm not watching Banjo collect Jiggies from a fixed camera. I'm standing in the room where it happens.

## Inside the VR build

There is no official VR mode for Banjo-Kazooie on any platform. What exists is a community rebuild: RaYRoD took Lighthouse — the open-source PC port of the N64 original — and added a native OpenXR renderer on top of it. This is not VorpX-style injection and it is not an emulator wrapper. The whole game renders per eye with true 6DOF head tracking, and it runs as one executable that boots flat when no headset is detected and boots VR when one is.

Getting into it is the usual retro-mod dance, but lighter than most. RaYRoD distributes through the Multiverse VR Hub, a small launcher that pulls the official PC port, applies the VR patch, and keeps it current. You supply your own US (NTSC) 1.0 N64 ROM — the build reads it once to generate its asset file and never needs it again — then launch with your VR runtime already running. No BepInEx, no MelonLoader, no DLL swaps. The README is honest that standalone Quest builds are planned but not here yet, so this is a PCVR experience, full stop. If you're on a Quest, you're streaming it from a PC over Link or Virtual Desktop.

## How it actually plays across every major headset profile — Quest Touch, Index, Reverb G2, WMR, Vive wands — and a gamepad or keyboard keeps working alongside them if you'd rather. The binding is pad-emulation, not hand-tracked grabbing: right trigger attacks, left trigger crouches, right grip jumps, left grip is the camera modifier, and the pause menu opens a VR options overlay, where the grip turns pages. Recenter is holding both triggers for about half a second, confirmed by a haptic tick. It is the right call for a game whose entire vocabulary is "press the jump button," and it means the platforming stays readable instead of fighting a gesture system it was never built around.

What surprised me most is how much the world holds up at life size. Mumbo's Mountain is a small valley you can now actually look up into, and Treasure Trove Cove's beach reads like a diorama you've been shrunk to fit inside. The collectathon loop — find the Jiggies, learn Bottles' moves, survive Gruntilda's Lair — was always about curiosity, and curiosity is exactly what VR rewards. You lean in to check a ledge. You crane your neck at the camera that used to be a fixed angle. The game was built to be explored, and the headset finally lets you.

## Where it earns its keep, and where it doesn't

The honest case for this build is simple: it is a real 6DOF reconstruction of a game that defined the collectathon, and it lets you live in worlds that were always behind a camera. That is the same reason Ocarina of Time and Mario 64 VR ports landed so well — N64 geometry at modern scale just works, and the curiosity that drives a Banjo level is exactly the thing a headset amplifies. The four view modes mean you're never stuck fighting the camera, which is the failure mode every third-person-in-VR project hits. Diorama alone is worth the install for anyone who grew up with the game; seeing Clanker's Cavern or Rusty Bucket Bay as a miniature you orbit with your head is the kind of "oh, that's what that space actually was" moment VR was built for.

The honest case against it is also simple, and it is mostly about maturity. The comfort extras that would make first-person platforming safe for sensitive players — snap-turn vignette, horizon lock — are not in the build yet. Movement is smooth-only, and the verticality plus physical lean in first person is a real, specific load on some people, and the build's own history shows Diorama used to induce sickness before it tracked the head properly. It runs efficiently, but efficiency doesn't fix a camera that occasionally surprises you. And because distribution moved entirely to the Multiverse VR Hub, you don't grab a zip from GitHub; you trust the launcher and its checksum. That's fine, just different from the usual muscle memory.

I'll be blunt about the other routes. Don't bother. The Dolphin VR plus Wii64 emulator setup that floats around in old videos is heavier, older, and unmaintained, and it never gave you the native per-eye renderer this build does. The Pavlov workshop maps that reuse Banjo art are shooter maps, not the game. RaYRoD's native OpenXR build is the highest-quality path by a wide margin, and it is the only one I'd point a reader at.

## The bottom line

Banjo-Kazooie was always a game about poking at a world until it gave up its secrets, and putting that world on a 1:1 scale in front of your face is the most faithful form the game has ever taken. It is not a flawless VR port — the comfort toolkit is a half-built promise, and first-person platforming will test anyone prone to sickness — but it is fully playable, genuinely transformed from the flat version, and built by someone clearly solving the right problems. If you already love this game and you've got a PCVR headset, this is the definitive way to replay it. If you've never cared about Banjo, the novelty will carry you for an afternoon and then the missing comfort options will start to nag. Either way, it's a remarkable thing that a 1998 Rare platformer has a cleaner VR implementation than some games shipped natively this year.

The single hardest problem with a third-person platformer in VR is the camera, and RaYRoD solved it by giving you four ways to look. You cycle them by clicking the right stick.

Third Person is the classic chase cam, but now the bear and Kazooie are life-size in front of you, walking around a world you're standing inside. First Person drops you behind Banjo's eyes — head-directed movement, a physical lean when you peek around corners, the bear hidden from your own view. Diorama shrinks the entire level to a tabletop miniature floating in front of you, and it tracks your head one-to-one. Theater throws the flat game onto a big virtual screen and the README calls it the maximum-comfort option.

Cutscenes and the file-select screen default to that virtual screen on purpose, because scripted camera sweeps read as motion sickness in stereo. There is a Stereo Cutscenes toggle if you want them in-world, but the default is the safe choice. Match Refresh Rate is on by default so the game paces at your headset's native rate, the HUD rides a head-locked plane and can be hidden, and you can tune world scale, stereo depth, eye height, camera distance, and draw distance to taste.

## The controls, and what surprised me

Motion controllers map to the N64 pad
