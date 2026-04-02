#!/usr/bin/env python3
# Until Dawn: Rush of Blood Hero Image Generator
# Creates a 1920x1080 hero image for CompoundVR
# Style: Horror carnival, on-rails mine cart perspective featuring clowns and wendigos

try:
    from PIL import Image, ImageDraw
    import math, os, random
    
    print("PIL imported successfully")
    print(f"Image module: {Image}")
    
    width, height = 1920, 1080
    output = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    
    print(f"Generating hero image: {width}x{height}")
    
    # Create dark gradient background
    img = Image.new('RGB', (width, height), "#080c18")
    draw = ImageDraw.Draw(img)
    
    # Vertical gradient
    for y in range(height):
        ratio = y / height
        r = 8 + int(7 * ratio)
        g = 12 + int(9 * ratio)
        b = 24 + int(16 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    print("Background created")
    
    # Convert to RGBA for effects
    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)
    
    # Mine cart track perspective
    for i in range(50):
        progress = i / 50.0
        y_start = int(height * (0.92 - progress * 0.62))
        y_end = int(height * (0.95 - progress * 0.62))
        track_width = 280 * (1 - progress * 0.85)
        brightness = 25 + int(18 * progress)
        draw.rectangle([width//2 - track_width, y_start, width//2 + track_width, y_end], 
                      fill=(brightness, brightness, brightness + 8))
    
    print("Track drawn")
    
    # Tunnel entrance
    tx, ty, tw, th = width//2, int(height * 0.12), 380, int(height * 0.32)
    for d in range(10, -1, -1):
        offset = d * 4
        dark = 10 + d * 2
        arch = [(tx - tw//2 + offset, ty + th), 
                 (tx - tw//2 + offset, ty + int(th * 0.35) - offset//10),
                 (tx - tw//4 + offset//2, ty + offset//3), 
                 (tx, ty - int(th * 0.12) + offset//4),
                 (tx + tw//4 - offset//2, ty + offset//3), 
                 (tx + tw//2 - offset, ty + int(th * 0.35) - offset//10),
                 (tx + tw//2 - offset, ty + th)]
        draw.polygon(arch, fill=(dark, dark, dark + 5))
    
    # Red glow inside tunnel
    draw.ellipse([tx - 35, ty - 25, tx + 35, ty + 15], fill=(50, 0, 0))
    
    print("Tunnel drawn")
    
    # Horror clown function
    def draw_horror_clown(x, y, scale, facing_right, is_distant):
        if not facing_right:
            x = int(x - 45 * scale)
        
        body_color = (25, 25, 30) if is_distant else (35, 35, 42)
        draw.ellipse([x - 35*scale, y - 65*scale, x + 35*scale, y + 45*scale], fill=body_color)
        
        head_y = int(y - 55 * scale)
        draw.ellipse([x - 28*scale, head_y - 32*scale, x + 28*scale, head_y + 32*scale], fill=(18, 18, 22))
        
        eye_y = head_y - 5
        eye_size = max(6, int(7 * scale))
        glow_orange = (255, 107, 53)
        
        if not is_distant:
            draw.ellipse([x - 20*scale, eye_y - 12, x + 20*scale, eye_y + 12], fill=(200, 80, 20))
        
        draw.ellipse([x - 14*scale, eye_y - eye_size//2, x - 6*scale, eye_y + eye_size//2], fill=glow_orange)
        draw.ellipse([x + 6*scale, eye_y - eye_size//2, x + 14*scale, eye_y + eye_size//2], fill=glow_orange)
        
        if not is_distant:
            draw.arc([x - 18*scale, head_y + 8, x + 18*scale, head_y + 28*scale], 0, 180, fill=glow_orange, width=3)
    
    draw_horror_clown(int(width * 0.22), int(height * 0.58), 1.35, True, False)
    draw_horror_clown(int(width * 0.80), int(height * 0.42), 0.85, False, True)
    
    print("Clowns drawn")
    
    # Wendigo function
    def draw_wendigo_silhouette(x, y, scale):
        shadow = (8, 8, 12)
        draw.polygon([(x - 12*scale, y), (x - 18*scale, y + 55*scale), (x - 8*scale, y + 75*scale),
                      (x + 8*scale, y + 75*scale), (x + 18*scale, y + 55*scale), (x + 12*scale, y)], fill=shadow)
        draw.ellipse([x - 10*scale, y - 38*scale, x + 10*scale, y - 3*scale], fill=shadow)
        draw.line([x - 6*scale, y - 32*scale, x - 28*scale, y - 65*scale], fill=shadow, width=2)
        draw.line([x + 6*scale, y - 32*scale, x + 28*scale, y - 65*scale], fill=shadow, width=2)
        draw.ellipse([x - 4*scale, y - 24*scale, x - 1*scale, y - 19*scale], fill=(232, 232, 232))
        draw.ellipse([x + 1*scale, y - 24*scale, x + 4*scale, y - 19*scale], fill=(232, 232, 232))
    
    draw_wendigo_silhouette(int(width * 0.43), int(height * 0.26), 0.55)
    draw_wendigo_silhouette(int(width * 0.57), int(height * 0.23), 0.45)
    
    print("Wendigos drawn")
    
    # Flickering carnival lights
    random.seed(666)
    light_positions = [(int(width * 0.12), int(height * 0.32)), 
                       (int(width * 0.88), int(height * 0.28)),
                       (int(width * 0.35), int(height * 0.22))]
    
    for lx, ly in light_positions:
        draw.ellipse([lx - 12, ly - 12, lx + 12, ly + 12], fill=(255, 150, 50))
        for radius in range(90, 20, -15):
            intensity = random.randint(180, 230)
            draw.ellipse([lx - radius, ly - radius, lx + radius, ly + radius], 
                        fill=(intensity, int(intensity * 0.4), 0))
    
    print("Lights drawn")
    
    # Atmospheric fog
    fog_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    fog_draw = ImageDraw.Draw(fog_layer)
    
    random.seed(42)
    for y_pos in range(int(height * 0.65), height):
        fog_density = (y_pos - height * 0.65) / (height * 0.35)
        for x_pos in range(0, width, 4):
            if random.random() < fog_density * 0.2:
                alpha = int(20 + random.randint(0, 30) * fog_density)
                fog_draw.point((x_pos, y_pos), fill=(100, 110, 130, alpha))
    
    for _ in range(200):
        x_pos = random.randint(0, width - 1)
        y_pos = random.randint(0, int(height * 0.75))
        particle_size = random.randint(1, 2)
        fog_draw.ellipse([x_pos, y_pos, x_pos + particle_size, y_pos + particle_size],
                        fill=(random.randint(120, 200), random.randint(100, 180), 
                              random.randint(80, 160), random.randint(15, 45)))
    
    img = Image.alpha_composite(img, fog_layer)
    print("Fog added")
    
    # Vignette effect
    vignette_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    vignette_draw = ImageDraw.Draw(vignette_layer)
    
    for i in range(130):
        alpha = int(i * 1.3)
        vignette_draw.line([(i, 0), (i, height)], fill=(0, 0, 0, alpha))
        vignette_draw.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, alpha))
        vignette_draw.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))
        vignette_draw.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, alpha))
    
    img = Image.alpha_composite(img, vignette_layer)
    print("Vignette added")
    
    # God rays from top
    ray_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    ray_draw = ImageDraw.Draw(ray_layer)
    
    for i in range(12):
        angle = (i - 6) * 0.06
        x_end_left = int(width//2 + math.tan(angle - 0.02) * height) - 20
        x_end_right = int(width//2 + math.tan(angle + 0.02) * height) + 20
        ray_draw.polygon([(width//2, 0), (x_end_left, height), (x_end_right, height)],
                        fill=(255, 200, 100, 3))
    
    img = Image.alpha_composite(img, ray_layer)
    print("God rays added")
    
    # Save as JPEG
    final_img = img.convert('RGB')
    final_img.save(output, "JPEG", quality=95, optimize=True, progressive=True)
    
    file_size = os.path.getsize(output)
    print(f"\n=== SUCCESS ===")
    print(f"Hero image generated: {output}")
    print(f"Dimensions: {width}x{height}")
    print(f"File size: {file_size // 1024} KB ({file_size} bytes)")
    print(f"Style: Horror carnival, on-rails mine cart, clowns and wendigos")
    
except ImportError as e:
    print(f"ERROR: PIL not available - {e}")
    import sys
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    import sys
    sys.exit(1)