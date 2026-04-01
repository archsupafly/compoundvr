#!/bin/bash
cd /home/antforce/compoundvr-project
.venv/bin/pip install requests pillow -q 2>&1
.venv/bin/python3 scripts/gen_hero_now.py 2>&1