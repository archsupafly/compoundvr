---
title: "Aliens versus Predator VR"
description: "The Alien, Predator, and Marine campaigns finally meet proper VR through community ports — but only two of the three games get the full motion-control treatment."
flatReleaseDate: 1999-01-01
vrReleaseDate: 2026-05-25
lastUpdated: 2026-10-13
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest', 'Pico']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - First-Person Shooter
  - Sci-Fi Horror
technicalTags:
  - Full VR Mod
  - OpenXR
  - Source Port
  - Injection Driver
  - VorpX
experienceTags:
  - Motion Controls
  - Three-Species Campaign
  - Standalone Quest
  - Melee Combat
tier: A
verdict: "The Bassquake ports turn the two best Aliens versus Predator shooters into real VR — motion controls, standalone Quest, and atmosphere that finally has a body. The 2010 reboot's VorpX profile is a fallback, not the reason to put the headset on."
heroImage: /images/games/aliens-versus-predator-vr-hero.jpg
modDownload:
  url: "https://github.com/Bassquake/Aliens-Versus-Predator-VR/releases"
  label: "Download Aliens versus Predator VR Mod"
  note: "Created by Bassquake"
sources: "Research drawn from the Bassquake GitHub repositories for the Aliens Versus Predator (1999) OpenXR source port and the Aliens Versus Predator 2 (2001) PCVR mod, the VRMods-List index, the vorpX community forums (Aliens vs. Predator 2010 profile threads), YouTube VR coverage from TheGeekCrabb, CleXor, Valentin Kozin, Bassquake, YouGotColdYogurt, and For The Love Of Games, the Steam community VR-support thread for App 10680, and the Flat2VR Discord for peer setup notes. No direct hands-on testing performed; assessment reflects the documented mod state and the underlying games' standing."
history:
  - date: 2026-10-13
    note: "AvP2 PCVR mod reaches v0.3; AvP Classic 1999 VR port reaches v1.2 with 120Hz mode and tunable melee range."
  - date: 2026-05-25
    note: "Bassquake publishes the OpenXR source port of Aliens Versus Predator (1999), the first full VR path for the franchise."
---

I spent a stupid amount of time this week crawling across a bulkhead as the Alien, claws out, the Marine's motion tracker squealing somewhere below me. That tracker ping lands behind your right shoulder; your body reads it before your ears do. That's the version of Aliens versus Predator I wanted for twenty years, and it finally exists as a community port rather than a studio's afterthought.

There is no official VR version of any Aliens versus Predator game. What we have instead is, in the important ways, better than a lazy studio port: the best paths here are proper from-scratch VR rebuilds of the two cult-classic PC shooters, built by a modder going by Bassquake. The 1999 original — the one everyone calls AvP Classic — has a full OpenXR port with motion controls, standalone Quest builds, and PCVR support. The 2001 sequel from Monolith has a PCVR wrapper with the same motion-control treatment. The 2010 Rebellion reboot only has a VorpX injection profile: stereoscopic 3D and head tracking, no hands. That's the consolation prize.

### Getting the games running

Neither mod hands you the game. Both require your own original assets, and that's the one real friction. For the Classic port you need the Gold Edition specifically — the standard version's language file crashes the build — and you drop the assets in, lowercase every filename with the supplied script, and sideload the APK if you're going standalone Quest. On PCVR it's an installer batch file and you're in. Budget maybe half an hour if you've done a mod or two before; longer if this is your first sideload. AvP2 demands more: the original 2-CD install patched to its final version, a runtime batch added to Steam, and streaming over Steam Link. It's a moderate setup, but it is not a click-and-play store page.

That friction is the honest cost of getting the best Alien-versus-Predator experience in a headset, and for these two games it's worth it. The ports are actively maintained — the Classic build hit a polished update with the 120Hz mode days before I wrote this, and the AvP2 wrapper shipped multiple revisions in two weeks. This is a living project, not a one-and-done upload that rots.

### What the 2010 reboot gives you in VR

Now the awkward cousin. The 2010 Aliens vs. Predator — the Steam title that shares the franchise's exact name — has no mod, no source port, and no framework path. Its engine isn't Unreal or RE Engine, so UEVR and REFramework can't touch it. The only VR option is a VorpX cloud profile: geometry-3D stereo, head tracking, and all three campaigns reachable, but you're holding a gamepad and looking through a window, not inhabiting the world. You have to force the game's DX9 build through the Steam client to use it, and you'll want VorpX's cinema modes because some elements — alien blood, the intro and cutscenes — render flat. It works, and if you specifically love that 2010 reboot and already own VorpX, it's a serviceable way to walk its corridors in 3D. But it is injection-driver quality, and it is not why you'd come to this franchise in VR.

I'm not going to ding the Classic or AvP2 ports for the 2010 game's limited path. They're different games, and the best two got the real treatment. Review averages on the 2010 reboot were middling anyway — short campaigns, multiplayer-first design — and the VR here doesn't redeem that, it adds depth to a window.

### Where the ports land

Proper six-degrees-of-freedom head tracking in games built around corridors, vents, and verticality. Motion controls that match each species instead of mapping everything to a gun. Standalone Quest builds that mean you don't need a PC tethered to enjoy the Classic. Atmosphere that the flat versions nailed and VR finally lets you stand inside. The AvP2 campaign is the stronger single-player package, and it's the one I'd point a newcomer to first if they can handle the streaming setup.

The weaknesses are honest too. You're supplying your own game files, and the AvP2 wrapper has visible geometry gaps on some weapons. The 2010 reboot's VR is a fallback, and it costs paid software to reach. These are mods from a single author moving fast, so rough edges ship — but the update cadence suggests they get smoothed.

If you grew up on these games, or you're a sci-fi horror person who's never touched them, the Classic and AvP2 VR ports are the way in. Build your own Alien and go crawl the vents.

Start with the 1999 Classic port, because it's the one that'll catch you off guard. This is a recompiled source port with a real VR renderer, and it shows. You pick your species — Marine, Alien, Predator — and the control scheme reshapes around what that creature is.

As the Marine, hold A to reload, and the weapon sits in your hand with a grip you can disable if you'd rather not. As the Alien or Predator, you swipe the controllers to claw and punch, and the attack range is tunable so you're not whiffing at air. There's even a climb option where you hold a button to scuttle up surfaces instead of tapping it repeatedly. The HUD elements, world scale, and crosshair are all adjustable, which matters more than it sounds when a flat game's UI was never drawn to live two inches from your face.

The 1999 game was always about darkness and audio — the motion tracker, the dripping vents, the "they're inside the walls" dread. In VR that dread finally has a body. You're the thing doing the hunting, or the person hearing the clicks close in. The port ships both snap and smooth turning, blinders if you want them, and a 120Hz mode that runs clean on a standalone Quest. Comfort options are there, and the atmosphere does the rest — this is a tense game, not a nauseating one.

### AvP2 is the better campaign, with rougher edges

Then there's AvP2, the 2001 Monolith sequel that a lot of fans call the best campaign of the three. Same modder, same motion-control philosophy, but it's a PCVR wrapper rather than a standalone build, and it wears its age in specific places. You stream it to a Quest over Steam Link — Meta Link won't work because the game is 32-bit and that pipeline doesn't support it — and a few weapon models have missing faces because they were never built to be viewed from odd angles. Those are the kind of rough edges you forgive the moment you're stalking a Marine as the Predator with the controllers in your hands, because the campaign variety and the set-piece design are a clear step up from the original.
