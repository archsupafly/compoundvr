#!/usr/bin/env python3
"""
Metroid VR Hero Image Generator - Planet Zebes Environment
Generates a 16:9 environment-only image for CompoundVR article

IMPORTANT: This image contains NO game name, NO VR references, NO people, NO characters.
It only depicts the atmospheric underground caverns of Planet Zebes.

Run this script to generate: python3 metroid-vr-hero-gen.py
"""
import os
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

# Configuration
API_KEY_FILE = "/home/antforce/.hermes/profiles/maya/.env"
OUTPUT_PNG = "/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.png"
OUTPUT_JPG = "/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.jpg"

# Environment-only prompt for Planet Zebes (NO game name, NO VR, NO characters, NO people)
# This describes ONLY the atmospheric environment
PROMPT = """Ancient alien underground cavern system with rocky geological formations, vertical shafts descending into darkness, crystalline structures embedded in cave walls, atmospheric glow from bioluminescent elements and distant magma, ancient ruined architecture seamlessly integrated into natural rock formations, mysterious doorways carved from stone, deep navy shadows with muted amber and cyan accent lighting emanating from energy sources, cinematic editorial photography, moody atmospheric style, sophisticated documentary composition, high detail, professional concept art quality, deep sense of isolation and descent through underground tunnels, NO text overlays, NO titles, NO subtitles, NO UI elements, NO watermarks, NO logos, NO person, NO characters, NO figures, NO headset, NO controllers, NO floating tech elements, NO promotional graphics, NO text of any kind"""

def get_api_key():
    """Extract GEMINI_API_KEY from Maya's .env file"""
    if not Path(API_KEY_FILE).exists():
        raise FileNotFoundError(f"API key file not found: {API_KEY_FILE}")
    
    with open(API_KEY_FILE) as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                key = line.split("=", 1)[1].strip()
                # Remove any trailing quotes or comments
                key = key.split('#')[0].strip().strip('"').strip("'")
                return key
    
    raise ValueError("GEMINI_API_KEY not found in .env file")

def generate_image():
    """Generate hero image using Gemini Imagen API"""
    print("=" * 60)
    print("METROID VR HERO IMAGE GENERATOR")
    print("Style: Planet Zebes Underground Environment")
    print("=" * 60)
    
    # Get API key
    api_key = get_api_key()
    print(f"\nAPI Key: {api_key[:10]}...{api_key[-4:]}")
    
    # Prepare API request
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"
    
    payload = {
        "instances": [{"prompt": PROMPT}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9"}
    }
    
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers)
    
    print(f"\nPrompt ({len(PROMPT)} chars):")
    print(f"  {PROMPT[:100]}...")
    print(f"\nOutput: {OUTPUT_PNG}")
    print("Aspect: 16:9 (1920x1080)")
    print("\nCalling Gemini Imagen 4.0 API...")
    
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            result = json.loads(resp.read().decode())
        
        predictions = result.get("predictions", [])
        if not predictions:
            print("\nERROR: No predictions in response")
            print(json.dumps(result, indent=2))
            return False
        
        if "bytesBase64Encoded" not in predictions[0]:
            print("\nERROR: No image data in response")
            print(json.dumps(result, indent=2))
            return False
        
        # Decode and save image
        img_data = base64.b64decode(predictions[0]["bytesBase64Encoded"])
        
        # Ensure output directory exists
        Path(OUTPUT_PNG).parent.mkdir(parents=True, exist_ok=True)
        
        # Save PNG
        with open(OUTPUT_PNG, "wb") as f:
            f.write(img_data)
        
        size = Path(OUTPUT_PNG).stat().st_size
        print(f"\n✓ PNG saved: {OUTPUT_PNG}")
        print(f"  Size: {size:,} bytes ({size/1024:.1f} KB)")
        
        # Convert to JPG using pure Python (if PIL available) or note manual conversion
        try:
            from PIL import Image
            img = Image.open(OUTPUT_PNG)
            img = img.convert("RGB")  # Remove alpha for JPG
            img.save(OUTPUT_JPG, "JPEG", quality=90, optimize=True)
            jpg_size = Path(OUTPUT_JPG).stat().st_size
            print(f"\n✓ JPG saved: {OUTPUT_JPG}")
            print(f"  Size: {jpg_size:,} bytes ({jpg_size/1024:.1f} KB)")
        except ImportError:
            print(f"\n! PIL not available - PNG saved, manual JPG conversion needed")
            print(f"  Run: ffmpeg -i {OUTPUT_PNG} -q:v 3 {OUTPUT_JPG}")
        
        print("\n" + "=" * 60)
        print("SUCCESS: Hero image generated")
        print("=" * 60)
        return True
        
    except urllib.error.HTTPError as e:
        print(f"\n✗ HTTP Error {e.code}")
        print(e.read().decode())
        return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = generate_image()
    exit(0 if success else 1)