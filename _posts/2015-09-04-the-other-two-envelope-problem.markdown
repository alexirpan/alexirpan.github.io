---
layout: post
title:  "The Other Two Envelope Problem"
date:   2015-09-04  18:00:00
---

There are at least 2 two envelope problems. The first I know of is considerably
more famous; it has
[its own Wikipedia page](https://en.wikipedia.org/wiki/Two_envelopes_problem).
It's an interesting problem and worth reading, but this is about that problem's
litte brother, who deserves his own time to shine.

Here is the formulation.

> There are two envelopes, one with $$A$$ and one with $$B$$ dollars, $$A \neq B$$.
> $$A$$ and $$B$$ are
> unknown distinct positive integers. You are randomly given an envelope,
> can look inside, then must choose whether to switch envelopes or not.
>
> Does there exists a switching strategy which ends with the larger envelope more than
> half the time?

At first glance, the answer should be no.
Although we know the contents
of one envelope, we have no information on how much the other envelope might have.
When the other envelope is a black box, how can we make a meaningful decision?

As it turns out, such a strategy does exist, and
the small amount of information we have (the amount in the current
envelope) is enough to improve our standing, even when the alternative has unknown value.

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
$$A,B$$ are arbitrary reals. The problem is that the number of flips comes
from a discrete distribution, so it does not have the granularity to distinguish
between values like $$A = 2.3, B = 2.4$$.

So, how is this strategy extendable? The way the current strategy works is by creating
a decision boundary based on the amount in the seen envelope.
The boundary is then applied to the geometric distribution
with parameter $$p=1/2$$.

IMAGINE A BEAUTIFUL PICTURE

To handle arbitrary reals, we should use a continious probability distribution
instead. Nothing in the previous logic relies on the distribution being discrete,
so we can simply drop in a distribution of our choice. The only requirement we
need is a strictly positive probability density function over $$(-\infty, \infty)$$
(we'll explain why we need this later.)
The standard normal distribution $$N(0, 1)$$ will do fine.

The modified strategy is

- Inspect amount $$X$$ inside the envelope.
- Sample $$Y$$ from $$N(0,1)$$.
- If $$Y \ge X$$. switch. Otherwise, do not switch.

The proof is also similar.
For $$A < B$$, $$P(Y \ge A) > P(Y \ge B)$$. This is why the p.d.f. needs to be
positive everywhere. If the p.d.f. is zero over some interval $$[a,b]$$, it is
possible that both $$A, B \in [a,b]$$, which gives $$P(Y \ge A) = P(Y \ge B)$$.
The chance of ending with the larger envelope is

$$
    \frac{1}{2}P(Y \ge A) + \frac{1}{2}\left(1 - P(Y \ge B)\right) = \frac{1}{2} + \frac{1}{2}\left(P(Y \ge A) - P(Y \ge B)\right) > \frac{1}{2}
$$

and this strategy generalizes to real valued envelopes. $$\blacksquare$$

Extending to Multiple Envelopes
---------------------------------

At this point, it's worth considering whether we can take any lessons from this problem.
The result suggests that even with no information on alternative choices, we could
use a random action to improve our current standing. It would be really, really nice
if this was applicable to real life decisions, since we often have very little
information on the outcomes of different choices.
However, in real life there are usually much more than two possible actions, so
we should first consider whether this two envelope framework is even valid.

When there are $$n$$ envelopes instead of $$2$$ envelopes, we can no longer
aim for only the best envelope. The switch could slightly help us, slightly hurt us,
especially help us, or especially hurt us. Because of this, we need to modify the
criteria of a good strategy.

> There are $$n$$ envelopes, which give utilities $$A_1 < A_2 < A_3 < \cdots < A_n$$.
> The $$A_i$$ are unknown real numbers.
> You are randomly given an envelope, can look inside, then must choose whether to switch
> with another envelope.
>
> Does there exist a switching strategy that improves your utility more often
> than it worsens your utility?

Once again, it turns out the real valued two envelope strategy still works with appropriate
modifications.
We still choose whether to swap by seeing if sample $$Y$$ is greater than
seen utility $$X$$.
The only difference is choosing which envelope to switch to. From the opener's
perspective, every other envelope appears identical. Thus, if the strategy says to
swap, we should pick an alternative envelope at random.

This leaves showing the improvement chance is higher than the worsening chance.
If the algorithm does not swap, the utility is unchanged, so it suffices to analyze
only situations where we switch envelopes.

For envelope $$i$$, the chance of switching is $$P[Y \ge A_i]$$.
The reward rises for $$n-i$$ envelopes and drops for $$i-1$$
envelopes. Thus, the chance of improving utility is

$$
    P[\text{utility rises}] = \sum_{i=1}^n \frac{1}{n} P[Y \ge A_i]\cdot \frac{n-i}{n-1}
$$

and the chance of worsening utility is

$$
    P[\text{utility drops}] = \sum_{i=1}^n \frac{1}{n} P[Y \ge A_i]\cdot \frac{i-1}{n-1}
$$

Now, take the difference and pair up terms with matching $$P[Y \ge A_i]$$ to get

$$
    P[\text{improves}] - P[\text{worsens}] = \frac{1}{n}\sum_{i=1}^n \frac{n-2i+1}{n-1} P[Y \ge A_i]
$$

The coefficients of the terms are $$\frac{n-1}{n-1}, \frac{n-3}{n-1}, \ldots, \frac{-(n-3)}{n-1}, \frac{-(n-1)}{n-1}$$.
Since we only care about whether the difference is positive, multiply by $$2$$ to get
two copies of the terms, then pair terms by coefficient, matching each coefficient with its negative.

$$
    2(P[\text{improves}] - P[\text{worsens}]) = \frac{1}{n}\sum_{i=1}^n \frac{n-2i+1}{n-1} (P[Y \ge A_i] - P[Y \ge A_{n+1-i}])
$$

Consider each term of this summation.

- For $$i < \frac{n+1}{2}$$, the coefficient
is positive and $$A_i < A_{n+1-i}$$. Thus,
$$P[Y \ge A_i] - P[Y \ge A_{n+1-i}]$$ is also positive.
- For $$i = \frac{n+1}{2}$$, the coefficent is $$0$$.
- For $$i > \frac{n+1}{2}$$, the
coefficient is negative, and $$A_i > A_{n+1-i}$$, so $$P[Y \ge A_i] - P[Y \ge A_{n+1-i}]$$
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
