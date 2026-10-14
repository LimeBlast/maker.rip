---
author: daniel
layout: post
title: I just can't do it Captain, I just don't have the power!
date: '2016-08-05 17:08:00'
image: /assets/img/2016/08/photo-1441171205449-f600f908a9f3--1-.jpg
categories:
- the-makers-guide-to-the-zombie-apocalypse
---

<p class="intro"><span class="dropcap">U</span>nfortunately, today has turned into a bit of a failure.</p>

This morning brought with it the final component I needed I start on the battery monitor project. At lunchtime, I quickly assembled the relevant bits and connected the battery...

...nothing!

One of the battery monitor's features is its ability to power it's Arduino component from the battery being tested - but of course, this only works if the battery in question has at least a trickle of power - it would appear that mine doesn't.

![](/assets/img/2016/08/voltchart1.gif)

I still don't fully understand the mechanisms behind this, but a battery's state of change is measured via its voltage output. On a 12-volt battery, a voltage of `12.6` is fully charged, while anything below `10.5` is empty.

Multimeter probes in hand, I measured the voltage on mine: `2.37`. This is severely under voltage, and I'd imagine probably beyond repair. I can't even get an LED to light up using it.

![](/assets/img/2016/08/IMG_20160805_142549282--1-.jpg)

Although I can't be sure, I think this is very possibly related to the broken charge controller I mentioned yesterday, and if nothing else, this is a hard-learned lesson about leaving unused batteries connected.

Checking back in with the Arduino for a moment, when supplied with power via the USB port it sprung into action and showed a reading of `4.34` on the display, while also making the buzzer sound off. This appears to be expected behaviour, as the script is set to activate the buzzer on anything less than `11.7` volts.

With a bit of tweaking to the Arduino, provided I maintain power via the USB, I think I can use this to measure the capacity of some 3-volt coin cells I have. I'll try that later today, and if I'm successful I'll post an update.

So what do I do now? Frankly, I'm a bit fed up with the idea of charging batteries (via solar, pedal, or even directly from the mains), so I think it might be time to invest in a bench power supply. I know nothing about them, but it appears models suitable for home enthusiast cost anywhere from about £50 to £100, which unfortunately means waiting for another payday.

But fear not, for I won't be spending the next month twiddling my thumbs  - instead, I'll see what I can make of the e-textile and circuit sticker goodies I have.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">My latest order of goodies from <a href="https://twitter.com/pimoroni">@pimoroni</a> had arrived. A bunch of e-textile and circuit sticker things to play with. <a href="https://t.co/Wb2ruZ7ec1">pic.twitter.com/Wb2ruZ7ec1</a></p>&mdash; Daniel Hollands (@LimeBlast) <a href="https://twitter.com/LimeBlast/status/761135549730156544">August 4, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
