---
layout: post
title:  "Introduction to the Hybrid Argument"
date:   2016-11-12 18:57:00 -0800
---

I was reading through some proofs from imitation learning,
and realized they were reminding me of hybrid arguments from cryptography.
It's always nice to realize connections between fields, so I figure it was
worth making a quick guide to how hybrid arguments work.

\*\*\*
{: .centered }

Hybrid arguments are a proof method, like proof by induction. Like induction,
they aren't always enough to
solve the problem. Also like induction, the details differ
on each problem, and filling in those details is the hardest part
of each method.

The hybrid argument requires the following.

* We want to compare two objects $$A$$ and $$A'$$.
* There is a sequence of objects $$A_0, A_1, \cdots, A_n$$ such that $$A_0 = A$$,
$$A_n = A'$$, and the $$A_i$$ can be seen as an interpolation from $$A_0$$ to $$A_n$$.
Intuitively, as $$i$$ increases, $$A_i$$ slowly drifts from $$A$$ to $$A'$$.
* The difference between two adjacent $$A_i$$ in the interpolation is small.

For concreteness, let's assume there's a function $$f$$ and we're trying to
bound $$f(A) - f(A')$$. Rewrite this difference as a telescoping series.

$$
    f(A) - f(A') = f(A_0) - f(A_n) = \sum_{i=0}^{n-1} \left(f(A_i) - f(A_{i+1})\right)
$$

Every term in the sum cancels, except for the starting $$f(A_0)$$ and
the ending $$-f(A_n)$$.

(Man, I love telescoping series. There's something
elegant about how it all cancels out. Although in this case, we're adding
more terms instead of removing them.)

This reduces bounding $$f(A) - f(A')$$ to bounding the sum of terms $$f(A_i) - f(A_{i+1})$$.
Since the difference between adjacent $$A_i$$ is small, $$f(A) - f(A')$$
is at most $$n$$ times that small value. And that's it!
Really, there are only two tricks to the argument.

* Creating a sequence $$\{A_i\}$$ with small enough differences.
* Applying the telescoping trick to use those differences.

**It's very important that there's both a reasonable interpolation and the
distance between interpolated objects is small. Without both these points, the
argument has no power.**

![You have no power here](/public/hybrid/nopower.jpg)
{: .centered }

This is all very fuzzy, so let's make things more concrete. This problem
comes from the [DAGGER](https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf) paper.
(Side note: if you're doing imitation learning, DAGGER is a bit old, and
[AGGREVATE](https://arxiv.org/abs/1406.5979) or [Generative Adversarial Imitation Learning](https://arxiv.org/abs/1606.03476) may be better.)

We have an environment in which agents can act for $$T$$ timesteps. Let $$\pi_E$$
be the expert policy, and $$\pi$$ be our current policy. Let $$J(\pi)$$ be
the expected cost of policy $$\pi$$. We want to prove that given the right
assumptions, $$J(\pi)$$ will be close to $$J(\pi_E)$$ by the end of training.

This is done with hybrids.
Define $$\pi_i$$ as the policy which follows $$\pi$$ for $$i$$
timesteps, then follows $$\pi_E$$ for the remaining $$T-i$$ timesteps. Note
$$\pi_0 = \pi_E$$ and $$\pi_T = \pi$$.
The telescoping trick gives

$$
    J(\pi_E) - J(\pi) = J(\pi_0) - J(\pi_T) = \sum_{i=0}^{T-1} J(\pi_i) - J(\pi_{i+1})
$$

The only difference between $$\pi_i$$ and $$\pi_{i+1}$$ is that in the first, the
expert takes over after $$i$$ steps, and in the second it takes over after
$$i+1$$ steps.
The paper then argues that as long as the environment has no key decision
where a single wrong move can lead to death, the ability of the
expert to correct after $$i+1$$ steps must be similar to its ability to
correct after $$i$$ steps.

This shows why hybrids are useful. They let us break down reasoning over
$$n$$ steps worth of differences to reasoning about $$n$$ differences of 1 step
each.

A similar flavor of argument shows up a ton in crypto.
Very often, we're trying to replace a true source of randomness with something that's
pseudorandom, and we need to argue that security is still preserved. For
example, we have $$n$$ PRNGs $$G_1,\cdots,G_n$$, and $$n$$ independently sampled
seeds $$s_i$$. Suppose we concatenated the $$n$$ inputs and $$n$$ outputs
together to get the function

$$
   G'(s_1s_2\cdots s_n) = G_1(s_1)G_2(s_2)G_3(s_3)\cdots G_n(s_n)
$$

We want to show $$G'$$ is still a PRNG.

Here, the hybrids are functions $$H_i$$, where $$H_i$$ uses
the first $$i$$ PRNGs and uses true randomness for the remaining $$n-i$$
blocks of bits. This makes $$H_0$$ truly random and $$H_n = G'$$.
If the difference between $$H_0$$ and $$H_n$$ is small, $$G'$$'s
output is close to truly random, which would show $$G'$$ is a PRNG. This
leaves arguing that switching from $$H_i$$ to $$H_{i+1}$$ (switching
the $$(i+1)$$th block of bits from true random to $$G_{i+1}$$) doesn't
change things enough to break security.

\*\*\*
{: .centered }

Like with many things, hybrid
arguments are something that you have to actually do to really understand. And
I don't have a library of hybrid problems off the top of my head. That being said,
I think it's useful to know what they are and roughly how they work.
Proof methods are only as useful as your ability to recognize when they might apply,
and it's hard to recognize something if you don't know it exists.

Whenever you have two objects and a reasonable interpolation between them,
it's worth thinking about whether you can bound the difference between adjacent
terms. And whenever you know how to bound the difference between two similar
objects, it's worth thinking about whether you can build an appropriate
sequence that lets you chain those differences into a conclusion about
objects further apart.

