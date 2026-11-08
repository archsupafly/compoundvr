---
title: "Metro Exodus VR"
description: "Metro Exodus never shipped an official VR mode, but a free community full-conversion mod drops you into the Russian wasteland with two-handed rifles, manual reloads, and proper 6DoF."
flatReleaseDate: 2019-02-15
vrReleaseDate: 2026-11-06
lastUpdated: 2026-11-06
featured: false
routeType: Framework Only
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Beginner Friendly
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - First-Person Shooter
  - Post-Apocalyptic
  - Survival
technicalTags:
  - Full VR Mod
  - OpenXR
  - 6DoF
  - Motion Controls
experienceTags:
  - Manual Weapon Handling
  - Two-Handed Weapons
  - Atmosphere
  - Post-Apocalyptic World
tier: A
verdict: "A great post-apocalyptic shooter finally earns its VR legs through a community mod that nails manual weapon handling and real presence — play it now, just know it's a fresh beta on the Standard Edition only."
heroImage: /images/games/metro-exodus-vr-hero.jpg
modDownload:
  url: "https://github.com/RippeR37/MetroExodusVR/releases"
  label: "Download Metro Exodus VR Mod"
  note: "Created by RippeR37"
sources: "Assessment based on the mod's GitHub repository and README, the first public beta release notes, the UnflatVR aggregator listing (UFVR Grade B, VR controls 25/25), and launch-window YouTube coverage from Gamertag VR, VR DaD, Headset-VR, Paradise Decay, JShodanVR, ChesBM, DenailS and Parzival. Engine-compatibility facts (4A Engine, D3D11 Standard Edition, D3D12 Enhanced Edition) drawn from the community engine dossier. UEVR confirmed inapplicable (Unreal-only scope). No direct hands-on testing; evaluation reflects the mod's documented feature set and launch-week reception."
---

I've wanted Metro Exodus in VR since the week it launched. The flat game is one of the best post-apocalyptic shooters of its generation — the Aurora train you call home, the dead husk of Moscow, the Volga at night — and it always felt built to be lived in, not watched. The problem was never the game. It was that 4A Games never gave it a headset mode, and the engine underneath isn't one any VR framework can reach. That changed a few days ago.

## What You're Getting

There is no official VR mode for Metro Exodus. Not from 4A Games, not from Deep Silver, not buried in a patch. If you've been hunting for a headset toggle in the settings for years, it isn't there, and it was never coming. What's there now is a community full-conversion mod that throws out the flat renderer and builds a native OpenXR VR pipeline on top of the game's Direct3D 11 build. This isn't a stereo-in-a-window hack with head tracking bolted on. It's a real 6DoF renderer with motion controls, manual weapon handling, and gear worn on your body.

The author is RippeR37, and the mod is free — no paywall, no Patreon tier, just a download and an optional donation link. Installation is about as painless as this hobby gets: grab the release archive, extract it, make sure your VR runtime and the store launcher are running, and launch the mod's executable. There's a built-in auto-updater, so you're not crawling GitHub for the next build by hand. If you've been burned by mod stacks that need three dependencies and a DLL-soup loader, this isn't that.

One hard boundary up front, because it bites a lot of owners: the mod targets the Standard Edition of Metro Exodus on Steam. The Enhanced Edition — the 2021 ray-traced upgrade — runs on a different Direct3D 12 renderer the mod doesn't support yet, and the Epic and GOG builds are still flagged work-in-progress. If you bought Exodus on the Epic Store back when it was a timed exclusive, or you're living in the Enhanced Edition, you don't have a clean path in right now. That's a real limitation, not a footnote, and I'll come back to it.

## Stepping Inside The Metro

The first thing that hits you is scale. Metro Exodus cuts between tight subway tunnels and wide, semi-open chapters — the Caspian desert, the swamp, the frozen Volga — and in the headset those spaces stop being backdrops and start being places. I spent the opening hours on the Aurora and being able to physically lean into a compartment, check a map pinned to my wrist, and shoulder a rifle to look down the car changed how the scene reads. The game's famous atmosphere — the dread of the dark, the wet hiss of the gas mask filter, the long quiet between firefights — lands harder when your own body is the camera.

