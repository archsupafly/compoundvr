#!/usr/bin/env python3
import os, sys, json, base64, urllib.request, urllib.error
from pathlib import Path

# Get API key
env = Path("/home/antforce/.hermes/profiles/maya/.env").read_text()
for line in env.splitlines():
    if line.startswith("GEMINI_API_KEY="):
        k = line.split("=", 1)[1].strip().strip('"')
        break
else:
    print("No GEMINI_API_KEY")
    sys.exit(1)

print(f"API key: {k[:4]}...{k[-3:]}")

out = Path("/home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg")
out.parent.mkdir(parents=True, exist_ok=True)

prompt = """Photorealistic cinematic 16:9 wide photograph of a pristine Aperture Science test chamber interior. Sterile white walls with subtle panel lines and clean geometric architecture. A large glowing orange portal on one pristine white wall, its surface shimmering with energy, and a matching blue portal visible on a distant platform. The portals create impossible geometry - looking through one reveals a completely different part of the facility. Industrial science facility aesthetic with recessed lighting, clean surfaces, and hints of advanced technology.

Deep atmospheric perspective showing multiple levels of the test chamber, with catwalks, platforms, and glass panels creating architectural depth. Subtle cyan accent lighting reflecting off white surfaces. Clean editorial photography style, magazine cover quality. The sense of spatial puzzle and discovery - a moment of wonder.

Technical details: Cool white and soft gray color palette with vibrant orange and blue portal glows providing contrasting focal points. Soft shadows, even lighting. Minimalist industrial design with hints of corporate science facility. High detail, photorealistic. No visible humans, no characters, no silhouettes, no robots, no turrets, no companions. Pure environmental scene. No text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Editorial documentary atmosphere, calm and mysterious. The quiet moment before a test begins."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={k}"
payload = {"instances": [{"prompt": prompt}], "parameters": {"sampleCount": 1, "aspectRatio": "16:9", "guidanceScale": 16.0}}

print("Calling Gemini Imagen 4.0...")
req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req, timeout=180) as resp:
        result = json.loads(resp.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTP ERROR {e.code}: {e.read().decode()}")
    sys.exit(1)

preds = result.get("predictions", [])
if not preds:
    print(f"ERROR: No predictions - {result}")
    sys.exit(1)

img = base64.b64decode(preds[0]["bytesBase64Encoded"])
out.write_bytes(img)
print(f"\nSUCCESS!\nOutput: {out}\nSize: {out.stat().st_size/1024:.1f} KB")