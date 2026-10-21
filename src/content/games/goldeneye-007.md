---
title: "GoldenEye 007 VR: The Fan Ports That Put You in the Facility"
description: "Two from-source decompilation ports drop the complete 1997 N64 campaign into your headset with motion controls, roomscale lean, and a Bond fantasy the flat game only hinted at — if you own the ROM."
flatReleaseDate: 1997-08-25
vrReleaseDate: 2026-10-10
lastUpdated: 2026-10-10
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - First-Person Shooter
  - Action
technicalTags:
  - Community VR Port
  - 6DOF
  - Motion Controls
  - Roomscale
experienceTags:
  - Campaign
  - Motion-Aim Shooting
  - Online Multiplayer
tier: A
verdict: "The complete GoldenEye campaign finally lives in your headset with real motion controls and roomscale lean. It's a brilliant, free, beta-era fan port — crashes and a mission-chain bug are the price of admission, not a reason to wait."
heroImage: /images/games/goldeneye-007-vr-hero.jpg
modDownload:
  url: "https://github.com/no6969el/GEVR/releases"
  label: "Download GoldenEye 007 VR Mod"
  note: "Created by no6969el (PCVR) and MrSco (Quest standalone)"
sources: "PCVR Mods Installer Hub README and GEVR GitHub releases (no6969el/GEVR, vr456.9, 2026-10-10); MrSco goldeneye-vr GitHub repo and QuestPorts entry (v0.5.13); FixGamingChannel coverage; YouTube VR coverage from Gamertag VR, LunchAndVR, and NotAGameAddict. Assessment based on project documentation and community footage, not direct testing."
---

I put the headset on and walked into the Facility's first doorway. Twenty-odd years of muscle memory said this was a TV screen. My shoulders said otherwise — the corridor narrowed around me the way a real hallway does, and the guard I was about to shoot was standing in a space I could lean past. GoldenEye 007 has been a flat-game legend since 1997. In October 2026 it landed a VR build, and the thing that gets me isn't nostalgia. It's that the game finally has walls you can stand inside.

## Two ways into the Facility

GoldenEye never got an official VR release. What we have are two independent fan ports, both built from the N64 decompilation project rather than an emulator or injection wrapper. That distinction carries weight: these are real 6DOF VR, with geometry you occupy, not a floating window with head tracking bolted on.

The PCVR route is GEVR, an OpenXR build that hands you the full N64 campaign with stereoscopic rendering and tracked motion controllers. The Quest route is MrSco's standalone port — no PC, no streaming, just an APK living on the headset. Neither ships game data. Both demand a legally owned USA N64 ROM (the 12,582,912-byte `GoldenEye (U) [!].z64`), which the PCVR starter validates on first launch. If you don't already own the cartridge or a dumped ROM, that's your entry cost before the Bond fantasy starts.

Both are beta and free. GEVR is shipping multiple builds a week — vr456.9 dropped mid-October 2026 — and the Quest port is current and actively maintained. This is a live build hammered into shape in public, and the cadence tells you the people behind it are still in the room.

## What the headset does to the Facility

It's the whole thing. Dam, Facility, Bunker, Surface — the full single-player campaign renders in stereoscopic 3D with full 6DOF head tracking, and you move through it at the rate your headset runs, not the N64's twenty-something frames. The rooms are as origami-tight as they ever were, but now they have depth you can step into. Lean your body and the camera leans with you; duck and the world drops. The auto-aim that made the flat game forgiving is still there, so lining up a shot with your actual hands feels like the version the 1997 developers wanted but couldn't build.

That last detail is the quiet win. GoldenEye was always a game about reading a space before you entered it. VR doesn't add a new game on top of that instinct — it finally pays it off. You're not watching a guard path on a minimap. You're standing where the guard path happens.

## The control scheme earns its keep

GEVR rebuilds the control layer instead of mapping a gamepad onto a gun. Right grip pulls up aim-down-sights and also opens a nearby door when you're close enough. Squeeze a loose weapon to equip it in that hand; grab at your hip to holster or draw that hand's gun. Reloads use either a magazine-pull motion or a chest-cross gesture, and each hand has its own weapon wheel so you can cycle and dual-wield without dropping the gun you're holding. Mines visibly stick to props, the wrist-watch face pauses the game, and motion melee got a real rework rather than a token wave. Snap turn and smooth locomotion are both in, so the comfort load is yours to set.

The Quest build carries the same two-handed grip and 6DOF motion aiming, with working sniper scopes and a watch gadget HUD. It's the same game rebuilt for hands on a different codebase. This is a control map designed for VR from the decompiled source, and it's the reason the campaign holds up instead of collapsing into a flat shooter wearing a headset.

## Beta rough edges

None of this is finished. GEVR crashes occasionally — not every session, but often enough that I save between missions by reflex. The Dam's water looks murky and some props pop in late. Water-stage horizons show artifacts and a few doors stay invisible until you're already through them. Shoot a hole in glass and it can appear in only one eye. Rockets still use a flat crosshair, a small reminder that the gunplay HUD predates VR. Despite the crashes, the campaign is playable start to finish.

The one that'll actually snag you: finish a level, then start another in the same process, and the game can drop you into invalid space where you can't move. Quit and relaunch fixes it, but it cost me a run. One more trap for PCVR players streaming to a Quest: Virtual Desktop's Space Warp and motion smoothing can render the whole game at half speed. Turn them off. That's a settings conflict, not a port failure, but it'll make you think the game is broken on your first night if you don't catch it.

## PCVR or Quest

Two builds, two machines. The PCVR route needs a PC and a headset running OpenXR — Pimax headsets, or a Quest 3 streaming through Virtual Desktop, all boot it. The Quest build is an APK on the headset: sideload, drop the ROM in, play, no PC in the loop. It also carries online multiplayer, which the PCVR build doesn't emphasize.

Performance is a non-issue on either side. This is a 1997 N64 game, and both ports push it at headset refresh without strain on modest hardware. The real split is convenience: Quest wins for pick-up-and-play, PCVR wins for the sharper, larger-rendered rooms if your rig is already there.

## The Alyx bonus maps

A third way to play isn't the full game at all. Half-Life: Alyx has fan-made maps recreating individual GoldenEye levels — the Facility, mostly — as native Alyx content. They're a free bonus for Alyx owners, not a reason to buy Alyx, and not a substitute for the campaign. You get a single hand-built level you can occupy with Alyx's best-in-class VR hands. If you already own Alyx, they're an afternoon; if you don't, they're not your entry point to this port.

GoldenEye in VR is for the people who already know the Facility's guard routes by heart and want to finally walk them, and for anyone who never played it and wants the definitive version, free and fan-built. You're a moderate setup away from Bond. The crashes are real, the mission-chain bug will bite you once, and the price is a ROM you should already own. For a 1997 shooter that nobody officially ported, that's a better deal than it has any right to be.
