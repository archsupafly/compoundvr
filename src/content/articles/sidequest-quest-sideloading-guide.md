---
title: "SideQuest: The Complete Guide to Quest Sideloading and VR's Underground App Store"
description: "SideQuest is the unofficial app store that turned every Quest headset into an open platform. Here's what it is, why it matters, what you can do with it, and how it connects to the VR modding ecosystem."
pubDate: 2020-10-28
lastVerified: 2020-10-28
author: Richard
category: guide
heroImage: /images/articles/sidequest-quest-sideloading-guide-hero.jpg
tags: ["sidequest", "quest", "quest-2", "sideloading", "vr-modding", "standalone-vr", "guide", "2020"]
---

If you own a Quest headset and you've only used the official Meta Store, you're seeing half the picture.

SideQuest is the unofficial app store that turned every Quest headset into an open platform. It's the tool that lets you install apps, games, tools, and mods that Meta hasn't approved — the content that doesn't make it through the official store's curation process, the experiments too niche for the mainstream, the community-built experiences that exist because someone thought "this should work in VR" and built it themselves. Since 2019, SideQuest has been the bridge between the Quest's walled garden and the modding community that refused to be contained by it.

If you've read about [Quest](/articles/oculus-quest-review) sideloading, VR modding, or the standalone ecosystem's underground scene, SideQuest is the tool they're all talking about. Here's what it actually is, why it exists, and how to get started.

## What Is SideQuest?

SideQuest is a desktop application — available for Windows, Mac, and Linux — that lets you browse, download, and install content on your Quest headset outside the official Meta Store. Think of it as an App Store for apps that aren't on the App Store.

The technical mechanism is sideloading: installing Android APK files directly onto the Quest's Android-based operating system. The Quest runs a modified version of Android, and like any Android device, it can install apps from sources other than the official store — if you know how to enable that capability. SideQuest makes the process visual, searchable, and accessible. Instead of manually downloading APK files and running ADB commands, you browse a curated catalog, click install, and the app appears in your Quest library.

SideQuest doesn't make the content. It's a distribution platform — the storefront, not the developer. The apps, games, and tools on SideQuest are built by independent developers, modders, tinkerers, and the VR community. SideQuest provides the infrastructure: the catalog, the installation pipeline, the ratings and reviews, and the community layer that connects creators with users. It's the relationship between SideQuest and its community that made it essential: the platform didn't just distribute content, it cultivated a scene.

## Why Does SideQuest Exist?

The Quest is a closed platform. Meta's store has approval processes, content guidelines, and a business model that favors polished commercial releases over experimental or niche content. That's fine for Beat Saber and [Pavlov](/games/pavlov) — the hits that justify the store's curation. But the VR community produces content faster than any store can curate it: indie experiments, ports of classic games, modding tools, accessibility features, performance tweaks, and experiences that are too weird, too niche, or too unfinished for the official pipeline.

Before SideQuest, getting this content onto your Quest meant manually enabling developer mode, downloading APK files from Discord threads or GitHub repos, connecting your headset to a computer, and running ADB commands from a terminal. It worked, but it was hostile to anyone who wasn't technically comfortable. The barrier wasn't the Quest's hardware — it was the distribution problem. SideQuest solved that by building a storefront for the stuff the storefront didn't carry.

The timing mattered. The [original Quest](/articles/oculus-quest-review) shipped in May 2019, and by summer, the sideloading scene was already growing — SideQuest launched the same year. The [Quest 2](/articles/oculus-quest-2-review), with its $299 price point and exploding install base in October 2020, turned SideQuest from a niche tool into an essential one. Millions of new headsets meant millions of new potential users for sideloaded content. SideQuest's catalog grew to match.

## What Can You Do with SideQuest?

The catalog is broad, but the content falls into a few categories:

### Sideloaded Games and Experiences

Indie VR games that aren't on the Meta Store. Some are polished enough to be commercial releases — they're on SideQuest because they bypassed the store's approval process, not because they're bad. Others are experimental, short, or deliberately weird: proof-of-concept experiences, game jams, one-person projects that couldn't justify the store's overhead. The quality varies, but the breadth is something the official store can't match.

### Classic Game Ports (Team Beef)

