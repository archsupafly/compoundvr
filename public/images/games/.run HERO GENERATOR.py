#!/usr/bin/env python3
from PIL import Image, ImageDraw
import math
import os
import random

# Brand colors
BG_PRIMARY = "#0b1020"
BG_SECONDARY = "#151d38"
BG_DARK = "#080c18"
ACCENT_CYAN = "#6ee7ff"

# Horror colors
CARNIVAL_RED = "#8b0000"
CLOWN_ORANGE = "#ff6b35"

def create_gradient_background(width, height, color1, color2):
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
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

def draw_clown_figure(draw, x, y, scale=1.0, facing_right=True):
    if not facing_right:
        x = x - 40 * scale
    draw.ellipse([x - 30 * scale, y - 60 * scale, x + 30 * scale, y + 40 * scale], fill="#2a2a35")
    head_y = y - 50 * scale
    draw.ellipse([x - 25 * scale, head_y - 30 * scale, x + 25 * scale, head_y + 30 * scale], fill="#1a1a20")
    draw.ellipse([x - 12 * scale, head_y - 8 * scale, x - 6 * scale, head_y - 2 * scale], fill=CLOWN_ORANGE)
    draw.ellipse([x + 6 * scale, head_y - 8 * scale, x + 12 * scale, head_y - 2 * scale], fill=CLOWN_ORANGE)

def draw_tunnel(draw, x, y, width, height):
    for d in range(8, -1, -1):
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

def draw_wendigo(draw, x, y, scale=0.8):
    color = "#0a0a0f"
    draw.polygon([(x - 15 * scale, y), (x - 20 * scale, y + 60 * scale), (x - 10 * scale, y + 80 * scale), (x + 10 * scale, y + 80 * scale), (x + 20 * scale, y + 60 * scale), (x + 15 * scale, y)], fill=color)
    draw.ellipse([x - 12 * scale, y - 35 * scale, x + 12 * scale, y - 5 * scale], fill=color)
    draw.line([x - 8 * scale, y - 30 * scale, x - 25 * scale, y - 60 * scale], fill=color, width=2)
    draw.line([x + 8 * scale, y - 30 * scale, x + 25 * scale, y - 60 * scale], fill=color, width=2)
    draw.ellipse([x - 5 * scale, y - 22 * scale, x - 2 * scale, y - 18 * scale], fill="#ffffff")
    draw.ellipse([x + 2 * scale, y - 22 * scale, x + 5 * scale, y - 18 * scale], fill="#ffffff")

def draw_fog(img, width, height):
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

width, height = 1920, 1080
img = create_gradient_background(width, height, "#080c18", "#0f1528")
img = img.convert('RGBA')
draw = ImageDraw.Draw(img)

draw_mine_track(draw, width, height)
draw_tunnel(draw, width * 0.5, height * 0.15, 400, height * 0.35)
draw_clown_figure(draw, width * 0.25, height * 0.55, scale=1.2, facing_right=True)
draw_clown_figure(draw, width * 0.78, height * 0.45, scale=0.8, facing_right=False)
draw_wendigo(draw, width * 0.45, height * 0.25, scale=0.6)
draw_wendigo(draw, width * 0.55, height * 0.22, scale=0.5)
random.seed(42)
draw.ellipse([width * 0.15 - 8, height * 0.35 - 8, width * 0.15 + 8, height * 0.35 + 8], fill=CLOWN_ORANGE)
draw.ellipse([width * 0.85 - 8, height * 0.3 - 8, width * 0.85 + 8, height * 0.3 + 8], fill=CLOWN_ORANGE)

img = draw_fog(img, width, height)
img = draw_vignette(img, width, height)

img_rgb = img.convert('RGB')
output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
img_rgb.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)

print(f"Generated: {output_path}")
print(f"Size: {width}x{height}")
print(f"Bytes: {os.path.getsize(output_path)}")