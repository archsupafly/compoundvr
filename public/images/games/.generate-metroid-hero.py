#!/usr/bin/env python3
"""
Metroid VR Hero Image Generator
Creates: /home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.jpg

Run with: python3 .generate-metroid-hero.py

This script generates a 16:9 environment-only image representing Planet Zebes.
NO game name, NO VR references, NO people, NO characters in the image.
"""
import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# Load API key from Maya's .env
ENV_FILE = "/home/antforce/.hermes/profiles/maya/.env"
OUTPUT_PNG = "/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.png"
OUTPUT_JPG = "/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.jpg"

# CRITICAL: Environment-only prompt (NO game name, NO VR, NO characters, NO people)
# This describes ONLY the atmospheric underground of Planet Zebes
PROMPT = """Ancient alien underground cavern system with rocky geological formations, vertical shafts descending into darkness, crystalline structures embedded in cave walls, atmospheric glow from bioluminescent elements and distant magma, ancient ruined architecture seamlessly integrated into natural rock formations, mysterious doorways carved from stone, deep navy shadows with muted amber and cyan accent lighting emanating from energy sources, cinematic editorial photography, moody atmospheric style, sophisticated documentary composition, high detail, professional concept art quality, deep sense of isolation and descent through underground tunnels, NO text overlays, NO titles, NO subtitles, NO UI elements, NO watermarks, NO logos, NO person, NO characters, NO figures, NO headset, NO controllers, NO floating tech elements, NO promotional graphics, NO text of any kind"""

def main():
    # Get API key
    api_key = None
    with open(ENV_FILE) as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
    
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found")
        return 1
    
    print(f"API Key: {api_key[:10]}...{api_key[-4:]}")
    print(f"\nPrompt: {PROMPT[:80]}...")
    print(f"\nOutput PNG: {OUTPUT_PNG}")
    print(f"Output JPG: {OUTPUT_JPG}")
    print(f"Aspect: 16:9 (1920x1080)")
    
    # Generate image via Gemini Imagen API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"
    
    payload = {
        "instances": [{"prompt": PROMPT}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9"}
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    
    print("\nCalling Gemini Imagen 4.0 API...")
    
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            result = json.loads(resp.read().decode())
        
        predictions = result.get("predictions", [])
        if not predictions or "bytesBase64Encoded" not in predictions[0]:
            print(f"ERROR: No image in response\n{json.dumps(result, indent=2)[:500]}")
            return 1
        
        # Save PNG
        img_data = base64.b64decode(predictions[0]["bytesBase64Encoded"])
        Path(OUTPUT_PNG).parent.mkdir(parents=True, exist_ok=True)
        
        with open(OUTPUT_PNG, "wb") as f:
            f.write(img_data)
        
        png_size = Path(OUTPUT_PNG).stat().st_size
        print(f"\n✓ PNG saved: {OUTPUT_PNG} ({png_size:,} bytes)")
        
        # Convert to JPG
        try:
            from PIL import Image
            img = Image.open(OUTPUT_PNG).convert("RGB")
            img.save(OUTPUT_JPG, "JPEG", quality=90, optimize=True)
            jpg_size = Path(OUTPUT_JPG).stat().st_size
            print(f"✓ JPG saved: {OUTPUT_JPG} ({jpg_size:,} bytes)")
        except ImportError:
            # Use ffmpeg if available
            import subprocess
            try:
                subprocess.run([
                    "ffmpeg", "-y", "-i", OUTPUT_PNG, "-q:v", "3", OUTPUT_JPG
                ], check=True, capture_output=True)
                jpg_size = Path(OUTPUT_JPG).stat().st_size
                print(f"✓ JPG saved: {OUTPUT_JPG} ({jpg_size:,} bytes)")
            except:
                print(f"! JPG conversion skipped - PNG is: {OUTPUT_PNG}")
        
        print("\n" + "="*50)
        print("SUCCESS: Hero image generated")
        print("="*50)
        return 0
        
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}:\n{e.read().decode()[:500]}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())