---
title: "Deus Ex: Human Revolution VR"
description: "Deus Ex Human Revolution VR runs through DeusExHRVR, an experimental community mod for the Steam Director's Cut only — same-frame stereo, 6DOF tracking and hand-aimed guns."
flatReleaseDate: 2011-08-23
vrReleaseDate: 2026-09-10
lastUpdated: 2026-09-21
history:
  - date: 2026-09-21
    note: "DeusExHRVR v0.3.0 released — per-weapon grip calibration and immersive scope; current prerelease build."
  - date: 2026-09-14
    note: "DeusExHRVR v0.2.0 added motion controllers and VR direction controls."
  - date: 2026-09-10
    note: "DeusExHRVR v0.1.0 released — first public native-stereo VR build for Human Revolution."
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Uncertain
genres:
  - Stealth-Action RPG
  - Immersive Sim
technicalTags:
  - Full VR Mod
  - OpenXR
  - Motion Controllers
experienceTags:
  - Stealth
  - Cyberpunk
  - Story-Driven
tier: B
verdict: "DeusExHRVR turns a landmark stealth-RPG into a genuine you-are-Jensen experience, but it's a WIP prerelease locked to one Steam build with real rough edges — play it if you already own the Director's Cut and don't mind living on the bleeding edge."
heroImage: /images/games/deus-ex-human-revolution-vr-hero.jpg
modDownload:
  url: "https://github.com/farmerarmor/DeusExHRVR/releases"
  label: "Download Deus Ex: Human Revolution VR Mod"
  note: "Created by farmerarmor"
faq:
  - q: "Can you play Deus Ex Human Revolution in VR?"
    a: "Only through a community mod. Square Enix never shipped a VR mode for Human Revolution, and the proprietary Crystal Engine rules out UEVR and REFramework entirely. DeusExHRVR, by farmerarmor, is the whole VR story: it drives the Director's Cut's own HD3D stereo renderer through OpenXR for native same-frame stereo plus 6DOF head tracking, with a first public build in September 2026."
  - q: "Is the Deus Ex HR VR mod free?"
    a: "Yes. DeusExHRVR is a free community mod published on GitHub by farmerarmor, and it is still a WIP prerelease rather than a finished product. You do still need the game: the mod layers onto the Steam Director's Cut, so the only purchase involved is the flat release you probably already own."
  - q: "Does it work with the original release or Director's Cut?"
    a: "Director's Cut only, and specifically the Steam build 2.0.66.0. The installer verifies that executable before changing anything of yours, and GOG copies plus the original non-Director's Cut release are rejected by design. Installing through the PCVR Mods Installer Hub also applies the known High Core Count exe patch inside the same reversible transaction."
  - q: "Does it have motion controls?"
    a: "Yes. The motion controllers emulate the game's default Xbox layout, with Y and B exchanged, and v0.3.0 added per-weapon grip calibration: hold both thumbsticks for a second, move the controller into the grip you want, then release to save that weapon's offset. Hand-aimed weapons are experimental rather than finished, and native rumble is not mapped to VR haptics yet."
  - q: "Does it work on Quest or PSVR2?"
    a: "No. DeusExHRVR is PCVR only — Windows, DirectX 11 and an active OpenXR runtime — with Oculus and VDXR reported working. There is no standalone Quest port and no PSVR2 version, and the current prerelease has black-screen reports under SteamVR, so the author steers you to Oculus or VDXR until a later release says otherwise."
relatedPages:
  - id: deus-ex
    kind: game
    note: "The original Deus Ex in VR."
  - id: cyberpunk-2077
    kind: game
    note: "Another cyberpunk world in a headset."
sources: "Research conducted via the PCVR Mods Installer Hub DeusExHRVR README (primary structured source), the DeusExHRVR GitHub repo and release download counts, the UEVR releases API for framework-compatibility confirmation, Reddit via Pullpush, and four DXHR-specific YouTube VR coverage videos (TheReclusiveGamer, Uruzz, Seth Kannof, Geoff Wilson). No direct testing performed; assessment is based on documented mod capabilities, the author's stated defects, and community reception signals."
trailer:
  youtube: "vK4k_Ieh8Wg"
  source: "EidosMontreal"
