---
layout: page
title: Research
permalink: /research/
---

This is not a standard research page.

Due to confidence issues, I didn't apply to PhD programs this year.
For more complete reasons, you may read this [blog post]({% post_url 2016-01-03-grad-school %}).

The research I've done so far hasn't led to publishable results, but it's
not nothing, and I'm still proud of the work I've done.
I haven't given up on academia just yet, meaning I still need to signal
my research abilities. This page is that signal.


---------------------------------------------

<p></p>

Exploring Boosted Neural Nets for Rubik's Cube Solving

*Spring 2016. Final project for CS 281B, Advanced Topics in Decision Making*


---------------------------------------------

<p></p>

Factored Q-Learning in Continuous State-Action Spaces

*Alex Irpan, mentored by John Schulman*

*Fall 2015. Final project for CS 281A, Statistical Learning Theory*

Overlap between research and class final project. Investigated whether



---------------------------------------------

<p></p>

An Overview of Sublinear Machine Learning Algorithms [[pdf](/public/research/sublinear-algorithms-optimization)]

*Alex Irpan\*, Ronald Kwan\**

*Spring 2015. Final project for CS 270, the introductory graduate course for algorithms*

A summary of papers detailing algorithms for solving SDPs and learning
perceptrons/SVMs in sublinear time, assuming a RAM model. Key ideas:
describe optimization as a max-min game, then sample entries using multiplicative
weights, in a way such that the update is an unbiased estimator of the update
from the standard algorithm.


---------------------------------------------

<p></p>

Integrating Monte Carlo Tree Search with Reinforcement Learning

*Alex Irpan, mentored by John Schulman*

*Fall 2015 - Spring 2015. Research Project*

Experiments with using Monte Carlo Tree Search to get Q-values for
Q-learning. Monte Carlo Tree Search turns a stochastic policy $$\pi$$
into a stronger stochastic policy $$\pi'$$ at the cost of doing search.
The idea was that given some $$\pi$$, we could use $$\pi$$ to get an episode
using MCTS. The rollouts give a natural Q-value on the observed states, which
can be used to update $$\pi$$ to a better $$\pi'$$, which can be fed to MCTS
to get an even better policy, and so on.

EXPLAIN MORE?


---------------------------------------------

<p></p>

Paper Presentation: Hiding Input Size in Two-Party Secure Computation

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

Paper Presentation: Secure Function Evaluation with Garbled Circuits

*Alex Irpan*

*Fall 2015. Final project for CS 276, Cryptography*

Explained Yao's garbled circuits. Presentation notes were adapted
into a blog post that's clearer but less technical.

ADD LINK
