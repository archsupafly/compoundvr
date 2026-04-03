#!/usr/bin/env python3
"""
Metroid VR Hero Image - Planet Zebes Environment
"""
import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# Try multiple ways to get the API key
api_key = None

# Method 1: Environment variable (already set)
api_key = os.environ.get("GEMINI_API_KEY")

# Method 2: Load from Maya's .env
if not api_key:
    env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
                    break

if not api_key:
    print("FAILED: GEMINI_API_KEY not found")
    exit(1)

print(f"API Key found: {api_key[:10]}...{api_key[-4:]}")

# Environment-only prompt for Planet Zebes (NO game name, NO VR, NO characters, NO people)
PROMPT = """Ancient alien underground cavern system with rocky geological formations, vertical shafts descending into darkness, crystalline structures embedded in cave walls, atmospheric glow from bioluminescent elements and distant magma, ancient ruined architecture seamlessly integrated into natural rock formations, mysterious doorways carved from stone, deep navy shadows with muted amber and cyan accent lighting emanating from energy sources, cinematic editorial photography, moody atmospheric style, sophisticated documentary composition, high detail, professional concept art quality, deep sense of isolation and descent through underground tunnels, NO text overlays, NO titles, NO subtitles, NO UI elements, NO watermarks, NO logos, NO person, NO characters, NO figures, NO headset, NO controllers, NO floating tech elements, NO promotional graphics, NO text of any kind"""

OUTPUT_PATH = "/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.png"

print(f"\nPrompt ({len(PROMPT)} chars):")
print(PROMPT[:200] + "...")
print(f"\nOutput: {OUTPUT_PATH}")
print("Aspect: 16:9")

# Gemini Imagen API call
url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {"sampleCount": 1, "aspectRatio": "16:9"}
}

headers = {"Content-Type": "application/json"}
data = json.dumps(payload).encode()
req = urllib.request.Request(url, data=data, headers=headers)

print("\nCalling Gemini Imagen API...")

try:
    with urllib.request.urlopen(req, timeout=180) as resp:
        result = json.loads(resp.read().decode())
    
    predictions = result.get("predictions", [])
    if predictions and "bytesBase64Encoded" in predictions[0]:
        img_data = base64.b64decode(predictions[0]["bytesBase64Encoded"])
        
        Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
        
        with open(OUTPUT_PATH, "wb") as f:
            f.write(img_data)
        
        size = Path(OUTPUT_PATH).stat().st_size
        print(f"\nSUCCESS: {OUTPUT_PATH}")
        print(f"Size: {size:,} bytes ({size/1024:.1f} KB)")
    else:
        print(f"FAILED: No image in response")
        print(json.dumps(result, indent=2)[:500])
        exit(1)
        
except urllib.error.HTTPError as e:
    print(f"FAILED: HTTP {e.code}")
    print(e.read().decode()[:500])
    exit(1)
except Exception as e:
    print(f"FAILED: {e}")
    exit(1)