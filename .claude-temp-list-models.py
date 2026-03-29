#!/usr/bin/env python3
"""List available Gemini models."""

from google import genai

def main():
    client = genai.Client()
    
    print("Available models:")
    for model in client.models.list():
        print(f"  {model.name}")
        if hasattr(model, 'supported_generation_methods'):
            print(f"    Methods: {model.supported_generation_methods}")

if __name__ == "__main__":
    main()
