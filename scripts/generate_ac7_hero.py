#!/usr/bin/env python3
"""
Generate Ace Combat 7 VR Hero Image
Brand: CompoundVR (deep navy #0b1020, cyan #6ee7ff accents)
Style: Technical authority, sophisticated restraint, arcade flight aesthetic
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

# Brand colors
BG_PRIMARY = "#0b1020"      # Deep navy background
BG_SECONDARY = "#0f1528"    # Slightly lighter
ACCENT_CYAN = "#6ee7ff"     # Primary accent
ACCENT_CYAN_GLOW = (110, 231, 255, 80)  # Semi-transparent cyan
TEXT_PRIMARY = "#f0f4ff"    # Headlines
TEXT_SECONDARY = "#c5cce6"  # Body
SURFACE_PRIMARY = "#151d38" # Cards

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

def draw_hexagon(draw, center, size, color, width=1):
    """Draw a hexagon shape."""
    points = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 2
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))
    draw.polygon(points, outline=color, width=width)

def draw_fighter_jet_silhouette(draw, x, y, scale, color):
    """Draw a stylized F-22-like fighter jet silhouette from top view."""
    # Main fuselage
    fuselage_points = [
        (x, y - 80 * scale),  # Nose
        (x - 8 * scale, y - 40 * scale),  # Nose sides
        (x - 12 * scale, y + 20 * scale),  # Wing root front
        (x - 50 * scale, y + 60 * scale),  # Left wing tip
        (x - 15 * scale, y + 50 * scale),  # Left wing trailing
        (x - 8 * scale, y + 80 * scale),  # Left tail
        (x, y + 70 * scale),  # Center tail
        (x + 8 * scale, y + 80 * scale),  # Right tail
        (x + 15 * scale, y + 50 * scale),  # Right wing trailing
        (x + 50 * scale, y + 60 * scale),  # Right wing tip
        (x + 12 * scale, y + 20 * scale),  # Wing root front
        (x + 8 * scale, y - 40 * scale),  # Nose sides
    ]
    draw.polygon(fuselage_points, fill=color)
    
    # Cockpit canopy highlight
    canopy_points = [
        (x, y - 20 * scale),
        (x - 5 * scale, y + 10 * scale),
        (x, y + 15 * scale),
        (x + 5 * scale, y + 10 * scale),
    ]
    draw.polygon(canopy_points, fill=ACCENT_CYAN_GLOW)

def draw_hud_element(draw, x, y, size, label, color):
    """Draw a stylized HUD display element."""
    # Draw box
    draw.rectangle([x - size, y - size/2, x + size, y + size/2], 
                   outline=color, width=2)
    # Draw crosshair in center
    draw.line([(x - size/3, y), (x + size/3, y)], fill=color, width=1)
    draw.line([(x, y - size/3), (x, y + size/3)], fill=color, width=1)

def draw_vr_headset_outline(draw, cx, cy, width, height, color):
    """Draw a subtle VR headset outline."""
    # Left lens
    draw.ellipse([cx - width/2 - 20, cy - 30, cx - width/2 + 20, cy + 30], 
                 outline=color, width=1)
    # Right lens
    draw.ellipse([cx + width/2 - 20, cy - 30, cx + width/2 + 20, cy + 30], 
                 outline=color, width=1)
    # Bridge
    draw.line([(cx - width/2 + 20, cy), (cx + width/2 - 20, cy)], 
              fill=color, width=1)
    # Head strap
    draw.arc([cx - width/2 - 60, cy - 40, cx + width/2 + 60, cy + 40], 
             120, 240, fill=color, width=1)

def create_hero_image():
    """Create the Ace Combat 7 VR hero image."""
    width, height = 1280, 720
    
    # Create base image with gradient
    img = create_gradient_background(width, height, BG_PRIMARY, BG_SECONDARY)
    draw = ImageDraw.Draw(img)
    
    # Add subtle radial glow in center-top (sky/cockpit area)
    for r in range(400, 0, -10):
        alpha = int(15 * (r / 400))
        color = (110, 231, 255, alpha)
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse([width/2 - r, height/3 - r/2, width/2 + r, height/3 + r/2], 
                            fill=color)
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Draw stylized fighter jet from below/behind (dramatic perspective)
    jet_x, jet_y = width // 2, height // 2 + 50
    jet_scale = 1.5
    
    # Jet body with gradient
    for i in range(10):
        offset = i * 3
        alpha = 255 - i * 20
        color = (30, 35, 60 + offset, alpha)
        draw_fighter_jet_silhouette(draw, jet_x + offset, jet_y + offset, 
                                   jet_scale - i * 0.02, color)
    
    # Main jet
    draw_fighter_jet_silhouette(draw, jet_x, jet_y, jet_scale, SURFACE_PRIMARY)
    
    # Jet outline/highlight with cyan
    nose_tip = (jet_x, jet_y - 80 * jet_scale)
    
    # Draw engine glow (cyan accent)
    for r in range(30, 5, -5):
        alpha = int(100 * (r / 30))
        color = (110, 231, 255, alpha)
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        # Left engine
        overlay_draw.ellipse([jet_x - 25 * jet_scale - r, jet_y + 75 * jet_scale - r/2,
                              jet_x - 15 * jet_scale + r, jet_y + 85 * jet_scale + r/2], 
                             fill=color)
        # Right engine
        overlay_draw.ellipse([jet_x + 15 * jet_scale - r, jet_y + 75 * jet_scale - r/2,
                              jet_x + 25 * jet_scale + r, jet_y + 85 * jet_scale + r/2], 
                             fill=color)
        img = Image.alpha_composite(img, overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Add HUD elements (cyan accents)
    # Left side HUD
    draw_hud_element(draw, 150, 200, 60, "SPD", ACCENT_CYAN)
    draw_hud_element(draw, 150, 350, 60, "ALT", ACCENT_CYAN)
    
    # Right side HUD
    draw_hud_element(draw, width - 150, 200, 60, "RAD", ACCENT_CYAN)
    draw_hud_element(draw, width - 150, 350, 60, "WPN", ACCENT_CYAN)
    
    # Center crosshair/targeting reticle
    cx, cy = width // 2, height // 2 + 20
    # Outer ring
    draw.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], outline=ACCENT_CYAN, width=2)
    # Inner cross
    draw.line([(cx - 40, cy), (cx + 40, cy)], fill=ACCENT_CYAN, width=2)
    draw.line([(cx, cy - 40), (cx, cy + 40)], fill=ACCENT_CYAN, width=2)
    # Corner brackets
    bracket_size = 25
    # Top left
    draw.line([(cx - 60, cy - 60), (cx - 60 + bracket_size, cy - 60)], fill=ACCENT_CYAN, width=2)
    draw.line([(cx - 60, cy - 60), (cx - 60, cy - 60 + bracket_size)], fill=ACCENT_CYAN, width=2)
    # Top right
    draw.line([(cx + 60, cy - 60), (cx + 60 - bracket_size, cy - 60)], fill=ACCENT_CYAN, width=2)
    draw.line([(cx + 60, cy - 60), (cx + 60, cy - 60 + bracket_size)], fill=ACCENT_CYAN, width=2)
    # Bottom left
    draw.line([(cx - 60, cy + 60), (cx - 60 + bracket_size, cy + 60)], fill=ACCENT_CYAN, width=2)
    draw.line([(cx - 60, cy + 60), (cx - 60, cy + 60 - bracket_size)], fill=ACCENT_CYAN, width=2)
    # Bottom right
    draw.line([(cx + 60, cy + 60), (cx + 60 - bracket_size, cy + 60)], fill=ACCENT_CYAN, width=2)
    draw.line([(cx + 60, cy + 60), (cx + 60, cy + 60 - bracket_size)], fill=ACCENT_CYAN, width=2)
    
    # Draw altitude bars on right side
    for i in range(10):
        y_pos = 150 + i * 40
        if i % 2 == 0:
            draw.line([(width - 50, y_pos), (width - 30, y_pos)], fill=ACCENT_CYAN, width=2)
        else:
            draw.line([(width - 40, y_pos), (width - 30, y_pos)], fill=ACCENT_CYAN, width=1)
    
    # Draw hexagonal decorative elements (CompoundVR brand motif)
    draw_hexagon(draw, (100, height - 100), 40, ACCENT_CYAN, 2)
    draw_hexagon(draw, (width - 100, height - 100), 40, ACCENT_CYAN, 2)
    
    # Subtle VR headset outline framing the scene
    draw_vr_headset_outline(draw, width // 2, height // 2 + 20, 500, 300, 
                            (110, 231, 255, 40))
    
    # Add some cloud/haze effects at bottom
    for i in range(5):
        x_pos = i * 300 + 100
        y_pos = height - 100 + (i % 3) * 30
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse([x_pos - 150, y_pos - 40, x_pos + 150, y_pos + 40], 
                            fill=(15, 21, 40, 100))
        img = Image.alpha_composite(img, overlay)
    
    # Convert to RGB for JPEG
    img_rgb = img.convert('RGB')
    
    return img_rgb

def main():
    # Ensure output directory exists
    output_dir = "/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/assets/images/games"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate image
    img = create_hero_image()
    
    # Save with web-optimized JPEG settings
    output_path = os.path.join(output_dir, "ace-combat-7-vr-hero.jpg")
    img.save(output_path, "JPEG", quality=85, optimize=True, progressive=True)
    
    print(f"Hero image saved to: {output_path}")
    print(f"Dimensions: {img.size}")
    print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
