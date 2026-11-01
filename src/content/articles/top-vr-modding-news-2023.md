---
title: "Top VR Modding News of 2023: The Year the Toolkit Ate AAA"
description: "CompoundVR's annual flat-to-VR modding roundup. 2023 didn't deliver studio VR modes — it delivered the tools to build them: UEVR, REFramework, Team Beef's Quest ports, and a scene that organized itself into an industry."
pubDate: 2023-12-15
lastUpdated: 2023-12-15
author: Ian
category: news
heroImage: /images/articles/top-vr-modding-news-2023-hero.jpg
tags: ['2023', 'vr-modding', 'uevr', 'flat-to-vr']
---

2022 was the year flat-to-VR modding stopped feeling like a hobby and started looking like a business. Luke Ross was pulling reported five-figure monthly Patreon totals converting the biggest games on Earth, and the community treated each new R.E.A.L. drop like a studio release. This year the frame shifted again. 2023 didn't prove modding was a business — it proved it was infrastructure. The studios still weren't building VR modes. So the modders built the platform instead.

The signal moment is technical, not commercial. A single generic injector — praydog's UEVR — learned to hook Unreal Engine at runtime and synthesize stereo rendering plus head tracking for thousands of titles at once. One tool, no per-title source work, free to use. That is not a port. That is a layer, and once the layer exists the catalogue behind it is just inventory.

I've spent the year watching that layer swallow the release calendar. The demand was already there: UEVR install tutorials from channels like GingasVR and VR Central were already drawing big viewership, and a curated "getting started" video proved especially popular. That is an audience that already owns the headsets and the games and just needs the method. Below are the stories I think defined 2023 for flat-to-VR, in the order I rate them. None of them came from a publisher's roadmap.

## 1. UEVR ends 2023 as the universal Unreal VR injector

praydog's UEVR is the lead story of 2023 and it isn't close. The repository goes back to September 2022, but 2023 is the year it moved from patron-only testing to a public 1.0 slated for December 31. The pitch is absurd in its breadth: a universal Unreal Engine VR mod covering UE 4.8 through 5.x, injecting full 6DOF head tracking, native stereo rendering, OpenVR and OpenXR output, three rendering modes (native stereo, synchronized sequential, alternating AFR), and automatic in-game UI projection into 3D space. It is free, Patreon-funded, and compatible with any PCVR headset including Quest 2 and 3 over Link or Air Link.

By the year-end launch window the tested catalogue ran into the hundreds of titles, with confirmed-compatible entries including RoboCop: Rogue City, Lies of P, Hogwarts Legacy, Darksiders III, Sifu, Talos Principle 2, and Star Wars Jedi: Fallen Order (rated as working well, with Jedi Survivor rougher). That is the infrastructure point made concrete: a tool this generic turns "is there a VR mod for X" into "does X run on Unreal, and is it on the tested list."

The honest caveats matter. UEVR preserves perspective, so third-person games stay third-person. Motion controls are possible but need custom per-game work and will land, at the year-end launch, on only a couple dozen titles such as RoboCop. Anti-cheat remains the most common wall between a game and a working inject. None of that dulls the achievement. A generic injector is a platform component, and the year ends with that component going public.

[Read the UEVR guide](/articles/uevr-guide/)

## 2. Luke Ross kept converting the biggest games on Earth

While praydog built the layer, Luke Ross kept doing what he has done since Cyberpunk 2077 joined his R.E.A.L. framework back in February 2022: hand-converting individual AAA titles into immersive VR through his paid Patreon system. Through 2023 his slate held Cyberpunk 2077 VR, added Hogwarts Legacy VR and Starfield VR. His own description puts the framework at 40-plus supported games, and reporting from 2022 pegged his Patreon take around $20,000 a month.

I'll state the tension plainly because it isn't going away: a paid VR mod sitting on top of someone else's IP is a legal fault line. Take-Two's earlier actions against paid GTA-related mods set the precedent, and the argument over whether Ross's software is independent code or monetized derivative work is live and unresolved. What I won't do is confuse that argument with the technical achievement. The man converts the games everyone else declares impossible, and 2023 was another year of him doing exactly that while the publishers stayed silent.

[Read the Luke Ross R.E.A.L. VR guide](/articles/luke-ross-real-vr-guide/)
[Cyberpunk 2077 VR coverage](/games/cyberpunk-2077/)
[Hogwarts Legacy VR coverage](/games/hogwarts-legacy/)
[Starfield VR coverage](/games/starfield/)

## 3. REFramework made RE Engine a first-class VR target

praydog's other 2023 project is the one that kept Capcom's catalogue in VR without Capcom lifting a finger. REFramework — a mod loader, scripting platform, and VR layer for RE Engine — shipped three public builds across the year: v1.4 on February 1, v1.5.1 on June 4, and v1.5.2 on October 2. That cadence is the story: steady, public, iterative, and free.

Resident Evil 4 Remake, which launched March 24, got REFramework VR support during 2023 in patron builds — 6DOF head tracking and gamepad control, though no first-person mode at that stage. The same layer services RE2, RE3, RE7, Village, Devil May Cry 5, Monster Hunter Rise, and Street Fighter 6. For PC VR owners who wanted Capcom in their headset, REFramework was the only door, and in 2023 it opened wider with each release.

[Read the REFramework VR guide](/articles/reframework-vr-guide/)
[Resident Evil 4 VR coverage](/games/resident-evil-4/)
[Monster Hunter Rise VR coverage](/games/monster-hunter-rise/)

## 4. Team Beef proved standalone Quest could do console-class VR

