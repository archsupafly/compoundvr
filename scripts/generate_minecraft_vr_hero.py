#!/usr/bin/env python3
"""Generate Minecraft VR hero image using Gemini Imagen - editorial documentary style."""
import os
import sys
import subprocess
import json
import base64
import urllib.request
import urllib.error
from io import BytesIO

# Install dependencies first
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "--user", "-q"])
from PIL import Image

# Output path
output_path = "/home/antforce/compoundvr-project/public/images/games/minecraft-vr-hero.jpg"

# Gemini API key - load from env or file
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    key_file = os.path.expanduser("~/.hermes/profiles/maya/.env")
    try:
        for line in open(key_file):
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.strip().split("=", 1)[1]
                break
    except:
        pass

if not api_key:
    print("ERROR: No GEMINI_API_KEY found")
    exit(1)

print(f"API Key found: {api_key[:10]}...")

# Prompt for Minecraft VR - Editorial documentary style, NO VR gimmicks
prompt = """Blocky voxel landscape at golden hour, sweeping view across a vast Minecraft world. Atmospheric volumetric fog rolls through a valley between blocky mountains. Deep navy sky transitions to cyan and amber bands at the horizon. In the foreground, a first-person view of a player's blocky hand reaching toward a crafting table. No UI, no text, no HUD.

The scene captures the transformative feeling of standing inside Minecraft in VR - genuine sense of scale with 1-meter blocks towering above. Volumetric lighting streams through blocky tree canopies. Dramatic shadows and atmospheric haze. A distant village silhouette with torchlight flickering.

Color palette: Deep navy (#0b1020) shadows, warm amber (#d97706) from setting sun, cyan accents (#6ee7ff) in distant water and sky gradients. Lifted blacks, cinematic film-like grading, reduced saturation.

Style: Editorial documentary photography, Wired magazine feature cover, atmospheric landscape photography. Cinematic 16:9 wide composition. Think in-game screenshot from a moody, atmospheric Minecraft world - NOT a marketing render, NOT a VR gimmick.

CRITICAL REQUIREMENTS:
- Full-frame landscape filling the entire 1920x1080 canvas edge-to-edge with visual content
- NO circular VR lens effect, NO VR viewport overlay, NO black letterboxing, NO black bars
- NO stereoscopic side-by-side view
- NO tech circles, NO sci-fi interface elements, NO promotional graphics
- Think: atmospheric screenshot, not VR demonstration
- Cinematic documentary still, not YouTube thumbnail, not VR marketing image
- No text, no logos, no watermarks, no game UI overlays
- Photorealistic rendering of voxel aesthetic, volumetric fog, atmospheric depth
- Editorial magazine quality - sophisticated, moody, contemplative
- First-person perspective that implies VR immersion WITHOUT literal VR viewport gimmicks"""

# Use correct model name
url = "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=" + api_key

payload = {
    "instances": [{"prompt": prompt}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating Minecraft VR hero image with Gemini Imagen...")
print(f"Style: Editorial documentary, NO VR gimmicks")
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

# Resize to exactly 1920x1080 if needed
if img.size != (1920, 1080):
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)

# Verify no black letterboxing (check top/bottom edges)
pixels = img.load()
has_top_black = all(pixels[x, 0][0] < 20 and pixels[x, 0][1] < 20 and pixels[x, 0][2] < 20 for x in range(img.width))
has_bottom_black = all(pixels[x, img.height-1][0] < 20 and pixels[x, img.height-1][1] < 20 and pixels[x, img.height-1][2] < 20 for x in range(img.width))

if has_top_black or has_bottom_black:
    print("WARNING: Detected potential black letterboxing! The image should fill the entire frame.")

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save with high quality
img.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
print(f"SUCCESS: Saved Minecraft VR hero to {output_path}")
print(f"Image size: {img.size[0]}x{img.size[1]}")
print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")
print(f"Style: Full-frame editorial documentary, no VR gimmicks")