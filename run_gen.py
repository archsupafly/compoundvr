#!/usr/bin/env python3
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "/home/antforce/compoundvr-project/scripts/generate_until_dawn_hero.py"],
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
sys.exit(result.returncode)