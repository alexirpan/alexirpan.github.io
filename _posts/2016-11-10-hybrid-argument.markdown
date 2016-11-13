---
layout: post
title:  "Introduction to the Hybrid Argument"
date:   2016-11-10 09:58:00 -0800
---

I was reading through a proof from a robotics paper for imitiation learning,
and realized the proof reminded me of hybrid arguments from cryptography.
It's always nice to realize connections between fields, so I figure it was
worth making a quick guide to how hybrid arguments work.

\*\*\*
{: .centered }

Hybrid arguments are a proof method, like proof by induction or proof by
contradiction. Like induction/contradiction, they aren't always enough to
solve the problem. Also like induction and contradiction, the details differ
on each problem, and filling in those details is the hardest part
of using the method.

The hybrid argument requires the following.

* We want to compare two objects $$A$$ and $$A'$$.
* There is a sequence of objects $$A_0, A_2, \cdots, A_n$$ such that $$A_1 = A$$,
$$A_n = A'$$, and the $$A_i$$ can be seen as an interpolation from $$A_1$$ to $$A_n$$.
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
comes from the DAgger paper,
which proposes an algorithm for imitation learning. (It's since been replaced by
AGGREVATE, and more recently GAIL.)
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

The only difference between $$\pi_i$$ and $$\pi_{i+1}$$ is the action taken at
timestep $$i+1$$, and how that carries through the rest of the episode.
The paper then goes on to argue that as long as the environment has no key decision
where a single wrong move at timestep $$i+1$$ can lead to death, the ability of the
expert to correct from timestep $$i+1$$ must be similar to its ability to
correct from timestep $$i$$. Hybrids let us break down reasoning over
$$n$$ steps worth of differences to reasoning about $$n$$ differences of 1 step
each.

A similar flavor of argument shows up a ton in crypto.
Very often, we're trying to replace a true source of randomness with something that's
pseudorandom, and we need to argue that security is still preserved. For
example, we have $$n$$ PRNGs $$G_1,\cdots,G_n$$, and want to prove that if
we sample $$n$$ seeds $$s_i$$ independetly, the function

$$
   G'(s_1s_2\cdots s_n) = G_1(s_1)G_2(s_2)G_3(s_3)\cdots G_n(s_n)
$$

is itself a PRNG. The hybrids $$H_i$$ would be functions that use only the first
$$i$$ PRNGs, with true randomness for the rest. Note that $$H_0$$ is a truly
random function, and $$H_n = G'$$. Arguing that the difference between each $$H_i$$
is small enough suffices to show $$G'$$ is a PRNG, because we only need $$n$$
small steps to go from the fully random $$H_0$$ to the desired function $$G'$$.

\*\*\*
{: .centered }

These aren't the greatest examples. Like with many things, hybrid
arguments are something that you have to actually do to really understand. And
I don't have a library of problems off the top of my head.

However, I think it's useful to keep in mind. Whenever you have two objects
and a reasonable interpolation, it's worth thinking about bounds on adjacent
terms in the interpolation. And whenever you only know how to bound the
difference between two similar objects, it's worth thinking about whether you
can chain that difference together by building an appropriate sequence.

