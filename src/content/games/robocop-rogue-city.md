---
title: "RoboCop: Rogue City VR"
description: "RoboCop: Rogue City turns a flat UE5 shooter into one of the most physically satisfying VR showcases around — provided you're willing to wire up UEVR and a community profile."
flatReleaseDate: 2023-11-02
vrReleaseDate: 2025-02-14
lastUpdated: 2025-08-05
featured: false
routeType: Framework Only
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Stable but Quiet
genres:
  - First-Person Shooter
  - Action
technicalTags:
  - UEVR
  - Community VR Port
experienceTags:
  - Motion Controls
  - Destructible Environments
  - Story-Driven
  - Single-Player
tier: A
verdict: "RoboCop: Rogue City is one of the best reasons to fire up UEVR: full 6DOF motion controls let you be the cyborg, and Old Detroit has never felt this solid. The Lumen lighting bug and profile rough edges mean you'll tinker before you suit up, but the spectacle is worth it."
heroImage: /images/games/robocop-rogue-city-vr-hero.jpg
history:
  - date: 2025-08-05
    note: "jbusfield 'First Person Profile V1.03' released — full physical gesture set, working scoped-weapon optics, and subtitle fixes"
  - date: 2025-02-14
    note: "CYB3R-JUNKI3 'Robocop-Rogue-City-VR' v1.0 released — first 6DOF motion-controller UEVR profile with weapon attachment and camera-shake fixes"
sources: "Research compiled from the CYB3R-JUNKI3 and jbusfield UEVR profile repositories and READMEs, PCVR Central's RoboCop: Rogue City VR listing and Flat2VR Discord compatibility scrape, Praydog's UEVR repository and issue tracker (including issues #73 and #349), mark-mon's UEVR Index Controls plugin, YouTube VR coverage from Beardo Benjo, Headset-VR, Paradise Decay and others, Reddit threads on r/virtualreality and r/Robocop, and the Steam Community UEVR discussion. Assessment is based on documented profile behavior and community experience; no direct hands-on testing was performed."
---

I stood in the wreckage of Old Detroit, raised my right hand, and watched a thug's pistol spin off into the rubble before I'd even decided to disarm him. RoboCop: Rogue City was never built for VR — Teyon shipped a flat Unreal Engine 5 shooter in late 2023 with no headset mode in the plans. But the moment the community got Praydog's UEVR injector onto it, this turned into one of the clearest arguments I've seen for why motion controls beat a mouse: you don't aim RoboCop's Auto-9, you hold it.

## What RoboCop in VR means

There is no official VR version of this game and never was. No first-party mode, no port, no studio-built headset build. The VR you get is delivered by UEVR — the open framework that injects proper stereoscopic 6DOF into Unreal Engine titles — and then a community profile does the actual heavy lifting of turning a flat shooter into something you wear. Two separate profiles exist, both free, both maintained on GitHub and listed on PCVR Central, and both are built around full motion controllers rather than a gamepad held up to your face.

Out of the box, UEVR on this title leaves your gun "pivoting on a central point instead of true 6DOF," as early adopters found — the weapon floats in front of you and the flat arms look wrong. The profiles are what attach the Auto-9 to your right controller, hide the dead flat arms, and let you point the gun where your hand points. Without one, you don't have RoboCop in VR; you have a flat game awkwardly stretched across two eyes.

The Flat2VR community's own compatibility scrape tags this one "Works Well" with 6DOF motion controls, and more than one high-signal VR channel has filed it under the best UEVR games of its year. That's the top of the pile for a framework title.

## Getting up off that gurney

You are heavy. RoboCop doesn't run, doesn't sprint, doesn't parkour. He walks like a vending machine with a grudge, and that deliberate, grounded locomotion is the single best comfort decision the flat game made, because it keeps motion sickness low even during firefights — your inner ear never gets lied to.

Then you punch someone. With the right profile, a punch is a real swing of your gun hand, and when you grab a thrown chair, a pistol, or a suspect and fling them across the room with a thrust, the game stops feeling like a shooter and starts feeling like a power fantasy you're physically living. The Auto-9 sits in your right hand; you bring it up, you line up the dot, you fire, and the drywall behind your target genuinely explodes into debris. That destructibility is the soul of the flat game's tone, and in VR it reads as cause-and-effect in a way a monitor never sells.

