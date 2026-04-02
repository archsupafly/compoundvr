# Mass Effect VR Hero Image Generation Script

## Brand Direction Reference
Based on `/home/antforce/compoundvr-project/design/hero-image-style-guide.md`:
- **NO game name** in image
- **NO "VR" text**
- **NO people/characters**
- **Environment/atmosphere only**
- **Technical Authority** aesthetic: engineered, sophisticated, editorial confidence
- **NOT generic game marketing art**

## Game Context
- **Title**: Mass Effect (2007)
- **Genre**: Sci-Fi RPG, Third-Person Shooter
- **Setting**: Space, Citadel space station, Normandy spaceship

## Visual Elements
- Citadel Presidium architecture
- Deep navy #0b1020 background
- Cyan #6ee7ff accent lighting
- Towering alien structures
- Reflection pools
- Atmospheric perspective
- Sophisticated editorial mood

---

## Generation Script

```python
#!/usr/bin/env python3
import os, sys, json, requests

env_file = "/home/antforce/.hermes/hermes-agent/.env"
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.strip().split("=", 1)
                v = v.strip().strip('"').strip("'")
                os.environ[k] = v

sys.path.insert(0, '/home/antforce/.hermes/hermes-agent')
from tools.image_generation_tool import image_generate_tool

OUT = "/home/antforce/compoundvr-project/public/images/games/mass-effect-vr-hero.jpg"

prompt = """Cinematic wide architectural photograph of the Citadel Presidium from Mass Effect, the vast central hub ring of an alien space station. Towering curved architecture stretching into atmospheric distance, deep navy #0b1020 atmospheric background with ethereal cyan #6ee7ff holographic energy streams. Standing at ground level looking up at immense alien structures, reflection pools in foreground, embassy towers in layered depth. Editorial magazine cover quality, professional documentary style. Desaturated cinematic color grading, moody atmospheric perspective, subtle film grain. Architectural scale and grandeur, clean geometric lines, sophisticated engineered aesthetic. Photorealistic render, high detail. NO characters NO people NO Shepard NO text NO words NO letters NO titles NO UI NO HUD NO watermark NO logo NO person NO headset NO tech elements NO graphics NO promotional marketing. 16:9 landscape."""

print("Generating Mass Effect VR Hero Image...")
r = json.loads(image_generate_tool(prompt=prompt, aspect_ratio="landscape"))

if r.get("success"):
    url = r["image"]
    print(f"URL: {url}")
    img = requests.get(url, timeout=90).content
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'wb') as f: f.write(img)
    print(f"✓ Done: {OUT}")
else:
    print(f"Failed: {r}")
    sys.exit(1)
```

## Run Instructions

```bash
cd /home/antforce/.hermes/hermes-agent && python3 -c "
import os, sys, json, requests
env_file = '.env'
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                v = v.strip().strip('\"').strip(\"'\")
                os.environ[k] = v
sys.path.insert(0, '.')
from tools.image_generation_tool import image_generate_tool
OUT = '/home/antforce/compoundvr-project/public/images/games/mass-effect-vr-hero.jpg'
prompt = '''Cinematic wide architectural photograph of the Citadel Presidium from Mass Effect, the vast central hub ring of an alien space station. Towering curved architecture stretching into atmospheric distance, deep navy #0b1020 atmospheric background with ethereal cyan #6ee7ff holographic energy streams. Standing at ground level looking up at immense alien structures, reflection pools in foreground, embassy towers in layered depth. Editorial magazine cover quality, professional documentary style. Desaturated cinematic color grading, moody atmospheric perspective, subtle film grain. Architectural scale and grandeur, clean geometric lines, sophisticated engineered aesthetic. Photorealistic render, high detail. NO characters NO people NO Shepard NO text NO words NO letters NO titles NO UI NO HUD NO watermark NO logo NO person NO headset NO tech elements NO graphics NO promotional marketing. 16:9 landscape.'''
print('Generating...')
r = json.loads(image_generate_tool(prompt=prompt, aspect_ratio='landscape'))
if r.get('success'):
    url = r['image']
    print(f'URL: {url}')
    img = requests.get(url, timeout=90).content
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'wb') as f: f.write(img)
    print(f'Saved: {OUT}')
else:
    print(f'Failed: {r}')
    sys.exit(1)
"
```

---

## Quality Checklist

After generation, verify:
- [ ] No visible text/words anywhere
- [ ] Deep navy background (#0b1020, not black)
- [ ] Cyan accent lighting (#6ee7ff)
- [ ] Citadel/Presidium environment aesthetic
- [ ] Sophisticated editorial mood
- [ ] No characters/people visible
- [ ] No promotional/marketing feel
- [ ] Works at 16:9 aspect ratio
- [ ] Center-weighted composition