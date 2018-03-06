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
feeling, but in the interest of avoiding the [Tough Act To Follow](http://tvtropes.org/pmwiki/pmwiki.php/Main/ToughActToFollow)
problem, I'm planning to write shorter posts, and to release them more
frequently.

For the first of those posts, I'll be exploring this question: **What's the
difference between a blog post and a research paper, and why did I choose to
write a blog post instead of a paper?**

In some sense, the deep RL blog post could have been a paper. Topic-wise, it
lies somewhere between a survey paper and a policy paper, and in principle,
I could have tossed it on arXiv if I wanted to.

However, I do think it needed to be a blog post, for a few reasons.

One of the big ones was videos.
When planning the post, I knew that I wanted lots of videos.
It is so, so much easier to explain the behavior of these algorithms
if you can actually show videos of those behaviors. Writing it as a blog
post made this easier.

Another was that I deliberately wanted to strike a more colloquial tone. If
it wasn't clear from the Futurama meme, the post was never trying to be
scholarly or formal. It's not that formal writing is a bad writing style.
It's more that there's a time and place for it, and I found it easier to make
the points I wanted to make if I let the writing be looser.

Although both of these reasons were important, they're a bit trivial. The
two most important reasons were that **I wanted a narrow target audience**, and
**I wanted it to be an opinion piece**.

This is going to sound pretentious, but the medium of writing
affects expectations about that writing. Messaging apps encourage short
sentence, whereas email encourages longer paragraphs. In a similar vein, I feel
that blog posts encourage making opinions, whereas papers encourage stating
truths. This might not make sense, so let me explain.

Both blog posts
and papers try to argue something by presenting evidence that supports
that argument, and explaining away evidence that refutes it. However, I feel
that the standard expected out of a paper is a lot higher. People expect papers
to be careful about their conclusions. Whether the average paper does this is
up for debate, but it's certainly a desired end goal. If papers are supposed
to be kernels of truth about the world, then it's only natural to hold them
to a high standard.

In contrast, although a blog post can state truths, they are not expected
to *only* say true things. Most blog posts only list one author, and because of
this, there's always this implicit question that the entire post is just that
person's opinion. That makes blog posts well-suited for writing about topics
that are inherently up for debate. Topics like, say, the state of a field, and
where it is, and where it's going.

At the time of writing, I wasn't sure whether people would agree with me or not.
And I was fine with that. As long as the post made it clear why I arrived at
the conclusions I did, I'd be okay with it.

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
inefficient. The introduction covers a problem you've known about for months.
The related work section cites papers you've already read, or at least have
already heard about, and seems to exist just to convince other researchers you're
aware of their work. The methods section is filled with preamble and
boilerplate you've seen a billion times. I have lost track of how many times
I've read an introdouction of RL, Q-Learning, or policy gradient, but I think
it's at least a hundred.

Here is a reviewer comment from a paper I worked on: "the 2 minute video
accompanying your paper was better than the paper itself." Isn't that
interesting?

I was not in the mood to explain how DQN worked, or how policy gradient worked.
I wanted to cut past all that, and writing it as a blog post made that easier.

The research paper format encourages the author to be complete, but very few
people are going to need everything the paper has to offer. That's fine! Papers
aren't written for just one person, they're written for everyone. But once
you strip out the problem definition, skip the careful qualification to prior
work, and accept the intervening details on faith, the core idea is often quite
short. Sometimes that's all you're looking for.

I have a pet theory that the reason academics like Twitter is because it's short
enough that writing boilerplate is impossible. But it's just a theory.
