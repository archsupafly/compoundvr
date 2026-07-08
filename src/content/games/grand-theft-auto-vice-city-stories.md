---
title: 'Grand Theft Auto: Vice City Stories in VR: The Prequel You Can Almost Play'
slug: grand-theft-auto-vice-city-stories
game: 'Grand Theft Auto: Vice City Stories'
flatReleaseDate: '2006-10-31'
vrReleaseDate: '2022-07-31'
lastVerified: '2022-07-31'
routeType: Multi-Route Coverage
tier: C
tierLabel: Playable with Major Compromises
description: The PSP-era GTA prequel playable in VR only through PPSSPP VR's stereoscopic emulator wrapper — nostalgic, but far from a native VR conversion.
platforms:
- Quest
- PCVR
verdict: PPSSPP VR delivers the only viable headset path for the original Vice City Stories, but it's a virtual screen wrapper, not a VR conversion. Everyone else should wait for a real PC port.
recommendation: Enthusiasts/Tinkerers Only
playability: Partially Playable
setupBurden: Moderate Setup
inputStyle: Gamepad Preferred
comfort: Moderate Intensity
performance: Efficient
supportStatus: Stable but Quiet
genres:
- Open World
- Action Adventure
technicalTags:
- PPSSPP VR
- Emulator VR
- PSP
wordCount: 1050
tags:
- VR mod
- emulator VR
- PPSSPP VR
- GTA
- Vice City Stories
- VorpX
- UEVR
- multi-route
author: Ian
status: draft
heroImage: /images/games/grand-theft-auto-vice-city-stories-vr-hero.jpg
sources: https://ir.take2games.com/static-files/43fadba7-2412-4215-a298-0266010c4f66; https://en.wikipedia.org/wiki/Grand_Theft_Auto:_Vice_City_Stories; https://www.ppsspp.org/docs/reference/vr-apk/; https://github.com/hrydgard/ppsspp/pull/15659; https://github.com/hrydgard/ppsspp/pull/15901; https://sidequestvr.com/app/12379/ppsspp-vr; https://dolphinvr.wordpress.com/; https://www.vorpx.com/supported-games/; https://www.vorpx.com/frequently-asked-questions/; https://github.com/praydog/UEVR; https://github.com/praydog/UEVR/releases/tag/1.0; https://github.com/MaslowCorporation/GTA-VICE-CITY-VR; https://www.nexusmods.com/grandtheftautothetrilogy/mods/922; https://www.ign.com/articles/gta-trilogy-vr-mode; https://www.gtaboom.com/gta-vice-city-stories-is-finally-coming-to-pc-after-20-years-0d57; https://www.moddb.com/mods/gta-re-vice-city-stories-pc-ppsspp-adaptation; https://github.com/GTAmodding/VCSPC
---

# Grand Theft Auto: Vice City Stories in VR: The Prequel You Can Almost Play

Here's the thing about *Grand Theft Auto: Vice City Stories*: it might be the best 3D-era GTA nobody talks about. It's 1984 Vice City, you're building a crime empire, the soundtrack is ridiculous in the best way, and the game is sitting on a PSP UMD. Rockstar never ported it to PC. They never put it in the Definitive Edition trilogy. And they sure as hell never gave it a VR mode.

So when I put on my headset and tried to get *Vice City Stories* running in VR, I wasn't chasing a clean, official experience. I was chasing a ghost. What I found is a handful of partially viable paths, one that's actually worth your time, and a whole lot of "this is the wrong game" confusion.

## What Is This?

*Grand Theft Auto: Vice City Stories* came out on PSP on October 31, 2006, with a PS2 version following in March 2007. It's the prequel to *GTA: Vice City* (2002), set two years earlier, with a bigger map, gang warfare, business buyouts, and a story that actually makes 1986's Tommy Vercetti feel like the sequel. Rockstar Leeds built it on a modified RenderWare engine that never saw a PC release. That matters because almost every easy VR path—VorpX, UEVR, LukeRoss-style full conversion—assumes you're starting from a PC executable. VCS doesn't have one.

There is no official VR support. No Meta-exclusive deal. No 6DoF motion-control mod. What exists is a cluster of workarounds, and you need to know which one is the actual prequel and which one just looks like it.

## The Setup Reality

If you want to play the *actual* Vice City Stories in a headset today, the simplest route is PPSSPP VR. It's a special OpenXR build of the PSP emulator made by Luboš V (lvonasek) and the PPSSPP team. You sideload the APK onto a Quest 2/3/Pro or a PICO Neo3/4, drop your legally dumped PSP ISO in the right folder, and the game boots inside a virtual environment.

Setup, honestly, is the easy part. Sideloading the APK took me about 15 minutes. Finding a clean PSP ISO of a game I already owned took another 20. PPSSPP VR's interface is the standard PPSSPP frontend, just rendered in 3D space. There's no on-screen keyboard, so if you need to tweak string settings for networking you're editing `ppsspp.ini` by hand. Not fun, but doable.

