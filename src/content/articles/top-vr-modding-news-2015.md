---
title: "Top VR Modding News of 2015: The Year Flat-to-VR Went Mainstream"
description: "2015 was the year VR modding exploded — from VorpX adding GTA V support to Dolphin VR letting you play GameCube in VR, here are the stories that defined the DK2 era."
pubDate: 2015-12-15
lastVerified: 2015-12-15
author: Richard
category: news
heroImage: /images/articles/top-vr-modding-news-2015-hero.jpg
tags: ['2015', 'vr-modding', 'vorpx', 'dolphin-vr', 'oculus-dk2', 'vireio', 'retro', 'flat-to-vr']
---

2015 was the year flat-to-VR modding stopped being a curiosity and started being a scene.

The Oculus Rift DK2 had been out since mid-2014, and by early 2015 a growing community of modders, injection driver developers, and VR enthusiasts had turned it into the platform where your existing PC game library could come alive in stereoscopic 3D. The tools were rough. The headsets were dev kits. Nothing "just worked." But that was the point — this was the frontier.

Here are the VR modding stories that mattered in 2015.

## 1. VorpX Adds GTA V Support — Hours After PC Launch

The biggest flat-to-VR moment of 2015 happened in April. Grand Theft Auto V finally landed on PC on April 14th, and within hours VorpX had a working profile for it. VorpX 0.8.1 shipped with GTA V support in Z3D (geometry-reconstructed stereo 3D) mode, letting DK2 owners step into Los Santos in stereoscopic 3D with headtracking.

Was it full VR? No. It was injection-driver VR — headtracking mapped to mouse look, no motion controls, plenty of jank. But the cultural moment was enormous. GTA V was the biggest game in the world, and you could play it in VR *the same day it launched on PC*. That sent a clear signal: if you wanted VR and were willing to tolerate compromises, the injection driver community was moving fast.

A modder named Falandorn also released a separate GTA V headtracking mod that hooked directly into the game's scripting API for smoother DK2 integration, showing that the community wasn't waiting for official support.

## 2. Dolphin VR Makes GameCube and Wii Playable in VR

2SDShyuan's Dolphin VR fork — a modified version of the Dolphin emulator with Oculus Rift DK2 and HTC Vive support — hit its stride in 2015. The project had been building momentum, and by April 2015 Dolphin VR 4.0-5286 was the stable release, letting you play *The Legend of Zelda: The Wind Waker*, *Super Mario Sunshine*, *Metroid Prime*, and dozens of GameCube/Wii titles in VR with headtracking.

This was a different kind of flat-to-VR than VorpX. Where VorpX injected stereo 3D into PC games designed for monitors, Dolphin VR leveraged the emulator's deep access to the game's rendering pipeline to produce proper stereoscopic output. The results varied wildly — some games looked incredible, others were nausea fuel — but the concept was proven: emulation + VR was a viable path.

## 3. PPSSPP VR Brings PSP Games to Your Face

In October 2015, CarlKenner (the same developer behind Dolphin VR) released PPSSPP VR, a fork of the PPSSPP PlayStation Portable emulator with Oculus Rift DK2 support. *Monster Hunter Freedom Unite*, *Wipeout Pulse*, *Crisis Core: Final Fantasy VII* — all suddenly playable on a virtual big screen, or with stereoscopic 3D for titles that supported it.

PSP games were never designed for VR, but their lower polygon counts and simpler rendering actually worked in their favor. On a DK2, the visual fidelity matched the headset's capabilities. PPSSPP VR was a quieter release than GTA V on VorpX, but it proved that the emulator-VR model wasn't a one-off.

## 4. VorpX Gets DK2 Positional Tracking and a Flood of Updates

2015 was the year VorpX became genuinely usable. Version 0.7.1 in early 2015 added initial DK2 support with positional tracking — a massive upgrade from the DK1's rotational-only tracking. A Skyrim positional tracking demo video made the rounds, showing the Elder Scrolls in VR with full 6DOF head movement for the first time.

By October, VorpX 0.8.1 had shipped with the GTA V profile, and throughout the year the driver accumulated support for dozens of new titles including *Dying Light*, *Alien: Isolation*, *Far Cry 4*, *Life Is Strange*, and *The Witcher 3* (the latter launching in May 2015). VorpX wasn't cheap at €39.99, but for the DK2 faithful, it was the single most important tool in the flat-to-VR toolbox.

