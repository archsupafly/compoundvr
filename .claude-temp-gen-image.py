#!/usr/bin/env python3
"""Generate Subnautica VR hero image using Gemini 2.5 Flash Image."""

import os
from google import genai
from google.genai import types

def main():
    # Initialize client
    client = genai.Client()
    
    # Output path
    output_path = "/home/archangel/.openclaw/workspace/projects/vr-modding-flat-games/assets/images/games/subnautica-vr-hero.png"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Prompt for Subnautica VR hero image
    prompt = """Cinematic underwater scene for Subnautica VR game. Deep ocean atmosphere with dark navy blue tones (#0b1020) dominating the composition. Subtle cyan (#6ee7ff) bioluminescent light accents from alien underwater flora and distant lights. Small silhouette of a futuristic submarine or underwater vehicle visible in the deep background, creating scale and mystery. Volumetric light rays filtering down from surface above. Marine particles and snow floating in water catching light. Sense of isolation, wonder, and deep ocean immersion. Technical, engineered aesthetic suitable for a VR gaming editorial website. No characters, no text overlays, no bright tropical colors. Mysterious and atmospheric."""
    
    # Generate image
    print("Generating image with Gemini 2.5 Flash Image...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["image", "text"]
        ),
    )
    
    # Save generated image
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            print(f"Saving image to {output_path}")
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            print(f"Image saved successfully!")
            return
    
    print("No image data found in response")
    return 1

if __name__ == "__main__":
    exit(main() or 0)
