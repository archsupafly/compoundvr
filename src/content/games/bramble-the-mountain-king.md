---
title: "Bramble: The Mountain King VR"
description: "A gorgeous Nordic folklore platformer becomes a diorama-scale horror show in UEVR — but its side-scrolling camera was never built for a headset, and the novelty only goes so far."
flatReleaseDate: '2023-04-27'
vrReleaseDate: '2024-01-01'
lastVerified: '2024-01-01'
featured: false
routeType: Multi-Route Coverage
platforms:
  - PCVR
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Gamepad Preferred
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Stable but Quiet
genres:
  - Action-Adventure
  - Platformer
  - Horror
technicalTags:
  - Framework Injection
  - UEVR
  - VorpX
  - No Native VR
experienceTags:
  - Diorama Scale
  - Nordic Folklore
  - Side-Scrolling VR
  - Boss Scale
  - First-Person UEVR
tier: B
verdict: "Bramble: The Mountain King is genuinely worth playing in UEVR for VR enthusiasts who can tolerate a side-scrolling camera. The diorama-scale presence, full 6DOF head tracking, and striking stereoscopic art direction make it one of the more memorable UEVR showcases, and the creature encounters gain real scale. The side-scrolling camera and moderate motion-sickness risk are real caveats, but the experience justifies the setup for anyone curious about what a dark fairy-tale diorama feels like inside a headset."
heroImage: /images/games/bramble-the-mountain-king-vr-hero.jpg
sources: "Research conducted via the Bramble: The Mountain King Steam store page and system requirements, Maximum Entertainment press release, Dimfrost Studio Unreal Engine developer interview on 80.lv and Unreal Engine official site, VorpX community forum topic (June 2023 profile), Steam Community 'Working well in VR with praydog mod' discussion, UEVR GitHub repository and documentation, UEVR profiles/community coverage from Mixed-news and uevr-profiles.com, and gameplay/camera details from Gamepressure, GamingBolt, and Noisy Pixel reviews."
---

There is a type of VR experience that doesn't get talked about enough: the diorama. You are not inside the character's body. You are standing outside a living storybook, leaning in to watch a tiny boy run through a forest that feels real enough to touch. *Bramble: The Mountain King* is basically built for this. It's a 2.5D Nordic folklore platformer full of towering trees, glowing mushrooms, and creatures the size of houses. Drop it into UEVR and it becomes one of the prettiest diorama horror games you can play in a headset.

But "pretty" is not the same as "comfortable," and "works in VR" is not the same as "should be played in VR." Bramble in UEVR is a fascinating experiment that almost justifies itself. Almost.

## The Flat Game You're Starting With

Here's the thing: *Bramble* is not a first-person action game pretending to be a platformer. It's a side-scroller. You play Olle, a small boy whose sister gets kidnapped by a troll, and you run through a grim fairy-tale forest to get her back. The camera is mostly side-scrolling, with cinematic shifts during boss fights and puzzle set pieces. It is *Little Nightmares* by way of Swedish folklore: beautiful, short, occasionally brutal, and stubbornly two-dimensional even when it looks three-dimensional.

Dimfrost Studio built it in Unreal Engine. That single fact is why VR is even on the table. Without Unreal, there is no UEVR path. Full stop.

## Getting It Running: The UEVR Reality

Look, I'm not gonna lie: the first time I injected Bramble into UEVR, I expected a janky side-scroller that happened to render in 3D. What I got was closer to a living storybook with head tracking — and a camera that occasionally wanted to eject my lunch.

If you already have UEVR installed, budget about 20 to 30 minutes from "I want to play Bramble in VR" to "Olle is running around in my headset." That includes launching the UEVR injector, finding the Bramble process, picking OpenVR or OpenXR, injecting, and then spending five minutes fiddling with the default camera distance because it always starts too close or too far. If this is your first UEVR game, give it 45 minutes and at least one full restart. You will forget to disable something — Steam overlay, HDR, maybe a controller wrapper — and then wonder why the image flickers. I have absolutely been there. It is not hard by PCVR mod standards; it is also not plug-and-play.

UEVR is praydog's public beta that dropped in late 2023, and it works across the 1.x builds. It gives you full 6DOF head tracking, native stereoscopic 3D, and OpenVR/OpenXR support. The game renders through Unreal's own stereo pipeline, so the depth is real, not a VorpX-style post-process guess. By default you will play with a gamepad or keyboard in the headset, though some UEVR profiles allow limited motion control binding depending on how the game exposes its input.

### What About VorpX?

VorpX has a community profile for *Bramble* from June 2023, with roughly two replies and no detailed follow-up. In theory it hooks DX11 Unreal Engine titles and outputs geometry 3D. In practice, geometry 3D for Unreal games is often unstable, and there is almost no signal that this profile works well. I would not make it my first attempt. UEVR is the only path I would bet an evening on.

