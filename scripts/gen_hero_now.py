#!/usr/bin/env python3
"""Generate DiRT Rally hero image using Gemini Imagen."""
import os
import requests
import base64
from io import BytesIO
from PIL import Image

# Output path
output_path = "/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg"

# Gemini API key - load from env or file
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    key_file = os.path.expanduser("~/.hermes/profiles/maya/.env")
    for line in open(key_file):
        if line.startswith("GEMINI_API_KEY="):
            api_key = line.strip().split("=", 1)[1]
            break

if not api_key:
    print("ERROR: No GEMINI_API_KEY found")
    exit(1)

print(f"API Key found: {api_key[:10]}...")

# Prompt for DiRT Rally
prompt = """Professional rally car speeding through a muddy forest rally stage, dynamic action shot with dramatic gravel and mud spray. A Ford Fiesta RS WRC rally car in motion, cockpit visible showing driver perspective for VR immersion. Dense pine forest lining a gravel rally stage, moody overcast atmosphere with cinematic lighting.

Color palette: Deep navy (#0b1020) dark background, cyan (#6ee7ff) accent highlights from headlights cutting through dust, subtle purple (#8b5cf6) undertones. Gritty, realistic motorsport aesthetic.

Style: Editorial magazine cover quality, dark sophisticated atmosphere, professional automotive photography. Wide 16:9 cinematic composition. High detail, photorealistic. No text, no logos, no watermarks, no game UI."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-preview:predict?key={api_key}"

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating hero image with Gemini Imagen...")
response = requests.post(url, json=payload, timeout=120)
response.raise_for_status()
data = response.json()

# Extract image
predictions = data.get("predictions", [])
if not predictions:
    print(f"No predictions in response: {data}")
    exit(1)

image_bytes = base64.b64decode(predictions[0]["bytesBase64Encoded"])
img = Image.open(BytesIO(image_bytes))

# Convert to RGB if needed
if img.mode in ('RGBA', 'LA', 'P'):
    bg = Image.new('RGB', img.size, (11, 16, 32))
    bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
    img = bg

# Resize to 1920x1080 if needed
if img.size != (1920, 1080):
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)

# Save
img.save(output_path, "JPEG", quality=95, optimize=True)
print(f"Saved: {output_path}")
print(f"Size: {os.path.getsize(output_path) / 1024:.1f} KB")