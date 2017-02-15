---
layout: post
title:  "Readthrough: Wasserstein GAN"
date:   2017-02-12 16:12:00 -0800
---

These are personal notes about the Wasserstein GAN paper that I made as I read
through the paper. The notes are written for me - as such I'm putting very
little effort into making sure they're clear to others, and will be very loose
with notataion. My hope is that parts of this will still be comprehensible.

Why Is This Paper Important?
----------------------------------------------------------------------

This paper makes a bunch of interesting points.

* Proposes a new GAN training algorithm that produces pretty good samples on
various datasets.
* Said training algorithm is justified by theory. The pattern I've seen in
deep learning is that not all theory-justified papers have good experimental
results, but theory-justified papers with good empirical results have *really*
good empirical results.
* Shows a correlation between loss and perceptual quality. This is actually
huge if it holds up across different problems. In my limited GAN experience,
one of the big problems is that the loss doesn't really mean anything, thanks
to adversarial training. Reinforcement learning has a similar problem, but
at least we have episode reward. GANs only get, I don't know, Mechanical Turk.
Even a rough quantitative measure of quality could be good enough to
use tricks like early stopping.

So, even though I'm not a GAN person, this paper has the potential to change
the game on GANs, and even if I don't use GANs in the near future, it'll likely
be good for me to know the ideas from this paper. This is especially true
because I buy Oriol's argument that GANs have close ties to actor-critic
reinforcement learning.

Introduction
-----------------------------------------------------------------------

(You may want to pick up the paper and start scanning through it yourself
at this point.)

Alright, sets up the problem of learning a probability distribution, by
finding the best distribution out of a parametrized
function family $$(P_\theta)$$.

They say that in the limit, maximizing the likelihood is equivalent to
minimizing $$KL(P_r \| P_\theta)$$, which sounds reasonable. It's been
a while since I verified the math but that's fine. They then say that
if distribution $$P_\theta$$ has low dimensional support (say if the dimensionality
of $$\theta$$ isn't high enough), then the KL distance isn't defined
or is infinite.

This pans out, remember that

$$
    KL(P || Q) = \sum_p p\log{p} - \sum_p p\log{q}
$$

If $$P_\theta$$ is 0 when $$P_r$$ isn't 0, then the latter summation will go to $$\infty$$.

(Yes, I know that these distributions are continuous, but my intuition refuses
to accept continuous distributions as a thing. I use summations in my head, and
assume that with nice enough distributions, I can turn all the sums into integrals
and everything will just work out.)

So to get around this, we need to add a dis
