#!/usr/bin/env python3
"""Generate Left 4 Dead 2 VR hero image using Gemini Imagen."""
import os
import json
import base64
import urllib.request
import urllib.error
from io import BytesIO
from PIL import Image

# Output path
output_path = "/home/antforce/compoundvr-project/public/images/games/left-4-dead-2-vr-hero.jpg"

# Gemini API key - load from env or file
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    key_file = os.path.expanduser("~/.hermes/profiles/maya/.env")
    try:
        for line in open(key_file):
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.strip().split("=", 1)[1]
                break
    except FileNotFoundError:
        pass

if not api_key:
    # Try alternate location
    alt_key_file = os.path.expanduser("~/.config/hermes/maya.env")
    try:
        for line in open(alt_key_file):
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.strip().split("=", 1)[1]
                break
    except FileNotFoundError:
        pass

if not api_key:
    print("ERROR: No GEMINI_API_KEY found in environment or config files")
    exit(1)

print(f"API Key found: {api_key[:10]}...")

# Prompt for Left 4 Dead 2
prompt = """A cinematic hero image for Left 4 Dead 2 VR featuring four survivors (Coach, Ellis, Rochelle, Nick) in a Southern Gothic zombie apocalypse setting. The survivors stand back-to-back in a defensive circle in a flooded New Orleans street, weapons raised against an overwhelming horde of infected zombies emerging from the dark bayou mist. 

A baseball bat, assault rifle, and chainsaw are visible among the survivors' weapons. In the background: abandoned French Quarter buildings with shattered windows, Spanish moss hanging from dead oak trees, and an ominous stormy sky with lightning.

Color palette: Deep navy blue (#0b1020) dark background, warm amber (#f59e0b) from flickering street fires and muzzle flash, blood red (#dc2626) accents from danger, and sickly swamp green (#4ade80) emergency lighting cutting through the darkness. Apocalyptic, atmospheric horror with cinematic lighting.

Style: Dark, gritty, cinematic movie poster quality. Wide 16:9 editorial composition. High detail, dramatic action scene. No text, no logos, no watermarks, no game UI. The scene should convey intense co-op survival horror action in virtual reality."""

# Use correct model name
url = "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=" + api_key

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating Left 4 Dead 2 VR hero image with Gemini Imagen...")
req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    with urllib.request.urlopen(req, timeout=120) as response:
        data = json.loads(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
    exit(1)

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

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save
img.save(output_path, "JPEG", quality=95, optimize=True)
print(f"Saved: {output_path}")
print(f"Size: {os.path.getsize(output_path) / 1024:.1f} KB")