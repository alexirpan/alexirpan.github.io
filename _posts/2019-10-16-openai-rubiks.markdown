---
layout: post
title:  "Let's Discuss OpenAI's Rubik's Cube Result"
date:   2019-10-16 01:25:00 -0700
---

Recently, OpenAI announced they had [gotten their dexterous
manipulation system to solve a Rubik's Cube](https://openai.com/blog/solving-rubiks-cube/).
I thought I wouldn't have too much to say, and then this post got longer and
longer.


What Did OpenAI Do?
----------------------------------------------------------------------

Using reinforcement learning, they learned a controller for a [Shadow Hand](https://www.shadowrobot.com/products/dexterous-hand/)
that lets them solve a Rubik's Cube with reasonable success rate. They
report a success rate of 60% for average scrambles, and 20% for the hardest
possible scrambles that require 26 quarter-face turns.

I say doing RL on the Shadow Hand platform, but really, I mean they do learning
on a simulated version of the Shadow Hand, then try to get that to transfer to
the real Shadow Hand with no real data.
It's a neat dexterous manipulation result.


Why is Dexterous Manipulation Hard?
-----------------------------------------------------------------------

As a general rule, robot hardware is terrible to work with, and simulators
suck unless you spend a bunch of time improving them. This is especially
true for robot hands, because they have way more degress of freedom and
complexity compared to simpler grippers.

OpenAI says they've been working on solving a Rubik's Cube since
May 2017. It took them 2 months (May 2017 - July 2017) to solve it in
simulation with a simulated hand. It took them 1 more year (July 2017 - July 2018)
to get a real hand to manipulate a solid wooden block. Then, another
14 months (July 2018 - October 2019) to get to the Rubik's Cube. The "runs on a
real robot" part is the entire reason to care about this work.


Wasn't This Robot Hand in the News Before?
----------------------------------------------------------------------

It was! It showed up in their
[Learning Dexterity](https://openai.com/blog/learning-dexterity/)
post from July 2018, where it also got a lot of press.


What Isn't New?
----------------------------------------------------------------------

Everything about this paper looks like
a ["moonshot achieved through roofshots"](https://rework.withgoogle.com/blog/the-roofshot-manifesto/)
project, where there's a clear line of steady, compounding improvements from
prior work.

The model is trained using
distributed PPO with OpenAI's Rapid framework, which was used for both OpenAI
Five and the Learning Dexterity paper. The model architecture is heavily
inspired by the DotA 2 architecture - each input features is embedded into
a 512-dimensional embedding space, and these embeddings are summed and
passed through a large LSTM.

Like the Learning Dexterity work, instead of learning a policy
directly on pixels through RL, they instead predict the pose of the Rubik's
Cube from three camera viewpoints, then feed those predicted poses to the RL
agent.

Again, like the Learning Dexterity work, they use the same asymmetric
actor-critic trick, where the critic gets all ground truth state information,
and the policy only gets the features visible from real-world data, which
is fine for zero-shot transfer because you only need the policy at inference
time.

It's the same ideas, likely even the same codebase, executed in a different
context.


What Is New?
-----------------------------------------------------------------------

One is the *automatic domain randomization*. In domain randomization, you
learn a model in several randomly sampled simulated environments, learning
a final model that's more robust and more likely to transfer to reality.

Applying domain randomization requires some tuning, both for deciding what
to randomize, and deciding the ranges from which to sample parameters.
Too little randomization, and the model won't be robust to real-world noise.
Too much, and the learning problem will become too difficult to learn.

Taking inspiration from automatic curriculum learning, they maintain a
distribution over simulator parameters, starting at a single point.
If the policy's recent performance is above a threshold, the distribution
is expanded to be wider. This lets us start from a simple problem, then
expand its difficulty as the policy gets better at the task. (The
distribution is never narrowed, and I assume you have to tune how much
you widen each dimension, and the performance threshold, but this is
still fewer parameters and less work than defining a fixed distribution
or fixed curriculum schedule.)

Another detail which I only found after a close reading was
*adversarial domain randomization*. This has been done before. An adversary
applies perturbations to the
force, torque, and actions, in a way that hurts performance to mine hard
examples. Or rather, that's the theory, but in practice they
found best results with a random adversary, which performed better than
any learned adversary.
This seems weird to me. I can believe the result, and at the same time it
feels like a learned adversary should be better (but perhaps it's tricky
to tune it properly.)

Finally, although it's not directly related, there is
a heavier lean on
*policy distillation* and *model surgery*. This is a lesson they've carried
over from DotA 2. Over the course of a long project, you will naturally want
add new input features or try new neural net architectures. If the model takes
a long time to train, it's worth designing methods that let you do this without
training from scratch. The reason they add embeddings together instead of
concatenating them is because you can easily add a new feature without changing
the shape of any existing weight matrices. This lets you avoid training entirely
from scratch.

For approaches that aren't compatible with this (like changing the LSTM size),
the current model can be distilled into the new model architecture, which is
also much faster than training from scratch.


What Are the Pros Of This Work?
----------------------------------------------------------------------------

I mean, it works. That's always worth celebrating. Based on their demos, the
result is pretty robust. They've also done a lot of work on interpreting the
model. It's cool that by applying
interpretability tools on the LSTM hidden state, they're able to identify
semantically meaningful clusters for cube manipulation. I know people have
complaints over how they got the policy to work (more details on that in the
next section), but I don't think OpenAI has gotten enough credit for their
analysis of what the learned policy does, and what emergent behaviors may
appear from sufficiently big neural nets.

In general, I've found that people without robot learning experience are
poorly calibrated on how much bullshit there is in getting a real robot
learning setup to work. It's always good to see something get there.

Finally, I know this is a weird thing to appreciate, but I actually like the
policy distillation and model surgery aspects the most. Yes, the automatic
domain randomization is nice, but of course automatic curriculum learning
should perform better than sampling tasks uniformly at random.

The policy distillation and model surgery aren't central to the project,
but they are indicative of the correct research culture:
**a focus on design decisions that encourage
long-term research success.**

At a party 2 years ago, I was with a few people talking about OpenAI, and an
employee came up to give a quick spiel. They said they felt the academic
community undervalued research infrastructure. That's why they released Gym.
That's why they released OpenAI Baselines. It was something where OpenAI
was in a position to provide value to the RL community.

Okay, yes, the obvious cynical point here is that Gym and Baselines are
also great branding tools for OpenAI's recruiting purposes.
This would have been true for any group that released something that got the
adoption Gym or Baselines did, so I don't think it's a valid criticism.

Research code is usually terrible, because you're trying to move fast on
an idea that may not even make sense. Designing everything properly the
first time slows down your experimenting too much. However, never cleaning
up anything is its own sin. People really underestimate the impact of
good research infra, in my experience. I'm not saying it's easy to build
good tools. It's absurdly difficult to build good tools. But if done properly,
it pays off long-term over all future projects. An RL diagnostics library
can be re-used for every RL project, An interpretability library can be
re-used for any project that wants interpretability.

The comments from this paper indicates that some people at OpenAI get it,
and are thinking about it at multiple levels of a research project - both
the code infrastructure, and the model architecture. It's cool and I wish
people did more of this.


What Are the Cons of This Work?
-----------------------------------------------------------------------------

[Skynet Today's article](https://www.skynettoday.com/briefs/openai-rubiks-cube)
has a good summary of some controversial points, along with their own take on
things. It's worth reading. Here are a few I want to point out.


Use of a Solver
===================================================================

The final robot controller is not learned entirely end-to-end from pixels to
actions. There are intermediate steps of estimating pose, and the sequence
of subgoals the policy should reach is outsourced to an existing solver
(Kociemba's algorithm).

These are fine. You can get reinforcement learning to learn to solve a Rubik's
Cube (see [McAleer et al, 2018](https://arxiv.org/abs/1805.07470)), but
the most important part of this work is the sim2real transfer of a dexterous
manipulation task. None of the manipulation problems are made easier if you
use a solver. I don't think the pose estimation is a problem either, since
it's learned from vision anyways.

What I'm less fine with is that the video OpenAI released never mentions this
multistage approach. To quote directly from the narration,

> "We're trying to build robots that learn a little bit like humans do, by trial and error. What we've done is trained an algorithm to solve the Rubik's Cube one-handed, with a robotic hand, which is actually pretty hard even for a human to do. We don't tell it how the hand needs to move the cube in order to get there. The particular friction that's on the fingers. How easy it is to turn the faces on the cube. What the gravity, what the weight of the cube is. All of these things it needs to learn by itself."

To me, this reads as someone saying things that are consistent with the truth,
but which leaves open interpretations that are stronger than the truth. The
phrasing of "We don't tell it how the hand needs to move the cube in order to
[solve it]" certainly doesn't imply any decomposition of the problem, and on
my first listen, I had 3 reactions.

1. They're almost certainly using a solver because not doing so would be really
silly.
2. People who just watch the video will definitely be confused by this.
3. That confusion may have been intentional.

It seems like people's opinion on #3
is almost entirely defined by whether they believe OpenAI's
PR strategy is acting in good faith. For what it's worth, I believe they are
acting in good faith, but they simplified things so much that they lost some
important nuance. To be fair, this happens everywhere. How many times have you
read a paper because of a good abstract, only to be disappointed once you actually read it?

I understand why people are fixated on this, but from a robotics perspective,
it really, really doesn't matter, and other parts deserve more focus.


Sensor Instrumentation
=======================================================================

In the results reporting a 60% average solve rate, the Rubik's Cube used is a
modified version of a Xiaomi Giiker cube, which comes with Bluetooth sensors
that report the rotation angles of each face. The sensors in the original
Giiker cube report face angles at $$90^\circ$$ resolution, so they modify
it by replacing some components to get to $$5^\circ$$ resolution.

This one, I actually do care about, because I couldn't find anywhere in the blog
post where it was clarified that the 60% solve rate required these Bluetooth
sensors. My assumption before reading the paper was that vision + domain
randomization were used to predict both the pose of the cube and the angles of
faces on that cube. They do have some pure vision results, and from purely
vision the solve rate is 20% on average solves and 0% on the hardest solves.

I don't have any particular problem with the added sensors, but I am let down,
because it plays into a bigger theme: for all the claims of sim2real transfer,
there's a long list of simulator details mentioned in the paper.


Simulation Design
========================================================================

I remember when I first heard about domain randomization. I thought it was going
to fix everything. Then I tried it myself, and talked to people who tried it
for their projects, and got more realistic.

The common explanation of domain randomization is that by adding lots of
randomness to your simulator, you can avoid exactly designing your simulator
and performing system identification or calibration. So far, I'd say this
is only sort of true.

Consider the problem of contact forces. Now, I have very little experience with
making physics simulators, but when I talk to colleagues with sim experience,
contact forces make them break out in cold sweats. It's simply very hard to
exactly model the forces between objects that are touching each other.
Somehow, there
are always more interactions that are not properly modelled by the simulator.

The domain randomization viewpoint is that if you randomize frictions
between everything, your model should generalize to real world dynamics without
issue. And *sometimes*, this works, but more commonly, there's complexity in
real-world contact forces that aren't correctly modeled by your simulator, and
you aren't able to recover this, no matter how you randomize things.

Think of it this way. Suppose we were trying to model the movements of two
magnets in simulation, but our simulator doesn't model electromagnetic forces.
It doesn't matter how much you randomize friction or mass, you're never going to
predict the movements of those magnets to any reasonable degree of accuracy.

Obviously, actual simulators will model these forces and other ones if there's
reason to believe they're relevant to the task. I'm just bringing it up as an
example of a known unknown within the simulator. But what about the unknown
unknowns?

If you look through sim2real papers, it's not a coincidence that many of the
best sim2real results are about sim2real transfer of vision, for tasks where
dynamics either don't matter or are simulated pretty well.
When transfer learning is bottlenecked on vision, domain randomization is great!
Convolutional
neural nets are absurdly good, random textures and lighting is something almost
all simulators support, and it seems like it does generalize pretty well.

Unfortunately, practically all interesting robot manipulation problems are
bottlenecked on dynamics.

Some calibration is necessary to get the simulated hand to be
reasonably close to the real one. I missed this last year, but it was true
in their Learning Dexterity paper too. From Appendix C.3 of the Learning
Dexterity paper:

> The MuJoCo XML model of the hand requires many parameters, which are then used as the mean of the randomized distribution of each parameter for the environment.
> Even though substantial randomization is required to achieve good performance on the physical robot, we have found that it is important for the mean of the randomized distributions to correspond to reasonable physical values.
> [...] For each joint, we optimize the damping, equilibrium position, static friction loss, stiffness, margin,and the minimum and maximum of the joint range. For each actuator, we optimize the proportional gain, the force range, and the magnitude of backlash in each direction. Collectively, this corresponds to 264 parameter values.

The Rubik's Cube paper mentions calibration as well, where they added some
tendons and pulleys to their simulated hand model to better match the real
hand.
Appedix D.1 helpfully includes the performance before and after this change.

![Calibration Results Table](/public/openai-rubiks/table.png)
{: .centered }

An increase from 4.8 face rotations to 14.30 face rotations seems like a pivotal
jump to me. Then, for the cube itself, they mention needing to model the
bevelled edges that appear on the real Rubik's Cube, because otherwise the model
is too unforgiving.


Takeaways
--------------------------------------------------------------------------

My understanding is that OpenAI was treating zero-shot sim2real transfer as
a non-negotiable part of the project. This is consistent with their research
directions: throw a bunch of compute at something that easily scales with
compute, and see what you can do in that regime. If you want to do this
in robotics, you have to mostly use simulation, because real robots don't
scale with compute.

So really, once you strip everything old away, and the solver controversary
away, what are we left with? We're left with the story that automatic
domain randomization is better than plain domain randomization, and
domain randomization can work for solving a Rubik's Cube, if you
calibrate your simulator to
be sort-of accurate, and instrument enough randomization
parameters. Like cube size, and action
delay, and action latency, and simulator timestep length, and frictions, and
mass, and action noise, but remember that action noise from a random network
works best, and, well, you get the picture. There's a lot. Basically, I'm
impressed by the effort that went into setting up the simulator and randomization,
and not by the improvements *from* that randomization.

Domain randomization isn't a tool. Domain randomization is a paradigm, and a
very useful one at that. But at a high level, it doesn't fully remove
simulator design. It just trades some software engineer design time for
GPU training time, and the conversion rate depends on whether it's easy to
model a reasonable version of your task in simulation.
