#!/usr/bin/env python3
"""
Generate a hero image for Castlevania VR (3dSen VR voxel transformation)
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Subject: Castlevania (1986) NES classic reimagined in VR with 3dSen voxel transformation
Style: Gothic horror, Dracula's castle, atmospheric dark corridors, torches, whip combat
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os
import sys

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

# Castlevania gothic colors
CASTLE_BLACK = "#0a0a0a"    # Deep black
CASTLE_STONE = "#2a2a3a"    # Dark stone grey
CASTLE_BLUE = "#1a1a2e"     # Midnight blue
TORCH_ORANGE = "#ff6b35"    # Warm torch orange
TORCH_YELLOW = "#ffc857"    # Torch flame yellow
BLOOD_RED = "#8b0000"      # Deep blood red
BLOOD_CRIMSON = "#dc143c"   # Brighter crimson

def create_gradient_background(width, height, color1, color2):
    """Create a vertical gradient background."""
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

def draw_castle_silhouette(draw, width, height):
    """Draw Dracula's castle silhouette in the background."""
    # Distant castle towers and spires (gothic architecture)
    castle_base_y = height * 0.6
    
    # Main castle body - large central tower
    points = [
        (width * 0.35, castle_base_y),
        (width * 0.35, castle_base_y - 120),
        (width * 0.38, castle_base_y - 150),  # Left spire
        (width * 0.40, castle_base_y - 120),
        (width * 0.42, castle_base_y - 180),  # Tall central spire
        (width * 0.44, castle_base_y - 120),
        (width * 0.45, castle_base_y - 200),  # Highest spire (Dracula's tower)
        (width * 0.46, castle_base_y - 120),
        (width * 0.48, castle_base_y - 160),  # Right spire
        (width * 0.50, castle_base_y - 120),
        (width * 0.55, castle_base_y),  # End of main castle
    ]
    
    draw.polygon(points, fill=CASTLE_STONE)
    
    # Left tower
    left_tower = [
        (width * 0.22, castle_base_y),
        (width * 0.22, castle_base_y - 80),
        (width * 0.25, castle_base_y - 110),
        (width * 0.28, castle_base_y - 80),
        (width * 0.28, castle_base_y),
    ]
    draw.polygon(left_tower, fill=CASTLE_STONE)
    
    # Right tower
    right_tower = [
        (width * 0.62, castle_base_y),
        (width * 0.62, castle_base_y - 90),
        (width * 0.65, castle_base_y - 130),
        (width * 0.68, castle_base_y - 90),
        (width * 0.68, castle_base_y),
    ]
    draw.polygon(right_tower, fill=CASTLE_STONE)
    
    # Add window lights (glowing windows in castle)
    window_positions = [
        (width * 0.40, castle_base_y - 60, 6, 8),
        (width * 0.44, castle_base_y - 50, 5, 7),
        (width * 0.48, castle_base_y - 70, 6, 8),
        (width * 0.25, castle_base_y - 40, 4, 6),
        (width * 0.65, castle_base_y - 50, 5, 6),
    ]
    for wx, wy, ww, wh in window_positions:
        draw.rectangle([wx, wy, wx + ww, wy + wh], fill=TORCH_YELLOW)

