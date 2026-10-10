---
title: "Hollow Knight VR"
description: "A community depth mod turns Hollow Knight's hand-drawn world into layered 3D space you can lean into — the gameplay stays 2D, but the world finally breathes around you."
flatReleaseDate: 2017-02-24
vrReleaseDate: 2024-01-01
lastUpdated: 2024-01-01
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Gamepad Preferred
comfort: Comfortable
performance: Efficient
supportStatus: Stable but Quiet
genres:
  - Metroidvania
  - Action
technicalTags:
  - Full VR Mod
  - BepInEx
  - Parallax Depth
  - OpenXR
experienceTags:
  - Seated Experience
  - Hand-Drawn World
  - Gamepad
  - Presence
tier: B
verdict: "The depth mod makes Hallownest worth inhabiting in a headset, but you're a spectator with head tracking, not a participant with hands — a beautiful diorama, not a rebuilt world. Recommended with caveats for fans who already love the game."
heroImage: /images/games/hollow-knight-vr-hero.jpg
modDownload:
  url: "https://www.nexusmods.com/hollowknight/mods/169"
  label: "Download Hollow Knight VR Mod"
  note: "Created by SadMonsterParty"
sources: "PCVR Mods Hub installer README for Astien's HollowKnight_VREnhanced; Astienth VR-Mods-Projects repository; Nexus Mods listing #169 (SadMonsterParty's Flat-To-VR); VRMods-List curated entry; author gameplay videos documenting the BepInEx parallax-depth mod approach."
---

I dropped into the Forgotten Crossroads and leaned forward without thinking. The lantern in the foreground and the crumbling wall behind it didn't just sit on a flat plane anymore — they slid apart in real space, and for a second I was standing inside a paper diorama that had been breathing the whole time I wasn't looking.

Here's the trick with Hollow Knight. It's a 2D hand-drawn Metroidvania — one of the best of its kind, a game where Team Cherry stacked painted sprite layers to fake depth on a monitor. The community figured out you don't have to rebuild that as a 3D game to make its world breathe. Separating the art into depth is enough, and a couple of modders turned that into something you can wear a headset for.

There's no official VR mode for Hollow Knight and there never was. What exists is a community BepInEx plugin that grabs those sprite layers and pushes them apart in 3D space, so the headset perceives real parallax as you move your head. The gameplay stays exactly what it always was — a 2D side-scroller you play with a gamepad. This isn't a rebuild. It's a better way to look.

Two independent mods do this, and they're worth telling apart. Astien's HollowKnight_VREnhanced ships through the PCVR Mods Hub installer, which auto-locates your Steam copy, offers a clean folder copy so your flat-screen version stays intact, and hands you a "Start in VR" button. It runs on OpenVR by default and flips to OpenXR with one config edit. SadMonsterParty's Flat-To-VR lives on Nexus and wants you to drop a BepInEx plugin and an OpenVR DLL into the game folder, then launch under SteamVR. Both target the Steam PC build only — this is a PCVR thing, full stop.

That split matters because the easy path and the manual path feel like different commitments. The Hub installer is close to turnkey: it does the folder juggling for you and leaves your regular install alone. The manual Nexus install is a fifteen-minute afternoon if you've ever touched a mod folder and a small adventure if you haven't. Either way you're installing into the game directory, which makes that folder VR-only until you revert — rename the winhttp.dll or verify files to get your flat screen back.

## The trick: depth without a rebuild

What a couple of modders figured out is that separating the art into depth is enough to make its world breathe. The config that drives it is simple: a `spaceBetweenMultiplier` setting, default 1.65, that controls the gap between sprite layers — higher pulls the world apart into pronounced depth, lower flattens it back toward the monitor. I run it a touch above default. It doesn't change the game. It changes how much I want to be in it.

There's a trade worth knowing. Cranking `worldScale` up makes Hallownest feel grander, more present, but it quietly tightens the headset's 6DoF freedom — a known side effect of how the scaling is implemented. You get a bigger world or a freer head, not both at max. I settled on a middle scale: present enough to feel like I'd stepped inside, free enough to lean and peek without hitting a wall I couldn't see. A seated setup is recommended, and it's the only way this makes sense — you're not walking anywhere, the camera does the moving, and your head is the only thing exploring the space.

Controls are unchanged from the flat game. Gamepad or keyboard, no motion controllers, and after ten minutes I stopped reaching for them. The depth is the headline, not the inputs. If your view drifts, you recenter by holding three buttons at once — up, quickmap, and pause — which sounds fiddly until the first time you need it and realize it's muscle memory by the second session.

## What lands, what doesn't

The thing that lands is the art. Hollow Knight is already one of the most beautiful 2D games ever painted, all moody caverns and patient insects, and the parallax that was a gentle suggestion on a monitor becomes a real room you're standing in. Greenpath's overgrowth has foreground, midground, and a hazy drop behind it. The City of Tears feels like a constructed space with actual volume. I keep coming back to that first lean in the Crossroads — the moment the world stopped being a picture and started being a place.

Performance is a non-issue. This is a lightweight Unity game with a sprite-depth plugin on top; any VR-capable PC runs it at framerate without breaking a sweat. Comfort is about as safe as VR gets — you're seated, the world moves and you don't, there's no artificial locomotion to fight. A real person has even finished a Steel Soul permadeath run inside the headset, which tells you the control scheme holds up under the worst the game can throw at it.
