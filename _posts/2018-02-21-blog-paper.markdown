---
layout: post
title:  "Blog Posts and Research Papers"
date:   2018-02-21 01:01:00 -0800
---

I've been blown away by the reception to my most recent "Deep RL Doesn't
Work Yet" blog post. In retrospect, it was a perfect storm - I spent a lot of
time on the post, it was about a popular subject, most people agreed with
the post's overarching message, and yet very few people had written about it.
That left room for me.

To any new readers I might have: prepare to be disappointed. There is a good
chance I'll never write anything as good or as popular again. It's a weird
feeling, but in the interest of avoiding the [Tough Act To Follow](http://tvtropes.org/pmwiki/pmwiki.php/Main/ToughActToFollow)
problem, I'm planning to write shorter posts, and to release them more
frequently.

For the first of those posts, I'll be exploring this question: **What's the
difference between a blog post and a research paper, and why did I choose to
write a blog post instead of a paper?**

In some sense, the deep RL blog post could have been a paper. Topic-wise, it
lies somewhere between a survey paper and a policy paper, and in principle,
I could have tossed it on arXiv if I wanted to.

However, I do think it needed to be a blog post.

One of the big reasons was videos.
When planning the post, I knew that I wanted lots of videos.
It is so, so much easier to explain the behavior of these algorithms
if you can actually show videos of those behaviors. Writing it as a blog
post made this easier.

Another was that I deliberately wanted to strike a more colloquial tone. If
it wasn't clear from the Futurama meme, the post was never trying to be
scholarly or formal. It's not that formal writing is a bad writing style.
It's more that there's a time and place for it, and I found it easier to make
the points I wanted to make if I let the writing be looser.

Although both of these reasons matter, the more important reasons were that
I wanted to be more opinionated, and I was aiming for a narrower target
audience.

This is going to sound pretentious, but the medium of writing
affects expectations about that writing. Messaging apps encourage short
sentence, whereas email encourages longer paragraphs. In a similar vein, I feel
that blog posts encourage stating opinions, whereas papers encourage stating
truths. This might not make sense, so let me explain.

Both blog posts
and papers try to argue something by presenting evidence that supports something
and explaining away evidence that refutes it. That's practically the definition
of writing. However, I feel that papers in particular are held to a high
standard. People expect papers to be both comprehensive and careful about their
conclusions. Whether the average paper does this is
up for debate, but it's certainly what people aim for.

If papers are supposed to be kernels of truth about the world, then it's only
natural that they be careful in their analysis. But the flip side of this is that
it's harder for papers to speculate. Increasing the burden of proof
places restrictions on what you can say.

In contrast, blog posts, keynote talks, and so on are often much more free to
state opinions, rather than facts. Of course, people still *expect* your argument
to be solid, but it's not required.
That makes blog posts well-suited for writing about topics
that are inherently up for debate. Topics like, say, the state of a field, and
where it is, and where it's going.

At the time of writing the deep RL post, I knew there was a chance it would be
controversial. And I was fine with that, as long as the post made it clear why
I arrived at the conclusions I did. (It also helped that I was the only author
on the post. That way, if people hated the post, at least they'd only hate me.)

As for the target audience: I specifically wrote the post towards people who
either worked on deep RL, or had a lot of interest in deep RL. If you were in
neither category and liked the post anyways, consider yourself lucky.
The advantage of narrow targeting is that I was free to jump directly to the
points I wanted to make.

I'm starting to believe that research papers are a shockingly inefficient
way to communicate.
When you're new to a field, research papers are a dense yet rewarding gold mine.
The introduction talks about a problem you didn't even know existed. The
related work is a treasure trove of papers to read next. The methods
and experiment sections take time to work through, but if you read them closely
enough, you'll understand not just the idea of the paper, but also all the ideas
the paper builds upon.

And that's how it starts. Then you read another paper, and another one, and soon
a pattern emerges.
The introduction covers a problem you've known about for months.
The related work section cites papers you've already heard about,
and seems to exist just to convince other researchers the authors have seen
their work. The methods section is filled with preamble and
boilerplate you've seen a billion times. I swear, every RL paper has a paragraph
like this:

> Let $$S$$ and $$A$$ be the states and actions of a Markov decision
process (MDP). Policy $$\pi$$ gives a distribution over actions, given state
$$s$$. Our objective is to maximize reward."

And then depending on the paper,
it'll either explain what Q-Learning is, or explain what policy gradient is.
I was not in the mood to explain any of that.

Did you know [there's a paper for MDP notation](https://arxiv.org/abs/1512.09075)?
It exists just so that authors can use a single sentence for their notation,
instead of writing paragraphs of it. I half-suspect this was created when the
author was trying to figure out how to get their paper to fit within the page
limit for one of the ML conferences.

The research paper format encourages the author to be complete. That's fine! I
don't think papers should be written any differently. Papers are written
for everyone, from the enthusiast to the new undergrad and the tenured
professor. It's just that very few people need everything that's in the paper.
These days, I usually read papers for their key ideas, and only read more
closely if I'm trying to reproduce or extend their results.
Once you strip out the problem definition, skip the careful qualification to prior
work, and accept the intervening details on faith, the core idea is often just
a few paragraphs.

Here is a paraphrased reviewer comment from a paper I worked on: "your 2 minute
video was better at explaining your work than the paper itself."
Isn't that interesting? It's technically wrong, since the video didn't mention
any of the implementation details. And at the same time, I found myself
agreeing with that revieiwer.

Everyone says that conferences are less about the papers, and more about networking
and talking shop with other people in the field. Papers are important, but they
aren't the only way to contribute something.

I went to NIPS last year. Over the course of a week, [679 papers](https://unsupervisedmethods.com/nips-accepted-papers-stats-26f124843aa0)
were presented. At the end of NIPS, what was everyone talking about?

[Ali Rahimi's Test of Time talk](http://www.argmin.net/2017/12/05/kitchen-sinks/).

Food for thought.
