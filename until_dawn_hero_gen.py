#!/usr/bin/env python3
"""
Generate Until Dawn: Rush of Blood hero image procedurally
Until Dawn: Rush of Blood is a PSVR on-rails horror shooter through a haunted carnival/mine ride
Game features: clowns, wendigos, dark mine tunnels, carnival atmosphere, horror
"""

# Pillow is installed in the venv
from PIL import Image, ImageDraw
import math
import os
import random

# Output path
output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"

# Dimensions: 1920x1080 (16:9 hero image specification)
width, height = 1920, 1080

# === Horror/CompoundVR color palette ===
BG_DARK = "#080c18"      # Deep navy black
BG_MID = "#0f1528"       # Dark blue
CLOWN_ORANGE = "#ff6b35" # Eerie carnival orange
CLOWN_YELLOW = "#ffc857" # Sickly yellow
BLOOD_RED = "#8b0000"    # Deep blood red
WENDIGO_WHITE = "#e8e8e8"  # Ghostly white

print("=== Generating Until Dawn: Rush of Blood hero image ===")
print(f"Dimensions: {width}x{height}")
print(f"Style: Horror carnival, on-rails mine cart perspective")
print(f"Output: {output_path}")

# Create base image with gradient
img = Image.new('RGB', (width, height), BG_DARK)
draw = ImageDraw.Draw(img)