## Rifles You Actually Hold

This is where the mod separates itself from every "Metro in VR" idea I'd dismissed over the years. You grip them, you two-hand them, you rack the bolt and flip the magazine out to reload by hand with custom poses and animations. The workbench ritual — stripping a Kalash, taping a makeshift suppressor, swapping the stock — is no longer a menu you click through; it's something you do with your hands at the bench. For a game whose whole identity is improvised post-war gunsmithing, that is the single biggest thing VR adds, and the mod delivers it cleanly.

Left-handed players are supported outright, which is rarer than it should be, and there's experimental bHaptics support if you've got a vest. Gear — your lighter, your compass, your filters — sits on your body rather than buried in a HUD, which pushes the survival-loop tension the series is built on. Foveated rendering and upscaling options are in there too, and they matter, because this is a heavy game to run in stereo.

## The Performance Tax

Metro Exodus was a demanding flat game and it stays a demanding VR one. We're rendering a dense, ray-traced-adjacent wasteland twice now, once per eye, through a community renderer that's weeks old. The mod supports DLSS, FSR2, and DLAA up to 4.5 to claw back frames, and foveated upscaling helps if your rig is mid-range, but make no mistake: this is a high-end or ultra-tier PC game in the headset. A mid-range machine will run it, but you'll be turning settings down and accepting some resolution trade-off to hold a stable frame rate. Comfort and presence both collapse the moment the framerate dips in a shooter this physical, so treat the performance budget seriously before you start a session.

## What's Genuinely Great

The world is the draw, and the mod lets you inhabit it instead of watching it. The semi-open chapters — scavenging the Volga, crossing the desert, creeping through the swamp — give you room to move and look, and the headset makes the emptiness feel earned rather than empty. The manual weapons handling is the headline feature and it earns the praise it's getting; it's not a gimmick bolted on for the trailer, it's the core verb of the game rebuilt for hands. Setup is beginner-friendly, the download is free, and the auto-updater means you won't be left managing versions by hand.

## Where It's Raw

This is a first public beta, and it reads like one in specific ways. Only the main campaign is playable. The two story DLCs, The Two Colonels and Sam's Story, aren't in the headset yet — the author has said they're coming in a later version, but right now your trip ends when the campaign does. If you were planning to replay Sam's Story as your VR entry point, hold.

The build, store, and edition walls are the other real catches. Steam Standard Edition owners are golden. Enhanced Edition owners, Epic owners, and GOG owners are out of luck until those builds get brought in line, and there's no timeline on that. A meaningful slice of the existing player base — anyone who grabbed the game during its Epic-exclusive window or upgraded to the ray-traced edition — currently can't play what's shipping. That's not a quality ding on the VR experience itself, but it's a purchasing-and-ownership reality you need to check before you get excited.

Then there's the simple fact that it's young. Two days into a public beta, the rough edges that do exist haven't all been cataloged, and the reception so far is launch-window enthusiasm rather than a settled verdict. The core works and works well, but I'm not going to pretend a two-day-old mod has the polish of a shipped port. The bones are excellent; the finish is still drying.

## The Wasteland Was Worth The Wait

Metro Exodus was always a world worth being inside, and this mod is the first thing that actually puts you there with your hands on the gun and your own weight behind the lean. The manual reloads, the body-worn gear, the sheer scale of the chapters — that's the game earning its VR, not a tech demo cosplaying as one. The catches are honest and mostly about freshness and ownership, not about broken VR: main campaign only, Standard Edition on Steam only, and a performance bill that wants a serious rig. If you own the right build and you've got the hardware, this is a recommended, genuinely special way to replay one of the best shooters of its era — and if you're on the Enhanced or Epic build, the move is to watch for the next version rather than force it today. Either way, the "Metro has no VR" answer I'd given friends for years is officially dead.

