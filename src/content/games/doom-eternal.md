---
title: "Doom Eternal VR"
description: "KHARVOX: ARGENT turns Doom Eternal into a native Vulkan VR conversion with full motion controls, two-hand gunstock support, and snap turning — a dramatic leap from the old injection-driver curiosity it once was."
flatReleaseDate: 2020-03-20
vrReleaseDate: 2020-04-01
lastUpdated: 2026-09-29
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Action
technicalTags:
  - Vulkan
  - Stereoscopic 3D
  - Head Tracking
  - Full Motion Controls
  - 6DOF
experienceTags:
  - Fast-Paced
  - Visually Impressive
  - High Intensity
  - Hand-Based Aiming
tier: A
verdict: "KHARVOX: ARGENT finally gives Doom Eternal the VR conversion it needed: native Vulkan, full motion controls, snap turning, and off-hand-directed movement. The base game is still a landmark shooter, and the mod is genuinely playable — but limited resources, AMD rendering issues, water artifacts, and experimental DLSS/PSVR2 features keep the recommendation caveated."
heroImage: /images/games/doom-eternal-hero.jpg
modDownload:
  url: "https://github.com/CactusVRStudios/KHARVOX-ARGENT"
  label: "Download Doom Eternal VR Mod"
  note: "Created by CactusVRStudios"
sources: "Assessment based on the KHARVOX: ARGENT GitHub repository and README, GitHub Releases API data, and YouTube VR coverage (Beardo Benjo, VR DaD, LunchAndVR, PCVR Gamer, JShodanVR, NotAGameAddict). Reddit and Flat2VR Discord were attempted without usable reception data. No direct testing performed."
history:
  - date: 2026-09-29
    note: "KHARVOX: ARGENT released v1.0, a native Vulkan VR conversion of Doom Eternal with full motion controls, Virtual Gunstock two-hand support, snap turning and optional bHaptics and PSVR2 haptics."
---

There is a moment in Doom Eternal when a Marauder fills your entire field of view, shield glowing green, eyes locked on, and for a split second you stop thinking about controllers and start thinking about survival. That is the kind of presence ARGENT now sells for real. Not as a stereoscopic curiosity. As a shooter you can actually play in a headset.

For years the only way into Doom Eternal VR was through injection drivers — VorpX's Reshade + Desktop Viewer kludge, or VK3DVision's excellent 3D with zero head tracking. Those options are still technically there if you already rely on them, but they are no longer the story. The story is KHARVOX: ARGENT, a native Vulkan conversion by CactusVRStudios that launched v1.0 on September 29, 2026, and it changes almost everything about how this game reads in VR.

## What ARGENT Actually Is

ARGENT is not an injection wrapper. It launches `DOOMEternalx64vk.exe` through its own `ArgentLauncher.exe`, replaces enough of the rendering path to deliver stereo VR, and gives you hand-tracked motion controls inside the full campaign. That makes it a conversion, not a profile.

The distinction matters because it shows up everywhere. Menus and tutorials auto-present on a virtual screen instead of floating brokenly in your face. The weapon is tied to your hand, not your neck. Glory kills are a physical motion, not a cutscene that wrestles the camera away from you. Where the old injection routes added depth to a flat image, ARGENT rewrites how you interact with the game.

Installation is moderate, not trivial. You extract the complete ZIP into a new, writable folder — not inside the Doom Eternal install directory, and definitely not by running it from inside the archive. After that, `ArgentLauncher.exe` becomes your entry point every session. Steam and Microsoft Store copies both work. The first launch runs a native VR intro, after which you can disable it under Rendering. The main failure modes are obvious: wrong folder, missing runtime, or launching the game directly instead of through the launcher.

## The Motion Controls

This is the part that makes the article feel like a different game. ARGENT gives you full 6DOF motion controls, a Virtual Gunstock for two-hand weapon support, and physical glory kills driven by controller speed.

The Virtual Gunstock is the standout. Hold the off-hand grip near the weapon's support point and the gun locks into a two-hand stance; release and you're back to one-hand. A grip press away from the weapon cycles equipment. For a game whose entire identity is heavy, fast gun handling, that physicality matters. The Super Shotgun and its meat hook finally make sense in a way they never did when the weapon was welded to your face.

Glory kills and melee use a selectable punch hand with a speed threshold. You need a valid target and the normal activation conditions, but the actual trigger is swinging your controller hard enough. It sounds like a gimmick until you realize how much it restores the Slayer fantasy: you are not pressing a button to watch a canned animation; you are physically finishing the demon.

