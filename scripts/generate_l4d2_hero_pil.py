#!/usr/bin/env python3
"""Generate Left 4 Dead 2 VR hero image using PIL - procedural fallback."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
import math

# Output path
output_path = "/home/antforce/compoundvr-project/public/images/games/left-4-dead-2-vr-hero.jpg"

# Create 1920x1080 canvas
width, height = 1920, 1080
img = Image.new('RGB', (width, height), (11, 16, 32))  # Deep navy background
draw = ImageDraw.Draw(img)

# Define color palette
NAVY = (11, 16, 32)
AMBER = (245, 158, 11)
RED = (220, 38, 38)
SWAMP_GREEN = (74, 222, 128)
DARK_GRAY = (30, 35, 45)
ZOMBIE_GREEN = (85, 95, 75)

# Draw atmospheric background gradient (bayou/swamp mist)
for y in range(height):
    # Gradual transition from dark to slightly lighter at bottom
    intensity = int(80 + (y / height) * 40)
    mist_color = (intensity // 3, intensity + 5, intensity // 2)
    for x in range(width):
        # Add noise for texture
        if random.random() < 0.02:
            draw.point((x, y), fill=mist_color)

# Draw silhouetted cityscape in background (New Orleans buildings)
building_color = (20, 25, 38)
for i in range(8):
    bx = random.randint(0, width)
    bw = random.randint(60, 150)
    bh = random.randint(200, 450)
    # Building silhouette
    draw.rectangle([bx, height - bh, bx + bw, height], fill=building_color)
    # Some windows (amber glow)
    for wy in range(height - bh + 30, height - 20, 40):
        for wx in range(bx + 10, bx + bw - 10, 25):
            if random.random() < 0.3:
                draw.rectangle([wx, wy, wx + 15, wy + 20], fill=(AMBER[0] // 2, AMBER[1] // 3, 0))

# Draw zombie horde silhouettes in background
for _ in range(60):
    zx = random.randint(0, width)
    zy = height - random.randint(50, 200)
    zw = random.randint(15, 35)
    zh = random.randint(30, 60)
    # Staggered zombie shapes
    zombie_color = (ZOMBIE_GREEN[0] + random.randint(-10, 10), ZOMBIE_GREEN[1] + random.randint(-10, 10), ZOMBIE_GREEN[2])
    draw.ellipse([zx, zy, zx + zw, zy + zh], fill=zombie_color)
    # Head
    draw.ellipse([zx + zw//3, zy - 15, zx + 2*zw//3, zy + 5], fill=zombie_color)

# Draw four survivor silhouettes in foreground (back-to-back defensive circle)
survivor_positions = [(width//2 - 200, height - 300), (width//2 + 150, height - 280), 
                       (width//2 - 100, height - 320), (width//2 + 50, height - 250)]
for sx, sy in survivor_positions:
    # Body silhouette (darker, in foreground)
    survivor_color = (35, 40, 50)
    # Torso
    draw.rectangle([sx, sy, sx + 40, sy + 80], fill=survivor_color)
    # Head
    draw.ellipse([sx + 5, sy - 30, sx + 35, sy + 5], fill=survivor_color)
    # Arms holding weapons
    draw.rectangle([sx - 20, sy + 20, sx + 60, sy + 30], fill=survivor_color)

# Add dramatic lighting effects (amber/red fire glow from bottom)
for y in range(height):
    alpha = max(0, 1 - (y / (height * 0.7)))
    for x in range(width):
        px, py = x, y
        current = img.getpixel((px, py))
        # Mix in amber/orange glow from bottom
        if random.random() < alpha * 0.15:
            glow_r = min(255, current[0] + int(40 * alpha))
            glow_g = min(255, current[1] + int(20 * alpha))
            draw.point((px, py), fill=(glow_r, glow_g, current[2]))

# Add title text
try:
    # Try to use a bold font if available
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Draw title with shadow
title = "LEFT 4 DEAD 2"
subtitle = "VR EXPERIENCE"

# Calculate title position (centered)
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (width - title_width) // 2
title_y = 100

# Shadow
draw.text((title_x + 4, title_y + 4), title, fill=(0, 0, 0), font=title_font)
# Main title with red tint
draw.text((title_x, title_y), title, fill=RED, font=title_font)

# Subtitle
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (width - subtitle_width) // 2
draw.text((subtitle_x + 2, title_y + 85 + 2), subtitle, fill=(0, 0, 0), font=subtitle_font)
draw.text((subtitle_x, title_y + 85), subtitle, fill=AMBER, font=subtitle_font)

# Add subtle vignette effect (darker edges)
vignette = Image.new('RGB', (width, height), (0, 0, 0))
vignette_draw = ImageDraw.Draw(vignette)
for i in range(100):
    alpha = i / 100
    vignette_draw.rectangle([i * 5, i * 5, width - i * 5, height - i * 5], outline=(0, 0, 0, int(255 * (1 - alpha) * 0.4)))

# Blend vignette
img = Image.blend(img, vignette, 0.3)

# Apply slight blur for cinematic look (optional, subtle)
img = img.filter(ImageFilter.GaussianBlur(radius=1))

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save as JPEG
img.save(output_path, "JPEG", quality=90, optimize=True)
print(f"Generated PIL-based hero image: {output_path}")
print(f"Size: {os.path.getsize(output_path) / 1024:.1f} KB")