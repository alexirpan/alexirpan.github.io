---
layout: post
title:  "Read-through: Wasserstein GAN"
date:   2017-02-12 16:12:00 -0800
---

I really, really like the Wasserstein GAN paper. I know it's already gotten a lot
of hype, but I feel like it could use more.

I also think the theory in the paper scared off a lot of people, which is a bit
of a shame. This is my contribution to help fix that.

Why Is This Paper Important?
----------------------------------------------------------------------

There's a giant firehose of machine learning papers - how do you decide which
ones are worth reading closely?

For Wasserstein GAN, it was mostly compelling word of mouth.

* The paper proposes a new GAN training algorithm that works well on the
common GAN datasets.
* Said training algorithm is backed up by theory. This really piqued my
interest. In deep learning, not all theory-justified papers have good
empirical results, but theory-justified papers with good empirical
results have *really* good empirical results. For those papers, it's very
important to understand their theory, because the theory usually explains
why they perform so much better.
* I heard that in Wasserstein GAN,
you can (and should) train the discriminator to convergence
in Wasserstein GAN. If true, it would remove needing to balance between
generator updates and discriminator updates, which feels like one of the
big tricks needed to get GANs to work.
* The paper shows a correlation between discriminator loss and perceptual
quality. This is actually also really huge. In my limited GAN experience,
one of the big problems is that the loss doesn't really mean anything, thanks
to adversarial training. Reinforcement learning has a similar problem, but
at least we have mean episode reward. GANs get basically nothing.
Even a rough quantitative measure of quality could be good enough to use
hyperparam optimization tricks, like early stopping, Bayesian optimization,
etc.

Additionally, although I'm not a GAN person, I am an RL person, and as Oriol
observed, GANs have close ties to actor-critic reinforcement learning. It
seemed likely the paper would have interesting nuggets of information.

$$\blacksquare$$

At this point, you may want to download the paper yourself and read along with
these more informal notes. The upcoming section names correspond exactly with
the paper's section names.


Introduction
-----------------------------------------------------------------------

The paper first starts with explain some background on generative models.
In all cases, we assume the data we have comes from some unknown
distribution $$P_r$$. We want to learn a distribution $$P_\theta$$ that
approximates $$P_r$$. The function family $$\{P_\theta\}_{\theta \in \mathbb{R}^d}$$
is defined such that this is tractable.

You can imagine two approaches for doing this.

* The parameters $$\theta$$ directly describe a probability density.
Meaning, $$P_\theta$$ is a function such that $$\int P_\theta(x)\, dx = 1$$.
We optimize $$P_\theta$$ through maximum likelihood estimation.
* The parameters $$\theta$$ describe a way to transform an existing
distribution into $$P_\theta$$. In this setup, $$g_\theta$$ is a deterministic
function, $$Z$$ is a common distribution (usually uniform or Gaussian),
and $$P_\theta = g_\theta(Z)$$.

The first page of the paper is dedicated to explaining why the first approach hasn't worked
well.

The MLE objective is

$$
    \max_{\theta \in \mathbb{R}^d} \frac{1}{m}\sum_{i=1}^m \log P_\theta(x^{(i)})
$$

In the limit, this is equivalent to minimizing the KL-divergence
$$KL(P_r \| P_\theta)$$.

Recall that for discrete distributions $$P$$ and $$Q$$, the KL divergence is
defined as

$$
    KL(P || Q) = \int_x P(x) \log \frac{P(x)}{Q(x)} \,dx
$$

If $$Q(x) = 0$$ at an $$x$$ where $$P(x) \neq 0$$, then the KL divergence goes
to $$+\infty$$.

This is bad for the MLE if $$P_\theta$$ has low dimensional support. If $$P_\theta$$
isn't defined at every possible data point, the KL divergence will explode.
This motivated adding random noise to $$P_\theta$$ when training the
MLE. Empirically, people needed to add a lot of random noise to get models
to train, and that kind of sucks.

This motivates the latter approach. The other motivation of the latter
approach is that it's very easy to generate samples. Simply sample random noise
$$z$$, and evaluate $$g_\theta(z)$$. Even if we know the density $$P_\theta$$
explicitly, it may be hard to sample from it efficiently.

To train $$g_\theta$$ (and by extension $$P_\theta$$), we need a measure of
distance between distributions. (I will use metric, distance function, and
divergence interchangeably. I know this isn't technically accurate, but the
terms are all heavily conflated in my head.)

