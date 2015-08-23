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

For now, suppose we use the same scheme. We need $$\lceil\log_2(10^{100})\rceil = 333$$
coin flips to get enouch outcomes. Then, succeed in 1 case, fail in $$10^{100} - 1$$ cases,
and retry in
$$2^{333} - 10^{100}$$ cases. By construction, the probability of halting
is $$> 1/2$$ since the scheme chooses the smallest power of $$2$$ that gives enough outcomes.
So, the expected number of flips is at least less than $$666$$.
Yes, that is... (•\_•) ( •\_•)>⌐■-■ (⌐■\_■) devilishly many flips, but things could be worse.

Now, suppose you needed to simulate $$p = 1 / \pi$$.

Uhhhh....

HORIZONTAL LINE HERE
--------------------

We'll get back to the irrational case later. First, we can try to optimize our
current scheme.

The current scheme simulates $$p=1/4$$ by flipping two coins all the time.
Recall that the scheme reports success only on HH. So, if the first flip lands
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

Making the outcomes arranged as prefix-free as possible gives some improvement,
but it does not
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
    P[success] = \sum_{n: b_n = 1}^\infty \frac{1}{2^n} = p
$$

Next, find the expected number of flips. It takes $$2$$ expected flips for the
coin to land heads. Thus, any biased coin can be simulated in $$2$$ expected flips
of a fair coin. Moreover, you can compute the bits $$b_i$$ lazily, so this is
implementable in code if you have a bit stream representing $$p$$.

This idea may have been obvious to you, but it certainly wasn't to me. However,
getting to $$2$$ expected flips is entirely reasonable to get to on your own,
and the way to get there is related to one of the most important algorithms in computer
science.

The CS Perspective
--------------------
Consider the following algorithm for solving the problem.

1. Construct a real number in $$[0,1]$$ by flipping an infinite number of coins,
generating a random decimal $$0.b_1b_2b_3\ldots$$, where $$b_i$$ is the outcome
of coin flip $$i$$. Let this number be $$x$$.
2. Report success if $$x \le p$$ and failure otherwise.

This algorithm is correct as long as the decimals generated follow a
uniform distribution over $$[0, 1]$$. I won't prove this because I do not
trust my formal understanding of continuous probability distributions. As an
appeal to intuition: any two finite bit strings of the same length $$k$$ are
generated with the same probabiilty ($$1/2^k$$), and the numbers these
represent are evenly distributed over the interval $$[0, 1]$$. As $$k \to\infty$$
this approaches a uniform distribution.)

Assuming this all sounds reasonable, this algorithm works! Only, there is the
small problem of flipping $$\infty$$ coins. However, similarly to the $$p = 1/4$$
case, we do not actually need to flip infinitely many coins. We can stop as soon
as it is impossible for the generated decimal to fall in $$[0, p]$$.

For now, limit to the case where $$p$$ has an infinite binary expansion.
For the sake of an example, suppose $$p = 0.1010010001\ldots$$, and suppose
we have generated $$0.10$$ so far. There are 2 cases.

1. The next coin lands $$1$$. It is still possible to fall under $$p$$ if a very
large number of subsequent bits land $$0$$, so the algorithm must keep going.
2. The next coin lands $$0$$. It is now impossible to exceed $$p$$. Even if
every subsequent bit turns up $$1$$, $$0.100111\ldots = 0.101 < p$$.
(This is why $$p$$ having infinitely many decimal places is important - it ensures there
will be another $$1$$ at some point in the sequence.)

So, the algorithm halts unless the coin flip matches the $$1$$ that follows in $$p$$'s expansion.
Similarly, if
the algorithm had generated $$0.101$$ so far, we can show that if the next flip
does not match the following $$0$$, then the number is guaranteed to be larger than $$p$$.
This gives the following algorithm

1. Flip a coin until the $$n$$th coin fails to match $$b_n$$
2. Report success if $$b_n = 1$$ and failure otherwise.

Note this is essentially the same algorithm as mentioned above! The only difference
is the ending condition - instead of halting on heads, the algorithm halts
if the random bit does not match the "true" bit. Both happen $$1/2$$ the time,
so the two algorithms are equivalent.

Here's a sample run of the algorithm told in pictures. The green region represents
the possible values of $$x$$ as bits are generated. Initially, any $$x$$ is possible.

![Test](/public/biased-coin-imgs/interval_start.png)
{: .centered }

The first generated bit is $$0$$ , reducing the valid region to

![Test](/public/biased-coin-imgs/interval_first.png)
{: .centered }

This still overlaps $$[0,p]$$, so continue.

![Test](/public/biased-coin-imgs/interval_second.png)
{: .centered }

The third generated bit is $$1$$, giving

![Test](/public/biased-coin-imgs/interval_final.png)
{: .centered }

