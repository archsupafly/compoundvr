---
title: "Don't Hand-Build Your Skyrim VR Modlist — Install FUS (or Yggdrasil) and Learn the Three Mods That Change Everything"
description: "Skyrim VR is the best VR game most people play wrong. Stop hand-building a modlist. Install FUS through Wabbajack, then learn the three interaction mods that actually transform it: VRIK, HIGGS, and Spell Wheel VR."
pubDate: 2018-04-03
lastVerified: 2025-10-26
author: Richard
category: guide
heroImage: /images/articles/skyrim-vr-mods-guide-hero.jpg
tags: ['2018','skyrim','skyrim-vr','vr-modding','vrik','higgs','wabbajack','fus','guide']
history:
  - date: 2025-10-26
    note: Updated modlist recommendations and interaction-stack versions.
---

[Skyrim VR](/games/skyrim) is the best VR game nobody plays the right way. Bethesda shipped a flat, menu-driven port with floating hands and a world that never reacts to your body. The modding community fixed all of it years ago. The trap is that most players try to earn that fix by hand-building a modlist from scratch: two hundred downloads, a crash on launch, and a week of troubleshooting before they ever swing a sword in VR.

You don't need to do that. Install FUS through Wabbajack, or Yggdrasil if your hardware is weak, then understand the three interaction mods that actually transform the game: VRIK, HIGGS, and Spell Wheel VR. That's the entire path from "broken port" to "the reason VR exists."

## Why Hand-Building a Modlist Is a Mistake

A Skyrim VR modlist that feels native takes conflict resolution, load order knowledge, and VR-specific patches most flat-Skyrim guides never touch. The interaction mods alone each need specific dependencies and ini edits. Doing this by hand means debugging other people's configurations instead of playing.

The community already solved this. Curated Wabbajack lists package a tested, load-ordered, VR-tuned setup into one install. You get the result of someone else's week in about an hour. Use that head start.

## FUS: The Modular Baseline

FUS is the reference Skyrim VR list, built by Kvitekvist and distributed as an official Wabbajack modlist. It's modular by design, which is why it works for two very different players: people who want a finished, lore-friendly overhaul and never want to touch modding again, and people who want a clean foundation to build a personal list on top of.

It ships in three profiles you pick inside the mod manager:

- **FUS (green):** the basics. The actual essentials for Skyrim VR, including the core interaction mods below. This is the profile to pick if you plan to build your own list later.
- **FUS RO (blue):** adds the visual overhaul layer on top of green, so the world looks like a current-generation game.
- **FUS RO DAH (yellow):** adds the gameplay overhaul layer on top of blue, changing combat, progression, and systems.

There's also a FUS Heavy variant (Nexus #146198) for stronger hardware that wants maximum density. The split matters because you can start at green, confirm your rig runs it, then step up to blue or yellow.

## Yggdrasil: The Lower-Spec Path

If your machine can't carry FUS RO DAH, Yggdrasil VR (Nexus #73867) is the alternative. It's a curated list of around 1,200 mods aimed at making Skyrim VR balanced, challenging, varied, and immersive while staying playable on lower-spec configurations with good performance. It remains distributed through Wabbajack as a featured list.

One honest caveat: large curated lists move at the maintainers' pace, and I couldn't verify Yggdrasil's current maintenance status — check the list's standing on the Wabbajack gallery before committing a long playthrough to it. For a weaker PC, the performance headroom is usually worth the trade.

For the upscaling side of why these lists run as well as they do, see our [DLSS 5 breakdown for Skyrim VR](/articles/dlss-5-skyrim-vr).

## The Wabbajack Install Path

Wabbajack itself is free and open source. It reads a list file and reconstructs the exact mod setup on your machine without redistributing any mod files. The install flow for FUS or Yggdrasil is the same:

1. Own Skyrim VR on Steam and run it once so the base files are in place.
2. Download the Wabbajack list file for FUS (or Yggdrasil) from the Wabbajack gallery.
3. Unzip the list file and run it. Wabbajack opens and walks through the standard install.
4. Point it at your Skyrim VR folder and let it resolve the mods.

Nexus Mods accounts are free, but Wabbajack's download step has two speeds. With a paid Nexus Premium subscription, Wabbajack downloads every mod automatically. Without it, you click each download manually as the installer pauses. The free path works, it just costs you time and attention on a list with hundreds of files. I can't confirm the current Premium price here, so check Nexus directly if cost matters to you. Either way, Wabbajack does the load ordering and patching, which is the part you never want to do by hand.

## The Interaction Layer: VRIK, HIGGS, Spell Wheel VR

The visuals get the screenshots. These three mods get the "I can't go back" feeling. They're the reason Skyrim VR stops feeling like a port and starts feeling like you're inside the world.

### VRIK: Your Body Exists

VRIK adds full-body inverse kinematics. Your head, hands, and a tracked body position drive a visible avatar, so you can see your own arms, belt, and sheathed weapons, and NPCs can react to where your body actually is. It's the foundation mod: without it you're disembodied hands poking at a world that doesn't acknowledge you. FUS green includes it, and if you ever build your own list, VRIK goes in first.

### HIGGS: Your Hands Have Physics

HIGGS (Nexus #43930) gives your hands and weapons real collision. You can grab objects directly, two-hand a bow or sword for proper draw and block, and shove things around like the gravity-gloves mechanic from Half-Life: Alyx. Melee stops being a button press and becomes a physical motion. With VRIK placing your body and HIGGS giving your hands weight, the game's tactile layer is mostly solved.

### Spell Wheel VR: Kill the Menus

Spell Wheel VR (Nexus #47630) replaces Skyrim's flat spell and item menus with a radial wheel you summon and spin in VR. Select spells, weapons, potions, and food without ever dropping to a 2D menu. Menu-diving is the single biggest friction point in VR Skyrim, and this mod removes it. It's the quietest of the three in screenshots and the most relieving in daily play.

### A Note on PLANCK

PLANCK sits in the same interaction-physics family as HIGGS and ships inside FUS, so most players get it without a separate install. I'll flag the uncertainty plainly: I couldn't verify its exact function, authorship, or current maintenance status from public sources at write time. Treat it as part of the curated list's payload, not a mod to chase separately until you've confirmed the details on its Nexus page.

## Ordering Advice

If you're installing FUS, the order is already decided for you: the list loads VRIK, then HIGGS, then Spell Wheel as part of green. The advice that matters is for what you do next.

Start at FUS green. Play it. Feel what VRIK, HIGGS, and Spell Wheel each contribute before you add a single thing. Then, if you build upward:

- Keep the three interaction mods as the non-negotiable core. Nothing visual or content-related is worth breaking them.
- Step to RO (blue) for visuals only after green runs stable on your hardware.
- Step to RO DAH (yellow) for gameplay changes only after blue is stable.

Layer one dimension at a time so when something breaks, you know which step caused it. The lists are built to be expanded this way; fighting that order is how hand-built disasters start.

## Where to Start Tonight

Download Wabbajack, pick FUS green (or Yggdrasil if your PC is modest), and run the install. An hour of setup buys you VRIK's body, HIGGS's hands, and Spell Wheel's menus. That combination is the real Skyrim VR, and it's been one installer away the whole time.
