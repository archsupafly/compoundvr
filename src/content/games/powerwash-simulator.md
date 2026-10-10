---
title: "PowerWash Simulator VR"
description: "A cozy cleaning sim that turns out to be a near-ideal VR fit — if you can get the community's full 6DOF mod running on your copy."
flatReleaseDate: 2022-07-14
vrReleaseDate: 2025-10-23
lastUpdated: 2025-10-23
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Enthusiasts/Tinkerers Only
playability: Partially Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Comfortable
performance: Efficient
supportStatus: Active
genres:
  - Simulation
  - Casual
technicalTags:
  - Full VR Mod
  - MelonLoader
  - OpenXR
  - Roomscale
experienceTags:
  - Cozy
  - Satisfying Loop
  - First-Person
  - Roomscale
tier: B
verdict: "PowerWash Simulator is a near-perfect VR fit — holding the washer and chasing grime across a dirty van is exactly the tactile loop this headset was built for — but the full 6DOF mod is built for PowerWash 2 and its PowerWash 1 support is unverified, so treat it as a tinkerer's project and confirm your copy runs before you commit."
heroImage: /images/games/powerwash-simulator-vr-hero.jpg
modDownload:
  url: "https://github.com/onetin84/Wet-Reality-XR-PWS2/releases"
  label: "Download PowerWash Simulator VR Mod"
  note: "Created by onetin84"
sources: "PowerWash Simulator (FuturLab / Square Enix Collective) flat-release and series context via Wikipedia and powerwashsimulator.wiki.gg; VR mod details from the Wet Reality XR (onetin84) GitHub repository and the PCVR Mods Installer Hub README; PWS1 VorpX fallback evidenced by Paradise Decay's YouTube coverage; additional mod coverage from Tino, NotAGameAddict, FastLawyer, and Obscure Nerd; current mod version and PWS1 compatibility confirmed via the Flat2VR Discord."
---

There's a moment in PowerWash Simulator where you finish a vehicle. The whole side of the van goes from encrusted brown to factory white in a slow sweep of your nozzle, and the game throws a little chime. Flat, on a monitor, that chime is a checkbox. In the headset, with the washer actually in your hand and the spray fanning out across the panel two feet from your face, it lands differently — like you did a small, stupid, deeply satisfying chore and the world noticed.

That's the whole pitch for PowerWash in VR. This is a cozy cleaning sim whose entire interaction model is "point a tool at a surface and hold the trigger." That is, almost suspiciously, the exact thing VR controllers were invented to do. The community noticed, and a modder going by onetin84 built Wet Reality XR — a full 6DOF VR mod that puts the washer in your hands with tracked motion controls, two-handed handling, haptics, and roomscale support.

Here's the catch you need to hear up front, because it changes how you should approach this: Wet Reality XR is built for PowerWash Simulator 2. The mod's cinematic trailer titles it as covering "PowerWash Simulator 1 & 2," but the publisher's own install README is blunt about it — the mod is for the sequel, and the first game is "unsupported." So if you're here for the original PowerWash Simulator (the one that blew up on Game Pass), the full VR mod is a claimed-but-unverified path. You might get it running on your copy. You might not. Confirm on the Flat2VR Discord before you sink time into setup.

That uncertainty is the difference between this being a clean recommendation and a tinkerer's weekend. Everything below describes what the mod delivers when it works — because when it works, it's genuinely good.

## Getting it running

The install is moderate, not brutal. The PCVR Mods Installer Hub automates most of the heavy lifting — it drops in MelonLoader, the portable .NET runtime, and the Unity OpenXR boot layer, then pulls the two mod assemblies. You need your OpenXR headset software running first (Quest 3 works fine streamed over Virtual Desktop; any SteamVR or OpenXR PCVR headset is in scope), and the first launch does a quiet ~30-second initialization. One gotcha: if you've got UnityExplorer sitting in your Mods folder from another project, pull it — it conflicts.

## What it actually feels like

Once you're in, the washer tracks your controller in six degrees of freedom and the gaze and aim are fully decoupled — you look where you want, the nozzle points where your hand points, which is exactly how a real pressure washer behaves and exactly how a lot of flat-to-VR ports get it wrong. Right trigger sprays. Right grip toggles continuous spray so you're not white-knuckling the trigger for twenty minutes. Left stick walks you around, because you're not actually roomscaling your way across a two-story house. Menus are driven by a pointer ray rather than a flat cursor you'd have to squint at, which is the kind of small VR-native touch that separates a real mod from a head-tracking afterthought.

And the loop is just... good in here. PowerWash is fundamentally about coverage and feedback: finding the last speck of grime on a wheel well, watching the dirt retract as the spray lands, hearing the pitch of the motor change when you swap to the turbo nozzle. That feedback is spatial now. You're leaning in to get the underside of a bumper. You're craning to reach the roofline. The satisfaction that made this a comfort-game phenomenon on flat screens is the same satisfaction, but your body is part of it instead of watching a character's body do it.

Comfort is a non-issue — the recent beta builds added teleport, snap turning, and a comfort vignette for anyone who wants them, but this is a slow, stationary-ish cleaning game. You're not getting motion sick chasing grime. It runs efficiently too; this isn't a demanding title, and a mid-range PC pushes it comfortably at 90Hz.

## The honest limitations

Two things keep this from being a flat-out recommendation. The first is the PowerWash 1 support question I opened with: the mod is scoped to the sequel by its own maintainer, and the first game's compatibility is a community claim, not a documented feature. If you own PowerWash 1 and not PowerWash 2, you're betting on an unverified path. The VorpX fallback exists for PowerWash 1 specifically — Paradise Decay put out a video calling it "a BLAST" — but that's stereoscopic 3D with head tracking and gamepad input, no motion controls, no hand presence. It's a way to be inside the game, not a way to hold the washer. For most of our readers that's a meaningfully lesser experience, so treat VorpX as the floor, not the goal.

The second limitation is maturity. Wet Reality XR is a beta that ships as a prerelease — the maintainer is actively iterating (recent builds added haptics tuning and a turbo-nozzle fix), which is great for momentum but means you're tracking a moving target. Profiles and versions shift; the Hub auto-tracks updates, but you should confirm the current build on the Flat2VR Discord before installing. This isn't abandonware, but it's not a polished 1.0 either.

## Who should bother

If you're already a PowerWash person — and a lot of you are; this thing was a Game Pass staple for a reason — and you own PowerWash 2, this is an easy yes. The full 6DOF mod turns a game you already liked into one you physically do, and the tactile loop is arguably better in VR than flat. Grab it, confirm your build on the Discord, and spend a Sunday making a fire truck gleam.

If you only own the original PowerWash Simulator, I'd hold the recommendation. The mod author doesn't claim your copy, the VorpX route is a thinner experience, and betting a setup afternoon on an unverified path is a different value proposition than installing something the maintainer stands behind. Check the Discord for current PowerWash 1 reports first — if people have it running clean, great; if the threads are quiet, that silence is your answer.

Either way, this is a tinkerer's project, not a store-page download. But the core truth holds: PowerWash Simulator is one of those games where you finish a job, step back, and the whole thing is just clean — and doing that with the washer in your own hands is the version of the game the concept always deserved.
