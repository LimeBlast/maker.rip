---
author: daniel
layout: post
title: Securing the perimeter
date: '2016-10-01 21:37:00'
image: /assets/img/2016/10/pexels-photo-179993--1-.jpg
categories:
- the-makers-guide-to-the-zombie-apocalypse
---

<p class="intro"><span class="dropcap">J</span>ust a quickie, this time, to let you know I've finally completed Project 6: PIR Zombie Detector.</p>

I'm not exactly sure what I did wrong the last time, although it's a safe bet that I probably fried the Arduino via too much current. Determined to not do it again, I was very careful to set the upper voltage of my power supply to `12.6v`.

Next, I attached the PIR sensor to the screw shield. The PIR sensor works by detecting changes in infrared light (aka body heat), upon which it sends a `high` signal to be interpreted by the Arduino as a zombie incursion.

The book suggests using a long telephone wire to position the PIR sensor outside the base (it's not a very good detector if it doesn't inform you of the intrusion until they're in the same room as you), but for my testing purposes, I'm happy with it just sitting on the table.

![](/assets/img/2016/10/WhatsApp-Image-2016-09-29-at-8-32-26-PM--1-.jpeg)

Finally, I compiled the sketch provided by the book, flashed it onto the Arduino, and connected the power. The display told me my battery was full, so I adjusted the power supply up and down and watched meter move up and down in accordance.

But then, as I was moving within the range of the PIR sensor, the buzzer went off as the display flashed `ZOMBIES!`. I stayed still for a few seconds, waiting for the sensor to return to normal, then waved my hand over it again - `ZOMBIES!`.

The book itself mentions that it's debatable whether a PIR sensor would be of any use as a zombie detector, as it relies on detecting heat to work, something a zombie's corpse body won't have - but justifies using one anyway as the movement of the body will generate a small amount of heat via friction, which will hopefully be enough to register.

Anyway, I don't my shed yet, but once I do, I can see myself using the PIR sensor as a girlfriend detector, as she walks up the garden path to fetch me for the washing up.
