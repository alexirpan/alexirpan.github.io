---
layout: post
title:  "Readthrough: Wasserstein GAN"
date:   2017-02-12 16:12:00 -0800
---

These are personal notes about the Wasserstein GAN paper that I made as I read
through the paper. The notes are written for me - as such I'm putting very
little effort into making sure they're clear to others, and will be very loose
with notataion. My hope is that parts of this will still be comprehensible.

Why Is This Paper Important?
----------------------------------------------------------------------

This paper makes a bunch of interesting points.

* Proposes a new GAN training algorithm that produces pretty good samples on
various datasets.
* Said training algorithm is justified by theory. The pattern I've seen in
deep learning is that not all theory-justified papers have good experimental
results, but theory-justified papers with good empirical results have *really*
good empirical results.
* Shows a correlation between loss and perceptual quality. This is actually
huge if it holds up across different problems. In my limited GAN experience,
one of the big problems is that the loss doesn't really mean anything, thanks
to adversarial training. Reinforcement learning has a similar problem, but
at least we have episode reward. GANs only get, I don't know, Mechanical Turk.
Even a rough quantitative measure of quality could be good enough to
use tricks like early stopping.

So, even though I'm not a GAN person, this paper has the potential to change
the game on GANs, and even if I don't use GANs in the near future, it'll likely
be good for me to know the ideas from this paper. This is especially true
because I buy Oriol's argument that GANs have close ties to actor-critic
reinforcement learning.

Introduction
-----------------------------------------------------------------------

(You may want to pick up the paper and start scanning through it yourself
at this point.)

Alright, sets up the problem of learning a probability distribution, by
finding the best distribution out of a parametrized
function family $$(P_\theta)$$.

