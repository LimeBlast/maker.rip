---
author: daniel
layout: post
title: Learning from one's mistakes
date: '2016-09-01 19:25:32'
image: /assets/img/2016/09/mistakes--1-.jpg
categories:
- the-makers-guide-to-the-zombie-apocalypse
---

<p class="intro"><span class="dropcap">A</span>fter a number of failures with the other projects I've worked on recently, I was looking forward to a success with Project 3: LED Lights.</p>

How hard can it be to wire up some LEDs? [I've done it at least once before](/2016/08/07/you-light-up-my-heart/), so surely this project is the same thing - just with larger LEDs? Bash 3 LEDs into a parallel circuit with the bench power supply, add a fuse to stop things from exploding, jobs a good'un.

It turns out the fact they're larger, is in fact, a complicating factor. Had I properly read the instructions in the book, I would have noticed the suggested wattage for the bulbs was between 2 and 10 watts. As the bulbs in question were 50-watt, and the maximum current my bench power supply can output is 5 amps, they were far too hungry for their own good, resulting in the ability to fully light one individual bulb at a time, but with vastly reduced light output when trying to attach two or more.

With a single bulb attached, setting the power supply to exactly `12.0` volts, I get a current draw of `4.23` amps. This is pretty bright and generates a lot of heat. I can increase the voltage up to `16.4` volts before the current maxes out at `5.07` amps, which makes the bulb even brighter, but equally even hotter.

Adding a second bulb to the mix results in `5.2` volts being the maximum the power supply can give before maxing out the current. The light output of the two bulbs together is vastly lower than the single, which I guess is a result of the reduced voltage. A third bulb maxes out at `3.1` volts.

I'm not too upset by this outcome, however, as I feel that I've learnt something. I think I understood there was a correlation between voltage and current before, but this outcome fully demonstrates it. I think - I'm still a bit iffy about it all.

It also helps demonstrate that, while a 50-watt bulb can produce a lot of light, it will also cause the battery to run out far quicker, so a balancing of your requirements and resources is always needed.

Anyway, this isn't the end of this project, as I've just ordered some [10-watt MR16 bulbs](http://amzn.to/2c4xB9Z). I'm hoping that, with them being 1/5th of the wattage, I should be able run 5 of them at maximum without any issues.
