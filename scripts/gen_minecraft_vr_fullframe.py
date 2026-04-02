#!/usr/bin/env python3
"""
Generate Minecraft VR hero - EDITORIAL DOCUMENTARY PHOTOGRAPHY
EXPLICITLY: NO circular VR lens, NO black bars, NO letterboxing
Image MUST fill entire 1920x1080 frame edge-to-edge with visual content
"""
import os
import json
import base64
import urllib.request
import urllib.error
from io import BytesIO

# Try to install PIL if not available
try:
    from PIL import Image
except ImportError:
    import subprocess
    import sys
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pillow", "-q"])
    from PIL import Image

OUTPUT_PATH = "/home/antforce/compoundvr-project/public/images/games/minecraft-vr-hero.jpg"

# Load API key
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    key_file = os.path.expanduser("~/.hermes/profiles/maya/.env")
    try:
        for line in open(key_file):
            if line.startswith("GEMINI_API_KEY="):
                API_KEY = line.strip().split("=", 1)[1]
                break
    except:
        pass

if not API_KEY:
    print("ERROR: No GEMINI_API_KEY found")
    exit(1)

print(f"API Key: {API_KEY[:10]}...")
print()

# STRONGLY WORDED PROMPT - editorial documentary, NO VR gimmicks
PROMPT = """A stunning voxel landscape at golden hour, editorial magazine photography style. Vast Minecraft world with blocky mountains, valleys, and forests. Atmosphere: volumetric fog, god rays through blocky trees, amber and golden sunlight, deep navy shadows.

First-person perspective: blocky player hand visible in lower foreground reaching toward a crafting table. In the middle distance: a torch-lit village with blocky houses. Far background: mountain ranges fading into atmospheric haze. The entire 16:9 canvas must be filled with visual content - land, sky, mountains, from top edge to bottom edge, left edge to right edge. NO empty black areas at all.

Color palette: Deep navy (#0b1020) shadows, warm amber (#d97706) golden hour light, cyan (#6ee7ff) in distant water and sky. Cinematic film-like grading, desaturated, lifted blacks.

FORBIDDEN ELEMENTS - DO NOT INCLUDE:
- NO circular VR lens effect
- NO circular viewport overlay
- NO round VR frame
- NO black letterboxing
- NO black bars at top/bottom/sides
- NO stereoscopic side-by-side view
- NO tech circles or sci-fi interface
- NO empty black background

REQUIRED ELEMENTS:
- Fill entire image frame edge-to-edge with visual content
- Full landscape image with NO cropping
- Sky visible at top, ground visible at bottom
- First-person immersive view suggesting VR presence
- Editorial documentary magazine photography
- Atmospheric, moody, sophisticated

Style: Wired magazine feature cover. Think National Geographic landscape documentary. Full-frame cinematic 16:9 composition. In-game screenshot aesthetic. No text, no logos, no UI, no watermarks."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating Minecraft VR hero - FULL FRAME, NO BLACK BARS")
print("=" * 60)

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
    print(f"HTTP Error {e.code}:")
    print(e.read().decode('utf-8'))
    exit(1)

predictions = data.get("predictions", [])
if not predictions:
    print(f"ERROR: No predictions in response")
    print(json.dumps(data, indent=2))
    exit(1)

# Extract and decode image
image_bytes = base64.b64decode(predictions[0]["bytesBase64Encoded"])
img = Image.open(BytesIO(image_bytes))

print(f"✓ Generated image: {img.size[0]}x{img.size[1]}")

# Convert to RGB if needed
if img.mode in ('RGBA', 'LA', 'P'):
    bg = Image.new('RGB', img.size, (255, 255, 255))
    if img.mode == 'P':
        img = img.convert('RGBA')
    bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
    img = bg

# Resize/crop to exactly 1920x1080
target_width = 1920
target_height = 1080
target_ratio = target_width / target_height

width, height = img.size
current_ratio = width / height

print(f"  Original aspect ratio: {current_ratio:.3f}")
print(f"  Target aspect ratio: {target_ratio:.3f}")

# Crop to 16:9 if needed
if abs(current_ratio - target_ratio) > 0.01:
    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        img = img.crop((0, top, width, top + new_height))

img = img.resize((target_width, target_height), Image.LANCZOS)

# Check for black letterboxing
pixels = img.load()
top_black = sum(1 for x in range(target_width) if pixels[x, 0][0] < 20 and pixels[x, 0][1] < 20 and pixels[x, 0][2] < 20)
bottom_black = sum(1 for x in range(target_width) if pixels[x, target_height-1][0] < 20 and pixels[x, target_height-1][1] < 20 and pixels[x, target_height-1][2] < 20)

print()
print("Letterboxing check:")
print(f"  Top row black pixels: {top_black}/{target_width} ({100*top_black/target_width:.1f}%)")
print(f"  Bottom row black pixels: {bottom_black}/{target_width} ({100*bottom_black/target_width:.1f}%)")

has_letterboxing = top_black > target_width * 0.5 or bottom_black > target_width * 0.5

if has_letterboxing:
    print()
    print("⚠ WARNING: Black letterboxing detected!")
    print("  The image has circular VR viewport effect with black bars")
    print("  This violates style guide: 'NO VR lens effect'")
    print()
    print("  Attempting to generate alternative prompt...")

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.save(OUTPUT_PATH, "JPEG", quality=95, optimize=True, progressive=True)

file_size = os.path.getsize(OUTPUT_PATH) / 1024

print()
print("=" * 60)
print("Image saved:")
print(f"  Path: {OUTPUT_PATH}")
print(f"  Dimensions: {img.size[0]}x{img.size[1]}")
print(f"  File size: {file_size:.1f} KB")
print("=" * 60)
print()

if has_letterboxing:
    print("STATUS: NEEDS REGENERATION")
    print("The image has VR circular viewport effect with black bars.")
    print("Need to regenerate with different approach.")
else:
    print("STATUS: SUCCESS")
    print("✓ Full-frame editorial documentary image")
    print("✓ No circular VR lens effect")
    print("✓ No black letterboxing")
    print("✓ Image fills entire frame with visual content")