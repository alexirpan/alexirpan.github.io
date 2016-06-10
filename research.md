---
layout: page
title: Research
permalink: /research/
---

*Last updated June 10, 2016.*

This is not a standard research page.

Due to confidence issues, I didn't apply to PhD programs senior year.
My more complete reasoning is in this [blog post]({% post_url 2016-01-03-grad-school %}).

The research I've done hasn't led to publishable results, but it's
not nothing. I'm still proud of it, and want to share it, in the off chance
someone finds it neat.
(I also haven't given up on academia just yet, so this page also
signals my research capabilities in case I apply in the future.)

Project list:

- Clobbered for auto generated table of contents
{:toc}


---------------------------------------------

<p></p>

# Exploring Boosted Neural Nets for Rubik's Cube Solving

*Alex Irpan*

*Spring 2016. Final project for CS 281B, Advanced Topics in Decision Making*

Poster (click for full size):

[![Poster](/public/research/posterimage.png)](/public/research/poster.pdf)

NIPS submission (in review but almost certain rejection): [PDF](/public/research/nips_2016.pdf)

Code: [GitHub](https://github.com/alexirpan/rubik_research)

Project where I trained neural nets mapping raw features to Rubik's Cube moves.
Started as a small side project, but
grew over time, eventually turning into an experiment
to see if AdaBoost reweighting while training could improve training
time or accuracy.
The short answer is that it did neither. For details, see the submission.


---------------------------------------------

<p></p>

# Factored Q-Learning in Continuous State-Action Spaces

*Alex Irpan, mentored by John Schulman*

*Fall 2015. Final project for CS 281A, Statistical Learning Theory*

Poster (click for full size):

[![281A Poster](/public/research/281aposterimage.png)](/public/research/281aposter.pdf)

Informal Writeup: [PDF](/public/research/281areport.pdf)

Code: [BitBucket](https://bitbucket.org/airpan/fall15-research)

The intention of this project was to
add independence assumptions between different dimensions of the action space to
decrease model size,
with specific application to discretized continuous MDPs.
Unfortunately I had difficulty getting Q-learning to work in small
continuous MDPs,
and there was no point moving forward until the small case worked.
Experimental results from the poster are from a discrete MDP, the Atari
game Asteroids.

Results were a wash, but I like some of the ideas here. I still want to test
stochastic policies based on graphical models,
but have too many other things on my plate.


---------------------------------------------

<p></p>

# An Overview of Sublinear Machine Learning Algorithms

*Alex Irpan\*, Ronald Kwan\* (worked equally)*

*Spring 2015. Final project for CS 270, Combinatorial Algorithms and Data Structures*

Report: [PDF](/public/research/sublinear-algorithms-optimization.pdf)

Summarizes algorithms for solving SDPs and learning
perceptrons/SVMs in sublinear time, including their performance proogs.
Each shares the same approach:
describe the optimization problem as a max-min game, and sample an
estimate of the gradient, which can be done in sublinear time.
Multiplicative weights and concentration inequalities glues the proofs together.


---------------------------------------------

<p></p>

# Integrating Monte Carlo Tree Search with Reinforcement Learning

*Alex Irpan, mentored by John Schulman*

*Fall 2014 - Spring 2015*

Code: [BitBucket](https://bitbucket.org/airpan/research-code)

My first research project. I experimented with integrating Monte
Carlo Tree Search with Q-learning on the toy problem of Connect Four.
The goal was to use MCTS for policy improvement. MCTS turns a bad
rollout policy $$\pi$$ into a better one while producing reasonably
accurate Q-values. Q-learning improves rollout policy $$\pi$$. MCTS on
the improved $$\pi$$ gives more accurate Q-values, which can further
improve $$\pi$$, and so on.

The goals I had were better implemented in this [NIPS paper](http://papers.nips.cc/paper/5421-deep-learning-for-real-time-atari-game-play-using-offline-monte-carlo-tree-search-planning)
and in AlphaGo, so I don't see much use in revisiting this.


---------------------------------------------

<p></p>

# Presentation: Secure Function Evaluation with Garbled Circuits

*Alex Irpan*

*Fall 2015. Final project for CS 276, Cryptography*

Blog post: [here]({% post_url 2016-02-11-secure-computation %})

A presentation on Yao's garbled circuits, the first solution to securely
computing functions between two semi-honest parties. I have presentation notes,
but they're messy. The blog post is more refined and has more
intuition.


---------------------------------------------

<p></p>

# Presentation: Hiding Input Size in Two-Party Secure Computation

*Alex Irpan*

*Spring 2016. Final project for CS 294, Secure Computation*

Presentation Notes: [PDF](/public/research/hiding_input_size.pdf)

Garbled circuits implicitly leak the input size of both parties. Can we do
better? A paper by Lindell, Nissim, and Orlandi on hiding input size helps
answer this question.
Presented the construction for one case assuming fully homomorphic encryption,
and impossibility proofs for other cases.

