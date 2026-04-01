#!/usr/bin/env python3
"""
Generate DiRT Rally VR Hero Image using Gemini Imagen API
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Style: Gritty rally motorsport, realistic simulation, cinematic
"""

import os
import sys
import json
import base64
from pathlib import Path

# Install dependencies
subprocess = __import__('subprocess')
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "pillow", "--user", "-q"])

import requests
from PIL import Image
from io import BytesIO

# Try to load API key from maya profile .env if not in environment
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    # Load from maya profile
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
output_path = Path("/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Prompt for DiRT Rally VR hero - gritty, realistic rally motorsport
prompt = """A cinematic 16:9 hero image for DiRT Rally VR. A rally race car in intense action on a muddy forest rally stage. Dramatic dust and mud spray kicked up behind the sliding car. Gravel trail with tall pine trees, atmospheric forest environment. Moody overcast lighting. Deep navy background (#0b1020) with cyan accent lighting (#6ee7ff) on car headlights cutting through dust. Purple undertones (#8b5cf6) in shadows. View suggests VR cockpit perspective. Gritty, realistic, serious motorsport simulation aesthetic. Editorial magazine cover quality with cinematic composition. No text, no logos, no watermarks. Professional automotive photography style."""

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

print(f"Generating DiRT Rally VR hero image...")
print(f"Prompt: {prompt[:100]}...")

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
        
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (11, 16, 32))
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        image.save(output_path, "JPEG", quality=95)
        print(f"Hero image saved to: {output_path}")
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