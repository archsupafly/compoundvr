#!/usr/bin/env python3
"""
Generate a hero image for Until Dawn: Rush of Blood (PSVR horror rail shooter)
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Subject: Until Dawn: Rush of Blood - on-rails horror carnival ride through nightmares
Style: Horror carnival, clowns, wendigos, dark mine tunnels, atmospheric terror
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os
import sys
import random

# Check for PIL availability
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

# CompoundVR brand colors
BG_PRIMARY = "#0b1020"      # Deep navy background
BG_SECONDARY = "#151d38"    # Slightly lighter navy
BG_DARK = "#080c18"         # Darker navy for shadows
ACCENT_CYAN = "#6ee7ff"     # Primary brand accent (cyan)
ACCENT_PURPLE = "#8b5cf6"   # Secondary accent
TEXT_PRIMARY = "#f0f4ff"     # Headlines
SURFACE_PRIMARY = "#1a2547" # Cards/elements

# Until Dawn: Rush of Blood horror colors
CARNIVAL_RED = "#8b0000"     # Deep blood red
CARNIVAL_CRIMSON = "#dc143c" # Brighter horror red
CLOWN_ORANGE = "#ff6b35"     # Eerie carnival orange
CLOWN_YELLOW = "#ffc857"     # Sickly yellow
MINE_BLACK = "#0a0a0a"       # Deep mine black
MINE_STONE = "#2a2a3a"       # Dark stone grey
MIST_BLUE = "#1a1a2e"       # Cold misty blue
FOG_WHITE = "#c0c0c0"       # Ghostly fog

def create_gradient_background(width, height, color1, color2, horizontal=False):
    """Create a gradient background."""
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
    """Draw a mine cart track leading into darkness."""
    # Track perspective - starts wide at bottom, narrows toward center-top
    vanish_y = height * 0.3
    vanish_x = width * 0.5
    
    # Track planks
    for i in range(40):
        progress = i / 40
        y_start = height * (0.95 - progress * 0.6)
        y_end = height * (0.98 - progress * 0.6)
        
        # Track width narrows with perspective
        track_width = 250 * (1 - progress * 0.8)
        
        x_left = vanish_x - track_width
        x_right = vanish_x + track_width
        
        # Track planks
        darkness = 30 + int(20 * progress)
        draw.rectangle(
            [x_left, y_start, x_right, y_end],
            fill=(darkness, darkness, darkness + 10)
        )
    
    # Rails (metal strips)
    for side in [-1, 1]:
        for i in range(50):
            progress = i / 50
            y = height * (0.95 - progress * 0.65)
            track_width = 250 * (1 - progress * 0.8)
            x = vanish_x + side * track_width
            
            rail_brightness = 60 + int(30 * (1 - progress))
            draw.ellipse(
                [x - 3, y - 2, x + 3, y + 2],
                fill=(rail_brightness, rail_brightness - 10, rail_brightness + 20)
            )

def draw_clown_figure(draw, x, y, scale=1.0, facing_right=True):
    """Draw a menacing clown silhouette emerging from darkness."""
    # Clown body - hunched menacing form
    body_width = 40 * scale
    body_height = 80 * scale
    
    if not facing_right:
        x = x - body_width
    
    # White/cream clown suit (illuminated by eerie glow)
    draw.ellipse(
        [x - 30 * scale, y - 60 * scale, x + 30 * scale, y + 40 * scale],
        fill="#2a2a35"  # Dark grey, barely visible
    )
    
    # Oversized clown head
    head_y = y - 50 * scale
    draw.ellipse(
        [x - 25 * scale, head_y - 30 * scale, x + 25 * scale, head_y + 30 * scale],
        fill="#1a1a20"  # Very dark
    )
    
    # Glowing eyes
    eye_glow = CLOWN_ORANGE
    draw.ellipse([x - 12 * scale, head_y - 8 * scale, x - 6 * scale, head_y - 2 * scale], fill=eye_glow)
    draw.ellipse([x + 6 * scale, head_y - 8 * scale, x + 12 * scale, head_y - 2 * scale], fill=eye_glow)
    
    # Creepy smile (just a curved line suggestion)
    smile_y = head_y + 8 * scale
    draw.arc(
        [x - 15 * scale, smile_y - 5 * scale, x + 15 * scale, smile_y + 15 * scale],
        0, 180, fill=CLOWN_ORANGE, width=2
    )

def draw_tunnel_entrance(draw, x, y, width, height, depth=8):
    """Draw a dark mine tunnel entrance."""
    # Multiple layers for depth
    for d in range(depth, -1, -1):
        offset = d * 5
        brightness = 15 + d * 3
        
        # Arch shape
        arch_points = [
            (x - width/2 + offset, y + height),  # Bottom left
            (x - width/2 + offset, y + height * 0.4),  # Left wall
            (x - width/4 + offset * 0.5, y + offset * 0.3),  # Left arch
            (x, y - height * 0.1 + offset * 0.2),  # Top center
            (x + width/4 - offset * 0.5, y + offset * 0.3),  # Right arch
            (x + width/2 - offset, y + height * 0.4),  # Right wall
            (x + width/2 - offset, y + height),  # Bottom right
        ]
        
        draw.polygon(arch_points, fill=(brightness, brightness, brightness + 5))
    
    # Red emergency light glow inside
    draw.ellipse(
        [x - 20, y - 30, x + 20, y + 10],
        fill=(60, 0, 0)  # Deep red glow
    )
    
    # Sparse mine support beams
    draw.rectangle([x - width/2 + 10, y, x - width/2 + 15, y + height * 0.6], fill="#3a3020")
    draw.rectangle([x + width/2 - 15, y, x + width/2 - 10, y + height * 0.6], fill="#3a3020")

def draw_flickering_light(draw, x, y, frame=0):
    """Draw a flickering carnival/emergency light."""
    random.seed(int(x * 100 + frame))
    
    # Light source (bare bulb or fixture)
    draw.ellipse([x - 8, y - 8, x + 8, y + 8], fill=CLOWN_ORANGE)
    
    # Glow effect
    for r in range(80, 10, -10):
        alpha = int(50 - r * 0.5)
        intensity = random.randint(180, 220)
        draw.ellipse(
            [x - r, y - r, x + r, y + r],
            fill=(intensity, int(intensity * 0.4), 0)
        )
    
    # Light rays
    for _ in range(5):
        angle = random.uniform(0, math.pi)
        ray_len = random.randint(50, 100)
        end_x = x + math.cos(angle) * ray_len
        end_y = y - abs(math.sin(angle)) * ray_len * 0.5
        draw.line([x, y, end_x, end_y], fill=(255, 150, 50, 100), width=1)

def draw_wendigo_silhouette(draw, x, y, scale=0.8):
    """Draw a distant wendigo silhouette in the shadows."""
    # Wendigo is tall, emaciated, antlered
    color = "#0a0a0f"  # Near-black silhouette
    
    # Emaciated body
    draw.polygon([
        (x - 15 * scale, y),
        (x - 20 * scale, y + 60 * scale),
        (x - 10 * scale, y + 80 * scale),
        (x + 10 * scale, y + 80 * scale),
        (x + 20 * scale, y + 60 * scale),
        (x + 15 * scale, y),
    ], fill=color)
    
    # Elongated head
    draw.ellipse([x - 12 * scale, y - 35 * scale, x + 12 * scale, y - 5 * scale], fill=color)
    
    # Antlers
    draw.line([x - 8 * scale, y - 30 * scale, x - 25 * scale, y - 60 * scale], fill=color, width=2)
    draw.line([x + 8 * scale, y - 30 * scale, x + 25 * scale, y - 60 * scale], fill=color, width=2)
    # Antler branches
    draw.line([x - 20 * scale, y - 55 * scale, x - 28 * scale, y - 52 * scale], fill=color, width=1)
    draw.line([x + 20 * scale, y - 55 * scale, x + 28 * scale, y - 52 * scale], fill=color, width=1)
    
    # Ghostly white eyes
    draw.ellipse([x - 5 * scale, y - 22 * scale, x - 2 * scale, y - 18 * scale], fill="#ffffff")
    draw.ellipse([x + 2 * scale, y - 22 * scale, x + 5 * scale, y - 18 * scale], fill="#ffffff")

def draw_atmospheric_fog(img, width, height):
    """Add atmospheric fog and particles."""
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    random.seed(42)  # Consistent fog pattern
    
    # Ground fog
    for y in range(int(height * 0.7), height):
        fog_density = (y - height * 0.7) / (height * 0.3)
        for x in range(0, width, 2):
            if random.random() < fog_density * 0.3:
                alpha = int(30 + random.randint(0, 40) * fog_density)
                draw.point((x, y), fill=(100, 100, 120, alpha))
    
    # Floating dust motes in light beams
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, int(height * 0.8))
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        alpha = random.randint(20, 60)
        draw.ellipse([x, y, x + size, y + size], fill=(brightness, brightness - 30, brightness - 50, alpha))
    
    return Image.alpha_composite(img, overlay)

def draw_vignette(img, width, height):
    """Add dark vignette effect."""
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Vignette intensity
    for i in range(120):
        alpha = int(i * 1.5)
        # All edges
        draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
        draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
        draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
        draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))
    
    return Image.alpha_composite(img, overlay)

def draw_carnival_signage(draw, width, height):
    """Draw broken carnival signage elements."""
    # Tilted sign in foreground
    sign_x = width * 0.15
    sign_y = height * 0.75
    
    # Sign post
    draw.rectangle([sign_x - 2, sign_y, sign_x + 2, sign_y + 80], fill="#3a2510")
    
    # Sign board (tilted, broken)
    sign_points = [
        (sign_x - 50, sign_y - 30),
        (sign_x + 60, sign_y - 40),
        (sign_x + 55, sign_y + 15),
        (sign_x - 55, sign_y + 20),
    ]
    draw.polygon(sign_points, fill="#4a3020")
    
    # Faint text suggestion (just shapes, not readable)
    for i in range(3):
        line_y = sign_y - 15 + i * 12
        line_width = 30 - i * 5
        draw.rectangle([sign_x - line_width, line_y, sign_x + line_width, line_y + 4], fill="#2a1a10")

def create_horror_rays(img, width, height):
    """Add god rays piercing through the darkness."""
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Light source from top-center (moon/spotlight above)
    ray_source_x = width * 0.5
    ray_source_y = 0
    
    # Multiple rays fanning down
    for i in range(8):
        angle_offset = (i - 4) * 0.08
        end_x = ray_source_x + math.tan(angle_offset) * height
        
        # Ray polygon
        ray_width = 40 + abs(i - 4) * 15
        ray_points = [
            (ray_source_x - 5, ray_source_y),
            (ray_source_x + 5, ray_source_y),
            (end_x + ray_width, height),
            (end_x - ray_width, height),
        ]
        
        # Very subtle ray
        alpha = 8 + random.randint(0, 5)
        draw.polygon(ray_points, fill=(255, 200, 100, alpha))
    
    return Image.alpha_composite(img, overlay)

def main():
    """Create the Until Dawn: Rush of Blood hero image."""
    width, height = 1920, 1080  # 16:9 hero image
    
    # Create base with dark gradient (dark mine atmosphere)
    img = create_gradient_background(width, height, "#080c18", "#0f1528")
    img = img.convert('RGBA')
    
    draw = ImageDraw.Draw(img)
    
    # Draw mine track in center (perspective leading into darkness)
    draw_mine_track(draw, width, height)
    
    # Draw tunnel entrance in background
    draw_tunnel_entrance(draw, width * 0.5, height * 0.15, 400, height * 0.35)
    
    # Draw menacing clown on the left
    draw_clown_figure(draw, width * 0.25, height * 0.55, scale=1.2, facing_right=True)
    
    # Draw second clown silhouette on right (darker, further back)
    draw_clown_figure(draw, width * 0.78, height * 0.45, scale=0.8, facing_right=False)
    
    # Draw wendigo silhouette in far background (inside tunnel)
    draw_wendigo_silhouette(draw, width * 0.45, height * 0.25, scale=0.6)
    draw_wendigo_silhouette(draw, width * 0.55, height * 0.22, scale=0.5)
    
    # Draw broken carnival signage
    draw_carnival_signage(draw, width, height)
    
    # Add flickering lights
    draw_flickering_light(draw, width * 0.15, height * 0.35, frame=0)
    draw_flickering_light(draw, width * 0.85, height * 0.3, frame=1)
    draw_flickering_light(draw, width * 0.4, height * 0.25, frame=2)
    
    # Atmospheric effects
    img = draw_atmospheric_fog(img, width, height)
    img = draw_vignette(img, width, height)
    img = create_horror_rays(img, width, height)
    
    # Convert to RGB for final output
    img_rgb = img.convert('RGB')
    
    # Save
    output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img_rgb.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    
    print(f"Generated Until Dawn: Rush of Blood hero image")
    print(f"  Output: {output_path}")
    print(f"  Dimensions: {width}x{height}")
    print(f"  File size: {os.path.getsize(output_path) / 1024:.1f} KB")
    print(f"  Style: Horror carnival, on-rails mine cart perspective")

if __name__ == "__main__":
    main()