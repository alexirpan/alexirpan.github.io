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
contradiction. Like induction/contradiction, they aren't always enough to
solve the problem. Also like induction and contradiction, filling in the
details of the argument is the hardest part of the proof.

The hybrid argument requires the following.

* We want to compare two objects $$A$$ and $$A'$$.
* There is a sequence of objects $$A_1, A_2, \cdots, A_n$$ such that $$A_1 = A$$,
$$A_n = A'$$, and each $$A_i$$ can be made by interpolating from $$A_1$$ to $$A_n$$
in some way. Intuitively, as $$i$$ increases, $$A_i$$ slowly shifts from
$$A_1$$ to $$A_n$$.
* The difference between two adjacent $$A_i$$ is small.

For concreteness, let's assume there's a function $$f$$ and we're trying to
bound $$f(A) - f(A')$$. Rewrite this difference as a telescoping series.

$$
    f(A) - f(A') = f(A_1) - f(A_n) = \sum_{i=1}^{n-1} \left(f(A_i) - f(A_{i+1})\right)
$$

Every term in the sum cancels, except for the starting $$f(A_1)$$ and
the ending $$-f(A_n)$$. (Man, I love telescoping series. There's something
elegant about how it all cancels out. Although in this case, we're adding
more terms instead of removing them.)

This reduces bounding $$f(A) - f(A')$$ to bounding the sum of $$f(A_i) - f(A_{i+1})$$.
Now recall the difference adjacent $$A_i$$ are small. And that's it!
Really, there are only two tricks to the argument.

* Creating a sequence $$\{A_i\}$$ with small enough differences.
* Applying the telescoping trick to use those differences.

**It's very important that there's both a reasonable interpolation and the
distance between interpolated objects is small. Without both these points, the
argument has no power.**

I know this is all very fuzzy, so let's make things more concrete. This problem
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


In this example, the function $$f$$ would be a measure of
how hard it is to distinguish 

To make this concrete, I'll give two examples, one from crypto and one from
statistical learning theory. First, the crypto example. A deterministic function $$G$$
is a pseudorandom number generator (PRNG) if it is hard to tell $$G(s)$$
apart from true random.

> We have $$n$$ pseudorandom number generators (PRNGs) $$G_1, G_2, G_3,\cdots, G_n$$.
> Let $$s = s_1s_2\cdots s_n$$ be the concatenation of $$n$$ independently sampled
> random seed. Prove
>
> $$
>    G'(s) = G_1(s_1)G_2(s_2)G_3(s_3)\cdots G_n(s_n)
> $$
>
> is also a PRNG.

We prove this with a hybrid argument. Let $$f(G)$$ be

$$
    f(G) = \text{the difference between}\, G(s) \,\text{and random, where}\,s\,\text{is random}
$$

Crypto convention is to use $ for randomness. By definition, $$f(\$) = 0$$, and
for any PRNG $$G$$, $$f(G)$$ is small. (I don't want to get into the details
of how you precisely define "difference" here, because the details aren't the
point of this blog post. If you're curious, there are a lot of crypto lecture
notes on the internet.)

We want to prove $$f(G')$$ is small. This is where the hybrid argument comes
in. Since $$f(\$) = 0$$, proving $$f(G')$$ is small is equivalent to proving $$f(G') - f(\$)$$ is
small. Define hybrids $$H_0, \cdots, H_n$$, where

$$
    H_i(s) = G_1(s_1)G_2(s_2)\cdots G_i(s_i)\$\$\cdots\$
$$

Or in words, $$H_i$$ uses the first $$i$$ PRNGs, then switches to pure random
for the rest. When defined this way, $$H_0$$ is true random, and $$H_n = G'$$.
Write the difference as

$$
    f(G') - f(\$) = \sum_{i=0}^n f(H_{i+1}) - f(H_i)
$$

Now, consider the difference between $$H_{i+1}$$ and $$H_i$$.

$$
    H_i(s) = G_1(s_1)\cdots G_i(s_i)\$\$\$\cdots
$$

$$
    H_{i+1}(s) = G_1(s_1)\cdots G_i(s_i)G_{i+1}(s_{i+1})\$\$\cdots
$$

The only difference is at the $$(i+1)$$th block of bits, where we replace
true random with $$G_{i+1}(s_{i+1})$$. Because $$G_{i+1}$$ is given to be a PRNG,
the difference
is a PRNG. Therefore, the difference $$f(H_{i+1}) - f(H_i)$$ is small. This
completes the (handwavey) proof. $$\blacksquare$$

Now, the lemma that inspired this blog post. This comes from the DAgger paper,
which proposes an algorithm for imitation learning. (It's since been replaced by
AGGREVATE, and more recently GAIL)


> We have an environment in which agents can act for $$T$$ timesteps. This
> environment is an MDP, meaning the next state only depends on the current
> state and action. Let $$C(s,a)$$ be the cost of taking action $$a$$ in
> state $$s$$. Let $$\pi$$ be our current policy and $$\pi^*$$ be the
> expert policy we are trying to imitate. Bound the expected difference in cost
> between using $$\pi$$ and using $$\pi^*$$.

Let $$J(\pi)$$ be the expected cost of policy $$\pi$$. To bound $$J(\pi^*) -
J(\pi)$$, we first construct a sequence of policies $$\{\pi_i\}$$. Let
$$\pi_i$$ be the policy where we follow $$\pi$$ for the first
$$T - i$$ timesteps, then follow $$\pi^*$$ for the remaining timesteps.
This gives $$\pi_0 = \pi$$ and $$\pi_T = \pi^*$$. The telescoping trick
gives

$$
    J(\pi^*) - J(\pi) = \sum_{i=1}^T J(\pi_i) - J(\pi_{i-1})
$$

Considering just one term, note that the first $$i-1$$ steps between
$$\pi_i$$ and $$\pi_{i-1}$$ are the same. Because the environment is
an MDP, $$J(\pi_i) - J(\pi_{i-1})$$ becomes the difference between
letting $$\pi^*$$ take over after $$i-1$$ steps, or letting $$\pi$$ make
one choice, then letting the expert take over. The rest of the argument
focuses on environments where the expert can correct from taking a single
unoptimal action.

$$

$$
