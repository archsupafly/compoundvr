#!/usr/bin/env python3
"""
Resident Evil 4 VR Hero Image Generator for CompoundVR
Uses Gemini Imagen 4.0 API - Pure stdlib (no dependencies)

Game: Resident Evil 4 (Original 2005/2007)
Article: /home/antforce/compoundvr-project/editorial/drafts/resident-evil-4-vr-feature-draft.md
Output: /home/antforce/compoundvr-project/public/images/games/resident-evil-4-vr-hero.jpg

COMPOUNDVR STYLE GUIDE COMPLIANCE:
- NO text, NO game name, NO "VR" label
- NO people, NO characters, NO silhouettes
- Environment/atmosphere ONLY
- Spanish rural village, fog, gothic horror
- Editorial documentary style, desaturated, cinematic
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path


def load_api_key():
    """Get GEMINI_API_KEY from environment or .env file."""
    # Check environment first
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        print(f"Found key in env: {key[:4]}...{key[-3:]}")
        return key
    
    # Load from maya profile .env
    env_path = Path("/home/antforce/.hermes/profiles/maya/.env")
    if not env_path.exists():
        print(f"ERROR: {env_path} does not exist")
        return None
    
    content = env_path.read_text()
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("GEMINI_API_KEY="):
            key = line.split("=", 1)[1].strip()
            # Remove quotes if present
            if key.startswith('"') and key.endswith('"'):
                key = key[1:-1]
            if key.startswith("'") and key.endswith("'"):
                key = key[1:-1]
            print(f"Found key in .env: {key[:4]}...{key[-3:]}")
            return key
    
    print("ERROR: GEMINI_API_KEY not found in environment or .env")
    return None


def main():
    print("=" * 60)
    print("Resident Evil 4 VR Hero Image Generator")
    print("CompoundVR - Editorial Documentary Style")
    print("=" * 60)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        sys.exit(1)
    
    # Output path
    output_path = Path("/home/antforce/compoundvr-project/public/images/games/resident-evil-4-vr-hero.jpg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # ================================================================
    # PROMPT CONSTRUCTION
    # Following CompoundVR style guide:
    # - NO text, game name, VR label
    # - NO people, characters, silhouettes
    # - Environment/atmosphere ONLY
    # - Spanish rural village, fog, gothic horror
    # - Editorial documentary style, desaturated, cinematic
    # ================================================================
    prompt = """Photorealistic cinematic 16:9 wide photograph of an abandoned rural Spanish village at twilight during foggy evening. Ancient stone buildings with weathered wooden doors and wrought iron lanterns lining narrow winding cobblestone streets. Thick atmospheric fog rolling through the village creating mysterious depth and limited visibility. Ivy and moss growing on old stone walls. Spanish rural gothic horror atmosphere with deep shadows and muted earth tones of brown gray and faded green. Deep navy blue evening sky transitioning to gray fog in the distance. Warm amber lantern light casting glow through the mist. Desaturated editorial documentary photography style, magazine cover quality. Moody foreboding oppressive atmosphere of rural European horror. Environmental storytelling through architecture and atmospheric lighting. No people, no human figures, no silhouettes, no characters, no text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Pure atmospheric environmental scene only. Film-like cinematic color grading with lifted blacks."""
    
    print(f"\nPrompt ({len(prompt)} chars):")
    print(f"  Spanish rural village, fog, gothic horror")
    print(f"  Editorial documentary style")
    print(f"  NO people, NO text, NO VR elements")
    
    # Gemini Imagen 4.0 API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"
    
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9",
            "guidanceScale": 16.0
        }
    }
    
    print(f"\nCalling Gemini Imagen 4.0 API...")
    
    req_data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=req_data, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"\nHTTP ERROR {e.code}:")
        print(error_body[:500])
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"\nURL ERROR: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)
    
    # Parse response
    predictions = result.get("predictions", [])
    if not predictions:
        print(f"\nERROR: No predictions in response")
        print(json.dumps(result, indent=2)[:1000])
        sys.exit(1)
    
    pred = predictions[0]
    if "bytesBase64Encoded" not in pred:
        print(f"\nERROR: No image data in prediction")
        print(f"Keys: {list(pred.keys())}")
        sys.exit(1)
    
    # Decode and save
    image_data = base64.b64decode(pred["bytesBase64Encoded"])
    
    with open(output_path, "wb") as f:
        f.write(image_data)
    
    file_size = output_path.stat().st_size
    
    print(f"\n{'='*60}")
    print("SUCCESS")
    print(f"{'='*60}")
    print(f"Output: {output_path}")
    print(f"Size: {file_size / 1024:.1f} KB ({file_size:,} bytes)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()