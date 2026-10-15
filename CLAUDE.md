# maker.rip

Personal maker blog: Jekyll 4 with the Chirpy theme gem, deployed to GitHub Pages at https://maker.rip. README.md has the authoring guide; this file holds what the files don't say.

## Theme stays stock

Change the site through `_config.yml`, `_tabs/`, `_data/`, `assets/img/favicons/` and post content. Copying a theme file into the repo freezes it against Dependabot's theme updates, so do that only when the owner explicitly asks, and say so when you do. Chirpy's own front matter and includes (`image.alt`, `pin`, `embed/video.html` for self-hosted video) cover most needs; a plain `<iframe>` gets `class="embed-video"` for full-width 16:9. Fonts and JS are self-hosted from the `assets/lib` git submodule (`assets.self_host`), so pages load nothing from Google or jsDelivr. The one theme-path file here is `_includes/metadata-hook.html`, Chirpy's empty placeholder for extra `<head>` tags; it loads self-hosted Umami (renamed `omen.js`, so Chirpy's `analytics.umami` setting stays empty).

## Content rules (the deploy enforces the first two)

- Every image has descriptive alt text; header images use `image: {path, alt}`.
- Every link is `https://`. Dead external links go to the closest archive.org snapshot, else become plain text.
- `description:` under 160 characters, in the owner's first-person voice.
- Images live in `assets/img/YYYY/MM/`, filenames without brackets (Chirpy's JS writes unquoted CSS `url()`). Longest side 1600px, under 400KB, no EXIF (phone photos carry GPS); the deploy fails otherwise. `python3 bin/check-images.py --fix` resizes, re-encodes and strips in place (needs Pillow).
- Third-party media is credited on the About page (`_tabs/about.md`), with any changes noted.

## Privacy

`_tabs/privacy.md` lists every third party a page contacts; keep it true when content changes. Third-party embeds are click-to-load: `{% include youtube.html id title %}` (poster at `assets/img/youtube/ID.jpg`) or the generic `{% include click-to-load.html %}`, styled and scripted from `_includes/metadata-hook.html`. A plain iframe would contact the third party on page load. Chirpy's refactor-content wraps any `<img>` not immediately followed by `</a>` in a lightbox link, so the include's `<a>` holds only the `<img>`. Tweets are plain Markdown quotes linking to the original.

## URLs

Posts are `/:year/:month/:day/:title/` and link to each other that way. Category and tag pages are `/categories/x/` and `/tags/x/`; Chirpy hardcodes those, so internal links match them.

## Verify before pushing

Run what CI runs (`.github/workflows/pages-deploy.yml`): `python3 bin/check-images.py`, `JEKYLL_ENV=production bundle exec jekyll b` then `bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"`. Locally htmlproofer needs `LANG=en_GB.UTF-8 LC_ALL=en_GB.UTF-8` or it crashes on non-ASCII.

## Gotchas

- Root files without front matter are published verbatim; add repo-only files (like this one) to `exclude:` in `_config.yml`.
- `jekyll serve` ignores `_config.yml` edits until restarted, and a running server rewrites `_site` over a separate `jekyll build`.
- The starter's git-lastmod plugin was removed on purpose: the 2026 import commits would label every old post "Updated".
- `Gemfile.lock` is committed with Linux platforms for CI; Dependabot groups gem and Actions updates weekly.
- DNS for maker.rip is at OVH and also carries Proton Mail records (MX, SPF, DKIM, verification TXT); keep those intact when editing the zone.
