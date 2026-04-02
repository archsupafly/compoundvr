#!/usr/bin/env python3
"""
Generate a hero image for Until Dawn: Rush of Blood (PSVR horror rail shooter)
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os
import sys
import random

# CompoundVR brand colors
BG_PRIMARY = "#0b1020"
BG_SECONDARY = "#151d38"
BG_DARK = "#080c18"
ACCENT_CYAN = "#6ee7ff"
ACCENT_PURPLE = "#8b5cf6"

# Horror colors
CARNIVAL_RED = "#8b0000"
CARNIVAL_CRIMSON = "#dc143c"
CLOWN_ORANGE = "#ff6b35"
CLOWN_YELLOW = "#ffc857"
MINE_BLACK = "#0a0a0a"
MINE_STONE = "#2a2a3a"
MIST_BLUE = "#1a1a2e"

def create_gradient_background(width, height, color1, color2, horizontal=False):
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    
    if horizontal:
        for x in range(width):
            ratio = x / width
            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)
            draw.line([(x, 0), (x, height)], fill=(r, g, b))
    else:
        for y in range(height):
            ratio = y / height
            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_mine_track(draw, width, height):
    vanish_y = height * 0.3
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
    
    for side in [-1, 1]:
        for i in range(50):
            progress = i / 50
            y = height * (0.95 - progress * 0.65)
            track_width = 250 * (1 - progress * 0.8)
            x = vanish_x + side * track_width
            rail_brightness = 60 + int(30 * (1 - progress))
            draw.ellipse([x - 3, y - 2, x + 3, y + 2], fill=(rail_brightness, rail_brightness - 10, rail_brightness + 20))

def draw_clown_figure(draw, x, y, scale=1.0, facing_right=True):
    body_width = 40 * scale
    body_height = 80 * scale
    
    if not facing_right:
        x = x - body_width
    
    draw.ellipse([x - 30 * scale, y - 60 * scale, x + 30 * scale, y + 40 * scale], fill="#2a2a35")
    head_y = y - 50 * scale
    draw.ellipse([x - 25 * scale, head_y - 30 * scale, x + 25 * scale, head_y + 30 * scale], fill="#1a1a20")
    
    eye_glow = CLOWN_ORANGE
    draw.ellipse([x - 12 * scale, head_y - 8 * scale, x - 6 * scale, head_y - 2 * scale], fill=eye_glow)
    draw.ellipse([x + 6 * scale, head_y - 8 * scale, x + 12 * scale, head_y - 2 * scale], fill=eye_glow)
    
    smile_y = head_y + 8 * scale
    draw.arc([x - 15 * scale, smile_y - 5 * scale, x + 15 * scale, smile_y + 15 * scale], 0, 180, fill=CLOWN_ORANGE, width=2)

def draw_tunnel_entrance(draw, x, y, width, height, depth=8):
    for d in range(depth, -1, -1):
        offset = d * 5
        brightness = 15 + d * 3
        
        arch_points = [
            (x - width/2 + offset, y + height),
            (x - width/2 + offset, y + height * 0.4),
            (x - width/4 + offset * 0.5, y + offset * 0.3),
            (x, y - height * 0.1 + offset * 0.2),
            (x + width/4 - offset * 0.5, y + offset * 0.3),
            (x + width/2 - offset, y + height * 0.4),
            (x + width/2 - offset, y + height),
        ]
        
        draw.polygon(arch_points, fill=(brightness, brightness, brightness + 5))
    
    draw.ellipse([x - 20, y - 30, x + 20, y + 10], fill=(60, 0, 0))
    draw.rectangle([x - width/2 + 10, y, x - width/2 + 15, y + height * 0.6], fill="#3a3020")
    draw.rectangle([x + width/2 - 15, y, x + width/2 - 10, y + height * 0.6], fill="#3a3020")

def draw_flickering_light(draw, x, y, frame=0):
    random.seed(int(x * 100 + frame))
    draw.ellipse([x - 8, y - 8, x + 8, y + 8], fill=CLOWN_ORANGE)
    
    for r in range(80, 10, -10):
        alpha = int(50 - r * 0.5)
        intensity = random.randint(180, 220)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(intensity, int(intensity * 0.4), 0))
    
    for _ in range(5):
        angle = random.uniform(0, math.pi)
        ray_len = random.randint(50, 100)
        end_x = x + math.cos(angle) * ray_len
        end_y = y - abs(math.sin(angle)) * ray_len * 0.5
        draw.line([x, y, end_x, end_y], fill=(255, 150, 50, 100), width=1)

def draw_wendigo_silhouette(draw, x, y, scale=0.8):
    color = "#0a0a0f"
    
    draw.polygon([
        (x - 15 * scale, y),
        (x - 20 * scale, y + 60 * scale),
        (x - 10 * scale, y + 80 * scale),
        (x + 10 * scale, y + 80 * scale),
        (x + 20 * scale, y + 60 * scale),
        (x + 15 * scale, y),
    ], fill=color)
    
    draw.ellipse([x - 12 * scale, y - 35 * scale, x + 12 * scale, y - 5 * scale], fill=color)
    
    draw.line([x - 8 * scale, y - 30 * scale, x - 25 * scale, y - 60 * scale], fill=color, width=2)
    draw.line([x + 8 * scale, y - 30 * scale, x + 25 * scale, y - 60 * scale], fill=color, width=2)
    draw.line([x - 20 * scale, y - 55 * scale, x - 28 * scale, y - 52 * scale], fill=color, width=1)
    draw.line([x + 20 * scale, y - 55 * scale, x + 28 * scale, y - 52 * scale], fill=color, width=1)
    
    draw.ellipse([x - 5 * scale, y - 22 * scale, x - 2 * scale, y - 18 * scale], fill="#ffffff")
    draw.ellipse([x + 2 * scale, y - 22 * scale, x + 5 * scale, y - 18 * scale], fill="#ffffff")

def draw_atmospheric_fog(img, width, height):
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    random.seed(42)
    
    for y in range(int(height * 0.7), height):
        fog_density = (y - height * 0.7) / (height * 0.3)
        for x in range(0, width, 2):
            if random.random() < fog_density * 0.3:
                alpha = int(30 + random.randint(0, 40) * fog_density)
                draw.point((x, y), fill=(100, 100, 120, alpha))
    
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, int(height * 0.8))
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        alpha = random.randint(20, 60)
        draw.ellipse([x, y, x + size, y + size], fill=(brightness, brightness - 30, brightness - 50, alpha))
    
    return Image.alpha_composite(img, overlay)

def draw_vignette(img, width, height):
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for i in range(120):
        alpha = int(i * 1.5)
        draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
        draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
        draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
        draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))
    
    return Image.alpha_composite(img, overlay)

def draw_carnival_signage(draw, width, height):
    sign_x = width * 0.15
    sign_y = height * 0.75
    
    draw.rectangle([sign_x - 2, sign_y, sign_x + 2, sign_y + 80], fill="#3a2510")
    
    sign_points = [
        (sign_x - 50, sign_y - 30),
        (sign_x + 60, sign_y - 40),
        (sign_x + 55, sign_y + 15),
        (sign_x - 55, sign_y + 20),
    ]
    draw.polygon(sign_points, fill="#4a3020")
    
    for i in range(3):
        line_y = sign_y - 15 + i * 12
        line_width = 30 - i * 5
        draw.rectangle([sign_x - line_width, line_y, sign_x + line_width, line_y + 4], fill="#2a1a10")

def create_horror_rays(img, width, height):
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    ray_source_x = width * 0.5
    ray_source_y = 0
    
    for i in range(8):
        angle_offset = (i - 4) * 0.08
        end_x = ray_source_x + math.tan(angle_offset) * height
        ray_width = 40 + abs(i - 4) * 15
        ray_points = [
            (ray_source_x - 5, ray_source_y),
            (ray_source_x + 5, ray_source_y),
            (end_x + ray_width, height),
            (end_x - ray_width, height),
        ]
        alpha = 8 + random.randint(0, 5)
        draw.polygon(ray_points, fill=(255, 200, 100, alpha))
    
    return Image.alpha_composite(img, overlay)

def main():
    width, height = 1920, 1080
    
    img = create_gradient_background(width, height, "#080c18", "#0f1528")
    img = img.convert('RGBA')
    
    draw = ImageDraw.Draw(img)
    
    draw_mine_track(draw, width, height)
    draw_tunnel_entrance(draw, width * 0.5, height * 0.15, 400, height * 0.35)
    draw_clown_figure(draw, width * 0.25, height * 0.55, scale=1.2, facing_right=True)
    draw_clown_figure(draw, width * 0.78, height * 0.45, scale=0.8, facing_right=False)
    draw_wendigo_silhouette(draw, width * 0.45, height * 0.25, scale=0.6)
    draw_wendigo_silhouette(draw, width * 0.55, height * 0.22, scale=0.5)
    draw_carnival_signage(draw, width, height)
    draw_flickering_light(draw, width * 0.15, height * 0.35, frame=0)
    draw_flickering_light(draw, width * 0.85, height * 0.3, frame=1)
    draw_flickering_light(draw, width * 0.4, height * 0.25, frame=2)
    
    img = draw_atmospheric_fog(img, width, height)
    img = draw_vignette(img, width, height)
    img = create_horror_rays(img, width, height)
    
    img_rgb = img.convert('RGB')
    
    output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img_rgb.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    
    print(f"SUCCESS: Generated Until Dawn: Rush of Blood hero image")
    print(f"Output: {output_path}")
    print(f"Dimensions: {width}x{height}")
    print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()