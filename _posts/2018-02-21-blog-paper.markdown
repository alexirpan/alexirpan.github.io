---
layout: post
title:  "Blog Posts and Research Papers"
date:   2018-02-21 01:01:00 -0800
---

I've been blown away by the reception to my most recent "Deep RL Doesn't
Work Yet" blog post. In retrospect, it was a perfect storm - I spent a lot of
time on the post, it was about a popular subject, most people agreed with
the post's overarching message, and yet very few people had written anything
similar.

To any new readers I might have: prepare to be disappointed. There is a good
chance I'll never write anything as good or as popular again. It's a weird
feeling, but in the interest of avoiding  "A [Tough Act To Follow](http://tvtropes.org/pmwiki/pmwiki.php/Main/ToughActToFollow)",
I'm planning to write shorter posts, released more frequently.

To close the thread on the deep RL post: why did I decide to make it a blog
post, instead of a paper? In some sense, it could have been a paper. The post
lies somewhere between a survey paper and a policy paper, and although there isn't
a great venue for either, I could have thrown it on arXiv if I wanted to.

However, I do think it needed to be a blog post, for a few reasons.

First of all, I knew going on that I wanted videos of learned agents. It is
so, so much easier to explain agent behavior if you can actually show recordings
of those agents. Papers often come with a recorded video, but this is often
relegated as supplemental material that can be skipped. I didn't want people to
skip my videos.

Secondly, I deliberately wanted a more colloquial tone that wasn't a great fit
for a paper. If it wasn't clear from the Futurama meme, the post was never
trying to be scholarly or formal. I felt it was easier for me to explain myself
that way. It's not that formal writing is a bad writing style. It's more that
there's a time and place for it, and the points I wanted to make didn't
require formal writing - so I just didn't write it that way.

The third reason is going to sound pretentious, but the medium of writing
affects expectations about that writing. Maybe it's just me, but I feel like
research papers are always implicitly trying to present something that's true
about the world. Usually, that truth is, "here is a problem, which has had
several approaches, and we demonstrate that our approach performs better."
On the other hand, blog posts can be much more opinionated. Both blog posts
and papers try to argue something by presenting evidence that supports
that argument, and explaining away evidence that refutes it. However, I feel
like the standard needed for a blog post is a lot lower, and that makes them
well-suited for arguments about more nebulous things, like the state of a field.
I'm glad that people are agreeing with my post, but at the time of writing it,
I knew that people might have disagreed with the entire thing. I was fine with
that, as long as it was clear why I arrived at the conclusions I did.

The fourth was that my target audience was much narrower than the audience for
a research paper. I was specifically writing towards people who either worked
on deep RL, or had a lot of interest in deep RL. If you were in neither
category and liked the post anyways, consider yourself lucky.

When you're new to a field, research papers are a dense yet rewarding gold mine.
The introduction talks about a problem you didn't even know existed. The
related work is a treasure trove of papers to read as follow-ups. The methods
and experiment sections will take time to work through, but will explain the
idea and how it worked out in practice.

Once you have experience in a field, research papers become shockingly
inefficient. The introduction covers a problem you've known about for months,
if not years. The related work section cites mostly papers you've heard about,
and exists just to convince other researchers that you've seen their work. The
methods section is filled with preamble and boilerplate. By now, I've probably
read over a hundred different introductions of RL, Q-Learning, and
policy gradient.


Research papers are for explaining new research. They do so according to
fairly strict constraints. There must be an introduction, explaining the
problem. There must be a related work section, citing every recent paper
that tried the same problem. There must be a methods section, there have
to be experiments, and there has to be a conclusion. In deep learning, it
also all has to fit in 8 pages, since that's a common page limit for
several conferences.

Once you have experience in a field, research papers are a shockingly
inefficient way of explaining knowledge.
The introduction and related
work sections are great when you're new, but veterans will already know
what your problem is and what's been done on it recently. The methods
section explains everything in detail to stay accountable, but veterans
can often get away with skimming a paper for the key idea, letting their
latent knowledge fill in the gaps. As an example, it feels like every RL paper
explains that policy $$\pi$$ is trained to maximize reward in an environment,
or defines what a $$Q$$-function is.
I've organized a few lightning talk
sessions, where people do quick 5-minute presentations of papers they've
read, and this is often enough for the key idea. Once you strip out the
problem definition, skip the careful qualification to prior work, and pass
over all the intervening details, the rest is quite short.

I still remember an interesting reviewer comment I got: "your 2 minute
video summarizing the paper was clearer than your actual paper." The
research paper format is meant to be complete, but not everybody needs
everything the paper is trying to explain.


