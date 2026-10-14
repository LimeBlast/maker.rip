---
title: "... and he said it was good"
description: "My Mad Scientist Light from the Instructables Electronics class: vintage filament bulbs on a wooden box, now switched by a Sonoff and Alexa."
date: '2017-09-30 15:31:15'
image:
  path: /assets/img/2017/09/photo-1440595228939-3673bdb622b4--1-.jpg
  alt: "Rows of bare filament bulbs hanging from brass holders"
categories:
- other-builds
tags:
- instructables
- alexa
- sonoff
---

I'm not sure why I've not spoken about this before, but back in June, after starting the [Electronics class on Instructables](https://www.instructables.com/Electronics-Class/), I completed my second large maker project: a [Mad Scientist Light](https://www.instructables.com/id/Build-a-Mad-Scientist-Light/#comment-CMMSLIYJ3EPQVMC).

![The finished Mad Scientist Light: three vintage filament bulbs on brass holders, mounted on a stained wooden box](/assets/img/2017/09/IMG_20170604_151522.jpg)

Unlike my [Halloween Box](/2017/02/09/my-halloween-box-isnt-four-months-late-its-eight-months-early/), I was determined to not only make the lamp functional - I wanted it to look good as well - something I don't consider the halloween box to be thanks to the leaking glue, issues with the laser cutter, and general incompetence on my part.

To this end, I knew that I wouldn't be able to build a pretty base box myself, so I decided to buy one from Etsy. I'd already purchased the [bulbs](https://www.amazon.co.uk/s?k=b22+vintage+filament+bulb) and [lamp holder battens](https://www.amazon.co.uk/dp/B01MRX3LV1) that I wanted, so I found a [friendly seller](https://www.etsy.com/uk/people/loulapworth) who was able to advise me what colour of stain and finish would look best with them, then built it for me.

Drilling the holes was the second most anxious part of the project because there would be no going back. Nevermind _measure twice, cut once_, this was more _measure four times, drill carefully_. The placement of the bulbs was mostly dictated by the box, as I had originally planned on placing them in a straight line along the middle, but the gap running down the middle meant this wasn't going to be possible.

![The top of the wooden lamp box, with holes drilled for the bulb holders](/assets/img/2017/09/IMG_20170527_120350--1-.jpg)

The _most_ anxious part was the wiring. Or more specifically, plugging it in after the wiring. This was my first mains voltage project, and could have gone horribly wrong in so many different ways. Because of this I wired each bulb in turn, testing for shorts with a continuity tester, then carefully plugging it to check that the bulb illuminated, before ensuring it was unplugged before moving onto the next bulb.

![The Mad Scientist Light switched on, its three filament bulbs glowing](/assets/img/2017/09/IMG_20170604_151536.jpg)

Anyway, I mention this now because I've finally added the component most sorely missing from the build - a switch. Until now, when we wanted to use it, someone would have to climb under the table and plug it in - which as I'm sure you can imagine meant it wasn't used very often.

But not just any switch, you understand. While it might have the look of the 19th century, it's firmly rooted in the 21st thanks to the use of a [Sonoff](https://www.amazon.co.uk/dp/B079CL1B5D) switch, which not only lets me control the lamp from an app on my phone, but also via Alexa on my Amazon Echo.

Installing the Sonoff is easy, as you simply put it in serial with the live and neutral wires coming in from the socket, which not only powers the device itself, but also lets you control a relay that feeds power on to the lamp.

![Product image of a Sonoff Wi-Fi smart switch, with a phone showing its control app](/assets/img/2017/09/61RHDZDsrCL._SL1213_--1-.jpg)

A momentary button on the device itself can be used to toggle the relay on and off manually, or when held down for five seconds enters a setup mode allowing me to feed it with everything it needs to connect with the wifi, and further, with the app (and thus Alexa).

{% include youtube.html id='DrybWl2v7Zg' title="Let there be light" %}
