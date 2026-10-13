---
title: "How to Play Castlevania on Quest for Free: Simon's Destiny Setup Guide"
description: "A free, fan-made first-person Castlevania runs on a standalone Quest through QuestZDoom. Here's the exact setup path, the free IWAD trick, and the caveat the breathless videos leave out."
pubDate: 2026-10-13
lastUpdated: 2026-10-13
author: Ian
category: guide
heroImage: /images/articles/castlevania-simons-destiny-quest-guide-hero.jpg
tags:
  - castlevania
  - quest
  - free
  - gzdoom
  - questzdoom
  - sideloading
  - fangame
  - setup-guide
sources: "batandy.itch.io/simonsdestiny (developer page); questzdoom.com (engine port, install steps, controls, performance); the ModDB QuestZDoom addon page; the r/QuestZDoom build note; the ZDoom forum release thread; Wikipedia Castlevania series facts; YouTube coverage (Johnny 5 Arcade, Pixelacos VR, TechHoller, CrbnBased, F guillotine). No hands-on benchmarking performed"
---

# How to Play Castlevania on Quest for Free: Simon's Destiny Setup Guide

There's a version of Castlevania you can play in first person, on a standalone Quest, for exactly zero dollars. Not a stream. Not an emulator stretched onto a flat screen. You're standing in Dracula's castle with the Vampire Killer in your hand, cracking it across a skeleton's ribs. That game is Simon's Destiny, a free fan-made rebuild of the 1986 NES original, and the Quest route into it is real. The setup is a short, specific sequence, and there's one honest caveat about what "free" actually means here that the breathless videos leave out.

## What Simon's Destiny actually is

Simon's Destiny is a non-profit fan game built on the GZDoom engine by a developer who goes by Batandy. It was announced and released in 2017, and its whole pitch is to reinvent the first NES Castlevania as a first-person, 3D, nostalgic-but-new game: Simon Belmont, the whip, the bestiary of bats and medusa heads and skeletons, the march through Dracula's castle. By most community write-ups the castle runs about six levels, and the combat is whip-centric melee with a few magical weapons tossed in. Konami's trademarks stay with Konami — this is a love letter, not a licensed product, and it's free.

The reason it matters for Quest owners is simple: GZDoom total conversions are content, not store apps. Playing Castlevania on Quest is an engine-port-plus-content-mod problem, not a purchase. That's also why it can be free — you're not buying a port, you're supplying a free engine and a free base game to run the fan content on top of.

## Why it runs on a Quest at all

The engine that makes this possible is QuestZDoom, the VR port of the LZDoom/GZDoom engine built by the Dr Beef / Team Beef group — the same people behind the standalone Quest ports of Doom, Quake, and Half-Life. Two facts about it decide everything that follows. First, it's built solely for the Oculus Quest and will not run on anything else, so this is a standalone-Quest guide, full stop. Second, it ships no game assets whatsoever — it's an engine, and to play anything you supply the content yourself.

That second fact is the whole trick behind "free." QuestZDoom can run without you owning a retail Doom, because the launcher downloads FreeDoom — a free, community-made base IWAD — directly in-headset. The fan Castlevania content then loads on top of that free base. The itch.io page for Simon's Destiny calls the game "completely standalone, only GZDoom required," yet also links a GOG Doom II purchase; the resolution is that a GZDoom total conversion still needs a base IWAD to boot, and on Quest the free path is FreeDoom rather than a retail Doom you pay for. You do need a base game to launch — you just don't have to buy one.

## The setup, step by step

You'll sideload two apps through SideQuest, the standard sideloading tool for standalone Android headsets. If you've never used it, the process is: enable developer mode on the Quest, plug in over USB, and drag-drop the APK — the QuestZDoom page points you at SideQuest specifically because it supports that drag-and-drop install. From there the sequence is:

