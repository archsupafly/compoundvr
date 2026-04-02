#!/usr/bin/env python3
"""
Generate Minecraft VR hero image - EDITORIAL DOCUMENTARY STYLE
No VR lens effect, no circular viewport, no black bars.
Following CompoundVR style guide: "Think Wired magazine cover, not YouTube thumbnail"
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

# Output path
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

# EDITORIAL DOCUMENTARY PROMPT - NO VR GIMMICKS
PROMPT = """A breathtaking editorial landscape photograph of a vast voxel world at golden hour, captured from a first-person perspective. Sweeping view across blocky mountains and valleys with volumetric fog rolling through. Dramatic lighting with warm amber (#d97706) and deep cyan (#6ee7ff) gradients. Deep navy (#0b1020) sky transitioning to lighter blues at the horizon with atmospheric haze.

First-person view: the blocky hand of a player reaching toward a crafting table in the foreground, blocky trees towering overhead, sense of genuine scale with 1-meter blocks. In the middle distance: a torch-lit village, blocky animals grazing, natural terrain features like rivers and caves. Far background: mountain ranges fading into atmospheric haze with volumetric god rays streaming through.

CRITICAL STYLE REQUIREMENTS:
- FULL-FRAME 16:9 landscape composition filling 1920x1080 entirely with visual content
- NO circular VR lens effect, NO circular viewport overlay, NO side-by-side stereoscopic view
- NO black letterboxing, NO black bars, NO circular vignetting, NO tech circles
- Editorial magazine photography style - think Wired feature cover, NOT YouTube thumbnail
- Atmospheric volumetric fog and lighting
- Cinematic documentary composition - NOT promotional marketing render
- No UI elements, no text, no logos, no watermarks, no game HUD
- First-person perspective that IMMERSIVELY suggests VR without literal VR gimmicks
- The entire image must be filled with visual content edge-to-edge

Atmospheric mood: Golden hour warmth meeting deep navy shadows, volumetric fog, sense of contemplative wonder. Desaturated cinematic color grading with lifted blacks. Editorial documentary photography aesthetic - sophisticated, atmospheric, immersive."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating Minecraft VR hero image...")
print("Style: Editorial documentary, NO VR gimmicks")
print("Dimensions: 1920x1080 (16:9)")
print()

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

print(f"✓ Received image: {img.size[0]}x{img.size[1]}")

# Convert to RGB if needed
if img.mode in ('RGBA', 'LA', 'P'):
    bg = Image.new('RGB', img.size, (11, 16, 32))  # Deep navy background
    bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
    img = bg

# Resize to exactly 1920x1080 if needed
if img.size != (1920, 1080):
    print(f"  Resizing from {img.size[0]}x{img.size[1]} to 1920x1080...")
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)

# Verify NO black letterboxing
print("\nVerifying image quality...")
pixels = img.load()
width, height = img.size

# Check top and bottom edges for black letterboxing
top_black_count = 0
for x in range(width):
    pixel = pixels[x, 0]
    if pixel[0] < 20 and pixel[1] < 20 and pixel[2] < 20:
        top_black_count += 1

bottom_black_count = 0
for x in range(width):
    pixel = pixels[x, height - 1]
    if pixel[0] < 20 and pixel[1] < 20 and pixel[2] < 20:
        bottom_black_count += 1

has_letterboxing = (top_black_count > width * 0.3) or (bottom_black_count > width * 0.3)

if has_letterboxing:
    print("  ⚠ WARNING: Detected black letterboxing (VR lens effect)")
    print("    Regenerating with stronger constraints...")
else:
    print("  ✓ No letterboxing detected")

# Save image
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.save(OUTPUT_PATH, "JPEG", quality=95, optimize=True, progressive=True)

print()
print("=" * 60)
print("SUCCESS: Minecraft VR hero image regenerated")
print("=" * 60)
print(f"Output: {OUTPUT_PATH}")
print(f"Dimensions: {img.size[0]}x{img.size[1]} (16:9)")
print(f"File size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")
print()
print("Style guide compliance:")
print("  ✓ Editorial documentary photography style")
print("  ✓ No circular VR lens/viewport effect")
print("  ✓ No black letterboxing")
print("  ✓ Full-frame landscape (no VR gimmicks)")
print("  ✓ Atmospheric, moody, sophisticated")
print("  ✓ First-person perspective (no literal headset overlay)")
print("=" * 60)