The investigation sequences — scanning a crime scene, locking evidence, cross-referencing clues — become something closer to leaning over a real body and sweeping a scanner across the room. And the ED-209 boardroom standoff, the set-piece every RoboCop fan waits for, hits differently when the enraged robot looms over you at scale. This is the world worth inhabiting: the grimy, neon-soaked Old Detroit of the 1987 film, Peter Weller's Murphy voice intact, rendered with enough density that the headset stops being a screen and starts being a place.

## Where the chassis creaks

It is not a clean conversion, and anyone telling you otherwise hasn't hit the rough edges. Two bugs from the profile layer will find you. Pressing the left trigger when you aren't holding a weapon can crash the game until you disable the scan fix — a foul-up that'll bite a new player in the first ten minutes if they don't read the README. The HUD glues itself to your face during the Shady Meetup mission, so you're reading objectives on your eyeball. A few cut-scenes ship without subtitles because the profile strips the UI bars to kill black framing, which is a fair trade until a dialogue-heavy beat goes silent.

Then there's the engine-level problem, and this one isn't the mod's fault. RoboCop runs on Unreal Engine 5 with Lumen global illumination, and UEVR's own tracker has an open, unresolved bug for exactly this: Lumen flickers and lights each eye differently in a cluster of UE5 titles including this one. The workaround is to drop global illumination to Low or disable Lumen entirely — which costs you some of the moody neon glow that makes the flat game look expensive. You trade a little atmosphere for a stable image. Acceptable, but it's a tax you pay on every session.

Performance sits at the heavy end of the scale. This is a UE5 Lumen title being rendered twice for VR at headset resolution with the framework's own overhead on top. You want a high-end rig to hold 90Hz through a crowded firefight without reprojection dragging the image into mush. The spectacle is the point — chunks of wall peeling off, muzzle flashes filling the room — and you don't want that choking on a mid-range GPU.

## The motion-control divide

The two profiles aren't interchangeable, and the choice shapes your whole session. CYB3R-JUNKI3's v1.0 is the older, lighter build: weapon attached to the right controller, most camera shake stripped, aim tightened, crosshair reduced to a dot. It asks for UEVR 1.05 or a nightly build — and explicitly warns that two specific nightly builds crash. jbusfield's V1.03 is the more complete package: full six-degree motion controls, a ten-gesture physical move set where you heal by touching your off-hand to your mouth, reload by bringing your off-hand to the weapon, and drop into bullet-time by sweeping your hand to your temple, plus working scope optics you can zoom and adjust. If you want RoboCop to read your body, that's the profile. If you want the simplest path to "gun in hand, city to clean," the first one gets you there faster.

Neither is hard to install — PCVR Central rates it an easy install — but it is a three-part assembly: UEVR itself, the profile zip imported into the UEVR frontend for the RoboCop executable, and an optional Index-controller plugin if you're on Valve hardware. Misbehave and you delete one config folder and re-import. This is framework territory, and the people who hate tinkering will feel that immediately.

## Suit up, Murphy

RoboCop: Rogue City in VR is the rare framework title that earns a spot beside the native greats for the simple reason that the fantasy fits the hardware perfectly. You are a 400-pound cyborg; motion controls are the most honest way to be one. The profile scene is mature, the coverage is wide, and the moment you throw a suspect through a wall with a flick of your hand, the setup friction stops mattering.

It's not flawless — the Lumen bug, the occasional crash trigger, the missing subtitles, and the heavy hardware demand are all real. But they're the cost of admission to one of the best showcases UEVR has produced, and the game underneath is a better, denser, more characterful world than most VR-native shooters ever manage. If you already own a VR-ready PC and a copy of the game, this is an easy yes. If you're weighing whether the tinkering is worth it: suit up. Old Detroit has never felt this solid, and nobody modded this hard for a game that wasn't worth the trouble.
