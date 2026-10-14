---
title: "Halo: Combat Evolved VR"
description: "The original Halo, rebuilt for VR by a community mod: motion-controlled weapons, working scopes, shoulder holsters, and the ringworld looming around you."
lastUpdated: 2026-01-10
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - First-Person Shooter
  - Sci-Fi
technicalTags:
  - Full VR Mod
  - 6DoF
  - Motion Controls
  - Community Mod
experienceTags:
  - campaign
  - classic-game
  - nostalgic
tier: A
history:
  - date: 2026-01-10
    note: HaloCEVR 1.4.0 released, the mod's latest update.
  - date: 2024-11-26
    note: HaloCEVR 1.0.0 released — the first full VR conversion for the original PC edition.
verdict: "HaloCEVR is the real thing: a full conversion of the original Halo for motion-controlled PCVR. It has rough edges, but the campaign is playable, the shooting feels native, and this is now the way to experience the ringworld in a headset."
heroImage: /images/games/halo-combat-evolved-vr-hero.jpg
flatReleaseDate: 2001-11-15
vrReleaseDate: 2024-11-26
modDownload:
  url: https://github.com/LivingFray/HaloCEVR/releases
  label: Download Halo CE VR Mod
  note: Created by LivingFray
sources: "Research conducted via the HaloCEVR GitHub repository by LivingFray (github.com/LivingFray/HaloCEVR), including release notes, documented features, and the known-issues list; the HALOCEVR-Installer by EllieWasteland; Flat2VR Discord community reports; and YouTube VR gameplay footage from established channels."
---

# Halo: Combat Evolved in VR: The Ring at Arm's Length

The first time you physically raise an MA5B assault rifle and the floating crosshair tracks with your hand, Halo stops being a game you remember and becomes a place you are standing inside. HaloCEVR is a full conversion of the original 2003 PC release for PCVR, and it finally puts your hands on the weapons, your eyes down the scopes, and your body behind the cover.

## What HaloCEVR actually gives you

HaloCEVR, by LivingFray, is a community-built full VR mod for the original Halo: Combat Evolved on PC. It is **not compatible with The Master Chief Collection** and it is not for the Custom Edition fork; the install targets the original 2003 PC release, patched to 1.0.10. The mod is actively maintained — 1.0.0 in late 2024 through 1.4.0 in early 2026 — and it turns a twenty-year-old shooter into a tracked, room-scale experience.

What the mod gives you:

- **Full 6DoF stereo view** with independent tracked hands
- **6DoF weapon and grenade aiming** — point and fire, arc a frag with your arm
- **Functional picture-in-picture scopes** on weapons that use them, plus a two-handed aiming mode
- **Motion melee, motion crouch, and a tap-the-head flashlight**
- **Shoulder weapon holsters** and the ability to swap weapons between hands
- **A detached floating UI layer** in 3D space
- **Joystick-steered vehicles** and a desktop mirror
- **Rebindable controls**, including a left-handed preset

This is not a gamepad game mapped to a headset. It is a conversion with presence, hand tracking, and interaction design that respects the fantasy Halo always implied.

## The rifle in your hands

**Controls:** Full motion controls. One hand for the rifle, the other for grenades, melee bound to a swing, crouch to a physical duck, flashlight to a tap at your temple. The shoulder holsters let you stash a secondary weapon and pull it from your body — a gimmick until you are mid-fight on the Pillar of Autumn and realize you planned the reload around where your shotgun lives. Two-handed aiming tightens precision weapons, and the PiP scopes magnify the world instead of faking a zoomed render.

**Comfort:** Moderate intensity. Halo was never designed for head-mounted locomotion, and the campaign still throws you into Warthog runs, narrow corridors, and elevator sequences where the camera has opinions of its own. Tune teleport or smooth-turn comfort settings in. The vehicle sections in particular deserve respect — the first time the Warthog fishtails across a canyon while your real body stays still is a test of equilibrium.

**Performance:** Efficient — the underlying game is lightweight — but motion smoothing can get aggressive in vehicles when the mod stutters, and that reprojection is visible and jarring. A budget-to-mid-range PC is enough for the campaign; the issue is less GPU headroom and more frame-pacing consistency during fast camera motion.

**Stability:** Mostly solid, with documented friction points. The game can launch unfocused, breaking input or sound until you click back onto it. The tutorial's "look around" step sometimes needs a mouse wiggle to register head movement. Reloading a checkpoint saved inside a vehicle can leave the camera displaced. These are not showstoppers; they are quirks you learn to route around within the first hour.

## The Fantasy, Delivered

This is the part that matters. Popping a Grunt with a pistol snap-shot because you actually aimed the controller. Arcing a plasma grenade over cover and hearing the stick-sizzle from the other side. Ducking behind a Forerunner pillar and feeling the geometry around your shoulders. The assault rifle's floating reticle follows your hand, the shotgun reloads with a press, and the sniper rifle's scope brings the ringworld into sharp, magnified focus. Looking down reveals armor rather than a missing body, which is exactly what a Halo game should do.

The campaign holds up. The AI still flanks, the shield dance still works, and the two-weapon limit still forces hard decisions. VR does not fix the occasional repetitive corridor, but it makes the quiet moments — the ring stretching overhead, the flood dripping from vents, the first Banshee silhouetted against the sky — land with real spatial weight. The mod did not rewrite the game. It gave you a body inside it.

## The Honest Caveats

No conversion this deep is clean. The documented issues are real, and they will affect your first session.

- **Install location matters.** Under Program Files, the mod's config file cannot write properly. Move the install out first.
- **On-screen prompts still show keyboard bindings.** The UI has not been taught otherwise. You learn the VR bindings quickly, but the prompts are a constant small lie.
- **Melee and interact use head-aiming.** You swing the controller, but the target is determined by where you are looking, not where your hand goes. It works; it does not always feel intuitive.
- **Vehicles are moody.** Entering and exiting can leave the camera at odd angles, and checkpoint reloads from inside a vehicle sometimes displace your view. Save before the big Warthog push.
- **The tutorial is finicky.** That "look around" step is a known trap; a tiny mouse movement clears it.
- **Stutters trigger motion smoothing.** In vehicles especially, a dropped frame becomes a smeared judder. Lock the framerate and keep settings conservative if you are sensitive.

These are mod rough edges, not fundamental flaws. They are the price of turning a 2003 PC shooter into a native-feeling VR campaign, and they are manageable after the first hour.

## Getting It Running

There are two paths. The easier one is the HALOCEVR-Installer by EllieWasteland, which handles much of the placement and patching automatically. The manual path needs a copy of Halo: Combat Evolved for PC, the 1.0.10 patch, the mod's own files, and the optional Chimera mod. Either way, the game must live outside Program Files, and you need a headset running SteamVR or OpenXR on a PC. There is no Quest standalone or console route. This is PCVR only.

If you loved Halo and own a PCVR headset, this is now the way to play the campaign — and if you only know the game from MCC, the original PC release is a small extra purchase that earns its keep. Start with short sessions and stay conservative in vehicles if you are prone to motion sickness.

---

This is not a perfect port. It is a full VR conversion of a twenty-year-old game, and it occasionally reminds you with a displaced camera or a keyboard prompt. But when you are crouched behind a rock on Installation 04, physically raising a pistol over the top to pick off an Elite, the imperfections stop mattering. The ring is real, the weapons are in your hands, and Halo finally feels like the science-fiction combat simulator it always wanted to be.
