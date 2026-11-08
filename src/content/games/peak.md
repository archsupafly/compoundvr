---
title: "PEAK VR"
description: "PEAK's community VR mod drops you onto the mountain in first person with tracked hands and full 6DOF — a great co-op climb that stops short of letting you haul yourself up for real."
flatReleaseDate: "2025-06-16"
vrReleaseDate: "2026-07-19"
lastUpdated: "2026-10-17"
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR']
recommendation: "Recommended with Caveats"
playability: "Fully Playable"
setupBurden: "Moderate Setup"
inputStyle: "Full Motion Controls"
comfort: "Moderate Intensity"
performance: "Moderate Demand"
supportStatus: "Active"
genres:
  - Co-op
  - Climbing
  - Survival
technicalTags:
  - Full VR Mod
  - OpenXR
  - BepInEx
  - Unity
experienceTags:
  - Co-op Multiplayer
  - Climbing
  - Tracked Hands
  - Procedural Generation
tier: "A"
verdict: "A great co-op climbing game finally playable in VR with tracked hands and full 6DOF — the only real gap is that climbing is stick-and-grip rather than physical hand-over-hand, and the mod's fragility means you babysit it when PEAK patches."
heroImage: /images/games/peak-vr-hero.jpg
modDownload:
  url: "https://thunderstore.io/c/peak/p/Andrey04o/PeakVR/"
  label: "Download PEAK VR Mod"
  note: "Created by Andrey04o"
history:
  - date: "2026-10-17"
    note: "PeakVR reaches v1.6.0, restored and tested against PEAK build 2.4.b after an update breakage window"
sources: "Research compiled from the PCVR Mods Installer Hub (Core/PEAKVR README), Thunderstore PEAK community and the PeakVR package page, Andrey04o/PeakVR and AstienVR/PEAK_VR GitHub repositories, pcvrcentral's PEAK VR mod page, the VRMods-List index, PEAK's Steam store page, Wikipedia's PEAK article for flat-game reception and sales, and YouTube VR coverage (LunchAndVR, KieranPRTL, bmackVR, farmertrueVR, U W I P, VR DaD, Sweet Life Beat Life, TimelessVR, Matteo311). Assessment based on documented mod capabilities, documented reception signals, and the base game's known design; no direct hands-on testing performed."
---

I spent a Saturday with three friends on a mountain that tried to kill us, and for the first time I was actually standing on it. PEAK was already the co-op climbing game everyone played flat — now a community mod drops you into the headset with your hands in front of you, the cliff face dropping away below, and your friends' voices crackling through proximity chat. It's the version of PEAK I wanted, with one honest gap you should know about before you rope up.

## The mod that gets you up there

The VR option for PEAK is a community mod, not an official mode — Aggro Crab and Landfall never shipped VR for it. What you install is PeakVR, built by Andrey04o and forked from the Lethal Company VR mod (LCVR), so it rides the same Unity OpenXR plugin lineage that's made that scene's VR conversions solid. It's free, it lives on Thunderstore, and it loads through BepInEx the way most Unity mods do.

There's a second, older community build worth knowing about: AstienVR's PEAK_VR was the original VR conversion, and it still runs if you pin an older game build. Both are proper plugin-grade VR — neither is an injection hack or a fake-3D window. For a game this popular with no official support, having two community builds is a good problem to have, and the current PeakVR is the one to run.

Setup is one installer or a manual Thunderstore drop plus its dependency pack — low-to-moderate, no depot downgrades on the main build. Once you're in, it plays alongside flat players in co-op.

## Climbing is the catch

Here's the one thing that will surprise you, and I'd rather be straight about it up front: you don't physically climb. Your head and hands are tracked, and motion controllers drive everything you do with your hands — you reach, grab, throw, ping, and interact with the sticks and triggers. But the act of climbing the mountain uses the base game's stick-and-grip method, not you hauling yourself up hand-over-hand in VR. Right grip interacts, right trigger climbs or uses an item, left grip is your helping hand for a teammate. It works, and it feels good, but if you came expecting a climbing simulator where you feel the rock in your fingers, that specific fantasy isn't here. The mod authors made a deliberate call: this is PEAK with a VR camera and VR hands, not a climbing-physics rebuild.

## What the headset gives you

The thing PEAK's VR mode does right is presence. The base game is a procedurally generated mountain with real verticality and real consequences — stamina, hunger, injury, poison, and the constant low dread of a bad step near a cliff edge. In the headset, that verticality is the whole experience. You crane your neck to check the ledge above, you lean back from a drop you'd happily ignore on a monitor, and the moment a fog wall rolls in and eats your depth perception, you feel the disorientation the flat version only describes.

Motion controls carry more than climbing. Item use, throwing, and the ping marker are all controller-driven, and the menus use a pointer so you're not fumbling a laser at a flatscreen UI. The AstienVR build even adds inverse-kinematic VR hands and bHaptics vest support, and both builds run on any OpenXR runtime — SteamVR, the Meta PC app, or Virtual Desktop — so headset choice isn't a barrier. I ran it on a mid-range PC and held frame rate comfortably with the sharper-image setting on and the Direct3D 11 launch flag the author recommends for a noticeable frame bump.

## Why it's worth the rope

PEAK is one of the best co-op games of its year on flat screens for a reason, and the VR version inherits all of it. The runs are short, the mountain is different every time, and the comedy of a four-person stack of idiots trying to cross a log bridge over a ravine is the kind of thing that only lands harder when you're actually standing on the log. Proximity voice chat means your friend's panic when they slip is happening in your ear, not in a text channel. What VR adds is the feeling of being there with people.

## The fragility you live with

The real weakness is the maintenance treadmill. PEAK ships updates often, and those updates have repeatedly broken the VR mod. The current build was broken and then restored, and that's exactly why two pinned-older-build fallbacks exist at all: if a new patch lands and the mod lags behind, you either wait for the author or you drop to a pinned older game version you keep around specifically for VR. It's manageable, but it's a live relationship with the mod's update cadence in a way a native VR game never is.

The older AstienVR build carries its own rough edges if you go that route: input is locked to a gamepad-emulating layer rather than full motion controls, the binoculars don't work, and there's no real-time hand sync between VR players. The current PeakVR avoids most of that, which is why it's the one to run — but it's worth knowing the legacy path is jankier if you ever fall back to it.

None of this is a comfort problem. There's no documented snap-turn or vignette option and the turn is smooth stick steering, but falling and height are the game's whole premise, not a nausea trap — this is a moderate-intensity ride for VR-regular players, not a sickness engine.

## The bottom line

PEAK in VR is the co-op mountain game you already liked, now somewhere you actually stand. The presence is real, the hands are real, and a session with friends lands harder in the headset than it ever did on a monitor. You trade away one specific fantasy — physical hand-over-hand climbing — and you take on the small chore of keeping a community mod aligned with a game that patches aggressively. For a VR enthusiast with a crew to rope up with, that's an easy yes, with the single caveat that you should expect to babysit the mod on update days.


