# Contra VR Hero Image Generation Script

## Image Ready for Generation

Follow these steps to generate the hero image:

### Step 1: Run the generation script

```bash
cd /home/antforce/.hermes/profiles/maya && \
source .env 2>/dev/null || true && \
python3 /tmp/contra_hero_gen.py
```

Alternative (using main skills directory):
```bash
python3 /home/antforce/.hermes/skills/creative/gemini-image-simple/scripts/generate.py \
"Cinematic wide shot of a voxel diorama jungle warfare scene viewed from first-person perspective. Blocky voxel soldier protagonist at foreground edge firing iconic spread gun with five-shot fan pattern spreading through dimensional space toward enemy targets. Deep layered jungle stage with platform structures extending into distance, rolling barrel tumbling through mid-ground. Deep navy #0b1020 atmospheric background with cyan #0ee7ff muzzle flash lighting accents. Editorial magazine cover quality, desaturated cinematic color grading, moody atmospheric fog. Angular geometric voxel 3dSen transformation aesthetic, standing at platform edge looking across the jungle canyon. Intense run-and-gun action composition, distant explosions silhouetted. High detail, professional concept art style, documentary photography aesthetic. NO text overlays, NO titles, NO subtitles, NO UI elements, NO watermarks, NO logos, NO person wearing headset, NO floating tech elements, NO promotional graphics, NO VR gimmicks, NO game HUD, NO on-screen text" \
/home/antforce/compoundvr-project/public/images/games/contra-vr-hero.jpg
```

### Output Location
- File: `/home/antforce/compoundvr-project/public/images/games/contra-vr-hero.jpg`
- Dimensions: 1920x1080 (16:9)
- Format: JPEG

---

## Prompt Construction Rationale

### Game Context (from article)
- **Title**: Contra VR (Contra NES in 3dSen VR)
- **Genre**: Run-and-gun action
- **Key visual elements**: 
  - Jungle stage with rolling barrels and platform depth
  - Spread gun's iconic five-shot fan pattern
  - Voxel diorama transformation (3dSen)
  - Intense, challenging gameplay

### Brand Direction Applied
- **Background**: Deep navy #0b1020
- **Accent**: Cyan #0ee7ff (muzzle flashes, lighting)
- **Style**: Editorial documentary, not promotional/gaming aesthetic
- **Composition**: First-person perspective from platform edge looking across jungle

### AI Pitfalls Avoided
- NO text overlays/promotional graphics
- NO VR headset photos
- NO floating tech elements
- NO UI/game HUD
- NO marketing imagery

### Style Influences
- Wired (cinematic documentary)
- Engadget (clean, authoritative)
- Nexus Mods (authentic gameplay)
- 16-bit retro aesthetic through voxel transformation lens

---

## Quality Verification Checklist

After generation, verify:
- [ ] No visible text anywhere
- [ ] Deep navy background (not pure black)
- [ ] Cyan accent lighting present
- [ ] Voxel/3dSen diorama aesthetic
- [ ] Jungle environment with depth
- [ ] Spread gun pattern visible (five-shot fan)
- [ ] Editorial cinematic mood
- [ ] Works at 16:9 mobile crop
- [ ] No promotional/marketing feel