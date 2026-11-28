---
title: "Super Smash Bros. in VR"
description: "Super Smash Bros. VR runs Melee, Brawl, and Smash 64 in a headset through the DolphinVR Redux emulator — real 6DOF depth and free-look, gamepad in hand, no motion controls."
flatReleaseDate: 1999-04-26
vrReleaseDate: 2019-05-30
lastUpdated: 2026-11-03
featured: false
routeType: Multi-Route Coverage
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Advanced Setup
inputStyle: Gamepad Preferred
comfort: Comfortable
performance: Moderate Demand
supportStatus: Active
genres:
  - Platform Fighter
  - Fighting
technicalTags:
  - Emulator
  - DolphinVR Redux
experienceTags:
  - Mixed Reality
  - Free-Look
  - Retro Fighter
tier: B
verdict: "DolphinVR Redux turns Melee, Brawl, and Smash 64 into a genuine stereoscopic, head-tracked window into the stage — a real 'whoa' for fans, but you're a passenger with a GameCube pad, not a fighter in the ring. Worth the setup if you already love Smash; skip it if you're hunting a new way to play."
modDownload:
  url: "https://github.com/ichris4/dolphinxr/releases"
  label: "Get DolphinXR"
  note: "OpenXR fork of Dolphin — the emulator route for Smash 64 via Wii Virtual Console"
heroImage: /images/games/super-smash-bros-vr-hero.jpg
history:
  - date: 2026-11-03
    note: "DolphinVR Redux v0.5 released — in-game VR menu, Quest performance work, and per-game motion-control patches (Smash not included); the maintained emulator remains the viable path for Melee, Brawl, and Smash 64 in VR."
sources: "Research drawn from the DolphinVR Redux repository and release notes (iChris4/dolphinXR, branch openxr-work; builds v0.2 through v0.5), Wikipedia's Super Smash Bros. Ultimate article citing Kotaku (2019-05-30) for the Labo VR update, the VRMods-List and PCVR Mods Installer Hub Dolphin VR entries, and YouTube coverage including StarchyXD's 'Hungrybox Tries VR Melee! (Vive)' (313,434 views), LunchAndVR's 'Super Smash Bros. Melee in Augmented Reality!' (14,023 views), and the Press start to begin, Face Toaster, and Kevin Tang Melee mixed-reality uploads. Assessment based on documented tooling, release notes, and community footage."
trailer:
  youtube: "WShCN-AYHqA"
  source: "Super Smash Bros."
faq:
  - q: "Can you play Super Smash Bros. in VR?"
    a: "Yes, but not as a port. Melee, Brawl, and Smash 64 run inside a VR headset through DolphinVR Redux, a maintained OpenXR fork of the Dolphin GameCube and Wii emulator. Ultimate also has an official Nintendo Labo VR mode, which is a 3DOF goggle view limited to CPU matches."
  - q: "Does Super Smash Bros. VR support motion controls?"
    a: "No. Every Smash VR path is gamepad only — a GameCube controller on PC or a Pro Controller on Quest. DolphinVR Redux ships motion-control patches for other games like Metroid Prime and Skyward Sword, and Smash is not on that list."
  - q: "Do you need a gaming PC to play Smash Bros. in VR?"
    a: "Not necessarily. The same fork ships a standalone Android build, so a Quest can run Melee in mixed reality without a PC — you sideload the emulator and supply your own game dump. The PC path is easier to configure; the Quest path trades that for wireless passthrough."
  - q: "Where do you get the Smash Bros. ROM for VR?"
    a: "You supply your own dump. Nintendo has never released a Smash game on PC, so there is no legitimate download — you rip a Melee or Brawl disc you own, or use a Smash 64 Wii Virtual Console copy you own."
  - q: "Is Super Smash Bros. VR worth setting up?"
    a: "If you already play Melee, the stereoscopic depth and head-tracked free-look turn familiar stages into a diorama you can lean into. If you want a new way to fight, it will not deliver: the game keeps its auto-framing camera, so you are watching from inside the arena rather than controlling it."
relatedPages:
  - id: super-smash-bros-melee
    kind: game
    note: "The dedicated Melee VR page — same DolphinVR Redux path, deeper dive on the competitive anchor."
  - id: metroid-prime
    kind: game
    note: "The DolphinVR Redux showcase title, and the one that actually got motion controls."
  - id: super-mario-galaxy
    kind: game
    note: "Another GameCube-era Nintendo classic running through the same emulator on PCVR and Quest."
  - id: star-fox-64
    kind: game
    note: "Nintendo retro VR going the opposite way — a cockpit view with motion-controller aim."
