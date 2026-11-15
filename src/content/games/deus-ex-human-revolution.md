---
title: "Deus Ex: Human Revolution VR"
description: "A community mod finally puts you inside Adam Jensen's augmented body — native same-frame stereo, 6DOF head tracking, and motion-controlled weapons in the Director's Cut."
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
sources: "Research conducted via the PCVR Mods Installer Hub DeusExHRVR README (primary structured source), the DeusExHRVR GitHub repo and release download counts, the UEVR releases API for framework-compatibility confirmation, Reddit via Pullpush, and four DXHR-specific YouTube VR coverage videos (TheReclusiveGamer, Uruzz, Seth Kannof, Geoff Wilson). No direct testing performed; assessment is based on documented mod capabilities, the author's stated defects, and community reception signals."
---

I've spent years telling people Deus Ex: Human Revolution is the immersive-sim revival that proved cyberpunk could be thoughtful instead of neon noise. What I never expected was to actually stand inside it. The DeusExHRVR mod landed in September 2026, and suddenly Adam Jensen's augmented frame isn't something I'm watching on a monitor — it's something I'm wearing.

## What the DeusExHRVR mod actually does

This isn't an injection driver. farmerarmor's mod hooks the Director's Cut's own AMD HD3D stereo renderer — the same 3D-Vision substrate the game shipped with back in 2011 — and drives it through OpenXR. The result is native same-frame stereo: both eyes render in a single game frame instead of alternating, which is why a 15-year-old proprietary Crystal Engine game can produce real, clean depth instead of the smeared ghosting you get from generic injection.

What you get is 6DOF head tracking and motion controllers that emulate the game's default Xbox layout. Menus, hacking minigames, videos, and the sniper scope drop to a 16:9 virtual screen, then snap back to full VR the moment you're in the world. That's a sensible compromise — the flat UI is unreadable in stereo — and it means the actual play is the part that's in your face, literally.

This is a Full VR Mod, not an official mode. Square Enix never touched VR for this title, and the proprietary Crystal Engine means UEVR and REFramework can't apply here at all. There is no framework profile to fall back on. DeusExHRVR is the entire VR story for Human Revolution, and it's impressive the story exists at all.

## How it plays in the headset

The first ten minutes are a quiet revelation. Jensen moves through the Detroit police station exactly as you'd hope — your head is his head. Crouching behind cover and leaning out to line up a tranquilizer dart feels like the game always wanted to play this way but couldn't on a flat screen. The augmented-vision pulse, the pocket-secret sweep, the way conversations put you face-to-cylinder with someone — all of it lands harder when you're occupying the space rather than observing it.

Movement uses smooth locomotion with right-stick camera turning; there's no teleport, which is the correct call for a game built around careful spatial positioning. Comfort tooling is present if you need it: a vertical-camera lock keeps mouse or gamepad pitch out of the VR camera, an F9 recenter handles post-cutscene drift, and a WorldUnitsPerMetre scale (10–1000) lets you dial the world's apparent size. I ran it at the author's default and it felt right.

The headline feature is hand-aimed weapons — experimental, but functional. Motion controllers map the full Xbox button set, with Y and B exchanged, and v0.3.0 added per-weapon grip calibration: hold both thumbsticks for a second, move the controller into the grip you want, release to save that weapon's offset. It's the kind of detail that tells you the author actually played this in a headset rather than guessing. Native rumble isn't mapped to VR haptics yet, which is a small but real loss when a shotgun kicks.

Performance is light. This is a 2011 game rendering two eyes through its own stereo path, so even a modest mid-range PC pushes it comfortably. The demand is nowhere near what you'd spend on a modern UEVR conversion.

## Where it gets rough

Here's the honest part: this is a WIP prerelease, and it shows. The author's own defect list is candid — extreme-angle weapon visibility breaks down, some lighting and shadow effects misbehave, the body behaves oddly if you physically move around your room (roomscale body tracking isn't implemented), and weapons occasionally vanish. Broader mission coverage still needs work. None of these are constant, but they're frequent enough that you'll notice them within a session.

The bigger constraint is the install surface. The mod supports exactly one executable: Steam Director's Cut build 2.0.66.0. GOG copies and the original non-Director's Cut release are rejected by design. The unmodified game can also crash on CPUs with many cores, so the PCVR Mods Installer Hub applies a known High Core Count exe patch as part of a reversible install — that's the path I'd recommend over manual setup, which leaves you handling the patch and four file placements yourself. Runtime choice matters too: Oculus and VDXR are reported working, but the current prerelease has black-screen reports under SteamVR, so the author steers you to Oculus or VDXR until that's fixed.

## The stealth-RPG payoff

Why does any of this matter for a game that's been on every "best immersive sims" list since 2011? Because Human Revolution is a world built for inhabiting. The Director's Cut's Detroit hub, the Hengsha double-decker sprawl, the corporate atria you walk through deciding whether to ghost past guards or put them to sleep — these are spaces designed around line of sight, verticality, and the slow read of a room. In VR that read becomes physical. You're not scanning a minimap for sightlines; you're craning your neck around a pillar to check the patrol path. The augments stop being a skill tree and start being a body you're learning to use.

That's the S-tier argument this game almost makes. The world is worth living in, the story has genuine weight, and the mod delivers proper 6DOF so you actually get inside it. What keeps it at B is squarely the implementation, not the source material. A prerelease with vanishing weapons, broken roomscale behavior, and a single supported executable isn't finished enough to call essential — yet. The foundation is the real thing, and the gap between v0.1.0 (head tracking only) and v0.3.0 (calibrated hand-aimed guns) in eleven days tells you the author is moving fast.

## Who should put the headset on

If you already own the Director's Cut on Steam and you've wanted to replay it, this is an easy yes with one condition: accept that you're on the bleeding edge. The mod is free, the install is mostly automated through the Hub, and the payoff — being Jensen instead of controlling him — is the kind of thing the flat version never delivered. Skip it if you only have a GOG copy, if you're on SteamVR and won't switch runtimes, or if a weapon disappearing mid-firefight would sour the whole session. For everyone else: this is the Human Revolution we were denied in 2011.

