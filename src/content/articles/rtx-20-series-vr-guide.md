---
title: "RTX 20-Series VR Performance: What Each Card Ran in 2018"
description: "NVIDIA's RTX 20-Series launched in 2018 with four cards and almost no VR testing. This guide rebuilds what each one actually ran in the 2018 VR library, flags the gaps reviewers left, and tells you which card was worth the money for a headset owner."
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

NVIDIA launched the RTX 20-Series in 2018 and sold it on ray tracing and DLSS. If you owned a VR headset, neither of those features did anything for you at launch. What you actually cared about was raw frame headroom: could the card hold 90 Hz in your games, and how far could you push supersampling before it fell over? Almost nobody benchmarked that properly. The reviews that shipped in September 2018 leaned on synthetic VR tests and flat-game framerates, then called it a day.

This guide reconstructs the answer from what period sources actually measured, and labels every gap as a gap. Where a number exists, it carries its source inline. Where it doesn't, it says so. The 2070 and 2060 never got a real VR review, and I'm not going to invent one.

## What "VR performance" meant in 2018

A VR headset renders two eye images every frame. Supersampling renders those images at higher than native resolution, then downsamples them, which buys real sharpness at a real GPU cost. Reprojection is the safety net: Oculus called it Asynchronous Spacewarp (ASW), HTC called it async reprojection. When the GPU can't hold 90 Hz, the headset halves your output to 45 Hz and synthesizes the missing frames. It keeps you from face-planting into a wall, but it smears and adds latency. The entire reason to buy a faster card was headroom: supersample for clarity without tripping reprojection.

That context matters because the 20-Series story is mostly a headroom story, not a raw-framerate story. In games that already ran fine on a GTX 1080, a 2080 Ti mostly bought you supersampling room and a buffer for higher-resolution headsets like the Vive Pro or Pimax. It did not double your framerate in already-runnable titles.

## DLSS and ray tracing: irrelevant at launch

DLSS 1.0 shipped with the Turing cards and zero VR titles supporting it. NVIDIA named 21 games that would adopt RT or DLSS over the following year, but VR adoption was effectively nil through 2018 and 2019. First-gen DLSS needed per-game training and was never applied to a VR release in this window. Ray-tracing cores sat unused in every VR application of the era. No source pins down the first VR title to adopt DLSS 1.0, or whether any shipped before 2020.

This is worth stating flat because the RTX marketing implied a generational leap. For a 2018 VR owner, the 20-Series was a conventional GPU generation with new silicon you couldn't use yet.

## RTX 2080 Ti ($999, September 2018)

The flagship is the only card in the stack with solid period VR data. UploadVR's September 2018 testing put it at "almost double the performance of the GTX 1080" in SteamVR's frame-count benchmark, and roughly 60% faster than the GTX 1080 Ti in VRMark's Blue Room (a 5K rendering test), and about 30% ahead of the RTX 2080. Their takeaway was blunt: unless you owned a very high-resolution headset, you probably did not need to upgrade from a 1080 or 1080 Ti. They also noted bottlenecking in some VR tests even on Threadripper systems, which tells you the GPU wasn't always the limit.

The community felt the same gap. A September 2018 r/Vive thread titled "Where are the real 2080 Ti VR benchmarks?" was mostly users pointing out that in real games, without RT cores doing anything, the card was only about 30% over the 1080 Ti.

