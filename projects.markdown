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
<br>


[**Divisibility Regex**](http://divisibilityregex.herokuapp.com/)

*Check if a number is divisible by another with regular expression*

![Screenshot of a big regex](/public/project-pics/divisibility.png)

Repo: [here](https://github.com/alexirpan/divisibility-regex)

Check if a number is divisible by matching it against an appropriate
regular expression. A brief explanation of how it works can be found at the
site's FAQ. Created to have fun exploring the equivalency between DFAs and
regular expressions.


[**Jaden Smith Generator**](http://jaden-generator.herokuapp.com/)

*Generate typical Jaden Smith tweets*

![A typical Jaden Smith tweet](/public/project-pics/jaden.png)

Repo: [here](https://github.com/alexirpan/Jaden-Smith-Generator)

Outputs typical sentences [Jaden Smith](https://twitter.com/officialjaden)
might tweet by using a Markov chain trained on two corpora:
all tweets made by Jaden Smith, and the full text of the King
James Bible. Created because it was too silly to not make.
I have considered switching this to an RNN-based model, but
so far I've convinced myself that's too stupid to do.


[**Python Flow Visualizer**](http://python-flow-visualizer.herokuapp.com/)

*Visualize the control flow of a Python program*

![Visualized control flow for memoized Fibonacci](/public/project-pics/python.png)

Repo: [here](https://github.com/alexirpan/python-visualizer)

(Note: will render poorly on a small screen.)

Runs a given Python snippet and animates the jumps in control flow.
The linked picture is a visualization of [Peter Norvig's Scheme interpreter](http://norvig.com/lispy.html)
evaluating tree recursive Fibonacci. Identifies lines that are jumped to
often, and makes a note on lines that fail a Python lint check.
Made for the Facebook NorCal Hackathon; I was part of a group of four.

