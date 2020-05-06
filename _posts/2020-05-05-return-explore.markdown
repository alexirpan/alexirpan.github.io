---
layout: post
title:  "A Reinforcement Learning Potpourri"
date:   2020-05-05 22:53:00 -0700
---

I've fallen behind on RL literature reading the past few months, in part because
the projects I'm working on have less RL focus. However, I'm still tuned in
enough to hear about papers super relevant to my interests.

First Return Then Explore
-------------------------------------------------------

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

Both First Return Then Explore and Go-Explore
aim to first return to a state that has been visited before, then explore from
that state. To make this more efficient, states are grouped into "cells"
through some encoding. In the original Go-Explore paper, these cells are defined
by downsampling by a fixed factor. First Return Then Explore changes this to
tune the downsampling factor online, by doing a small search to maximize
normalized entropy across a fixed budget of $$T$$ cells. There are also
more heuristics on choosing which cell to return to, instead of uniformly at
random.

Besides this change, the Atari experiments mostly operate the same way:
they assume a simulator or deterministic environment, learn the policy by
leveraging the determinism, then do a robustification step where they try to
reproduce behavior in a stochastic version of the environment.

The part I care about is the part they call Policy-based Go-Explore. My main
criticism of the first version was that it required access to a deterministic
analogue of your final environment. They proposed learning a goal-conditioned
policy to return to previous states, instead of following a memorized trajectory.
but didn't have any results for it.

Well, now they have results. They're quite nice, but it appears that it
was only tested on Montezuma's Revenge with domain-specific features. I
follow an anthropic principle based view of papers: if there's an experiment that's
natural in the paper's context, but isn't in the paper, then it probably didn't work.
So for now, I'm assuming it didn't beat SOTA with domain agnostic features.

My final verdict is that this paper is an even stronger case that good exploration
can be reduced to learning to quickly return to states you've visited before.
It continues to be a good argument that detachment and derailment are
important concepts that pure intrinsic motivation doesn't always handle.
Learning that return policy, however, is still an open problem for general
domains.

The reduction is valuable, and I hope it encourages more work on efficiently
learning goal-conditioned policies.


Data Augmentation
------------------------------------------------------------------

The new hotness for RL is data augmentation. Three papers came out on arXiv in the
past week: [Constrastive Unsupervised Reinforcement Learning (CURL)](https://arxiv.org/abs/2004.04136), from Srinivas and Laskin et al, [Image Augmentation is All You Need (DrQ)](https://arxiv.org/abs/2004.13649) from Kostrikov and Yarats et al, and
[Reinforcement Learning with Augmented Data (RAD)](https://arxiv.org/abs/2004.14990) from Laskin and Lee et al.
It also made it to [VentureBeat](https://venturebeat.com/2020/05/02/uc-berkeley-researchers-open-source-rad-to-improve-any-reinforcement-learning-algorithm/)
of all places.

These three papers all find that for image-based RL, data augmentation gives
very large gains on several tasks. Now at this point, I should mention that CURL
and RAD are from people at UC Berkeley I know, and DrQ is from people I know
from Google internships, so I'm going to step very carefully.

CURL learns a representation by contrastive learning. Two randomly sampled
data augmnetations are applied to the same image, and their representations are
encouraged to be close to one another through an InfoNCE loss. (See the
[SimCLR paper](https://arxiv.org/abs/2002.05709) for an ablation showing this
contrastive loss does better than other ones.)

RAD compares just using data augmentation, without any contrastive losses, and
finds that it outperforms CURL on the DMControl Suite. The theory is that in
these environments, RAD beats CURL because it only optimizes for the task reward
we care about, while CURL has to balance RL and constrastive learning. An
ablation of the data augmentations used finds that random cropping is by far
the most important data augmentation.

DrQ also does data augmentation, using random shifts. This is the same
as padding the image, then doing a random crop. In an actor-critic framework,
they sample data augmentations to
estimate $$Q(s,a)$$, sample other data augmentations to estimate target Q-value $$Q(s', a')$$,
and use this to regularize the learning.

Each paper positions themselves a bit differently. If you're interested, you
can read more.

Now, are these results surprising? Uh, kind of? It isn't surprising because
data augmentation isn't new.
Specifically doing random cropping isn't
new either - the [QT-Opt](https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html) paper
I worked on always used random cropping in its RL. Other groups have used
data augmentation as well.

The distinction is that these papers are the first to carefully design
an experimental setup to measure the effects of data augmentation, and they've
all found the effect is pretty large. It's the sort of paper that makes you
feel dumb you didn't write it yourself. (Especially because I've even run
data augmentation ablations before, just never on the standard RL benchmarks.)

I'm very big on data augmentation. It just seems like the obvious thing to do.
You can either view it as multiplying the size of your dataset by a constant factor,
or you can view it as decreasing the probability your model learns a spurious
correlation, but in either case it usually doesn't hurt and it often really
helps.


AI Economist
--------------------------------------------------------------------------

Salesforce put out a paper that uses [reinforcement learning to design
tax policy in a toy economic environment](https://www.salesforce.com/company/news-press/stories/2020/4/salesforce-ai-economist/),
and they argue their tax policies give better equality-productivity
trade-offs, compared to the Saez framework.

I do not understand tax policy very well, but my first instinct is that
the economy is really complicated, a model of the economy has to be
too simplistic somewhere, and therefore the results should be taken with massive
caveats. However, the authors are aware of this, they did partner with an
Economics professor, and the ideas it's playing with are interesting. For papers
like this, I've found they are best viewed as idea generators. Within a model,
the AI discovers a new strategy, which could be useful in the more complex
environment. However, that strategy should be reviewed by humans first.

Within the simulated economy, the agent preferred higher tax rates for the
top brackets and lower tax rates for the middle class. So that's interesting.

That being said, I think it's very unlikely this makes it to actual tax policy
anytime soon. The real economy is more complicated, the politics is a nightmare
to navigate, and the people in charge of
policy probably care more about the perception of a good economy than a truly good
economy. Given the ethics questions around economics experiments, perhaps that's
for the best.


Offline Reinforcement Learning
----------------------------------------------------------------------------

https://arxiv.org/abs/2005.01643
