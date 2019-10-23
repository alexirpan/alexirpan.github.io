---
layout: post
title:  "Let's (Briefly) Discuss OpenAI's Rubik's Cube Result"
date:   2019-10-16 01:25:00 -0700
---

Recently, OpenAI announced they had [gotten their dexterous
manipulation system to solve a Rubik's Cube](https://openai.com/blog/solving-rubiks-cube/).
I thought I wouldn't have too much to say, and then this post became longer
than I expected.


What Did OpenAI Do?
----------------------------------------------------------------------

Using reinforcement learning, they learned a controller for a [Shadow Hand](https://www.shadowrobot.com/products/dexterous-hand/)
that lets them solve a Rubik's Cube with reasonable success rate. They
report a success rate of 60% for average scrambles, and 20% for the hardest
possible scrambles (that require 26 quarter-face turns).

I say doing RL on the Shadow Hand platform, but really, I mean they do learning
on a simulated version of the Shadow Hand, then try to get that to transfer to
the real Shadow Hand with no real data.

If you can successfully manipulate a cube, solving it isn't too hard. There
are known search algorithms to find the sequence of turns (Kociemba's
algorithm is the standard one), and they rely on Kociemba's algorithm to
provide the sequence of turns, which the RL policy then executes.

The true result here is the successful dexterous manipulation of the
Rubik's Cube with the Shadow Hand.


Why is Dexterous Manipulation Hard?
-----------------------------------------------------------------------

Okay, big cavaet. I've worked on robotic manipulation, but I haven't worked
on dexterous manipulation with hands before. So, maybe I'm totally off here.
But the TL;DR answer is that hardware is terrible and simulators suck unless
you spend a bunch of time improving them.

OpenAI says they've been working on solving a Rubik's Cube since
May 2017. It took them 2 months (May 2017 - July 2017) to solve it in
simulation with a simulated hand. It took them 1 more year (July 2017 - July 2018)
to get a real hand to manipulate a solid wooden block. Then, another
14 months (July 2018 - October 2019) to get to the Rubik's Cube. The "runs on a
real robot" part is the entire reason the learning problem is difficult.


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

DIAGRAM

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

Finally, this is something I *really* haven't seen enough credit for. The part
I was most excited about in this work wasn't the Rubik's Cube solving. That
felt inevitable, given time. Nor was I that excited about automatic
domain randomization. I'm sure it was important to their work, but
it's well established that automatic curriculum learning works if set up
properly.

I'm most excited by the comments on policy distillation and model surgery.
Although these ideas aren't central to the project, they are indicative
of the right research culture: **a focus on building systems that encourage
long-term research success.**

About 2 years ago, I talked with an OpenAI employee about why OpenAI spent
a lot of time working on Gym and OpenAI Baselines. The paraphrased answer
was that they felt like aspects of research that were undervalued by the
RL community, and OpenAI was in a position to provide value.

It's really stuck with me. Okay, yes, Gym and Baselines are also great
branding tools for recruiting purposes. But this would have been true for
any group that released something that got the adoption of Gym or Baselines.
In general, it's very easy to build something that's only good for one
experiment, or one reserach project. There are a lot of pressures to do
so. But good tooling is actually absurdly helpful for speeding up research,
because if done properly, the investment pays off long-term over all future
research projects. Build an interpretability library, and every project can
try it if they want to. Build RL diagnostics tools, and every RL project
can try them out. TensorFlow exists because Google wanted different ML
teams to use the same ML framework.

I'm not saying it's easy to build good tools. It's really hard to build good
tools, and a lot of times people are reluctant to work on it, because
it's SWE work that's less interesting than the "real" research work. I fall in
this bucket too. But, it's all research work. Research informs what kind of tools
you want to build, and tools feed back into faster research.

THIS IS ABRUPT, BAD

To me, the comments on policy distillation and model surgery indicate that
some people at OpenAI "get it", and that at the organization level, they're
thinking both about the current research project and the systems behind the
research projects.


What Are the Cons of This Work?
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

The common explanation of domain randomization is that by adding lots of
randomness to your simulator, you can avoid the meticulous process of system
identification. I'm starting to think this is only sort of true.

Consider the problem of contact forces. Now, I have very little experience with
making physics simulators, but when I talk to colleagues with sim experience,
contact forces make them break out in cold sweats. It's simply very hard to
model the forces between objects that are touching each other. Somehow, there
are always more interactions that are not properly modelled by the simulator.

Now, the domain randomization viewpoint here is that if you randomize frictions
between everything, your model should generalize to real world dynamics without
issue. And *sometimes*, this works, but more commonly, some aspect of physics
isn't in the space of interactions your simulator can represent. REPHARSE THIS.
Imagine something like modelling the movements of two magnets, in a simulator
that doesn't model electromagnetic forces between objects. It doesn't matter
how much you randomize friction or mass - you're never going to predict the
movement of those magnets.

Obviously simulators will model electromagnetic forces if there's reason to
believe they're relevant to the task at hand, and in fact they do use magnetic
field sensors to estimate joint angles.
I'm just bringing them up as
an example of a known unknown. What do you do about the unknown unknowns?
The dynamical effects that are out of the space of any of your randomized simulators?

If you look through sim2real papers, it's not a coincidence that many of the
best sim2real results are about sim2real transfer of vision, for tasks with
limited dynamics mismatch. If the transfer
learning is bottlenecked on vision, domain randomization is great! Convolutional
neural nets are absurdly good, random textures and lighting is something almost
all simulators support, and if tuned properly it should just work.

Unfortunately, practically all interesting robot manipulation problems are
bottlenecked on dynamics.


What Was I Talking About Again? Right, Rubik's Cube
-------------------------------------------------------------------------------

The reason I'm bringing up all my domain randomization opinions is because on
a closer read, the Rubik's Cube result is much less of a win story for
domain randomization than I thought. Even with randomization, simulator calibration
has a noticeable effect on their results.

I missed this before, but this was true in their Learning Dexterity result
as well. From Appendix C.3 of that paper:

> The MuJoCo XML model of the hand requires many parameters, which are then used as the mean of the randomized distribution of each parameter for the environment.
> Even though substantial randomization is required to achieve good performance on the physical robot, we have found that it is important for the mean of the randomized distributions to correspond to reasonable physical values.
> [...] For each joint, we optimize the damping, equilibrium position, static friction loss, stiffness, margin,and the minimum and maximum of the joint range. For each actuator, we optimize the proportionalgain, the force range, and the magnitude of backlash in each direction. Collectively, this corresponds to 264 parameter values.

UPDATE THIS PART TO CLARIFY IT'S FROM THE HAND

> We test how much of an impact simulation calibration has. [...] We evaluate a
> policy trained on the old simulation and on the new simulation (i.e. with
> coupling and dynamics calibration).

The results table says they say an increase from 4.8 successful face rotations
to 14.30 face rotations. That's a pretty big jump!

In addition, Section 4.2 of the paper



BETTER TITLE
-----------------------------------------------------------


One question you may have is, "why don't they train with real data?" In robotics,
real data is generally much more useful than simulated data. My understanding
is that two things are at play. First, OpenAI is curious how far they can
push zero-shot sim2real transfer, because simulation scales with compute while
real robot doesn't. Second, OpenAI's goal is to show that deep reinforcement
learning can solve difficult robotics problems. Therefore, they've set their
sights on a problem hard enough that simulation is the *only* way they'd be
able to get enough data for RL to learn something.
