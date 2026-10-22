#!/usr/bin/env python3
"""Convert approved SMT PNG artwork to Windows/macOS resources (requires Pillow)."""
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
icons = root / 'assets/smt-icons'
for name in ('app', 'document'):
    with Image.open(icons / f'{name}.png') as source:
        source = source.convert('RGBA')
        source.save(icons / f'{name}.ico', sizes=[(s, s) for s in (16, 20, 24, 32, 40, 48, 64, 128, 256)])
        source.save(icons / f'{name}.icns')
        if name == 'app':
            source.resize((256, 256), Image.Resampling.LANCZOS).save(icons / 'app-256.png', optimize=True)
