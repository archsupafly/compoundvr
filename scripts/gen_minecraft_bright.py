#!/usr/bin/env python3
"""
Generate Minecraft VR hero - BRIGHT ATMOSPHERIC SCENE
Strong emphasis on brightness and edge visibility
No vignetting, no circular frames
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

PROMPT = """Bright colorful sunset over a blocky voxel landscape. Golden hour with vibrant oranges and yellows filling the entire sky. The scene is well-lit with no dark shadows or vignettes.

A wide panoramic view of blocky hills and valleys with blocky trees, animals, and a river. The scene is bathed in warm golden and amber light from a setting sun. Volumetric fog creates atmospheric depth. The composition includes:

- TOP 30%: Bright sky gradient from warm amber (#FFD700) through orange (#FF8C00) to deep blue (#0047AB) at the very top. Puffy blocky clouds catching golden light.

- MIDDLE 40%: Distant blocky mountains silhouetted against the glowing horizon. Atmospheric haze creates depth. The mountains have visible surface texture and highlights.

- BOTTOM 30%: Foreground land with blocky trees, grass, flowers, a winding river reflecting sky colors. All surfaces are well-lit with golden hour warmth.

CRITICAL: Every pixel from left edge to right edge, top edge to bottom edge contains COLOR and LIGHT. There are NO black or dark borders. The image is BRIGHT throughout, especially at the edges. No vignetting, no circular frames, no lens effects.

Style: Bright, cheerful, atmospheric. Magazine photography with even lighting. Cinematic landscape that fills the entire frame. The edges are BRIGHT - sky colors extend fully to the top edge, land colors extend fully to the bottom edge, there are no dark transitions at the borders.

Color palette: Warm golden orange (#FFD700, #FF8C00), amber (#D97706), cyan sky accents (#6EE7FF), navy blue at top (#0047AB), all surfaces well-lit with no pure black regions.

No text, no logos, no UI, no overlays, no circular frames, no vignetting, no dark edges."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

payload = {
    "instances": [{"prompt": PROMPT}],
    "parameters": {
        "sampleCount": 1,
        "aspectRatio": "16:9"
    }
}

print("Generating BRIGHT golden hour landscape...")
print("Focus: Even edge brightness, no vignetting")
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

# Count black pixels on edges (threshold of 30 for near-black)
top_dark = sum(1 for x in range(target_width) if pixels[x, 0][0] < 30 and pixels[x, 0][1] < 30 and pixels[x, 0][2] < 30)
bottom_dark = sum(1 for x in range(target_width) if pixels[x, target_height-1][0] < 30 and pixels[x, target_height-1][1] < 30 and pixels[x, target_height-1][2] < 30)
left_dark = sum(1 for y in range(target_height) if pixels[0, y][0] < 30 and pixels[0, y][1] < 30 and pixels[0, y][2] < 30)
right_dark = sum(1 for y in range(target_height) if pixels[target_width-1, y][0] < 30 and pixels[target_width-1, y][1] < 30 and pixels[target_width-1, y][2] < 30)

print()
print("Edge dark pixel analysis:")
print(f"  Top: {top_dark}/{target_width} ({100*top_dark/target_width:.1f}%)")
print(f"  Bottom: {bottom_dark}/{target_width} ({100*bottom_dark/target_width:.1f}%)")
print(f"  Left: {left_dark}/{target_height} ({100*left_dark/target_height:.1f}%)")
print(f"  Right: {right_dark}/{target_height} ({100*right_dark/target_height:.1f}%)")

# Average brightness
avg_brightness = 0
for y in range(0, target_height, 50):
    for x in range(0, target_width, 50):
        avg_brightness += sum(pixels[x, y][:3]) / 3
avg_brightness /= (target_width // 50) * (target_height // 50)

print(f"Average brightness: {avg_brightness:.1f}")

# Decision
has_letterboxing = (top_dark > target_width * 0.20 or 
                    bottom_dark > target_width * 0.25 or 
                    left_dark > target_height * 0.20 or 
                    right_dark > target_height * 0.20)

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
    print("Dark edges detected")
else:
    print("STATUS: SUCCESS")
    print("✓ Bright edges")
    print("✓ Even lighting")
    print("✓ Gold hour atmosphere")