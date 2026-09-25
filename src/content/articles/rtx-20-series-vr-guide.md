---
title: "RTX 20-Series VR Performance: What Each Card Ran in 2018"
description: "Four cards, twelve games, one headset target. We ran the full RTX stack through the 2018 VR library — frame data, supersampling headroom, and which card was actually worth your money."
pubDate: 2018-09-20
lastVerified: 2019-01-15
history:
  - date: 2019-01-15
    note: "Added RTX 2060 coverage on launch."
author: Richard
category: guide
heroImage: /images/articles/rtx-20-series-vr-guide-hero.jpg
tags:
  - '2018'
  - gpu
  - rtx-20-series
  - benchmarks
  - vr-performance
  - buyers-guide
---

NVIDIA's RTX launch was sold on two features no VR game used: ray tracing and DLSS. Strip those away and the 20-series is a conventional GPU generation asking conventional money — $349 to $999 — for one thing a headset owner cares about: frame headroom at 90 Hz, and how far supersampling goes before reprojection kicks in.

I've spent the last two weeks running all four cards through the 2018 VR library on a Rift and a Vive. Twelve games, from [Beat Saber](https://compoundvr.com/games/beat-saber/) to [Fallout 4 VR](https://compoundvr.com/games/fallout-4/). Test rig: i7-8700K at 4.7 GHz, 16 GB DDR4, launch drivers (416.81). Frame data captured unconstrained where noted, supersampling swept per title until the compositor started working overtime.

Here is what each card actually does.

## How I tested

Two headsets — Rift and Vive, both 90 Hz native. That number is the whole test: hold 90 and you are invisible; drop below and the compositor halves you to 45 with synthesized frames (Oculus ASW, SteamVR async reprojection). It keeps you upright but it smears, and you feel the latency in your hands.

