---
layout: post
title:  "A Readthrough of Wasserstein GAN"
date:   2017-02-12 16:12:00 -0800
---

These are personal notes about the Wasserstein GAN paper that other people
may find useful. The notes are written for me - as such I'm putting very little
effort into making sure they're clear to others.

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
be good for me to know the ideas from this paper.
