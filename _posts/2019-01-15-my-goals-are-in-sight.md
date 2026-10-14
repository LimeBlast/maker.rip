---
layout: post
title: My goals are in sight
date: '2019-01-15 09:57:56'
image: /assets/img/2019/01/IMG_20190115_090111-1-.jpg
categories:
- personal
tags:
  - trello
  - magicmirror
  - screenly
  - github-pages
---

<p class="intro"><span class="dropcap">S</span>ince the end of 2015 I've been using a board on Trello to log and track my yearly goals.</p>

The setup is quite simple - at the start of each year I review the goals in the previous year's column, using a sticker to indicate success or otherwise, then create a new column for the upcoming year. Each goal is written using the [SMART methodology](https://en.wikipedia.org/wiki/SMART_criteria), and added as a card, then embellished with an image that represents the goal to serve as visual reminder.

{% figure [caption:"All my ducks in a row"] %}
  ![](/assets/img/2019/01/trello-goals-1-.png) 
{% endfigure %}

For the most part this has worked pretty well. It informs me where I was in previous years, reminding me what problems I wanted to solve at the time, and lets me appreciate how far I've progressed since.

But it suffers from the same issue that other _new year's resolutions_ suffer from - they're too easy to forget about. Sure, you start the year full of enthusiasm (despite the hangover), but by the 2nd of January you're back at work, by the end of the week all your festive cheer has drained away, and there's a good reason the [12th of January is known as Quitter's Day](https://www.independent.co.uk/life-style/quitters-day-new-years-resolutions-give-up-fail-today-a8155386.html).

But what kind of maker would I be if I didn't attempt to solve this problem?

I figured the easiest way to keep my goals in mind was to setup a display somewhere in the house that used the Trello API to show the goals, reminding me at a glance what they are every time I walk past.

# Mirror mirror on the wall

My first attempt at this was to use the [MagicMirror²](https://magicmirror.builders/) platform, as since my earliest maker days I've wanted to [construct my own MagicMirror](https://www.raspberrypi.org/magpi/magic-mirror/), but always fell short of actually starting because I didn't feel my woodworking abilities were up to scratch.

Not content to let something as silly as that stop me, I reached into my [LEAN methodology](https://leankit.com/learn/lean/lean-methodology/) toolkit, grabbed a Raspberry Pi and an old laptop screen, and set about creating a [Minimum Viable Product (MVP)](https://en.wikipedia.org/wiki/Minimum_viable_product) - that is, just enough to prove the concept without using too many resources. In this instance, that meant installing the software and exploring the options provided within.

{% figure [caption:"Illustration by [Henrik Kniberg](http://blog.crisp.se/author/henrikkniberg)"] %}
  ![](/assets/img/2019/01/mvp.png) 
{% endfigure %}

Now, the MagicMirror² platform seems very well designed, with a lot of support for pulling data from a range of sources, but it wasn't quite what I wanted for this project. It had the benefit of being able to read directly from my Trello list, but each goal was nothing more than an entry on a small bulleted list, lost in among a whole bunch of other information.

I could have spent some time building my own module for the platform, but this felt like a step in the wrong direction as rather than solving the direct problem - that of displaying my goals - I'd instead be spending my time [Yak shaving](https://seths.blog/2005/03/dont_shave_that/) in the guise of learning how to build the module.

# Digital signage solution

It was actually during the initial install of Raspbian for the above idea that I first saw what would end up being my solution to the problem, an operating system offered via the NOOBs installer called [Screenly](https://www.screenly.io/ose/).

Screenly, it turns out, is a digital signage platform which lets you remotely configure any number of assets (such as webpages, images, YouTube videos, et al) to display, in rotation, upon your Pi's screen. I'd never heard of it before, but figured if I could find a suitable HTML carousel or sideshow template, I'd be able to host it for free using [GitHub Pages](https://pages.github.com/), so I set out to find a suitable template.

I reviewed a couple of choices, including a [Fullscreen Background Image Slideshow with CSS3](https://tympanus.net/codrops/2012/01/02/fullscreen-background-image-slideshow-with-css3/) template, and the [Vegas 2 Background Slideshow jQuery Plugin](https://vegas.jaysalvat.com/), but settled upon the [Fullscreen Image Blur Effect with HTML5](https://tympanus.net/codrops/2011/11/18/fullscreen-image-blur-effect-with-html5/) template provided by codrops, as this provided the quickest route to the features I wanted - namely the ability to automatically switch between multiple images and messages at an easily controlled rate, all without requiring me to spend too long learning anything new.

I already had the images and wording for the goals, so it took no more than about an hour to update my own content into the template, and make some small changes to the design and functionality, and before I knew it, I had a sideshow hosted on GitHub.

{% figure [caption:"Completing six hikes is one of my goals for 2019"] %}
  ![](/assets/img/2019/01/Screenshot_2019-01-15-2019-Saurus-Goals-1-.jpg) 
{% endfigure %}

Of course, all this information is hard-coded into the template, rather than being dynamically supplied by the Trello API - but do I really need it to be dynamic?

By definition, a yearly goal is something you set once a year, and the 30 minutes it might take each year to update the sideshow is easily more justifiable than the several hours it'll take to implement something which pulls in from the API, not to mention the relative complexity and cost of hosting a dynamic script over that of a static page which I can host for free.

That's not to say I'd never make the slide show dynamic - it might be fun to learn the Trello API, and I could probably do the whole thing using client side JavaScript, or as a Ruby Serverless application, but the LEAN methodology advocated failing fast, such as I did with the MagicMirror² approach, so there's no point spending any time even looking at anything like that when there's a quicker way of achieving the same end result.

{% figure [caption:"'The faster you can fail, the faster you can succeed'"] %}
  ![](/assets/img/2019/01/3069944_3x2_fail_fast.jpg) 
{% endfigure %}

# Bringing it all together

Now that I had an eye-catching slide show of goals hosted on GitHub, all that remained was to install Screenly and point it at the page. But it's at this point that I took a second pivot - given the sheer mess of components needed to make the laptop screen work, was this really the best approach?

{% figure %}
  ![](/assets/img/2019/01/IMG_20190115_093324-1-.jpg) 
{% endfigure %}

To make a suitable enclosure for the display, driver board, and Pi, would take more effort that I really wanted to spend, and seeing as I am still planning on building my own smart mirror (spurred on by how impressed I was with the MagicMirror² platform, even if it wasn't suitable for this project) I'd rather keep these components for that.

So instead, as you will see from the feature image for this post, I used my [7" touchscreen display](https://thepihut.com/products/official-raspberry-pi-7-touchscreen-display) instead. This has the benefit of being compact and self contained, providing something that was large enough to grab your attention, but small enough that you can use it like a picture frame, and with as much versatility.

All in all, I'm very happy with the outcome of this project, even if it didn't end up look anything like I thought it would, because I think the end result is far better than what I initially had in mind, and I was able to reach it quickly and easily.

{% figure %}
  ![](/assets/img/2019/01/path-to-success-1.jpg) 
{% endfigure %}
