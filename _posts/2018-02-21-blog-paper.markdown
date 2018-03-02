---
layout: post
title:  "Blog Posts and Research Papers"
date:   2018-02-21 01:01:00 -0800
---

I've been blown away by the reception to my most recent "Deep RL Doesn't
Work Yet" blog post. In retrospect, it was a perfect storm of several factors.

* Reinforcement learning is a popular subject.
* I had experience with RL, which helped a lot for finding papers to
cite.
* I cared enough about the post to get the writing as good as possible.
* Most researchers agreed with the overarching message, even if they didn't
agree with all the details. I have a theory that the easiest way to sound
smart is to write things the reader implicitly agrees with. By that, I mean
things the reader agrees with in retrospect, but which they may not have
*realized* they agreed with until they read your writing.
* Despite this general agreement, very few people had written
something similar. That left the door open for my post.


Outline notes:
explain post, mention it could have been a survey or policy paper, then mention
why it wasn't.

There is a good chance I'll never write anything as good or as popular again.

It's a weird thing to realize
realizing that yes, people actually read this blog, and that adds a lot of
pressure. The best way to relieve that pressure is to just write more posts,
and try not to get hung up if people don't read them (since that was never
why I started writing in the first place.)

However, there's one question left about the blog post: did it have to be
a blog post? Why couldn't it have been a paper?

In some ways, it already is a paper. It is long enough to be a paper.
It cites plenty of prior work. It even went through peer review - at
least 20 people gave comments on early drafts, in some shape or form.

And yet, I do think that post had to be a blog post. This is going to sound
pretentious, but the medium of exchange affects expectations about the text,
and I specifically wanted the expectations that come from the blog posts.

If I want to elaborate on this, I first need to explain what "paper" means
to me. In machine learning, there are three broad categories of papers:
research papers, survey papers, and policy papers.

Research papers are for explaining new research. They do so according to
fairly strict constraints. There must be an introduction, explaining the
problem. There must be a related work section, citing every recent paper
that tried the same problem. There must be a methods section, there have
to be experiments, and there has to be a conclusion. In deep learning, it
also all has to fit in 8 pages, since that's a common page limit for
several conferences.

Once you have experience in a field, research papers are a shockingly
inefficient way of explaining knowledge. The introduction and related
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

The "Deep RL Doesn't Work Yet" blog post is immediately disqualified,
because it does no original research. It only cites existing work.


Survey papers try to summarize an entire field. Usually, these surveys are
pretty long.

This is a massive endeavor,
and usually survey papers are pretty long. The goal of these papers is to
be complete.
