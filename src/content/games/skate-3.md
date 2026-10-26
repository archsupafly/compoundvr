---
title: "Skate 3 VR"
description: "A community mod rebuilds Skate 3 as a first-person VR skate session — tracked hands, full-body IK, and Port Carverton at eye level."
flatReleaseDate: 2010-05-11
vrReleaseDate: 2026-09-01
lastUpdated: 2026-09-01
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Intense
performance: Moderate Demand
supportStatus: Active
genres:
  - Skateboarding
  - Sports
  - Sandbox
technicalTags:
  - Full VR Mod
  - Recompilation
  - OpenXR
experienceTags:
  - First-Person
  - Tracked Hands
  - Sandbox
tier: B
verdict: "Skate3VR is a genuine first-person rebuild of Skate 3 with tracked hands and full-body IK — the most surprising VR transformation of a console-only game I've tried this year. The setup wall, a broken tutorial, and a camera that occasionally snaps out of first person are real caveats, but if you already own the game and can mod, it's worth the climb."
heroImage: /images/games/skate-3-vr-hero.jpg
modDownload:
  url: "https://github.com/whachuvr/Skate3VR/releases"
  label: "Download Skate 3 VR Mod"
  note: "Created by whachuvr"
sources: "Skate3VR GitHub repository and v0.1 release notes (whachuvr); skate3recomp recompilation project via recomp.gg; andrewnakas/skate3-quest-ar releases; YouTube VR coverage from Syphrus, Nightspeeds, NotAGameAddict, and ThatDankCheese; r/Skate3 and r/VRMods community sweeps; Flat2VR Discord."
---

## The line you couldn't see before

I dropped into Port Carverton last week and for the first time in sixteen years I was standing in it. Not watching a skater from behind a third-person camera — standing on the board, hands on the trucks, the city spreading out at eye level. Skate 3 in VR isn't a remaster or a port someone at EA signed off on. It's a community mod called Skate3VR, and it does something I didn't think was possible for a 2010 console game: it puts your actual body inside the world.

Skate 3 shipped in 2010 on Xbox 360 and PS3 and never got an official PC release. The flat version has lived a long second life through emulation and, more recently, a native x86 recompilation (skate3recomp) that builds the game as a real PC executable. Skate3VR is a community mod that takes the natively-PC-recompiled Skate 3 and wraps it in OpenXR, first-person skating, and your own hands. That's a Full VR Mod in the real sense — substantial community VR work with tracked hands and full-body IK. You're not watching a stereoscopic video of the game. You're in it.

## How you actually get in

Getting there is the tax. This isn't a store-page download. You pull the Skate3VR release from GitHub, you supply your own legally obtained Xbox 360 Skate 3 ISO, you run the setup wizard to install Title Update 3, and you launch through Run-VR.bat, which flips the game into DirectX 12 and turns the VR flags on. You need a Windows PC with a DX12-capable GPU and an active OpenXR runtime. None of that is hard if you've modded a game before, but it's a wall if you haven't — there's no installer hub holding your hand, and the README assumes you know what an OpenXR runtime is.

A Quest headset plugged into a PC runs the same build, so the door's open there too. There's also a separate standalone Quest AR alpha from another developer, but that's its own install with its own data-import step and a much earlier state — I'm not counting that as the main way to play it in VR, and you should confirm its current build on the Flat2VR Discord before touching it.

## What it feels like to skate

Your hands are tracked. That's the headline. When you're carrying the board, it sits in your hands; when you push off, your hands move with the motion; when you're riding, they're down at the trucks like you're actually holding a deck. Full-body IK means your arms and torso follow you into the world, and for the first ten minutes I just pushed around downtown popping tiny ollies because the simple act of seeing my own hands on a skateboard in Port Carverton was enough to sell it.

So your body is in the world and your thumbs still do the flipping. The trick system is still Skate 3's right-stick flicks — moving your hands doesn't replace the stick inputs for flips, grabs, and spins. What the motion controllers add is presence, not a new control scheme: you feel like a person on a board, even though the actual tricking is still thumbwork. That's a real distinction and it's worth being straight about it. This is first-person skating with your body present, not a motion-controlled skate sim where you swing your arms to flip.

## Where it breaks

It's v0.1. The seams show, and a few of them are more than cosmetic. Coach Frank's Skate School tutorial is unfinished — board ownership bugs mean the early lessons don't behave, and you'll want to skip the tutorial and free-skate instead. After a respawn or a board remount the camera can snap back to third person, which yanks you out of first person and back into spectator mode on your own character; the workaround is a quick Y-cycle to force it back. Riding up high walls needs camera refinement — the view gets twitchy at the top of big drops. And building entry, one of Skate 3's signature bits, is still rough in VR.

None of those are death blows. The core free-skate loop — pushing, ollieing, hitting spots, stringing lines — works, and it's the part that matters. But this is early software, and the bugs interrupt the spell at exactly the moments you're starting to believe it.

## Performance

Performance sits at moderate demand: it's a recompiled last-gen game rendering in stereo, so a mid-range PC handles it without the overhead UEVR-style injectors pile onto modern titles. The README doesn't list comfort toggles yet, and first-person skating at speed is inherently comfort-intense — but your locomotion is your own pushing and carving, not forced camera flight.

## The rebuild is real

If you already own Skate 3 and you've modded a game before, this is the most surprising thing I've put a headset on this year. It's a genuine first-person rebuild of a game that never had a PC version, let alone VR — tracked hands, full-body IK, and Port Carverton at eye level. The caveats are real: the setup wall, a broken tutorial, a camera that occasionally ejects you from first person, and trick input that stays on the stick. But the feeling of standing on your own board in that city is something the flat game never gave you.

Multiple VR creators have covered it with enthusiasm, and the standalone Quest side is moving too. If you've ever wanted to know what Skate 3 feels like from the inside, this is the moment to find out, because it's brand new and still moving.