Around this point, the paper starts talking about distance functions inducing
weak or strong topologies. Different metrics induce different sets of convergent
sequences; a sequence that converges under one distance function may not
converge under another. The topology induced by distance $$\rho$$ is weaker
than the one induced by $$\rho'$$ if every sequence that converges under
$$\rho'$$ converges under $$\rho$$. (It's weaker because more things converge.)

Looping back to generative models, given a distance $$\rho$$, we can treat
$$\rho(P_r, P_\theta)$$ as a loss function. Minimizing $$\rho(P_r, P_\theta)$$
with respect to $$\theta$$ will bring $$P_\theta$$ close to $$P_r$$. This
is principled as long as the mapping $$\theta \mapsto P_\theta$$ is
continuous (which will be true if $$g_\theta$$ is a neural net).


Different Distances
--------------------------------------------------------------------------------

We know we want to minimize $$\rho$$, but how do we define $$\rho$$? This
section compares various distances and their properties.

Immediately, we're thrown into discussions of compact metric sets, Borel subsets,
and spaces of probability measures. Now, I'll be honest, my measure theory is
pretty bad. However, in machine learning, we're usually working with functions
that are "nice enough". I like to tell myself that as long as we aren't doing
any bullshit like the Cantor set, we're probably good, and all intuitions from
discrete probability carry over.

Anyways, on to the distances at play.

* The Total variation (TV) distance is

 $$\delta(P_r, P_g) = \sup_{A} | P_r(A) - P_g(A) |$$

 In words, find the subset of outcomes $$A$$ that maximizes the difference
in probability of falling in $$A$$.

* The Kullback-Leibler (KL) divergence is

$$KL(P_r\|P_g) = \int \log\left(\frac{P_r(x)}{P_g(x)}\right) P_r(x) dx$$

 This isn't symmetric. The reverse KL divergence is defined as $$KL(P_g \| P_r)$$.

* The Jenson-Shannon (JS) divergence. Let $$M$$ be the mixture distribution.
$$M = 1/2 P + 1/2 Q$$. Then

 $$JS(P_r,P_g) = KL(P_r\|P_m)+KL(P_g\|P_m)$$

* Finally, the Earth Mover (EM) or Wasserstein distance. Let $$\Pi(P_r, P_g)$$
be the set of all joint distributions $$\gamma$$ whose marginal distributions
are $$P_r$$ and $$P_g$$. Then.

 $$W(P_r, P_g) = \inf_{\gamma \in \Pi(P_r ,P_g)} E_{(x, y) \sim \gamma}\big[\:\|x - y\|\:\big]$$

Aside: What's Up With The Earth Mover Definition?
===============================================================================

