---
title: "Unturned VR"
description: "A two-week-old free Unity mod finally puts a headset on the zombie sandbox Smartly Dressed Games never built for VR."
flatReleaseDate: 2014-07-07
vrReleaseDate: 2026-10-23
lastUpdated: 2026-11-01
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Experimental
setupBurden: Advanced Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - Survival
  - Open World
  - FPS
  - Sandbox
  - Zombie
technicalTags:
  - Full VR Mod
  - Unity
  - Tracked Hands
  - Roomscale
  - 6DOF
  - GPL-3.0
experienceTags:
  - Zombie Survival
  - Open World Sandbox
  - Hands-on Shooting
  - Workshop Content
tier: B
verdict: "A free community mod delivers real tracked-hands VR to a game the studio never touched — unfinished, singleplayer-only by force, but the most honest way to finally be inside Unturned."
heroImage: /images/games/unturned-vr-hero.jpg
modDownload:
  url: "https://github.com/GoldenHeartbell/UnturnedVR-mod/releases"
  label: "Download Unturned VR Mod"
  note: "Created by GoldenHeartbell"
history:
  - date: 2026-11-01
    note: "v0.2.7 test build adds physical melee, grenades, and fishing"
sources: "Assessment based on the UnturnedVR mod documentation, its public source tree (GitHub), and community gameplay footage rather than direct hands-on testing. Primary sources: GoldenHeartbell/UnturnedVR-mod README and Releases, PCVR Central mod listing, and YouTube coverage (Kuroga, Cachorrão BR, TheVRViking's 2015 VorpX record)."
---

## The flat screen finally comes off

Unturned has been free on Steam since 2014, and for most of that run the only way to wear a headset in it was VorpX — a 2015-era injection hack that gave you a flat picture with head tracking and a HUD you literally could not read. A mod that showed up two weeks ago does what Smartly Dressed Games never did: it puts you inside the world with your own hands.

UnturnedVR is a free, open-source Unity mod by GoldenHeartbell, licensed GPL-3.0 and built on the same lineage as the Valheim VR (VHVR) project. It doesn't inject a stereoscopic screen — it patches Unturned's own player, equipment, and UI classes and drives OpenVR poses directly. The result is real 6DOF: tracked arms and hands, roomscale, and body holsters instead of a hotbar you click with a mouse.

The author develops and tests on a Valve Index and Steam Frame, but any SteamVR headset qualifies. There's no official VR mode on any platform and no console path — this is the only working way to play it in VR, and it's a community project, not a studio one.

## The catch that closes the servers

The catch shapes how you'll play, and you need to know it before you install. Unturned ships with BattlEye anti-cheat, and the mod cannot run with it on. You launch the game with its anti-cheat disabled, which means no official or public servers — singleplayer and self-hosted only. Server-side sync exists but it's experimental; players without the mod can join a modded server and just won't get VR effects.

This is the single biggest limitation, and it's structural, not a bug. Unturned's natural habitat is populated servers, and the mod walls those off. If you wanted to loot Washington with a friend in VR, you can — but you're both running a privately hosted server with BattlEye off, not dropping into the official ones.

## Hands, holsters, and the dumb thrill of reaching for a rifle

The world that used to be a flat screen is suddenly around your shoulders. Walk forward and the map opens up the way it always should have — you're standing in the dirt, not watching a character stand in it.

The controls are the part that actually sells it. Your hands follow the controllers, and you pick things up with whichever hand is pointing at them. The gun you're holding sits in that hand; pass it over or grip with both for two-handed aim. Firing comes off the trigger of the hand holding the item, and the gun actually fires from the barrel — not from a crosshair floating at screen center. The mod ships a crosshair-fix patch precisely because your hands aim independently of your head, which is the whole point.

Aiming down sights is the gesture that makes it click: you raise the gun's sight to your eye, and scopes get a hand-shake smoothing pass so they don't jitter themselves useless. Per-gun rumble means a pistol kicks different from a rifle. Gear lives on your body — hotbar items sit in holsters, a night-vision gesture lives at your ear, and the tactical light and laser ride the second trigger. The dumb, specific thrill of reaching down, picking a rifle off your hip, and shouldering it to line up a zombie is the thing no flat playthrough ever gave you.

## What still falls back to the keyboard

Unturned has years of maps, vehicles, and Workshop content behind it, and the mod lets you actually inhabit that world instead of watching it. But it's two weeks old and openly labelled work in progress, and the seams show in specific places.

Reloading and melee still fall back to flat-era input on the current stable build, though v0.2.7 — the test build released at the start of the month — adds physical melee, grenades, and fishing, so that gap is closing fast. Inventory and menus use a laser pointer rather than a physical grab: you point and click through the UI instead of handling objects. It works, but it's the part that reminds you this is a mod translating a mouse-and-keyboard game, not a world built hand-first.

Locomotion is smooth thumbstick walking and turning, with crouch and prone, and there's no snap-turn option — fine for VR veterans, worth knowing if you're sensitive. The flat game's long, low-poly look, which always read as a stylistic choice, turns out to be a VR advantage: there's very little for the GPU to do, so you've got generous headroom to push resolution without the frame drops that plague denser survival sandboxes.

## Getting it running

Install is advanced but clean. You grab the zip from the GitHub Releases page, copy the `Modules` and `Unturned_Data` folders into your Unturned install directory, and merge them — nothing in the game gets overwritten. Start SteamVR, launch Unturned with BattlEye off, and open a singleplayer game. Uninstall is just deleting `Modules/UnturnedVR`, because the mod touches no game files. No Workshop subscription, no launcher, no dependency chain — the friction is the file merge and the anti-cheat toggle, not a dependency hunt.

The author shipped three releases in the ten days after the first public build, and the repo shows zero open issues. That's a young, active project, not a stalled one — but it also means you're an early adopter running a mod that's explicitly unfinished. The version ladder matters if you want the newest features: the physical melee and grenades live in the test build, not the stable one.

## A B-tier sandbox you build yourself

What keeps it out of the A tier is maturity. The transformation is real — real hands, real holsters, real sight-to-eye aim on a game with a decade of maps and Workshop content behind it. But reloading and melee still fall back to flat input on stable, the inventory is a laser pointer, and BattlEye-off means you're playing alone or on a private server by design. Those aren't polish nits; they're the difference between "this is the way to play" and "this is the way to play alone, for now."

If you've ever wanted to actually stand in Unturned's world instead of clicking through it, this is the mod that finally lets you — free, open-source, and improving weekly. Just go in knowing the servers are closed and the work isn't done. For a VR enthusiast who'll trade a little unfinished rough edge for the dumb, specific joy of shouldering a rifle off their own hip, that trade is worth making.