## 5. Vireio Perception Keeps the Open-Source Flame Alive

While VorpX went commercial, Vireio Perception remained the free, open-source alternative. In 2015, Vireio was still in its 2.x line, supporting DK2 in Extended Mode with a more limited game roster than VorpX. The project was slower-moving — maintained by community contributors rather than a dedicated developer — but it mattered. Vireio proved that flat-to-VR wasn't locked behind a paywall.

The MTBS3D forums (Meant to Be Seen), founded by Neil Schneider, were the gathering place for Vireio users and the broader stereoscopic 3D community. If you were modding games into VR in 2015, you were on MTBS3D.

## 6. The Helix Mod / 3DMigoto Scene Levels Up

The shader-fixing community — centered around Helix Mod (blogspot) and DarkStarSword's 3DMigoto toolkit — had been doing stereoscopic 3D fixes for nVidia 3D Vision for years. In 2015, that work became increasingly relevant to VR because VorpX's Z3D and Geometry 3D modes relied on the same stereoscopic rendering correctness that 3D Vision fixes addressed.

Key 2015 Helix Mod releases included fixes for *Dying Light* (February), *Life Is Strange* (ongoing through episodes), and *Far Cry 4*. These fixes resolved rendering errors like incorrect shadows, broken reflections, and 2D HUD elements that ruined the stereo 3D experience. For VorpX users, a good Helix Mod fix could be the difference between "technically works" and "actually playable."

## 7. Minecrift Continues Pushing Minecraft VR

The Minecrift mod — a community-built VR implementation for Java Minecraft — continued active development through 2015, adding DK2 support and refining the VR experience. Minecrift was notable because it wasn't an injection driver; it was a proper mod that added VR rendering directly into Minecraft's codebase. That meant full headtracking, stereo 3D, and even experimental motion control support — far beyond what VorpX could offer for Minecraft.

Oculus would announce at Connect 2 (September 2015) that an official Minecraft VR edition was coming to the Rift in 2016, but throughout 2015, Minecrift was the way to play Minecraft in VR.

## 8. Oculus Rift CV1 Announced — Q1 2016 Ship Date

On May 6, 2015, Oculus officially revealed the consumer Rift (CV1) design and confirmed Q1 2016 shipping. For the modding community, this was the signal that VR was about to go from developer kits to consumer hardware. The implications were clear: the rough, DK2-era injection drivers and community mods would need to work with a new runtime, new tracking, and new expectations from users who weren't developers.

At Oculus Connect 2 in September 2015, Oculus also announced the consumer Samsung Gear VR at $99 and a Minecraft VR edition for Rift — both signs that the platform was expanding beyond dev kits.

## 9. The HTC Vive Announced, Changing the Hardware Landscape

Valve and HTC announced the Vive in March 2015, with dev kits shipping later in the year. For the modding scene, this was significant: the Vive's room-scale tracking and motion controllers raised the bar for what "VR" meant. VorpX, Dolphin VR, and Vireio were all built around the seated, gamepad-driven VR model of the DK2. The Vive suggested a future where VR meant standing up, walking around, and using your hands — a standard that injection drivers couldn't meet.

This tension — between seated headtracking VR and room-scale interactive VR — would define flat-to-VR modding for years to come.

## The State of the Scene at Year's End

By December 2015, the flat-to-VR modding landscape looked like this:

- **VorpX** was the dominant injection driver, commercial and actively developed, with ~100+ supported profiles
- **Vireio Perception** was the open-source alternative, functional but slower-moving
- **Dolphin VR** and **PPSSPP VR** had proven the emulator-VR model
- **Minecrift** showed what was possible when a mod went beyond injection and into the game's code
- **Helix Mod / 3DMigoto** provided the shader fixes that made stereo 3D actually look correct
- **The Oculus DK2** was the headset of choice for modders, with CV1 preorders about to open
- **The HTC Vive** was on the horizon, promising a fundamentally different VR experience

The tools were rough, the results were inconsistent, and nothing "just worked." But 2015 was the year the flat-to-VR modding scene proved it was real. Every major approach that exists today — injection drivers, framework mods, emulator forks, full game mods — had a working representative by the end of 2015. The scene just needed better hardware and more developers to take it further.

Both of which were coming in 2016.