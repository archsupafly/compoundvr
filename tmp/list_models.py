#!/usr/bin/env python3
"""List available Gemini models."""

import os
import sys

api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    print("Error: GEMINI_API_KEY not set")
    sys.exit(1)

from google import genai

client = genai.Client(api_key=api_key)

print("Listing available models...")
models = client.models.list()
for model in models:
    print(f"  - {model.name}")
