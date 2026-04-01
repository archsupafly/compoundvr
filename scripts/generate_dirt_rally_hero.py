#!/usr/bin/env python3
"""
Generate a hero image for DiRT Rally VR using FAL.ai FLUX 2 Pro API.
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Subject: DiRT Rally (2015) by Codemasters - serious rally racing simulation
Style: Realistic, gritty motorsport, rally car action, dust/mud aesthetic
"""

import os
import json
import base64
from pathlib import Path
import sys

# Output path
output_path = Path("/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg")

# Ensure output directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Check for FAL.ai API key
fal_api_key = os.environ.get("FAL_KEY", "")
if not fal_api_key:
    print("Error: FAL_KEY environment variable not set")
    print("Get your API key from https://fal.ai/dashboard/keys")
    sys.exit(1)

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

# FLUX 2 Pro prompt for DiRT Rally VR hero image
# Based on CompoundVR brand guide v1:
# - Background: deep navy (#0b1020)
# - Accent: cyan (#6ee7ff)
# - Secondary: purple (#8b5cf6)
# - Gritty, realistic motorsport aesthetic

prompt = """Professional rally car speeding through a muddy forest rally stage, dynamic action shot. 
A Ford Fiesta RS WRC rally car kicking up a dramatic spray of gravel, mud, and dust as it powers through a corner. 
The cockpit and driver's perspective are visible through the windshield, suggesting VR immersion. 
Dense forest environment with tall pine trees lining a gravel rally stage, atmospheric lighting with moody overcast sky.

Color palette: Deep navy (#0b1020) dark background atmosphere, cyan (#6ee7ff) accent highlights on the car's headlights cutting through dust, 
subtle purple (#8b5cf6) undertones in the shadows. Gritty, realistic, cinematic quality.

Style: Editorial magazine cover quality, dark sophisticated motorsport atmosphere, realistic racing sim aesthetic, 
professional automotive photography. Wide 16:9 cinematic composition. High detail, photorealistic rendering.
No text, no logos, no watermarks, no game UI. Pure environmental storytelling focused on the rally experience."""

# FAL.ai FLUX 2 Pro API endpoint
url = "https://queue.fal.run/fal-ai/flux-pro/v1.1"

# API request payload for FLUX 2 Pro
payload = {
    "prompt": prompt,
    "image_size": "1920x1080",  # 16:9 aspect ratio
    "num_images": 1,
    "safety_tolerance": "2",  # Standard safety
}

headers = {
    "Authorization": f"Key {fal_api_key}",
    "Content-Type": "application/json"
}

print("Generating DiRT Rally VR hero image with FAL.ai FLUX 2 Pro...")
print(f"Prompt: {prompt[:150]}...")

try:
    # Submit request to FAL.ai
    response = requests.post(url, json=payload, headers=headers, timeout=180)
    response.raise_for_status()
    
    data = response.json()
    
    # FAL.ai returns URLs or base64 data
    # Handle different response formats
    image_url = None
    
    if "images" in data and len(data["images"]) > 0:
        image_url = data["images"][0].get("url") or data["images"][0].get("content")
    elif "image" in data:
        image_url = data["image"].get("url") or data["image"].get("content")
    elif "url" in data:
        image_url = data["url"]
    
    if image_url:
        if image_url.startswith("http"):
            # Download image from URL
            print(f"Downloading image from: {image_url[:60]}...")
            img_response = requests.get(image_url, timeout=60)
            img_response.raise_for_status()
            image_data = img_response.content
        else:
            # Assume base64
            image_data = base64.b64decode(image_url)
        
        # Open with PIL and save as JPEG
        image = Image.open(BytesIO(image_data))
        
        # Convert to RGB if necessary
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (11, 16, 32))  # Deep navy background
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        # Resize to standard hero size if needed
        if image.size != (1920, 1080):
            image = image.resize((1920, 1080), Image.Resampling.LANCZOS)
        
        # Save as JPEG with high quality
        image.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
        print(f"Hero image saved to: {output_path}")
        print(f"  Image size: {image.size}")
        print(f"  File size: {os.path.getsize(output_path) / 1024:.1f} KB")
    else:
        print(f"Error: No image in response. Response keys: {list(data.keys())}")
        print(f"Full response: {json.dumps(data, indent=2)}")
        sys.exit(1)

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Response: {e.response.text}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)