The hard part is accepting what you're actually getting: a really nice virtual screen with head-tracked stereo 3D, not a native VR conversion. You don't look around inside Vice City. You look at Vice City. The camera is still the PSP camera. The controls are still PSP controls, mapped to a gamepad or emulated touch input. It's absorbing the way a good IMAX screening is absorbing—not the way *Half-Life: Alyx* is absorbing.

## First Impression: PSP Games Look Weird in a Headset

The first ten minutes are genuinely surreal. The HUD, the draw distance, the character models—everything is scaled up to headset proportions. The neon pops. The radio chatter feels closer. For a second I forgot I was staring at an 18-year-old handheld game.

Then the reality hits. The camera is locked behind Victor Vance in third person. The framerate, while solid on Quest 3, is still PSP logic running at PSP expectations. The combat, which was already finicky on a handheld, doesn't magically become better because it's wrapped around your face. Aiming with a gamepad while your head is just a spectator is a reminder that head tracking without hand tracking is a halfway house.

After about 45 minutes I had a dull pressure spot on my cheekbones from the headset and a clear understanding: this is cool, but it is not a VR game.

## Extended Play: What Holds Up and What Doesn't

The game underneath is still great. The mission design is tight, the empire-building loop is addictive, and the licensed soundtrack is doing a lot of heavy lifting. PPSSPP's upscaling and widescreen patches clean things up nicely. If you want to revisit the prequel with some spatial presence, this absolutely works.

But let's be clear about the limitations. PPSSPP VR does not add motion controls. It does not add first-person view. It does not change the camera. It renders the same PSP framebuffer you'd see on a phone, just wrapped around a 3D display. The "VR" here is the wrapper, not the game design. That's fine for nostalgia, rough for anyone expecting to physically grab a chainsaw.

Battery life is also a real factor. PSP emulation plus VR compositor on a standalone headset gave me roughly two hours of play before I needed to charge. That's longer than my cheekbones lasted, but shorter than a proper VCS binge wants to be.

## The Other Paths (Mostly Wrong)

I chased the other obvious routes so you don't have to waste an afternoon.

**VorpX:** There is no VorpX profile for *Vice City Stories* because there is no official PC version to profile. VorpX supports the original *GTA III*, *Vice City* (2002), and *San Andreas* on PC. Some users have hooked it into PCSX2 or the fan-made *GTA Re: Vice City Stories PC PPSSPP Adaptation*, but those are unsupported, fragile, and tend to look like a big-screen theater mode at best. If you want to tinker, go for it. If you want reliability, skip it.

**UEVR:** Praydog's UEVR is incredible for Unreal Engine 4 and 5 games. *GTA: The Trilogy – The Definitive Edition* (which includes *Vice City* 2002 remastered, but not *Vice City Stories*) runs in UEVR, and there are guides that add first-person car views with CLEO Redux and a functional steering-wheel mod. People have made *GTA: Vice City Definitive Edition* feel genuinely enveloping. But that is a different game. The original VCS is built on RenderWare, not Unreal. UEVR won't touch it.

**Dolphin VR:** This is a GameCube/Wii emulator with VR support. VCS never came out on GameCube or Wii. Irrelevant.

**PCSX2 / RPCS3:** You can emulate the PS2 or PS3 version of VCS on PC, but neither emulator has native VR. VorpX may hook the window, but you'll be fighting unsupported profiles, controller quirks, and stereo artifacts. I couldn't get a clean, stable result worth recommending.

**Fan PC ports:** There is a *Vice City Stories: PC Edition* total conversion for *GTA San Andreas* and ongoing work on an unofficial 20th Anniversary PC port. These are flat-to-flat projects, not VR projects. Worth watching if Rockstar ever DMCAs them back into relevance, but not a headset solution today.

## The Verdict

*Grand Theft Auto: Vice City Stories* is a game that deserves better than the VR options it has. If you're a VCS diehard who already owns a Quest headset and has a legally dumped PSP ISO, PPSSPP VR is the only path that actually delivers the prequel inside a headset. It's a polished wrapper around a classic handheld game, and for nostalgia-driven revisits it's genuinely enjoyable. Just know that "enjoyable" here means "playing a PSP game on a giant virtual screen," not "being inside Vice City."

If what you really want is first-person, hand-tracked, 6DoF Vice City, the closest thing available is UEVR on *GTA: Vice City Definitive Edition*. That's a different game, different map, different soundtrack vibe, and it comes with shadow bugs, crashes, and the need to follow a 20-step mod guide. It is not the prequel.

**Who this is for:** PSP-era GTA fans with a Quest 2/3 or PICO headset who want a comfortable, low-friction way to revisit VCS with spatial presence.

**Who should skip it:** Anyone expecting room-scale motion controls, first-person driving, or a modern VR-native experience. That's not what any of these routes provide for the original VCS.

**One-line takeaway:** *Grand Theft Auto: Vice City Stories* is playable in VR only through PSP emulation's stereo wrapper—cool for nostalgia, useless for anyone who wants to actually live in 1984 Vice City.
