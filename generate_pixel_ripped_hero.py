#!/usr/bin/env python3
"""
Generate a hero image for Pixel Ripped 1989 using Gemini Imagen API.
"""

import os
import json
import base64
from pathlib import Path

# Ensure output directory exists
output_dir = Path("/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "pixel-ripped-1989-hero.jpg"

# Check for API key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set")
    exit(1)

# Import required libraries
try:
    import requests
    from PIL import Image
    from io import BytesIO
except ImportError:
    print("Installing required packages...")
    os.system("pip3 install requests pillow --user")
    import requests
    from PIL import Image
    from io import BytesIO

# The prompt for Pixel Ripped 1989 hero image
# Based on CompoundVR brand guide:
# - Dark navy (#0b1020), cyan (#6ee7ff) and purple (#8b5cf6) accents
# - Sophisticated, restrained, editorial quality
# - Pixel Ripped 1989 is a VR game about retro gaming - a character playing classic games

prompt = """A cinematic hero image for a VR game mod website. Scene: A stylized composition representing retro 1980s gaming meeting modern VR. In the foreground, a VR headset floating or being worn, with vibrant pixel art game elements bursting outward from the visor - classic 8-bit space invaders, platformer characters, and arcade sprites in bright neon colors against the dark background. The color palette is dominated by deep dark navy blue (#0b1020), with striking cyan (#6ee7ff) accent lighting on the VR headset and glowing purple (#8b5cf6) highlights on the retro pixel elements. Subtle CRT scanline effects and vintage arcade cabinet geometry frame the composition.

The mood evokes nostalgia for 1980s gaming culture mixed with futuristic VR technology - think Tron meets retro arcade. Clean lines, sophisticated composition, editorial quality game artwork. No text, no logos. Wide 16:9 cinematic aspect ratio. High quality, detailed, professional game marketing artwork style."""

# Gemini Imagen 4.0 API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"

# API request payload
payload = {
    "instances": [
        {"prompt": prompt}
    ],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9",
        "guidanceScale": 15.0
    }
}

headers = {
    "Content-Type": "application/json"
}

print("Generating Pixel Ripped 1989 hero image with Gemini Imagen...")
print(f"Prompt: {prompt[:200]}...")

try:
    response = requests.post(url, json=payload, headers=headers, timeout=120)
    response.raise_for_status()
    
    data = response.json()
    
    # Imagen returns base64 encoded images
    predictions = data.get("predictions", [])
    if not predictions:
        print(f"Error: No predictions in response. Response: {json.dumps(data, indent=2)}")
        exit(1)
    
    # Get the first prediction
    prediction = predictions[0]
    
    # The image is base64 encoded
    if "bytesBase64Encoded" in prediction:
        image_data = base64.b64decode(prediction["bytesBase64Encoded"])
        
        # Open with PIL and save as JPEG
        image = Image.open(BytesIO(image_data))
        
        # Convert to RGB if necessary (in case it's RGBA)
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (11, 16, 32))  # #0b1020
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        # Save as JPEG with high quality
        image.save(output_path, "JPEG", quality=95)
        print(f"✓ Hero image saved to: {output_path}")
        print(f"  Image size: {image.size}")
    else:
        print(f"Error: No base64 image data in prediction. Keys: {list(prediction.keys())}")
        exit(1)
        
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
    if hasattr(e, 'response') and e.response:
        print(f"Response: {e.response.text}")
    exit(1)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
