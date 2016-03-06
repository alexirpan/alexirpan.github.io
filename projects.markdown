---
layout: page
title: Personal Projects
permalink: /projects/
---

These are personal projects that I consider good enough to share.

All of these projects are hosted on a Heroku free plan. Heroku
automatically powers down the site if no one has visited in a while,
so the first page load may be slow.

-----------------------


<br>[**Divisibility Regex**](http://divisibilityregex.herokuapp.com/)

*Checks divisibility of numbers by using regular expressions. December 2015*

![Screenshot of a big regex](/public/project-pics/divisibility.png)
{: .centered }

Repo: [here](https://github.com/alexirpan/divisibility-regex)

Creates regular expressions that match a number if and only if it is divisible
by another number. Works for checking divisibility up to 9.
A brief explanation of how this works can be found at the
site's FAQ.

Made this to have fun exploring DFAs and regular expressions.

-----------------------


<br>[**Jaden Smith Generator**](http://jaden-generator.herokuapp.com/)

*Generates typical Jaden Smith tweets. September 2014*

![A typical Jaden Smith tweet](/public/project-pics/jaden.png)
{: .centered }

Repo: [here](https://github.com/alexirpan/Jaden-Smith-Generator)

Outputs typical [Jaden Smith](https://twitter.com/officialjaden) tweets
by using a Markov chain trained on
all tweets made by Jaden Smith and the full text of the King
James Bible. (Adding the King James Bible makes the output coherent more
often.)

This idea was incredibly silly, so of course I decided I needed to make it real.
I have considered upgrading this to an RNN model, but
so far I've convinced myself that would be really, really dumb.

-----------------------


<br>[**Python Flow Visualizer**](http://python-flow-visualizer.herokuapp.com/)

*Visualize the control flow of a Python program. October 2013*

[![Visualized control flow for memoized Fibonacci](/public/project-pics/python.png)](/public/project-pics/python.png)
{: .centered }

Repo: [here](https://github.com/alexirpan/python-visualizer)

(Note: site renders poorly on a small screen. Click image for a larger version.)

Runs a given Python snippet and animates the jumps in control flow.
The picture above is a visualization of [Peter Norvig's Scheme interpreter](http://norvig.com/lispy.html)
evaluating tree recursive Fibonacci. Identifies the lines that are jumped to most
often, and notes which lines fail Python lint checks.

Made in 24 hours for the Facebook NorCal Hackathon. Worked with
Anting Shen, Chenyang Yuan, and Ena Hariyoshi. Uses [D3.js](https://d3js.org/) and
[Angular](https://angularjs.org/).


