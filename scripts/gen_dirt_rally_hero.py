#!/usr/bin/env python3
"""
Generate DiRT Rally VR Hero Image
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Style: Technical authority, rally motorsport, gritty realistic
"""

import subprocess
import sys

# Install dependencies first
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "--user", "-q"])

from PIL import Image, ImageDraw, ImageFilter
import math
import os

# Brand colors
BG_PRIMARY = "#0b1020"
BG_SECONDARY = "#0f1528"
ACCENT_CYAN = "#6ee7ff"
ACCENT_CYAN_GLOW = (110, 231, 255, 80)
TEXT_PRIMARY = "#f0f4ff"
SURFACE_PRIMARY = "#151d38"

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

def draw_rally_car_silhouette(draw, x, y, scale, color):
    """Draw a simplified rally car silhouette from side angle."""
    # Car body - rally car shape (hatchback silhouette)
    body_points = [
        (x - 100*scale, y + 20*scale),  # Front bottom
        (x - 95*scale, y - 20*scale),   # Front hood
        (x - 60*scale, y - 30*scale),   # Hood top
        (x - 20*scale, y - 45*scale),   # Windshield front
        (x + 10*scale, y - 50*scale),   # Roof front
        (x + 50*scale, y - 50*scale),   # Roof rear
        (x + 70*scale, y - 35*scale),   # Rear window slope
        (x + 90*scale, y - 15*scale),   # Trunk
        (x + 100*scale, y + 10*scale),  # Rear
        (x + 100*scale, y + 25*scale),  # Rear bottom
        (x - 100*scale, y + 25*scale),  # Front bottom
    ]
    draw.polygon(body_points, fill=color)
    
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
    
    # Draw atmospheric dust/mud spray effect (circles with low opacity)
    for _ in range(50):
        x = int(os.urandom(2).hex(), 16) % width
        y = int(os.urandom(2).hex(), 16) % height
        size = int(os.urandom(1).hex(), 16) % 80 + 20
        alpha = int(os.urandom(1).hex(), 16) % 30 + 10
        draw.ellipse([x-size, y-size, x+size, y+size], fill=(139, 90, 43, alpha))
    
    # Draw rally car in center-right
    draw_rally_car_silhouette(draw, width*0.55, height*0.55, 3.0, SURFACE_PRIMARY)
    
    # Cyan accent streaks (speed lines)
    for i in range(5):
        y_start = 300 + i * 100
        draw.line([(100, y_start), (600, y_start - 50)], fill=ACCENT_CYAN_GLOW, width=2)
    
    # Atmospheric glow in center
    for r in range(200, 50, -20):
        alpha = int(20 * (200 - r) / 150)
        draw.ellipse([width//2-r, height//2-r, width//2+r, height//2+r], 
                     outline=(110, 231, 255, alpha), width=3)
    
    # Ground/dust texture layer
    for y in range(height - 200, height):
        for x in range(0, width, 40):
            alpha = int(os.urandom(1).hex(), 16) % 20 + 5
            draw.point((x + int(os.urandom(1).hex(), 16) % 40, y), fill=(139, 90, 43, alpha))
    
    # Apply slight blur for atmosphere
    img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
    
    # Save
    output_path = "/home/antforce/compoundvr-project/public/images/games/dirt-rally-vr-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    print(f"Hero image saved to: {output_path}")
    print(f"Size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()