def draw_voxel_diorama_layer(draw, x, y, width, height, depth_offset=0):
    """Draw a layer representing 3dSen VR's voxel diorama effect."""
    # This simulates the 2D-to-3D voxel transformation
    # Each "layer" represents a depth slice
    
    # Stone wall blocks (voxel-style)
    block_size = 20
    for bx in range(0, int(width), block_size):
        for by in range(0, int(height), block_size):
            # Alternate brick pattern
            offset_x = (by // block_size) % 2 * (block_size // 2)
            brick_x = x + bx + offset_x + depth_offset * 3
            brick_y = y + by
            
            # Depth-based color variation (darker as it goes back)
            depth_factor = 1 - (depth_offset / 20)
            base_color = int(42 * depth_factor)
            fill_color = (base_color, base_color + 10, base_color + 30)
            
            draw.rectangle(
                [brick_x, brick_y, brick_x + block_size - 2, brick_y + block_size - 2],
                fill=fill_color, outline=(base_color // 2, base_color // 2, base_color // 2)
            )

def draw_torch(draw, x, y, flame_frame=0):
    """Draw a flaming torch with flicker effect."""
    # Torch holder
    draw.rectangle([x - 4, y, x + 4, y + 40], fill="#4a3728")  # Wooden handle
    
    # Flame (multiple layers)
    import random
    random.seed(int(x * 100 + flame_frame))
    
    # Outer flame glow
    for i in range(15):
        offset_y = random.randint(-25, -15)
        offset_x = random.randint(-12, 12)
        radius = random.randint(15, 25)
        alpha = random.randint(40, 80)
        draw.ellipse(
            [x + offset_x - radius, y + offset_y - radius,
             x + offset_x + radius, y + offset_y + radius],
            fill=(255, 107, 53, alpha)
        )
    
    # Flame core (yellow/white)
    flame_points = [
        (x - 10, y),
        (x, y - 30 - random.randint(0, 5)),
        (x + 10, y),
    ]
    draw.polygon(flame_points, fill=TORCH_YELLOW)
    
    # Inner bright core
    inner_points = [
        (x - 5, y - 5),
        (x, y - 20 - random.randint(0, 8)),
        (x + 5, y - 5),
    ]
    draw.polygon(inner_points, fill="#ffffff")

def draw_gothic_archway(draw, x, y, width, height, depth=5):
    """Draw a gothic archway with depth layers for 3D effect."""
    # Draw multiple layers for depth (voxel diorama style)
    for d in range(depth, -1, -1):
        offset = d * 8
        alpha_factor = 1 - (d / depth) * 0.5
        
        # Gothic pointed arch shape
        arch_points = [
            (x - width/2 + offset, y + height),  # Bottom left
            (x - width/2 + offset, y + height * 0.3 + offset/2),  # Left side
            (x - width/4 + offset, y + offset/2),  # Left arch curve
            (x, y - height * 0.15 + offset/3),  # Arch peak
            (x + width/4 - offset, y + offset/2),  # Right arch curve
            (x + width/2 - offset, y + height * 0.3 + offset/2),  # Right side
            (x + width/2 - offset, y + height),  # Bottom right
        ]
        
        stone_color = (
            int(45 * alpha_factor),
            int(42 * alpha_factor),
            int(58 * alpha_factor)
        )
        draw.polygon(arch_points, fill=stone_color, outline=(30, 28, 45))

def draw_vampire_silhouette(draw, x, y, scale=0.8):
    """Draw a mysterious vampire/skeleton silhouette."""
    # Cape flowing
    cape_points = [
        (x - 30 * scale, y + 50 * scale),
        (x - 40 * scale, y + 100 * scale),
        (x - 35 * scale, y + 120 * scale),
        (x + 10 * scale, y + 120 * scale),
        (x + 15 * scale, y + 100 * scale),
        (x + 5 * scale, y + 50 * scale),
    ]
    draw.polygon(cape_points, fill="#1a0a0a")
    
    # Body
    draw.rectangle([x - 20 * scale, y, x + 20 * scale, y + 50 * scale], fill="#0a0a0a")
    
    # Head
    draw.ellipse([x - 15 * scale, y - 20 * scale, x + 15 * scale, y + 10 * scale], fill="#0a0a0a")
    
    # Glowing red eyes
    draw.ellipse([x - 8 * scale, y - 10 * scale, x - 4 * scale, y - 6 * scale], fill=BLOOD_CRIMSON)
    draw.ellipse([x + 4 * scale, y - 10 * scale, x + 8 * scale, y - 6 * scale], fill=BLOOD_CRIMSON)

def draw_whip_trail(draw, x1, y1, x2, y2, segments=12):
    """Draw a whip attack trail."""
    import random
    points = []
    for i in range(segments + 1):
        t = i / segments
        px = x1 + (x2 - x1) * t
        py = y1 + (y2 - y1) * t + math.sin(t * math.pi * 3) * 20
        points.append((px, py))
    
    # Draw whip segments with tapering
    for i in range(len(points) - 1):
        width = max(1, 4 - i // 3)
        draw.line([points[i], points[i + 1]], fill="#c0c0c0", width=width)

def draw_3dsen_voxel_effect(img, width, height):
    """Add distinctive 3dSen VR voxel transformation overlay."""
    # Create overlay for voxel edge effects
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Voxel grid lines (subtle)
    grid_spacing = 30
    for x in range(0, width, grid_spacing):
        overlay_draw.line([(x, 0), (x, height)], fill=(110, 231, 255, 10), width=1)
    for y in range(0, height, grid_spacing):
        overlay_draw.line([(0, y), (width, y)], fill=(110, 231, 255, 10), width=1)
    
    return Image.alpha_composite(img, overlay)

def draw_title_text(draw, width, height):
    """Draw the game title overlay."""
    # Try to use a gothic/serif font
    font_path = None
    font_paths_to_try = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf",
    ]
    
    for fp in font_paths_to_try:
        if os.path.exists(fp):
            font_path = fp
            break
    
    # Title fonts
    if font_path:
        title_font = ImageFont.truetype(font_path, size=72)
        subtitle_font = ImageFont.truetype(font_path, size=36)
    else:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Main title: "CASTLEVANIA"
    # Position in upper-left with good contrast area
    title_x = 80
    title_y = 80
    
    # Draw shadow/glow effect
    for offset in range(5, 0, -1):
        alpha = 255 - offset * 40
        draw.text(
            (title_x + offset, title_y + offset),
            "CASTLEVANIA",
            font=title_font,
            fill=(139, 0, 0, alpha)  # Blood red shadow
        )
    
    # Main title in gothic white/gold
    draw.text((title_x, title_y), "CASTLEVANIA", font=title_font, fill="#f0e68c")
    
    # Subtitle: "in VR"
    subtitle_y = title_y + 95
    subtitle_x = title_x + 50
    
    # Glow effect for subtitle
    for offset in range(3, 0, -1):
        alpha = 200 - offset * 50
        draw.text(
            (subtitle_x + offset, subtitle_y + offset),
            "in VR",
            font=subtitle_font,
            fill=(110, 231, 255, alpha)  # Cyan glow
        )
    
    draw.text((subtitle_x, subtitle_y), "in VR", font=subtitle_font, fill=ACCENT_CYAN)
    
    # Method badge: "3dSen VR Diorama"
    badge_x = width - 200
    badge_y = height - 60
    
    # Badge background
    draw.rounded_rectangle(
        [badge_x, badge_y, badge_x + 180, badge_y + 40],
        radius=10, fill=BG_DARK, outline=ACCENT_CYAN
    )
    
    # Badge text
    if font_path:
        badge_font = ImageFont.truetype(font_path, size=16)
    else:
        badge_font = ImageFont.load_default()
    
    draw.text((badge_x + 10, badge_y + 10), "3dSen VR Diorama", font=badge_font, fill=ACCENT_CYAN)

def draw_atmospheric_effects(img, width, height):
    """Add atmospheric fog and particle effects."""
    # Create overlay for effects
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    import random
    random.seed(666)  # Castlevania seed! 🧛
    
    # Floating dust/mist particles
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 3)
        
        # Mix of torch-glow particles and cold blue mist
        if random.random() > 0.6:
            # Warm torch ember
            color = (255, 200, 100, random.randint(20, 60))
        else:
            # Cold mist
            color = (110, 231, 255, random.randint(10, 30))
        
        draw.ellipse([x, y, x + size, y + size], fill=color)
    
    # Ground fog
    fog_height = 150
    for y in range(height - fog_height, height):
        alpha = int(40 * ((y - (height - fog_height)) / fog_height))
        draw.line([(0, y), (width, y)], fill=(11, 16, 32, alpha))
    
    # Add vignette effect
    for i in range(100):
        alpha = int(i * 0.5)
        # Left edge
        draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
        # Right edge
        draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
        # Top edge
        draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
        # Bottom edge
        draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))
    
    return Image.alpha_composite(img, overlay)

