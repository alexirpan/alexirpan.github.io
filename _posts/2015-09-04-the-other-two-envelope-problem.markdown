---
layout: post
title:  "The Other Two Envelope Problem"
date:   2015-09-04  18:00:00
---

There are at least 2 two envelope problems. The first I know of is considerably
more famous; it has
[its own Wikipedia page](https://en.wikipedia.org/wiki/Two_envelopes_problem).
If you haven't seen it before, it's worth reading, but this is about the other
two envelope problem.

Here is the formulation.

> There are two envelopes, one with $$A$$ and one with $$B$$ dollars, $$A \neq B$$.
> $$A$$ and $$B$$ are
> unknown distinct positive integers. You are randomly given an envelope.
> You are allowed to look inside, then must choose whether to switch envelopes
> or not.
>
> Does there exists a switching strategy that ends with the larger envelope more than
> half the time?

At first glance, the answer should be no.
Although we know the contents
of one envelope, we have no information on how much the other envelope might have,
so how can any decision we make be meaningful?
As it turns out, the small amount of information we have (the amount in the current
envelope) is enough to make a better
decision, even when the alternative is unkown.

The Power of Randomness
--------------------------

The trick is to make the switching decision randomly, in a way that biases outcomes
to end with the larger envelope. The strategy is as follows:

- Inspect amount $$X$$ inside the envelope.
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
    \frac{1}{2} + \frac{1}{2^{A+1}} - \frac{1}{2^{B+1}}
$$

which is indeed larger than $$1/2$$ for $$A < B$$. $$\blacksquare$$

Extending to the Reals
--------------------------

This coin flip strategy works when $$A$$ and $$B$$ are integers, but fails when
they are arbitrary reals.

So, how is this strategy extendable? The intuition behind why the coin flipping
strategy worked is that the amount in the current envelope gives a decision boundary
for our random process. In the coin flip strategy (REPHARSE to avoid using coin
flip twice), the random process is a sample from the geometric distribution
with parameter $$p=1/2$$. This distribution is discrete, but nothing stops us
from using a continuous probability distribution instead.
(Technically, we need to sample
a distribution with a probability density function that is positive over $$(-\infty, \infty)$$,
but most common distributions satisfy this.)

For simplicity, sample from the normal distribution $$N(0,1)$$. The final scheme is

- Inspect amount $$X$$ inside the envelope.
- Sample $$Y$$ from $$N(0,1)$$.
- Switch if $$Y \ge X$$. Otherwise, do not switch.

Again, to argue it works, for $$A < B$$, $$P(N(0,1) \ge A) \ge P(N(0,1) \ge B)$$,
so this switches envelopes more often when the first envelope is $$A$$, giving a
better than half chance of ending with the larger envelope.

Extending to Multiple Envelopes
---------------------------------

At this point, it's worth considering whether we can take any lessons from this problem.
The result suggests that even with no information on alternative choices, we can
potentially use a random action to improve our current standing. However, in real
life there are usually much more than two possible actions, so this strategy does
not apply.

This raises an interesting question: what if there are more than $$2$$ envelopes?
Consider the following formulation.

> There are $$n$$ envelopes, which give utilities $$A_1 < A_2 < A_3 < \cdots < A_n$$.
> The $$A_i$$ are unknown real numbers.
> You are randomly given an envelope, can look inside, then choose to switch
> with any other envelope.
>
> Does there exist a switching strategy that improves your utility more often
> than it worsens your utility?

Given how similar this problem is to the two envelope problem, we should first
try adapting the current strategy.
It turns out this strategy still works once modified.
We still choose whether to swap by sampling from $$N(0,1)$$.
The only difference is choosing which envelope to switch to. From the opener's
perspective, every other envelope appears identical. So, if the opener decides to
swap, he or she should do so at random.

This leaves showing the improvement chance is higher than the worsening chance.
If the algorithm does not swap, the utility is unchanged, so it suffices to analyze
only situations where we switch envelopes.
For envelope $$i$$, the chance of switching is $$P[Y \ge A_i]$$.
The reward drops for $$i-1$$ envelopes, and increases for $$n - i$$
envelopes. Thus, the chance of improving utility

$$
    P[\text{utility rises}] = \sum_{i=1}^n \frac{1}{n} P[Y \ge A_i]\cdot \frac{n-i}{n-1}
$$

and the chance of decreasing utility is

$$
    P[\text{utility decreases}] = \sum_{i=1}^n \frac{1}{n} P[Y \ge A_i]\cdot \frac{i-1}{n-1}
$$

Now, take the difference and pair up terms with matching $$P[Y \ge A_i]$$ to get

$$
    P[improves] - P[worsens] = \frac{1}{n}\sum_{i=1}^n \frac{n-2i+1}{n-1} P[Y \ge A_i]
$$

The coefficients go from $$\frac{n-1}{n-1}, \frac{n-3}{n-1}, \ldots, \frac{-(n-3)}{n-1}, \frac{-(n-1)}{n-1}$$.
Since we only care about whether the difference is positive, multiply by $$2$$ to get
two of each term, then pair terms by matching each coefficient with its negative.

$$
    2(P[improves] - P[worsens]) = \frac{1}{n}\sum_{i=1}^n \frac{n-2i+1}{n-1} (P[Y \ge A_i] - P[Y \ge A_{n-i+1}])
$$

Consider each term of this summation. For $$i < \frac{n+1}{2}$$, the coefficient
is positivem and $$A_i < A_{n-i+1}$$. Thus,
$$P[Y \ge A_i] - P[Y \ge A_{n-i+1}]$$ is also positive.
For $$i = \frac{n+1}{2}$$, the coefficent is $$0$$. For $$i > \frac{n+1}{2}$$, the
coefficient is negative, and $$A_i > A_{n-i_1}$$, so $$P[Y \ge A_i] - P[Y \ge A_{n-i+1}]$$
is also negative.

Every term in the summation is positive or zero, so the entire sum is positive, and
the probability of increasing utility is higher than the probability of decreasing
it. $$\blacksquare$$


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
