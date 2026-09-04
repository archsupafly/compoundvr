---
title: "Quest Link: The Complete Guide to Meta's Free PCVR Connection"
description: "Quest Link (wired) and Air Link (wireless) turn your Quest into a PCVR headset for free. Here's setup, cable truth, requirements, and when to buy Virtual Desktop instead."
pubDate: 2026-09-03
lastVerified: 2026-09-03
author: Richard
category: guide
heroImage: /images/articles/quest-link-guide-hero.jpg
tags: ['quest-link', 'air-link', 'quest', 'quest-2', 'quest-3', 'pcvr', 'wired-pcvR', 'wireless-pcvR', 'guide', 'virtual-desktop']
---

Your Quest can play your PC's VR library two ways: Meta's free official route, or the paid app. This guide covers the free route — Quest Link and Air Link — completely, and tells you honestly where it ends and [Virtual Desktop](/articles/virtual-desktop-guide/) begins.

## What Quest Link and Air Link Are

Quest Link is Meta's wired PCVR connection: a USB cable between your Quest and your gaming PC, carrying the rendered frames one way and your tracking and input the other. It launched alongside the original Quest in 2019 as "Oculus Link" and was later renamed Quest Link. Your standalone headset becomes a PCVR headset, playing your Rift and SteamVR libraries.

Air Link is the wireless version, added in 2021: same idea, over Wi-Fi instead of cable. No cord, more freedom, more ways for your network to ruin your evening.

Both are free and built into the Quest OS and the Meta Quest PC app. If you own a Quest and a gaming PC, you already own everything except possibly a cable.

## Wired Setup: Quest Link

What you need: a Quest headset, a gaming PC, the free Meta Quest PC app (formerly Oculus PC software), and a USB cable. The cable is where everyone overthinks it.

**Cable truth:** Meta sells an official 5-meter fiber-optic cable for around $80. It's excellent — light, flexible, long. You do not need it. Any quality USB 3 cable rated for 5Gbps works: a $20–30 third-party USB-C to USB-C (or USB-A to USB-C) cable of sufficient length does the job. What matters is USB 3 speeds (USB 2 works but throttles quality), a secure fit that won't wiggle loose mid-session, and enough length to move — 3 meters minimum, 5 is better. Test the connection in the PC app; it reports the measured bandwidth, and anything above ~2Gbps plays fine.

Setup: install the Meta Quest PC app, plug in, put on the headset, accept the prompt, done. First connection takes five minutes. If the headset isn't detected, try a different USB port (motherboard rear ports beat front-panel headers), update your GPU drivers, and restart the PC app before anything exotic.

Wired Link is the most reliable PCVR connection available on Quest. No encoding surprises, no Wi-Fi lottery, consistent latency. Its only cost is the cord.

## Wireless Setup: Air Link

Air Link has stricter demands than the cable, and this is where most people fail:

- **PC wired to the router via ethernet.** Not optional. Your PC on Wi-Fi plus your headset on Wi-Fi means every frame crosses the air twice, and it shows.
- **5GHz Wi-Fi minimum** (6GHz better on Quest 3/Pro), router ideally in the same room you play in.
- Both devices on the same network.

Enable Air Link in the headset's experimental/quick settings and in the PC app, pair once, and it connects from the quick panel thereafter. When the network is right, Air Link is genuinely good — good enough that plenty of players never touch anything else.

When the network is wrong, it's stutter, gray thicker than fog, and complaint threads. Fix the network, not the settings.

## Link vs Air Link: Which to Pick

Wired if: you play seated sims or long sessions (cable doubles as charging), your Wi-Fi is congested or far, you want maximum reliability, or you're troubleshooting anything — always test wired first to isolate network issues.

Wireless if: you play room-scale, you turn a lot (shooters, melee), your router is in the play space and your PC is ethernet-wired, and you've verified clean performance. Freedom is real; so is the failure mode.

## Where Virtual Desktop Wins (and Where It Doesn't)

Honest comparison, same verdicts as our [Virtual Desktop guide](/articles/virtual-desktop-guide/):

Air Link is free and fine for the official library. If you play Rift and Steam store games and your network is solid, stop here — you need nothing else.

[Virtual Desktop](/articles/virtual-desktop-guide/) earns its ~$20 with lower practical latency, wider codec support (H.265/AV1 quality per megabit that Air Link doesn't match), per-game settings, and the VDXR runtime that skips SteamVR overhead. For modded PCVR — [UEVR-injected games](/articles/uevr-guide/), [Luke Ross conversions](/articles/luke-ross-real-vr-guide), anything launched outside a storefront — it's the default recommendation. Air Link covers the mainstream; Virtual Desktop covers everything else, better.

Neither fixes a bad network or a weak PC. That's the part no app solves.

## Mod-Player Notes

Most flat-to-VR conversions don't care which streamer you use — they see a PCVR headset either way. Two exceptions worth knowing:

- If a mod's docs name a runtime (VDXR vs SteamVR vs Oculus), match it. Runtime mismatches cause most "black screen on launch" reports, and the fix is a dropdown, not a reinstall.
- If you're debugging anything — a new mod, a new headset, a new router — test over wired Link first. It removes the network from the equation. Once it works wired, go wireless.

## When It Breaks

- **Headset not detected (wired):** different USB port, preferably motherboard rear. Update GPU drivers. Restart the PC app.
- **Stutter (wireless):** network, always network first. Bitrate down, router closer, devices off the band, PC on ethernet.
- **Air Link option missing:** update Quest OS and the PC app to current versions on both ends.
- **Game launches flat or won't enter VR:** check the game's launch options and the runtime the mod expects.

## The Bottom Line

Quest Link is the free, official, reliable default — wired for maximum stability, Air Link for freedom when your network earns it. It covers the official library completely and costs nothing. When you outgrow it — mods, tuning, codecs, latency — [Virtual Desktop](/articles/virtual-desktop-guide/) is waiting, and our guide covers that side in full. Learn both, pay once or never, play everything.
