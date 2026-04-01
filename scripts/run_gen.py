#!/usr/bin/env python3
"""DiRT Rally VR Hero Generator - Using Gemini Imagen"""
import os
import sys
import json
import base64
import subprocess
from pathlib import Path

# Get API key
api_key = None
env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if line.startswith("GEMINI_API_KEY="):
            api_key = line.split("=", 1)[1].strip().strip('"')
            break

if not api_key:
    print("ERROR: GEMINI_API_KEY not found")
    sys.exit(1)

print(f"API Key found: {api_key[:8]}...{api_key[-4:]}")

# Install deps
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "pillow", "--user", "-q"])

import requests
from PIL import Image
from io import BytesIO

# Output
output_path = Path("/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Prompt
prompt = """Cinematic hero image for DiRT Rally VR video game. A rally race car speeds through a muddy forest stage, dramatic dust and mud spray surrounding it. Dark moody atmosphere with deep navy (#0b1020) background. Cyan headlights (#6ee7ff) cut through the dust with purple (#8b5cf6) accent shadows. Gritty realistic motorsport aesthetic, 16:9 wide cinematic composition. VR cockpit perspective implied. Editorial magazine cover quality, no text or logos."""

# API call
url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"
payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {"sampleCount": 1, "aspectRatio": "16:9", "guidanceScale": 15.0}
}

print("Generating image with Gemini Imagen...")
try:
    resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    
    preds = data.get("predictions", [])
    if not preds:
        print(f"ERROR: No predictions")
        print(json.dumps(data, indent=2))
        sys.exit(1)
    
    pred = preds[0]
    if "bytesBase64Encoded" not in pred:
        print(f"ERROR: No image data. Keys: {list(pred.keys())}")
        sys.exit(1)
    
    img_data = base64.b64decode(pred["bytesBase64Encoded"])
    img = Image.open(BytesIO(img_data))
    
    if img.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', img.size, (11, 16, 32))
        bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = bg
    
    img.save(output_path, "JPEG", quality=95)
    print(f"SUCCESS: Image saved to {output_path}")
    print(f"SIZE: {img.size}, {output_path.stat().st_size // 1024} KB")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)