# maker.rip

Jekyll blog using the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme (based on [chirpy-starter](https://github.com/cotes2020/chirpy-starter)).
Posts imported from [2019-06-02.maker.limeblast.co.uk](https://github.com/LimeBlast/2019-06-02.maker.limeblast.co.uk).

```bash
bundle install
bundle exec jekyll serve --livereload
```

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

<p class="intro">Opening line, styled as the intro.</p>

Body in Markdown.

![What the photo shows](/assets/img/2026/10/photo.jpg)
_Optional caption, in italics on the line straight after the image_

{% include embed/youtube.html id='VIDEO_ID' %}
```

- **Images** go in `assets/img/YYYY/MM/`. Header images work best around 1200×630. Shrink phone photos and strip their metadata (it includes GPS) before committing, and avoid brackets in filenames.
- **Every image needs alt text** and **every link must be `https://`**: the deploy's link check fails otherwise. Details show in the repo's Actions tab.
- **Categories** in use: `personal`, `weekend-woodworker`, `wildcat`, `spooktober`, `other-builds`, `review`, `the-building-block`, `the-makers-guide-to-the-zombie-apocalypse`. New ones get a page automatically.
- `pin: true` keeps a post at the top of the homepage.
- A post dated in the future stays hidden until a rebuild after that date.

**Drafts:** put unfinished posts in `_drafts/slug.md` (no date). They never deploy; preview them with `bundle exec jekyll serve --drafts`, then move to `_posts/` with a date to publish.

**Without a local setup:** press `.` on the GitHub repo page to edit in the browser. Committing there deploys too, without a preview.

## Other pages and settings

- Sidebar pages (About, Archives, …): `_tabs/`. Keep each file's front matter; it sets the icon and order.
- Site settings: `_config.yml` (restart `jekyll serve` after changing it). Sidebar contact icons: `_data/contact.yml`.
- Favicons: `assets/img/favicons/`. The zombie hand is [Raise zombie](https://game-icons.net/1x1/skoll/raise-zombie.html) by Skoll, CC BY 3.0, credited on the About page.
- The theme is used stock, so updates stay drop-in: Dependabot opens a weekly PR for gem and Actions updates. To change a theme file anyway, copy it from `bundle info --path jekyll-theme-chirpy` into the same path here, knowing it stops receiving theme updates.
