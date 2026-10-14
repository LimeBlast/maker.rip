---
author: daniel
layout: post
title: What's in the box?
date: '2016-10-03 16:24:21'
image: /assets/img/2016/10/pexels-photo-24325--1-.jpg
categories:
- review
tags:
- arduino
---

<p class="intro"><span class="dropcap">A</span> couple of months ago I got really excited when I saw that Adafruit had launched a curated box of products suitable for anyone that's part of the maker scene. The <a href="https://www.adafruit.com/adabox">AdaBox</a> follows the same concept as something like Loot Crate, which has a unique theme per box and includes a bunch of items related to that theme. Once a particular box is gone, it's gone.</p>

Unfortunately, this excitement soon died down when I discovered AdaBox isn't available in the UK ([yet](http://forums.pimoroni.com/t/any-plans-for-curated-boxes-for-makers-and-or-electronics-enthusiasts/2816/1)), but I wasn't going give up hope, so off I went looking for an alternative - which is when I found [Creation Crate](https://mycreationcrate.com/refer/Danie-TCVKWSNV).

Unlike AdaBox, each Creation Create is designed as an individual lesson in electronics, with each additional box building upon the knowledge gained in the previous one. This means everyone will get the same first box, no matter when they join, followed by the same second box, then third, etc..

Each box contains everything you need to complete that month's project, which at a minimum includes a (clone) Arduino, breadboard, and an instruction manual, along with the various components needed for that lesson.

The manual itself is nicely produced, with diagrams showing how to assemble the components, the code for the Arduino (including a secret link to download the code), a troubleshooting section, additional exercises to complete (along with another secret link to the answers), and a sneak peek at the next box's project.

My only complaint about the manual is the presentation of the code for the Arduino. It doesn't use a monospace font, nor feature any indentation, and while it is commented throughout (which helps explain what it's doing), the comments are under the code they describe (rather than above, which tends to be the standard for such things). This may be nitpicking, but these are simple things to fix and would go a long way towards setting best practice expectations.

The first project was simple enough to assemble. It features a colour changing Chinese lantern controlled by three LEDs. The LEDs, one each of red, green and blue, step in turn through different levels of brightness, allowing for the mixing of the colours to light up the lantern.

![](/assets/img/2016/10/IMG_20161003_162531500_HDR--1-.jpg)

It also has a light sensor which is meant switch the lantern off during the day, but in my case, it didn't. This is probably something to do with the threshold defined in the script, which I've been far too lazy to toy about with.

Now, having got the first two boxes (although I've not assembled the second one yet *[yes I have, see update below - Dan]*), I think I'm going to wait for the third one (seeing as I've already paid for it) then cancel my subscription *[maybe, see below - Dan]*. This isn't a bad service by any means, but it also isn't aimed at me: someone that's much closer to 40 years of age than 10.

When my niece is a bit older, I can very much see myself gifting a subscription to her, and would very much enjoy helping her assemble each project, but she's a few years off that just now, and I can think of cheaper ways of getting spare Arduinos.

Hopefully, AdaBox (or something like it) will cross the pond in the near future, and I'll have something else to spend my disposable income on, until then, I'll stick to preparing for the zombie apocalypse.

**Update: 5th October:** Since I first published this post I've had a chance to build the second kit, a memory game which plays like [Simon](https://www.wikiwand.com/en/Simon_(game)).

Unlike with the first kit, I really couldn't be bothered to type out all the code manually, so after I'd assembled the components, I downloaded the code from their secret URL (which I was disappointed to see also didn't feature code indentation) and flashed it onto the Arduino.

It was fun to play for a couple of minutes, but as I'm quick to bore I soon put it to one side. I have no intention of playing it again, but I've also not disassembled it yet, nor have I disassembled the first one. Maybe my interest is a bit more piqued than I figured.

In any case, the last page of the instruction manual always features a sneak peek of what's coming in the next box, along with the challenge of guessing what it does. This time, it shows a photo of a breadboard with a [HC-SR04 Ultrasonic Range Sensor](http://amzn.to/2cSGKUC). I've not used one of these before, but I've often seen them used as *eyes* on robots, so I'm interested to see what the project is going to do with it.

With all this in mind, I'm going to wait until I've built the third project before I decide if I'm going to continue with my subscription or not. I'll update this post accordingly.

**Update: 4th November:** Another update, but probably my last.

I received the third kit earlier in the week and had a chance to assemble it today. As mentioned above, I was excited to play with an ultrasonic sensor, but the final build is more disappointing that anything.

{% figure %}
  <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/ASHR9tgtyBQ' frameborder='0' allowfullscreen></iframe></div>
{% endfigure %}

In addition to the range sensor, the kit contains 6 LEDs, a piezo buzzer, and some resistors. Unlike the previous kits, this one told you where to put the components, but not the connecting wires - instead, you're challenged to figure this out using the fully commented code sample (which I'm happy to report finally featured code indenting). This should be simple enough for anyone that has gotten this far in the process, but a cheat sheet diagram is available behind their passworded portal.

I assembled the kit, waved my hand in front of it, watched the LEDs turn on and off. Filmed the above video clip, then put it away. Maybe it's just me (as, again, I don't think I'm the target audience), but this left me unfulfilled.

And at around £22 per box (£66 for the three I've had so far), I'm having trouble finding this to be good value for money. At the time of going to press, for just a penny more than £62, you can get the [official Arduino Starter Kit](http://amzn.to/2e95SqH). This contains a genuine Arduino Uno R3 (not a Chinese clone that made my Mac crash), a whole ton of fun and interesting components, and a very nicely produced 170-page guidebook with the instructions to build 15 different projects.

I wish Creation Crate all the luck in the world, but it's not for me, and it's not something which I can recommend.
