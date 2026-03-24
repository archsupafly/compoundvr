#!/usr/bin/env python3
"""
Generate a hero image for Batman: Arkham VR using Gemini Imagen API.
"""

import os
import json
import base64
from pathlib import Path

# Ensure output directory exists
output_dir = Path("/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "batman-arkham-vr-hero.jpg"

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

# The prompt for Batman: Arkham VR hero image
prompt = """A cinematic hero image for Batman: Arkham VR. Features Batman in his iconic armored suit and cowl from the Arkham series, standing in a dramatic pose with his cape flowing. He is positioned in a dark gothic environment that transitions into a deep VR void space. The background is a dark navy void (#0b1020) with subtle cyan neon grid lines (#0ee7ff) suggesting VR boundaries and detective vision mode. Batman is partially illuminated by soft cyan accent lighting from below and subtle purple ambient light (#8b5cf6) reflecting off his armor. The aesthetic is sophisticated, dark, and technical - like a premium gaming editorial header. Clean composition with generous negative space on the left for text overlay. Photorealistic 3D render style with cinematic lighting, high contrast, moody atmosphere. Gothic architecture elements like gargoyles or cathedral spires fade into the VR grid. Professional game journalism header image quality. Dark, brooding, immersive VR atmosphere."""

# Gemini Imagen 4.0 API endpoint
model_name = "imagen-4.0-generate-001"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:predict?key={api_key}"

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

print(f"Generating Batman: Arkham VR hero image with Gemini {model_name}...")
print(f"Prompt: {prompt}")

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
