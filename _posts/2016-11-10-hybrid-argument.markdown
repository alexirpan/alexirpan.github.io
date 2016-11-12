---
layout: post
title:  "Quick Guide to The Hybrid Argument"
date:   2016-11-10 09:58:00 -0800
---

I was reading through a proof from a robotics paper for imitiation learning,
and realized the proof reminded me of hybrid arguments from cryptography.
It's always nice to realize connections between fields, so I figure it was
worth making a quick guide to how hybrid arguments work.

\*\*\*
{: .centered }

Hybrid arguments are a proof method, like proof by induction or proof by
contradiction. Like induction/contradiction, the details will differ between
problems, and solving those details is often the hardest part of the proof.

The hybrid argument may apply when we have the following.

* We have two objects $$A$$ and $$A^*$$.
* There is a sequence of objects $$A_1, A_2, \cdots, A_n$$ such that $$A_1 = A$$,
$$A_n = A^*$$, and each $$A_i$$ can be made by interpolating from $$A_1$$ to $$A_n$$
in some way. Intuitively, as $$i$$ increases, $$A_i$$ slowly shifts from
$$A_1$$ to $$A_n$$.
* We have a function $$f$$ that acts on these objects.
* We want to bound the difference between $$f(A)$$ and $$f(A^*)$$.

Difference does not necessarily mean subtraction, but for simplicity let's assume
it does mean subtraction and $$f$$ is a function that always returns real
numbers. To continue the proof, we use one of my favorite tricks - rewrite the
term as a telescoping series.

$$
    f(A^*) - f(A)
        = f(A_n) - f(A_1)
        = \left(f(A_n) - f(A_{n-1})\right) + \left(f(A_{n-1}) -
        f(A_{n-2})\right) + \cdots + \left(f(A_2) - f(A_1)\right)
$$

Man, I love telescoping series. There's a sense of elegance in how all the
terms cancel just right. Although in this case, instead of cancelling terms,
we're reintroducing them.

This reduces bounding the difference $$f(A^*) - f(A)$$ to bounding the sum
of differences $$f(A_{i+1}) - f(A_i)$$.

Why does this help? The intuition is that if you can construct a nice
enough sequences $$A_1,A_2,\cdots,A_n$$, reasoning about the difference
between two adjacent terms is much easier. In fact, a useful hybrid argument
basically requires that $$A_i$$ and $$A_{i+1}$$ differ in a nice, explainable
way. Otherwise, you aren't getting any power out of this rearrangement.


Once you bound the difference, that's it! Really, there are only two tricks
here.

* Creating a sequence $$\{A_i\}$$ that acts the way you want it to.
* Noticing the telescoping trick to expand out the difference.

Much like induction, this forms the shell of the proof, and it's up to the
prover to provide the details to carry the argument through.

Some examples. First, a simple crypto example. Suppose we have a collection
of pseudorandom number generators $$G_1, G_2, G_3,\cdots, G_n$$. Prove that if
each PRNG $$G_1$$ is seeded independently with seed $$s_i$$, then the concatenated
output

$$
    G_1(s_1)|G_2(s_2)|G_3(s_3)|\cdots|G_n(s_n)
$$

is itself pseudorandom.

Construct hybrids $$H_i$$, where $$H_i$$ uses the first $$i$$ PRNGs, and uses
true randomness for the rest. (By convention, we'll use $$\$$$ for truly random
data.

$$
    H_i = G_1(s_1)|\cdots|G_i(s_i)|\$|\$|\cdots|\$
$$



ThiThis is all very abstract, so let's get into examples. Here's the problem that
inspired this blog post.

> We have an environment in which agents can act for $$T$$ timesteps. This
> environment is an MDP, meaning the next state only depends on the current
> state and action. Let $$C(s,a)$$ be the cost of taking action $$a$$ in
> state $$s$$. Let $$\pi$$ be our current policy, and let $$\pi^*$$ be the
> expert policy we are trying to imitate. Bound the expected difference in cost
> between using $$\pi$$ and using $$\pi^*$$.

Let $$J(\pi)$$ be the expected cost of policy $$\pi$$. To bound $$J(\pi^*) -
J(\pi)$$, we first construct a sequence of policies $$\{\pi_i\}$$. Let
$$\pi_i$$ be the policy where we follow $$\pi$$ for $$T - i$$ timesteps, then
follow $$\pi^*$$ for the remaining timesteps. Note that $$\pi_0 = \pi$$
and $$\pi_T = \pi^*$$. We now have

$$
    J(\pi^*) - J(\pi) = \sum_{i=1}^T J(\pi_i) - J(\pi_{i-1})
$$
