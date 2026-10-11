---
title: "Bomb Rush Cyberfunk VR"
description: "A community BepInEx mod drops Team Reptile's cel-shaded skating adventure into VR — third-person on a gamepad by default, with an optional first-person mode that puts VR hands on the board."
flatReleaseDate: 2023-08-18
vrReleaseDate: 2025-01-24
lastUpdated: 2025-01-24
featured: false
routeType: Full VR Mod
platforms: ['PCVR']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Moderate Demand
supportStatus: Stable but Quiet
genres:
  - Action
  - Adventure
  - Skating
technicalTags:
  - Full VR Mod
  - BepInEx
  - Third-Person VR
  - First-Person VR
experienceTags:
  - Skating
  - Open World
  - Graffiti
  - Trick Combos
tier: B
verdict: "A faithful VR window into one of the best skating games of the decade — best enjoyed third-person on a gamepad, with an optional first-person VR-hands mode for riders with strong legs."
heroImage: /images/games/bomb-rush-cyberfunk-vr-hero.jpg
modDownload:
  url: "https://github.com/AstienVR/Bomb_Rush_Cyberfunk_VR/releases"
  label: "Download Bomb Rush Cyberfunk VR Mod"
  note: "Created by AstienVR"
sources: "Research compiled from the AstienVR BombRushCyberfunk_VR GitHub repository and README, the Thunderstore mod page, PCVR Central listings for both the Astien and Cyberhead mods, the VRMods-List directory entry, Astien's demo video, and NotNite's Cyberhead README. Assessment reflects documented mod capabilities and structured compatibility tags."
---

There's a specific kind of joy in leaning into a grind while the New Amsterdam skyline smears past your peripheral vision, and Bomb Rush Cyberfunk sells that feeling hard on a flat screen. Strap a headset on and the question becomes: does the world hold up when you're actually standing inside it? I spent a Sunday afternoon chasing combo timers through the mod's third-person view, then flipped into first-person to see whether VR hands change the ride. Here's what's real.

There's no official VR mode here — Team Reptile never shipped one, and nothing in the flat release points that way. What you get is a community mod: AstienVR's BombRushCyberfunk_VR, a BepInEx plugin that hooks the Steam build and renders it in 6DOF inside your headset, headset-tethered to a PC. It landed in early 2025 and, per the author, makes the game "fully playable in VR." It's a single-maintainer project, and that cuts both ways — one person means a coherent vision and fast fixes when something breaks, but it also means you're trusting the whole experience to one person's free time. Right now it's the only way this game gets into VR. An earlier attempt, NotNite's Cyberhead, proved the concept back in early 2024 but stayed an unfinished proof-of-concept — broken menus, broken cutscenes, broken graffiti tagging — so treat it as a historical footnote, not a contender.

Getting it running is about as gentle as Unity modding gets. It's a BepInEx plugin — the standard Unity modding framework — so you drop the folder into your game root, run the included MoveFiles.bat, and launch. A mod manager handles it if you'd rather not touch the file system directly. The one real gotcha: flipping into first-person view and motion controls means opening a config file and changing a flag, which is a small step but a step the default install won't take for you. Also know that the mod writes into the game's Bomb Rush Cyberfunk_Data folder, so if you ever remove it, you'll want to clean that up by hand rather than just deleting the mod folder — otherwise you can leave the game's files modified.

How it plays depends entirely on which view you pick. In third-person, you're on a gamepad — left stick moves, right stick handles the camera, and all the trick inputs are exactly where they sit in the flat game. That's the mode I'd hand to anyone who just wants the game bigger and more present. The skating reads beautifully from behind: the cel-shaded streaks, the way your character leans through a manual, the spray of paint when you tag a wall — it all has weight when your head is the camera. You're not waving your arms, but you are inside the city, and that's the part that matters for a game this stylish.

First-person is where the VR hands come in. Switch the config flag and you're on the board yourself, VR controllers mapped to the tricks, no gamepad required. It's a genuinely different feel — closer to the fantasy of actually riding — but it's also the less comfortable option. The author flags the full-immersive setting (which adds full in-game head movement) as something that needs strong VR legs, and I'd believe it: Bomb Rush is a fast, whip-pan traversal game, and putting your own head on a character who's grinding a rail at speed is exactly the kind of motion that catches people out. The motion controls are first-person-only, so this isn't a "use controllers the whole time" setup — it's a toggle you flip when you want the deeper immersion and can stomach it.

Performance sits in the moderate band. It's a Unity game from 2023 with a clean art style rather than heavy rendering, so a mid-range PC pushes it fine, but it's not a featherweight either — the draw distance of an open city and the particle work during big combo finishes will ask for headroom if you're on older hardware. I never saw it buckle, but I wasn't running it on a potato either.

What actually lands is the city. New Amsterdam in Bomb Rush is a joy on a monitor and a different thing on your face — the verticality of the districts, the gap between rooftops you can now feel in your gut, the way a combo line carries you from a back alley up onto a billboard. This is a game built around movement through space, and VR is movement through space concretized. The 6DOF head tracking means you're craning to watch a rival tag a wall above you, not panning a fixed camera. That alone justifies the headset for anyone who already loves the flat game.

And the flat game is worth loving. Bomb Rush Cyberfunk is one of the best skating games of the last decade — a Jet Set Radio successor with real style, a soundtrack that earns the word, and trick systems with enough depth to keep you chasing a cleaner line for an hour. The mod doesn't dilute any of that. It hands you the same campaign, the same crew battles, the same graffiti spots, just rendered around your head instead of behind a screen. I'm not grading the mod up because the base game is great — but I'm not pretending the mod invented the fun either. The fun was already there; the mod lets you stand inside it.

The honest catch is that "inside it" mostly means "watching it from behind you, in a headset." Third-person-on-gamepad is the flat game with presence bolted on, not a reinvention. It doesn't transform Bomb Rush the way a true first-person VR skating sim would — there's no physical pushing, no leaning into carves with your body, no weight you control with your hands unless you flip the first-person flag and accept the comfort cost. That's the line that keeps this out of the top tier: the default experience is wonderful and present, but it's a window, not a rebuild.

Support is steady without being loud. AstienVR pushed the working build out and it's stayed live and installable; it isn't abandoned, but it isn't a living project shipping weekly patches either. For a free community mod of a game this size, that's a fair trade, and it's worth knowing before you install that you're betting on one person's continued goodwill rather than a studio-backed pipeline.

So who's this for? If you already wanted to play Bomb Rush Cyberfunk — and if you own a VR headset and like skating games, you should — the mod is an easy yes: install it, play third-person on a gamepad, and enjoy a stylish city you can finally inhabit. Flip on first-person VR hands only if your stomach signs off on fast, constant motion. It's not the transformative VR skating dream, and Cyberhead's broken proof-of-concept is a dead end you should skip. But a great game, made present in your headset, is exactly what this mod delivers — and that's enough to earn the afternoon.
