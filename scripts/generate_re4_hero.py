#!/usr/bin/env python3
"""
Resident Evil 4 VR Hero Image Generator for CompoundVR
Pure stdlib - no external dependencies

Uses Gemini Imagen 4.0 API
Output: resident-evil-4-vr-hero.jpg
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path


def get_api_key():
    """Get API key from environment or .env files."""
    # Try environment first
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    
    # Try .env files
    env_paths = [
        Path("/home/antforce/.hermes/profiles/maya/.env"),
        Path("/home/antforce/.hermes/.env"),
    ]
    for env_path in env_paths:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
                    if key.startswith('"') and key.endswith('"'):
                        key = key[1:-1]
                    if key.startswith("'") and key.endswith("'"):
                        key = key[1:-1]
                    return key
    return None


def main():
    api_key = get_api_key()
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found")
        sys.exit(1)
    
    print(f"API Key: {api_key[:5]}...{api_key[-4:]}")
    
    output_path = Path("/home/antforce/compoundvr-project/public/images/games/resident-evil-4-vr-hero.jpg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # PROMPT: Spanish rural horror - NO people, NO text, NO VR
    prompt = """Cinematic 16:9 wide shot of an abandoned foggy rural Spanish village at twilight. Ancient stone buildings with weathered wooden doors and wrought iron lanterns along narrow winding cobblestone streets. Dense atmospheric fog rolling through the village creating mysterious depth. Ivy and moss on old stone walls. Gothic horror atmosphere with deep shadows and muted earth tones. Deep navy blue sky fading into gray fog. Warm amber lantern light cutting through mist. Editorial documentary photography style. Moody, foreboding, oppressive rural European horror environment. No people, no figures, no silhouettes, no characters, no text, no writing, no logos, no watermarks, no game UI, no VR equipment. Pure atmospheric environmental scene."""
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={api_key}"
    
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9",
            "guidanceScale": 16.0
        }
    }
    
    print("Calling Gemini API...")
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode(), 
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            result = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()[:500]}")
        sys.exit(1)
    
    predictions = result.get("predictions", [])
    if not predictions or "bytesBase64Encoded" not in predictions[0]:
        print(f"ERROR: No image data. Response: {json.dumps(result)[:500]}")
        sys.exit(1)
    
    img_data = base64.b64decode(predictions[0]["bytesBase64Encoded"])
    
    with open(output_path, "wb") as f:
        f.write(img_data)
    
    print(f"\nSUCCESS: {output_path}")
    print(f"File size: {output_path.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()