---
layout: post
title:  "A Reinforcement Learning Potpourri"
date:   2020-05-05 22:53:00 -0700
---

I've fallen behind on RL literature reading the past few months, in part because
the projects I'm working on have less RL focus. However, I'm still tuned in
enough to hear about papers super relevant to my interests.

Let's start with [First Return Then Explore](https://arxiv.org/abs/2004.12919),
by Ecoffet et al. This is an extension of the Go-Explore work from UberAI.

When Go-Explore first came out, I was very excited by its announced results,
but got upset by how they were presented.
I wrote [a post]({% post_url 2018-11-27-go-explore %}) attempting to explain
that tension - that I really liked the paper's ideas, and really disliked
its media strategy. The media strategy for First Return Then Explore is comparatively
muted. For one, this time they actually have an arXiv paper! (Sorry, I'm
never going to stop ribbing them for that.) They've also been more careful in
their claims, and have improved their previous results.

A quick review of Go-Explore: both First Return Then Explore and Go-Explore
aim to first return to a state that has been visited before, then explore from
that state. To make this more efficient, states are grouped into "cells"
through some encoding. In the original Go-Explore paper, these cells are defined
by downsampling by a fixed factor.

On a skim, for the Atari experiments, the only change is that this downsampling
is tuned online, by doing a small search to maximize normalized entropy across
a fixed budget of $$T$$ cells.

The part I care about is the part they call Policy-based Go-Explore. My main
criticism of the first version was that if you don't have access to a deterministic
analogue of your final environment, then you're stuck. The solution proposed was
to learn a goal-conditioned policy, then return to states by following that
policy conditioned on the desired goal state. That sounds fine, but I expected
it would be hard to learn that in a stochastic environment.

Looking at the results, I still think it's hard. It appears that the only
policy-based Go-Explore results they have use domain knowledge features. I'm
assuming that they would have included domain-agnostic results if they had
gotten that to work well, and that therefore the domain-agnostic methods still
struggled a bit.

Final verdict: the paper is an even stronger case that good exploration can
be reduced to learning to quickly return to states you've visited before.
Learning that return policy, however, is still an open problem for general
domains, but the reduction is valuable, and I hope it encourages more work
on goal-conditioned policies.



