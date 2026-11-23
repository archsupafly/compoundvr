---
title: "How to Play World of Warcraft in VR (WoVR Setup, Settings & Optimization)"
description: "How to play World of Warcraft in VR: WoVR setup, settings, and optimization for the 3.3.5a fan mod. Covers performance, Quest patch, and WoW Forever VR compatibility."
pubDate: 2026-11-22
lastUpdated: 2026-11-23
author: "Ian"
category: guide
heroImage: /images/articles/how-to-play-world-of-warcraft-in-vr-hero.jpg
tags: ['world-of-warcraft', 'wow-vr', 'wovr', 'vr-mod', 'pcvr', 'steamvr', '3.3.5a', 'private-server', 'guide', 'wow-forever-vr']
relatedPages:
  - id: world-of-warcraft
    kind: game
    note: "The WoVR game page covers the mod; this guide covers the setup."
  - id: virtual-desktop-guide
    kind: article
    note: "Quest owners reach SteamVR over a PC streaming bridge — the linked guide covers that setup."
sources: "GitHub (ProjectMimer/WoVR repo and issues), the WoVR README, Road to VR (2024-04-29), Blizzard EULA, YouTube coverage, and Flat2VR Discord (distribution only)."
faq:
  - q: "Can you play World of Warcraft in VR?"
    a: "Yes, with the fan-made WoVR mod on a compatible World of Warcraft 3.3.5a (Wrath of the Lich King) client through SteamVR/OpenVR. It is not an official Blizzard VR mode and does not support retail WoW."
  - q: "Does WoW Forever work in VR?"
    a: "No. There is no working WoW Forever VR mod. The closest option is playing WoW Forever in cinema mode in a headset, optionally with a first-person addon such as Terren's Forever First Person. For actual WoW VR with headset tracking, WoVR requires a compatible 3.3.5a client."
  - q: "Can you play retail WoW or modern WoW Classic in VR with WoVR?"
    a: "No. WoVR targets patch 3.3.5a only. Retail, official modern Classic, Season of Discovery, and Hardcore are different client/anti-cheat paths and are not supported by WoVR."
---

## What is WoVR and can I play retail WoW in VR?

WoVR is a free, fan-made VR mod for World of Warcraft, built by Streetrat and Marulu under the Project Mimer name — the same two behind the XIVR mod for Final Fantasy XIV. Blizzard didn't make it and doesn't support it. It takes the legacy WotLK client, hooks the D3D9 renderer, and pushes stereo output to a SteamVR headset.

The question I get most is whether you can play *current* WoW in VR. The answer is no. WoVR targets patch 3.3.5a only — the final build of Wrath of the Lich King from 2010. Retail, official Classic (any era), Season of Discovery, Hardcore — none of them work. Those are different binaries with live anti-cheat in the path, and WoVR doesn't touch them. If you want to stand in Stormwind in VR, you're doing it on a private 3.3.5a server, full stop.



## What do I need to play WoW in VR?

Prerequisites first. Some are documented by the mod; the rest is community practice, and I say which is which.

- **A Windows PC.** The mod is a D3D9 proxy plus a Windows-only on-screen keyboard helper. Linux is possible only through Proton — someone reported a working "proton hotfix" setup as recently as October 2026, but that's a community path, not something the mod supports.
- **A SteamVR/OpenVR runtime.** The source tree has SteamVR and OpenVR code and nothing for OpenXR. If your headset speaks SteamVR, you're fine. A Quest reaches it through PC streaming (more on that below).
- **A 3.3.5a client and a private-server account.** The mod ships no game files. You supply a 3.3.5a client (unmodified, 4GB-patched, and lua-unlocked executables all work), point its realmlist at a private server, and log in flat first to confirm it works.
- **VR motion controllers.** The control scheme assumes two sticks, two triggers, A/B/X/Y, grips, and stick clicks — Touch- or Index-class. The README frames it as a seated experience with motion controllers. You also keep a keyboard and mouse within reach; you'll need them.
- **A "beefy" PC, unspecified.** Nobody has published a minimum GPU. The mod renders internally at 2× native resolution per eye by default, on a single-threaded 2004 engine, so both CPU per-core speed and GPU fill rate matter. I won't quote you a card tier, because none is documented.

The precompiled build itself comes from the Flat2VR Discord. The GitHub repo has no releases and no tags — it's source, configs, and a README. The README's first line points you at Discord for the actual binaries and install steps.

