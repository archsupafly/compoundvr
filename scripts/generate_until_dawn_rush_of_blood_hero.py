#!/usr/bin/env python3
# Until Dawn: Rush of Blood Hero Image Generator
# Generates a 1920x1080 JPG featuring horror carnival atmosphere
# Key elements: mine cart track, tunnel, clowns, wendigos, fog

from PIL import Image, ImageDraw
import math, os, random

def main():
    width, height = 1920, 1080
    output_path = "/home/antforce/compoundvr-project/public/images/games/until-dawn-rush-of-blood-hero.jpg"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create base image
    img = Image.new('RGB', (width, height), (8, 12, 24))
    draw = ImageDraw.Draw(img)
    
    # Gradient background
    for y in range(height):
        r, g, b = 8 + int(7 * y/height), 12 + int(9 * y/height), 24 + int(16 * y/height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Convert for transparency effects
    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)
    
    # Draw mine cart track
    for i in range(50):
        p = i / 50.0
        y1 = int(height * (0.92 - p * 0.62))
        y2 = int(height * (0.95 - p * 0.62))
        tw = 280 * (1 - p * 0.85)
        b = 25 + int(18 * p)
        draw.rectangle([width//2 - tw, y1, width//2 + tw, y2], fill=(b, b, b + 8))
        for s in [-1, 1]:
            rx = width//2 + s * (tw - 5)
            rb = 50 + int(25 * (1 - p))
            draw.rectangle([rx - 2, y1, rx + 2, y2], fill=(rb, rb - 5, rb + 15))
    
    # Draw tunnel entrance
    tx, ty, tw, th = width//2, int(height * 0.12), 380, int(height * 0.32)
    for d in range(10, -1, -1):
        o, dark = d * 4, 10 + d * 2
        arch = [(tx - tw//2 + o, ty + th), (tx - tw//2 + o, ty + th*0.35 - o//10),
               (tx - tw//4 + o//2, ty + o//3), (tx, ty - th*0.12 + o//4),
               (tx + tw//4 - o//2, ty + o//3), (tx + tw//2 - o, ty + th*0.35 - o//10),
               (tx + tw//2 - o, ty + th)]
        draw.polygon(arch, fill=(dark, dark, dark + 5))
    draw.ellipse([tx - 35, ty - 25, tx + 35, ty + 15], fill=(50, 0, 0))
    
    # Draw clowns (menacing figures with glowing orange eyes)
    def clown(x, y, sc, fr, dist):
        if not fr: x = int(x - 45 * sc)
        bc = (25, 25, 30) if dist else (35, 35, 42)
        draw.ellipse([x - 35*sc, y - 65*sc, x + 35*sc, y + 45*sc], fill=bc)
        hy = int(y - 55 * sc)
        draw.ellipse([x - 28*sc, hy - 32*sc, x + 28*sc, hy + 32*sc], fill=(18, 18, 22))
        ey = hy - 5
        es = max(6, int(7 * sc))
        if not dist: draw.ellipse([x - 20*sc, ey - 12, x + 20*sc, ey + 12], fill=(200, 80, 20))
        draw.ellipse([x - 14*sc, ey - es//2, x - 6*sc, ey + es//2], fill=(255, 107, 53))
        draw.ellipse([x + 6*sc, ey - es//2, x + 14*sc, ey + es//2], fill=(255, 107, 53))
        if not dist: draw.arc([x - 18*sc, hy + 8, x + 18*sc, hy + 28*sc], 0, 180, fill=(255, 107, 53), width=3)
    
    clown(int(width * 0.22), int(height * 0.58), 1.35, True, False)
    clown(int(width * 0.80), int(height * 0.42), 0.85, False, True)
    
    # Draw wendigos (tall, emaciated, antlered silhouettes)
    def wendigo(x, y, sc):
        c = (8, 8, 12)
        draw.polygon([(x - 12*sc, y), (x - 18*sc, y + 55*sc), (x - 8*sc, y + 75*sc),
                     (x + 8*sc, y + 75*sc), (x + 18*sc, y + 55*sc), (x + 12*sc, y)], fill=c)
        draw.ellipse([x - 10*sc, y - 38*sc, x + 10*sc, y - 3*sc], fill=c)
        draw.line([x - 6*sc, y - 32*sc, x - 28*sc, y - 65*sc], fill=c, width=2)
        draw.line([x + 6*sc, y - 32*sc, x + 28*sc, y - 65*sc], fill=c, width=2)
        draw.ellipse([x - 4*sc, y - 22*sc, x - 1*sc, y - 17*sc], fill=(232, 232, 232))
        draw.ellipse([x + 1*sc, y - 22*sc, x + 4*sc, y - 17*sc], fill=(232, 232, 232))
    
    wendigo(int(width * 0.43), int(height * 0.26), 0.55)
    wendigo(int(width * 0.57), int(height * 0.23), 0.45)
    
    # Carnival lights
    random.seed(666)
    for lx, ly in [(int(width * 0.12), int(height * 0.32)), 
                   (int(width * 0.88), int(height * 0.28)),
                   (int(width * 0.35), int(height * 0.22))]:
        draw.ellipse([lx - 12, ly - 12, lx + 12, ly + 12], fill=(255, 150, 50))
        for r in range(90, 20, -15):
            i = random.randint(180, 230)
            draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=(i, int(i * 0.4), 0))
    
    # Fog
    fog = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fog)
    random.seed(42)
    for y in range(int(height * 0.65), height):
        dens = (y - height * 0.65) / (height * 0.35)
        for x in range(0, width, 4):
            if random.random() < dens * 0.2:
                fd.point((x, y), fill=(100, 110, 130, int(20 + random.randint(0, 30) * dens)))
    for _ in range(200):
        x, y = random.randint(0, width-1), random.randint(0, int(height * 0.75))
        fd.ellipse([x, y, x + random.randint(1, 2), y + random.randint(1, 2)],
                   fill=(random.randint(120, 200), random.randint(100, 180), 
                         random.randint(80, 160), random.randint(15, 45)))
    img = Image.alpha_composite(img, fog)
    
    # Vignette
    vig = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vig)
    for i in range(130):
        a = int(i * 1.3)
        vd.line([(i, 0), (i, height)], fill=(0, 0, 0, a))
        vd.line([(width - i, 0), (width - i, height)], fill=(0, 0, 0, a))
        vd.line([(0, i), (width, i)], fill=(0, 0, 0, a))
        vd.line([(0, height - i), (width, height - i)], fill=(0, 0, 0, a))
    img = Image.alpha_composite(img, vig)
    
    # God rays
    ray = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    rd = ImageDraw.Draw(ray)
    for i in range(12):
        ang = (i - 6) * 0.06
        rd.polygon([(width//2, 0), 
                   (int(width//2 + math.tan(ang - 0.02) * height) - 20, height),
                   (int(width//2 + math.tan(ang + 0.02) * height) + 20, height)],
                  fill=(255, 200, 100, 3))
    img = Image.alpha_composite(img, ray)
    
    # Save
    img.convert('RGB').save(output_path, "JPEG", quality=95, optimize=True, progressive=True)
    
    print(f"SUCCESS: Generated Until Dawn: Rush of Blood hero image")
    print(f"Output: {output_path}")
    print(f"Dimensions: {width}x{height}")
    print(f"File size: {os.path.getsize(output_path) // 1024} KB")

if __name__ == "__main__":
    main()