# Resident Evil 4 VR Hero Image Generation Request

## Image Ready for Generation

Execute the following to generate the hero image:

```bash
python3 /home/antforce/compoundvr-project/scripts/generate_re4_hero_gemini.py
```

## Output Location
- File: `/home/antforce/compoundvr-project/public/images/games/resident-evil-4-vr-hero.jpg`
- Dimensions: 16:9 (Imagen default)
- Format: JPEG

---

## Prompt Construction Rationale

### Game Context (from article)
- **Title**: Resident Evil 4 (Original 2005/2007)
- **Genre**: Survival Horror / Third-Person Shooter / Action Horror
- **Route**: VorpX injection driver (PCVR)
- **Key themes**: Spanish rural village, Los Ganados, castle, fog, gothic horror atmosphere
- **Article verdict**: C tier - great game, poor VR fit due to third-person camera design

### Visual Elements from Game
- Spanish rural village setting (Los Ganados)
- Narrow cobblestone streets
- Ancient stone buildings with weathered doors
- Wrought iron lanterns
- Thick atmospheric fog
- Ivy and moss on architecture
- Gothic horror atmosphere
- Muted earth tones (brown, gray, faded green)

### Brand Direction Applied (from style guide)
- **Background**: Deep navy #0b1020
- **Style**: Editorial documentary, not promotional/gaming aesthetic
- **Composition**: Atmospheric environmental mood piece
- **Color**: Desaturated, cinematic, film-like
- **References**: Wired (documentary), Engadget (clean authority), Eurogamer (technical)

### CompoundVR Critical Constraints
- **NO** text overlays
- **NO** game name ("Resident Evil")
- **NO** "VR" text/labels
- **NO** people, characters, silhouettes
- **NO** headset imagery
- **NO** VR equipment
- **NO** watermarks or promotional graphics

### Final Prompt
```
Photorealistic cinematic 16:9 wide photograph of an abandoned rural Spanish village at twilight during foggy evening. Ancient stone buildings with weathered wooden doors and wrought iron lanterns lining narrow winding cobblestone streets. Thick atmospheric fog rolling through the village creating mysterious depth and limited visibility. Ivy and moss growing on old stone walls. Spanish rural gothic horror atmosphere with deep shadows and muted earth tones of brown gray and faded green. Deep navy blue evening sky transitioning to gray fog in the distance. Warm amber lantern light casting glow through the mist. Desaturated editorial documentary photography style, magazine cover quality. Moody foreboding oppressive atmosphere of rural European horror. Environmental storytelling through architecture and atmospheric lighting. No people, no human figures, no silhouettes, no characters, no text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Pure atmospheric environmental scene only. Film-like cinematic color grading with lifted blacks.
```

---

## Quality Verification Checklist

After generation, verify:
- [ ] No visible text anywhere (no "RE4", "VR", game title, etc.)
- [ ] Deep navy/muted color palette (not bright/saturated)
- [ ] Spanish village environment visible
- [ ] Atmospheric fog present
- [ ] Gothic horror mood
- [ ] No people/characters visible
- [ ] Editorial cinematic quality
- [ ] Works at 16:9 aspect ratio

---

## API Details
- **Provider**: Gemini Imagen 4.0
- **Endpoint**: `v1beta/models/imagen-4.0-generate-001:predict`
- **API Key Source**: `/home/antforce/.hermes/profiles/maya/.env`
- **Parameters**: 
  - aspectRatio: "16:9"
  - guidanceScale: 16.0
  - sampleCount: 1

---

## Files Created
- `/home/antforce/compoundvr-project/scripts/generate_re4_hero_gemini.py` - Generator script

## Article Reference
- `/home/antforce/compoundvr-project/editorial/drafts/resident-evil-4-vr-feature-draft.md`
- Hero image path in article frontmatter: `/images/games/resident-evil-4-vr-hero.jpg`