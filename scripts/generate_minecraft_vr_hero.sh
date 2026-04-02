#!/bin/bash
# Generate Minecraft VR hero image using Gemini Imagen API
# Editorial documentary style - NO VR gimmicks, NO circular lens effect

# Load API key
API_KEY=$(grep GEMINI_API_KEY ~/.hermes/profiles/maya/.env | cut -d'=' -f2)

if [ -z "$API_KEY" ]; then
    echo "ERROR: No GEMINI_API_KEY found"
    exit 1
fi

echo "API Key found: ${API_KEY:0:10}..."
echo ""

# Prompt for Minecraft VR - Editorial documentary style, NO VR gimmicks
PROMPT='Blocky voxel landscape at golden hour, sweeping view across a vast Minecraft world. Atmospheric volumetric fog rolls through a valley between blocky mountains. Deep navy sky transitions to cyan and amber bands at the horizon. In the foreground, a first-person view of a players blocky hand reaching toward a crafting table. No UI, no text, no HUD.

The scene captures the transformative feeling of standing inside Minecraft in VR - genuine sense of scale with 1-meter blocks towering above. Volumetric lighting streams through blocky tree canopies. Dramatic shadows and atmospheric haze. A distant village silhouette with torchlight flickering.

Color palette: Deep navy (#0b1020) shadows, warm amber (#d97706) from setting sun, cyan accents (#6ee7ff) in distant water and sky gradients. Lifted blacks, cinematic film-like grading, reduced saturation.

Style: Editorial documentary photography, Wired magazine feature cover, atmospheric landscape photography. Cinematic 16:9 wide composition. Think in-game screenshot from a moody, atmospheric Minecraft world - NOT a marketing render, NOT a VR gimmick.

CRITICAL REQUIREMENTS:
- Full-frame landscape filling the entire 1920x1080 canvas edge-to-edge with visual content
- NO circular VR lens effect, NO VR viewport overlay, NO black letterboxing, NO black bars
- NO stereoscopic side-by-side view
- NO tech circles, NO sci-fi interface elements, NO promotional graphics
- Think: atmospheric screenshot, not VR demonstration
- Cinematic documentary still, not YouTube thumbnail, not VR marketing image
- No text, no logos, no watermarks, no game UI overlays
- Photorealistic rendering of voxel aesthetic, volumetric fog, atmospheric depth
- Editorial magazine quality - sophisticated, moody, contemplative
- First-person perspective that implies VR immersion WITHOUT literal VR viewport gimmicks'

# Create JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "instances": [
    {
      "prompt": $(echo "$PROMPT" | python3 -c 'import json, sys; print(json.dumps(sys.stdin.read()))')
    }
  ],
  "parameters": {
    "sampleCount": 1,
    "aspectRatio": "16:9"
  }
}
EOF
)

# API endpoint
URL="https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=$API_KEY"

echo "Generating Minecraft VR hero image with Gemini Imagen..."
echo "Style: Editorial documentary, NO VR gimmicks"
echo ""

# Make API request
RESPONSE=$(curl -s -X POST \
    -H "Content-Type: application/json" \
    -d "$JSON_PAYLOAD" \
    "$URL")

# Check for errors
if echo "$RESPONSE" | grep -q "error"; then
    echo "API Error:"
    echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
    exit 1
fi

# Extract base64 image data
IMAGE_B64=$(echo "$RESPONSE" | python3 -c "import json, sys; data = json.load(sys.stdin); print(data['predictions'][0]['bytesBase64Encoded'])" 2>/dev/null)

if [ -z "$IMAGE_B64" ]; then
    echo "ERROR: No image data in response"
    echo "$RESPONSE"
    exit 1
fi

# Output path
OUTPUT_PATH="/home/antforce/compoundvr-project/public/images/games/minecraft-vr-hero.jpg"
mkdir -p "$(dirname "$OUTPUT_PATH")"

# Decode and save image
echo "$IMAGE_B64" | base64 -d > "$OUTPUT_PATH"

# Verify
if [ -f "$OUTPUT_PATH" ]; then
    FILESIZE=$(stat -f%z "$OUTPUT_PATH" 2>/dev/null || stat -c%s "$OUTPUT_PATH")
    echo "SUCCESS: Saved Minecraft VR hero to $OUTPUT_PATH"
    echo "File size: $(( FILESIZE / 1024 )) KB"
    echo "Style: Full-frame editorial documentary, no VR gimmicks"
    echo ""
    echo "Image generated following style guide:"
    echo "  - NO circular VR lens/viewport effect"
    echo "  - NO black letterboxing"
    echo "  - Full 16:9 frame with visual content edge-to-edge"
    echo "  - Editorial documentary photography style"
else
    echo "ERROR: Failed to save image"
    exit 1
fi