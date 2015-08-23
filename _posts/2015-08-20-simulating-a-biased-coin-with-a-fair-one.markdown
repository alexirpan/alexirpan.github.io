---
layout: post
title:  "Simulating a Biased Coin With a Fair One"
date:   2015-08-20  01:10:00
---

Suppose you need a coin that lands heads with $$p = 1/4$$, and all you have is a
fair coin. Well, that's easy enough. Flip the coin twice. Report success if
you get 2 heads, and report failure otherwise. Two coin flips, not so bad.

Suppose you need a coin for $$p = 1/3$$. That may not
be a power of 2, but there is still a simple solution. Flip the fair coin twice.
Report success on HH, report failure on HT or TH, and try again on TT.
Conditioned on the process halting this iteration, we report success in
1 out of 3 events, all equally likely. Again, we're interested in the computation
time.
Each iteration takes $$2$$ coin flips. There is a $$3/4$$ probability
of halting, giving $$8/3$$ expected coin flips.

Now, suppose you needed to simulate the probability $$1/10^{100}$$.

Well, nothing is especially wrong with the current scheme, so let's see how it does.
We need $$\lceil\log_2(10^{100})\rceil = 333$$
coin flips to get enouch outcomes. Then, label 1 case as success, $$10^{100} - 1$$ as failure,
and the rest as retries. These numbers are getting messy, but we can at least
ballpark the expected number of flips.
By construction, the probability of halting
is $$> 1/2$$ since the scheme chooses the smallest power of $$2$$ that gives enough outcomes.
So, the expected number of flips is less than $$666$$.
Yes, that is...

(•\_•) ( •\_•)>⌐■-■ (⌐■\_■)
{: .centered }

a devilish upper bound, but things could be worse.

(I'm not sorry.)

Now, suppose you needed to simulate $$p = 1 / \pi$$.

Uhhhh....

Easy Optimizations
--------------------

We'll get back to the irrational case later.

Recall how we simulated $$p=1/4$$.
The scheme reports success only on HH. So, if the first flip lands
tails, we can halt immediately. The revised algorithm is

1. Flip a coin. If tails, report failure.
2. Flip a coin. Report success on heads and failure on tails.

This gives $$3/2$$ expected flips instead of $$2$$ flips.

Unfortunately, this optimization doesn't work as well for some values of $$p$4.
Suppose we used the current scheme for $$p = 1/5$$. First, divide the 8 outcomes
from 3 flips into 1 success case, 4 failure cases, and 3 retry cases.
These can be distributed as

- accept: HHH
- failing: THH, THT, TTH, TTT
- retry: HHT, HTH, HTT

If the first coin is T, we can stop immediately. If the first two coins are HT,
we can retry immediately. The only case left is HH, for which we need to see
the third flip before deciding what to do.

(This may give some of you flashbacks to prefix-free codes. If you haven't seen
those, don't worry, they won't show up in this post.)

With clever rearrangement, we can bundle outcomes of a given type under as few
unique prefixes as possible. This gives some improvement
for rational $$p$$, but still does not let us simulate irrational $$p$$.
For this, we need to switch to a new framework.

A New Paradigm
--------------------

I did not come up with this method - I discovered it from (LINK). I wish I
had come up with it, because the math works out so elegantly.

Suppose we need to simulate a coin that lands heads with probability $$p$$.
Let $$p = 0.b_1b_2b_3b_4b_5\ldots$$ be the binary expansion of $$p$$.
Proceed as follows.

- Flip a coin until it lands on heads.
- Let $$n$$ be the number of coins flipped. Report success if $$b_n = 1$$ and report failure
otherwise

The probability the process stops after $$n$$ flips
is $$1/2^n$$. The probability of success is

$$
    P[success] = \sum_{n: b_n = 1}^\infty \frac{1}{2^n} = p
$$

Now, figure out efficiency. It takes $$2$$ expected flips for the
coin to land heads. Thus, any biased coin can be simulated in $$2$$ expected flips.
This works for any $$p$$, including irrational ones.
Additionally, you can compute the bits $$b_i$$ lazily, making this implementable
in real life.

Slick, right? This idea may have been obvious to you, but it certainly wasn't to me.
After thinking about the problem more, I eventually recreated a potential chain
of reasoning to reach the same result.

Discrete Considerations of a Continuous Problem
--------------------
(Starting now, I will use $$1$$ interchangeably with heads and $$0$$ interchangeably
with tails.)

Consider the following algorithm.

1. Construct a real number in $$[0,1]$$ by flipping an infinite number of coins,
generating a random decimal $$0.b_1b_2b_3\ldots$$, where $$b_i$$ is the outcome
of coin flip $$i$$. Let this number be $$x$$.
2. Report success if $$x \le p$$ and failure otherwise.

This algorithm is correct as long as the decimals generated follow a
uniform distribution over $$[0, 1]$$. I won't prove this, but for an
appeal to intuition: any two bit strings of length $$k$$ are
generated with the same probabiilty $$1/2^k$$, and the numbers these
represent are evenly distributed over the interval $$[0, 1]$$. As $$k \to\infty$$
this approaches a uniform distribution.)