For the 2018 library, that translated to: comfortable in everything, with meaningful headroom in the heavy titles. In [Skyrim VR](https://compoundvr.com/games/skyrim/) and [Fallout 4 VR](https://compoundvr.com/games/fallout-4/), both Creation Engine ports notorious for hammering the GPU, even a 1080 Ti owner struggled at 100% supersampling with max settings. The honest estimate: the 2080 Ti's ~20–30% flat-game margin over the 1080 Ti, combined with period reports of Creation Engine VR being GPU-bound, suggests real but not unlimited headroom — settings compromises for stable 90 Hz, and supersampling beyond 100% often impractical even on the flagship. No period source measured concrete supersampling percentages here. In [Project CARS 2](https://compoundvr.com/games/project-cars-2/) and [Elite Dangerous](https://compoundvr.com/games/elite-dangerous/) (both in BabelTechReviews' test suite), the 2080 Ti gave a clear improvement over the 1080 Ti, and Elite Dangerous' cockpit text became readable at higher supersampling. The lightweight roster — [Beat Saber](https://compoundvr.com/games/beat-saber/), [SUPERHOT VR](https://compoundvr.com/games/superhot-vr/), [Moss](https://compoundvr.com/games/moss/), [Robo Recall](https://compoundvr.com/games/robo-recall/), [Lone Echo](https://compoundvr.com/games/lone-echo/), [Arizona Sunshine](https://compoundvr.com/games/arizona-sunshine/), [Pavlov](https://compoundvr.com/games/pavlov/), and Onward — ran with massive supersampling headroom to spare, though no period review quoted specific percentages for these titles.

## RTX 2080 ($699, September 2018)

This is the card with the most damaging finding in the whole stack, and it comes from BabelTechReviews' FCAT-VR suite (November 2018), which tested five Oculus Rift titles: [Batman: Arkham VR](https://compoundvr.com/games/batman-arkham-vr/), Chronos, DiRT Rally, [Project CARS 2](https://compoundvr.com/games/project-cars-2/), and [Elite Dangerous](https://compoundvr.com/games/elite-dangerous/). In Batman: Arkham VR, the GTX 1080 Ti hit 193.3 FPS unconstrained while the RTX 2080 managed 183.3 FPS. The newer card lost. BabelTechReviews attributed it to driver maturity, and noted neither card dropped frames or needed ASW in that title. That result is the spine of this guide's thesis: at launch, the 2080 did not consistently beat the 1080 Ti in VR, and in at least one measured game it lost.

On paper the 2080 was slightly ahead of the 1080 Ti in flat gaming, but VR is its own workload, and the 2080's real win was modest. It cleared the 2018 library comfortably and reduced ASW triggers versus 10-Series cards in demanding scenes, but the upgrade from a 1080 Ti was not the story NVIDIA's launch slides told. Period sources gave no per-card ASW trigger rates, so fewer reprojection events is a general inference from the class jump, not a measured figure.

## RTX 2070 ($499, October 2018)

No period VR benchmark review exists for this card. It launched a month after the 2080 and 2080 Ti and received almost no VR-specific attention. NVIDIA positioned it as GTX 1080-class performance at a lower price, so in VR expect roughly 1080-tier frame headroom — a notch below the 2080 and behind the 1080 Ti where the 1080 Ti led. Treat that as an architecture-based estimate, not a measurement.

What that means for the 2018 library: the lightweight titles ran fine, and the heavy Creation Engine ports were playable with settings pulled down, but you would not have the supersampling buffer a 1080 Ti or 2080 Ti owner enjoyed. No per-game FPS figures for the 2070 exist in period sources, so any specific claim would be invented. Do not trust a "2070 ran Skyrim VR at X" number from this era.

## RTX 2060 ($349, January 2019)

The budget entry, and the same problem as the 2070: zero dedicated VR benchmarks at launch. With 1,920 CUDA cores and 6 GB of GDDR6, it lands near GTX 1070 / 1070 Ti class in VR — a step below the 2070. That is architecture, not measurement. The one hard limitation is the 6 GB of VRAM, which caps supersampling in memory-heavy titles. Skyrim VR and Fallout 4 VR, which eat VRAM when you push resolution, are exactly where 6 GB bites. The specific VRAM impact on 2018 titles for the 2060 was never measured in a period review.

For a 2018 VR owner buying in early 2019, the 2060 was the entry ticket: it ran the lightweight catalog and the heavier ports at reduced settings, but it was the card you bought because it was cheap, not because it had headroom.

## The GTX 1080 Ti yardstick

The only 10-Series card that matters here is the 1080 Ti, because it's the direct comparison period reviewers actually ran. Two measured data points exist: BabelTechReviews' FCAT-VR put the 1080 Ti ahead of the 2080 in Batman VR (193.3 vs 183.3 FPS), and UploadVR's VRMark Blue Room put the 2080 Ti about 60% over the 1080 Ti. Everything else about 10-Series comparison is out of scope for this guide, and I'm not dragging in the 1060 or 1070. The takeaway is narrow and real: if you already owned a 1080 Ti in 2018, the 2080 was not a clear VR upgrade, and only the 2080 Ti moved the needle enough to justify the cost for a high-resolution headset.

## Which card was actually worth it

If you were buying for VR in the 2018 window, the hierarchy was honest in a way the marketing wasn't. The 2080 Ti was the only card that clearly separated from the previous generation's best, and only if you were feeding a high-resolution headset or refused to compromise in Skyrim VR and Fallout 4 VR. The 2080 was a lateral move from a 1080 Ti for most of the library. The 2070 and 2060 were sensible buys only if you didn't already own a 10-Series card near their class, and both shipped without the VR testing you'd want before trusting them in the heavy ports.

The 20-Series' real VR legacy wasn't 2018. It was the silicon that aged into later VR titles, where the extra headroom finally had something to do. In its launch year, for the library that actually existed, the cards mostly bought supersampling room, not framerate you could feel.
