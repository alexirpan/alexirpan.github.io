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
Dexterous manipulation is a huge pain to learn.


Why is Dexterous Manipulation Hard?
-----------------------------------------------------------------------

Okay, big cavaet. I've worked on robotic manipulation, but I haven't worked
on dexterous manipulation. So maybe I'm totally off here. But the TL;DR
answer is that hardware is terrible and simulators suck unless you invest a
lot of effort. One common
piece of wisdom is that if you learn a model in a simulator, all you really
learn is where your simulator is inaccurate.

For context, OpenAI says they've been working on solving a Rubik's Cube since
May 2017. It took them 2 months (May 2017 - July 2017) to solve it in
simulation. It took them 1 more year (July 2017 - July 2018) to get to manipulating
a solid wooden block. It took them 14 more months (July 2018 - October 2019)
to get to the Rubik's Cube. The "runs on a real robot" part is the entire
reason the learning problem is difficult.


Hang On, Wasn't This Robot Hand in the News Before?
----------------------------------------------------------------------

It was! OpenAI announced they were doing RL on the Shadow Hand
back in July 2018 in their [Learning Dexterity](https://openai.com/blog/learning-dexterity/)
post.

I say doing RL on the Shadow Hand platform, but really, it's more like they do
RL on many randomized versions of a simulated version of the Shadow Hand, and
then try to get that to transfer to the real Shadow Hand in a zero-shot manner,
with no additional real data.


What's New?
-------------------------------------------------------------------------------

Actually, not very much. This is one of those
["moonshots achieved through roofshots"](https://rework.withgoogle.com/blog/the-roofshot-manifesto/)
projects, where there's a rather clear line of steady, compounding
improvements.

The model is trained using distributed PPO, using the Rapid (LINK) system
they've developed in house, used in both the DotA 2 project and the original
Learning Dexterity results. The model architecture is reminiscent
of the DotA 2 architecture - different input features are embedded into a
512-dimensional embedding space, then summed together and passed through a
large LSTM. Like the Learning Dexterity work, instead of learning a policy
directly on pixels through RL, they instead predict the pose of the Rubik's
Cube from three camera images, then feed those predicted poses to the RL
agent. Again, like the Learning Dexterity work, they use the same asymmetric
actor-critic trick. The Q-function is allowed to use all the ground-truth
state information to estimate Q-values. Meanwhile, the policy is only
allowed to use features that will exist in the real-world. This is fine if
you just want zero-shot transfer, because you only need the policy at inference
time.

If you've been following their work (like I have), the threads of past research
are very clear. It's ideas from a year ago, re-executed in a new context.
A good start, but not enough by themselves.

The main two new things I saw were the automatic domain randomization, and the
adoption of policy cloning and distillation from the DotA 2 project.



One question you may have is, "why don't they train with real data?" In robotics,
real data is generally much more useful than simulated data. My understanding
is that two things are at play. First, OpenAI is curious how far they can
push zero-shot sim2real transfer, because simulation scales with compute while
real robot doesn't. Second, OpenAI's goal is to show that deep reinforcement
learning can solve difficult robotics problems. Therefore, they've set their
sights on a problem hard enough that simulation is the *only* way they'd be
able to get enough data for RL to learn something.