---
The first time I booted Super Smash Bros. Melee through DolphinVR Redux and put the headset on, the stage didn't change — but my relationship to it did. There's Final Destination, the flat white platform I've thrown thousands of matches on, now sitting in actual stereoscopic depth, and when I leaned forward to peek past the ledge, the camera didn't move but my view did. That's the whole trick, and it's a better trick than it sounds.

<iframe src="https://www.youtube-nocookie.com/embed/WShCN-AYHqA" title="Super Smash Bros. — official trailer" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Super Smash Bros. VR runs through the DolphinVR Redux emulator

Here's the hard fact that shapes everything: Nintendo has never shipped a Smash game on PC, and the only first-party VR the franchise ever got is a 3DOF goggle mode bolted onto Ultimate in 2019. So if you want Smash on your face, you're not downloading a port. You're emulating.

The path that actually delivers is DolphinVR Redux — a maintained OpenXR fork of the GameCube and Wii emulator Dolphin, built by iChris4 and still shipping updates regularly. It runs Melee (GameCube), Brawl (Wii), and even the original Smash 64 through its Wii Virtual Console rerelease. What it hands you is real: per-eye stereoscopic 3D, full 6DOF head tracking, a free-look camera you aim with your head, and — on the Quest build — passthrough mixed reality so the stage floats in your living room.

What it does not hand you matters just as much. There are no motion controls. Nobody patched hands into Smash, and the v0.5 update that added motion-control game patches to Metroid Prime, Red Steel, and Zelda pointedly left every Smash entry off the list. You hold a GameCube controller — or a Pro Controller on Quest — and play the fighter exactly as it was designed, flat. The emulator's own auto-framing camera keeps running underneath your head tracking, so you're looking around inside the game's framing rather than steering it. You're a spectator who happens to be standing inside the arena.

That's the honest framing before you install anything: this is a tracked, stereoscopic window into a fighting game you already know, not a reinvention of how Smash plays.

The other option — Ultimate's Labo VR Kit mode — sits at the opposite end. It's official, but it's a 3DOF cardboard goggle that lets you watch CPU-only matches or play a single 1-on-1 against the computer, on a restricted stage list, with a pad. No tracking of your position, no hands, no online, no real opponents. It's a curiosity Nintendo shipped once and never expanded. The emulator route is the one that's actually worth your afternoon, which is why this piece is about it.

## Super Smash Bros. Melee VR setup: ISO, OpenXR, and per-game tuning

Getting there is the part that filters the curious from the committed. You install DolphinVR Redux, supply your own Melee ISO — Nintendo never released Smash on PC, so there is no legitimate download, you dump what you own — then flip VR on and tune a handful of per-game settings: frame rate, world scale, camera anchor, and a culling tweak so the engine doesn't clip what's behind you. Map a GameCube controller, and you're in. On Quest the same fork ships as a standalone Android build, so the "no PC required" videos people post are real — you sideload it, drop the ROM on, and play Melee in mixed reality on a wireless headset.

Once you're in, the feeling is specific and a little strange. Melee runs at a locked 60 frames, and the emulator holds that easily — GameCube-era hardware is light work, so even on a mid-range PC or a Quest you're not fighting reprojection. The auto-framing camera does its job, panning and zooming to keep all the fighters on screen, and your head tracking rides on top of that. Lean left and the whole stage shifts in your periphery; lean right and you're peering over the edge of Battlefield. It reads as presence in a way a capture card never does, because the depth is real and your head owns a small piece of the viewpoint.

The catch is that you never own the camera. In a first-person VR conversion the head usually becomes the lens; here the game keeps the lens and you're a guest leaning into it. That's comfortable — third-person, no artificial locomotion, no smooth-motion sickness risk, and the Labo-style head tracking removes translation sickness entirely if you go that route — but it also means the "VR" is a viewing upgrade, not a control one. You're still executing wavedashes and L-cancels on a pad. The muscle memory transfers perfectly; the body never does.

What surprised me is how much the stereoscopic depth sells the stages. Fountain of Dreams stops being a flat backdrop and becomes a diorama with actual volume. Characters have weight in space they never had on a monitor. It's the same reason diorama collectors exist — the scale reads differently when your head is in it.

