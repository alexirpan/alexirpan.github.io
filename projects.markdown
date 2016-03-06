---
layout: page
title: Personal Projects
permalink: /projects/
---

These are personal projects that I consider completed, or at least good
enough.

All of these projects are hosted on a Heroku free plan. Heroku
automatically powers down the site if no one has visited in a while,
so the first page load may be slow.


**Divisibility Regex**

Link: [here](http://divisibilityregex.herokuapp.com/)

Repo: [here](https://github.com/alexirpan/divisibility-regex)

Check if a number is divisible by matching it against an appropriate
regular expression. A brief explanation of how it works can be found at the
site's FAQ. Created to have fun exploring the equivalency between DFAs and
regular expressions.


**Jaden Smith Generator**

Link: [here](http://jaden-generator.herokuapp.com/)

Repo: [here](https://github.com/alexirpan/Jaden-Smith-Generator)

Outputs typical sentences [Jaden Smith](https://twitter.com/officialjaden)
might tweet. Generates sentences with a Markov chain trained on
a corpus of every tweet by Jaden Smith. Except,
it wasn't funny or coherent enough, so I also trained the Markov chain
on the King James Bible. I have considered switching this to an
RNN-based language model, but so far I've convinced myself it would
be too stupid to do so.


**Python Flow Visualizer**

Link: [here](http://python-flow-visualizer.herokuapp.com/)

Repo: [here](https://github.com/alexirpan/python-visualizer)

When given a Python snippet, this inspects the jumps in execution made by the
Python interpreter, then animates a visualization of the control flow.
Highlights especially connected lines in shades of green, where greener
lines are jumped to more often. Made by a group of four for the
Facebook NorCal Hackathon.

