---
title: "Atomic Heart VR"
description: "Mundfish's retro-Soviet shooter becomes a full-motion-controls VR experience through a UEVR plugin that puts the Polymer glove in your actual hand."
flatReleaseDate: 2023-02-21
vrReleaseDate: 2025-11-11
lastUpdated: 2025-12-21
featured: false
routeType: Native VR
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Action
  - Narrative
technicalTags:
  - UEVR
  - Motion Controls
  - Unreal Engine 4
experienceTags:
  - Full 6DOF
  - Physical Melee
  - Retro-Soviet Setting
  - Single-Player Campaign
tier: A
verdict: "A genuine showcase for what UEVR can do with a first-person shooter — full motion controls, physical melee, and a world worth standing inside — held back only by the setup tax and the rough edges any injection carries."
heroImage: /images/games/atomic-heart-vr-hero.jpg
history:
  - date: 2025-12-21
    note: "Ashok0 AtomicHeart-UEVR plugin reached v1.02, adding continued 6DOF motion-control refinements and DLC compatibility fixes."
sources: "Research compiled from the Ashok0 AtomicHeart-UEVR GitHub repository and release notes, the 77kdv77 Nexus Mods UEVR profile, PCVR Central's Atomic Heart VR guide, ReaperzVR's UEVR profile, YouTube VR coverage (Beardo Benjo, Paradise Decay, Headset-VR, MrSurviv0r), and r/UEVR community reports."
---

I didn't expect to fall for Atomic Heart in VR. Mundfish's retro-Soviet shooter launched flat in early 2023 to a messy, divisive reception — a gorgeous world, baffling pacing, a story that lost the thread somewhere around the midpoint. Two and a half years later, a community UEVR plugin showed up that turns the whole thing into a first-person, full-motion-controls experience. I spent a weekend inside it. Here's what actually happened.

This is one of the better UEVR conversions I've put on my headset. The Polymer glove sits in your left hand. The shotgun racks in your right. When you swing the glove to melee a robot, your real arm swings. That physicality is the entire reason to bother, and it lands.

## What the UEVR mod actually hands you

There is no official VR mode for Atomic Heart. Mundfish never shipped one, and the Steam page carries no VR support tag. What you get instead is a community-built layer on top of UEVR — the open-source Ashok0 AtomicHeart-UEVR plugin, with community profiles from 77kdv77 and ReaperzVR filling in configuration. You run the UEVR nightly injector against your Steam copy, import the profile, drop a couple of .pak files into the game's Paks folder, and launch.

What that gets you is real: 6DOF head tracking, motion-controlled weapons with adjusted positioning so they sit where your hands are, physical melee, aim-down-sights that actually align the barrel with your sight picture, and roomscale movement. The plugin also fixes things you'd never think about until they're broken — menu and cutscene camera angles, a volumetric cloud rendering bug, 3D audio, and the world map. It even supports the DLC areas. The crosshair is removed because your hands aim independently of your head now, which is exactly how it should be.

This is not a virtual screen with head tracking bolted on. It's the game rendered natively in stereo with your body in it.

## Holding the Polymer glove

Let me talk about the thing that sold me. In flat Atomic Heart, the Polymer glove is a magic-hand gimmick — you wave it at enemies and objects. In VR, it's a physical object in your left palm. You reach out, grab a hovering robot ball, and yank it. You swing it like a club. The Ashok0 plugin remaps glove activation to the left controller, so the moment you trigger it, your right hand's gun holsters and the glove takes over. That handoff feels deliberate, not janky.

The guns are the bigger win. Weapon positioning is corrected so muzzles don't float near your face, and ADS lines the projectile up with the sight. I spent an embarrassing amount of time just racking the shotgun and watching the shell eject in stereo. Small thing, but it felt great. Combat against the ballerina robots and the lab husks reads completely differently when you're physically ducking a swing and answering with a melee strike instead of mashing a button.

Comfort sits at moderate intensity — it's a smooth-locomotion roomscale shooter, and the plugin disables vignette by default, which removes one common aid for motion-sensitive players.

## Getting it running

Setup is the honest catch. This is an Advanced Setup burden, not a double-click. You need the UEVR nightly build, import the AtomicHeart-Win64-Shipping config, manually move .pak files into the Paks directory, then inject. If you own the DLC, there's an extra step: the Gold Midas glove reskin breaks the mod, so you have to switch back to the Standard glove. None of it is hard in the sense of being confusing — the README is clear — it takes 30 to 60 minutes and some tuning before you're standing in the Facility.

There's a softer on-ramp if you don't want to hand-place files. MrSurviv0r's VR HUB auto-inject video walks through a setup that handles most of the lifting for you. If you've run UEVR before, you'll be fine. If this is your first injection, budget an evening and keep the guide open in a browser tab on your monitor.

One note for the cautious: confirm the current profile version on the Flat2VR Discord before you start. These community profiles iterate, and a stale version is the difference between floating hands and a T-pose.

## The world is the point

Here's where Atomic Heart earns its place on a VR headset. Facility 3826 and the sprawling Soviet utopia-gone-wrong are dense, weird, and confidently designed. Standing in the central hub with robots gliding past, the architectural detail filling your peripheral vision, is the kind of presence flat screens flatten. The game's much-mocked art direction — the chubby red robots, the brutalist candy-colored interiors — reads as charming rather than try-hard when it's wrapped around your head.

The performance load is real. This is a Heavy Demand title on PC, and the UEVR injection adds overhead on top of an already hungry UE4 shooter. You'll want a high-end rig to hold 90Hz with the volumetric effects and crowd density the game throws at you. Drop the settings and you'll keep framerate, but the visual lavishness that makes the world worth inhabiting is exactly what costs you frames. That tension is the central trade of playing Atomic Heart in VR.