The EM distance definition is a bit opaque. It took me a while to understand it,
but I was very pleased once I figured out the intuition. If you'd like to do so
on your own (or don't care about the intuition), jump to the black square.

Probability distributions are defined by how much mass they put on each point.
Imagine we started with distribution $$P_r$$, and wanted to move mass around
to change the distribution into $$P_g$$. Moving mass $$m$$ by distance $$d$$
costs $$m\cdot d$$ effort. The earth mover distance is the minimal effort
we need to spend.

Why is $$\Pi(P_r, P_g)$$ defined the way it is? You can think of each $$\gamma \in \Pi$$
as a transport plan.
To execute the plan, for all $$x,y$$ move $$\gamma(x,y)$$ mass
from $$x$$ to $$y$$.

Every strategy for moving weight can be represented this
way. But what properties does the plan need to satisfy to transform $$P_r$$ into $$P_g$$?

* The amount of mass that leaves $$x$$ is $$\int_y \gamma(x,y) dy$$. This
must equal $$P_r(x)$$, the amount of mass originally at $$x$$.
* The amount of mass that enters $$y$$ is $$\int_x \gamma(x,y) dx$$. This
must equal $$P_g(y)$$, the amount of mass that ends up at $$y$$.

This shows why the marginals of $$\gamma \in \Pi$$ must be $$P_r$$ and $$P_g$$.
For scoring, the effort spent is
$$\int_x \int_y \gamma(x,y) \| x - y \| dy dx = E_{(x,y) \sim \gamma}\big[\|x - y\|\big]$$
Computing the infinum of this over all valid $$\gamma$$ gives the earth
mover distance.

$$\blacksquare$$

Now, the paper introduces a simple example to argue why we should care about
the Earth-Mover distance.

Consider probability distributions defined over $$\mathbb{R}^2$$. Let the
true data distribution be $$(0, y)$$, with $$y$$ sampled uniformly from $$U[0,1]$$.
Consider the family of distributions $$P_\theta$$, where $$P_\theta = (\theta, y)$$,
with $$y$$ also sampled from $$U[0, 1]$$.

![Picture of distributions described above](/public/wasserstein/distribution.png)
{: .centered }

Real and fake distribution when $$\theta = 1$$
{: .centered }

We'd like our optimization algorithm to learn to move $$\theta$$ to $$0$$,
As $$\theta \to 0$$, the distance $$\rho(P_0, P_\theta)$$
should decrease. But for many common distance functions, this doesn't happen.

* Total variation: For any $$\theta \neq 0$$, let $$A = \{(0, y) : y \in [0,1]\}$$.
This gives

 $$ \delta(P_0, P_\theta) =
  \begin{cases}
    1 &\quad \text{if } \theta \neq 0~, \\
    0 &\quad \text{if } \theta = 0~.
  \end{cases}
 $$

* KL divergence and reverse KL divergence: Recall that the KL divergence $$KL(P\|Q)$$ is $$+\infty$$ if there
is any point $$(x,y)$$ where $$P(x,y) > 0$$ and $$Q(x,y) = 0$$. For $$KL(P_0 \| P_\theta)$$,
this is true at $$(\theta, 0)$$. For $$KL(P_\theta \| P_0)$$, this is true at
$$(0, 0)$$.

 $$ KL(P_0 \| P_\theta) = KL(P_\theta \| P_0) =
  \begin{cases}
    +\infty &\quad \text{if } \theta \neq 0~, \\
    0 &\quad \text{if } \theta = 0~,
  \end{cases}
 $$

* Jenson-Shannon divergence: Consider the mixture $$M = \frac{1}{2} P_0 + \frac{1}{2} P_\theta$$,
and now look at just one of the KL terms.

 $$
    KL(P_0 \| M) = \int_{(x,y)} P_0(x,y) \log \frac{P_0(x,y)}{(\frac{1}{2}P_0 + \frac{1}{2}P_\theta)(x,y)} dxdy
 $$

 For any $$x,y$$ where $$P_0(x,y) \neq 0$$, $$M(x,y) = \frac{1}{2} P_0(x,y)$$, so
this integral works out to $$\log 2$$. The same is true of $$KL(P_\theta \| M)$$,
so the JS divergence is

 $$ JS(P_0, P_\theta) =
  \begin{cases}
    \log 2 &\quad \text{if } \theta \neq 0~, \\
    0 &\quad \text{if } \theta = 0~,
  \end{cases}
 $$

* Earth Mover distance: Because the two distributions are just translations of one
another, the best way transport plan is moving the weight in a straight line.
This gives $$W(P_0, P_\theta) = |\theta|$$

**This example shows that there exist sequences of distributions that don't
converge under the JS, KL, reverse KL, or TV divergence, but which do converge
under the EM distance.**

**This example also shows that for the JS, KL, reverse KL, and TV divergence,
there are cases where the gradient is always $$0$$.** This is especially
damning from an optimization perspective - any approach that works by
taking the gradient $$\nabla_\theta \rho(P_0, P_\theta)$$ could fail badly.

Admittedly, this is a contrived example because the supports are disjoint, but
the paper points out that when the supports are low dimensional manifolds in
high dimensional space, it's very easy for the intersection to be measure zero,
and you can get similarly bad results for the TV and KL divergences.

This argument is then strengthened by the following theorem.

> Let $$P_r$$ be a fixed distribution. Let $$Z$$ be a random variable.
> Let $$g_\theta$$ be a deterministic function parametrized by $$\theta$$, and let $$P_\theta = g_\theta(Z)$$.
> Then,
>
> 1. If $$g$$ is continuous in $$\theta$$, so is $$W(P_r, P_\theta)$$.
> 2. If $$g$$ is sufficiently nice, then $$W(P_r, P_\theta)$$ is continuous
> everywhere, and differentiable almost everywhere.
> 3. Statements 1-2 are false for the Jensen-Shannon divergence $$JS(P_r, P_\theta)$$
> and all the KLs.

You'll need to refer to the paper to see what "sufficiently nice" means, but
for our purposes it's enough to know that it's satisfied for feedfoward
networks that use standard nonlinearites. Thus, out of JS, KL, and Wassertstein
distance, only the Wasserstein distance has guarantees of continuity and
differentiability, which are both things you really want in a loss function.

The second theorem shows that not only does the Wasserstein distance
give better guarantees, it's also easier to optimize.

> Let $$P$$ be a distribution, and $$(P_n)_{n \in \mathbb{N}}$$ be a sequence
> of distributions. Then, the following are true about the limit.
>
> 1. The following statements are equivalent.
>   * $$\delta(P_n, P) \to 0$$
> with $$\delta$$ the total variation distance.
>   * $$JS(P_n,P) \to 0$$ with
> $$JS$$ the Jensen-Shannon divergence.
> 2. The following statements are equivalent.
>   * $$W(P_n, P) \to 0$$.
>   * $$P_n \rightarrow P$$, where $$\rightarrow$$ represents
> convergence in distribution for random variables.
> 3. $$KL(P_n \| P) \to 0$$ or $$KL(P \| P_n) \to 0$$ imply
> the statements in (1).
> 4. The statements in (1) imply the statements in (2).

Together, this proves that every distribution that converges under the
KL, reverse-KL, TV, and JS divergences also converges under the Wasserstein
divergence, and that the topology from the Wasserstein distance is indeed weak.
It also proves that a small earth mover distance corresponds to a small
difference in distributions.

Combined, this shows that the Wasserstein distance is a compelling loss function
for generative models.

Wasserstein GAN
-----------------------------------------------------------------------------------

Unfortunately, computing the Wasserstein distance exactly is intractable.
Let's repeat the definition below.

 $$W(P_r, P_g) = \inf_{\gamma \in \Pi(P_r ,P_g)} E_{(x, y) \sim \gamma}\big[\:\|x - y\|\:\big]$$

The paper now shows how we can compute an approximation of this.

A result from Kantorovich-Rubinstein duality showed $$W$$ was equivalent to.

$$W(P_r, P_\theta) = \sup_{\|f\|_L \leq 1}
E_{x \sim P_r}[f(x)] - E_{x \sim P_\theta}[f(x)]$$

where the supremum is taken over all $$1$$-Lipschitz functions.

Aside: What Does Lipschitz Mean?
===============================================================================

Let $$d_X$$ and $$d_Y$$ be metrics on spaces $$X$$ and $$Y$$. (In our case, this
will always be Euclidean distance, but might as well be complete.)
A function $$f: X \to Y$$ is $$K$$-Lipschitz if for all $$x_1, x_2 \in X$$,

$$
    d_Y(f(x_1), f(x_2)) \le K d_X(x_1, x_2)
$$

Intuitively, a $$K$$-Lipschitz function never has a slope more than $$K$$. We're
just generalizing slope to general domains with general distance functions.

$$\blacksquare$$

Note that if we replace the supremum over $$1$$-Lipschitz functions
with the supremum over $$K$$-Lipschitz functions, then the supremum is
$$K \cdot W(P_r, P_\theta)$$ instead. (This is true because every $$K$$-Lipschitz
function is a $$1$$-Lipschitz function if you divide it by $$K$$, and the Wasserstein
objective is linear.)

The supremum over $$K$$-Lipschitz functions $$\{f : \|f\|_L \le K\}$$ is still
intractable, but now it's easier to approximate.
Suppose we have a parametrized function family $$\{f_w\}_{w \in \mathcal{W}}$$,
where $$w$$ are the weights and $$\mathcal{W}$$ is the set of all possible
weights. Further suppose these functions are all
$$K$$-Lipschitz for some $$K$$. Then we have

$$
    \max_{w \in \mathcal{W}}
        E_{x \sim P_r}[f_w(x)] - E_{x \sim P_\theta}[f_w(x)]
    \le \sup_{\|f\|_L \le K}
        E_{x \sim P_r}[f(x)] - E_{x \sim P_\theta}[f(x)]
    = K \cdot W(P_r, P_\theta)
$$

For optimization purposes, we don't even need to care what $$K$$ is!
It's enough to know that it exists, and that it's fixed throughout
training process. Sure, gradients of $$W$$ will be scaled by an unknown $$K$$,
but they'll also be scaled by the learning rate $$\alpha$$, so $$K$$ will
get absorbed into the hyperparam tuning.

If $$\{f_w\}$$ contains the true supremum among
$$K$$-Lipschitz functions, this gives the distance exactly. This probably won't
be true. In that case, the approximation's
quality depends on what $$K$$-Lipschitz functions are missing from $$\{f_w\}$$.

Now, let's loop all this back to generative models.
We'd like to train $$P_\theta = g_\theta(Z)$$ to match $$P_r$$. Intuitively, given a fixed
$$g_\theta$$, we can compute the optimal $$f_w$$
for the Wasserstein distance. We can then backprop through $$W(P_r, g_\theta(Z))$$
to get the gradient for $$\theta$$.

$$
    \nabla_\theta W(P_r, P_\theta) = \nabla_\theta (E_{x \sim P_r}[f_w(x)] - E_{z \sim Z}[f_w(g_\theta(x))]) = -E_{z \sim Z}[\nabla_\theta f_w(g_\theta(z))]
$$

The training process has now broken into three steps.

* For a fixed $$\theta$$, compute an approximation of $$W(P_r, P_\theta)$$ by
training $$f_w$$ to convergence.
* Once we find the optimal $$f_w$$, compute the $$\theta$$ gradient $$-E_{z \sim Z}[\nabla_\theta f_w(g_\theta(z))]$$
by sampling several $$z \sim Z$$.
* Update $$\theta$$, and repeat the process.

There's one final detail. This entire derivation only works when the
function family $$\{f_w\}$$ is $$K$$-Lipschitz. To guarantee this is true,
we use weight clamping. The weights $$w$$ are constrained to lie within $$[-c, c]$$,
by clipping $$w$$ after every update to $$w$$.

The full algorithm is below.

![Picture of algorithm because it was too hard to typeset](/public/wasserstein/algorithm.png)
{: .centered }

Aside: Compare & Contrast: Standard GANs
===================================================================================

Let's compare the WGAN algorithm with the standard GAN algorithm.

* In GANS, the discriminator maximizes

    $$
  \frac{1}{m} \sum_{i=1}^m \log D(x^{(i)}) + \frac{1}{m} \sum_{i=1}^m \log (1 - D(g_\theta(z^{(i)})))
    $$

    where we constraint $$D(x)$$ to always be a probabiity $$p \in (0, 1)$$.

In WGANs, nothing requires $$f_w$$ to output a probability. This explains why
the authors tend to call $$f_w$$ the critic instead of the discriminator -
it's not explicitly trying to classify inputs as real or fake.

* As argued in the original GAN paper, in the limit the maximum of the objective
above is the Jenson-Shannon divergence instead of the Wasserstein divergence.
(This is true up to scaling and constant factors.)

In practice, we never train $$D$$ to convergence.
In fact, usually the discriminator is too strong, and we need to alternate
gradient updates between $$D$$ and $$G$$ to get reasonable generator updates.
So we aren't updating $$G$$ against the Jenson-Shannon divergence, or even an
approximation of the Jenson-Shannon divergence, we're updating $$G$$ against
an objective that kind of aims towards the JS divergence, but doesn't go
all the way. It certainly works, but in light of the points this paper
makes about gradients of the JS divergence, it's a bit surprising it does work.

In contrast, because the earth mover distance is differentiable nearly everywhere,
we can (and should) train $$f_w$$ to convergence before each generator update,
to get as accurate an estimate of $$W(P_r, P_\theta)$$ as possible.


Empirical Results
--------------------------------------------------------------------------------

First, the authors set up a small experiment to showcase the difference between
GAN and WGAN. There are two 1D Gaussian distributions, blue for real and green
for fake. Train a GAN discriminator and WGAN critic to optimality, then
plot their values over the space.
The red curve is the GAN discriminator output, and
the cyan curve is the WGAN critic output.

![Distribution comparison](/public/wasserstein/gauss1d.png)
{: .centered }

Both identify which distribution is real and which is fake, but the GAN
discriminator does so in a way that makes gradients vanish over most of the space.
In contrast, the weight clamping in WGAN gives a reasonably nice gradient over
everything.

Next, the Wasserstein loss seems to correlate well with image quality. Here,
the authors plot the loss curve over time, along with the generated samples.

![Loss curve and photos](/public/wasserstein/w_mlp512.png)
{: .centered }

After reading through the paper, this isn't too surprising. Since we're training
the critic $$f_w$$ to convergence, these critic's value should be good approximations of
$$K \cdot W(P_r, P_\theta)$$, where $$K$$ is whatever the Lipschitz constant
is. As argued before, a low $$W(P_r, P_\theta)$$ means $$P_r$$ and $$P_\theta$$ are "close"
to one another. It would be more surprising if the critic value
*didn't* correspond to visual similarity.

The image results also look quite good. Compared to the DCGAN baseline on the
bedroom dataset, it performs about as well.

![WGAN with DCGAN architecture](/public/wasserstein/wgan_bn.png)
{: .centered }

![DCGAN with DCGAN architecture](/public/wasserstein/dcgan_bn.png)
{: .centered }

*Top:* WGAN with the same DCGAN architecture. *Bottom:* DCGAN
{: .centered }

If we remove batch norm from the generator, WGAN still generates okay samples,
but DCGAN fails completely.

![WGAN with DCGAN architecture, no batch norm](/public/wasserstein/wgan_nobn.png)
{: .centered }

![DCGAN with DCGAN architecture, no batch norm](/public/wasserstein/dcgan_nobn.png)
{: .centered }

*Top:* WGAN with DCGAN architecture, no batch norm. *Bottom:* DCGAN, no batch norm.
{: .centered }

Finally, we make the generator a feedforward net instead of a convolutional one.
This keeps the number of parameters the same, while removing the inductive
bias from convolutional models. The WGAN samples are more detailed, and don't
mode collapse as much as standard GAN. In fact, they report never running
into mode collapse at all for WGANs!

![WGAN with MLP architecture](/public/wasserstein/wgan_mlp.png)
{: .centered }

![DCGAN with MLP architecture](/public/wasserstein/gan_mlp.png)
{: .centered }

*Top:* WGAN with MLP architecture. *Bottom:* Standard GAN, same architecture.
{: .centered }

$$\blacksquare$$

The read-through of the paper ends here. If you're interested in related work,
or the proofs for the theorems, you'll have to read the paper.


Follow-Up Questions
------------------------------------------------------------------------------

This is a rich enough paper to have several natural follow-up questions.

The weights in $$f_w$$ are clamped to $$[-c, +c]$$. How important is $$c$$
for performance? Based on lurking /r/MachineLearning, the tentative results
say that low $$c$$ trains more reliably, but high $$c$$ trains faster when
it does work. I imagine $$\{f_W\}$$ imagine the discrepancy between the two sets
changes with $$c$$. There could be interesting work in describing that discrepancy,
or in finding ways to make $$\{f_w\}$$ be closer to $$K$$-Lipschitz functions
while still be optimizable.

Given a fixed critic architecture and fixed $$c$$ for clamping, can we
quantitatively compare different generators by computing the
Wasserstein estimate of both? Note there's an approximation
error from optimizing over $$\{f_w: w \in \mathcal{W}\}$$ instead of $$\{f: \|f\|_L \le K\}$$,
so the estimate may not be accurate. However, because we fix both the critic
architecture and $$c$$, the hope is that most of the error is some universal
error that appears in all distributions. If the approximation error doesn't change
too much between distributions, this would give a way to judge generation quality
without relying on Mechanical Turk. (And if the error does change a lot, it would probably be
interesting to investigate when that happens.)

The constant $$K$$ depends on both $$c$$ and the model architecture, and
therefore we can't directly compare the critics between models with different
architectures. Is there a way to estimate $$K$$? Recall the critic objective
converges to $$K \cdot W(P_r, P_\theta)$$, so dividing by $$K$$ would normalize
the difference between architectures.

* This actually seems pretty straightforward. Take either a random generator or
pretrained generator, then train critics $$f_w$$ from varying architectures and
compare their final values. Again, the approximation error could complicate
this, but this could be a way to analyze the approximation error itself. Given
a few different generators, the change in estimated $$K$$ between different
distributions would show how important the distribution is to the approximation
error.

How important is it to train the critic to convergence? A converged critic
gives the most accurate gradient, but it takes more time.
In settings where that's impractical, can a simple alternating gradient
scheme work?

Are ideas from this work are applicable to actor-critic RL? At a first
glance, I'm now very interested in investigating the magnitude of the actor
gradients. If they tend to be very large or very small, we may have a similar
saturation problem, and adding a Lipschitz bound through weight clamping
could help give better gradients.

Are there any low-hanging distribution matching problems? Personally,
I have my eye on imitation learning. The
Generative Adversarial Imitation Learning paper showed a GAN approach made
sense, and there could be easy gains just from switching to a WGAN approach.

