---
layout: page
title: Research
permalink: /research/
---

*Last updated June 9, 2016.*

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

Poster (click for full size):

[![Poster](/public/research/posterimage.png)](/public/research/poster.pdf)

NIPS submission (in review but almost certain rejection): [PDF](/public/research/nips_2016.pdf)

Code: [GitHub](https://github.com/alexirpan/rubik_research)

Project where I tried training a neural net to learn how to
solve a Rubik's Cube from raw features. Originally a small side project, but it
grew over time, eventually turning into an experiment
to see if AdaBoost reweighting while training could improve training
time or accuracy.
The short answer is that it did neither. The long answer
is in the submission.


---------------------------------------------

<p></p>

**Factored Q-Learning in Continuous State-Action Spaces**

*Alex Irpan, mentored by John Schulman*

*Fall 2015. Final project for CS 281A, Statistical Learning Theory*

Poster (click for full size):

[![281A Poster](/public/research/281aposterimage.png)](/public/research/281aposter.pdf)

Informal Writeup: [PDF](/public/research/281areport.pdf)

Code: [BitBucket](https://bitbucket.org/airpan/fall15-research)

The intention of this project was to
apply factorization to discretized multi-dimensional continuous MDPs,
but I had difficulty getting Q-learning to work in small continuous MDPs,
and there was no point moving forward until the small case worked.
Experimental results from the poster are from a discrete MDP, the Atari
game Asteroids.

I'm still interested in stochastic policies based on graphical models,
but have too many other things on my plate.


---------------------------------------------

<p></p>

**An Overview of Sublinear Machine Learning Algorithms**

*Alex Irpan\*, Ronald Kwan\* (worked equally)*

*Spring 2015. Final project for CS 270, the introductory grad level algorithms course*

Report: [PDF](/public/research/sublinear-algorithms-optimization.pdf)

A summary of algorithms for solving SDPs and learning
perceptrons/SVMs in sublinear time. Each shares the same approach:
describe the optimization problem as a max-min game, and sample an
estimate of the gradient, which can be done in sublinear time.
Multiplicative weights and concentration inequalities glues the proof together.


---------------------------------------------

<p></p>

**Integrating Monte Carlo Tree Search with Reinforcement Learning**

*Alex Irpan, mentored by John Schulman*

*Fall 2015 - Spring 2015. Research Project*

Code: [BitBucket](https://bitbucket.org/airpan/research-code)

My first research project ever, where I experimented with integrating Monte
Carlo Tree Search with Q-learning on the toy problem of Connect Four.
The goal was to use MCTS for policy improvement. MCTS turns a bad
rollout policy $$\pi$$ into a better one while producing reasonably
accurate Q-values. Q-learning improves rollout policy $$\pi$$. MCTS on
the improved $$\pi$$ gives more accurate Q-values, and so on.
I didn't know about policy gradient at the time;
I probably would have used that if I knew it.

The goals I had were better implemented in this [NIPS paper](http://papers.nips.cc/paper/5421-deep-learning-for-real-time-atari-game-play-using-offline-monte-carlo-tree-search-planning)
and in AlphaGo,
so I don't see much use in revisiting this.


---------------------------------------------

<p></p>

**Presentation: Secure Function Evaluation with Garbled Circuits**

*Alex Irpan*

*Fall 2015. Final project for CS 276, Cryptography*

Blog post: [here]({% post_url 2016-02-11-secure-computation %})

A presentation on Yao's garbled circuits, the first solution to securely
computing functions between two semi-honest parties. I have presentation notes,
but they're messy. The blog post is more refined and has more
intuition.


---------------------------------------------

<p></p>

**Presentation: Hiding Input Size in Two-Party Secure Computation**

*Alex Irpan*

*Spring 2016. Final project for CS 294, Secure Computation*u

Presentation Notes: [PDF](/public/research/hiding_input_size.pdf)

Garbled circuits implicitly leak the input size of both parties, so can we do
better? A paper by Lindell, Nissim, and Orlandi on hiding input size helps
answer this question.
Presented the construction for one case assuming fully homomorphic encryption,
and impossibility proofs for other cases.