## How do I install WoVR and set it up?

There is no public, step-by-step install guide. The mod's own documentation tells you to visit the Flat2VR Discord for install instructions and support, and that URL redirects straight into Discord — not a webpage. So the order below is reconstructed from what the files and README establish; confirm it against the Discord or a community video before trusting it.

What's documented as real is that the mod generates a `/vr/config.txt` on first launch. It ships `config/actions.json` and `config/actions_touch.json` (the controller action-set definitions, including a Touch variant). There's an `OSK.exe` on-screen keyboard that needs the game launched as administrator.

The install order:

1. Install SteamVR and confirm your headset tracks normally.
2. Get a clean 3.3.5a client. Set its realmlist to your chosen private server and log in flat to prove the client works.
3. Pull the precompiled WoVR build from the Flat2VR Discord.
4. Drop the proxy DLL and its support files next to the client executable. The repo names the project `dxProxyWoVR` and the proxy source (`proxydll`), so the deployed artifact is a `d3d9`-class proxy — but the exact deployed filename and folder layout are not documented publicly. Confirm on Discord.
5. Launch the game once to generate `/vr/config.txt`, then set snap-turn degrees, your mounts, and any buffer options there.
6. If you want the floating on-screen keyboard, launch the game as administrator.
7. Set windowed mode in-game, set resolution and UI scale per the Discord guide, then verify the action sets load.
8. Click the right stick to recenter and toggle first/third person.

Steps 4, 5, and 7 have the least public documentation. The folder layout, the exact DLL name, and the in-game settings all live behind the Discord gate.

## What is the WoVR Quest Community Patch?

