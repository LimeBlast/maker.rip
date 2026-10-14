---
author: daniel
layout: post
title: Project Wildcat... has been delayed
date: '2018-11-10 21:35:58'
image: /assets/img/2018/11/IMG_20181110_100407-1-.jpg
categories:
- wildcat
tags:
- feather-huzzah
- adafruit-io
- c
- arduino
---

<p class="intro"><span class="dropcap">I</span>t is with no small amount of sadness that I have to report that, in the final stretches of the build of Wildcat, I've inadvertently managed to set my progress back for a few days.</p>

As [mentioned in my previous post](https://maker.limeblast.co.uk/2018/11/09/introducing-apricat/), the addition of a new member of the family hasn't been without its issues, with Apricat being somewhat liberal in her use of tooth and claw to show her distrust of us.

To help combat this I devised the idea of an incident board, such as you'll see in factories showing how long it's been since the last accident, but designed to show how long it's been since Apricat last misbehaved.

![np74ijwbwxo11](/assets/img/2018/11/np74ijwbwxo11.jpg)

The plan was to use an [Adafruit Feather Huzzah](https://amzn.to/2PSGurk) and a [16x8 LED matrix](https://amzn.to/2Dxtlht), connected with a physical button, and a super cute cat photo frame we found in Homesense, to build a ticker which used data persisted on [Adafruit IO](https://io.adafruit.com/) to calculate and display how long it's been since the button was last pressed.

Arguably, rather than relying on the cloud for something trivial like this, I could have done the entire project locally, using any number of development boards that support non-volatile memory with a real time clock - but I don't have any of those things.

OK, so that's a bit of a lie.

I could easily have based the project on a Raspberry Pi Zero, which would have solved the persistence issue, with the addition of an [RTC PiZero addon](https://thepihut.com/products/rtc-pizero) solving the clock problem, but that would mean writing the project using Python, and figuring out how to make it start properly on boot - and honestly, do we really need an entire Debian-based operating system for something as simple as recording a time and powering an LED display? It just feels like overkill.

Alternatively, the use of the [Feather M0 Adalogger](https://amzn.to/2JRuMHN) I have, combined with a [DS3231 Precision RTC FeatherWing](https://amzn.to/2DuF7Jq), would also solve these problems and let me use the Arduino platform - but that would prevent me from doing fancy things like Alexa integration...

Not that I have any plans to do that, but I can if I want.

Truth is, I wanted more experience logging data to the cloud from remote devices like this to help with a project I have planned for the future, and, well, I'm a web guy - I'd never live it down if I didn't make it _smart_.

Anyway, back to this morning, and I'm in the final stages of assembly, having just soldered the button onto the back of the frame. I needed to test it with a power unit that wasn't my laptop, so I grabbed the first spare USB charger I had spare and plugged it in.

Little did I know that by this point, it was already too late.

I had a couple of flashing LEDs on the board, but nothing else. Confused as to why it wasn't working, I tried plugging it back into my laptop, and while it booted the display, I wasn't able to keep it running for more than a couple of seconds, nor did the Arduino software recognise it was connected, and something on the board was getting very hot.

After a few minutes searching I found the following on the [power management page for the Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/power-management):

![Power-Management-_-Adafruit-Feather-HUZZAH-ESP8266-_-Adafruit-Learning-System-2018-11-10-8-pm-33-33](/assets/img/2018/11/Power-Management-_-Adafruit-Feather-HUZZAH-ESP8266-_-Adafruit-Learning-System-2018-11-10-8-pm-33-33.png)

The power unit I'd chosen at random was the official Raspberry Pi 3 power adaptor, one which supplied the same 2.5 amps as the CanaKit one in the warning.

Basically, I fried the unit.

This sucks, especially when I was in the final stretch of assembly - but at least I've learnt that not all USB power supplies are the same, and will be far more selective with how I power my projects in the future.

Anyway, thanks to a generous donation by Lucy I've ordered another Feather Huzzah, so I'm hoping to be back on track soon. Once I've finally completed the assembly, and have proven to myself that it all works, I'll make another post explaining some of the more technical aspects of it.

Until then I guess we'll all have to sit here frustrated at being so close, but being denied success due to something really dumb. Oh well.

UPDATE: [Wildcat is live](/2018/11/19/wildcat-is-live-and-angry/)!
