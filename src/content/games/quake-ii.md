---
title: "Quake II VR"
description: "The 1997 shooter classic finds new life in headsets, but not all paths are equal — the standout is a standalone port that makes Strogg hunting feel surprisingly native."
lastVerified: 2026-04-30
featured: false
routeType: "Full VR Mod"
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Intense
performance: Efficient
supportStatus: Stable but Quiet
genres:
  - First-Person Shooter
technicalTags:
  - Source Port
  - Sideloading Required
experienceTags:
  - Classic
  - Fast-Paced
  - Sci-Fi
tier: B
verdict: "Quake II VR is a solid B-tier experience: the underlying game is a landmark FPS, and the Quest standalone port by Team Beef delivers genuine motion-controlled Strogg-slaying with enough polish to feel modern. The PCVR Q2VR mod is functional but archived and lacks the hand presence depth of contemporary VR mods. For Quest owners willing to sideload, this is one of the better classic shooter ports available. For PCVR users, it is playable but shows its age."
heroImage: /images/games/quake-ii-vr-hero.jpg
flatReleaseDate: 1997-12-09
vrReleaseDate: 2013-12-10
sources: "Research conducted via dghost.net project page, GitHub repository (dghost/quake2vr), SideQuest store page and community reviews, Polygon coverage (2014), UploadVR coverage, Holochip Corporation website, VorpX forums, Reddit community reports (r/OculusQuest, r/virtualreality), and NVIDIA Quake II RTX documentation. No direct testing performed."
---

# Quake II VR

The first time you step into the Strogg processing plant and actually *look up* at the hanging machinery, something clicks. Quake II was built for CRT monitors the size of microwave ovens, yet its industrial sci-fi architecture — all rusted corridors, pulsing energy conduits, and alien bulkheads — translates surprisingly well to a headset. The scale feels right. The claustrophobia feels right. Even the chunky 1997 weapon models feel right when they're tracking your actual hands.

But here's the thing: getting there depends entirely on which path you take. Quake II has multiple VR options, and they are not created equal. One is a genuinely good standalone port. Another is a functional but aging PC wrapper. A third is basically a tech demo. Know which one you're signing up for before you start copying files around.

## Three Very Different Ways to Play

**PCVR: Q2VR by Luke Groeninger**

The original Quake II VR mod, forked from KMQuake II, has been around since 2013. It natively supports Oculus Rift and SteamVR-compatible headsets, offers decoupled view-and-aiming, and includes some genuinely forward-thinking comfort features like HUD counter-rotation to reduce simulation sickness. The audio layer uses OpenAL with HRTF support, which means spatial sound actually works in a way that helps you locate Strogg around corners.

What it does *not* offer is the deep hand presence that modern VR mods have trained us to expect. You can point-and-shoot with VR controllers, but the weapon model stays centered — there's no physical weapon tracking, no holster reloading, no throwing grenades with a natural motion. Movement is thumbstick-based, and while it works, it feels more like "Quake II with a VR view" than "Quake II rebuilt for VR." The GitHub repository was archived in January 2021, and the last release (v1.9.3) dates to that same window. It still functions, but don't expect updates, bug fixes, or modern runtime compatibility guarantees.

**Quest Standalone: Quake2Quest by Team Beef**

This is the standout option. Built on the Yamagi Quake 2 engine and released via SideQuest in late 2019, Quake2Quest brings fully tracked weapons, high-resolution texture upgrades, and 6DoF movement to standalone headsets. The weapons actually follow your dominant hand. You can physically duck behind cover in your playspace. The visual enhancements — improved models, lighting tweaks, better effects — do meaningful work making a 1997 game readable on a Quest display.

The catch is the setup dance. You sideload the APK via SideQuest (or similar), then manually copy your `pak0.pak` and `pak1.pak` files from a purchased PC copy into the right folder on the headset. Want the soundtrack and cutscenes? Copy those too. It's not hard, but it's not frictionless. Team Beef has remained active — they added a new developer in late 2024 and have stated plans to migrate their ports to OpenXR for future-proofing. For a sideloaded classic port, the support posture is better than you'd expect.

**Quake II RTX VR by Holochip**

NVIDIA's ray-traced remaster is a gorgeous technical achievement on flat screens, and Holochip demonstrated VR integration using OpenXR at SIGGRAPH 2023. In practice, this is not a consumer-ready VR option as of 2025. It requires building from source, developer tooling, and a level of technical commitment that puts it well outside what most players will attempt. Treat this as a curiosity, not a viable way to play.

**VorpX Injection**

VorpX supports Quake II via its injection driver, offering stereoscopic 3D and head tracking. It does not provide motion controls, hand presence, or any VR-native interaction. You are playing the flat game with depth and headlook — functional, but not transformative. Given that native ports exist, VorpX is only relevant if you specifically want the RTX remaster visuals in some form of VR, and even then, the Holochip path (frustrating as it is) offers more native integration.

## How It Actually Plays

On Quest, Quake2Quest feels surprisingly natural. The railgun charges in your hand. The shotgun pumps with a wrist flick. The super shotgun's double-barrel spread has real weight when you're physically aiming it at a approaching Berserker. Room-scale movement means you can sidestep fire, lean around corners, and physically crouch behind barriers. The game's slower, heavier pace compared to the original Quake actually helps here — you're not bunny-hopping at light speed, so the VR locomotion feels less destabilizing.

That said, Quake II is still a fast shooter. Strogg come at you in waves, projectiles fill the screen, and the dodge-and-shoot rhythm demands quick turns. Snap turning is available for those who need it, and smooth locomotion is the default. If you're sensitive to motion sickness, the industrial corridors with their tight sightlines and sudden combat encounters will test your tolerance. This is not a gentle introduction to VR.

The campaign is fully playable start to finish on Quest, including both mission packs if you have the files. Multiplayer is not a focus for the port, but the core single-player experience — the entire reason Quake II matters — is intact.

On PCVR via the Q2VR mod, the experience is more sedate. The decoupled aiming works well: look one direction, shoot another. The HRTF audio is genuinely impressive for a 2013-era mod. But without physical weapon presence, without tracked hands, and with archived code that predates modern OpenXR runtimes, it feels like a historical artifact rather than a current recommendation. It works. It's free. It just isn't exciting next to what the Quest port achieves.

## The Verdict

Quake II earns its B-tier honestly. The underlying game is a foundational FPS with atmosphere and weapon design that still hold up. The Quest standalone port by Team Beef is the way to play it in VR today — tracked weapons, visual upgrades, full campaign, and a setup process that's annoying but not unreasonable. For Quest owners who don't mind sideloading, this is one of the best classic shooter ports available, sitting comfortably alongside Team Beef's other work.

The PCVR picture is weaker. The original Q2VR mod was pioneering for its era but is now archived and outpaced by modern VR expectations. There's no equivalent of the deep VR-native rebuild that Quake received from Vittorio Romeo's mod. If you're strictly PCVR, Quake II in VR is a nostalgia trip with competent aiming and good audio — worthwhile for fans, but not essential.

Play this if you want a solid classic FPS in standalone VR with actual motion controls. Skip it if you need plug-and-play simplicity, if you're highly motion sensitive, or if you're expecting the hand-presence depth of the best modern VR mods. The Strogg are waiting, but they don't care how much setup you endured to face them.
