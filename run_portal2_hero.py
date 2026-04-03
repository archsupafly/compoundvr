#!/usr/bin/env python3
"""
Run Portal 2 hero image generation
"""
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

def load_api_key():
    """Get GEMINI_API_KEY from environment or .env file."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    
    env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
    if not env_path.exists():
        print(f"ERROR: {env_path} does not exist")
        return None
    
    content = env_path.read_text()
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("GEMINI_API_KEY="):
            key = line.split("=", 1)[1].strip()
            if key.startswith('"') and key.endswith('"'):
                key = key[1:-1]
            if key.startswith("'") and key.endswith("'"):
                key = key[1:-1]
            return key
    
    return None

print("=" * 60)
print("Portal 2 VR Hero Image Generator")
print("=" * 60)

api_key = load_api_key()
if not api_key:
    print("ERROR: No GEMINI_API_KEY found")
    sys.exit(1)

print(f"API key found: {api_key[:4]}...{api_key[-3:]}")

output_path = Path("/home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

prompt = """Photorealistic cinematic 16:9 wide photograph of a pristine Aperture Science test chamber interior. Sterile white walls with subtle panel lines and clean geometric architecture. A large glowing orange portal on one pristine white wall, its surface shimmering with energy, and a matching blue portal visible on a distant platform. The portals create impossible geometry - looking through one reveals a completely different part of the facility. Industrial science facility aesthetic with recessed lighting, clean surfaces, and hints of advanced technology.

Deep atmospheric perspective showing multiple levels of the test chamber, with catwalks, platforms, and glass panels creating architectural depth. Subtle cyan accent lighting reflecting off white surfaces. Clean editorial photography style, magazine cover quality. The sense of spatial puzzle and discovery - a moment of wonder.

Technical details: Cool white and soft gray color palette with vibrant orange and blue portal glows providing contrasting focal points. Soft shadows, even lighting. Minimalist industrial design with hints of corporate science facility. High detail, photorealistic. No visible humans, no characters, no silhouettes, no robots, no turrets, no companions. Pure environmental scene. No text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Editorial documentary atmosphere, calm and mysterious. The quiet moment before a test begins."""

print(f"\nPrompt length: {len(prompt)} chars")
print("Generating image...")

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9",
        "guidanceScale": 16.0
    }
}

req_data = json.dumps(payload).encode()
req = urllib.request.Request(url, data=req_data, headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req, timeout=180) as response:
        result = json.loads(response.read().decode())
except urllib.error.HTTPError as e:
    error_body = e.read().decode()
    print(f"\nHTTP ERROR {e.code}:")
    print(error_body[:1000])
    sys.exit(1)

predictions = result.get("predictions", [])
if not predictions:
    print(f"ERROR: No predictions")
    print(json.dumps(result, indent=2)[:1000])
    sys.exit(1)

pred = predictions[0]
if "bytesBase64Encoded" not in pred:
    print(f"ERROR: No image data")
    print(f"Keys: {list(pred.keys())}")
    sys.exit(1)

image_data = base64.b64decode(pred["bytesBase64Encoded"])
with open(output_path, "wb") as f:
    f.write(image_data)

file_size = output_path.stat().st_size
print(f"\n{'='*60}")
print("SUCCESS")
print(f"{'='*60}")
print(f"Output: {output_path}")
print(f"Size: {file_size / 1024:.1f} KB ({file_size:,} bytes)")