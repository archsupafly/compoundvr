#!/usr/bin/env python3
"""Generate Star Wars TIE Fighter cockpit hero image using PIL."""

from PIL import Image, ImageDraw, ImageFilter
import math
import random

random.seed(42)

# Canvas size
W, H = 1200, 600
img = Image.new('RGB', (W, H), '#050510')
draw = ImageDraw.Draw(img)

def draw_gradient_bg():
    """Draw space background with gradient."""
    for y in range(H):
        for x in range(W):
            dist = math.sqrt((x - W//2)**2 + (y - H//2)**2)
            t = min(dist / 600, 1.0)
            r = int(10 * (1 - t * 0.8))
            g = int(10 * (1 - t * 0.8))
            b = int(20 + 6 * (1 - t))
            img.putpixel((x, y), (r, g, b))

def draw_nebula():
    """Draw subtle nebula effects."""
    # Purple nebula on left
    for i in range(150):
        angle = i * 0.15
        dist = i * 2.5
        x = int(350 + math.cos(angle) * dist * 0.8)
        y = int(200 + math.sin(angle) * dist * 0.5)
        size = int(100 - i * 0.5)
        if size > 0 and 0 < x < W and 0 < y < H:
            alpha = int(40 * (1 - i/150))
            overlay = Image.new('RGBA', (size*2, size*2), (42, 26, 74, alpha))
            img.paste(overlay, (x-size, y-size), overlay)
    
    # Blue nebula on right
    for i in range(120):
        angle = i * 0.12 + math.pi
        dist = i * 2.2
        x = int(900 + math.cos(angle) * dist * 0.7)
        y = int(350 + math.sin(angle) * dist * 0.4)
        size = int(80 - i * 0.5)
        if size > 0 and 0 < x < W and 0 < y < H:
            alpha = int(35 * (1 - i/120))
            overlay = Image.new('RGBA', (size*2, size*2), (26, 42, 58, alpha))
            img.paste(overlay, (x-size, y-size), overlay)

def draw_stars():
    """Draw stars."""
    stars = [
        (100, 80, 0.8), (250, 150, 1.2), (400, 60, 0.6), (550, 120, 1),
        (700, 90, 0.7), (850, 180, 0.9), (1000, 70, 0.5), (1100, 200, 1.1),
        (150, 300, 0.8), (320, 350, 0.6), (480, 280, 1), (620, 320, 0.7),
        (780, 290, 0.5), (920, 340, 0.9), (1050, 260, 0.8), (200, 450, 1),
        (380, 480, 0.6), (540, 420, 0.7), (680, 460, 0.5), (840, 400, 0.9),
        (1020, 470, 1.2), (60, 520, 0.8), (1150, 380, 0.6)
    ]
    for x, y, r in stars:
        if y < 500:
            draw.ellipse([x-r, y-r, x+r, y+r], fill='#ffffff')

def draw_lasers():
    """Draw distant laser fire."""
    # Red lasers
    draw.line([(750, 100), (680, 80)], fill='#ff6b6b', width=2)
    draw.line([(800, 120), (720, 100)], fill='#ff6b6b', width=2)
    draw.line([(820, 150), (750, 130)], fill='#ff6b6b', width=2)
    
    # Blue lasers
    draw.line([(200, 200), (280, 180)], fill='#4a9eff', width=2)
    draw.line([(180, 250), (260, 220)], fill='#4a9eff', width=2)
    
    # Distant battle sparks
    draw.ellipse([649, 149, 651, 151], fill='#ffaa44')
    draw.ellipse([719, 179, 721, 181], fill='#ffaa44')
    draw.ellipse([579, 199, 581, 201], fill='#ffaa44')

def draw_hexagon(cx, cy, size):
    """Draw a hexagonal viewport."""
    points = []
    for i in range(6):
        angle = (math.pi / 3) * i - math.pi / 2
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        points.append((x, y))
    
    # Frame
    draw.polygon(points, fill='#050510', outline='#1a1a1a', width=8)
    # Inner highlight
    draw.polygon(points, outline='#3a3a3a', width=2)

def draw_cockpit_frames():
    """Draw the TIE fighter cockpit structure."""
    # Left side panel
    draw.polygon([(0, 0), (200, 0), (180, 150), (0, 200)], 
                 fill='#151515', outline='#2a2a2a', width=2)
    
    # Right side panel
    draw.polygon([(1200, 0), (1000, 0), (1020, 150), (1200, 200)], 
                 fill='#151515', outline='#2a2a2a', width=2)
    
    # Bottom area
    draw.polygon([(0, 600), (300, 600), (400, 450), (800, 450), 
                  (900, 600), (1200, 600), (1200, 500), (1020, 450),
                  (1020, 350), (1200, 300), (1200, 250), (1000, 200),
                  (1000, 0), (1200, 0)],
                 fill='#101010', outline='#2a2a2a', width=2)

def draw_side_panels():
    """Draw side dashboard panels."""
    # Left panel
    draw.rectangle([220, 400, 320, 550], fill='#151515', outline='#2a2a2a', width=1)
    # Right panel  
    draw.rectangle([880, 400, 980, 550], fill='#151515', outline='#2a2a2a', width=1)
    
    # Metal texture on side consoles
    for x in [220, 880]:
        for y in range(400, 551, 20):
            draw.line([(x, y), (x+100, y)], fill='#252525', width=1)

def draw_hex_viewports():
    """Draw hexagonal viewports."""
    # Left viewports
    draw_hexagon(280, 120, 50)
    draw_hexagon(280, 220, 50)
    draw_hexagon(280, 320, 50)
    
    # Right viewports
    draw_hexagon(920, 120, 50)
    draw_hexagon(920, 220, 50)
    draw_hexagon(920, 320, 50)

def draw_center_viewport():
    """Draw the main central viewport."""
    # Main viewport - octagonal shape
    points = [(400, 100), (500, 60), (700, 60), (800, 100), 
              (800, 350), (700, 390), (500, 390), (400, 350)]
    draw.polygon(points, fill='#050510', outline='#1a1a1a', width=10)
    draw.polygon(points, outline='#3a3a3a', width=3)

def draw_dashboard():
    """Draw the center dashboard."""
    # Main dashboard area
    points = [(350, 400), (450, 380), (750, 380), (850, 400), 
              (850, 500), (350, 500)]
    draw.polygon(points, fill='#0a0a0a', outline='#2a2a2a', width=2)
    
    # Dashboard buttons
    buttons = [
        (400, 420, 50, 30), (470, 415, 60, 35), (550, 420, 40, 25),
        (610, 415, 50, 30), (680, 420, 45, 28), (750, 425, 50, 25)
    ]
    for bx, by, bw, bh in buttons:
        draw.rectangle([bx, by, bx+bw, by+bh], fill='#1a1a1a', outline='#3a3a3a', width=1)

def draw_hud():
    """Draw green HUD elements."""
    hud_color = '#39ff14'
    
    # Target reticle - center of main viewport
    cx, cy = 600, 225
    radius = 60
    
    # Outer circle
    draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], 
                 outline=hud_color, width=2)
    
    # Crosshairs
    # Top
    draw.line([(cx, cy-65), (cx, cy-45)], fill=hud_color, width=3)
    # Bottom
    draw.line([(cx, cy+45), (cx, cy+65)], fill=hud_color, width=3)
    # Left
    draw.line([(cx-65, cy), (cx-45, cy)], fill=hud_color, width=3)
    # Right
    draw.line([(cx+45, cy), (cx+65, cy)], fill=hud_color, width=3)
    
    # HUD frame lines
    draw.line([(420, 320), (450, 290), (750, 290), (780, 320)], 
              fill=hud_color, width=2)
    
    # Side HUD boxes
    draw.rectangle([280, 100, 340, 120], outline=hud_color, width=1)
    draw.rectangle([860, 100, 920, 120], outline=hud_color, width=1)
    draw.line([(310, 110), (330, 110)], fill=hud_color, width=2)
    draw.line([(870, 110), (890, 110)], fill=hud_color, width=2)

def draw_indicators():
    """Draw dashboard green indicators."""
    indicator_color = '#39ff14'
    indicators = [
        (410, 428, 30, 4), (480, 423, 40, 4), (560, 428, 20, 4),
        (620, 423, 30, 4), (690, 428, 25, 4), (760, 432, 30, 4)
    ]
    for x, y, w, h in indicators:
        draw.rectangle([x, y, x+w, y+h], fill=indicator_color)

# Build the image
draw_gradient_bg()
draw_nebula()
draw_stars()
draw_lasers()
draw_cockpit_frames()
draw_side_panels()
draw_hex_viewports()
draw_center_viewport()
draw_dashboard()
draw_hud()
draw_indicators()

# Save as JPG
output_path = '/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games/tie-fighter-hero.jpg'
img = img.convert('RGB')
img.save(output_path, 'JPEG', quality=95)
print(f"Saved: {output_path}")