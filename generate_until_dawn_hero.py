#!/usr/bin/env python3
"""
Generate Until Dawn: Rush of Blood hero image procedurally
Using PIL - no external API required
"""

from PIL import Image, ImageDraw
import math
import os
import random

def main():
    # Output path
    output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Dimensions: 1920x1080 (16:9)
    width, height = 1920, 1080
    
    # Horror colors
    CLOWN_ORANGE = "#ff6b35"
    
    print("Generating Until Dawn: Rush of Blood hero image...")
    print(f"  Dimensions: {width}x{height}")
    
    # Create gradient background (dark navy to slightly lighter)
    img = Image.new('RGB', (width, height), "#080c18")
    draw = ImageDraw.Draw(img)
    
    # Vertical gradient
    r1, g1, b1 = 8, 12, 24  # #080c18
    r2, g2, b2 = 15, 21, 40  # #0f1528
    for y in range(height):
        ratio = y / height
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Convert to RGBA for effects
    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)
    
    # Draw mine cart track (perspective leading into darkness)
    vanish_x = width * 0.5
    for i in range(40):
        progress = i / 40
        y_start = height * (0.95 - progress * 0.6)
        y_end = height * (0.98 - progress * 0.6)
        track_width = 250 * (1 - progress * 0.8)
        x_left = vanish_x - track_width
        x_right = vanish_x + track_width
        darkness = 30 + int(20 * progress)
        draw.rectangle([x_left, y_start, x_right, y_end], fill=(darkness, darkness, darkness + 10))
    
    # Draw tunnel entrance (dark mine shaft)
    tunnel_x = width * 0.5
    tunnel_y = int(height * 0.15)
    tunnel_w = 400
    tunnel_h = int(height * 0.35)
    
    for d in range(8, -1, -1):
        offset = d * 5
        brightness = 15 + d * 3
        arch_points = [
            (tunnel_x - tunnel_w/2 + offset, tunnel_y + tunnel_h),
            (tunnel_x - tunnel_w/2 + offset, tunnel_y + int(tunnel_h * 0.4)),
            (tunnel_x - tunnel_w/4 + offset * 0.5, tunnel_y + int(offset * 0.3)),
            (tunnel_x, tunnel_y - int(tunnel_h * 0.1) + int(offset * 0.2)),
            (tunnel_x + tunnel_w/4 - offset * 0.5, tunnel_y + int(offset * 0.3)),
            (tunnel_x + tunnel_w/2 - offset, tunnel_y + int(tunnel_h * 0.4)),
            (tunnel_x + tunnel_w/2 - offset, tunnel_y + tunnel_h),
        ]
        draw.polygon(arch_points, fill=(brightness, brightness, brightness + 5))
    
    # Red emergency light glow inside tunnel
    draw.ellipse([tunnel_x - 30, tunnel_y - 40, tunnel_x + 30, tunnel_y], fill=(60, 0, 0))
    
    # Draw menacing clown figure (silhouette with glowing eyes)
    def draw_clown(draw, x, y, scale, facing_right):
        if not facing_right:
            x = x - 40 * scale
        # Body
        draw.ellipse([x - 30 * scale, y - 60 * scale, x + 30 * scale, y + 40 * scale], fill="#2a2a35")
        # Head
        head_y = y - 50 * scale
        draw.ellipse([x - 25 * scale, head_y - 30 * scale, x + 25 * scale, head_y + 30 * scale], fill="#1a1a20")
        # Glowing orange eyes
        draw.ellipse([x - 12 * scale, head_y - 8 * scale, x - 6 * scale, head_y - 2 * scale], fill=CLOWN_ORANGE)
        draw.ellipse([x + 6 * scale, head_y - 8 * scale, x + 12 * scale, head_y - 2 * scale], fill=CLOWN_ORANGE)
        # Creepy smile arc
        draw.arc([x - 15 * scale, head_y + 3 * scale, x + 15 * scale, head_y + 18 * scale], 0, 180, fill=CLOWN_ORANGE, width=2)
    
    # Clown on left (larger, closer)
    draw_clown(draw, width * 0.25, height * 0.55, 1.2, True)
    # Clown on right (smaller, further)
    draw_clown(draw, width * 0.78, height * 0.45, 0.8, False)
    
    # Draw wendigo silhouettes in far background (inside tunnel)
    def draw_wendigo(draw, x, y, scale):
        color = "#0a0a0f"
        # Emaciated body
        draw.polygon([
            (x - 15 * scale, y),
            (x - 20 * scale, y + 60 * scale),
            (x - 10 * scale, y + 80 * scale),
            (x + 10 * scale, y + 80 * scale),
            (x + 20 * scale, y + 60 * scale),
            (x + 15 * scale, y),
        ], fill=color)
        # Elongated head with antlers
        draw.ellipse([x - 12 * scale, y - 35 * scale, x + 12 * scale, y - 5 * scale], fill=color)
        draw.line([x - 8 * scale, y - 30 * scale, x - 25 * scale, y - 60 * scale], fill=color, width=2)
        draw.line([x + 8 * scale, y - 30 * scale, x + 25 * scale, y - 60 * scale], fill=color, width=2)
        # Ghostly white eyes
        draw.ellipse([x - 5 * scale, y - 22 * scale, x - 2 * scale, y - 18 * scale], fill="#ffffff")
        draw.ellipse([x + 2 * scale, y - 22 * scale, x + 5 * scale, y - 18 * scale], fill="#ffffff")
    
    draw_wendigo(draw, width * 0.45, height * 0.25, 0.6)
    draw_wendigo(draw, width * 0.55, height * 0.22, 0.5)
    
    # Flickering carnival lights
    random.seed(42)
    lights = [(width * 0.15, height * 0.35), (width * 0.85, height * 0.3), (width * 0.4, height * 0.25)]
    for lx, ly in lights:
        # Light source
        draw.ellipse([lx - 10, ly - 10, lx + 10, ly + 10], fill=CLOWN_ORANGE)
        # Glow
        for r in range(80, 10, -15):
            intensity = random.randint(200, 250)
            draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=(intensity, int(intensity * 0.4), 0))
    
    # Atmospheric fog
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    fog_draw = ImageDraw.Draw(overlay)
    for y in range(int(height * 0.7), height):
        fog_density = (y - height * 0.7) / (height * 0.3)
        for x in range(0, width, 3):
            if random.random() < fog_density * 0.25:
                alpha = int(25 + random.randint(0, 35) * fog_density)
                fog_draw.point((x, y), fill=(100, 100, 120, alpha))
    img = Image.alpha_composite(img, overlay)
    
    # Vignette effect
    overlay2 = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    vig_draw = ImageDraw.Draw(overlay2)
    for i in range(120):
        alpha = int(i * 1.5)
        vig_draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
        vig_draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
        vig_draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
        vig_draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))
    img = Image.alpha_composite(img, overlay2)
    
    # Convert to RGB and save
    img_rgb = img.convert('RGB')
    img_rgb.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    
    file_size = os.path.getsize(output_path)
    print(f"SUCCESS: Generated hero image")
    print(f"  Output: {output_path}")
    print(f"  Dimensions: {width}x{height}")
    print(f"  File size: {file_size / 1024:.1f} KB")

if __name__ == "__main__":
    main()