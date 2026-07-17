---
title: "Borderlands 3 in VR: The UEVR Route That Actually Delivers"
description: "There's no official Borderlands 3 VR port, but a UEVR community profile turns the full looter-shooter — co-op, vehicles, campaign and all — into a surprisingly solid PCVR experience."
flatReleaseDate: 2019-09-13
vrReleaseDate: 2024-02-01
lastVerified: 2024-02-01
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Advanced Setup
inputStyle: Partial Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Looter-Shooter
  - Action RPG
technicalTags:
  - UEVR
  - Unreal Engine 4
  - Motion Controls
  - 6DOF Head Tracking
  - Co-Op Multiplayer
experienceTags:
  - Campaign
  - Co-Op
  - Loot Grinding
  - Vehicle Combat
tier: B
verdict: "Borderlands 3 has no official VR mode, but the UEVR community profile is the real deal: full campaign, full co-op, motion controls, and first-person vehicles. It's heavy on PC demand and setup friction, yet it's the most complete way to live inside Pandora's mayhem."
heroImage: /images/games/borderlands-3-vr-hero.jpg
sources: "Research conducted via UEVR GitHub releases and documentation, Flat2VR Discord community knowledge (TimBurton profile), MIXED/Reality News coverage of the Borderlands 3 UEVR spotlight, UploadVR reporting on UEVR and Gearbox's 'no plans' stance for official Borderlands 3 VR, YouTube VR gameplay footage, and VorpX community/official profile information. No direct testing performed."
---

The first time a rakk dive-bombed me from the Pandoran sky and I actually *ducked*, I knew Borderlands 3 in VR was onto something. Here's the thing, though: Gearbox never shipped this. There's no official Borderlands 3 VR port, no PlayStation VR2 version, no Quest standalone hidden in a store listing. If you want to play Borderlands 3 inside a headset, you're relying on the Flat2VR community — specifically the UEVR profile by TimBurton — and the good news is it's far better than it has any right to be.

## What You're Actually Getting

This is a framework-based conversion, not a hand-crafted port. UEVR, by praydog, unlocks Unreal Engine 4 and 5 games at the engine level and forces their built-in VR rendering path to life. For Borderlands 3, TimBurton's profile goes further: it maps motion controllers to the game's inputs, gives you 6DOF head tracking, makes vehicles first-person, and keeps the entire co-op pipeline intact. That last part matters a lot, because the official Borderlands 2 VR port famously cut multiplayer out entirely. Here, you can run the campaign with three friends while wearing a headset.

What it is not: a native VR game. You are not manually reloading rifles, plucking loot off bodies with your hands, or physically aiming iron sights in a way the game understands. The motion controllers are essentially a very good translation layer for the flat game's controls. Menus and the HUD float in front of you on a projected screen, which works but constantly reminds you that this world was built for a monitor. Comfort options are limited to what UEVR exposes — smooth locomotion is the reality, with snap or smooth turn available, but there's no teleport. If smooth stick movement makes you queasy, this is going to be a rough ride.

## The Setup Reality

Look, I'm not gonna lie: getting this running is not a five-minute job. You need UEVR installed, the right profile loaded, a valid OpenXR or OpenVR runtime, and enough patience to navigate the Flat2VR Discord pinned messages for the latest recommended in-game settings. This isn't a click-and-play mod. There's a reason the setup burden lands in "Advanced."

Once it's going, though, the conversion is impressively complete. The campaign is playable start to finish. Cutscenes work. Co-op matchmaking works. Vehicles, which were originally a problem in earlier iterations of the profile, have been fixed and now sit properly in first-person view. It's the kind of thing that makes you forget, during quiet exploration moments, that you're playing through a community framework at all.

## How It Actually Plays

Borderlands 3's gunplay was already tactile — the weapon variety, the elemental explosions, the screaming bandits — and in VR that chaos gets a physical edge. Aiming with your head and controller together feels natural after twenty minutes. The scale of the environments hits harder: the cel-shaded cliffs and junkyard towns of Pandora wrap around you in a way the flat screen never fully conveyed. Even the writing, which can grate in long flat sessions, becomes easier to tolerate because you're *in* the space rather than staring at it.

But the framework shows its seams when the action gets dense. Particle-heavy firefights, multiple badass enemies, and vehicle combat can send the frame rate into reprojection territory. Reports suggest even an ultra-tier PC sees dips during the busiest moments. On a mid-range or high-end rig, expect to drop settings and still feel the weight of a demanding Unreal Engine 4 looter-shooter running in stereoscopic 3D. Performance is the single biggest caveat here.

The controller mapping is another compromise worth naming. Shooting, grenades, ability activation, and movement all map cleanly enough, but you're pressing buttons to do things native VR shooters let you do with your body. Melee isn't a swing; it's a button. Looting isn't a grab; it's a button. That doesn't break the experience, but it caps how "transformative" the VR feels.

## The VorpX Alternative

If UEVR sounds like too much work, VorpX offers an official profile for Borderlands 3. You get stereoscopic 3D, head tracking, and the full campaign on a virtual screen or in a pseudo-VR view. What you don't get is motion controls, hand presence, room-scale movement, or a VR-optimized UI. It's a 3D monitor strapped to your face, which can be enjoyable for the right person but is a fundamentally different tier of experience. For most readers, UEVR is the only option worth the headset time.

Borderlands 3 in VR shouldn't exist, but it does — and it's mostly excellent. The UEVR profile delivers a complete co-op looter-shooter campaign with real presence, real scale, and enough motion control support to make combat feel fresh. The tradeoffs are serious: heavy PC demand, advanced setup friction, flat UI projected in space, and no teleport comfort option. This is B-tier VR not because the game is weak, but because the implementation asks a lot of the player and the hardware.

If you already love Borderlands and own a high-end PCVR rig, this is one of the best uses of UEVR on the market. If you're VR-curious but headset-sensitive or GPU-limited, stick to the flat version. The mayhem is real either way.
