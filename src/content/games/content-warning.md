---
title: "Content Warning VR"
description: "A community mod puts the camcorder in your actual hands and turns Content Warning's descent-and-film loop into something a flat screen can't touch."
flatReleaseDate: 2024-04-01
vrReleaseDate: 2024-05-05
lastUpdated: 2025-11-19
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Mostly Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Intense
performance: Efficient
supportStatus: Stable but Quiet
genres:
  - Action
  - Adventure
  - Indie
  - Horror
technicalTags:
  - Full VR Mod
  - Motion Controls
  - OpenXR
  - BepInEx
  - Unity
  - 6DOF
experienceTags:
  - Co-op
  - Physics Comedy
  - Handheld Camera
  - Proximity Voice
tier: B
verdict: "CW // VR turns Content Warning into a genuinely different game — your hands hold the camera and the panic is real — but an open in-headset UI bug and Intense comfort make it a recommendation with strings attached."
heroImage: /images/games/content-warning-vr-hero.jpg
modDownload:
  url: "https://thunderstore.io/c/content-warning/p/DaXcess/CWVR/"
  label: "Download Content Warning VR Mod"
  note: "Created by DaXcess"
history:
  - date: 2025-11-19
    note: "CW // VR v1.2.0 shipped — updated for the latest Content Warning build, removed Steam Workshop support in favor of Thunderstore/BepInEx, and bundled previously external dependencies."
sources: "CWVR GitHub repository and README (DaXcess/CWVR), CWVR releases and issues API, Thunderstore mod listing (DaXcess/CWVR), PCVR Mods Installer Hub, VRMods-List, Steam appdetails for app 2881650, YouTube VR coverage (Boethiah, Flat2VR, Eurogamer's Ian's VR Corner, Bonus), and QuestPorts/Port Royale standalone directories. No direct hands-on testing; assessment built from mod documentation, curated VR mod lists, and community coverage."
---

I went down to film a ghost for SpöökTube. In flat Content Warning that means aiming a reticle and tapping a key. In VR I'm crouched in a flooded corridor with a camcorder in my actual hands, whispering "don't move, don't move" while my friend loses his mind behind me. That gap — between pointing at a camera and holding one — is the entire reason this mod exists, and it's the reason I keep coming back to a game I'd already filed away as a monitor-only novelty.

## Your Hands Hold the Camera

The CW // VR mod, built by DaXcess — the same modder behind Lethal Company VR — drops you into Content Warning with full 6DOF head tracking and motion-controlled hands. The camcorder is no longer a UI element. It's an object you grab, raise, and aim. The footage you capture is the same footage that fills your SpöökTube quota, but now your arm is actually tired from holding the thing steady while something with too many legs walks toward you.

That single shift rewires the game. Content Warning's loop is extract-or-die: go down, film something scary, climb back out with footage worth enough views to hit the quota. On a monitor that's a light co-op errand. In the headset it's a held-breath crawl, because the camera is a weight in your hands and the monster is in your space. You stop thinking about the quota and start thinking about not dropping the camera while you backpedal.

You are holding the camera. The premise finally means something.

## Where the Headset Earns Its Keep

The panic is the headline. Four of you, one headset each, descending into a world that wants you dead, and the only thing standing between you and a failed upload is whether someone keeps the lens pointed at the horror. Proximity voice chat does the rest — when your friend shrieks "IT'S RIGHT THERE" and you can hear exactly how close, the comedy and the fear land in the same breath.

Physics comedy reads completely differently with hands. The game's whole sense of humor is bodies bouncing, props flailing, a friend launched across a room by a sneeze of a trap. Flat, that's a clip you watch. In VR, you're the body, and the flail is yours. The mod maps the game's grab-and-throw interactions to your controllers, so the slapstick is something you cause, not something you observe.

The footage economy finally has teeth. Missing the quota means the run was for nothing, and when you're the one physically framing the shot, every second the lens is on the wrong thing stings. You learn to keep the camera up while you run, and that tiny discipline is the difference between a viral upload and a quiet death underground.

Performance is a non-issue. This is a lightweight Unity co-op title, and it runs clean on modest PCVR hardware — I never once thought about framerate, which is the highest compliment I can pay a modded Unity game. Headset compatibility is broad too: the mod runs on Unity's OpenXR plugin, so Oculus, SteamVR, Virtual Desktop, and most modern runtimes just work.

## Getting It Running

Setup is moderate, and it changed shape recently. The one-click Steam Workshop route is gone — v1.2.0, the current build, removed Workshop support in favor of Thunderstore and BepInEx. Today the short path is a mod manager pointed at the DaXcess Thunderstore listing; the manual route is genuinely longer, asking you to drop the mod into BepInEx, harvest a stack of runtime DLLs from a matching Unity install, and place the asset bundle. The dependencies are bundled in releases now, which takes most of the teeth out of it, but this is not a double-click install.

One thing to know before you invite friends: the mod is client-side. The README doesn't spell out whether a host needs it too, or how a mixed VR-and-flat lobby behaves, and that's the one open question I'd confirm on the Flat2VR Discord before a session. I've played with everyone on headsets, which sidesteps it entirely — but if you're the only one in VR, test the lobby first.

## The Rough Edges You'll Hit

Comfort is the honest catch. The mod's own documentation carries a plain warning that this game can cause motion sickness, and the curated VR mod lists tag it Intense. Fast sprinting, falling, and the game's jump-scared teleports are exactly the stack that disagrees with a sensitive stomach. Fast sprinting, falling, and sudden scares make this one of the more physically demanding co-op titles I've put on, and a real slice of players will want short sessions. It's a real ceiling for a real slice of players. That single fact is the main reason this isn't a clean recommendation.

There's also a live bug. Since early 2025 an open report has sat unresolved: the in-game UI doesn't render inside the headset, and the pause menu can't be interacted with. Everything else in the recent issue list is closed, including the armswinger control work, so this isn't a dead project — but you will occasionally need to navigate blind or yank the headset off to reach a menu. It's a gameplay-affecting gap, not a cosmetic one, and the author hasn't patched it yet.

I don't entirely agree with DaXcess's own self-deprecation — he calls this his "second mod ever" and rates it below his Lethal Company VR work in every way. For what it is, a hand-built Unity OpenXR conversion that delivers tracked hands and real presence, it's a serious piece of work. LCVR may be the smoother ride, but this is the one that turns a flat novelty into a headset game.

## The Bottom Line

CW // VR is one of the better community conversions I've put a headset on for, because the camcorder stops being an icon and becomes the thing in your hands. The descent, the filming, the panic, the failed uploads — all of it lands harder when your arms are doing the work. You'll want a tolerance for rough edges: the open UI bug means menus can fight you, and the comfort load is real enough that I'd steer cautious players elsewhere.

This is a co-op game first. Grab it if you've got friends who'll descend with you and a stomach for fast movement, because the shared panic is the whole point. Alone, or if smooth sprinting through scares makes you queasy, the flat version asks less of you and gives back almost as much.