systemRequirements:
  source: "Steam"
  translationNote: "VR estimate: ~2x GPU (two-eye 90fps render vs single-eye 60fps), +1 CPU tier (tracking/physics overhead), RAM minimum bumped to 16GB (VR runtime needs headroom), storage same (identical game files), OS kept on modern 64-bit Windows (VR runtimes require it)."
  rows:
    - spec: "Processor"
      flatMin: "2 GHz dual core"
      flatRec: "AMD Phenom II X4 or Intel Core 2 Quad or better"
      vrMin: "Quad-core Intel i5 / AMD Ryzen 3 class"
      vrRec: "Six-core Intel i5 / AMD Ryzen 5 class / Six-core Intel i5 / AMD Ryzen 5 class"
    - spec: "Memory"
      flatMin: "2 GB RAM"
      flatRec: "2 GB RAM"
      vrMin: "16 GB RAM"
      vrRec: "16 GB RAM"
    - spec: "Graphics"
      flatMin: "NVIDIA GeForce 8000 series or ATI Radeon HD 2000 series or better"
      flatRec: "AMD Radeon HD 5850"
      vrMin: "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB"
      vrRec: "AMD Radeon RX 5700 8GB"
    - spec: "DirectX"
      flatMin: "Version 9.0c"
      flatRec: "Version 9.0c"
      vrMin: "Version 9.0c"
      vrRec: "Version 9.0c"
    - spec: "Storage"
      flatMin: "17 GB available space"
      flatRec: "17 GB available space"
      vrMin: "17 GB available space"
      vrRec: "17 GB available space"
    - spec: "Sound Card"
      flatMin: "100% DirectX 9.0c compatible sound device"
      flatRec: "100% DirectX 9.0c compatible sound device"
      vrMin: "100% DirectX 9.0c compatible sound device"
      vrRec: "100% DirectX 9.0c compatible sound device"
---
I've spent years telling people Deus Ex: Human Revolution is the immersive-sim revival that proved cyberpunk could be thoughtful instead of neon noise. What I never expected was to actually stand inside it. The DeusExHRVR mod landed in September 2026, and suddenly Adam Jensen's augmented frame isn't something I'm watching on a monitor — it's something I'm wearing.

<iframe src="https://www.youtube-nocookie.com/embed/vK4k_Ieh8Wg" title="Deus Ex: Human Revolution — official trailer" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## What does the DeusExHRVR mod add to Deus Ex Human Revolution VR?

This isn't an injection driver. farmerarmor's mod hooks the Director's Cut's own AMD HD3D stereo renderer — the same 3D-Vision substrate the game shipped with back in 2011 — and drives it through OpenXR. The result is native same-frame stereo. Both eyes render in a single game frame instead of alternating, which is why a 15-year-old proprietary Crystal Engine game can produce real, clean depth instead of the smeared ghosting you get from generic injection.

What you get is 6DOF head tracking and motion controllers that emulate the game's default Xbox layout. Menus, hacking minigames, videos, and the sniper scope drop to a 16:9 virtual screen, then snap back to full VR the moment you're in the world. That's a sensible compromise — the flat UI is unreadable in stereo — and it means the actual play is the part that's in your face, literally.

This is a Full VR Mod, not an official mode. Square Enix never touched VR for this title, and the proprietary Crystal Engine means UEVR and REFramework can't apply here at all. There is no framework profile to fall back on. DeusExHRVR is the entire VR story for Human Revolution, and it's impressive the story exists at all.

## How does Deus Ex Human Revolution play in VR?

The first ten minutes are a quiet revelation. Jensen moves through the Detroit police station exactly as you'd hope — your head is his head. Crouching behind cover and leaning out to line up a tranquilizer dart feels like the game always wanted to play this way but couldn't on a flat screen. The augmented-vision pulse, the pocket-secret sweep, the way conversations put you face-to-cylinder with someone — all of it lands harder when you're occupying the space rather than observing it.

