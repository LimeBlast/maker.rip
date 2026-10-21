#!/usr/bin/env python3
"""Fail if any image under assets/img is oversized or carries metadata; --fix shrinks and strips in place.

Limits: longest side 1600px, 400KB, no EXIF. Header images (image.path in a post) must also be
40:21, Chirpy's header frame, and at most 1200px wide; --fix leaves those alone, the crop needs an eye.
Needs Pillow (pip install pillow).
"""
import pathlib
import re
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
        if f.stat().st_size > MAX_BYTES:
            # ponytail: no auto PNG->JPEG, renaming breaks post references and drops transparency
            hint = '; convert to .jpg and update the posts that use it' if f.suffix.lower() == '.png' else ''
            bad.append(f'{f.relative_to(ROOT.parent.parent)}: still {f.stat().st_size // 1024}KB after fixing{hint}')
    else:
        bad.append(f'{f.relative_to(ROOT.parent.parent)}: {", ".join(problems)}')

# ponytail: front matter read by regex, matches the "image:\n  path:" form every post uses
SITE = ROOT.parent.parent
for post in sorted([*SITE.glob('_posts/*.md'), *SITE.glob('_drafts/*.md')]):
    m = re.search(r'^image:\s*\n\s+path:\s*["\']?([^"\'\s]+)', post.read_text(), re.M)
    if not m or not (SITE / m.group(1).lstrip('/')).is_file():
        continue
    w, h = Image.open(SITE / m.group(1).lstrip('/')).size
    if abs(w / h - 40 / 21) > 0.01 or w > 1200:
        bad.append(f'{m.group(1).lstrip("/")}: header for {post.name} is {w}x{h}; crop to 40:21, max 1200x630')

if bad:
    print('\n'.join(bad))
    if fix:
        print(f'\n{len(bad)} image(s) need fixing by hand.')
    else:
        print(f'\n{len(bad)} image problem(s). Run python3 bin/check-images.py --fix for size and EXIF; crop headers by hand.')
    sys.exit(1)
print('images ok')
