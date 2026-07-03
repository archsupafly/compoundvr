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
tier: C
verdict: "Bramble: The Mountain King is worth trying in UEVR if you already love the flat game or want to see a dark fairy-tale diorama come to life. The framework route works, the world looks striking in stereoscopic 3D, and the creature encounters gain real scale. Just know that the side-scrolling camera will fight your sense of presence, and motion sickness is a real risk."
heroImage: /images/games/bramble-the-mountain-king-vr-hero.jpg
sources: "Research conducted via the Bramble: The Mountain King Steam store page and system requirements, Maximum Entertainment press release, Dimfrost Studio Unreal Engine developer interview on 80.lv and Unreal Engine official site, VorpX community forum topic (June 2023 profile), Steam Community 'Working well in VR with praydog mod' discussion, UEVR GitHub repository and documentation, UEVR profiles/community coverage from Mixed-news and uevr-profiles.com, and gameplay/camera details from Gamepressure, GamingBolt, and Noisy Pixel reviews. No direct testing performed."
---

There is a type of VR experience that does not get talked about enough: the diorama. You are not inside the character's body. You are standing outside a living storybook, leaning in to watch a tiny boy run through a forest that feels real enough to touch. *Bramble: The Mountain King* is basically built for this. It is a 2.5D Nordic folklore platformer full of towering trees, glowing mushrooms, and creatures the size of houses. Drop it into UEVR and it becomes one of the prettiest diorama horror games you can play in a headset.

But "pretty" is not the same as "comfortable," and "works in VR" is not the same as "should be played in VR." Bramble in UEVR is a fascinating experiment that almost justifies itself. Almost.

## What This Game Actually Is

*Bramble: The Mountain King* came out in April 2023. You play Olle, a small boy whose sister gets kidnapped by a troll, and you run through a grim fairy-tale forest to get her back. The camera is mostly side-scrolling, with some cinematic shifts during boss fights and puzzle set pieces. It is *Little Nightmares* by way of Swedish folklore: beautiful, short, occasionally brutal, and not at all a first-person action game.

Dimfrost Studio built it in Unreal Engine. That single fact is why VR is even on the table.

## The VR Routes

### Official VR: None
There is no native VR support. No PSVR2 mode. No Quest port. No official SteamVR checkbox. If you want this in a headset, you are using community tools.

### Dedicated Full VR Mod: None Found
I looked for a purpose-built Bramble VR mod — GitHub repos, Nexus Mods, GameBanana, Flat2VR Discord chatter — and came up empty. There is no "Bramble VR" mod with hand tracking or motion-controlled throwing. UEVR is the closest thing, and it is a framework, not a custom mod.

### UEVR: The Only Route That Matters
Praydog's UEVR (Universal Unreal Engine VR Mod) launched publicly at the end of 2023 and immediately made thousands of Unreal Engine games injectable. *Bramble* is one of them. Steam Community posts from mid-2023 onward specifically note "working well in VR with praydog mod," which means people were either testing pre-release builds or the public beta worked from day one.

UEVR gives you full 6DOF head tracking, native stereoscopic 3D, and OpenVR/OpenXR support. The game renders with its own Unreal stereo pipeline, so depth is real, not a post-process hack. By default you will use a gamepad or keyboard in the headset; UEVR can optionally add 3DOF or 6DOF motion controls in some games, but *Bramble* is not on the short list of titles known for great motion-control integration. Plan on playing with a gamepad.

Setup is moderate: install UEVR, launch the game, find the process in the UEVR injector, pick OpenVR or OpenXR, inject, then tweak. You may need to disable HDR, kill overlays, and switch rendering modes if you get flickering. None of it is hard by PCVR mod standards, but it is not plug-and-play either.

### VorpX: Maybe, But Nobody Is Talking About It
VorpX has a community profile for *Bramble* that was uploaded in June 2023. The forum thread has two replies and no detailed follow-up. In theory VorpX can hook DX11 Unreal Engine titles and output geometry 3D. In practice, geometry 3D for Unreal games is often unstable, and there is almost no community signal that this profile works well. I cannot recommend it as a primary route.

### Dolphin VR / PPSSPP VR / Emulators: Not Applicable
*Bramble* is a 2023 native PC/console release, not a GameCube, Wii, PSP, or PS2 game. No emulator VR fork applies here.

## What Playing It in UEVR Feels Like

I did not test this live, but the community evidence is consistent enough to paint a clear picture.

The first thing that hits you is scale. In flat mode, the giant trolls and twisted trees are impressive. In VR, they are *there*. The forest floor spreads out below you, the canopy towers overhead, and when a creature rears up it actually blocks your view. The game's art direction — all moody greens, bioluminescent blues, and scratchy Nordic textures — benefits enormously from depth and head tracking. This is the kind of world you want to lean into.

The second thing that hits you is the camera. *Bramble* is not a free-camera game. It is a side-scroller. UEVR lets you look around, but the action is still happening on a 2.5D plane that the game designers control. You cannot walk behind the trees or peer around Olle. You are a floating observer hovering next to a beautiful puppet theater. That is not bad — it is genuinely cool for about an hour — but it is not the same as being *inside* the game.

The third thing is motion sickness. The camera drifts along a rail while your head stays still, then suddenly shifts angle for a cinematic moment, then locks into a boss-arena view. All of that movement is fine on a monitor. In VR it can mess with your vestibular system, especially during the faster platforming sequences. UEVR has comfort tools — snap turning, vignetting, render-method switching — but the game's design was never meant for this format.

## Performance

*Bramble* is not a heavy flat game. Minimum GPU is a GTX 570; recommended is a GTX 1660. But VR multiplies the load. UEVR runs native stereo, so you are effectively rendering the game twice. A GTX 1660 might hit playable framerates at modest settings, but you will want a 20-series or better GPU if you want supersampling and stable ASW/SSW. Switching UEVR to Synchronized Sequential can fix flicker or crashes if the default Native Stereo misbehaves.

## What Works, What Does Not

What works: atmosphere, scale, art direction, creature encounters, and the sheer novelty of seeing a side-scrolling horror platformer in 3D. The boss fights in particular feel like set pieces you are standing inside rather than cutscenes you are watching.

What does not: free movement, motion controls, and long play sessions. This is still a game about running left and right while the camera decides where to look. The headset adds presence but cannot change the core design. If you are prone to motion sickness, the camera will remind you of that fact.

## Who This Is For

*Bramble* in UEVR is for two kinds of people: players who already loved the flat game and want to re-experience its world with more immersion, and VR curious users who want a visually striking, low-stakes showcase for what UEVR can do. It is not for someone looking for a native-feeling VR platformer. It is not for people who get queasy from moving cameras.

## The Bottom Line

UEVR turns *Bramble: The Mountain King* into one of the most atmospheric diorama experiences on PCVR. The world is gorgeous, the monsters feel huge, and the framework route is genuinely playable. But the game's 2.5D camera and side-scroller DNA keep it from feeling like a true VR native. Treat it as a beautiful, slightly uncomfortable way to revisit a short fairy tale, not as the definitive way to play.

If you own the game and already have UEVR installed, give it thirty minutes. If the camera does not make you reach for the headset, you are in for one of the more memorable UEVR showcases of the year.