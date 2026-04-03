#!/usr/bin/env python3
"""
Portal 2 VR Hero Image Generator for CompoundVR
Uses Gemini Imagen 4.0 API - Pure stdlib

Game: Portal 2 (2011)
Article: /home/antforce/compoundvr-project/editorial/drafts/portal-2-feature-draft.md
Output: /home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg

COMPOUNDVR HERO IMAGE STYLE GUIDE:
- NO text, game name, VR label
- NO people, characters, silhouettes  
- Environment/atmosphere ONLY
- Aperture Science test chambers, sterile white environments
- Orange/blue portal colors, industrial science facility aesthetic
- "Moment of wonder" - evocative atmosphere
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# Read API key from maya profile .env
env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
api_key = None
for line in env_path.read_text().splitlines():
    if line.startswith("GEMINI_API_KEY="):
        api_key = line.split("=", 1)[1].strip()
        if api_key.startswith('"') and api_key.endswith('"'):
            api_key = api_key[1:-1]
        break

if not api_key:
    print("ERROR: No GEMINI_API_KEY found")
    sys.exit(1)

print(f"API key: {api_key[:4]}...{api_key[-3:]}")

output_path = Path("/home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

prompt = """Photorealistic cinematic 16:9 wide photograph of a pristine Aperture Science test chamber interior. Sterile white walls with subtle panel lines and clean geometric architecture. A large glowing orange portal on one pristine white wall, its surface shimmering with energy, and a matching blue portal visible on a distant platform. The portals create impossible geometry - looking through one reveals a completely different part of the facility. Industrial science facility aesthetic with recessed lighting, clean surfaces, and hints of advanced technology.

Deep atmospheric perspective showing multiple levels of the test chamber, with catwalks, platforms, and glass panels creating architectural depth. Subtle cyan accent lighting reflecting off white surfaces. Clean editorial photography style, magazine cover quality. The sense of spatial puzzle and discovery - a moment of wonder.

Technical details: Cool white and soft gray color palette with vibrant orange and blue portal glows providing contrasting focal points. Soft shadows, even lighting. Minimalist industrial design with hints of corporate science facility. High detail, photorealistic. No visible humans, no characters, no silhouettes, no robots, no turrets, no companions. Pure environmental scene. No text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Editorial documentary atmosphere, calm and mysterious. The quiet moment before a test begins."""

print(f"\nGenerating Portal 2 VR hero image...")
print(f"Prompt: Aperture Science test chamber with portals")
print(f"Output: {output_path}")

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9",
        "guidanceScale": 16.0
    }
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req, timeout=180) as response:
        result = json.loads(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"\nHTTP ERROR {e.code}:")
    print(e.read().decode()[:1000])
    sys.exit(1)

predictions = result.get("predictions", [])
if not predictions:
    print("ERROR: No predictions")
    sys.exit(1)

pred = predictions[0]
if "bytesBase64Encoded" not in pred:
    print("ERROR: No image data")
    sys.exit(1)

image_data = base64.b64decode(pred["bytesBase64Encoded"])
with open(output_path, "wb") as f:
    f.write(image_data)

file_size = output_path.stat().st_size
print(f"\n{'='*60}")
print("SUCCESS!")
print(f"{'='*60}")
print(f"Output: {output_path}")
print(f"Size: {file_size/1024:.1f} KB")