The [Team Beef](https://github.com/nicoplv/sidequest-wiki/wiki/Team-Beef-VR-Ports) ports are SideQuest's most famous content category: native Quest ports of classic flat games, built by a community team that reverse-engineered the originals and rebuilt them for VR. Doom, Quake, Half-Life, Return to Castle Wolfenstein, Duke Nukem 3D, and dozens more — running natively on the Quest's hardware, with full motion controls, room-scale support, and 6DOF tracking. These aren't streaming or injection-driver approximations. They're the actual games, rebuilt for VR, running on a standalone headset. The Team Beef ports are the reason many Quest owners discovered sideloading in the first place.

### Modding Tools and Utilities

Apps that extend what the Quest can do: custom home environments, file managers, media players that play formats the official apps don't support, screen recorders, and developer tools. Some of these fill gaps that Meta hasn't addressed — features that users want but that don't fit the official store's roadmap.

### PC VR Streaming and Companion Apps

[Virtual Desktop](/articles/virtual-desktop-guide/), the wireless PC VR streaming app, gained its largest audience through SideQuest — the enhanced version with better streaming quality was sideload-only for a significant period. Other companion tools that bridge the Quest and PC ecosystems live here too.

## How to Get Started

The setup is straightforward, but it requires a few steps that aren't immediately obvious if you've only used the official store.

### Step 1: Enable Developer Mode

You need a Meta developer account (free). Go to [developer.oculus.com](https://developer.oculus.com), create an account, and verify it. Then open the Meta mobile app, go to Settings → Developer Mode, and enable it. This doesn't make you a developer — it just unlocks the ability to install unofficial apps on your headset.

### Step 2: Install SideQuest

Download SideQuest from [sidequestvr.com](https://sidequestvr.com). It's available for Windows, Mac, and Linux. Install it like any desktop application. Launch it, and you'll see the catalog: browseable, searchable, rated, and reviewed.

### Step 3: Connect Your Quest

Plug your Quest into your computer with a USB-C cable. Put the headset on and accept the "Allow USB Debugging" prompt that appears. SideQuest should detect your headset — you'll see a green indicator if the connection is successful.

### Step 4: Install Content

Browse the SideQuest catalog. Find something you want. Click "Install." The app downloads and installs directly onto your Quest. It appears in your Quest library — you might need to enable "Unknown Sources" in the library filter to see sideloaded apps.

That's it. The whole process, from first launch to first sideloaded app, takes about five minutes. SideQuest also offers a standalone headset version — you can install SideQuest directly onto the Quest itself and browse/install without a computer, though the desktop version is more full-featured.

## The Modding Connection

SideQuest matters to the [VR modding](/articles/luke-ross-real-vr-guide) ecosystem because it solved the distribution problem for an entire community.

The modding scene — from [VorpX](/articles/vorpx-injection-driver-guide) injection-driver profiles to Team Beef's classic-game ports to independent developers building experiences that Meta's store wouldn't carry — needed a way to reach users. Discord servers and GitHub repos worked for the technically inclined, but they couldn't scale. SideQuest scaled it: a centralized catalog with search, ratings, reviews, and one-click installation. The community built the content; SideQuest built the distribution.

This mattered because it created a pipeline. Content that didn't fit Meta's store policies — too experimental, too niche, too mod-adjacent — had a home. The sideloading ecosystem became the VR equivalent of the early PC shareware scene: a distribution layer built by the community, for the community, outside the official channels. And as the Quest's install base grew, the community grew with it.

For the [flat-to-VR modding scene](/articles/top-vr-modding-news-2020), SideQuest was particularly important because it gave Quest-only users access to content that previously required a gaming PC. The Team Beef ports brought classic Doom, Quake, and Half-Life to a standalone headset — no PC required. That's the kind of experience that turns a Quest from "Beat Saber machine" into a legitimate gaming platform.

## What SideQuest Isn't

A few clarifications for the uninitiated:

**SideQuest isn't piracy.** The content on SideQuest is overwhelmingly free, built by independent developers, or available through official purchase. It's not a torrent site — it's a distribution platform for content that exists outside the official store.

**SideQuest isn't unsafe.** Sideloading carries inherent risks — you're installing apps that haven't been through Meta's review process — but SideQuest curates its catalog, and the community provides ratings and reviews. The risk is comparable to installing apps from any open platform. Stick to well-reviewed content and you're fine.

**SideQuest isn't a replacement for the Meta Store.** It's a complement. The best Quest experience uses both: the official store for the polished commercial releases, SideQuest for everything else. They serve different audiences and different content, and the Quest is better for having both.

**SideQuest won't void your warranty.** Enabling developer mode and sideloading apps doesn't modify the headset's firmware or violate Meta's warranty terms. It's a supported Android feature, used in exactly the way the platform was designed to support.

## The Bigger Picture

SideQuest is a snapshot of what happens when a closed platform meets an open community. Meta built the Quest as a curated experience — control the hardware, control the store, control the ecosystem. The community looked at that and said "what about the stuff you didn't approve?" SideQuest was the answer.

The sideloading scene matters because it's the proof that VR content demand outpaces official supply. Users want experiences that don't exist on the store. Developers want to build them. SideQuest connected the two. And in doing so, it created a parallel ecosystem that made the Quest platform stronger — not weaker — by giving users more reasons to keep the headset on.

If you own a Quest and you've been curious about sideloading, SideQuest is the place to start. The setup is five minutes. The catalog is deep. And the content you'll find there — the indie experiments, the classic ports, the tools that fill gaps Meta hasn't addressed — is the reason the Quest is more than just an official store with a headset attached.
