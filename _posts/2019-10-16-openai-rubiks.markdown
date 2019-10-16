---
layout: post
title:  "Let's (Briefly) Discuss OpenAI's Rubik's Cube Result"
date:   2019-10-16 01:25:00 -0700
---

Recently, OpenAI announced they had [gotten their dexterous
manipulation system to solve a Rubik's Cube](https://openai.com/blog/solving-rubiks-cube/).
This is pretty cool, and I actually don't have too much to add besides that.
I figured it would be good to explain some background here, because this is
very much a steady continuation of existing work, rather than something insane.


What Did OpenAI Do?
----------------------------------------------------------------------

Using reinforcement learning, they've learned a controller for a [Shadow Hand](https://www.shadowrobot.com/products/dexterous-hand/)
that lets them solve a Rubik's Cube with reasonable success rate. Their reported
success rate is 60% for average scrambles and 20% for the hardest possible
scrambles (that require 26 quarter-face turns).

This numbers sound low out of context. In context, they're pretty good.
Dexterous manipulation is *hard* to learn.


Hang On, Wasn't This Robot Hand in the News Before?
----------------------------------------------------------------------

It was! In July 2018 OpenAI revealed they were doing RL on the Shadow Hand
platform in their [Learning Dexterity](https://openai.com/blog/learning-dexterity/)
post, where they demoed manipulating a solid block to match a given target
orientation.

I say doing RL on the Shadow Hand platform, but really, it's more like they do
RL on many versions of a simulated version of the Shadow Hand, and then apply
a number of techniques to get models trained in simulation to transfer to the
real robot.

One question you may have is, "why don't they train with real data?" In robotics,
real data is generally much more useful than simulated data. My understanding
is that two things are at play. First, OpenAI is curious how far they can
push zero-shot sim2real transfer, because simulation scales with compute while
real robot doesn't. Second, OpenAI's goal is to show that deep reinforcement
learning can solve difficult robotics problems. Therefore, they've set their
sights on a problem hard enough that simulation is the *only* way they'd be
able to get enough data for RL to learn something.


Why is Dexterous Manipulation Hard?
-----------------------------------------------------------------------

Okay, big cavaet. I've worked on robotic manipulation, but I haven't worked
on dexterous manipulation. So maybe I'm totally off here. But the TL;DR
answer is that hardware is terrible and good simulators are hard. The rule
of thumb is that the best way to find simulator defects is to learn a model
against the simulator, run it on a real robot, and watch what goes horribly
wrong this time.

OpenAI says they've been working on solving a Rubik's Cube since May 2017.
They solved it in simulation in July 2017 (2 months). They got manipulation
of a solid wooden block *a year* later (JUly 2018). Moving from a solid
block to a Rubik's Cube then took another 14 months. The
"works on a real robot" part is the main reason it's tricky.
