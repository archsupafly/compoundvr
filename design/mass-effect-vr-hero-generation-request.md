# Mass Effect VR Hero Image - Generation Request

## Task Summary
Generate a hero image for the Mass Effect VR article following the compoundvr-hero-image skill guidelines.

## Status: PLACEHOLDER USED

### Issue
FAL_KEY is not configured (empty in ~/.hermes/.env line 92), so image generation via FAL.ai FLUX 2 Pro is not possible.

### Fallback Strategy Applied
Per the compoundvr-hero-image skill fallback strategy:
> "If hero generation fails and would block publication: copy an existing hero from a similar genre game as placeholder."

Used **Elite Dangerous hero** (space station/spaceship sci-fi theme) as temporary placeholder.

## Files Created/Modified

### Hero Image (Placeholder)
- **Path**: `/home/antforce/compoundvr-project/public/images/games/mass-effect-vr-hero.jpg`
- **Source**: Elite Dangerous hero (similar sci-fi space theme)
- **Size**: Same as source

### Documentation
- **Path**: `/home/antforce/compoundvr-project/public/images/games/mass-effect-vr-hero-prompt.txt`
- **Content**: Full prompt for future generation + status notes

## Original Prompt (for future generation)

```
Cinematic wide architectural photograph of the Citadel Presidium from Mass Effect,
the vast central hub ring of an alien space station. Towering curved architecture
stretching into atmospheric distance, deep navy #0b1020 atmospheric background with
ethereal cyan #6ee7ff holographic energy streams. Standing at ground level looking
up at immense alien structures, reflection pools in foreground, embassy towers in
layered depth. Editorial magazine cover quality, professional documentary style.
Desaturated cinematic color grading, moody atmospheric perspective, subtle film
grain. Architectural scale and grandeur, clean geometric lines, sophisticated
engineered aesthetic. Photorealistic render, high detail.

NO characters NO people NO Shepard NO text NO words NO letters NO titles NO UI
NO HUD NO watermark NO logo NO person NO headset NO tech elements NO graphics
NO promotional marketing. 16:9 landscape.
```

## Brand Guidelines Applied
- NO game name in image ✓
- NO "VR" text ✓
- NO people/characters ✓
- Environment/atmosphere only ✓
- Technical Authority aesthetic ✓
- Deep navy (#0b1020) + cyan (#6ee7ff) ✓

## To Generate Original Hero Image
1. Get FAL.ai API key from https://fal.ai/dashboard/keys
2. Add to `~/.hermes/.env`: `FAL_KEY=your-key-here`
3. Run the generation script at `/tmp/mass_effect_gen.py`

## Verification
The article at `/home/antforce/compoundvr-project/editorial/drafts/mass-effect-feature-draft.md`
references `heroImage: /images/games/mass-effect-vr-hero.jpg` which now exists as a placeholder.