They say that in the limit, maximizing the likelihood is equivalent to
minimizing $$KL(P_r \| P_\theta)$$, which sounds reasonable. It's been
a while since I verified the math but that's fine. They then say that
if distribution $$P_\theta$$ has low dimensional support (say if the dimensionality
of $$\theta$$ isn't high enough), then the KL distance isn't defined
or is infinite.

This pans out, remember that

$$
    KL(P || Q) = \sum_p p\log{p} - \sum_p p\log{q}
$$

If $$P_\theta$$ is 0 when $$P_r$$ isn't 0, then the latter summation will go to $$\infty$$.

(Yes, I know that these distributions are continuous, but my intuition refuses
to accept continuous distributions as a thing. I use summations in my head, and
assume that with nice enough distributions, I can turn all the sums into integrals
and everything will just work out.)

In total, for the MLE approach, if $$P_\theta(x^{(i)})$$ is $$0$$ for any $$x$$
in the data, the objective goes to $$-\infty$$, which is bad. So for the MLE to
make sense we need to add random noise to make sure the probability is never 0,
and empirically we need to add a lot of random noise to get nice training. That
kinda sucks.

Which then motivates the discussion of approaches closer to GANs and VAEs. In
these models we have some distribution $$Z$$ and a deterministic
$$g_\theta: : Z \to X$$. Let $$Z = N(0, I)$$, because that's what everyone does
these days. We can think of each $$g_\theta$$ as inducing a distribution,
if we define $$P_\theta := g_\theta(Z)$$.

Now that we have distributions, we want a measure of distance between
distributions. We want a metric because we want a notion of convergence - we want
the distribution $$P_\theta$$ to converge to the data distribution $$P_r$$,
and the convergence definition needs a distance.

Paper starts talking about distance functions inducing topologies, with weaker
topologies happening when it's easier for a sequence of distributions to converge.
Then there's a footnote.

> More exactly, the topology induced by ρ is weaker than that induced by ρ'
> when the set of
> convergent sequences under
> ρ
> is a superset of that under
> ρ'

Oh okay, so a topology is weaker than another one if everything that converges under
the first's notion of distance also converges under the second's notion of distance.
Got it. Cool.

We want the mapping $$\theta \to P_\theta$$ to be continuous, because if that's
true, then a converging $$\theta$$ gives converging distributions $$P_\theta$$.
La dee dah, okay. Oh, but then there's a neat point - convergence is defined
with respect to the metric of the space. We get to choose the distance function,
so we want one that leads to continuity.

Summary of sections that I already read when deciding to closely read this paper
in the first place.

Different Distancess
--------------------------------------------------------------------------------

This section is about comparing the properties of different distance functions.

It starts by talking about compact metric sets $$X$$, and Borel subsets $$\Sigma$$ of $$X$$, and so forth,
and to be honest my measure theory isn't that good. But intuitively, I just
think of all of this as "things are nice enough to make everything go through",
and I assume they're defined such that all the intuitions I have about probability
keep working.

Anyways, on to the distances.

* Total variation distance,

$$
    \delta(P_r, P_g) = \sup_{A \in \Sigma} | P_r(A) - P_g(A) |
$$

Or in words, the subset of outcomes that maximize the difference in mass
one distribution has versus the other.

PICTURE?

* KL divergence

$$
    KL(P_r | P_q) = \sum p \log{p} - \sum p \log{q}
$$

which as we saw before, isn't symmetric and could be inifinite.

* The Jenson-Shannon (JS) divergence, which is defined by taking the mixture
$$M = 1/2 P + 1/2 Q$$, then averaging the KL divergenccs between $$P$$ and $$M$$
and $$Q$$ and $$M$$.

* Finally, the Wasserstein, or earth-mover distance. The definition is pretty
opaque at first.

DEFINITION

The intuitive definition is that probability distributions are defined by how
much mass they put on each point. It costs effort to move mass from one point to
another, and the minimal effort needed is the the distance according to the
Wasserstein metric.

I didn't understand this for a bit, but I think I understand the intuition
now. Let me digress for a bit.

We're taking the infinum over all joint distributions whose marginals
match $$P_r$$ and $$P_g$$. This means that for all $$y$$, every distribution
$$\gamma$$ satisfies

$$
    \sum_x \gamma(x, y) = P_g(y)
$$

Now, let's consider $$E_{(x,y) ~ \gamma} [ \| x - y\|]$$ for a fixed $$y$$.
That expectation expands to

$$
    \sum_x \gamma(x,y) \|x - y \|
$$

Intuitively, this is the same as

* Enumerating all locations $$x$$ where $$\gamma(x,y) \neq 0$$.
* Move some weight from $$y$$ to $$x$$, where the weight moved is $$\gamma(x, y)$$.
* It takes 1 unit of work to move 1 unit of mass 1 unit of distance.
Charge accordingly.

Because the marginal distribution is the same, we know that all the mass at $$y$$
must be charged in this way.

Now, the paper introduces a simple example to argue why we should care about
the Earth-Mover distance.

Consider probability distributions defined over $$\mathbb{R}^2$$. Let the
true data distribution be $$(0, y)$$, with $$y$$ sampled uniformly from $$U[0,1]$$.
Consider the family of distributions $$P_\theta$$, where $$P_\theta = (\theta, y)$$,
with $$y$$ also sampled from $$U[0, 1]$$. We'd like our optimization algorithm
to learn to move $$\theta$$ to $$0$$.

According to intuition, as $$\theta \to 0$$, the distribution $$P_\theta$$ is
getting closer to $$0$$, and the distance between $$P_0$$ and $$P_\theta$$
should decrease. But for many common distance functions, this doesn't happen.

* Total variation: For any $$\theta \neq 0$$, let $$A$$ be the support of
$$P_0$$, meaning all $$(x,y)$$ where $$P_0(x, y) \neq 0$$. Because the distributions
have disjoint support, we have CASES
* KL divergence and reverse KL divergence: Recall that the KL divergence $$KL(P\|Q)$$ is $$+\infty$$ if there
is any point $$(x,y)$$ where $$P(x,y) > 0$$ and $$Q(x,y) = 0$$. For $$\theta \neq 0$$,
the distributions have disjoint support, so we can always find a point $$(0,y)$$
or $$(\theta, y)$$ where this is true. CASES
* Jenson-Shannon divergence: In the expression

$$
    KL(P_0 \| \frac{1}{2} P_0 + \frac{1}{2} P_\theta) = \sum_{(x,y)} P_0(x,y) \log \frac{P_0(x,y)}{(\frac{1}{2}P_0 + \frac{1}{2}P_\theta)(x,y)}
$$

the fraction of probabilities is always $$2$$.
So $$KL(P_0 \| \frac{1}{2} P_0 + \frac{1}{2} P_\theta) = \log(2)$$, and thus CASES

If our optimization algorithm was based off taking the gradient $$d(P_0, P_\theta)$$,
then if we used any of these as our distance function, the gradient would be
$$0$$ for all $$\theta \neq 0$$.

However, with the Wasserstein-1 distance, the distance does decrease.

* Wasserstein-1: Because the two distributions are just translations of one
another, the best way to move weight is by a straight line. Therefore,
$$W(P_0, P_\theta) = |\theta|$$

**This example shows that there exist sequences of distributions that don't
converge under the JS, KL, reverse KL, or TV divergence, but which do converge
under the Wasserstein-1 distance.**

This is a contrived example because the supports are disjoint, but the paper then
points out that when working with low dimensional manifolds in high dimensional spaces,
this case is easy to hit unless you actively try to avoid it.

This argument is then strengthened by the following theorem.

THEOREM

The conditions in statement 1 and 2 are satisfied by feedforward networks, and
thus this result guarantees that $$W(P_r, P_\theta)$$ is differentiable almost
everywhere, making it a reasonable loss function. Furthermore, this is **not**
true for the JS, KL, or reverse-KL divergences.

The second theorem proved strengthens the argument even further,

THEOREM

Together, this proves that

* If a sequence converges under the KL or reverse-KL divergence, it converges
under the TV and JS divergence too.
* If a sequence converges under the TV or JS divergence, it converges
under the Wasserstein distance.

This shows the topology under the Wasserstein distance is indeed weak, as stated
earlier in the paper; the set of convergent sequences is strictly larger than
the alternatives given.

Furthermore, when the Wasserstein distance approaches $$0$$, the distributions