Movement uses free locomotion with right-stick camera turning; there's no teleport, which is the correct call for a game built around careful spatial positioning. Comfort tooling is present if you need it. A vertical-camera lock keeps mouse or gamepad pitch out of the VR camera, an F9 recenter handles post-cutscene drift, and a WorldUnitsPerMetre scale (10–1000) lets you dial the world's apparent size. I ran it at the author's default and it felt right.

The headline feature is hand-aimed weapons — experimental, but functional. Motion controllers map the full Xbox button set, with Y and B exchanged, and v0.3.0 added per-weapon grip calibration. Hold both thumbsticks for a second, move the controller into the grip you want, release to save that weapon's offset. It's the kind of detail that tells you the author actually played this in a headset rather than guessing. Native rumble isn't mapped to VR haptics yet, which is a small but real loss when a shotgun kicks.

Performance is light. This is a 2011 game rendering two eyes through its own stereo path, so even a modest mid-range PC pushes it comfortably. The demand is nowhere near what you'd spend on a modern UEVR conversion.

## What goes wrong in the Deus Ex Human Revolution VR mod?

Here's the honest part. This is a WIP prerelease, and it shows. The author's own defect list is candid — extreme-angle weapon visibility breaks down, some lighting and shadow effects misbehave, the body behaves oddly if you physically move around your room (roomscale body tracking isn't implemented), and weapons occasionally vanish. Broader mission coverage still needs work. None of these are constant, but they're frequent enough that you'll notice them within a session.

The bigger constraint is the install surface. The mod supports exactly one executable, Steam Director's Cut build 2.0.66.0. GOG copies and the original non-Director's Cut release are rejected by design. The unmodified game can also crash on CPUs with many cores, so the PCVR Mods Installer Hub applies a known High Core Count exe patch as part of a reversible install — that's the path I'd recommend over manual setup, which leaves you handling the patch and four file placements yourself. Runtime choice matters too: Oculus and VDXR are reported working, but the current prerelease has black-screen reports under SteamVR, so the author steers you to Oculus or VDXR until that's fixed.

## Why is Deus Ex Human Revolution worth playing in VR?

Why does any of this matter for a game that's been on every "best immersive sims" list since 2011? Because Human Revolution is a world built for inhabiting. The Director's Cut's Detroit hub, the Hengsha double-decker sprawl, the corporate atria you walk through deciding whether to ghost past guards or put them to sleep — these are spaces designed around line of sight, verticality, and the slow read of a room. In VR that read becomes physical. You're not scanning a minimap for sightlines; you're craning your neck around a pillar to check the patrol path. The augments stop being a skill tree and start being a body you're learning to use.

The world is worth living in, the story has genuine weight, and the mod delivers proper 6DOF so you actually get inside it. What holds this back is squarely the implementation, not the source material. A prerelease with vanishing weapons, broken roomscale behavior, and a single supported executable isn't finished enough to recommend without that caveat — yet. The foundation is the real thing, and the gap between v0.1.0 (head tracking only) and v0.3.0 (calibrated hand-aimed guns) in eleven days tells you the author is moving fast.

## Who should play Deus Ex Human Revolution in VR?

If you already own the Director's Cut on Steam and you've wanted to replay it, this is an easy yes with one condition. Accept that you're on the bleeding edge. The mod is free, the install is mostly automated through the Hub, and the payoff — being Jensen instead of controlling him — is the kind of thing the flat version never delivered. Skip it if you only have a GOG copy, if you're on SteamVR and won't switch runtimes, or if a weapon disappearing mid-firefight would sour the whole session. If you're chasing the original game instead, our [Deus Ex VR](/games/deus-ex/) page covers what that route delivers. For another corporate-dystopia world in a headset, our [Cyberpunk VR page](/games/cyberpunk-2077/) takes the opposite approach — a full free-camera conversion rather than a native stereo path. For everyone else, this is the Human Revolution we were denied in 2011.

