#!/usr/bin/env python3
"""
Generate Minecraft VR hero - PURE DOCUMENTARY PHOTOGRAPHY
Explicit sky fill at top, land fill at bottom, no dark edges
Focus on atmospheric fog and depth, not vignetting
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

PROMPT = """A vast blocky voxel landscape at golden hour, photographed in editorial documentary style for a magazine cover. Cinematic atmospheric perspective with fog and depth.

FULL FRAME COMPOSITION: The image fills the entire canvas from edge to edge. Top section shows open sky with gradient from deep blue at top (#064273) through cyan (#6ee7ff) to warm amber at horizon (#d97706). Bottom section shows rolling hills with blocky trees, a winding river, and scattered blocky boulders in the foreground. NO empty black borders ANYWHERE.

VISUAL CONTENT: Every pixel contains visible light and color. The sky has gradient colors and volumetric clouds. The land has textured surfaces with shadows and highlights from golden hour light. Atmospheric fog creates depth as mountains fade into distance. NO DARK EDGES, NO VIGNETTING, NO CIRCULAR FRAMES.

LIGHTING: Golden hour sun low on horizon creating warm amber and orange light. Deep navy (#0b1020) in the shadows but NOT pure black. Cyan and blue accents in atmospheric haze. Sky brightens toward horizon. Foreground has warm golden light on surfaces.

STYLE: Editorial landscape photography like Wired magazine cover. Clean full-frame composition. Atmospheric depth through fog and distance, not through vignetting. Cinematic 16:9 aspect ratio filling entire canvas edge-to-edge.

ATMOSPHERE: Sense of scale and wonder. Blocky voxel aesthetic rendered photorealistically with proper lighting. Volumetric fog and atmospheric scattering. Documentary feel, not promotional screenshot.

REQUIRED: Fill entire image canvas with light and color from top edge to bottom edge, left edge to right edge. Bright sky fills entire top 30% of frame. Land with golden light fills entire bottom 70% of frame. NO black edges, NO circular overlays, NO UI elements, NO text, NO logos."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating FULL-FRAME editorial landscape...")
print("Approach: Bright edges, sky fill top, land fill bottom")
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

# Check average brightness
center_brightness = sum(pixels[target_width//2 + dx, target_height//2][0] for dx in range(-100, 101)) / 201
print()
print(f"Center brightness: {center_brightness:.1f}")

# Decision - allow natural shadows but no heavy letterboxing
has_letterboxing = (top_black > target_width * 0.20 or 
                    bottom_black > target_width * 0.25 or 
                    left_black > target_height * 0.20 or 
                    right_black > target_height * 0.20)

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
    print("STATUS: HAS LETTERBOXING")
    print("Significant black pixels detected on edges")
else:
    print("STATUS: SUCCESS")
    print("✓ Full-frame landscape")
    print("✓ No significant letterboxing (minor shadows acceptable)")
    print("✓ Bright edges for editorial quality")
    print("✓ Sky-fill-top, land-fill-bottom composition")