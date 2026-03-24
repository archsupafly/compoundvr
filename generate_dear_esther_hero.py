#!/usr/bin/env python3
"""
Generate a hero image for Dear Esther VR using Gemini Imagen API.
"""

import os
import json
import base64
from pathlib import Path

# Ensure output directory exists
output_dir = Path("/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "dear-esther-vr-hero.jpg"

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

# The prompt for Dear Esther VR hero image
# Based on CompoundVR brand guide:
# - Dark navy (#0b1020), cyan (#6ee7ff) accents
# - Sophisticated, restrained, atmospheric
# - Dear Esther is a haunting narrative walking sim on a Hebridean island

prompt = """A cinematic hero image for a VR game mod website. Scene: A misty, atmospheric Hebridean island coastline at dusk or dawn, with moody fog rolling over rocky cliffs and a solitary abandoned bothy (small stone cottage) in the distance. The color palette should be dominated by deep dark navy blues (#0b1020) and midnight blues, with subtle cyan (#6ee7ff) accent lighting suggesting VR immersion - perhaps faint glow from a lighthouse or bioluminescent elements on the shore. The mood is haunting, lonely, and contemplative - evoking the walking simulator "Dear Esther". 

Style: Sophisticated, restrained, editorial quality. Not game screenshot but artistic interpretation. Dramatic composition with strong depth, atmospheric fog, subtle lens flare. Clean, technical, trustworthy aesthetic. No text, no logos. Wide 16:9 cinematic aspect ratio. High quality, detailed, professional game marketing artwork style."""

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

print("Generating Dear Esther VR hero image with Gemini Imagen...")
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
