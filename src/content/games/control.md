---
title: "Control VR"
description: "Control reaches VR only through VorpX — a stereoscopic 3D window into the Oldest House, not a headset-native experience."
flatReleaseDate: 2019-08-27
vrReleaseDate: 2019-11-21
lastVerified: 2019-11-21
featured: false
routeType: Framework Only
platforms: ['PCVR']
recommendation: Enthusiasts/Tinkerers Only
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Mixed Input
comfort: Intense
performance: Moderate Demand
supportStatus: Stable but Quiet
genres:
  - Action-Adventure
  - Supernatural
  - Third-Person Shooter
technicalTags:
  - Injection Driver
  - VorpX
  - Z-Normal 3D
  - Northlight Engine
experienceTags:
  - Third-Person
  - Telekinesis
  - Diorama Effect
  - Stereoscopic 3D
tier: C
verdict: "Control via VorpX is a stereoscopic 3D curiosity, not a VR experience — you watch Jesse Faden's story through a window instead of living it. Worth a look only if you already own the game and VorpX and want to see the Oldest House with depth; otherwise the flat version remains the better way to play."
heroImage: /images/games/control-vr-hero.jpg
sources: "Research compiled from VorpX official supported-games list and VorpX community forums (user reports of Red Dead Redemption 2 profile compatibility, DX11/DX12 hooking behavior), Remedy Entertainment's July 2019 developer interview on VR suitability (GamingBolt), and Control platform/engine documentation (Wikipedia, Remedy). Assessment based on documented injection-driver capabilities and third-person camera behavior."
---

I spent a weekend trying to stand inside the Oldest House. Remedy's brutalist skyscraper — concrete that breathes, hallways that lie about where they lead — is one of the most striking spaces in modern games, and I wanted to occupy it, not just watch it.

There is exactly one way to do that in a headset, and it isn't a port. It's VorpX.

## What you're actually getting

VorpX is an injection driver, not a VR engine. It hooks into Control's render pipeline and reconstructs the flat image into stereoscopic 3D with head tracking. That's the whole trick. You get depth and the ability to look around the scene by moving your head. You do not get motion controls, hand presence, a VR-optimized interface, or any sense that you are Jesse Faden. Control is a third-person game, so the camera sits behind and above her shoulder — in VorpX, that means you're peering at a diorama, not wearing the character's eyes.

The stereo effect is Z-Normal 3D, which builds depth from the image's depth buffer rather than rendering true geometry. It works, and the Oldest House gains real volume — those vast concrete atria finally have scale you can feel — but it's a step behind Geometry 3D, and transparent surfaces or particle effects won't separate correctly between eyes. There's no custom Control profile in VorpX; the community runs it on the Red Dead Redemption 2 profile as a base, which gets you there but isn't tuned for this game.

## How it plays

You play Control exactly as you would on a monitor: keyboard and mouse or a gamepad, aiming a screen-space reticle, triggering Jesse's telekinetic powers from hotkeys. VorpX passes your inputs through untouched. The head tracking lets you lean and look, but the camera itself is the game's — when Jesse dashes with Evade or hurls a desk across a room with Launch, the view swings on rails you don't control.

Performance sits at moderate demand. Control is a 2019 AAA title with heavy rendering, and VorpX adds stereoscopic overhead on top, so you'll want a mid-range or better PC to hold frame rate. One hard constraint: VorpX only hooks the game's DirectX 11 mode. DirectX 12 doesn't initialize the driver, which locks you out of the ray-traced reflections that made Control's surfaces sing on capable hardware — you're playing the DX11 build, flat lighting and all.

The third-person camera is the honest catch — because the view follows Jesse rather than your head, fast combat and reality-bending set pieces can turn the stomach in a way native VR rarely does.

## What's genuinely good here

The art direction carries the experience. Remedy built a world that looks incredible in flat, and stereoscopic depth adds something real to the brutalist architecture and the paranormal corruption creeping through it. The shifting environments — offices that rearrange while you watch, gravity that decides to lie — read differently with volume behind them. If you already love Control, seeing the Oldest House with actual depth is a novelty worth an evening.

## Where it falls apart

It is not VR. No presence, no room-scale, no sense of being inside the event. You are a passenger watching a well-directed action movie through a 3D window. For a game whose entire identity is kinetic, physical movement — Jesse flipping through the air, debris flying under your telekinetic grip — watching it from a fixed shoulder cam drains the thing that makes Control feel alive.

Beyond the conceptual limit, the execution has rough edges. Z-Normal 3D means some visual effects won't stereo-separate, so occasional flicker or flat-looking particles break the illusion. The lack of an official profile means menu text and HUD sit as a flat overlay in space rather than integrating into the world. And you're locked to DX11, which is a real visual downgrade from the ray-traced build.

Remedy themselves flagged this before launch. When asked about VR, director Mikael Kasurinen said the game's pace and physical movement would make for "quite a nauseous experience" in a headset — and through VorpX, with a camera you don't own, that assessment lands as a warning rather than a rejection.

## Should you bother?

If you already own Control and VorpX, spend an hour with the depth on. The Oldest House in stereoscopic 3D is a neat way to revisit a great game, and the atmosphere holds up. But don't buy either for this. There's no motion-controlled Jesse, no presence, no VR-native moment waiting in the Bureau's depths — and the flat version, on a good display with the ray-traced lighting, is still the real Control.
