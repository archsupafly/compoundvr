#!/usr/bin/env python3
"""
Generate a hero image for The Elder Scrolls: Daggerfall VR using Gemini Imagen API.
"""

import os
import json
import base64
from pathlib import Path

# Ensure output directory exists
output_dir = Path("/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "daggerfall-vr-hero.jpg"

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

# The prompt for Daggerfall VR hero image
# Based on CompoundVR brand guide v1:
# - Background: dark navy (#0b1020)
# - Accent: cyan (#6ee7ff)
# - Highlight: purple (#8b5cf6)
# - Atmospheric, gothic, dark fantasy aesthetic
# - Daggerfall: classic 1996 RPG, medieval fantasy, sprawling dungeons, castles

prompt = """A cinematic hero image for The Elder Scrolls: Daggerfall VR. Dark, atmospheric gothic fantasy scene showing the iconic sprawling medieval world of the 1996 classic RPG reimagined for virtual reality.

The composition features a dramatic view of ancient stone architecture - towering castle spires, massive dungeon archways, and weathered fortress walls shrouded in atmospheric fog and twilight gloom. Gothic medieval aesthetic with intricate stonework, moss-covered ruins, and mysterious pathways leading into shadowy depths.

Color palette: Deep dark navy (#0b1020) dominates the shadows, sky, and distant background. Ethereal cyan (#6ee7ff) magical glows emanate from ancient runes, spell effects, and mysterious light sources. Subtle purple (#8b5cf6) highlights accentuate magical auras and distant mystical phenomena. The lighting is moody and dramatic - think dark fantasy, not bright heroic fantasy.

Style: Atmospheric, immersive, slightly gritty retro-RPG aesthetic blended with modern cinematic quality. Dark, mysterious, epic in scale. Gothic medieval atmosphere with fog, dramatic shadows, and subtle magical elements. Wide 16:9 cinematic composition with the dark navy atmosphere consuming most of the frame, punctuated by the cyan and purple accent glows. No text, no logos, no watermarks, no characters, no UI elements. Pure environmental storytelling."""

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

print("Generating Daggerfall VR hero image with Gemini Imagen...")
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
            background = Image.new('RGB', image.size, (250, 250, 250))  # #fafafa
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
