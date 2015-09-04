---
layout: post
title:  "The Other Two Envelope Problem"
date:   2015-09-04  18:00:00
---

There are two two envelope problems.

The first is well known, and has
[its own Wikipedia page](https://en.wikipedia.org/wiki/Two_envelopes_problem).
That problem is interesting, but this is about the other two envelope problem.
(BAD WORDING, FIX). Here is the setup:

> There are two envelopes, one with A and one with B dollars, $$A \neq B$$.
> A and B are
> unknown distinct positive integers. You are randomly given an envelope.
> You are allowed to look inside, then must choose whether to switch envelopes
> or not.
>
> Give a strategy where you walk away with the larger envelope more than
> half the time.
>
> Harder variation: do the same, except A and B are arbitrary positive real numbers.

At first glance, it should be very strange to see how you can guarantee getting
the larger envelope more than half the time.
Although we know the contents
of one envelope, we have no information on how much the other envelope might have.
So, it is not clear how we can make a meaningful decision at all. The only
information we have to inform our decision is the money in the current envelope.
As it turns out, that small amount of information is enough to make a better
decision, even when the other envelope's contents are a complete mystery.

The Power of Randomness
--------------------------

The trick is to make the switching decision randomly, in a way that biases outcomes
to end with the larger envelope. The strategy is as follows:

- See amount $$X$$ inside the envelope.
- Flip a fair coin until it lands tails.
- If there were at least $$X$$ flips, switch envelopes. Otherwise, do not switch.

For analysis, assume without loss of generality that $$A < B$$. There are two ways
to end with envelope $$B$$. Either start with $$A$$ and switch, or start with $$B$$
and do not switch. The first case happens with probability

$$
    P[\text{started A, switched}] = \frac{1}{2}\left(\frac{1}{2^{A}}\right)
$$

The second happens with probability

$$
    P[\text{started B, did not switch}] = \frac{1}{2}\left(1 - \frac{1}{2^{B}}\right)
$$

So, the chance to end with $$B$$ is

$$
\frac{1}{2^{A+1}} + \frac{1}{2} - \frac{1}{2^{B+1}} = \frac{1}{2} + \frac{2^{B-A} - 1}{2^{B+1}} > \frac{1}{2}
$$

Extending to the Reals
--------------------------

This coin flip strategy works when $$A$$ and $$B$$ are integers, but fails when
they are arbitrary reals. For instance, when $$A = 1.3, B = 1.4$$, the coin flip
strategy would switch on $$\ge 2$$ flips for both envelopes $$A$$ and $$B$$.

So, how is this strategy extendable? The intuition behind why the coin flipping
strategy worked is that even though we assume nothing about the other envelope,
we can act in a way that is less likely to switch while on the greater envelope.
(AGAIN BAD WORDING)

Formalizing the switching strategy gives

- Inspect amount $$X$$ inside the envelope.
- Sample a $$Y$$ from the geometric distribution with $$p = 1/2$$.
- Switch if $$Y \ge X$$. Otherwise, do not switch.

The only reason this fails for some envelope values $$A, B$$ is because the
geometric distribution is discrete. If we sampled from a continous distribution
instead, the scheme should extend to all reals. (Technically, we need to sample
a distribution with a probability density function that is positive over $$[0, \infty)$$,
but most common distributions satisfy this.)

For simplicity, sample from the normal distribution $$N(0,1)$$. The final scheme is

- Inspect amount $$X$$ inside the envelope.
- Sample $$Y$$ from $$N(0,1)$$.
- Switch if $$Y \ge X$$. Otherwise, do not switch.

Again, to argue it works, for $$A < B$$, $$P(N(0,1) \ge A) \ge P(N(0,1) \ge B)$$,
so this switches envelopes more often when the first envelope is $$A$$.

Implications
---------------------------

One of the incredibly neat consequences of this puzzle is to show how insiduous
information leakage can be. Knowing only the value of keeping the current envelope,
we can still have better than even chances of getting the larger envelope.

Unforunately, we cannot argue how much better this performs than random chance
because $$A$$ and $$B$$ are still chosen through some unknown process. Without
knownig how $$A$$ and $$B$$ are generated, it is impossible to quantify how well
this strategy does. (If we knew the distributions $$A$$ and $$B$$ came from, we
could design our switching scheme to use that information, but that turns the puzzle
into a plain expected value question.)

As for real life implications, I unfotunately don't see ways this can help you
make decisions in real life. It's very tempting to try to fit this into a
decision theory framework, because the ability to slightly improve
outcomes given a total information blackout is very appealing. The problem is that
such a scheme assumes you can quantify your current utility. The more structural
problem is that the envelope problem relies on having a $$1/2$$ chance of starting
in a given decision $$A$$. Consider what happens to the analysis when the default decision
is $$A$$ with probability $$p$$.

$$
Pr(improve) = somethign
$$
