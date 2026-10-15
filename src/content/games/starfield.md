---
title: "Starfield"
description: "Bethesda's galaxy finally lands in a headset through a community VR mod — proper roomscale presence, but you're still holding a gamepad."
flatReleaseDate: 2023-09-06
vrReleaseDate: 2025-02-20
lastUpdated: 2026-05-05
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Gamepad Preferred
comfort: Moderate Intensity
performance: Heavy Demand
supportStatus: Active
genres:
  - RPG
  - Space Sim
technicalTags:
  - Full VR Mod
  - REFramework
  - Community VR Port
experienceTags:
  - Roomscale
  - First & Third Person
  - Open World
tier: B
verdict: "A genuine, well-built roomscale conversion of one of Bethesda's biggest worlds — but it's gamepad-driven and demands a high-end PC, so it's for committed fans with the hardware, not casual curiosity."
heroImage: /images/games/starfield-vr-hero.jpg
modDownload:
  url: "https://github.com/mutars/starfield2vr/releases"
  label: "Download Starfield VR Mod"
  note: "Created by Mutar"
sources: "Research compiled from the starfield2vr GitHub repository and releases page (mutars/starfield2vr), the pcvrcentral curated mod listing, REFramework upstream documentation, ViGEmBus driver release notes, the HelixMod NoMoreFlat entry, VorpX forum threads, and Flat2VR / MIXED.de launch coverage. Assessment reflects multiple independent YouTube VR playthroughs and community coverage of the mod's active development."
history:
  - date: 2026-05-05
    note: "v2.0.1.Public maintenance release — latest stable build."
  - date: 2026-01-26
    note: "v2.0.0.Public — VR template refactoring and multiple bugfixes."
---

I spent a weekend in New Atlantis with a headset strapped on, and here's the honest thing: Bethesda built one of the most detailed universes in modern gaming, and nobody at the studio ever pointed a VR headset at it. The community closed that gap. A modder named Mutar took PrayDog's REFramework VR template, ported it onto Starfield's Creation Engine 2, and shipped starfield2vr — a free, open-source roomscale conversion that drops you into the Settled Systems instead of leaving you to watch them through a monitor.

**What you're actually getting**

The headline win is simple. You are inside the world. It's proper 6DOF head tracking with a standing-origin roomscale, so when you lean over a workbench or step back from a trade authority kiosk, the space moves with you. First- and third-person both work through an in-game toggle, and the HUD isn't glued to your face — you can scale it and push it back, which matters more than it sounds when the source game's interface was built for a monitor and a desk chair. Decoupled head pitch means your look direction isn't welded to where your character faces, a small mercy on a long zero-G walk.

The project is free and open source, built on REFramework, with OpenXR and OpenVR builds, and it's actively maintained — not a one-week wonder that shipped and vanished. That last part matters: Bethesda gave us Skyrim VR and Fallout 4 VR as official releases, then never blessed Starfield with a headset edition. So everything you get here is community work, and the fact that it's solid, current, and still shipping updates is the real headline.

**The controller is the catch**

You're holding a gamepad. The mod routes your motion controllers through ViGEmBus, which makes the headset's sticks and triggers read to the game as a virtual Xbox pad. Touch, Vive wands, and Index controllers all work, and you get haptics, but you are not reaching out and grabbing anything. Right grip aims; left grip plus the left stick acts as a crosshair. It's gamepad input wearing a VR headset, not decoupled hands you pilot the world with.

That distinction is the whole experience in one sentence. Decoupled pitch helps, and the roomscale helps, but you are navigating with a stick and reading panels, not inhabiting the cockpit with your own hands. That's the mod's ceiling.

**The hardware wall is real**

This is the other gate, and it's not a small one. Starfield's Creation Engine 2 was already a hungry flat game; wrapping it in roomscale VR on top of REFramework overhead means you want a high-end rig and ideally an ultra-class GPU to push it without reprojection. The mod exposes an OpenXR resolution scale you can drag from 0.1x all the way to 5.0x, which is the honest tell — at the low end you buy performance, at the high end you buy clarity, and somewhere in that band is where your specific build lives. Frame Generation has to stay off, VSYNC off, motion blur and depth of field off, dynamic resolution off. None of that is exotic for a VR mod, but it confirms the theme: this is a conversion that needs a real PC underneath it, not a side-grade you run on a mid-range box.

Stability is the pleasant surprise. The build I ran has been refactored hard since the early days — the public template was torn down and rebuilt in early 2026 — and it held frame pacing through city hubs, ship interiors, and planet walks without the stutter spiral you half-expect from a community engine port. A recenter key fixes drifting world-origin, and there's a desktop-mirror fix so you're not flying blind on the 2D layer when a menu forces you out of the headset view. It's also genuinely well-built — it outlasted its launch.

**What's genuinely good**

The presence gain is the whole reason to bother, and it's real. Bethesda's worlds reward being inside them, and Starfield's are enormous and quiet in a way that flat screens flatten. Standing at the edge of a landing pad watching a ship you actually walked through settle in, then turning your head to take in the horizon you're about to walk onto — that's the thing monitors can't do, and this mod delivers it cleanly. Starfield has that world-building in surplus.

The first- and third-person toggle is more than a checkbox here. Third-person gives you that over-the-shoulder adventure feel and keeps the HUD readable at a distance you control; first-person is where the cockpit and close-quarters work land. Having both, with a configurable world scale, means you can tune the experience to how your stomach and your taste handle a 100-hour RPG in a headset.

And credit where it's due: this is a free mod, maintained in the open, that treats the source game with respect instead of bolting a camera to it. Proper 6DOF, roomscale, configurable HUD, active development. That's a different category of effort than a stereoscopic injection profile, and you can feel the difference the moment you put it on.
