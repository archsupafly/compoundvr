#!/usr/bin/env python3
"""List available Gemini models."""
import os
import json
import urllib.request

# Gemini API key - load from env or file
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    key_file = os.path.expanduser("~/.hermes/profiles/maya/.env")
    for line in open(key_file):
        if line.startswith("GEMINI_API_KEY="):
            api_key = line.strip().split("=", 1)[1]
            break

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
req = urllib.request.Request(url)
with urllib.request.urlopen(req, timeout=30) as response:
    data = json.loads(response.read().decode('utf-8'))

for model in data.get("models", []):
    name = model.get("name", "")
    if "imagen" in name.lower() or "image" in name.lower():
        print(f"{name}: {model.get('supportedGenerationMethods', [])}")