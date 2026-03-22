---
title: "Garry's Mod VR"
description: "A community-made VR mod transforms the physics sandbox into a full VR experience with motion controls, but rough edges and addon conflicts mean it's best for enthusiasts willing to tinker."
lastVerified: 2026-03-20
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Enthusiasts/Tinkerers Only
playability: Mostly Playable
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Highly Variable
performance: Heavy Demand
supportStatus: Active
genres:
  - Sandbox
  - Physics
  - Multiplayer
technicalTags:
  - Source Engine
  - SteamVR
  - Steam Workshop
  - Module Installation Required
experienceTags:
  - Creative Building
  - Multiplayer
  - Experimental
  - Community Content
tier: B-
verdict: "Garry's Mod's massive sandbox and endless workshop content become surprisingly playable in VR, but the mod requires patience, troubleshooting, and realistic expectations about stability and compatibility."
---

# Garry's Mod in VR: The Physics Sandbox, Unleashed — With Caveats

Garry's Mod exists as a platform more than a game. It's a physics sandbox with nearly two decades of community content — game modes, weapons, vehicles, maps, and experiments piled on top of the Source engine. When VRMod arrived, it didn't just add VR support to GMod. It attempted to make the entire platform work in head-mounted displays with motion controls. The ambition is enormous. The execution is impressive. The stability is experimental.

This is a mod that works — but only if you're willing to troubleshoot, accept rough edges, and accept that some of GMod's vast library simply won't cooperate.

## What This VR Route Actually Is

VRMod is a community-made modification that adds full VR support to Garry's Mod through SteamVR. It's not official support, not a publisher-backed port, and not a polished product. The original creator, Catse, released it in March 2019 with explicit warnings: this is unfinished, experimental, and comes with bugs, bad performance, and potential crashes. Don't buy VR or GMod just for this.

Since then, the ecosystem has grown. The original VRMod still exists but is no longer actively maintained. A semi-official fork by Pescorr added melee systems, weapon handling improvements, and resumed active development. The most stable and feature-rich version is now VRMod x64 Extended, maintained by Abyss_c0re, which targets GMod's x64 branch, adds Linux support, and integrates features from various community forks into a single package.

All three require installing a binary module plus subscribing to a Steam Workshop addon. This is not a one-click experience.

## How It Plays

### Motion Controls and Interaction

VRMod provides full motion control support for all major SteamVR controller types: Vive wands, Index controllers, Oculus Touch, and Windows Mixed Reality controllers. Your virtual hands can pick up props, manipulate the physics gun, fire weapons, and interact with the world.

The mod includes a holster system for storing items on your body, melee combat with velocity-scaled damage, and proper two-handed weapon grip for rifles and heavier equipment. The physics gun — GMod's signature tool — works in VR with motion-controlled rotation and positioning, similar to the official Half-Life 2 VR implementation.

Hand collisions exist. You can physically grab objects, throw them, and interact with buttons in the world. The x64 Extended version improves hand physics significantly, eliminating the phantom prop sounds that plagued earlier builds.

### Locomotion and Comfort

VRMod supports four locomotion modes: right-hand, left-hand, HMD-directed, and legacy. There's seated mode support for players who prefer playing from a chair. The experience is highly variable — some maps and game modes feel comfortable, others induce motion sickness rapidly depending on locomotion choices and frame rate.

Full body tracking works with Vive trackers, though the x64 Extended developer notes FBT support is limited and unpolished due to lack of testing hardware. Eye and lip tracking support exists through SRanipal integration for Vive Pro users, though this is advanced configuration.

### Performance

This is where expectations need calibration. GMod's Source engine was never designed for VR. The game renders twice, once per eye, with all the physics and entity calculation that makes GMod CPU-intensive even on desktop. The original developer recommends achieving over 400 fps on desktop before expecting smooth VR performance in the same scenario.

Performance is CPU-bound. High-end GPUs help, but not as much as you'd expect. The x64 Extended fork optimizes the codebase for lower latency and fixes some rendering issues, but the fundamental constraint remains: GMod in VR is demanding and inconsistent.

The recommended settings include:
- Running GMod windowed at lower desktop resolution
- Disabling VSync, motion blur, and reducing shadow quality
- Capping FPS to your headset's refresh rate (or double it)
- Avoiding maps with heavy foliage and complex geometry

Linux support exists in the x64 Extended version, but requires additional setup scripts and only works with ALVR for wireless streaming.

## What Works Well

The core sandbox experience translates to VR impressively well. Spawning props, building contraptions, and experimenting with physics all feel natural. The physics gun in particular gains new life when you can reach into the world and manipulate objects directly. Vehicle support has improved significantly — you can drive while gripping the wheel motion-controlled, and even fire weapons from inside vehicles.

The x64 Extended version's overhaul of the pickup system adds visual halos, server-side weight limits, and NPC interaction. Melee combat with velocity-scaled damage makes hitting things feel satisfying rather than floaty. Shooting mechanics work across a wide variety of community weapons, with dedicated VR-compatible weapon packs available on the Workshop.

