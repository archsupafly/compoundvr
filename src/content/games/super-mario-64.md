---
title: "Super Mario 64 VR"
description: "A native OpenXR rebuild that drops you inside the N64 platformer with your own two hands — jump, swim, and punch your way through the painting."
flatReleaseDate: 1996-06-23
vrReleaseDate: 2019-06-15
lastUpdated: 2026-10-12
featured: false
routeType: Full VR Mod
platforms: ['PCVR', 'Quest']
recommendation: Recommended with Caveats
playability: Fully Playable
setupBurden: Moderate Setup
inputStyle: Full Motion Controls
comfort: Moderate Intensity
performance: Efficient
supportStatus: Active
genres:
  - 3D Platformer
technicalTags:
  - Full VR Mod
  - OpenXR
  - 6DOF
  - Motion Controls
experienceTags:
  - Platforming
  - Collectathon
  - Fan Mod
tier: A
verdict: "A genuine 6DOF, motion-controlled rebuild of one of the greatest 3D platformers ever made — you physically leap through that painting instead of watching Mario do it. Setup friction and first-person platforming jank keep it shy of essential, but it's the only VR option that earns a recommendation."
heroImage: /images/games/super-mario-64-vr-hero.jpg
modDownload:
  url: "https://github.com/fulldivegames/sm64coopdx-VR-Physics-based"
  label: "Download Super Mario 64 VR Mod"
  note: "Created by Fulldivegames"
history:
  - date: 2026-10-12
    note: "Fulldivegames sm64coopdx-VR fork observed at v0.9.21 under active development; RaYRoD-TV build distributed via the Multiverse VR Hub. Both lead VR paths current."
sources: "Fulldivegames sm64coopdx-VR repository README; PCVR Mods Installer Hub README (RaYRoD-TV build); VRMods-List index entries; YouTube VR coverage from Beardo Benjo, Gamertag VR, Nathaniel Bandy, Nathie, VRified Games, and Kaze Emanuar; r/Dolphin_VR community thread (2019)."
---

The first time I got Mario to grab a ledge, I didn't press a button. I raised both fists to my chest and threw them overhead like I was hauling myself up a rock face, and the little guy did exactly that — scrambled onto the brick, my arms still locked overhead, legs kicking. I laughed like an idiot. That is the entire pitch for Super Mario 64 in VR: you stop watching a controller avatar jump and you start being the thing that jumps.

There is no official VR version of Super Mario 64. Nintendo has never touched this, and given their history, they are not about to. What you actually get is a community rebuild — a native OpenXR fork of the decompiled PC port (sm64coopdx, the same base that added online co-op to the PC game) with first-person motion controls and a rebuilt input layer. It's the actual game running natively with a VR-aware renderer and a rebuilt input layer — not a wrapper or a hack stapled onto an emulator.

Two groups ship it right now. Fulldivegames maintains the lead build, with a PCVR edition and a separate standalone edition for Quest. RaYRoD-TV ships a second implementation through the Multiverse VR Hub installer. Both are unofficial, unauthorized, and require you to supply your own Super Mario 64 ROM — nothing Nintendo is distributed, and you should be comfortable with that legal gray area before you start, because there is no support line and no store page to hide behind.

## How it actually plays

Super Mario 64 is one of the best 3D platformers ever made, and the VR fork doesn't sand down what made it great — it puts you inside it. The motion vocabulary is the part people ask about, so here it is straight. You jump by raising a fist — either hand, or both together if you want a bigger leap — and you hold that fist overhead to sustain height, which is how you hang in the air to line up a long jump or a dive. Swimming is the surprise standout: alternating strokes with each controller, or an overhead pull to kick upward, and suddenly the underwater sections stop being a flat-game chore and become something you're doing with your arms. Punching, grabbing, climbing, and the swing-and-release dives off vines all map to hand gestures. You punch by thrusting a fist; you grab by closing a hand near an object; you climb by reaching.

If all that arm-waving makes you nervous, there's a trigger-based jump option and a third-person gamepad mode buried in the settings, so you can play it more like the original with a head-tracked camera if the full-physics route fights you. I respect that as an option. I also barely used it, because the point of this build is that your body is the controller.

Comfort-wise, the lead forks ship real options rather than forcing one camera on you — diorama mode pulls the world into a floating scene you can scale, there's a stereo-depth toggle, and head-motion plus HUD-size controls let you dial the intensity down. Frame rate is locked and light on hardware; this is a 1996 game running a native PC port, so a modest rig handles it without breaking a sweat.

## What's genuinely good

The motion controls reframe a game you've already beaten a dozen times into something you get to physically do. Leaping out of the painting into Lethal Lava Land and watching the world swing around your head as you fall is not the same experience as nudging an analog stick. You're getting the real course layout, the real stars, the real secret hunts, rendered in stereoscopic 3D with 6DOF head tracking and a camera that understands depth — not a stripped VR reskin.

That depth is the whole justification. Bob-omb Battlefield has always been a diorama you orbit; in VR it's a place you stand in. The camera finally understands vertical space the way the original demanded you imagine it. For a game whose entire design thesis is "what if a 3D space you could poke at," handing you 6DOF is less a mod than a correction.

## Where it fights you

The catch is baked into the design. Super Mario 64's courses were built around a precise third-person camera and clean 2D-style ledge jumps, and first-person platforming with free movement will test anyone. There are moments — tight wall jumps, the sliding penguin course, anything that wants you to judge a gap by something other than your own two eyes — where the physicality stops feeling like play and starts feeling like compensating. The optional trigger-jump and third-person mode exist because the maintainers knew this; that's not a knock on the build, it's an honest admission that the source game wasn't drawn for a head inside Mario's skull.

Setup is the other tax. You are downloading a fork, pointing it at a ROM you legally obtained, and starting your OpenXR runtime in the right order. If you've wrangled PCVR mods before, this is a Tuesday. If you haven't, the lack of any official hand-holding means a wrong move gets you a black screen and a forum search, not a support chat. The RaYRoD-TV route is gentler here — the Hub installer does the fetching and checksumming — but you're still dropping a ROM into a folder either way.

And the thing nobody can promise: this is a fan build, not a product. It's active and current as of right now, but a project like this can shift under you tomorrow — forks merge, repos go quiet, a new upstream change breaks the physics. That's the deal with the best unofficial VR work, and it's worth saying out loud before you sink an afternoon into 120 stars.

## The verdict

Super Mario 64 in VR is the rare mod that doesn't just translate a game into a headset — it changes what the game is. You stop watching Mario jump and you start jumping, and a 1996 masterpiece that everyone has already finished becomes something you physically do for an evening. The first-person platforming jank and the ROM-and-fork setup are real, and they keep this out of the unquestionable-essential tier. But for anyone who has ever wanted to fall into that painting instead of sending Mario through it, this is the only path that earns a recommendation.

If you're already a VR tinkerer who cut their teeth on PC ports, this is a Tuesday-afternoon install and a weekend of grinning stupidity. If you need a store page and a support line, wait — but know you're missing the most surprising thing you can currently put a headset on for.
