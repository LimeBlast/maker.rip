# maker.rip

Jekyll blog using the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme (based on [chirpy-starter](https://github.com/cotes2020/chirpy-starter)).
Posts imported from [2019-06-02.maker.limeblast.co.uk](https://github.com/LimeBlast/2019-06-02.maker.limeblast.co.uk).

```bash
git clone --recurse-submodules git@github.com:LimeBlast/maker.rip.git   # or, in an existing clone: git submodule update --init
bundle install
bundle exec jekyll serve --livereload
```

Fonts and scripts are self-hosted from the `assets/lib` submodule ([chirpy-static-assets](https://github.com/cotes2020/chirpy-static-assets)); Dependabot keeps it updated.

Pushing to `main` builds, link-checks and deploys to https://maker.rip via GitHub Actions (about 30 seconds).

## Writing a post

Create `_posts/YYYY-MM-DD-slug.md`. The filename sets the date and the URL (`/YYYY/MM/DD/slug/`).

```markdown
---
title: Post title
description: "One sentence for the homepage card and search results, under 160 characters."
image:
  path: /assets/img/2026/10/header.jpg
  alt: "What the photo shows"
categories:
- personal
tags:
- some-tag
---

Body in Markdown.

![What the photo shows](/assets/img/2026/10/photo.jpg)
_Optional caption, in italics on the line straight after the image_

{% include youtube.html id='VIDEO_ID' title="Video title" %}
```

- **Images** go in `assets/img/YYYY/MM/`. Header images work best around 1200×630. Shrink phone photos and strip their metadata (it includes GPS) before committing, and avoid brackets in filenames.
- **Every image needs alt text** and **every link must be `https://`**: the deploy's link check fails otherwise. Details show in the repo's Actions tab.
- **Categories** in use: `personal`, `weekend-woodworker`, `wildcat`, `spooktober`, `other-builds`, `review`, `the-building-block`, `the-makers-guide-to-the-zombie-apocalypse`. New ones get a page automatically.
- **YouTube and other embeds load only when clicked**, so no third party sees a page view and no consent banner is needed. For YouTube, save `https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg` as `assets/img/youtube/VIDEO_ID.jpg` and use the include above. Anything else (e.g. Tinkercad): `{% include click-to-load.html service="Tinkercad" src="<iframe URL>" href="<page URL>" poster="/assets/img/…" title="…" %}`.
- `pin: true` keeps a post at the top of the homepage.
- A post dated in the future stays hidden until a rebuild after that date.

**Drafts:** unfinished posts live in `_drafts/slug.md` (no date) and never deploy. [jekyll-compose](https://github.com/jekyll/jekyll-compose) handles the filenames and dates:

```bash
bundle exec jekyll draft "Post title"              # new draft with the front matter above, minus image
bundle exec jekyll serve --drafts --livereload     # preview drafts alongside posts
bundle exec jekyll publish _drafts/post-title.md   # move to _posts/ dated today, then commit and push
bundle exec jekyll unpublish _posts/YYYY-MM-DD-post-title.md   # back to drafts
```

Add the `image:` block only once you have a photo; left blank, it renders a broken image and fails the deploy check.

In VS Code the same steps are tasks (Terminal → Run Task): **New draft** and **New post** (prompt for a title), **Serve with drafts**, **Publish open draft** and **Unpublish open post** (act on the file in the active editor), and **Check** (the deploy's build and link check, run locally). Titles become the filename and URL, with apostrophes turned into hyphens (`Daniel's` → `daniel-s`); rename the file before publishing if that matters.

**Without a local setup:** press `.` on the GitHub repo page to edit in the browser. Committing there deploys too, without a preview.

## Other pages and settings

- Sidebar pages (Archives, Privacy, …): `_tabs/`. Keep each file's front matter; it sets the icon and order.
- Site settings: `_config.yml` (restart `jekyll serve` after changing it). Sidebar contact icons: `_data/contact.yml`.
- Analytics: self-hosted Umami at https://pythia.limeblast.co.uk, loaded by `_includes/metadata-hook.html` on production builds only.
- Favicons: `assets/img/favicons/`, cut from the Maker.RIP sticker (the logo, `assets/img/logo.png`).
- The theme is used stock, so updates stay drop-in: Dependabot opens a weekly PR for gem and Actions updates. To change a theme file anyway, copy it from `bundle info --path jekyll-theme-chirpy` into the same path here, knowing it stops receiving theme updates.
