#!/usr/bin/env python3
"""Fail if any image under assets/img is oversized or carries metadata; --fix shrinks and strips in place.

Limits: longest side 1600px, 400KB, no EXIF. Needs Pillow (pip install pillow).
"""
import pathlib
import sys

from PIL import Image, ImageOps

MAX_PX, MAX_BYTES = 1600, 400_000
ROOT = pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'img'
# ponytail: favicons are generated at fixed sizes, leave them alone
SKIP = {ROOT / 'favicons'}

fix = '--fix' in sys.argv
bad = []
for f in sorted(ROOT.rglob('*')):
    if not f.is_file() or f.suffix.lower() not in ('.jpg', '.jpeg', '.png') or any(s in f.parents for s in SKIP):
        continue
    im = Image.open(f)
    problems = []
    if max(im.size) > MAX_PX:
        problems.append(f'{im.size[0]}x{im.size[1]}')
    if f.stat().st_size > MAX_BYTES:
        problems.append(f'{f.stat().st_size // 1024}KB')
    if im.getexif():
        problems.append('exif')
    if not problems:
        continue
    if fix:
        im = ImageOps.exif_transpose(im)
        im.thumbnail((MAX_PX, MAX_PX))
        if f.suffix.lower() == '.png':
            im.save(f, 'PNG', optimize=True)
        else:
            im = im.convert('RGB')
            # ponytail: step quality down, then size, until it fits; good enough for a blog
            for px, q in ((MAX_PX, 85), (MAX_PX, 80), (MAX_PX, 75), (1200, 80)):
                im.thumbnail((px, px))
                im.save(f, 'JPEG', quality=q, optimize=True, progressive=True)
                if f.stat().st_size <= MAX_BYTES:
                    break
        print(f'fixed {f.relative_to(ROOT.parent.parent)} ({", ".join(problems)})')
    else:
        bad.append(f'{f.relative_to(ROOT.parent.parent)}: {", ".join(problems)}')

if bad:
    print('\n'.join(bad))
    print(f'\n{len(bad)} image(s) over {MAX_PX}px / {MAX_BYTES // 1000}KB or with EXIF. Run: python3 bin/check-images.py --fix')
    sys.exit(1)
print('images ok')
