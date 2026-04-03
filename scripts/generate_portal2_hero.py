#!/usr/bin/env python3
"""
Portal 2 VR Hero Image Generator for CompoundVR
Uses Gemini Imagen 4.0 API - Pure stdlib (no dependencies)

Game: Portal 2 (2011)
Article: /home/antforce/compoundvr-project/editorial/drafts/portal-2-feature-draft.md
Output: /home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg

COMPOUNDVR HERO IMAGE STYLE GUIDE COMPLIANCE:
- NO text, NO game name, NO "VR" label
- NO people, NO characters, NO silhouettes
- Environment/atmosphere ONLY
- Aperture Science test chambers, sterile white environments
- Orange/blue portal colors, industrial science facility aesthetic
- "Moment of wonder" - evocative atmosphere
- 16:9 aspect ratio
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
    print("Portal 2 VR Hero Image Generator")
    print("CompoundVR - Aperture Science Environment Focus")
    print("=" * 60)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        sys.exit(1)
    
    # Output path
    output_path = Path("/home/antforce/compoundvr-project/public/images/games/portal-2-vr-hero.jpg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # ================================================================
    # PROMPT CONSTRUCTION
    # Following CompoundVR style guide:
    # - NO text, game name, VR label
    # - NO people, characters, silhouettes
    # - Environment/atmosphere ONLY
    # - Aperture Science test chambers, sterile white
    # - Orange/blue portal colors, industrial aesthetic
    # - "Moment of wonder" - evocative atmosphere
    # ================================================================
    prompt = """Photorealistic cinematic 16:9 wide photograph of a pristine Aperture Science test chamber interior. Sterile white walls with subtle panel lines and clean geometric architecture. A large glowing orange portal on one pristine white wall, its surface shimmering with energy, and a matching blue portal portal visible on a distant platform. The portals create impossible geometry - looking through one reveals a completely different part of the facility. Industrial science facility aesthetic with recessed lighting, clean surfaces, and hints of advanced technology.

Deep atmospheric perspective showing multiple levels of the test chamber, with catwalks, platforms, and glass panels creating architectural depth. Subtle cyan accent lighting reflecting off white surfaces. Clean editorial photography style, magazine cover quality. The sense of spatial puzzle and discovery - a moment of wonder.

Technical details: Cool white and soft gray color palette with vibrant orange and blue portal glows providing contrasting focal points. Soft shadows, even lighting. Minimalist industrial design with hints of corporate science facility. High detail, photorealistic. No visible humans, no characters, no silhouettes, no robots, no turrets, no companions. Pure environmental scene. No text, no writing, no letters, no numbers, no logos, no watermarks, no game interface, no VR equipment, no headsets, no promotional graphics. Editorial documentary atmosphere, calm and mysterious. The quiet moment before a test begins."""

    print(f"\nPrompt ({len(prompt)} chars):")
    print(f"  Aperture Science test chamber environment")
    print(f"  Orange/blue portal colors")
    print(f"  Sterile white industrial aesthetic")
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