---
title: "Grand Theft Auto IV VR"
description: "A free community mod finally drops you inside Liberty City with tracked hands, physical guns, and your grip on the steering wheel — but it's a month-old work in progress, and it shows."
flatReleaseDate: 2008-04-29
vrReleaseDate: 2026-10-10
lastUpdated: 2026-11-09
history:
  - date: 2026-11-09
    note: "GTA4VR reaches v0.6.0, its twelfth release in the mod's first month of development"
featured: false
routeType: Native VR
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Inconsistent / Unpredictable
supportStatus: Active
genres:
  - Action
  - Open World
  - Shooter
technicalTags:
  - Full VR Mod
  - OpenXR
  - 6DOF
  - Motion Controls
experienceTags:
  - Open World
  - First-Person
  - Driving
  - Physical Interaction
tier: A
verdict: "GTA4VR puts you inside one of the best open worlds ever made with real tracked hands and physical driving — a genuine transformation let down only by its age as a month-old work in progress. If you already own GTA IV on PC and you like tinkering, this is the most alive Liberty City has ever felt."
heroImage: /images/games/grand-theft-auto-iv-vr-hero.jpg
modDownload:
  url: "https://github.com/bordplate/GTA4VR/releases/latest"
  label: "Download Grand Theft Auto IV VR Mod"
  note: "Created by bordplate"
sources: "GitHub repository and release history for bordplate/GTA4VR; pcvrcentral GTA IV conversion pages; VRMods-List directory entry; YouTube VR coverage (NotAGameAddict, VRified Games, FastLawyer, Uruzz, StoniVR and others); VorpX supported-games documentation and a community-compiled VorpX game list. Assessment based on the documented feature set, the author's README, and creator gameplay footage rather than direct hands-on testing."
---

For the better part of two decades, the only way to "be" Niko Bellic was to watch him from a camera floating over his shoulder. Last month that finally changed. A free community mod called GTA4VR drops you directly into Liberty City — head tracking, tracked hands, and a steering wheel you actually grip — and it is the closest this game has ever come to feeling like a place you inhabit instead of a cutscene you watch.

## What GTA4VR actually is

GTA4VR is a community-made conversion of Grand Theft Auto IV: The Complete Edition on PC, built by a modder who goes by bordplate and first published in mid-October. This is not an injection trick that paints the flat game onto a virtual screen. It renders true per-eye stereo, tracks your head in six degrees of freedom, and reconstructs Niko's arms and hands from your controllers so you reach, grab, reload, and steer with your own body.

The mod is built on FusionFix, the standard modern patch that cleans up GTA IV's ancient DirectX 9 problems and runs it cleanly through DXVK and Vulkan. The clever part is that bordplate bundles the whole foundation — FusionFix, the ASI loader, DXVK, and the OpenXR loader — into a single zip you drop into the game folder. You do not chase a dependency chain. You need a 32-bit-capable OpenXR runtime (SteamVR is the developer's tested reference) and a legitimate copy of the Complete Edition, and then you launch the game like you always have.

One honesty note the author puts right at the top of the readme: the code is, in his words, entirely AI-generated — he directed it, he did not write it. I'm not going to pretend that does not matter for long-term maintainability, but it also has not stopped the thing from shipping a dozen builds in its first month, each one adding real features. The feature list reads like a wishlist someone actually fulfilled: physical weapons with manual reloads and diegetic ammo counters, a pump shotgun you have to pump between shots, sniper scopes that magnify inside the lens, grab-able car doors and trunks, ragdoll NPCs you can haul around, and a wrist radar that shows your health, armor, and wanted stars without yanking you out of the world.

## Driving, shooting, and opening doors with your hands

Here is what actually sold me. I walked up to a parked sedan, grabbed the door handle, pulled it open, slid in, and wrapped both hands around a steering wheel that rotates as I rotate my controllers. The dashboard shows its own radar. I pulled out onto the Algonquin expressway with my left hand on the wheel and my right hand out the window for a drive-by, and the city scrolled past in proper stereoscopic depth. No flat replay gives you that. That is the reason a headset earns its shelf space.

On foot it holds up just as well. Locomotion is head-relative thumbstick movement with jogging, sprinting, jumping, and physical crouching — and because snap and continuous turning are both options, the walking never has to fight your stomach. Combat is where the mod stops pretending to be a flat port. Pistols and SMGs sit in your hands with two-handed aim and real recoil. The pump shotgun makes you rack the slide. Grenades and Molotovs are physically wound up and thrown. Melee is tracked punches and bat swings. You grab props, you yank open car hoods, you drag a limp NPC by the arm. ## The honest catch: this is a month-old build

I am not going to dress this up. GTA4VR is thirty days old and it shows. As of the latest build, the author has not verified a full VR-only playthrough, and the README is blunt about what breaks. The bowling minigame in the Michelle mission can't be played through VR controls — you enter and immediately back out to progress. A cinder block in one tutorial can't be picked up, so you smash a window with your fist instead. Some native pickup interactions simply don't register, and a handful of story missions may force you to either drop to keyboard and mouse or temporarily disable VR to get past a section. The two DLC episodes, The Lost and Damned and The Ballad of Gay Tony, have not been tested at all.

None of that stopped me from stealing cars and causing chaos for an hour straight, but it does mean this is a mod for someone who reads the README first and keeps a gamepad within arm's reach. There's a flat-screen bail-out built in: flip one INI line, relaunch, and the game runs like the flat version it always was. That escape hatch is the difference between a frustrating blocker and a five-second detour.

## Performance is the real variable

The README refuses to promise a steady 90 FPS, and it is right to refuse. Liberty City's dense skyline and traffic are a heavy load for the DXVK path, and busy intersections can drop below the headset's refresh rate. You want a high-end PC to push this cleanly — a mid-range rig will run it, but you'll be leaning on reprojection in the thick of downtown. The developer tested only a Vive Pro at 90 Hz with Vive Wands; every other headset and controller combination is officially "plausible, not tested." In practice the Quest 3 over PC streaming has become a common way people are running it, and creator footage of that setup looks solid, but treat your own hardware as unverified until you try it.

Before GTA4VR existed, the only way to see GTA IV in a headset was VorpX injection — the flat game on a floating screen with head-tracked look and zero hand presence. It still works as a no-mod fallback, but it is a different experience entirely and not one I'd point you to first.

## Why it still lands as a recommended experience