## Inside the Diorama: What UEVR Actually Does to Bramble

The first thing that hits you is scale. In flat mode, the giant trolls and twisted trees are impressive. In VR, they are *there*. The forest floor spreads out below you, the canopy towers overhead, and when a creature rears up it actually blocks your view. The art direction — moody greens, bioluminescent blues, scratchy Nordic textures — benefits enormously from depth and head tracking. This is the kind of world you want to lean into.

Holy shit, some of the boss encounters look genuinely stunning in stereoscopic 3D. A house-sized troll leaning into the frame is a completely different event when it is actually filling your peripheral vision. The game becomes a dark fairy-tale diorama, and for the first hour that is enough.

The second thing that hits you is the camera. *Bramble* is not a free-camera game. It is a side-scroller. UEVR lets you look around, but the action is still happening on a 2.5D plane that the designers control. You cannot walk behind the trees or peer around Olle. You are a floating observer hovering next to a beautiful puppet theater. That is not bad — it is genuinely cool — but it is not the same as being *inside* the game. Or at least, that is how it starts.

Here is where it gets interesting: UEVR can also push *Bramble* into first-person view. It is a UEVR-specific camera trick for some Unreal games, not an official game mode, and it is absolutely not perfect. Olle's animations are built for a side-scrolling silhouette, so when you drop the camera behind his eyes the climbing, cowering, and getting-swallowed motions look weirdly detached. Some interactions are clearly meant to be read from the side, and in first person they read as broken puppet theater.

But the presence is real. With first-person view plus 6DOF head tracking and semi-motion controls, the forest stops being a diorama you watch and becomes a fairy tale you are walking through. A glowing mushroom that looked charming at arm's length now looms overhead like a lantern. A troll that filled the side-view frame now fills your actual field of view. The camera still drifts and the platforming still happens on a rail, so you are not getting Skyrim — you are getting a guided walk through a dark storybook with your head inside it. There are jank moments, no question. I had times where the view clipped through Olle's own geometry or a scripted camera pull yanked my stomach sideways. But when it settles, the first-person mode adds a genuine "I am actually here" surprise that the third-person diorama view cannot quite match.

That first-person wrinkle is a big part of why I land on B-tier instead of C-tier. It does not turn *Bramble* into a native VR game, but it pushes it from "curiosity" to "worth playing." If you only try the default third-person camera, you are getting maybe seventy percent of what makes this one special.

The third thing is motion sickness. The camera drifts along a rail while your head stays still, then suddenly shifts angle for a cinematic moment, then locks into a boss-arena view. First-person mode makes the rail drift feel more intimate and, for me, slightly more nauseating during fast sequences. All of that movement is fine on a monitor. In VR it can mess with your vestibular system, especially during the faster platforming sequences. UEVR has comfort tools — snap turning, vignetting, render-method switching — but the game's design was never meant for a headset. If you are sensitive, this one will let you know, especially in first person. Keep sessions short and toggle back to third person when the camera gets aggressive.

## How Hard It Pushes Your PC

*Bramble* is not a heavy flat game. Minimum GPU is a GTX 570; recommended is a GTX 1660. But VR multiplies the load. UEVR runs native stereo, so you are effectively rendering the game twice. A budget-tier PC might hit playable framerates at modest settings, but you will want a mid-range rig or better if you want supersampling and stable ASW/SSW. Switching UEVR to Synchronized Sequential can fix flicker or crashes if the default Native Stereo misbehaves.

## Why It Almost Justifies Itself

What works: atmosphere, scale, art direction, creature encounters, and the sheer novelty of seeing a side-scrolling horror platformer in 3D. The boss fights in particular feel like set pieces you are standing inside rather than cutscenes you are watching.

What doesn't: free movement, motion controls, and long play sessions. This is still a game about running left and right while the camera decides where to look. The headset adds presence but cannot change the core design. If you are prone to motion sickness, the camera will remind you of that fact.

## The Bottom Line

UEVR turns *Bramble: The Mountain King* into one of the most atmospheric diorama experiences on PCVR. The world is gorgeous, the monsters feel huge, and the framework route is genuinely playable. The side-scrolling camera and side-scroller DNA keep it from feeling like a true VR native, but the diorama-scale presence and 6DOF head tracking add enough to make it worth playing rather than just worth knowing about.

If you already own the game and have UEVR installed, give it half an hour. If the camera doesn't make you reach for the headset, you are in for one of the more memorable UEVR showcases of the year. If you get queasy from moving cameras, you can still try it — keep sessions short and a fan pointed at your face — but know that the camera is the price of admission. This one is for flat-game fans and VR-curious tinkerers who can handle a little discomfort for a lot of atmosphere.