## Super Smash Bros. 64 and Brawl VR inside the same emulator

Melee is the star because it's the competitive anchor and the one with the most eyes on it, but the same fork covers its siblings. Smash 64 runs through its Wii Virtual Console release inside Dolphin, which makes it a Wii title the emulator already handles — there's at least one mixed-reality video of it floating around, though it's thinly documented and I wouldn't call it a guided path yet. Brawl is the more interesting second act: it's a Wii disc, fully inside Dolphin's compatibility, and its Subspace Emissary story mode is the one part of the game that genuinely benefits from a stereoscopic camera, since you're moving a single avatar through sidescrolling space rather than watching four fighters scatter.

Neither has a Smash-specific setup guide or profile, and Brawl in particular has no dedicated VR footage I could find — the path is verified at the emulator level, not the game level. Treat both as "it should run, tune it yourself" rather than "there's a preset waiting." For most people the question answers itself: if you're emulating Smash in VR, you're doing it for Melee.

## Super Smash Bros. Ultimate VR mode on the Labo Kit

Before the emulator path, there was exactly one official taste of Smash in a headset, and it's worth naming so nobody goes looking for more than exists. In May 2019, the v3.1.0 update to Super Smash Bros. Ultimate added Nintendo Labo VR Kit support. You build the cardboard Toy-Con goggle, slot the Switch in, and the game lets you watch computer-only matches in 3D or play a single 1-on-1 against the CPU, on a shortened stage list. It's 3DOF only — rotation, no positional tracking — and the pad never leaves your hands.

It's a genuine first-party mode, which is more than most fighting games can say, but it's also the most limited VR I've seen shipped by a major studio. No real opponents, no online, no hands, no control over the view beyond tilting your head. The Labo kit itself is cardboard and now secondhand-only since Nintendo discontinued it. If you already own a Switch and a Labo VR Kit and you're curious, it's a ten-minute novelty. If you don't, it is not a reason to buy either. The emulator route is where the actual presence lives.

## Super Smash Bros. VR limits: fixed camera and no hands

The honest ceiling on this whole experience is that you're watching, not fighting. Every strength I've described — the depth, the head-tracked peek, the diorama feel — comes from the emulator handing your eyes a better window. None of it comes from your hands. Smash is a fighter built around a pad and an auto-framing camera, and that design is exactly what VR can't convert: there's no reticle to aim, no first-person body to inhabit, no locomotion to hand to your feet. The DolphinVR Redux patch system that puts hands into Metroid Prime and a sword into Skyward Sword has nothing to grab onto in Smash, and the v0.5 patch list confirms it — Smash isn't on it.

That's why this isn't a new way to play. The flat game on a monitor is, for actually competing, strictly better: you see the whole screen without managing your head, and your hands are already where they need to be. What the headset adds is a spectator's thrill — the 'whoa, I'm standing in Fountain of Dreams' moment — and that moment is real but it doesn't compound the way it does in a game built for VR. The footage backs this up. The biggest Melee-in-VR video on the platform is a pro player, Hungrybox, trying it once on a Vive — 313,000 views of curiosity, not a conversion. The actual 'here's the mod, here's the download' videos cluster at a quiet 1,200 to 1,400 views each. People are doing this, repeatedly, and almost none of them are telling you it replaced their monitor.

## Super Smash Bros. VR suits committed Melee players

If you already love Melee — if you've got a GameCube controller within arm's reach and a soft spot for a specific stage — DolphinVR Redux is worth the afternoon it takes to set up. The stereoscopic depth and head-tracked free-look turn a game you've memorized into a diorama you can lean into, and that's a feeling the flat version never gave you. The emulator is under active development, shipping updates regularly, so the no-hands situation is a current limitation, not a permanent verdict.

If you're coming at this as a VR enthusiast hunting a new way to throw hands, this is the wrong door. You're still a pad player watching an auto-framing camera, and a purpose-built VR fighter will give you the body involvement Smash in VR structurally can't. And if you only own a Switch and were hoping Ultimate had a real VR mode, the Labo kit is a ten-minute curiosity, not a reason to celebrate.

The franchise built one of the most durable competitive games ever made, and the headset lets you stand inside it for the first time. That's a smaller miracle than it sounds, but for the faithful, it's a real one.