The PCVR crowd does not own the whole story. Team Beef spent 2023 pushing console-class flat titles onto standalone Quest hardware, no PC in the loop. Jedi Academy VR, Quake 4 VR, Prey VR, and Doom 3 BFG all landed on Quest through the year. These are not streamed compromises — they are native ports tuned for mobile-class silicon, and they argue that "standalone" and "serious" are not contradictory.

I rate this higher than the press did at the time. Every headset maker sells the hardware; almost none ship the library. Team Beef is quietly closing that gap on the cheapest tier of the market, and 2023 was their most convincing year yet. When a free community port of Doom 3 BFG runs on a standalone headset, the "there's no content" excuse loses what little weight it had.

[Jedi Academy VR coverage](/games/jedi-academy/)
[Quake 4 VR coverage](/games/quake-4/)
[Prey VR coverage](/games/prey/)
[Doom 3 BFG VR coverage](/games/doom-3-bfg/)

## 5. The Source engine crowd finally delivered

Valve's own engine generated the year's most satisfying community momentum. VR work on Half-Life 2's episodes, Portal 2, and Left 4 Dead 2 all pushed through in 2023, driven by community teams rather than any official green light. These are games with deep modding roots, and the VR conversions inherit that scaffolding instead of fighting it.

The significance is generational. Half-Life 2 defined PC shooters two decades ago; seeing its episodes playable in 6DOF on a modern headset is the clearest possible rebuttal to the idea that VR needs new content to thrive. Sometimes the content is already on the shelf, waiting for someone to wire up the camera.

[Half-Life 2 VR coverage](/games/half-life-2/)
[Portal 2 VR coverage](/games/portal-2/)
[Left 4 Dead 2 VR coverage](/games/left-4-dead-2/)

## 6. The toolkit reached past Unreal

UEVR is the headline, but 2023 also showed the generic-conversion mindset is not Unreal-only. The clearest proof is CryEngine. Luke Ross's R.E.A.L. framework carried both Crysis and Far Cry 6 into VR, and both run on CryEngine-family code — Crysis on CryEngine itself, Far Cry 6 on Ubisoft's Dunia fork — rather than through a generic Unreal hook.

That is a different road from UEVR's single-injector model. Ross's line works the same way across every title it touches: the game's own render pipeline, alternating-eye output, gamepad-first, so each conversion is a separate build rather than a toggle in a shared tool. UEVR covers the Unreal catalogue; the R.E.A.L. conversions cover engines the engine-level tools were never built to reach. Together they show the 2023 toolkit was never bound to one engine.

[Crysis VR coverage](/games/crysis/)
[Far Cry VR coverage](/games/far-cry/)

## 7. The scene organized itself into an industry

Flat-to-VR stopped being a collection of lone developers in 2023. The Flat2VR Discord became the coordination hub the whole space routes through, linked straight from the UEVR README, and Flat2VR itself began operating as a studio-like outlet publishing mod releases and news. RoadToVR's modding column gave the work a regular press beat. When the community's infrastructure starts looking like a publisher's org chart, the studios' absence stops being a gap and starts being a choice they're making.

The hub status is not incidental. The UEVR README itself points modders to Flat2VR as the place to find releases and coordination, which is how a Discord becomes the switchboard for an entire scene. When the tool that defines the year sends its users there by default, the community's center of gravity stops being any single developer and becomes the directory. That is the difference between a hobby and an industry.

## 8. Runtime plumbing made mods feel native

The unglamorous story is the one that made everything above usable. Virtual Desktop's VDXR runtime, alongside OpenXR and OpenComposite, quietly removed the friction between a modded flat game and a headset's native path. Good plumbing is invisible; you only notice it when a mod stops feeling like a hack and starts feeling like a game. 2023 was the year the plumbing caught up to the ambition, and the reason so many of this year's mods "just worked" is mostly invisible engineering nobody filmed.

Each piece removed a different wall. OpenXR gave mods one standard runtime interface instead of a separate path per headset maker, so a tool like UEVR could target any OpenXR headset without rewriting for each. OpenComposite let OpenVR-native mods run on top of OpenXR runtimes, so a flat-game inject didn't have to be tied to a single vendor's OpenVR host. VDXR, Virtual Desktop's runtime, gave Quest its own native PCVR path over Wi-Fi instead of a tethered PC connection. None of it is glamorous, but all of it is why a modded flat game stopped feeling like a workaround.

[Read the Virtual Desktop guide](/articles/virtual-desktop-guide/)

## 9. More headsets, same silence from the studios

Two headset launches bookended 2023's hardware story: PSVR2 arrived February 22 and Meta Quest 3 followed October 10. Both put more headsets in more homes. Neither studio planned a first-party VR mode for its 2023 flat releases. That mismatch is exactly why the toolkit ate AAA this year instead of next — the demand was on the shelf and the modders were the only ones who showed up to meet it.

Only one of those two headsets actually fed the modding wave. UEVR and its cousins require a PCVR runtime, so the path into flat-to-VR runs through a PC connected to the headset — the role Quest's Link and Air Link play for standalone hardware. PSVR2 grew the installed base too, but its tethered console pipeline has no native route into a modded PC game. So the Quest 3 landing in homes in October mattered to this story in a way the PSVR2 launch in February did not: more standalone headsets within reach of a PC meant more seats for the toolkit to fill.

[PSVR2 launch review](/articles/psvr2-release-review/)

## The platform was built by the community

My takeaway for 2022 was that modding had become a business. My takeaway for 2023 is stronger: it became the platform itself. UEVR is a runtime. REFramework is a loader. Team Beef is a porting house. Flat2VR is a publisher. None of it came from the studios that own the IP, and all of it works.

The only question left for 2024 is whether the studios notice. The layer is built. The catalogue is inventory. The only missing piece is the people who were supposed to ship VR modes in the first place — and at this point, they're late to their own market.
