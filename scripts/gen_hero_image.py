#!/usr/bin/env python3
"""
Generate DiRT Rally VR Hero Image - Procedural Generator
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents, purple #8b5cf6)
Style: Gritty rally motorsport, realistic simulation, cinematic
"""

import subprocess
import sys
import os
import math
import random

# Install dependencies first
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "--user", "-q"])
from PIL import Image, ImageDraw, ImageFilter

# Brand colors
BG_PRIMARY = "#0b1020"
BG_SECONDARY = "#0f1528"
ACCENT_CYAN = "#6ee7ff"
ACCENT_CYAN_GLOW = (110, 231, 255, 80)
TEXT_PRIMARY = "#f0f4ff"
SURFACE_PRIMARY = "#151d38"
PURPLE_ACCENT = (139, 92, 246, 60)
MUD_BROWN = (139, 90, 43)

def create_gradient_background(width, height, color1, color2):
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
        g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
        b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def draw_rally_car(draw, x, y, scale, color):
    """Draw a rally car silhouette."""
    # Car body
    body = [
        (x - 100*scale, y + 20*scale),
        (x - 95*scale, y - 20*scale),
        (x - 60*scale, y - 30*scale),
        (x - 20*scale, y - 45*scale),
        (x + 10*scale, y - 50*scale),
        (x + 50*scale, y - 50*scale),
        (x + 70*scale, y - 35*scale),
        (x + 90*scale, y - 15*scale),
        (x + 100*scale, y + 10*scale),
        (x + 100*scale, y + 25*scale),
        (x - 100*scale, y + 25*scale),
    ]
    draw.polygon(body, fill=color)
    
    # Wheels
    wheel_y = y + 30*scale
    draw.ellipse([x-70*scale-15, wheel_y-15, x-70*scale+15, wheel_y+15], fill=color)
    draw.ellipse([x+50*scale-15, wheel_y-15, x+50*scale+15, wheel_y+15], fill=color)
    
    # Headlight glow
    draw.ellipse([x-102*scale, y-5*scale, x-95*scale, y+15*scale], fill=ACCENT_CYAN)

def main():
    width, height = 1920, 1080
    img = create_gradient_background(width, height, BG_PRIMARY, BG_SECONDARY)
    draw = ImageDraw.Draw(img, 'RGBA')
    
    random.seed(42)  # Consistent results
    
    # Atmospheric dust/mud spray
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(20, 120)
        alpha = random.randint(10, 40)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=(139, 90, 43, alpha))
    
    # Purple accent glows
    for _ in range(40):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(30, 100)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=PURPLE_ACCENT)
    
    # Draw rally car
    draw_rally_car(draw, width*0.55, height*0.55, 3.0, SURFACE_PRIMARY)
    
    # Cyan speed lines
    for i in range(10):
        y_start = 150 + i * 90
        draw.line([(30, y_start), (620, y_start - 55)], fill=ACCENT_CYAN_GLOW, width=3)
        draw.line([(1300, y_start + 35), (1890, y_start - 15)], fill=ACCENT_CYAN_GLOW, width=2)
    
    # Central atmospheric glow
    for r in range(280, 40, -30):
        alpha = max(5, int(30 * (280 - r) / 240))
        draw.ellipse([width//2-r, height//2-r, width//2+r, height//2+r], 
                     outline=(110, 231, 255, alpha), width=5)
    
    # Ground texture
    for y in range(height - 250, height):
        for x in range(0, width, 55):
            alpha = random.randint(5, 30)
            draw.point((x + random.randint(0, 55), y), fill=(139, 90, 43, alpha))
    
    # Blur for atmosphere
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Save
    output_path = "/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    print(f"SUCCESS: Hero image saved to {output_path}")
    print(f"SIZE: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()