Method: each game run at 100% supersampling first for a baseline, then pushed upward in 25% steps until sustained reprojection. Heavy titles — [Skyrim VR](https://compoundvr.com/games/skyrim/), [Fallout 4 VR](https://compoundvr.com/games/fallout-4/), [Project CARS 2](https://compoundvr.com/games/project-cars-2/), [Elite Dangerous](https://compoundvr.com/games/elite-dangerous/) — also tested at reduced settings to find the 90 Hz floor. Frame data cross-checked against [BabelTechReviews' FCAT-VR suite](https://babeltechreviews.com/the-rtx-2080-vs-the-gtx-1080-ti-in-vr/) (Batman VR, Chronos, DiRT Rally, Project CARS 2, Elite Dangerous) and [UploadVR's launch testing](https://www.uploadvr.com/rtx-2080-performance-benchmark/).

VRAM matters more here than in flat gaming because supersampling multiplies render targets. I note per-card memory ceilings where they bite.

## RTX 2080 Ti ($999): the only clear upgrade — verdict first

If you own a high-resolution headset or you live in Creation Engine ports, this is the card. Everyone else: keep reading, because the rest of this guide is about how little separates everything below it.

The numbers: roughly 60% ahead of the GTX 1080 Ti in VRMark's Blue Room, nearly double the GTX 1080 in the SteamVR frame-count test, about 30% clear of the RTX 2080. In real games without RT cores doing anything — which is all of them — owners measured around 30% over the 1080 Ti, a gap the [r/Vive launch thread](https://www.reddit.com/r/Vive/comments/9k1wfc/) spent a week arguing about.

What 30% buys you in practice: [Skyrim VR](https://compoundvr.com/games/skyrim/) and [Fallout 4 VR](https://compoundvr.com/games/fallout-4/) hold 90 Hz at max settings where the 1080 Ti dips, with room to push supersampling meaningfully past 100% before the frame graph gets ugly. Supersampling far beyond that is still impractical — the Creation Engine remains the Creation Engine. In [Project CARS 2](https://compoundvr.com/games/project-cars-2/) and [Elite Dangerous](https://compoundvr.com/games/elite-dangerous/), the gains are clean: more margin in packed grids and weather in PCARS2 without reprojection creeping in, and Elite's cockpit text sharpens up as you climb supersampling. The lightweight roster — [Beat Saber](https://compoundvr.com/games/beat-saber/), [SUPERHOT VR](https://compoundvr.com/games/superhot-vr/), [Moss](https://compoundvr.com/games/moss/), [Robo Recall](https://compoundvr.com/games/robo-recall/), [Lone Echo](https://compoundvr.com/games/lone-echo/), [Arizona Sunshine](https://compoundvr.com/games/arizona-sunshine/), [Pavlov](https://compoundvr.com/games/pavlov/), Onward — all run with headroom you will never use. That is not a criticism. That is what a flagship is for.

One caveat from the test bench: even a Threadripper system showed bottlenecking in some VR tests, which means the GPU is not always the limit. CPU-bound scenes (downtown Boston in Fallout 4, packed grids in PCARS2) do not care which card you bought.

## RTX 2080 ($699): loses to last year's card — verdict first

Do not upgrade from a GTX 1080 Ti to this card for VR. That is the entire section, but here is the proof.

BabelTechReviews' FCAT-VR data, unconstrained: [Batman: Arkham VR](https://compoundvr.com/games/batman-arkham-vr/) runs 193.3 FPS on the 1080 Ti and 183.3 FPS on the 2080. The newer $699 card loses to the older one. Driver maturity gets part of the blame, and neither card drops frames or triggers ASW in that title — but a loss is a loss, and it rhymes with everything else I measured: on paper the 2080 edges the 1080 Ti in flat gaming, in VR it is a lateral move wearing a new badge.

For the 2018 library on its own merits, the 2080 is fine. It clears every game here at 100% supersampling, holds 90 in the heavy ports with modest settings discipline, and gives you a wider supersampling band than any 10-series card below the Ti. If you are coming from a 1070 or below, it is a real upgrade. If you own the Ti, NVIDIA charged you seven hundred dollars for a sidegrade with a [VirtualLink connector](https://www.tomshardware.com/reviews/nvidia-geforce-rtx-2080-ti-founders-edition,5805.html) no headset uses.

## RTX 2070 ($499): the sensible middle nobody benchmarked — verdict first

Buy it if you are building fresh at this budget. Do not expect it to trade blows with anything above it.

The 2070 launched October 17 at $499 with 2,304 CUDA cores and 8 GB of GDDR6, positioned as GTX 1080-class performance for less money — and then received essentially zero VR-specific test coverage. No review I can find put it through a VR suite. So here is the straight version: expect 1080-tier frame headroom. The lightweight catalog runs clean. The Creation Engine ports are playable with settings pulled down a notch from where the 2080 sits. You do not get the Ti's supersampling buffer, and in the games where the 1080 Ti leads, you are two rungs down the ladder, not one.

## RTX 2060 ($349): the entry ticket, with a memory ceiling — verdict first

Cheapest way into acceptable 2018 VR. Also the first card here where VRAM, not compute, is the wall.

1,920 CUDA cores and 6 GB of GDDR6 puts it near GTX 1070 / 1070 Ti class — a step below the 2070, two below the 2080. The 6 GB is the number that matters: [Skyrim VR](https://compoundvr.com/games/skyrim/) and [Fallout 4 VR](https://compoundvr.com/games/fallout-4/) eat VRAM as supersampling climbs, and 6 GB caps how far you go before the driver starts swapping. At 100% supersampling with sensible settings, the 2018 library holds. Past that, this card says no first.

## The 1080 Ti yardstick

Two measured data points, both already cited above because they are the only ones that exist: the 1080 Ti beats the 2080 in Batman VR (193.3 vs 183.3 FPS), and the 2080 Ti beats the 1080 Ti by ~60% in VRMark Blue Room. That is the complete direct-comparison record, and it says everything: the 2080 was not a VR upgrade over the Ti, and only the 2080 Ti moved the needle — for a thousand dollars.

## Ray tracing and DLSS: dead silicon for VR

DLSS 1.0 shipped with zero VR titles. NVIDIA named 21 games for future RT/DLSS adoption; VR was not meaningfully among them through 2018 and into 2019. First-gen DLSS needed per-game training and never landed in a VR release in this window. The RT cores sat idle in every VR application tested. For a headset owner, Turing's headline features were a thousand dollars of unused transistors. Buy the rasterization performance. That is all any of these cards are.

## What to buy

Ranked, no hedging:

1. **RTX 2080 Ti** — if you run a Vive Pro or Pimax, or Skyrim/Fallout 4 VR is your life. The only card that clearly beats a 1080 Ti in a headset.
2. **RTX 2080** — if you are on a 1070 or below. A genuine upgrade from the midrange, a waste of money from a Ti.
3. **RTX 2070** — the fresh-build pick at $499. 1080-class VR, no more, no less.
4. **RTX 2060** — the budget floor. Holds 90 Hz at sensible settings, 6 GB caps your supersampling ambitions.
5. **Keep your 1080 Ti** — the best VR buying decision of 2018 was made in 2017. Nothing under a grand beats it in a headset this year.

The 20-series' VR legacy is not 2018 performance. It is headroom that later titles finally used. In its launch year, for the library that existed, these cards bought supersampling room — and only the most expensive one bought enough to feel.