Multiplayer works. Other players on a server don't need VR — only the server needs the addon. This means VR players can join existing GMod communities, though competitive servers may not appreciate the potential for instability or unfair advantages.

## What Doesn't Work

### Addon Conflicts

GMod's greatest strength becomes VRMod's biggest weakness. The game hosts an enormous Workshop ecosystem — weapons, player models, post-processing effects, game modes, and utilities accumulated over years. Many conflict with VRMod.

The x64 Extended documentation explicitly warns:
- Post-processing addons like ReShade and GShaderLibrary break rendering
- Animation-altering addons cause issues
- Collision-modifying addons create problems
- Non-standard player models may not work correctly

The recommended approach is starting with a clean GMod installation and adding addons slowly, testing for conflicts. This is the opposite of how most people play GMod, which is with hundreds of Workshop subscriptions accumulated over years.

### Stability

The experimental label is accurate. Crashes happen. Some players report issues that mysteriously fix themselves. Others can't get VR working at all. The original VRMod developer notes it "may not even work for some people."

The x64 Extended version is more stable, but still warns that the developer prioritizes adding features over maintaining perfect stability. If you need something reliable, you're in the wrong place.

### Game Mode Compatibility

Sandbox works — that's the primary focus. But GMod's appeal extends to countless community game modes, and VR compatibility varies wildly:

- **Trouble in Terrorist Town (TTT):** A dedicated addon, TTT VR, provides compatibility through UI ports, VR weapon replacements, and HUD adaptations. It works, but requires setup and has limitations with certain weapons.
- **Prop Hunt:** No dedicated VR support. The prop disguising mechanic doesn't translate cleanly to VR interaction.
- **DarkRP and roleplay modes:** No documented VR-specific support. Complex UI and custom interactions may not work correctly.
- **Half-Life 2 maps:** You can load them, but the mod isn't designed for this experience. It's possible, not polished.

If your interest in GMod centers on specific game modes, research whether VR-compatible versions exist before assuming they'll work.

### Setup Friction

This is not "subscribe and play." The installation process requires:

1. Subscribing to the Workshop addon
2. Downloading and installing a binary module (files placed in correct directories)
3. Disabling SteamVR Desktop Game Theater in Steam settings
4. Disabling other addons or clearing addon subscriptions entirely
5. Removing launch options
6. Starting in Sandbox mode, single player
7. Using console commands to activate VR

The x64 Extended version adds another step: switching GMod to the x64 branch, which some players may not even know exists.

Mistakes in any step produce errors like "module not installed" or crashes when entering VR. The troubleshooting process is documented but assumes willingness to dig through configuration.

## Who This Is For

**Good for:**
- GMod enthusiasts who already own the game and want to experience their favorite sandbox in VR
- Players willing to troubleshoot, accept crashes, and configure settings
- Creative builders who primarily use GMod for physics experiments and construction
- VR enthusiasts interested in the novelty of an entire modding platform in head-mounted display

**Not for:**
- Players expecting a polished, stable VR experience comparable to native VR games
- Competitive multiplayer (the original developer explicitly warns against PVP servers)
- Casual VR users who want something that "just works"
- Those attached to heavy Workshop addon collections — conflicts are common

## The Verdict

**Tier: B-**

**Game Quality: A-**
Garry's Mod is a platform for creativity. The physics sandbox, combined with nearly unlimited community content, offers endless replayability. It's one of the most player-driven games ever made — a toolset for experiments, games, and nonsense that has sustained a community for nearly two decades.

**VR Implementation Quality: C+**
The implementation is impressive for community-made work. Full motion controls, hand physics, holster systems, melee combat, vehicle support, and multiplayer compatibility represent enormous effort. But it remains experimental. Performance is demanding, crashes occur, addon conflicts are endemic, and setup requires technical comfort. The "experimental" label in the mod's name is accurate and honest.

**Overall Tier: B-**
GMod in VR works better than it has any right to. But it works because dedicated community members put in hundreds of hours optimizing and maintaining something the original developer stepped away from. The result is a functional VR sandbox that lets you reach into GMod's physics playground — if you're willing to tolerate friction, troubleshoot conflicts, and accept that "experimental" is not underselling it. For enthusiasts and tinkerers, it's worth the effort. For everyone else, it's a fascinating proof of concept with rough edges that never quite smooth out.

---

## Source Log

- Original VRMod Steam Workshop page (id: 1678408548) — developer warnings, setup instructions, controller bindings
- VRMod Semi-Official Fork (id: 2780083257) — Pescorr's maintained fork with melee and weapon improvements
- VRMod x64 Extended Steam Workshop page (id: 3442302711) — Abyss_c0re's optimized all-in-one package
- GitHub: Abyss-c0re/vrmod-x64 — technical documentation, feature list, installation requirements
- TTT VR Workshop page (id: 2129490712) — game mode compatibility addon for TTT
- GMod Fandom Wiki — VRMod article for version comparison and historical context