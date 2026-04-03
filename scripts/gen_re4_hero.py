#!/usr/bin/env python3
"""
Generate Resident Evil 4 VR Hero Image using Gemini Imagen API
Brand: CompoundVR (deep navy #0b1020, cinematic editorial style)
Style: Rural Spanish horror atmosphere, fog, gothic environmental
"""

import os
import sys
import json
import base64
import subprocess
from pathlib import Path

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "pillow", "--user", "-q"])

import requests
from PIL import Image
from io import BytesIO

# Load API key from maya profile .env
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.split("=", 1)[1].strip()
                if api_key.startswith('"') and api_key.endswith('"'):
                    api_key = api_key[1:-1]
                break

if not api_key:
    print("Error: GEMINI_API_KEY not found")
    sys.exit(1)

print(f"Found GEMINI_API_KEY: {api_key[:5]}...{api_key[-4:]}")

# Output path
output_path = Path("/home/antforce/compoundvr-project/public/images/games/resident-evil-4-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Prompt for RE4 VR hero - Spanish rural horror atmosphere
# Following CompoundVR style: NO text, NO game name, NO VR label, NO people
# Environment/atmosphere ONLY - fog, rural village, gothic horror
prompt = """A cinematic 16:9 hero image for a survival horror game feature article. Atmospheric Spanish rural village environment at dusk, dense fog rolling through narrow cobblestone streets between old stone buildings with weathered wooden doors and lanterns. Creeping ivy and moss on ancient architecture. Foreboding gothic horror atmosphere with deep shadows and muted earth tones. Deep navy background (#0b1020) fading into foggy gray distances. Warm amber lantern glow cutting through mist. Desaturated cinematic magazine cover quality, editorial documentary photography style. Moody, oppressive, tense atmosphere. Environmental storytelling through architecture and lighting. No characters, no people, no text, no logos, no watermarks, no UI elements, no headset imagery, no promotional graphics. Pure environmental mood piece capturing rural European horror atmosphere. Film-like color grading with lifted blacks."""

# Gemini Imagen 4.0 API
url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9",
        "guidanceScale": 15.0
    }
}

headers = {"Content-Type": "application/json"}

print(f"Generating Resident Evil 4 VR hero image...")
print(f"Style: Spanish rural horror atmosphere, fog, environmental only")
print(f"Prompt: {prompt[:120]}...")

try:
    response = requests.post(url, json=payload, headers=headers, timeout=120)
    response.raise_for_status()
    
    data = response.json()
    predictions = data.get("predictions", [])
    
    if not predictions:
        print(f"Error: No predictions in response")
        print(json.dumps(data, indent=2))
        sys.exit(1)
    
    prediction = predictions[0]
    
    if "bytesBase64Encoded" in prediction:
        image_data = base64.b64decode(prediction["bytesBase64Encoded"])
        image = Image.open(BytesIO(image_data))
        
        # Convert to RGB if needed, using deep navy as background
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (11, 16, 32))
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        image.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
        print(f"\nSUCCESS: Hero image saved to: {output_path}")
        print(f"Image size: {image.size}")
        print(f"File size: {output_path.stat().st_size / 1024:.1f} KB")
    else:
        print(f"Error: No base64 image data")
        print(f"Keys: {list(prediction.keys())}")
        sys.exit(1)
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)