# Software/Tool Article Queue

Master list of VR software, tools, and emulator candidates for CompoundVR coverage. These are not individual games but software that enables VR experiences.

**Published Software Articles:** vorpx-injection-driver-guide

---

## Emulators with VR Support

### Nintendo Consoles

| Software | Platform | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **Citra VR** | Nintendo 3DS | Native VR fork | High | Citra fork with stereoscopic 3D support, plays 3DS games in VR. Active development. |
| **Dolphin VR** | GameCube / Wii | Native VR fork | High | Dolphin fork with VR support. Plays GameCube and Wii games in VR. Head tracking, motion controls for Wii. |
| **PPSSPP VR** | PlayStation Portable | Native VR fork | High | PPSSPP fork with VR support. Plays PSP games in VR. Active development. |
| **3dSen VR** | Nintendo NES | Native VR emulator | High | Unique NES emulator that transforms 2D games into 3D voxel dioramas in real-time. $24.99 on Steam. 10+ years development, v1.0 released June 2025. Not just VR wrapper — actual 2D-to-3D transformation. |
| **3DSenVR** | Nintendo 3DS | VR support | High | 3DS emulator with VR capabilities. Stereoscopic 3D games in VR. |

### Sony Consoles

| Software | Platform | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **PCSX2 VR** | PlayStation 2 | VR fork/mod | Research | PCSX2 has VR work in progress. Need to verify current status. |
| **RPCS3** | PlayStation 3 | Research needed | Research | PS3 emulator. VR support status unclear. |
| **PCSX-Redux VR** | PlayStation 1 | VR fork | Research | PS1 emulator with VR possibilities. |

### Microsoft Consoles

| Software | Platform | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **Xenia VR** | Xbox 360 | Research needed | Research | Xbox 360 emulator. VR support status unclear. |
| **xemu VR** | Xbox | Research needed | Research | Original Xbox emulator. VR support status unclear. |

### Handhelds / Other

| Software | Platform | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **melonDS VR** | Nintendo DS | VR fork | Research | DS emulator. VR possibilities for dual-screen in VR. |
| **BigPEmu VR** | Atari Jaguar | VR support | Research | Jaguar emulator. Has VR support. Niche but notable. |
| **DuckStation VR** | PlayStation 1 | VR fork | Research | PS1 emulator with VR possibilities. |

### Sega Consoles

| Software | Platform | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **Sega Genesis Classics** | Genesis/Mega Drive | Official VR Hub | ✅ DONE | Official Sega collection with VR bedroom hub. 50+ Genesis games playable in virtual 90s bedroom. Steam VR support added 2018. Delisted December 2024. |

### Multi-System

| Software | Platforms | VR Support | Priority | Notes |
|----------|----------|-----------|----------|-------|
| **RetroArch VR** | Multiple cores | VR core support | Research | Frontend with multiple emulator cores. Some cores have VR support. |
| **EmuVR** | Multiple systems | Native VR frontend | High | VR emulator frontend. Virtual room with retro consoles/TVs. Multi-emulator environment. Play retro games on virtual CRT TVs in a 3D space. |

---

## VR Injection Drivers / Frameworks

| Software | Type | Priority | Notes |
|----------|------|----------|-------|
| **VorpX** | Injection Driver | ✅ DONE | Commercial injection driver. Already published. |
| **Vireio Perception** | Injection Driver Framework | High | Free, open source. Predates VorpX. DK1 era. Historical significance. |
| **UEVR** | Unreal Engine VR Injector | High | Praydog's UEVR. Enables VR for Unreal Engine 4/5 games. Major community tool. |
| **UUVR** | Unity VR Injector | High | Raicuparta's Universal VR mod for Unity games. Newer alternative to VRGIN. Active development since July 2024. Integrated with Rai Pal. |
| **REFramework** | RE Engine VR | High | Praydog's REFramework with VR support. Enables VR for RE Engine games (RE2, RE3, RE7, RE8, DMC5, etc.). |
| **Luke Ross R.E.A.L. VR** | Injection Driver | High | Patreon-supported injection driver. GTA V, RDR2, Cyberpunk, Witcher 3, Elden Ring. |
| **VRGIN** | Unity VR Injection Framework | High | Open-source VR injection framework for Unity games. Works best with Unity 5.x (5.0-5.6). Created by Eusth. Enables VR for flat Unity games. Requires DLL injection via IPA or similar. |

