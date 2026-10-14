---
title: Wildcat is live (and angry)
date: '2018-11-19 21:27:24'
image: /assets/img/2018/11/IMG_20181119_202201--1-.jpg
categories:
- wildcat
tags:
- feather-huzzah
- tinkercad
---

<p class="intro">This is the third post in the <a href="/categories/wildcat/">Wildcat saga</a>, so if this is your first time reading this blog it might be worth catching up - to find out more about the antagonist of our story, start with <a href="/2018/11/09/introducing-apricat/">Introducing Apricat</a>, and to understand our approach to solving the problem (and one of the challenges I've encountered on the way), read <a href="/2018/11/10/project-wildcat-has-been-delayed/">Project Wildcat... has been delayed</a>.</p>

All caught up? Good. Because I'm happy to reveal that Wildcat is live.

<figure>
  <img src="/assets/img/2018/11/IMG_20181119_153753--1-.jpg" alt="IMG_20181119_153753--1-" loading="lazy">
</figure>

I spoke a little about the technical hardware and general software approach in my last post, so instead of rehashing that I'm simply going to supply a link to the [git repo for the project](https://github.com/LimeBlast/wildcat) which I'm hoping, combined with the diagram below, will be self explanatory:

<figure>
  <img src="/assets/img/2018/11/wildcat_bb.png" alt="wildcat_bb" loading="lazy">
</figure>

For this post I'm more interested in talking about the fabrication of the non-technical parts of the project, most of which were designed around a cat ear frame we found in HomeSense.

The front panel was designed in about an hour (based on some initial measurements of the frame and LEDs) using [Tinkercad](https://www.tinkercad.com/#/dashboard), then after 3D printing and realising that nothing fit, slightly refined into what you see below:

<figure>
  <iframe src="https://www.tinkercad.com/embed/2Vc65P0oUIG" title="Embedded content" loading="lazy" allowfullscreen></iframe>
</figure>

This second print fit perfectly, so was primed using [Rust-Oleum Surface Primer](https://amzn.to/2QUVWAt), expertly painted by Lucy using acrylics, then glued into the frame using [Gorilla glue](https://amzn.to/2BhsWO3).

The next problem was housing the electronics. Thankfully Adafruit provide a really cool system for printing [modular Feather cases](https://learn.adafruit.com/3d-printed-case-for-adafruit-feather/overview), of which I used a [tall variation](https://www.thingiverse.com/thing:2438577), allowing the stacking headers on my Huzzah to fit.

Before attaching the board into the case with some bolts, I removed the plastic housing from the female ends of a couple of jumper wires (so they'd also fit in the case), and slipped them into the pins of the header, wrapped them around the internal case mounts (to help stop them being tugged out) and lead them out the hole in the side, ready to be attached to the button.

<figure>
  <img src="/assets/img/2018/11/IMG_20181119_154303-cropped--1-.jpg" alt="IMG_20181119_154303-cropped--1-" loading="lazy">
</figure>

I could have soldered the jumper wires to the pins, which I'm sure would make them more secure, but one of my guiding principles with this build was the ability to disassemble everything easily if I wanted to salvage any of the electronics.

I wanted the button to be hidden but easily accessible, so using two strips of copper tape and some glue, I attached it to the back of the left ear, soldering the contacts to one end of the strips and the jumper wires to the other.

<figure>
  <img src="/assets/img/2018/11/IMG_20181119_154141--1-.jpg" alt="IMG_20181119_154141--1-" loading="lazy">
</figure>

The final bit of assembly was sticking the lid from the case module to the back of the front panel. Due to the size of the LED matrix there was a small gap between them when dry fitted, but half a [Command Strip](https://amzn.to/2A4xfKB) either side not only filled this gap nicely, but will allow me to easily separate the two if I need to.

<figure>
  <img src="/assets/img/2018/11/IMG_20181119_154020--1-.jpg" alt="IMG_20181119_154020--1-" loading="lazy">
</figure>

And that's the build. I asked Apricat what she thought of the project, and think the look she gave me summed it up:

<figure>
  <img src="/assets/img/2018/11/IMG_20181119_202416--2-.jpg" alt="IMG_20181119_202416--2-" loading="lazy">
</figure>

In truth, she had calmed down a lot before I even started making this project, and I think she's truly feeling at home with us. So of course this project isn't designed for punishment, instead it's just a bit of fun and an excuse to build something, because we really love Apricat, and know that when she does bite us, it's not aggressive, but instead just her playful way of showing she loves us.
