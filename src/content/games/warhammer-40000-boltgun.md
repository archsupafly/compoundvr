---
title: "Warhammer 40,000: Boltgun VR"
description: "A retro boomer shooter that becomes a fast, close-quarters purging fantasy the moment UEVR drops you inside the boltgun's muzzle."
flatReleaseDate: 2023-05-23
vrReleaseDate: 2024-01-01
lastUpdated: 2024-01-01
featured: false
routeType: Framework Only
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Stable but Quiet
genres:
  - First-Person Shooter
  - Boomer Shooter
technicalTags:
  - UEVR
experienceTags:
  - Motion Controls
  - Fast-Paced
  - Retro Shooter
tier: B
verdict: "Boltgun in VR is a genuinely fun, lightweight boomer shooter that puts you inside the 40K purging fantasy, held back by one unavoidable flaw: the guns are flat 2D sprites glued to your view. Recommended for shooter fans who want speed and presence over weapon fidelity."
heroImage: /images/games/warhammer-40000-boltgun-vr-hero.jpg
sources: "Research conducted via Wikipedia (engine, release date, platforms), pcvrcentral profile listings (LunchAndDinner and nemphis UEVR profiles, install difficulty, release date), Steam community forum (out-of-box UEVR and motion controls report), ReaperzVR Patreon profile notes (flat sprite weapons, lightweight performance), the UEVR-profiles index, and YouTube VR coverage from ReaperzVR, Waifu Enjoyer, VARIY, LunchAndVR, and Paradise Decay."
---

I spent a weekend with Boltgun in a headset, and here's the thing: this is the Doom-like the Warhammer 40,000 universe always deserved, and UEVR is what finally lets you stand inside it.

Boltgun is Auroch Digital's 2023 retro "boomer shooter" — a deliberate throwback to the 1990s first-person shooter, all chunky guns, swarming enemies, and gothic-industrial cathedrals built from rust and piety. On a monitor it's a loving homage. In VR it becomes something closer to the fantasy the setting keeps promising: you, a single guardsman, hip-deep in heretics, with a boltgun that throws explosions the size of your head.

The catch is how you get there. Boltgun has no official VR mode. The way in is UEVR — praydog's universal Unreal Engine VR injector. Because Boltgun runs on Unreal Engine 4 and puts you in a first-person camera, this is UEVR's best-case scenario: full six-degrees-of-freedom head tracking, native stereo rendering, and a working first-person view the moment you inject. You're standing inside it.

Getting it running is about as friendly as framework injection gets. You install UEVR from uevr.io, grab a community profile, launch the game, point the UEVR frontend at the running process, and inject. The community profiles are the real workhorses here: LunchAndDinner's build, which shipped in March 2024, takes nemphis's original profile and fixes the weapon sizing while adding head-following movement. Both are listed on the UEVR-profiles index. pcvrcentral rates the install "Easy install," and per-game tweaks live in a config folder under your AppData UnrealVRMod directory. Nothing about the setup requires compiling anything or editing engine files by hand.

And the motion controls are real. The out-of-box Steam report of "VR working perfectly" alongside controller aiming, and the 6DOF motion-control gameplay videos that surfaced right after UEVR went public, confirm it: on a current LunchAndDinner or nemphis-line profile you aim with the controllers, not a gamepad. Snap-turn and vignette sit in the in-game menu if the speed gets to you, but the smooth locomotion is exactly what a boomer-shooter audience wants — this is a genre built on moving fast and never stopping.

Where Boltgun earns its keep is speed. The level design is a series of interlocking arenas — narrow corridors that open into cavernous chapels, catwalk runs over vat pits, shrine rooms where the floor drops out if you stand still too long. In VR, the scale of these spaces finally reads the way the art direction intends. You feel the height of a vaulted ceiling because you're craning your neck at it. You feel a shotgun heretic flank you because you heard the step behind your left ear, not because a minimap pip moved.

The weapons sound enormous. The boltgun's report is a wet, percussive thump-crack that lands in your chest, and when you fire it in VR the recoil isn't a screen shake — it's your arms pushing back. The chainsword is a snarling, teeth-on-metal roar you swing with your whole shoulder. Auroch built a game about feeling like a Space Marine, and the headset is the first version of Boltgun that delivers on the promise honestly.

The weapons are flat 2D sprite animations in VR.

This isn't a profile bug or a settings miss — it's baked into how Boltgun renders its guns. The game draws its weapon viewmodels as sprite-based animations, so in the headset your boltgun and chainsword stay pinned flat against your view instead of existing as real 3D objects you can move your head around. Two independent sources — a Steam forum poster and the ReaperzVR profile notes — confirm this separately, and they're permanent. In a fully realized 3D world, the gun in your hands is a flat sticker of one, glued to your view.

It reads as wrong the first time you notice it. You're sweeping a bolter across a line of cultists, the muzzle flash pops, and your peripheral vision catches that the weapon itself has no depth. It's a small thing and then it isn't, because you're looking at it the entire game. Boltgun is a shooter, and the shooter is the part you stare at.

What keeps Boltgun in the "play it" column anyway is that everything around the gun is so committed. The enemy variety — cultists, daemons, armored elites that take a magazine and a prayer to drop — pushes you to keep moving, and movement is where VR pays off hardest. Dodging a projectile around a pillar by leaning, then snapping a headshot on the recoil, is the loop the game lives for, and it works in the headset better than it has any right to.

Performance helps. Boltgun is a lightweight title — the sprite-based rendering that curses the weapons also keeps the GPU load low — and the ReaperzVR notes flag it running light even with the headset overhead. On a mid-range PC this is a smooth, reprojection-free experience at full framerate. The single-player campaign is complete and substantial; this isn't a tech demo with three rooms. You get the full purging arc, start to finish.

The honest ledger:

**Why it works** — full 6DOF with working motion controls out of the box on current profiles; blistering, physical close-quarters combat; a complete campaign; and a game light enough to run clean on modest hardware.

**Why it hesitates** — the flat 2D weapon sprites are unavoidable and visible in every single firefight; this is framework injection, so you're self-managing the profile and any engine updates can break the injection until the community catches up; and there is no native or console VR path, so it's PCVR or nothing.

None of that is a dealbreaker for the right player. The flat gun is a blemish you learn to ignore the way you ignore film grain, because the act of playing — the speed, the space, the weight of the fight — is the real draw, not the model in your hands. This is not Half-Life: Alyx depth. It's a boomer shooter, its ambitions are tight and its one visual flaw is unavoidable. What it sets out to do — make you feel like a guardsman clearing a cathedral with a gun that roars — it does, and it does it on hardware that doesn't need to be a super computer.

If you came to Boltgun for the Warhammer power fantasy and you've got a PCVR rig, this is an easy yes with one eye open. Grab a current LunchAndDinner-line profile, confirm the build on the Flat2VR Discord, and go purge something. The sprite guns are the price of admission. The purging itself is the reason to stay.
