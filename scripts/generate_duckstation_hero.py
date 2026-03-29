#!/usr/bin/env python3
"""
Generate DuckStation VR Hero Image
Brand: CompoundVR (deep navy #0b1020, cyan #0ee7ff accents)
Style: Nostalgic yet futuristic, retro PS1 meets modern VR
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

# Brand colors v2 (light body, dark header theme)
BG_PRIMARY = "#0b1020"      # Deep navy background (for hero/header)
BG_SECONDARY = "#151d38"    # Slightly lighter
ACCENT_CYAN = "#0ee7ff"     # Primary accent (cyan)
ACCENT_CYAN_GLOW = (14, 231, 255, 60)  # Semi-transparent cyan
ACCENT_PURPLE = "#8b5cf6"   # Secondary accent
TEXT_PRIMARY = "#f0f4ff"    # Headlines
SURFACE_PRIMARY = "#1a2547" # Cards/elements

# PS1 nostalgic colors
PS1_GRAY = "#c0c0c0"        # Classic PlayStation gray
PS1_BLUE = "#003087"        # PlayStation blue

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

def draw_vr_headset(draw, cx, cy, scale, color, accent_color):
    """Draw a stylized modern VR headset silhouette."""
    # Main headset body (rounded rectangle shape)
    width = 300 * scale
    height = 160 * scale
    
    # Outer shell
    headset_points = [
        (cx - width/2, cy - height/2 + 30),  # Top left curve
        (cx - width/2 + 30, cy - height/2),  # Top left corner
        (cx + width/2 - 30, cy - height/2),  # Top right corner
        (cx + width/2, cy - height/2 + 30),  # Top right curve
        (cx + width/2, cy + height/2 - 30),  # Bottom right curve
        (cx + width/2 - 30, cy + height/2),  # Bottom right corner
        (cx - width/2 + 30, cy + height/2),  # Bottom left corner
        (cx - width/2, cy + height/2 - 30),  # Bottom left curve
    ]
    draw.polygon(headset_points, fill=color, outline=accent_color, width=2)
    
    # Left lens (glowing)
    lens_glow = (14, 231, 255, 100)
    draw.ellipse([cx - width/3 - 50*scale, cy - 40*scale, 
                  cx - width/3 + 50*scale, cy + 40*scale], 
                 fill=BG_PRIMARY, outline=accent_color, width=2)
    
    # Right lens (glowing)
    draw.ellipse([cx + width/3 - 50*scale, cy - 40*scale, 
                  cx + width/3 + 50*scale, cy + 40*scale], 
                 fill=BG_PRIMARY, outline=accent_color, width=2)
    
    # Head strap
    strap_points = [
        (cx - width/2, cy - 20),
        (cx - width/2 - 80*scale, cy - 10),
        (cx - width/2 - 80*scale, cy + 10),
        (cx - width/2, cy + 20),
    ]
    draw.polygon(strap_points, fill=color, outline=accent_color, width=1)
    
    strap_points_r = [
        (cx + width/2, cy - 20),
        (cx + width/2 + 80*scale, cy - 10),
        (cx + width/2 + 80*scale, cy + 10),
        (cx + width/2, cy + 20),
    ]
    draw.polygon(strap_points_r, fill=color, outline=accent_color, width=1)

def draw_ps1_controller(draw, x, y, scale, color, accent_color):
    """Draw a stylized floating PS1 controller."""
    # Controller body (classic shape)
    body_width = 200 * scale
    body_height = 120 * scale
    
    # Main body with handles
    ctrl_points = [
        (x - body_width/2 + 20, y - body_height/2),  # Top left
        (x + body_width/2 - 20, y - body_height/2),  # Top right
        (x + body_width/2 + 30, y + body_height/2 - 20),  # Right handle
        (x + body_width/2 - 20, y + body_height/2),  # Bottom right
        (x + 20, y + body_height/2 + 10),  # Center bottom
        (x - 20, y + body_height/2 + 10),  # Center bottom
        (x - body_width/2 + 20, y + body_height/2),  # Bottom left
        (x - body_width/2 - 30, y + body_height/2 - 20),  # Left handle
    ]
    draw.polygon(ctrl_points, fill=color, outline=accent_color, width=1)
    
    # D-Pad (cross shape)
    dpad_size = 25 * scale
    draw.rectangle([x - body_width/2 + 40 - dpad_size/3, y - dpad_size/2,
                    x - body_width/2 + 40 + dpad_size/3, y + dpad_size/2], 
                   fill=accent_color)
    draw.rectangle([x - body_width/2 + 40 - dpad_size/2, y - dpad_size/3,
                    x - body_width/2 + 40 + dpad_size/2, y + dpad_size/3], 
                   fill=accent_color)
    
    # Action buttons (geometric shapes)
    btn_size = 15 * scale
    # Triangle
    tri_points = [(x + body_width/2 - 40, y - 20), 
                  (x + body_width/2 - 40 - btn_size, y + 5),
                  (x + body_width/2 - 40 + btn_size, y + 5)]
    draw.polygon(tri_points, outline=accent_color, width=2)
    
    # Square
    draw.rectangle([x + body_width/2 - 70 - btn_size, y - btn_size,
                    x + body_width/2 - 70 + btn_size, y + btn_size], 
                   outline=accent_color, width=2)
    
    # X
    draw.line([(x + body_width/2 - 40 - btn_size, y + 30 - btn_size),
               (x + body_width/2 - 40 + btn_size, y + 30 + btn_size)], 
              fill=accent_color, width=2)
    draw.line([(x + body_width/2 - 40 + btn_size, y + 30 - btn_size),
               (x + body_width/2 - 40 - btn_size, y + 30 + btn_size)], 
              fill=accent_color, width=2)
    
    # Circle
    draw.ellipse([x + body_width/2 - 10 - btn_size, y + 30 - btn_size,
                  x + body_width/2 - 10 + btn_size, y + 30 + btn_size], 
                 outline=accent_color, width=2)

def draw_ps1_console(draw, x, y, scale, color, accent_color):
    """Draw a stylized floating PS1 console."""
    width = 280 * scale
    height = 60 *scale
    depth = 120 * scale
    
    # Top surface
    top_points = [
        (x - width/2, y - depth/2),  # Back left
        (x + width/2, y - depth/2),  # Back right
        (x + width/2 - 20, y + depth/2),  # Front right
        (x - width/2 + 20, y + depth/2),  # Front left
    ]
    draw.polygon(top_points, fill=color, outline=accent_color, width=2)
    
    # Front face
    front_points = [
        (x - width/2 + 20, y + depth/2),
        (x + width/2 - 20, y + depth/2),
        (x + width/2 - 20, y + depth/2 + height),
        (x - width/2 + 20, y + depth/2 + height),
    ]
    draw.polygon(front_points, fill=BG_SECONDARY, outline=accent_color, width=1)
    
    # Disc lid line
    draw.line([(x - width/3, y + depth/2 + 15), (x + width/3, y + depth/2 + 15)], 
              fill=accent_color, width=2)
    
    # Power LED
    draw.ellipse([x + width/3 - 8, y + depth/2 + 35, x + width/3 + 8, y + depth/2 + 55], 
                 fill=accent_color, outline=accent_color, width=2)

def draw_geometric_shapes(draw, width, height, accent_color):
    """Draw floating geometric shapes representing VR/retro fusion."""
    # Handle accent_color as either hex string or RGB tuple
    if isinstance(accent_color, str):
        r = int(accent_color[1:3], 16)
        g = int(accent_color[3:5], 16)
        b = int(accent_color[5:7], 16)
    else:
        r, g, b = accent_color[:3]
    
    # Hexagons (VR/grid aesthetic)
    for i in range(3):
        cx = width * (0.15 + i * 0.35)
        cy = height * (0.2 + (i % 2) * 0.15)
        size = 30 + i * 10
        
        points = []
        for j in range(6):
            angle = math.pi / 3 * j - math.pi / 2
            px = cx + size * math.cos(angle)
            py = cy + size * math.sin(angle)
            points.append((px, py))
        draw.polygon(points, outline=accent_color, width=1)
    
    # Floating squares/voxels (PS1 retro aesthetic)
    for i in range(4):
        cx = width * (0.1 + i * 0.25)
        cy = height * (0.7 - (i % 2) * 0.1)
        size = 15 + (i % 3) * 8
        
        # Wireframe cube effect
        draw.rectangle([cx - size, cy - size, cx + size, cy + size], 
                      outline=accent_color, width=1)

def draw_light_beams(img, width, height, accent_color):
    """Draw subtle cyan light beams/glows."""
    # Handle accent_color as either hex string or RGB tuple
    if isinstance(accent_color, str):
        r = int(accent_color[1:3], 16)
        g = int(accent_color[3:5], 16)
        b = int(accent_color[5:7], 16)
    else:
        r, g, b = accent_color[:3]
    
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top-center glow
    for radius in range(300, 50, -20):
        alpha = int(10 * (radius / 300))
        color = (r, g, b, alpha)
        draw.ellipse([width/2 - radius, -radius/2, width/2 + radius, radius/2], fill=color)
    
    # Side accent lines
    for i in range(3):
        x_pos = width * (0.15 + i * 0.35)
        for y in range(0, height, 20):
            draw.line([(x_pos, y), (x_pos, y + 10)], 
                     fill=(r, g, b, 30), width=1)
    
    return Image.alpha_composite(img, overlay)

def create_hero_image():
    """Create the DuckStation VR hero image."""
    width, height = 1280, 720
    
    # Create base image with gradient
    img = create_gradient_background(width, height, BG_PRIMARY, BG_SECONDARY)
    img = img.convert('RGBA')
    
    draw = ImageDraw.Draw(img)
    
    # Draw floating geometric shapes (background layer)
    draw_geometric_shapes(draw, width, height, ACCENT_CYAN)
    
    # Draw PS1 console floating on left (retro element)
    draw_ps1_console(draw, width * 0.2, height * 0.3, 0.8, SURFACE_PRIMARY, ACCENT_CYAN)
    
    # Draw PS1 controller floating on right
    draw_ps1_controller(draw, width * 0.8, height * 0.35, 0.7, SURFACE_PRIMARY, ACCENT_CYAN)
    
    # Draw central VR headset (futuristic element)
    draw_vr_headset(draw, width // 2, height // 2 + 50, 1.2, SURFACE_PRIMARY, ACCENT_CYAN)
    
    # Add subtle glow effects around VR headset
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Cyan glow around headset
    for r in range(150, 20, -10):
        alpha = int(25 * (r / 150))
        color = (14, 231, 255, alpha)
        overlay_draw.ellipse([width//2 - r - 100, height//2 - r//2,
                              width//2 + r + 100, height//2 + r//2 + 100], 
                             outline=color, width=2)
    
    img = Image.alpha_composite(img, overlay)
    
    # Add light beams
    img = draw_light_beams(img, width, height, ACCENT_CYAN)
    
    # Add floating particles/voxels
    draw = ImageDraw.Draw(img)
    for i in range(20):
        px = (i * 60 + 50) % width
        py = (i * 80) % height
        size = 2 + (i % 3)
        alpha = 100 + (i % 100)
        color = (14, 231, 255, alpha)
        draw.rectangle([px, py, px + size, py + size], fill=color)
    
    # Convert to RGB for JPEG
    img_rgb = img.convert('RGB')
    
    return img_rgb

def main():
    # Ensure output directory exists
    output_dir = "/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/articles"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate image
    img = create_hero_image()
    
    # Save with web-optimized JPEG settings
    output_path = os.path.join(output_dir, "duckstation-vr-hero.jpg")
    img.save(output_path, "JPEG", quality=85, optimize=True, progressive=True)
    
    print(f"Hero image saved to: {output_path}")
    print(f"Dimensions: {img.size}")
    print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