# Vertical gradient (dark at top to slightly lighter at bottom)
r1, g1, b1 = 8, 12, 24
r2, g2, b2 = 15, 21, 40
for y in range(height):
    ratio = y / height
    r = int(r1 * (1 - ratio) + r2 * ratio)
    g = int(g1 * (1 - ratio) + g2 * ratio)
    b = int(b1 * (1 - ratio) + b2 * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Convert to RGBA for transparent overlay effects
img = img.convert('RGBA')
draw = ImageDraw.Draw(img)

# === ELEMENT 1: Mine cart track leading into darkness ===
# Creates depth perspective - track starts wide at bottom, narrows toward tunnel
vanish_x = width * 0.5
for i in range(50):
    progress = i / 50
    y_start = int(height * (0.92 - progress * 0.62))
    y_end = int(height * (0.95 - progress * 0.62))
    track_width = 280 * (1 - progress * 0.85)
    x_left = vanish_x - track_width
    x_right = vanish_x + track_width
    brightness = 25 + int(18 * progress)
    draw.rectangle([x_left, y_start, x_right, y_end], fill=(brightness, brightness, brightness + 8))
    
    # Rails on track
    for side in [-1, 1]:
        rail_x = vanish_x + side * (track_width - 5)
        rail_brightness = 50 + int(25 * (1 - progress))
        draw.rectangle([rail_x - 2, y_start, rail_x + 2, y_end], fill=(rail_brightness, rail_brightness - 5, rail_brightness + 15))

# === ELEMENT 2: Dark mine tunnel entrance ===
tunnel_x = int(width * 0.5)
tunnel_y = int(height * 0.12)
tunnel_w = 380
tunnel_h = int(height * 0.32)

# Draw arch depth layers
for d in range(10, -1, -1):
    offset = d * 4
    brightness = 10 + d * 2
    arch_points = [
        (tunnel_x - tunnel_w // 2 + offset, tunnel_y + tunnel_h),
        (tunnel_x - tunnel_w // 2 + offset, tunnel_y + tunnel_h * 0.35 - offset // 10),
        (tunnel_x - tunnel_w // 4 + offset // 2, tunnel_y + offset // 3),
        (tunnel_x, tunnel_y - tunnel_h * 0.12 + offset // 4),
        (tunnel_x + tunnel_w // 4 - offset // 2, tunnel_y + offset // 3),
        (tunnel_x + tunnel_w // 2 - offset, tunnel_y + tunnel_h * 0.35 - offset // 10),
        (tunnel_x + tunnel_w // 2 - offset, tunnel_y + tunnel_h),
    ]
    draw.polygon(arch_points, fill=(brightness, brightness, brightness + 5))

# Red emergency light glow deep in tunnel
draw.ellipse([tunnel_x - 35, tunnel_y - 25, tunnel_x + 35, tunnel_y + 15], fill=(50, 0, 0))
draw.ellipse([tunnel_x - 25, tunnel_y - 18, tunnel_x + 25, tunnel_y + 8], fill=(70, 5, 5))

# === ELEMENT 3: Menacing clown figures ===
def draw_clown(draw, x, y, scale, facing_right=True, distant=False):
    """Draw a horror clown silhouette with glowing orange eyes."""
    if not facing_right:
        x = int(x - 45 * scale)
    
    body_color = (25, 25, 30) if distant else (35, 35, 42)
    
    # Hunched body
    draw.ellipse([x - 35 * scale, y - 65 * scale, x + 35 * scale, y + 45 * scale], fill=body_color)
    
    # Head
    head_y = int(y - 55 * scale)
    draw.ellipse([x - 28 * scale, head_y - 32 * scale, x + 28 * scale, head_y + 32 * scale], fill=(18, 18, 22))
    
    # Glowing eyes (signature clown horror element)
    eye_y = head_y - 5
    eye_size = max(6, int(7 * scale))
    draw.ellipse([x - 14 * scale, eye_y - eye_size // 2, x - 6 * scale, eye_y + eye_size // 2], fill=CLOWN_ORANGE)
    draw.ellipse([x + 6 * scale, eye_y - eye_size // 2, x + 14 * scale, eye_y + eye_size // 2], fill=CLOWN_ORANGE)
    
    if not distant:
        # Creepy wide smile
        draw.arc([x - 18 * scale, head_y + 8, x + 18 * scale, head_y + 28 * scale], 0, 180, fill=CLOWN_ORANGE, width=3)
        # Glow effect around eyes
        draw.ellipse([x - 20 * scale, eye_y - 12, x + 20 * scale, eye_y + 12], fill=(200, 80, 20))

# Foreground clown on left (larger, more menacing)
draw_clown(draw, width * 0.22, height * 0.58, scale=1.35, facing_right=True, distant=False)

# Background clown on right (smaller, in shadows)
draw_clown(draw, width * 0.80, height * 0.42, scale=0.85, facing_right=False, distant=True)

# === ELEMENT 4: Wendigo silhouettes in far background ===
def draw_wendigo(draw, x, y, scale):
    """Draw a wendigo silhouette - tall, emaciated, antlered."""
    color = (8, 8, 12)
    
    # Emaciated body
    draw.polygon([
        (x - 12 * scale, y),
        (x - 18 * scale, y + 55 * scale),
        (x - 8 * scale, y + 75 * scale),
        (x + 8 * scale, y + 75 * scale),
        (x + 18 * scale, y + 55 * scale),
        (x + 12 * scale, y),
    ], fill=color)
    
    # Elongated head
    draw.ellipse([x - 10 * scale, y - 38 * scale, x + 10 * scale, y - 3 * scale], fill=color)
    
    # Antlers
    draw.line([x - 6 * scale, y - 32 * scale, x - 28 * scale, y - 65 * scale], fill=color, width=2)
    draw.line([x + 6 * scale, y - 32 * scale, x + 28 * scale, y - 65 * scale], fill=color, width=2)
    # Antler points
    draw.line([x - 22 * scale, y - 58 * scale, x - 30 * scale, y - 55 * scale], fill=color, width=1)
    draw.line([x + 22 * scale, y - 58 * scale, x + 30 * scale, y - 55 * scale], fill=color, width=1)
    
    # Ghostly white eyes
    draw.ellipse([x - 4 * scale, y - 24 * scale, x - 1 * scale, y - 19 * scale], fill=WENDIGO_WHITE)
    draw.ellipse([x + 1 * scale, y - 24 * scale, x + 4 * scale, y - 19 * scale], fill=WENDIGO_WHITE)

# Two wendigos in the tunnel darkness
draw_wendigo(draw, width * 0.43, height * 0.26, scale=0.55)
draw_wendigo(draw, width * 0.57, height * 0.23, scale=0.45)

# === ELEMENT 5: Flickering carnival/emergency lights ===
random.seed(666)  # Horror seed!

# Light positions and their glow
light_positions = [
    (width * 0.12, height * 0.32),   # Left side
    (width * 0.88, height * 0.28),    # Right side  
    (width * 0.35, height * 0.22),    # Upper left
]

for lx, ly in light_positions:
    lx, ly = int(lx), int(ly)
    
    # Bright core
    draw.ellipse([lx - 12, ly - 12, lx + 12, ly + 12], fill=(255, 150, 50))
    
    # Outer glow (multiple layers)
    for radius in range(90, 20, -15):
        intensity = random.randint(180, 230)
        draw.ellipse([lx - radius, ly - radius, lx + radius, ly + radius], 
                     fill=(intensity, int(intensity * 0.4), 0))

# === ELEMENT 6: Atmospheric fog ===
fog_overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
fog_draw = ImageDraw.Draw(fog_overlay)

for y in range(int(height * 0.65), height):
    fog_density = (y - height * 0.65) / (height * 0.35)
    for x in range(0, width, 4):
        if random.random() < fog_density * 0.2:
            alpha = int(20 + random.randint(0, 30) * fog_density)
            fog_draw.point((x, y), fill=(100, 110, 130, alpha))

# Dust particles in light beams
for _ in range(200):
    x = random.randint(0, width - 1)
    y = random.randint(0, int(height * 0.75))
    size = random.randint(1, 2)
    brightness = random.randint(120, 200)
    alpha = random.randint(15, 45)
    fog_draw.ellipse([x, y, x + size, y + size], fill=(brightness, brightness - 20, brightness - 40, alpha))

img = Image.alpha_composite(img, fog_overlay)

# === ELEMENT 7: Vignette for cinematic feel ===
vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
vig_draw = ImageDraw.Draw(vignette)

for i in range(130):
    alpha = int(i * 1.3)
    vig_draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
    vig_draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
    vig_draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
    vig_draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))

img = Image.alpha_composite(img, vignette)

# === ELEMENT 8: God rays from above ===
ray_overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
ray_draw = ImageDraw.Draw(ray_overlay)

# Subtle light rays from upper center
for i in range(12):
    angle_start = (i - 6) * 0.06
    x_start = int(width * 0.5)
    x_end_left = int(x_start + math.tan(angle_start - 0.02) * height)
    x_end_right = int(x_start + math.tan(angle_start + 0.02) * height)
    
    points = [
        (x_start, 0),
        (x_end_left - 20, height),
        (x_end_right + 20, height),
    ]
    ray_draw.polygon(points, fill=(255, 200, 100, 3))

img = Image.alpha_composite(img, ray_overlay)

# === Save final image ===
img_rgb = img.convert('RGB')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
img_rgb.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)

file_size = os.path.getsize(output_path)
print("\n=== SUCCESS ===")
print(f"Generated: Until Dawn: Rush of Blood hero image")
print(f"Output: {output_path}")
print(f"Dimensions: {width}x{height}")
print(f"File size: {file_size / 1024:.1f} KB ({file_size} bytes)")
print("Style: Horror carnival, on-rails mine cart perspective, clowns and wendigos")