1. Install **QuestZDoom** from SideQuest (it's listed as app 796 on the SideQuest store).
2. Install the **QuestZDoom Launcher** from SideQuest (app 802). This companion app, built by Grant Bagwell (BaggyG), is what pulls mod files and base IWADs down in-headset so you're not shuffling files over USB by hand.
3. Start the launcher, then accept the permission dialogs for both the launcher and the QuestZDoom app. You need internet access for the first setup pass — the launcher downloads what it needs on that initial run.

## Getting the free Castlevania content in

This is where I have to be honest about a gap rather than paper over it. The Quest-specific modified 1.4 build of Simon's Destiny is confirmed to exist and is distributed through ModDB and community threads — that's a verified fact. What isn't confirmed is whether the QuestZDoom Launcher carries Simon's Destiny as a one-tap download inside its own mod list, or whether you grab the modified PK3 from ModDB and side-load it manually into the wads folder yourself. I couldn't verify the in-launcher path this run, so before you assume a one-tap install, open the launcher's live mod list and check. If it's there, you're done in three taps. If it's not, you download the QuestZDoom addon PK3 from ModDB and drop it into the QuestZDoom wads directory the same way you'd add any mod.

Whichever route you use, you still need that base IWAD underneath it, and this is the part that stays free:

- **Free route:** inside the launcher, grab FreeDoom as your base IWAD. It downloads directly. No purchase, no file hunting.
- **Retail route (if you already own Doom):** copy your `DOOM.WAD` or `DOOM2.WAD` into `/QuestZDoom/wads` on the headset, hit "Rescan" in the launcher, and use "Send Missing Hashes" if it doesn't recognize the file right away.

One more unconfirmed step I'd flag the same way: the exact load order for stacking FreeDoom under the Simon's Destiny mod in the launcher wasn't something I could pin down from primary sources. The launcher is built to load a base IWAD plus mods in a specific order, so check the mod's own readme or the r/QuestZDoom thread for the correct sequence before you assume it'll just work — a wrong order is the difference between a castle and a crash to desktop.

## Performance: set it before you complain

QuestZDoom's own documentation is candid that the GZDoom engine gets resource-hungry the moment mods enter the picture, and that you should expect noticeable frame drops when a lot is happening on screen. The settings that actually help are specific:

- Drop **super-sampling to 0.9**. The engine's recommended starter combo sets SS to 0.9 and forces the **60Hz refresh rate**. Do that first.
- Don't chase higher refresh or sharper sampling on the heavier modded content — the stripped maps and missing props in the Quest build are already doing the heavy lifting to keep it playable, and fighting them with settings just reintroduces the stutter the mod was built to remove.

The good news is the engine itself is comfortable to handle: two-handed weapon grip, haptic feedback, smooth locomotion plus teleport, and smooth or snap turning. The bad news is that comfort is the engine's, not a promise about Simon's Destiny's framerate under load — set the numbers above and the castle stays smooth enough to swing in.

## The controls you'll actually use

QuestZDoom's default scheme is right-handed, and it's worth learning before you're mid-fight. The baseline mapping:

- **A** — open door / switch
- **B** — jump
- **Y** — AutoMap
- **X** — unmapped by default
- **Dominant-hand trigger** — fire (your whip / weapon)
- **Off-hand trigger** — run
- **Off-hand grip** — weapon stabilisation for the two-handed grip mode
- **Off-hand thumbstick** — locomotion and teleport
- **Menu** — the left controller's menu button

Teleport is its own little dance: point the off-hand at the floor, push the thumbstick forward, release. If you've come from a native Quest game where every button is a context action, this is the GZDoom legacy showing — a keyboard-and-mouse scheme stapled onto motion controllers. It works, and after ten minutes the muscle memory lands, but the first skeleton you fight will expose how much of this is "learn the layout" rather than "intuitive."

## Who this is actually for

Be clear about the player this rewards. If you own a Quest, you've already spent the hardware money, and you want a free, genuinely first-person Castlevania you can sink an afternoon into — this is a no-brainer. The whole cost is sideloading two apps and downloading a free base IWAD. For that, you get a real, fan-built castle with the right monsters and the right weapon in your hand.

If what you want is a polished, officially supported VR Castlevania with a tutorial and a comfort settings menu and a patch roadmap, this isn't it and never will be. It's a 2017 fan total conversion running on a community engine port, stripped down to stay smooth on a standalone headset. The frame drops under heavy load are real, the control scheme is a port of a port, and the one-tap install is only true if the launcher currently carries the mod — which you have to verify yourself. The standalone Quest route also rules out the PC VR path entirely; QuestZDoom is Quest-only hardware.

## The bottom line

Free, first-person Castlevania on a standalone Quest is real, and it's closer to "an afternoon of sideloading" than "a weekend of pain." The path is two SideQuest apps, a free FreeDoom base pulled by the launcher, and the Quest-modified 1.4 Simon's Destiny build on top — with super-sampling at 0.9 and 60Hz set before you launch. The two things I couldn't confirm and you should check yourself are whether the launcher downloads the mod directly or you side-load the PK3 by hand, and the exact load order for stacking the base under the mod. Get those two right and the only thing standing between you and a whip in your hand is a USB cable. If a free, slightly rough-around-the-edges Castlevania is worth an hour of setup, this is the cleanest route to one on Quest — and it costs exactly what you already paid for the headset.