If you're on a modern Quest headset, the base WoVR build isn't the one you want. A community patch by Briinc3, the [WoVR Quest Community Patch](https://github.com/Briinc3/WoVR-Quest-Community-Patch), builds on ProjectMimer's original because that build had rendering and camera problems that made it close to unusable on current Quest hardware with SteamVR.

It's the same class of mod, a proxy next to your 3.3.5a client. Install this instead of the older precompiled build and treat it as the current community baseline.

What it fixes, from its own changelog:

- **Eye flicker and stereo breakage.** Rapid flickering between the eyes, one eye rendering black or wrong, and misaligned stereoscopic views are corrected, with a reworked rendering path for a stable image.
- **The camera swing.** Changing direction in the base build could rotate your view by roughly 180 degrees. The patch removes that movement-driven rotation and keeps head tracking independent of character movement.
- **Walk/run toggling.** Right-stick camera movement no longer flips the character between walking and running.
- **A visible pointer.** The interaction laser is green and easier to read against WoW's interface.
- **UI pointing.** Its notes verify pointer interaction with bags, the character sheet, the quest log and the talent window, with tooltips and left/right click intact.
- **Quest controllers.** Independent left and right grip detection, grip modifiers, full Action Bar 1-12 access, a two-page action bar, and up to 24 controller-reachable ability slots.

Two things to know before you install it:

- **Double nameplates.** With nameplates on you'll see two slightly offset copies. The author documents roughly 24 hours of investigation and left it as a known visual limitation; targeting and combat still work.
- **Memory crashes.** WoW 3.3.5a is 32-bit. Apply the Large Address Aware (4GB) patch to Wow.exe or expect "Not enough memory resources" in Dalaran, big pulls and effect-heavy fights. The patch README recommends it, and suggests launching Wow.exe at High CPU priority for smoother frames.

Scope note: "Quest" here means Quest controllers and headset over PC streaming or Link. This patch doesn't make WoW run standalone on the headset.

## What are the WoVR controller bindings?

The mod maps a lot onto two controllers, but there's a hard input-budget limit you should know before you commit. Only keys 0–3, 8, and 9 are reachable from the controller itself. The rest of a 30-ability rotation has to come from keyboard, mouse, or an action-set workaround. That comes from the mod's own control map.

The mapping (EG = either grip held, LG = left grip, RG = right grip):

- **Left hand angle** — direction of movement, flying, swimming.
- **Left stick** — character movement.
- **Left trigger** — next action set (hold left grip: previous action set).
- **Left stick click** — random mount; set the specific ground/flying mount in `config.txt` (hold either grip: key 1).
- **X button** — Esc (hold either grip: key 2).
- **Y button** — toggle map (hold either grip: key 3).
- **Right hand angle** — ray into the world: targeting, aiming, UI.
- **Right stick** — camera snap-turn (hold left grip: camera zoom).
- **Right trigger** — left click (hold right grip: right click).
- **Right stick click** — toggle first/third person + recenter (hold either grip: key 0).
- **B button** — next target (hold either grip: key 9).
- **A button** — jump (hold either grip: key 8).

Ray-based targeting is the headline feature. Point your controller at an NPC, enemy, or mining node and pull the trigger to interact. AoE abilities like Mage Blizzard or Hunter traps drop on the ground where you point. The "Legacy Movement" mode (from XIVR) lets your character run in the direction the stick points at full speed without backpedaling, and "Auto Face Target" turns you toward your target on each action.

## What settings actually matter in WoVR?

Settings live in three places, and only the mod-side ones are documented.

**In `/vr/config.txt` (mod-side, documented):**
- Snap-turn degrees — both vertical and horizontal, adjustable.
- Your random-mount choices — a specific ground mount and flying mount.
- `gameMultiplier` — the intended internal resolution multiplier. Heads up — a GitHub bug report (#1) says this value is ignored because the config file is read only after `hmdBufferSize` is set, so the effective value is hardcoded to 2. There's no merged fix.
- `hmdBufferSize` — a real config key, but its accepted values and meaning are not documented publicly. Don't guess at it.

**In-game / WTF (partially documented):**
- You can set render resolution above your monitor's maximum via the WTF file. The catch, straight from the README: your mouse cursor is still confined to what the desktop shows, so clicking UI past the monitor edge fails.
- Windowed mode plus a desktop resolution is the usual setup for this class of mod.
- UI scale, plus an optional made-for-VR UI (Discord-only) with windows attached to your hands and face.

**In SteamVR (inferred):**
- Per-app render resolution and supersampling stack multiplicatively on top of the mod's internal 2×. Double-scaling is the classic performance trap. Cap it.

Graphics levers the community names — shadows, view distance, projected textures, ground clutter, MSAA — aren't in the README. They're community knowledge, not documented mod settings.

## What actually improves WoVR performance?

Some of this moves frames by mechanism; some is folklore. The two get blurred together constantly, so I split them.

**Moves frames (mechanism-backed):**
- Lower the internal resolution or per-eye buffer. The default 2× per eye on a DX9 client is the single biggest lever, and the `gameMultiplier` bug means you can't turn it down through config — you'd need a fork, a patch, or a Discord build.
- Cut shadows, view distance, projected textures, and ground clutter. These are fill-rate and CPU draw-call costs on an engine that was never built for this.
- Disable in-game MSAA and let the compositor resolve AA instead.
- Reduce your addon count and heavy raid frames. 3.3.5a's Lua and its draw calls are single-thread-bound, so addon load hits the same thread that feeds VR.
- Cap supersampling in SteamVR so it doesn't multiply the mod's 2×.
- Close the desktop mirror or drop the desktop resolution if the mirror is expensive.

**Folklore (community claims, not measured here):**
- "VR needs a 4090." Nothing supports a specific card tier. The ceiling is per-eye resolution times fill rate, not a GPU class.
- "AMD can't run the VR UI." The README's only UI complaint is low resolution on 1080p monitors. AMD-specific breakage is community-reported, and nothing public confirms a driver-level cause. Treat it as unconfirmed.
- "Disabling the desktop mirror doubles FPS." Plausible, unmeasured. I'm not printing it as a fact.
- "Private-server population affects FPS." Player density can; server choice doesn't directly.

Nobody has published FPS numbers for this mod, so I won't invent any.

## What are the known issues and workarounds?

These come straight from the mod's README and its GitHub issues, except where I mark them as community-reported.

- **Loading screens and the race intro cutscene flicker** — the mod ships an epilepsy warning about this. Look away or close your eyes during loads. No fix offered.
- **Head-tracked lean is wrong on elevators, ships, and zeppelins.** Recenter (right-stick click) after the platform moves, or avoid leaning on transports.
- **Some UI elements draw with a black background.** Use the made-for-VR UI, or live with it. No documented fix.
- **The made-for-VR UI looks very low-res on 1080p monitors.** Run a higher desktop resolution, or use the default floating UI.
- **Auto Face Target turns you on every action, including Blink.** Disable the option for classes where it hurts.
- **Map chunks that would be visible in VR get culled.** Raise view distance or near/far clip; it may persist.
- **No camera turn on the right stick during flight paths.** Wait it out — head look still works.
- **`gameMultiplier` ignored (always 2×).** No merged fix; a fork, patch, or Discord build is the only path.
- **SteamOS needs a "proton hotfix" (GitHub issue #3, opened October 2026).** Run on Windows, or follow that thread. What the hotfix actually is — patched DLL, Proton version, launch flag — isn't stated.
- **Camera fights mouse-look; alt-tab loses focus** (community-reported, not in the README). Play with the mouse idle and alt-tab back deliberately.
- **Only keys 0–3, 8, 9 reachable on the controller.** Keyboard and mouse for the rest, or action-set switching.
- **Mounts invisible in first person.** Third person for travel — first-person mount visibility was never shipped.

## What does VR not fix in WoW?

VR changes how Azeroth looks and how you point. It doesn't change the game underneath.

- **Auction house, mail, chat, profession, and vendor windows** are still 2D frames you operate with a ray pointer. Workable, slow, and worse than a mouse for bulk actions.
- **Hotbar density.** The mod maps six spare keys. A 30+ ability rotation does not fit on the controller. Keyboard and mouse stay primary for real play.
- **Raid addon dependence.** DBM- and BigWigs-style timers render in the floating UI, but reacting to them with controller-only input is the constraint, not the display.
- **Tab-target combat stays tab-target.** Motion aiming changes how you pick targets, not the combat model.
- **Social and economic play** — trade chat, AH flipping, guild management — has no VR affordance.
- **Modern content.** The entire post-2010 game is out of reach. No setting changes that; the client version does.

## Can you play WoW Forever in VR?

**There is no working VR mod for WoW Forever.** WoVR targets a compatible World of Warcraft **3.3.5a** client, and it is not a generic VR mod for other WoW versions or custom server clients. If you came here looking for a true WoW Forever VR mod with 6DOF headset tracking and motion controls, that path doesn’t currently exist.

The closest you can get right now is **cinema mode**: play WoW Forever on your PC and view it on a big virtual screen inside your headset through Virtual Desktop, Bigscreen, or SteamVR desktop view. That gives you immersion, but it is not native VR gameplay.

If you want a first-person camera feel on the flat/cinema-mode side, there are addon options to watch:

- **[Terren's Forever First Person](https://www.curseforge.com/wow/addons/terrens-forever-first-person)** — a CurseForge addon for first-person camera behavior. It can make cinema-mode play feel closer to being in the world, but it is still not a VR mod.
- **Arkhaines Retro Forever mod** — not out yet at the time of this update. Treat it as something to watch, not a working WoW Forever VR solution.

If your goal is actual WoW in VR today, the working path is still the one in this guide: a compatible 3.3.5a client + WoVR (or the WoVR Quest Community Patch) + SteamVR.

## Is playing WoW in VR against the terms of service?

I'll state the clause and stop there. I'm not a lawyer, and nothing I found settles the question.

Blizzard's End User License Agreement, in its prohibited-conduct section, lists both "modify" and "create derivative works based on or related to the Platform." Separately, it prohibits unauthorized code that allows "automated control of a Game" — cheats, bots, hacks. WoVR modifies the game client. It does not automate play; it remaps input. Whether "modify" as written covers this mod is the plain-text question, and the answer isn't one my research can give you.

WoVR runs only against 3.3.5a private servers, so Blizzard's live anti-cheat (Warden) is not in the execution path. And running a private server is itself a separate, long-litigated issue from the mod. I won't tell you Blizzard "doesn't care" — nothing I retrieved supports that claim, and the EULA language is what it is.

## What isn't documented publicly

A few things live behind the Discord gate or aren't documented anywhere public.

- The full `config.txt` key list — Discord-only, not in the repo.
- The base mod's current precompiled build number. The newest source-side label is v6 (May 2024); the Quest Community Patch documents its own changes but not which base build it was cut from.
- The deployed DLL filename, folder layout, and launcher behavior.
- The semantics of `hmdBufferSize`.
- Whether the `gameMultiplier` bug is fixed in any Discord build.
- Whether Blizzard has ever commented on WoVR specifically.

If you're setting this up, the Flat2VR Discord is where those answers live. Confirm the undocumented parts before you blame the mod.
