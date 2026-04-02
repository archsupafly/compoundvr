#!/usr/bin/env python3
"""Run the hero image generator directly with proper path setup."""
import subprocess
import sys

# Run the generator script
result = subprocess.run(
    [sys.executable, "/home/antforce/compoundvr-project/scripts/generate_until_dawn_hero.py"],
    cwd="/home/antforce/compoundvr-project",
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print("Return code:", result.returncode)
sys.exit(result.returncode)