def create_hero_image():
    """Create the Castlevania VR hero image."""
    width, height = 1200, 630  # OG image dimensions
    
    # Create base with gradient (dark gothic atmosphere)
    img = create_gradient_background(width, height, BG_DARK, CASTLE_BLUE)
    img = img.convert('RGBA')
    
    draw = ImageDraw.Draw(img)
    
    # Draw distant castle silhouette in background
    draw_castle_silhouette(draw, width, height)
    
    # Draw gothic archway (3D depth layers for voxel effect)
    draw_gothic_archway(draw, width * 0.65, height * 0.1, 300, height * 0.7, depth=6)
    
    # Add torches with flame effects
    draw_torch(draw, 100, height * 0.35)
    draw_torch(draw, 250, height * 0.40)
    draw_torch(draw, width - 150, height * 0.30, flame_frame=1)
    draw_torch(draw, width - 80, height * 0.45, flame_frame=2)
    
    # Draw vampire silhouette in archway
    draw_vampire_silhouette(draw, width * 0.65, height * 0.35, scale=0.7)
    
    # Draw whip attack trail (Simon Belmont's whip)
    draw_whip_trail(draw, 150, height * 0.55, 300, height * 0.45)
    
    # Add title and text
    draw_title_text(draw, width, height)
    
    # Add atmospheric effects
    img = draw_atmospheric_effects(img, width, height)
    
    # Add 3dSen VR voxel grid effect
    img = draw_3dsen_voxel_effect(img, width, height)
    
    # Convert to RGB for final output
    img_rgb = img.convert('RGB')
    
    return img_rgb

def main():
    output_path = "/home/antforce/compoundvr-project/public/images/games/castlevania-vr-hero.jpg"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print("Generating Castlevania VR hero image...")
    print("  Theme: Castlevania (1986) NES → 3dSen VR voxel diorama")
    print("  Style: Gothic horror, Dracula's castle, atmospheric corridors")
    print(f"  Output: {output_path}")
    
    img = create_hero_image()
    
    # Save with web-optimized JPEG settings
    img.save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    
    print(f"\n✓ Hero image saved successfully!")
    print(f"  Dimensions: {img.size[0]}x{img.size[1]}")
    print(f"  File size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()