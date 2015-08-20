---
layout: post
title:  "Simulating a Biased Coin With a Fair One"
date:   2015-08-20  01:10:00
---

Suppose you needed to simulate a coin with $$p = 1/4$$, and all you had was a
fair coin. Well, that's easy enough. Flip the coin twice. Report a success if
you get 2 heads, and report failure otherwise. Two coin flips, not so bad.

Now, suppose you needed to simulate $$p = 1/3$$. Well, that may not
be a power of 2, but the solution is still simple. Flip the fair coin twice.
Report a success on HH, report a failure on HT or TH, and try again on TT.
That way, conditioned on the process halting this iteration, we report success in
1 out of 3 events, all equally likely.
Each iteration takes $$2$$ coin flips, and there is a $$3/4$$ probability
of halting, giving $$8/3$$ expected coin flips. (Add proof of this?)

Now, suppose you needed to simulate the probability $$1/10^{100}$$.

Well, if we followed the same scheme, we would need $$\lceil\log_2(10^{100})\rceil = 333$$
coin flips. That's before considering the process retries in
$$2^{333} - 10^{100}$$ of the $$2^{333}$$ cases. The probability of halting
is $$> 1/2$$ since the scheme chooses the smallest power of $$2$$ such that
it is bigger than $$10^{100}$$, so the expected number of flips is at least less than $$666$$.
Yes, that is a lot of flips, but things could be worse.

Now, suppose you needed to simulate $$p = 1 / \pi$$.

Uhhhh....

HORIZONTAL LINE HERE
--------------------

We'll get back to the irrational case later. First, we can try to optimize our
current scheme.

The current scheme simulates $$p=1/4$$ by flipping two coins all the time.
Recall that the scheme reports success only on HH, So, if the first flip lands
tails, we can halt immediately, since TH and TT both fail. The revised scheme
becomes
1. Flip a coin. If tails, report failure.
2. Flip a coin. Report success on heads and failure on tails.

This gives $$3/2$$ expected flips instead of $$2$$ flips. Now, unfortunately
this does not let us improve the $$p = 1/3$$ problem. H is a prefix for both
success (HH) and failure (HT). T is a prefix for both failure (TH) andd
retry (TT). However, this can help for other values of $$p$$.
If we were solving $$p = 1/5$$ instead, there would be
1 accept case, 4 failing cases, and 3 retry cases. These can be distributed as

- accept: HHH
- failing: THH, THT, TTH, TTT
- retry: HHT, HTH, HTT

which would let us report failure immediately if the first coin is tails.

This gives some improvment for the $$p = 1/10^{100}$$ case, but it does not
solve the $$p = 1/\pi$$ case. It turns out this is solvable, once you find
the right coin flipping paradigm.

HORIZONTAL LINE HERE
--------------------

I did not come up with this method - I discovered it from (LINK). I wish I
had come up with it, because the math works out so elegantly.

Suppose we need to simulate a biased coin that lands on heads with probabiilty $$p$$.
Let $$p = 0.b_1b_2b_3b_4b_5\ldots$$ be the binary expansion of $$p$$. Use the following
algorithm

- Flip a coin until it lands on heads
- Let $$n$$ be the number of coins flipped. Report success if $$b_n = 1$$ and report failure
otherwise

First, verify this works. The probability the process stops after $$n$$ flips
is $$1/2^n$$. The probability of success is
$$
    \sum_{n: b_n = 1}^\infty \frac{1}{2^n}
$$
which works out to $$p$$ by definition.

Next, find the expected number of flips. It takes $$2$$ expected flips for the
coin to land heads. Thus, any biased coin can be simulated in $$2$$ expected flips
of a fair coin. Moreover, you can compute the bits $$b_i$$ lazily, so you can
implement this in actual code to simulate irrational probabilities.


