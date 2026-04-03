#!/bin/bash
# Metroid VR Hero Image Generator
# Generates Planet Zebes environment image (NO game name, NO VR, NO characters)

# Set the API key from Maya's .env
export GEMINI_API_KEY=$(grep "^GEMINI_API_KEY=" /home/antforce/.hermes/profiles/maya/.env 2>/dev/null | cut -d'=' -f2- | tr -d '\r\n')

if [ -z "$GEMINI_API_KEY" ]; then
    echo "ERROR: GEMINI_API_KEY not found in /home/antforce/.hermes/profiles/maya/.env"
    exit 1
fi

echo "API Key: ${GEMINI_API_KEY:0:10}...${GEMINI_API_KEY: -4}"

# Environment-only prompt (NO game name, NO VR references, NO people, NO characters)
PROMPT='Ancient alien underground cavern system with rocky geological formations, vertical shafts descending into darkness, crystalline structures embedded in cave walls, atmospheric glow from bioluminescent elements and distant magma, ancient ruined architecture seamlessly integrated into natural rock formations, mysterious doorways carved from stone, deep navy shadows with muted amber and cyan accent lighting emanating from energy sources, cinematic editorial photography, moody atmospheric style, sophisticated documentary composition, high detail, professional concept art quality, deep sense of isolation and descent through underground tunnels, NO text overlays, NO titles, NO subtitles, NO UI elements, NO watermarks, NO logos, NO person, NO characters, NO figures, NO headset, NO controllers, NO floating tech elements, NO promotional graphics, NO text of any kind'

OUTPUT="/home/antforce/compoundvr-project/public/images/games/metroid-vr-hero.png"

echo ""
echo "Generating Metroid VR hero image..."
echo "Prompt length: ${#PROMPT} characters"
echo "Output: $OUTPUT"
echo "Aspect ratio: 16:9"
echo ""

# Run the generation script
python3 /home/antforce/.hermes/skills/creative/gemini-image-simple/scripts/generate.py "$PROMPT" "$OUTPUT" --aspect-ratio 16:9

EXITCODE=$?

if [ $EXITCODE -eq 0 ]; then
    echo ""
    echo "SUCCESS: Image generated"
    
    # Convert to JPG if needed (output is PNG from Gemini)
    if [ -f "$OUTPUT" ]; then
        # Check if ffmpeg is available for PNG to JPG conversion
        if command -v ffmpeg &> /dev/null; then
            JPG_OUTPUT="${OUTPUT%.png}.jpg"
            ffmpeg -y -i "$OUTPUT" -q:v 3 "$JPG_OUTPUT" 2>/dev/null
            if [ -f "$JPG_OUTPUT" ]; then
                echo "Converted to JPG: $JPG_OUTPUT"
                ls -la "$JPG_OUTPUT"
            fi
        else
            # List the PNG file
            ls -la "$OUTPUT"
        fi
    fi
else
    echo ""
    echo "FAILED: Generation failed with exit code $EXITCODE"
fi

exit $EXITCODE