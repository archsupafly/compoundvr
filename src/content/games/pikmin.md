---
title: "Pikmin VR"
description: "Project Honeydew is a free native VR port of the original Pikmin that puts you on the garden floor at true scale, with tracked hands that pull, throw, pet and punch. It is an unofficial fan project, and coverage is still thin."
flatReleaseDate: "2001-10-26"
vrReleaseDate: "2016-07-13"
lastUpdated: "2026-10-15"
featured: false
routeType: "Multi-Route Coverage"
platforms: ['PCVR', 'Quest']
recommendation: "Recommended with Caveats"
playability: "Fully Playable"
setupBurden: "Moderate Setup"
inputStyle: "Full Motion Controls"
comfort: "Comfortable"
performance: "Moderate Demand"
supportStatus: "Active"
genres:
  - Real-Time Strategy
  - Puzzle
  - Adventure
technicalTags:
  - Full VR Mod
  - Native 6DOF
  - Motion Controls
  - Hand Presence
  - Online Co-op
  - Monitor Play
  - Emulator
experienceTags:
  - First-Person
  - Hand Interaction
  - Co-op
  - Scale
  - Diorama Scale
  - Puzzle Strategy
  - Nintendo
  - Retro
tier: A
verdict: "Project Honeydew finally delivers the Pikmin fantasy: you are standing in the garden, reaching into the dirt, commanding a swarm at real scale. The physicality is real, the game is complete, and the caveats are the honest kind — young project, thin third-party coverage, and a few untested platforms."
heroImage: /images/games/pikmin-vr-hero.jpg
modDownload:
  url: https://projecthoneydew.com
  label: "Download Project Honeydew VR Mod"
  note: "Unofficial fan project by the Project Honeydew team — not affiliated with Nintendo"
history:
  - date: 2026-10-15
    note: "Project Honeydew 0.3.0 released — native first-person VR port of the GameCube original with online co-op, Quest 3/3S standalone and Steam Frame builds."
sources: "Research conducted via projecthoneydew.com (downloads, changelog, install guide, VirusTotal link, SHA-256 checksums), the Project Honeydew YouTube channel and the 0.3.0 trailer 'Pikmin in VR, Now With Online Co-op', NotAGameAddict 'Pikmin VR Performance / Meta Quest 3 Standalone VR Mod with 6DOF Motion Controls', Topomx 'Pikmin VR! (Quest 3 Standalone)' livestream, r/ProjectHoneydew and the 0.3.0 launch cross-posts across r/Pikmin, r/OculusQuest, r/VRGaming, r/virtualreality and r/Emulationonquest, the Pikmin 4K texture pack by Henriko Magnifico, and Dolphin VR historical coverage via VR Bites, VRborg and the Dolphin VR blog."
---

The fantasy of Pikmin in VR has always been obvious. You're a tiny astronaut commanding an army of two-inch plant-creatures through a backyard that acts like a jungle. Scale is the whole point. Leaning down and seeing your swarm scurry through grass blades taller than they are is exactly the kind of thing a headset should do well.

For years, the only way in was Dolphin VR, a 2016 fork of the GameCube emulator that bolted stereoscopic 3D and head tracking onto the original game. It turned Pikmin into a pretty overhead diorama, then stopped updating. That path is still technically around, but it is frozen in time and not the story anymore.

The story now is Project Honeydew, a free native VR port of the 2001 GameCube original that dropped in October 2026. It is built from the ground up around first-person scale and hand presence, and it plays like the thing I assumed was years away.

## In the Dirt, Not Above It

Honeydew switches the camera from overhead strategy view to first-person ground level. You are Olimar-sized now, standing in the garden with the Pikmin at your feet. The painted forest wall that normally boxes in the flat version is gone in VR — you see the open horizon beyond the level, which makes the space feel unexpectedly large.

The hands are the center of the design. You reach down and pluck a Pikmin out of the dirt. You grab one by the stem, pull back, and throw it toward a target. A white ring at a Pikmin's feet shows which one your hand is about to grab, which keeps the action readable when the swarm clusters together. Whistling is aimed with your hand, not a cursor. You can pet a Pikmin — it waits under your palm and reacts to each stroke — or punch an enemy with a closed fist if you want Olimar to get personally involved.

Hold the throwing stick up and the view deliberately blinks to roughly eight meters above Olimar, looking down on him like a toy. Let go and it snaps back. A tabletop view sits higher and tilted toward you like a drafting board, where everything looks 1.5× bigger by default and you can zoom by pulling both grips apart. The diorama fantasy is still there; it is just one mode among several, not the whole experience.