---

## VR Middleware / Tools

| Software | Type | Priority | Notes |
|----------|------|----------|-------|
| **OpenVR Space Calibrator** | Multi-Headset Tool | Research | Tool for calibrating multiple VR headsets in same space. |
| **OpenComposite** | Compatibility Layer | Research | Converts OpenVR calls to OpenXR. Performance improvement for some games. |
| **OVR Advanced Settings** | VR Utility | Research | SteamVR overlay with advanced settings. |
| **vrperfkit** | Performance Tool | Research | Open-source VR performance toolkit. Foveated rendering, upscaling. |

---

## VR Launchers / Frontends

| Software | Type | Priority | Notes |
|----------|------|----------|-------|
| **Vortex** | Game Launcher | Research | VR game launcher. |
| **Oculus Tray Tool** | Utility | Research | Meta/Quest PCVR optimization tool. |

---

## High Priority Queue (Next 15)

Software articles sorted by priority for coverage:

1. **UEVR** — Major community tool enabling VR for Unreal Engine games. Praydog's work. High impact.
2. **UUVR** — Raicuparta's Universal VR mod for Unity games. Newer alternative to VRGIN. Active development since July 2024. Integrated with Rai Pal.
3. **REFramework VR** — Praydog's RE Engine VR support. RE2/RE3/RE7/RE8/DMC5. Major for horror gaming.
4. **Citra VR** — 3DS in VR. Stereoscopic 3D games become genuinely 3D. Active development.
5. **Dolphin VR** — GameCube/Wii in VR. Wii motion controls translate well. Long history.
6. **PPSSPP VR** — PSP in VR. Active development, portable games on big screen.
7. **Luke Ross R.E.A.L. VR** — GTA V, RDR2, Cyberpunk, Witcher 3, Elden Ring. High-profile games.
8. **Vireio Perception** — Historical significance. First VR injection driver. Free/open source.
9. **EmuVR** — VR emulator frontend. Virtual room with retro consoles/TVs. Multi-emulator environment.
10. **3dSen VR** — Unique NES emulator. Transforms 2D games into 3D voxel dioramas. $24.99 on Steam. v1.0 June 2025.
11. **VRGIN** — Unity VR injection framework. Works with Unity 5.x games. Firewatch, Dear Esther, Ghost of a Tale, Layers of Fear, DARQ confirmed working.
12. **PCSX2 VR** — PS2 in VR. Need to verify current status.
13. **OpenComposite** — Performance tool, converts OpenVR to OpenXR.
14. **3DSenVR** — 3DS emulator with VR support. Stereoscopic 3D games in VR.
15. **melonDS VR** — DS in VR, dual-screen setup possibilities.
16. **DuckStation VR** — PS1 in VR.
17. **Sega Genesis Classics** — Official Sega collection with VR bedroom hub. 50+ Genesis games. Delisted December 2024.
18. **RetroArch VR** — Multi-system frontend, identify VR-capable cores.

---

## Notes

### Research Needed
- **3DSense** — Need to identify. Is this a Citra fork? Different emulator?
- **PCSX2 VR** — What's the current state of PS2 VR emulation?
- **RPCS3 VR** — Any VR support for PS3 emulation?
- **Xenia VR** — Xbox 360 VR status?
- **RetroArch VR** — Which cores have VR support?

### Article Format Differences
Software articles differ from game articles:
- **No tier rating** — Software isn't "playable" like games
- **Focus on:** Setup difficulty, compatibility, performance, active development
- **Recommendation based on:** Utility, stability, community support, documentation
- **Route type:** Emulator, Injection Driver, Framework, Tool

---

**Last Updated:** 2026-03-23