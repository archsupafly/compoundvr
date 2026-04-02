#!/usr/bin/env python3
"""
Generate Eagle Flight VR Hero Image using Gemini Imagen API
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Style: Editorial magazine cover, sophisticated, atmospheric
Subject: Paris from eagle altitude - soaring view, no eagle visible
"""

import os
import sys
import json
import base64
from pathlib import Path

# Check dependencies first
try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests --user -q")
    import requests

try:
    from PIL import Image
except ImportError:
    print("Installing pillow...")
    os.system(f"{sys.executable} -m pip install pillow --user -q")
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
output_path = Path("/home/antforce/compoundvr-project/public/images/games/eagle-flight-vr-hero.jpg")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Prompt for Eagle Flight hero - Paris from eagle altitude, soaring view
# CRITICAL: NO game name, NO VR/platform references, NO people/headsets/controllers
# ONLY describe the game WORLD/ENVIRONMENT
# Viewer IS the eagle - no eagle visible, just the soaring view
prompt = """A breathtaking editorial magazine cover photograph of Paris from high altitude, as if soaring through the sky. The iconic Eiffel Tower stands tall in the distance against a vast open sky. The Seine River winds gracefully through the city, reflecting light. Endless Parisian rooftops stretch to the horizon in beautiful architectural detail. Golden hour warm daylight illuminating the scene with long dramatic shadows. Deep navy atmospheric background (#0b1020) with subtle cyan accent lighting (#6ee7ff) catching golden hour sun rays. Sophisticated, dark, atmospheric editorial quality. Cinematic 16:9 composition. Wide-angle bird's eye perspective. Sense of freedom and vast open sky. No text, no logos, no watermarks, no UI, no people. Pure environmental photography capturing the soaring experience over Paris."""

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

print(f"Generating Eagle Flight hero image...")
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
        
        # Convert to RGB if necessary
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (11, 16, 32))  # Deep navy
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        # Resize to standard hero size if needed
        if image.size != (1920, 1080):
            image = image.resize((1920, 1080), Image.Resampling.LANCZOS)
        
        image.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
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