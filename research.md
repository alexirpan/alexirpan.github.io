---
layout: page
title: Research
permalink: /research/
---

*Last updated June 7, 2016.*

This is not a standard research page.

Due to confidence issues, I didn't apply to PhD programs senior year.
My more complete reasoning is in this [blog post]({% post_url 2016-01-03-grad-school %}).

The research I've done hasn't led to publishable results, but it's
not nothing. I'm still proud of it, and want to share it, in the off chance
someone finds it neat.

(Additionally, I haven't given up on academia just yet, meaning I need
to signal my research capabilities in case I apply in the future.
This page is that signal.)


---------------------------------------------

<p></p>

**Exploring Boosted Neural Nets for Rubik's Cube Solving**

*Alex Irpan*

*Spring 2016. Final project for CS 281B, Advanced Topics in Decision Making*

Poster (click for full-size PDF):

[![Poster](/public/research/posterimage.png)](/public/research/poster.pdf)

NIPS submission (in review but almost certain rejection): [PDF](/public/research/nips_2016.pdf)

I originally started a side project of training a neural net to learn how to
solve a Rubik's Cube from raw features. Over time, it grew into a life of its
own, eventually pulling in ideas from boosting and turning into an experiment
to see if AdaBoost reweighting could guide neural net training while giving
a natural ensemble model. The short answer is that it didn't. The long answer
is in the submission.



---------------------------------------------

<p></p>

**Factored Q-Learning in Continuous State-Action Spaces**

*Alex Irpan, mentored by John Schulman*

*Fall 2015. Final project for CS 281A, Statistical Learning Theory*

Poster (click for full-size PDF):

[![281A Poster](/public/research/281aposterimage.png)](/public/research/281aposter.pdf)

Informal Writeup: [PDF](/public/research/281areport.pdf)

The title is misleading. Although the intention of this project was to
apply factorization to discretized multi-dimensional continuous MDPs,
I had difficulty getting Q-learning to work in small cases, and there was no
point moving forward until the small case worked.
The experimental results from the poster are from the Atari game Asteroids,
a problem with a discrete action space.

I'm still interested in representing stochastic policies with graphical
models instead of joint distributions over all actions, but not interested enough
to try implementing it.


---------------------------------------------

<p></p>

**An Overview of Sublinear Machine Learning Algorithms**

*Alex Irpan\*, Ronald Kwan\**

*Spring 2015. Final project for CS 270, the introductory graduate course for algorithms*

Report: [PDF](/public/research/sublinear-algorithms-optimization.pdf)

A summary of papers detailing algorithms for solving SDPs and learning
perceptrons/SVMs in sublinear time. Each paper uses a similar approach:
describe the optimization problem as a max-min game, then sample entries
from the data matrix using multiplicative weights. The sampled entries
are used to compute an unbiased estimator of the update each iteration.
Tons of concentration inequalities glue it all into a sublinear run-time
bound.


---------------------------------------------

<p></p>

**Integrating Monte Carlo Tree Search with Reinforcement Learning**

*Alex Irpan, mentored by John Schulman*

*Fall 2015 - Spring 2015. Research Project*

Experiments with using Monte Carlo Tree Search to get Q-values for
Q-learning. Monte Carlo Tree Search turns a stochastic policy $$\pi$$
into a stronger stochastic policy $$\pi'$$ at the cost of doing search.
The idea was that given some $$\pi$$, we could use $$\pi$$ to get an episode
using MCTS. The rollouts give a natural Q-value on the observed states, which
can be used to update $$\pi$$ to a better $$\pi'$$, which can be fed to MCTS
to get an even better policy, and so on.


---------------------------------------------

<p></p>

**Presentation: Hiding Input Size in Two-Party Secure Computation**

*Alex Irpan*

*Spring 2016. Final project for CS 294, Secure Computation*

Explained Yindell and Pinkas (CHECK) work on securely computing functions
while hiding input sizes. In the semi-honest setting, functions with
bounded output size are always securely computable while hiding one party's
input size, assuming FHE. The unbounded case is impossible in general, and
it is also impossible to hide both party's input size except for functions with
small communication efficiency.


---------------------------------------------

<p></p>

**Presentation: Secure Function Evaluation with Garbled Circuits**

*Alex Irpan*

*Fall 2015. Final project for CS 276, Cryptography*

A presentation on Yao's garbled circuits, the first solution to securely
computing functions between two semi-honest parties. The presentation notes
were adapted into this [blog post]({% post_url 2016-02-11-secure-computation %}).
