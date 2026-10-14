---
author: daniel
layout: post
title: One step forward, two steps back
date: '2016-08-27 14:28:47'
image: /assets/img/2016/08/one_step--1-.jpg
categories:
- the-makers-guide-to-the-zombie-apocalypse
---

<p class="intro"><span class="dropcap">O</span>ne of my friends, a young gentleman by the name of Cos, has a healthy respect for the idea that the zombie apocalypse isn't an <em>if</em> - but a <em>when</em>. This is something which informs his everyday life, and will often guide his decisions.</p>

Don't get me wrong, Cos isn't a prepper, but he does, for example, like to get good quality hardware in case he needs it to fend off an attack. On many occasions, you'd have found us in Homebase discussing the pros and cons of various kitchen knives in relation to this very purpose.

He also has a survival plan for this eventuality, one which he has shared with me, but I won't share with you (get your own damn plan). I'll often joke with him that, like in any classic zombie film, one member of the party will do something that results in rest getting killed - and that person will be me. I won't do this deliberately, of course, but through incompetence, pride, or some other silly mistake.

I feel this is worth mentioning, you see, as the further I get into the book, the more I realise my self-prediction is probably accurate, and that if this was the apocalypse I would very much be dead by now.

Nothing I do seems to be working out quite as intended, as even within the comfortable quarters of my living room, with access to next day delivery from Amazon Prime funded from a generous budget, I'm having trouble making anything work. And that's without that added pressure of a zombie's cold breath on my neck.

---------------

Yesterday saw the delivery of my [DC Bench Power Supply](http://amzn.to/2bObzar). This is what I've purchased in lieu of using car batteries to power my projects, as it'll give me a lot more control over the power supplied to the projects, letting me emulate the different states of charge in a battery, for example.

![](/assets/img/2016/08/bps--1-.jpg)

I also think it'll be a handy tool going forward in my electronics learning, as I've heard it described as the second most important thing in an electronics toolkit, after the multimeter. 

Anyway, excited by the ability to put another project to rest, I reassembled the various battery meter components, attached the leads from the power supply, and squeed with excitement as I saw the value on the display go up and down in relation to the voltage I was pumping into it.

Emboldened by this success, I prepared my PIR module ready for Project 6 and uploaded the relevant sketch into the Arduino. This is where it started to go wrong, as the voltage value on the Arduino display no longer matched that on the power supply (it was about `2.8 volts` under).

At first, I thought this might have something to do with the resistors, so I swapped them for fresh ones - no change. So I decided to go back to the previous sketch to see if that made any difference - and it's at this point that I realised the Arduino was no longer being recognised by my computer.

This is the second Arduino I've managed to destroy - only, I'm not sure that it is destroyed. The first one was subjected to a voltage far higher than it was able to handle and became unresponsive, but this one still does _stuff_. When the power leads are connected, the sketch skill runs and the (albeit incorrect) voltage is shown on the display.

I have another Arduino on its way to me via a subscription to [Creation Crate](https://mycreationcrate.com/), so after I've finished the experiment contained within, I may repurpose it and continue down this route, but I'm a little lax to do that until I know what the problem is, as I don't want to keep _breaking_ Arduinos, especially if the thing that's wrong with it is fixable.

In any case, I have the bits needed to complete Project 3: LED Lighting, so I'll give that a go at some point in the week, and have another project involving a dinosaur and a Raspberry Pi on the back burner, so I'll see if I can get that working too.

As ever, watch this space.
