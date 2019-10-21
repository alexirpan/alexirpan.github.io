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
answer is that hardware is terrible and simulators suck unless you spend a
bunch of time improving them.

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

I say doing RL on the Shadow Hand platform, but really, I mean they do learning
on a simulated version of the Shadow Hand, then try to get that to transfer to
the real Shadow Hand with no real data.


What's New?
-------------------------------------------------------------------------------

From a learning perspective, there actually isn't that much.
This looks like a ["moonshot achieved through roofshots"](https://rework.withgoogle.com/blog/the-roofshot-manifesto/)
project, where there's a clear line of steady, compounding improvements.

It's easier to start with what isn't new. The model is trained using
distributed PPO with OpenAI's Rapid framework, which was used for both DotA 2
and the original Learning Dexterity paper.
The model architecture is reminiscent of the DotA 2 architecture - different
input features are embedded into a
512-dimensional embedding space, then summed together and passed through a
large LSTM. Like the Learning Dexterity work, instead of learning a policy
directly on pixels through RL, they instead predict the pose of the Rubik's
Cube from three camera images, then feed those predicted poses to the RL
agent. Again, like the Learning Dexterity work, they use the same asymmetric
actor-critic trick, where the critic gets all ground truth state information,
and the policy only gets the features visible from real-world data, which
is fine for zero-shot transfer because you only need the policy at inference
time.

It's clear that the Rubik's Cube result is the same ideas, re-executed in a
new context. And that's fine, that's how almost all research goes. You try what
should work, and then it gets you partway, and then you need a few new ideas to
get further through.

One is the *automatic domain randomization*. In domain randomization, you
randomly change several aspects of the simulator, learning a model against all
those variations. This makes the final model more robust and makes it transfer
better to the real world. However, applying it requires some tuning. Too
little randomization, and the model won't be robust enough for the real world.
Too much, and the learning problem becomes too hard to learn.

The proposed solution is to take inspiration from automatic curriculum learning.
We maintain a distribution over simulator parameters, starting with just a
single point. If the policy reaches a certain performance threshold, we expand
the distribution. This lets the model to learn a simpler task, before
learning a more randomized (more difficult) task.

One detail which I only found after a close reading was that they also do
*adversarial domain randomization*. An adversary applies perturbations to the
force, torque, and actions, in a way that hurts performance...or rather, that's
the theory. In practice, a random network (re-initialized every episode)
performed better than any attempt to learn the adversary. This seems weird
to me - I can believe the result, but my intuition is still too optimistic
about adversarial learning to fully believe it.

From a learning perspective, the final new thing is a heavier lean on
*policy distillation* and *model surgery*. This is a lesson they've carried
over from DotA 2. Over the course of a long project, you will naturally want
add new input features or try new neural net architectures. If the model takes
a long time to train, it's worth designing methods that let you do this without
training from scratch. Their model architecture is always structured as one
that embeds each feature into a separate embedding that is added together, and
the reason is because when you add a new feature, the added parameters don't
change the semantic meaning of any other parameter, leaving you closer to a good
initialization.

DIAGRAM

For approaches that aren't compatible with this (like changing the LSTM size),
existing models can be distilled into the new model architecture, which runs
much faster than training from scratch.


Is This Actually Impressive?
-----------------------------------------------------------------------------

And now we dive into some of the more controversial aspects. Like every press
release, there are hidden details, and like every press release, these hidden
details make the work less impressive.

(I want to be very clear here: this is not a shot at OpenAI, or at scientific
press reporting. It's something shared by all papers. You open a research paper,
and the abstract sounds great. You read it some more, and it starts looking
worse. That's how it goes.)

As mentioned before,
the final robot controller is not learned entirely end-to-end from pixels to
action. There's an intermediate step of estimating pose, and then learning
from approximate pose to actions.

The same is true of the solving algorithm. Reinforcement learning is not
used to decide what moves are needed to solve the cube. Instead, the cube's
state is fed to an existing solver (Kociemba's algorithm), and this is
translated to a series of instructions, of the form "rotate the top face clockwise",
"rotate the top face counterclockwise", and "orient the cube such that the
top face is the one we want to turn". This is treated as a sequence of subgoals,
and the model's job is to achieve each of these subgoals in order.

This is fine. You can get a reinforcement learning algorithm to learn how to
solve a Rubik's Cube, but there's no point in doing so when the real research
question is robot dexterity and manipulation. This isn't the controversial
part. The controversial part is that the press video never talks about this
multistage approach. By some readings, the video heavily implies that it *was*
learned end-to-end, without ever saying so.

Let me quote directly from the video.

> "We're trying to build robots that learn a little bit like humans do, by trial and error. What we've done is trained an algorithm to solve the Rubik's Cube one-handed, with a robotic hand, which is actually pretty hard even for a human to do. We don't tell it how the hand needs to move the cube in order to get there. The particular friction that's on the fingers. How easy it is to turn the faces on the cube. What the gravity, what the weight of the cube is. All of these things it needs to learn by itself."

I do actually agree with this criticism. In particular, when the narration says
"We don't tell it how the hand needs to move the cube in order to get there",
I know that this is consistent with the truth: the hand is not told what forces
need to be applied at what joints to get the desired movement of the cube. I
also know that there is another interpretation consistent with this
statement - that machine
learning is used to both learn the sequence of moves, and what moves to
execute.

The number one lesson of writing is that what you intend to say does not
matter. What matters is the interpretation people take away from it. If you're
trying to be clear, you want your intention to match the interpretation.
If, on the other hand, your writing is
deliberately misleading, then you can get people to believe things you've
never actually said.

The question, then, is whether OpenAI was deliberately misleading, or if they
were trying so hard to strip details that they ended up stripping important
ones. I'm not touching this, because the arguments I've read suggest it's mostly
defined by your prior on whether OpenAI does good research or not. So let's move
on.


Simulation Design
------------------------------------------------------------------------------

I remember when I first heard about domain randomization. I thought it was going
to fix everything. Then I tried it myself, and talked to people who tried it
for their projects, and got more realistic.

If your sim2real transfer difficulties are bottlenecked on vision, then domain
randomization is great. Define some random textures and lighting, instrument
your simulator, then go to town. I think vision problems naturally lend themselves
to invariance, and randomization is essentially a way to augment training
data to not care about certain parts of the environment. If you're trying to
estimate the pose of an object from vision, it doesn't matter what color or
texture that object is.

If your sim2real transfer problem is bottlenecked on physics and dynamics, then
you have problems. Unfortunately, almost all interesting manipulation problems
are bottlenecked on dynamics.

That's just my opinion, so let me justify it. Consider the problem of contact
forces. How should we model the forces between objects that are touching each
other? Physics simulators do okay at this, but also have many, many imperfections.



One question you may have is, "why don't they train with real data?" In robotics,
real data is generally much more useful than simulated data. My understanding
is that two things are at play. First, OpenAI is curious how far they can
push zero-shot sim2real transfer, because simulation scales with compute while
real robot doesn't. Second, OpenAI's goal is to show that deep reinforcement
learning can solve difficult robotics problems. Therefore, they've set their
sights on a problem hard enough that simulation is the *only* way they'd be
able to get enough data for RL to learn something.
