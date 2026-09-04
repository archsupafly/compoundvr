---
title: "Perfect Dark VR"
description: "The N64 decompilation project gets a full VR port — and after a furious summer of releases, it's shaping into something genuinely worth your time."
flatReleaseDate: 2000-08-28
vrReleaseDate: 2026-06-30
lastVerified: 2026-06-30
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Action
technicalTags:
  - N64 Decompilation
  - Community VR Port
  - Open Source
experienceTags:
  - Classic FPS Revival
  - Motion Controls
  - Stealth Action
tier: B
verdict: "A legitimately good VR port of a legitimately good game, held back by beta-tier jank that's clearly being worked through release by release."
heroImage: /images/games/perfect-dark-vr-hero.jpg
sources: "Research via Alex-LeTux/perfect_dark_VR GitHub repository, GitHub API release verification (v1.0-beta through v1.7.1-beta), community reports and release notes, YouTube gameplay footage. No direct testing performed."
---

The first time you pick up the Falcon 2 in VR and feel the weight of a proper dual-wield setup — Magsec 4 in one hand, assault rifle in the other — you realize someone actually cared about this. Perfect Dark in VR isn't a quick VorpX profile bolted onto an N64 emulator. It's a full community port built on the n64decomp/perfect_dark decompilation, complete with motion controls, hand presence, and enough ambition to ship eleven builds in under two months.

That ambition is both the reason this works and the reason it's still rough around the edges.

## What You're Actually Getting

Alex-LeTux's perfect_dark_VR is a Full VR Mod — not an emulator profile, not a framework wrapper, not stereoscopic injection. It's a native VR port reconstructed from the ground-up N64 decompilation, rebuilt with 6DOF head tracking, motion controls, and per-eye rendering that gives you actual stereo depth in a world that was designed for a flat TV.

The mod supports both PCVR (via SteamVR) and Quest standalone. That dual-platform story is important: the Quest version runs natively without a PC, which means you can take this to a friend's house with just a headset. The PCVR version gives you more headroom for visual quality and the ability to push HD texture packs when you want them.

What you don't get: VR-specific comfort options, a polished VR UI, or anything resembling the polish of a native VR release. The menus are flat panels floating in space. Locomotion is standard snap-turn and smooth-move without vignette options. This is a community project — it plays like one, for better and worse.

## The N64 Agent, Rebuilt in 3D

Perfect Dark's campaign was always Rare at their most ambitious — espionage set pieces, an alien conspiracy that escalates from corporate infiltration to full-scale invasion, and an arsenal of gadgets that gave the game its identity. The laptop gun that unfolds into an autonomous turret. The Magsec 4. The Farsight XR-20, a rifle that lets you see through walls and shoot people in the next room.

In VR, that arsenal transforms. The laptop gun deploying into a turret while you crouch behind cover isn't a button press anymore — you're reaching down, planting it, watching it unfold. Dual-wielding in Perfect Dark was already a signature mechanic, and doing it with two actual controllers makes the gunplay feel properly kinetic. You're not selecting a weapon from a radial menu; you're physically grabbing what you need.

The level design holds up better than it has any right to. N64-era corridors and arenas are tight, linear, and purpose-built — which means they work well in VR where open-world sprawl can cause discomfort. The dark, industrial interiors of dataDyne and the shadowy government facilities feel claustrophobic in the right way. You're somewhere, and the architecture tells you something about where you are.

Combat is the main event. The remapped controls put you behind the sights of each weapon with motion-tracked aiming, and the Falcon 2's fan-fire pattern feels satisfying when you're pulling the trigger with your own hand. The Farsight's X-ray visor is particularly effective in VR — peering through a sniper scope that shows enemies through walls while standing in a physical stance creates a tension that the flat version never quite matched.

## What's Working

The development pace is remarkable. Ten updates since the June 30 beta launch — including gesture fixes, throwing mechanics, per-eye culling corrections, HD texture pack support, and a Quest crash fix — means the mod is actively being refined. Version 1.6 fixed motion-gesture direction for throwing and melee, added rumble feedback to both hands on two-handed weapons, and corrected per-eye view frustums so full-screen effects actually cover both eyes. Version 1.7 added support for HD texture packs ported from the Perfect Dark PC port project, a proper VR pause environment, and fixed weapon and hand disappearance bugs. Version 1.7.1 squashed a Quest launch crash and an antivirus false positive.

That's not an abandoned project. That's someone who plays their own mod and fixes what breaks.

The core VR implementation is solid where it counts: 6DOF tracking works cleanly, weapon aiming feels natural, and the stereo rendering gives the N64 geometry real depth. The decompilation foundation means the mod runs with native performance characteristics rather than emulation overhead — a mid-range PC pushes this without breaking a sweat, and the Quest version runs standalone at acceptable frame rates.

## Where It's Still Rough

It's a beta. That word does a lot of work here.

The VR pause environment was added in 1.7 because pausing the game previously dropped you into a void. Weapon and hands disappearing mid-firefight was a known issue that took multiple releases to address. The throwing gesture direction was backwards at launch. These aren't nitpicks — they're the kind of bugs that break immersion mid-mission, and they were all present in the initial release.

There's no VR comfort layer. No snap-turn vignette, no smooth locomotion tunneling, no seated/standing toggle that actually adjusts the camera rig. If you're sensitive to locomotion discomfort, you're relying on whatever your headset's built-in comfort settings provide. The mod doesn't hold your hand.

The menus and UI are functional but unadapted. You're looking at flat N64-era interface panels in 3D space. They work — you can navigate them with motion controllers — but there's no VR-native redesign. It's fine for a beta. It's not where you'd want it to stay.

Multiplayer support status is unclear. The original game's Combat Simulator and co-op modes were a significant part of its appeal, but the VR mod's focus has been on single-player campaign and training missions. If you're here for the multiplayer, you may not find what you're looking for.

## The Development Story

What's genuinely impressive is the velocity. Beta 1.0 shipped June 30th. By mid-August, the mod had shipped eleven builds addressing gesture mechanics, per-eye rendering, texture loading, platform-specific crashes, and visual consistency. The GitHub repo sits at 146 stars — modest by mainstream standards, but active for a niche VR port of a 26-year-old N64 game.

The progression tells a story: early releases fixed fundamental control problems. Middle releases addressed rendering and comfort. Recent releases are adding features — HD texture support, a VR pause space. That's the trajectory of a project moving from "does it work" to "does it work well," which is exactly where you want a beta to be heading.

The external HD texture pack support is a meaningful quality bump. The original N64 textures, even when rendered in stereo, look like what they are: low-resolution assets designed for a CRT. The ported HD textures give the world detail that makes the VR presence feel earned rather than nostalgic.

## Who This Is For

If you played Perfect Dark on N64 and wondered what thedataDyne headquarters would feel like with your actual eyes inside it, this delivers on that curiosity with motion controls and stereo depth. If you're looking for a polished, comfort-option-rich VR shooter, this isn't it yet — but it's clearly heading that direction.

The active development cadence means the experience you have today won't be the experience you have next month. That's both the appeal and the caveat: you're buying into a project that's still becoming itself.

For a B-tier mod of a game this well-designed, the core experience is solid enough to recommend — with the understanding that you're playing a beta that's improving at an impressive pace.
