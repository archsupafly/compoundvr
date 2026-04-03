#!/bin/bash
# Generate Resident Evil 4 VR Hero Image
# Loads GEMINI_API_KEY from maya profile and runs generator

set -e

# Load environment
ENV_FILE="/home/antforce/.hermes/profiles/maya/.env"
if [ -f "$ENV_FILE" ]; then
    echo "Loading environment from $ENV_FILE"
    # Source the env file (export variables)
    set -a
    source "$ENV_FILE" 2>/dev/null || true
    set +a
fi

# Check API key is loaded
if [ -z "$GEMINI_API_KEY" ]; then
    echo "ERROR: GEMINI_API_KEY not found"
    exit 1
fi

echo "API Key loaded: ${GEMINI_API_KEY:0:4}...${GEMINI_API_KEY: -3}"

# Run the generator
echo ""
echo "Generating Resident Evil 4 VR hero image..."
python3 /home/antforce/compoundvr-project/scripts/generate_re4_hero_gemini.py