The VR UI is thoughtful. A wristwatch shows radar, time of day and a mute badge. Enemy health bars drop to your eye level when they matter. An over-the-shoulder hand camera lets you photograph the squad without your own helmet in frame. Settings are laid out in a headset-friendly menu with tabs, a quick bar, and a render-resolution slider that auto-reverts after ten seconds so you can't accidentally brick your view. It is the kind of polish that suggests someone actually put the headset on while building it.

## The One Real Gate

Setup is no longer emulator archaeology, but it still has one hard requirement: you need your own Pikmin GameCube disc image, USA Rev 1, as ISO, GCM, CISO or NKit. The mod reads the disc image and never touches or copies the game files. The launcher is straightforward — unzip, run `nectar-launcher`, install, point it at your disc image, then hit Play with SteamVR already running — but the disc requirement is the gate that decides whether you can play at all.

Windows 64-bit is the main build and the most tested. Linux x86-64 is available for Steam Deck and Linux PCs, but it is untested on real hardware. There is an experimental Steam Frame ARM64 build and an experimental Meta Quest 3 / 3S standalone APK via SideQuest or `adb install`. The Quest build needs the disc image copied over USB as .iso or .gcm, with other formats converted first, and it cannot play online with the PC builds yet. The app is unsigned, so Windows SmartScreen will complain until you click through. The site publishes a SHA-256 checksum and a VirusTotal scan for every build.

Headset support is honest about its limits. The mod was built and tested on the original HTC Vive and tested on Meta Quest 3 through Link. Valve Index, Steam Frame streaming, Quest via Steam Link / Air Link / Virtual Desktop, and other SteamVR headsets are untested. If you are on a headset outside the Vive / Quest 3-via-Link pair, you are in early-adopter territory.

## What Works and What Is Still Young

The physical scale works. Pikmin feel appropriately tiny, Bulborbs feel appropriately massive, and the spatial relationships that matter in combat and routing are easier to read when you are standing inside them rather than hovering above them. The motion controls map cleanly to the game's actions, and the quality-of-life touches add up: Olimar no longer slides down gentle slopes while idle, skipped cutscenes preserve the day-one Main Engine pickup, and a sleeping Pikmin may stir instead of every single one snapping to look at you on cue.

Online co-op is built for two, mixed VR and monitor play, with proximity voice chat, high-fives and handoffs of Pikmin between players. Room codes are short so a friend behind a strict router can still join. Both players need the same version, and Windows, Linux and Steam Frame builds of the same version can play together.

But the project is young. r/ProjectHoneydew was created on October 8, 2026 and currently holds a single post. The 0.3.0 launch was cross-posted to several subreddits and sits at score 1 with zero comments. Independent video coverage is thin: NotAGameAddict has a performance-focused Quest 3 standalone video, and Topomx streamed the Quest build. There is no established review record, no aggregate score, no long-term stability report. That is not a knock on the build quality; it is a reason to keep expectations calibrated.

Performance is generally modest for a 2001 GameCube game. The optional Pikmin 4K texture pack by Henriko Magnifico adds VRAM load and can stutter briefly the first time an area's textures load, which is normal for a big pack. Base play is comfortable, seated mode and snap turn are supported, and the site is upfront that VR can cause motion discomfort in general.

## What You Are Actually Playing

This is the original Pikmin — not [Pikmin 2 in VR](/games/pikmin-2/), not Pikmin 3 Deluxe, not Pikmin 4, not the Switch remasters, not Hey! Pikmin on 3DS. Project Honeydew needs exactly that GameCube USA Rev 1 disc. If you do not own it, you cannot play. Pikmin 2 is its own product with its own page, and nothing else in the series currently has a meaningful VR path. The Switch remasters remain the definitive flat way to play the broader franchise.

## The Honest Bottom Line

The thing the old emulator path only hinted at — standing in the garden, hands in the dirt, actually directing a swarm at real scale — now exists and works. Project Honeydew is a real native VR port with real interaction design, real co-op, and a real respect for the original game. It is also two weeks old, unofficial, thin on independent coverage, and partly untested across headsets.

If you own the disc and have a Vive or a Quest 3 via Link, this is worth the moderate setup. If you do not own the disc, the question is moot until you source one. If you are betting on Quest standalone or an untested headset, you are buying into a promising early build. The garden is finally worth visiting in a headset. Just know you are visiting a fan project, not a Nintendo release.
