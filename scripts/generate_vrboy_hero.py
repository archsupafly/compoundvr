#!/usr/bin/env python3
"""
Generate VRboy Virtual Boy Emulator Hero Image
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Subject: Nintendo Virtual Boy (1995) reimagined for Meta Quest VR
Style: Retro-futuristic, moody, atmospheric, editorial - red monochrome meets modern VR

Usage:
    python generate_vrboy_hero.py
    python generate_vrboy_hero.py --output /path/to/output.jpg

Requirements:
    Pillow (PIL): pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os
import sys

# Check for PIL availability
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

# CompoundVR brand colors
BG_PRIMARY = "#0b1020"      # Deep navy background
BG_SECONDARY = "#151d38"    # Slightly lighter navy
ACCENT_CYAN = "#6ee7ff"     # Primary brand accent (cyan)
ACCENT_PURPLE = "#8b5cf6"   # Secondary accent
TEXT_PRIMARY = "#f0f4ff"     # Headlines
SURFACE_PRIMARY = "#1a2547" # Cards/elements

# Virtual Boy colors
VB_RED = "#ff0000"          # Iconic Virtual Boy red LED
VB_RED_GLOW = "#ff3333"     # Lighter red for glow effects
VB_RED_DARK = "#aa0000"     # Darker red
VB_SCREEN_BG = "#000000"    # Black screen background

def create_gradient_background(width, height, color1, color2):
    """Create a vertical gradient background."""
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
        g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
        b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_virtualboy_headset(draw, cx, cy, scale):
    """Draw the iconic Virtual Boy headset - red monochrome aesthetic."""
    # Main visor (large rectangular shape)
    visor_width = 280 * scale
    visor_height = 140 * scale
    
    # The distinct red/black Virtual Boy visor
    # Outer shell (dark surface)
    draw.rectangle(
        [cx - visor_width/2, cy - visor_height/2, 
         cx + visor_width/2, cy + visor_height/2],
        fill=BG_SECONDARY, outline=VB_RED, width=3
    )
    
    # Inner display area (black with red glow)
    display_margin = 15 * scale
    draw.rectangle(
        [cx - visor_width/2 + display_margin, cy - visor_height/2 + display_margin,
         cx + visor_width/2 - display_margin, cy + visor_height/2 - display_margin],
        fill="#000000", outline=VB_RED, width=2
    )
    
    # Add red scanline effect inside display
    for i in range(0, int(visor_height - 2*display_margin), 4):
        y_pos = cy - visor_height/2 + display_margin + i
        alpha = 30 + (i % 20)
        draw.line(
            [(cx - visor_width/2 + display_margin + 5, y_pos),
             (cx + visor_width/2 - display_margin - 5, y_pos)],
            fill=(255, 0, 0), width=1
        )
    
    # Left eye lens glow
    lens_cx_l = cx - visor_width/4
    lens_cy = cy
    lens_r = 35 * scale
    draw.ellipse(
        [lens_cx_l - lens_r, lens_cy - lens_r,
         lens_cx_l + lens_r, lens_cy + lens_r],
        fill=None, outline=VB_RED, width=2
    )
    # Inner glow
    draw.ellipse(
        [lens_cx_l - lens_r/2, lens_cy - lens_r/2,
         lens_cx_l + lens_r/2, lens_cy + lens_r/2],
        fill=(255, 0, 0), outline=None
    )
    
    # Right eye lens glow
    lens_cx_r = cx + visor_width/4
    draw.ellipse(
        [lens_cx_r - lens_r, lens_cy - lens_r,
         lens_cx_r + lens_r, lens_cy + lens_r],
        fill=None, outline=VB_RED, width=2
    )
    draw.ellipse(
        [lens_cx_r - lens_r/2, lens_cy - lens_r/2,
         lens_cx_r + lens_r/2, lens_cy + lens_r/2],
        fill=(255, 0, 0), outline=None
    )
    
    # Side protrusions (stereoscopic mirrors characteristic of VB)
    side_width = 40 * scale
    side_height = 80 * scale
    # Left side mirror housing
    draw.rectangle(
        [cx - visor_width/2 - side_width, cy - side_height/2,
         cx - visor_width/2, cy + side_height/2],
        fill=BG_SECONDARY, outline=VB_RED, width=2
    )
    # Right side mirror housing
    draw.rectangle(
        [cx + visor_width/2, cy - side_height/2,
         cx + visor_width/2 + side_width, cy + side_height/2],
        fill=BG_SECONDARY, outline=VB_RED, width=2
    )
    
    # Controller attachment wire (simplified)
    draw.line(
        [(cx - 20, cy + visor_height/2), (cx - 20, cy + visor_height/2 + 30*scale)],
        fill=VB_RED, width=2
    )

def draw_virtualboy_controller(draw, cx, cy, scale):
    """Draw the Virtual Boy controller with its dual d-pads."""
    # Controller body
    body_width = 200 * scale
    body_height = 80 * scale
    
    # Main body
    draw.rounded_rectangle(
        [cx - body_width/2, cy - body_height/2,
         cx + body_width/2, cy + body_height/2],
        radius=10*scale, fill=BG_SECONDARY, outline=VB_RED, width=2
    )
    
    # Two D-pads (characteristic VB controller feature)
    dpad_size = 30 * scale
    # Left D-pad
    draw.rectangle(
        [cx - body_width/2 + 35*scale - dpad_size/3, cy - dpad_size/2,
         cx - body_width/2 + 35*scale + dpad_size/3, cy + dpad_size/2],
        fill=VB_RED
    )
    draw.rectangle(
        [cx - body_width/2 + 35*scale - dpad_size/2, cy - dpad_size/3,
         cx - body_width/2 + 35*scale + dpad_size/2, cy + dpad_size/3],
        fill=VB_RED
    )
    
    # Right D-pad (for 3D movement)
    draw.rectangle(
        [cx + body_width/2 - 35*scale - dpad_size/3, cy - dpad_size/2,
         cx + body_width/2 - 35*scale + dpad_size/3, cy + dpad_size/2],
        fill=VB_RED
    )
    draw.rectangle(
        [cx + body_width/2 - 35*scale - dpad_size/2, cy - dpad_size/3,
         cx + body_width/2 - 35*scale + dpad_size/2, cy + dpad_size/3],
        fill=VB_RED
    )
    
    # A and B buttons
    btn_r = 12 * scale
    draw.ellipse(
        [cx - 10 - btn_r, cy - 20*scale - btn_r,
         cx - 10 + btn_r, cy - 20*scale + btn_r],
        fill=VB_RED, outline=VB_RED_DARK, width=2
    )
    draw.ellipse(
        [cx + 10 - btn_r, cy - 20*scale - btn_r,
         cx + 10 + btn_r, cy - 20*scale + btn_r],
        fill=VB_RED, outline=VB_RED_DARK, width=2
    )

def draw_quest_headset(draw, cx, cy, scale):
    """Draw a stylized Meta Quest headset silhouette."""
    # Modern Quest headset shape
    width = 240 * scale
    height = 100 * scale
    
    # Main visor - rounded modern shape
    draw.rounded_rectangle(
        [cx - width/2, cy - height/2, cx + width/2, cy + height/2],
        radius=20*scale, fill=BG_SECONDARY, outline=ACCENT_CYAN, width=2
    )
    
    # Display area (dark)
    display_margin = 12 * scale
    draw.rounded_rectangle(
        [cx - width/2 + display_margin, cy - height/2 + display_margin,
         cx + width/2 - display_margin, cy + height/2 - display_margin],
        radius=15*scale, fill="#000000", outline=None
    )
    
    # Quest-style camera sensors (subtle dots)
    sensor_r = 4 * scale
    for ox, oy in [(-width/3, -height/4), (width/3, -height/4),
                   (-width/3, height/4), (width/3, height/4)]:
        draw.ellipse(
            [cx + ox - sensor_r, cy + oy - sensor_r,
             cx + ox + sensor_r, cy + oy + sensor_r],
            fill=ACCENT_CYAN
        )
    
    # Side straps
    draw.rectangle(
        [cx - width/2 - 20*scale, cy - 8*scale,
         cx - width/2, cy + 8*scale],
        fill=BG_SECONDARY, outline=ACCENT_CYAN, width=1
    )
    draw.rectangle(
        [cx + width/2, cy - 8*scale,
         cx + width/2 + 20*scale, cy + 8*scale],
        fill=BG_SECONDARY, outline=ACCENT_CYAN, width=1
    )

def draw_scanlines(img, width, height):
    """Add CRT-style scanlines overlay for retro feel."""
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for y in range(0, height, 3):
        draw.line([(0, y), (width, y)], fill=(0, 0, 0, 20), width=1)
    
    return Image.alpha_composite(img, overlay)

def draw_red_grid(draw, width, height):
    """Draw subtle red grid pattern (Virtual Boy aesthetic meets VR grid)."""
    # Vertical lines
    for x in range(0, width, 40):
        alpha = 15 + (x % 60)
        draw.line([(x, 0), (x, height)], fill=(255, 0, 0, alpha), width=1)
    
    # Horizontal lines (fewer, for perspective feel)
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=(255, 0, 0, 10), width=1)

def draw_vr_grid_perspective(draw, width, height):
    """Draw a retro VR grid emanating from center - Virtual Boy style."""
    # Vanishing point near center
    vp_x = width * 0.6
    vp_y = height * 0.45
    
    # Draw converging lines
    for angle in range(-60, 61, 5):
        rad = math.radians(angle)
        end_x = vp_x + 2000 * math.cos(rad)
        end_y = vp_y + 2000 * math.sin(rad)
        draw.line([(vp_x, vp_y), (end_x, end_y)], fill=(255, 0, 0, 30), width=1)
    
    # Draw horizontal depth lines (perspective)
    for dist in [150, 300, 500, 800]:
        scale_factor = dist / 300
        y_offset = int(dist * 0.3)
        draw.line(
            [(vp_x - dist, vp_y + y_offset), (vp_x + dist, vp_y + y_offset)],
            fill=(255, 0, 0, 20), width=1
        )

def draw_particles(draw, width, height, count=30):
    """Draw floating red particles/dots."""
    import random
    random.seed(42)  # Consistent pattern
    
    for i in range(count):
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        size = random.randint(2, 4)
        
        # Red particles with glow
        draw.ellipse(
            [x - size, y - size, x + size, y + size],
            fill=(255, 0, 0, random.randint(100, 200))
        )

def draw_wireframe_world(draw, width, height):
    """Draw a wireframe 3D world representation (Virtual Boy game aesthetic)."""
    # Perspective grid floor
    horizon = height * 0.55
    
    # Horizontal lines going into distance
    for i, y_mult in enumerate([0.1, 0.15, 0.2, 0.3, 0.45]):
        y = horizon + height * y_mult
        perspective = 1 - y_mult
        x_inset = int(100 * perspective)
        draw.line(
            [(x_inset, y), (width - x_inset, y)],
            fill=(255, 0, 0, 40 - i*5), width=1
        )
    
    # Vertical lines converging to vanishing point
    vp_x = width * 0.55
    for x_offset in range(-4, 5):
        base_x = vp_x + x_offset * 80
        draw.line(
            [(base_x, height), (vp_x, horizon)],
            fill=(255, 0, 0, 25), width=1
        )

def draw_brand_accent(draw, width, height):
    """Add subtle cyan brand accent for modern VR feel."""
    # Gradient cyan glow at top
    for i in range(30):
        alpha = 30 - i
        y = i * 3
        r, g, b = 110, 231, 255  # Cyan #6ee7ff
        draw.line(
            [(50, y), (width - 50, y)],
            fill=(r, g, b, alpha), width=2
        )

def add_glow_effect(img, cx, cy, color, intensity=1.0):
    """Add a radial glow effect at specified center."""
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    max_radius = int(200 * intensity)
    for radius in range(max_radius, 20, -5):
        alpha = int(15 * (radius / max_radius) * intensity)
        if color == 'red':
            draw.ellipse(
                [cx - radius, cy - radius, cx + radius, cy + radius],
                fill=(255, 0, 0, alpha), outline=None
            )
        elif color == 'cyan':
            draw.ellipse(
                [cx - radius, cy - radius, cx + radius, cy + radius],
                fill=(110, 231, 255, alpha), outline=None
            )
    
    return Image.alpha_composite(img, overlay)

def create_hero_image():
    """Create the VRboy Virtual Boy hero image."""
    width, height = 1280, 720
    
    # Create base with gradient
    img = create_gradient_background(width, height, BG_PRIMARY, BG_SECONDARY)
    img = img.convert('RGBA')
    
    draw = ImageDraw.Draw(img)
    
    # Add subtle perspective grid (Virtual Boy aesthetic)
    draw_vr_grid_perspective(draw, width, height)
    
    # Add wireframe world
    draw_wireframe_world(draw, width, height)
    
    # Draw Virtual Boy headset (left side, larger - retro element)
    draw_virtualboy_headset(draw, int(width * 0.28), int(height * 0.45), 0.85)
    
    # Draw Virtual Boy controller (lower left)
    draw_virtualboy_controller(draw, int(width * 0.22), int(height * 0.78), 0.65)
    
    # Draw Quest headset (right side - modern VR element)
    draw_quest_headset(draw, int(width * 0.72), int(height * 0.40), 0.9)
    
    # Add red glow around Virtual Boy elements
    img = add_glow_effect(img, int(width * 0.28), int(height * 0.45), 'red', 1.2)
    
    # Add cyan brand accent
    draw_brand_accent(draw, width, height)
    
    # Add floating particles
    draw_particles(draw, width, height, 40)
    
    # Add scanline overlay
    img = draw_scanlines(img, width, height)
    
    # Add text area indicator (left side clear for potential text overlay)
    # Subtle vignette on edges
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Right edge fade (for text space)
    for x in range(100):
        alpha = int(50 * (x / 100))
        overlay_draw.line(
            [(width - x, 0), (width - x, height)],
            fill=(11, 16, 32, alpha), width=1
        )
    
    img = Image.alpha_composite(img, overlay)
    
    # Draw final ambient particles
    draw = ImageDraw.Draw(img)
    for i in range(25):
        x = (i * 51 + 30) % width
        y = (i * 29 + 100) % height
        size = 2 + (i % 3)
        # Mix of red (VB) and cyan (modern VR) particles
        if i % 3 == 0:
            color = (255, 0, 0, 80 + i*3)
        else:
            color = (110, 231, 255, 60 + i*2)
        draw.rectangle([x, y, x + size, y + size], fill=color)
    
    # Convert to RGB for final output
    img_rgb = img.convert('RGB')
    
    return img_rgb

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate VRboy Virtual Boy Hero Image')
    parser.add_argument('--output', '-o', 
                        default='/home/antforce/compoundvr-project/public/images/articles/vrboy-virtual-boy-hero.jpg',
                        help='Output path for the hero image')
    args = parser.parse_args()
    
    # Ensure output directory exists
    output_path = args.output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Generate image
    print("Generating VRboy Virtual Boy hero image...")
    print("  Theme: Nintendo Virtual Boy (1995) → Meta Quest VR")
    print("  Style: Retro-futuristic, red monochrome meets modern VR")
    print(f"  Output: {output_path}")
    
    img = create_hero_image()
    
    # Save with web-optimized JPEG settings
    img.save(output_path, "JPEG", quality=90, optimize=True, progressive=True)
    
    print(f"\n✓ Hero image saved successfully!")
    print(f"  Dimensions: {img.size[0]}x{img.size[1]}")
    print(f"  File size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()