#!/usr/bin/env python3
"""Generate Dead Space hero image using Gemini API with Imagen 4."""

import os
import sys

# Get API key from environment
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    print("Error: GEMINI_API_KEY not set")
    sys.exit(1)

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
    
    client = genai.Client(api_key=api_key)
    
    prompt = """Cinematic hero image for Dead Space VR mod. Dark sci-fi horror atmosphere, Isaac Clarke in iconic engineering suit with glowing blue RIG health bar on spine, floating in zero gravity corridor of the USG Ishimura spaceship. Industrial sci-fi environment with metallic surfaces, emergency red lighting, and distant necromorph silhouettes. Cinematic composition, dramatic lighting with cyan accent glows on suit details and holographic UI elements. Clean, editorial style suitable for a technical gaming publication. High contrast, atmospheric fog, professional game photography aesthetic. No text, no logos."""
    
    # Use imagen-4.0-generate-001 which is available
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            output_mime_type='image/jpeg',
            aspect_ratio='16:9'
        )
    )
    
    output_path = "/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/site/public/images/games/dead-space-hero.jpg"
    
    for generated_image in response.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.save(output_path, 'JPEG', quality=95)
        print(f"Image saved to: {output_path}")
        sys.exit(0)
    
    print("No images generated")
    sys.exit(1)
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
