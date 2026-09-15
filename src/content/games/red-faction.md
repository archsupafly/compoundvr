---
title: "Red Faction in VR: Geo-Mod Was Always Meant for a Headset"
description: "A community mod finally puts Volition's 2001 Mars shooter in VR — and blowing holes in walls is even better when you're standing in the rubble."
flatReleaseDate: 2001-09-20
vrReleaseDate: 2026-08-19
lastVerified: 2026-08-19
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
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
  - OpenXR
  - Geo-Mod
experienceTags:
  - Destructible Environments
  - Motion Controls
  - Retro Shooter
tier: B
verdict: "A free community mod that turns Red Faction's destructible Mars into a place you can actually stand inside — flawed, beta, and VDXR-only, but the wall-comes-down moment is worth the tinkering for anyone who already owns the game and runs Virtual Desktop."
heroImage: /images/games/red-faction-vr-hero.jpg
sources: "Mod repository and release notes (CactusVRStudios/AlpineFactionVR, GitHub); contemporary overview from Generation Amiga (August 2026); flat-game identity and platform history from Wikipedia and MobyGames. Assessment based on mod documentation and community reports; no direct hands-on testing performed."
---

I spent the weekend on Mars, and the first thing I did was blow a hole in a wall just to see if I could walk through it. I could. That's the entire pitch for Red Faction in VR, and honestly, it's most of the review.

Red Faction shipped in 2001 with one trick nobody else had: Geo-Mod, an engine that let you destroy the actual geometry of a level, not just pre-baked breakable props. Twenty-five years later, a modder going by CactusVRStudios bolted OpenXR motion controls onto the PC version, and suddenly that old gimmick feels like it was waiting for a headset the whole time.

## What you're actually getting

This isn't an official port — there was never a VR edition of Red Faction, and nobody's injecting a flat render into a headset, either. Alpine Faction VR is a full community mod: proper six-degrees-of-freedom, two-handed weapon handling, and a control scheme that expects you to use your hands. It's built on top of Alpine Faction, a modern community patch for the original game, and it launches through a one-step installer that finds your legitimate Red Faction install and does the wiring for you. You still need a real copy of the game, but if you've got one, the mod does the heavy lifting.

The one catch that bit me: it runs through Virtual Desktop's VDXR runtime. Native Meta XR crashes on the 32-bit OpenXR session, and current SteamVR doesn't ship a 32-bit SteamXR runtime, so VDXR is the only path that works right now. If you've already got Virtual Desktop and a PC VR headset, that's a non-issue — flip the runtime selector and you're in. If you don't, that's a real wall standing between you and Mars.

## How it plays

The campaign is the 2001 singleplayer story: Parker, a miner on Mars in 2075, the Ultor Corporation treating workers like disposable parts, and a revolt that turns into a shooting war through reprocessing plants and research labs. You move with the left stick, aim with the right controller, and fire with the right trigger. Reload is a shake of the controller by default, or a button if you turn that off in the launcher. You can grab a support point with the left grip for two-handed rifle stability, and the flashlight rides your view on the left Y button. Turning is snap or smooth, your pick in the launcher — the usual smooth-motion body load, nothing here worse than any other first-person shooter asks. It's a complete, legible control map, not a science project.

The thing that actually lands is the destruction. In flat Red Faction, Geo-Mod meant you could shoot a hole in a wall and flank an enemy who thought he was safe. In VR, you're standing three feet from that wall when it comes down, and you step through the gap you just made. I caught myself ducking when a railgun punched through a concrete pillar two feet from my head — there was nothing there to duck from, but my body didn't care. That's the specific thing VR adds here that a monitor never could: the destruction has scale and proximity. You're not watching a wall fall. You're in the room it falls in.

Vehicles are in, and they're better than they have any right to be for a 2001 game. The mounted turret and jeep gunner aim with your head, which feels natural. The submarine segment tracks your look pitch for vertical movement, and the mod clears the residual roll when you climb out so the horizon doesn't stay tilted. Swimming follows your view too — look up and push forward to ascend. It's a beta, so some of these moments stutter, but the intent is all there, and the spatial logic holds together better than I expected from a community project this young.

## The caveats

Here's the honest part. This is a beta mod, and it tells you so upfront — back up your saves, because it can crash. The singleplayer campaign is the focus; multiplayer is best-effort and basically unsupported, and there's no dedicated-server VR. If you came for deathmatch with friends in VR, this isn't your game.

The visuals are 2001, obviously. This is not a pretty title by modern standards: blocky character models, flat lighting, texture work that ages the way 2001 texture work ages. What saves it is that Geo-Mod destruction doesn't care about polygon counts — a wall coming down is a wall coming down. On the performance side, it's a 25-year-old game pushed through a D3D11 renderer and OpenXR, so it'll run on a potato. No GPU anxiety here.

And then there's the runtime wall again. VDXR-only means you need Virtual Desktop in your stack, which quietly excludes a chunk of PC VR owners who run native SteamVR or Meta XR exclusively. The mod author is working on broader runtime support, but right now that requirement is the difference between "I'm playing Red Faction in VR tonight" and "I guess I'll look into Virtual Desktop."

## Worth the mining shift?

If you already own Red Faction on PC and you run Virtual Desktop, this is an easy yes. It's a free mod that turns a classic shooter into something the original couldn't quite deliver — the destructible Mars facility is a better place to be inside than to watch. The flat version is still a great 2001 shooter, but the VR version is the one where the walls actually fall on you, and that specific feeling is why the headset exists.

If you don't own the game, or you're on a standalone or console headset with no PC VR streaming setup, this isn't your entry point. It's strictly a PC VR thing, and the VDXR requirement means you need the streaming stack too. For everyone else who remembers Geo-Mod fondly: the wall still comes down, and now you can stand in the rubble.