Assuming this all sounds reasonable, this algorithm works! Only, there is the
small problem of flipping $$\infty$$-ly many coins. However, similarly to the
$$p = 1/4$$ case, we can stop coin flipping as soon as
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

(You can easily extend this reasoning to $$p$$ with finite binary decimal expansions.
Consider that $$0.1 = 0.0111\ldots$$.)

Here's a sample run of the algorithm told in pictures. The green region represents
the possible values of $$x$$ as bits are generated. Initially, any $$x$$ is possible.

![0 to 1](/public/biased-coin-imgs/interval_start.png)
{: .centered }

The first generated bit is $$0$$ , reducing the valid region to

![0 to 0.5](/public/biased-coin-imgs/interval_first.png)
{: .centered }

This still overlaps $$[0,p]$$, so continue.

![0.25 to 0.5](/public/biased-coin-imgs/interval_second.png)
{: .centered }

The third generated bit is $$1$$, giving

![0.375 to 0.5](/public/biased-coin-imgs/interval_final.png)
{: .centered }

The feasible region for $$x$$ no longer intersects $$[0,p]$$, so the algorithm
reports failure.

CS-minded people may see similarities to binary search. Each bit chooses which
half of the feasible region we move to, and the halving continues until
the feasible region is a subset of $$[0,p]$$ or disjoint from $$[0,p]$$.

Proving Optimality
--------------------

This scheme is very, very efficient. Is there an algorithm that does
better than $$2$$ expected flips for any $$p$$?

It turns out that no, $$2$$ expected flips is optimal, and more suprisingly
the proof for this is pretty short.

For a given $$p$$, any algorithm can be represented by a computation tree.
That tree encodes whether the algorithm succeeds, fails, or continues
based on the next bit and all previously generated bits.

![Computation trees](/public/biased-coin-imgs/3-4.png)
{: .centered }

Two sample computation trees for $$p = 3/4$$.
{: .centered }

With the convention that the root is level $$0$$, children of the root are
level $$1$$, and so on down, let the *weight* of a node be $$1/2^{\text{level}}$$.
Equivalently, the *weight* is the probability the algorithm reaches that
node.

For a given algorithm and $$p$$, the expected number of flips is the expected
number of edges traversed in the computation tree, which is the expected
number of vertices visited ignoring the root.
By linearity of expectation,

$$
E[flips] = \sum_{v \in T, v \neq root} \text{weight}(v)
$$

For the algorithm to be correct, the sum of weights for all leaf nodes labeled
success must be $$p$$. For $$p$$ with infinitely long binary decimal expansions,
any correct algorithm we must have an infinitely deep computation tree. If the tree
had finite depth $$d$$, any leaf node weight would be a multiple of $$2^{-d}$$,
and it would be impossible to have the success weights sum to $$p$$.

Thus, the computation tree must be infinitely deep. To be infinitely deep, every
level of the tree (except the root) must have at least 2 nodes. Thus, a lower
bound on the expected number of fliips is

$$
E[flips] \ge \sum_{k=1}^\infty 2 \cdot \frac{1}{2^k} = 2
$$

and as we have shown earlier, this lower bound is acheivable. $$\blacksquare$$

(You can adapt this to prove optimality bounds for $$p$$ with finite
binary decimal expansions, which I'll leave as an exercise.)

The Takeaway
-----------------
From a very general perspective - although it is okay to use a quick and easy
solution, it is worth at least thinking about whether it can be improved.

From a math perspective - most results can be explained in many ways, and
framing a problem correctly can make proving things about it straightforward.

From a cool stuff perspective - this is one of my favorite results of all time,
since it turns all your coins into efficient arbitrarily biased coins.