Left-handed layouts are also properly handled. Button Swap moves weapon trigger and grip plus Use and melee stick-click to the left controller; Button-and-Stick-Swap goes further, swapping face buttons and stick directions so movement and weapon control land where they should. The Pause Menu stays on the physical Menu button, and Index users can reach it via touchpad click.

## Movement and Comfort

Doom Eternal's combat has always been the central problem in VR. Fast, aggressive gunplay plus dash-jumping plus threats arriving from every direction is a brutal combination for a headset. The injection routes had no snap turning, no hand-directed movement, and no real comfort options. ARGENT removes most of that problem.

You can choose smooth or snap turning, with adjustable speed and snap angle. You can choose head-directed or off-hand-directed movement. Snap turning is a real option here, not a checkbox added for liability, and off-hand-directed movement means you can aim with your head while your off-hand handles locomotion. That is the exact control separation that makes fast shooters tolerable in VR.

Menus and tutorials appear on a virtual screen automatically. Glory kills are controller-driven, so the camera does not rip you around during the animation. The result is still intense — Doom Eternal is still Doom Eternal — but the intensity is now mostly under your control, not forced on you by a driver that does not understand the headset.

## Haptics and Rendering

ARGENT supports bHaptics suit feedback and PSVR2 adaptive triggers, though both require separate hardware and software. bHaptics needs the bHaptics Player for Windows and paired gear; missing it does not block startup. PSVR2 adaptive triggers are experimental and require PSVR2 Toolkit 1.0 or newer installed separately, plus a working PSVR2 SteamVR setup. Normal rumble works on its own.

Rendering options are unusually deep for a community conversion. Stereo rendering is standard, with optional 3D Cinematics requiring a restart after toggling. RenderScale starts at 100% as the native reference; lower values reduce render work. FSR Upscaling is available but disabled at 100% and up, and on the SteamVR path it does not apply the launcher's FSR reduction — you adjust resolution through SteamVR instead. DLSS is selectable in-game on NVIDIA hardware, but stereo DLSS is experimental and uses separate per-eye histories. FSR and DLSS are mutually exclusive because FSR forces anti-aliasing off.

The README also notes that ARGENT blocks the game's native TAA in stereo, which is what otherwise blurs the VR image. A Desktop Mirror option outputs the right eye at 720p to 4K for spectators or recording, though the mirror resolution only affects the desktop feed and can add GPU overhead without improving headset detail.

## What Still Needs Honesty

I want to be clear about what ARGENT is not. It is a private project developed with limited resources, and the README says so itself. That framing is important: this is not a Bethesda-supported feature with a QA department and a refund policy.

AMD graphics cards currently have known rendering issues, which may or may not improve with updates. Water specifically can produce visual artifacts in VR. Runtime coverage is limited to VDXR, SteamVR OpenXR, and Meta OpenXR — other runtimes are unvalidated and unsupported. The recommended pairings are explicit: Quest headsets should use VDXR or MetaXR, not SteamVR, because SteamVR with Meta hardware is known to cause issues. Index users should stick to SteamVR.

Stereo DLSS and PSVR2 adaptive triggers are experimental. Extended Logging helps debugging but hurts performance and should be turned back off. These are not footnotes; they are the reasons the recommendation stays "with Caveats" despite the A-tier leap.

## If You Already Run VorpX or VK3DVision

VorpX and VK3DVision still exist if you are already invested in them. VK3DVision remains the simplest path to excellent stereoscopic 3D with no head tracking, and VorpX can still deliver head tracking through its Reshade + Desktop Viewer workaround. Neither gives you motion controls or 6DOF, and neither is the subject of this page anymore. They are legacy options for legacy users.

## Closing Take

KHARVOX: ARGENT is the difference between "Doom Eternal looks amazing in 3D" and "Doom Eternal is a real VR shooter." The conversion has a full feature set: motion controls, gunstock support, physical glory kills, snap turning, off-hand-directed movement, deep rendering options, and active support. The base game is still S-tier material. The VR implementation is now good enough that I can recommend it to VR enthusiasts who own Doom Eternal and are willing to do a little launcher setup.

But I am not going to pretend this is a polished first-party release. Limited resources, AMD issues, water artifacts, a narrow validated-runtime list, and two explicitly experimental features all mean the same thing: read the README, use the recommended runtime for your headset, and go in with your eyes open. The caveats are real. They just no longer outweigh the achievement.
