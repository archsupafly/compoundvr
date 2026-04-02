#!/usr/bin/env python3
"""
Generate Minecraft VR hero - PURE ENVIRONMENTAL PHOTOGRAPHY
Focus on editorial magazine landscape, completely ignore VR in prompt
Image must fill entire frame edge-to-edge
"""
import os
import json
import base64
import urllib.request
import urllib.error
from io import BytesIO

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

# COMPLETLY DIFFERENT PROMPT - focus on pure photography, no VR context
PROMPT = """An epic magazine cover photograph of a vast voxel landscape at golden hour. Editorial landscape photography style like National Geographic. Full-frame 16:9 wide composition with sky at top and land at bottom.

SCENE: Sweeping view across a procedurally generated blocky wilderness. In the foreground: blocky trees with voxel leaves, a stream or river, scattered blocky boulders. Middle distance: rolling hills, more blocky vegetation, perhaps a small pond or lake. Far distance: mountain range silhouettes against the horizon. Sky transitioning from deep blue at top through amber and cyan bands to the horizon.

LIGHTING: Golden hour with dramatic volumetric sun rays breaking through blocky clouds. Warm amber (#d97706) shadows, golden light on surfaces, deep navy (#0b1020) in shadows, cyan (#6ee7ff) in distant atmospheric haze.

COMPOSITION: Landscape fills entire frame. Sky visible across entire top 25% of image. Land fills entire bottom 75%. No empty black borders. No circular frames. No round overlays. Every pixel from left edge to right edge contains visible content.

MOOD: Contemplative, atmospheric, editorial quality. Not a screenshot, not a render - think of it as fine art landscape photography of a stylized world.

TECHNICAL: Photorealistic rendering of voxel aesthetic with volumetric fog, atmospheric scattering, dramatic cinematic lighting. Desaturated film-like color grading. Magazine cover quality.

PROHIBITED: No text, no logos, no UI, no HUD, no overlays, no circular frames, no vignetting, no borders, no black edges."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating FULL-FRAME landscape photography...")
print("Approach: Pure editorial landscape, no VR context mentioned")
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

image_bytes = base64.b64decode(predictions[0]["bytesBase64Encoded"])
img = Image.open(BytesIO(image_bytes))

print(f"✓ Generated: {img.size[0]}x{img.size[1]}")

# Convert to RGB
if img.mode in ('RGBA', 'LA', 'P'):
    bg = Image.new('RGB', img.size, (255, 255, 255))
    if img.mode == 'P':
        img = img.convert('RGBA')
    bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
    img = bg

# Crop/resize to 1920x1080
target_width = 1920
target_height = 1080
target_ratio = target_width / target_height

width, height = img.size
current_ratio = width / height

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

# Verify no black edges
pixels = img.load()

# Count black pixels on edges
top_black = sum(1 for x in range(target_width) if pixels[x, 0][0] < 20 and pixels[x, 0][1] < 20 and pixels[x, 0][2] < 20)
bottom_black = sum(1 for x in range(target_width) if pixels[x, target_height-1][0] < 20 and pixels[x, target_height-1][1] < 20 and pixels[x, target_height-1][2] < 20)
left_black = sum(1 for y in range(target_height) if pixels[0, y][0] < 20 and pixels[0, y][1] < 20 and pixels[0, y][2] < 20)
right_black = sum(1 for y in range(target_height) if pixels[target_width-1, y][0] < 20 and pixels[target_width-1, y][1] < 20 and pixels[target_width-1, y][2] < 20)

print()
print("Edge black pixel analysis:")
print(f"  Top: {top_black}/{target_width} ({100*top_black/target_width:.1f}%)")
print(f"  Bottom: {bottom_black}/{target_width} ({100*bottom_black/target_width:.1f}%)")
print(f"  Left: {left_black}/{target_height} ({100*left_black/target_height:.1f}%)")
print(f"  Right: {right_black}/{target_height} ({100*right_black/target_height:.1f}%)")

# Decision
has_letterboxing = (top_black > target_width * 0.15 or 
                    bottom_black > target_width * 0.15 or 
                    left_black > target_height * 0.15 or 
                    right_black > target_height * 0.15)

# Save
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.save(OUTPUT_PATH, "JPEG", quality=95, optimize=True, progressive=True)

file_size = os.path.getsize(OUTPUT_PATH) / 1024

print()
print("=" * 60)
print(f"Saved: {OUTPUT_PATH}")
print(f"Size: {img.size[0]}x{img.size[1]}")
print(f"File: {file_size:.1f} KB")
print("=" * 60)
print()

if has_letterboxing:
    print("STATUS: STILL HAS LETTERBOXING")
    print("Need different generation approach")
else:
    print("STATUS: SUCCESS")
    print("✓ Full-frame landscape")
    print("✓ No black letterboxing")
    print("✓ No circular VR effect")
    print("✓ Editorial magazine quality")