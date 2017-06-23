---
layout: post
title:  "Read-through: Hyperparameter Optimization: A Spectral Approach"
date:   2017-06-18 00:52:00 -0700
---

Similar to Wasserstein GAN, this is another theory-motivated paper with neat
applications to deep learning. Once again, the paper has a lot of theory, but
if you allow for some looseness in rigor, the core idea isn't too difficult
to implement.

This, by the way, is the general trend with many theory papers - the
algorithm isn't that bad, but the runtime proof is complicated. If you're looking
to do theory, you should read the paper. If, however, you're just looking to
apply the method, keep reading.

Why Is This Paper Important?
----------------------------------------------------------------------

I really, really don't like doing hyperparam optimization. Nobody does. It's
grunt work that's required to get the best results, and it has to be done, but
that doesn't mean I like doing it.

Because of this, I try to keep an eye on the hyperparam optimization space.
For one, anything that lets me spend less time on hyperparam optimization makes
me happy, because it means I can get to the parts of research I actually like.

Also, I think it's always worth keeping an eye on the current state of
black-box optimization and meta-learning.

Some Quick Background
---------------------------------------------------------------------

For two approachable introductions to the subject, I highly recommend two blog
posts from Ben Recht's blog, linked [here](http://www.argmin.net/2016/06/20/hypertuning/)
and [here](http://www.argmin.net/2016/06/23/hyperband/). They're very short,
but if you're really lazy, here's my summary.

* One simple benchmark for hyperparam optimization is random search. This can
be really difficult to beat. Random search can't exploit any existing structure
in the problem, but it also means it can't get exploited by pathological
problems.
* Another common approach is Bayesian optimization, where you fit a distribution
(i.e. a mixture of Gaussians)
based on the data so far, sample a new point based on uncertainty and estimated
performance, and update the distribution.
* In practice, Bayesian optimization does a bit better than random search, but
not by a lot, and is often outperformed by simply running random search at twice
the speed. Yes, the random search gets more compute time, but sometimes it's a
lot easier to just ask for another computer.
* One way to speed up random search is by doing *successive halving*. The idea
of this approach is, you run $$N$$ hyperparam settings at once. After running
each for time $$T$$, stop the bottom half runs and keep going. After running
each for time $$2T$$ total, stop the bottom half, and keep going again. By
repeatedly pruning bad runs, you get to try more settings in the same amount
of computation time. This is later extended to the Hyperband algorithm,
described [here](https://arxiv.org/abs/1603.06560).


Problem Setting
---------------------------------------------------------------------------

The paper focuses on discrete hyperparameter optimization. Generally, optimizing
over discrete choice is harder than optimizing over continuous ones, and it's
easy to discretize continuous spaces, and hard to relax discrete choices to
continuous ones. Additionally, some prior work showed that when your hyperparam
is continuous, gradient descent in hyperparam space can be good enough (ADD
CITATION HERE.)

Specifically, the paper assumes all hyperparams are binary variables with value
$$-1$$ or $$+1$$. In this setting, if there are $$n$$ hyperparams, we're trying
to learn a function $$f: \{-1,+1\}^n \to \mathbb{R}$$, where the input is
the hyperparam setting, and the output is the performance of the trained model.
In the upcoming sections, we'll use two different notations.

* $$f(x)$$, in which case $$x = (x_1,x_2,x_3,\ldots, x_n)$$ is some $$n$$-bit
vector.
* $$f(x_1,x_2,\ldots,x_n)$$, in which case each $$x_i$$ is either $$-1$$ or $$+1$$
and we interpret the function as a polynomial of $$n$$ variables.

Next is the key guiding framework of the algorithm - hyperparam optimization
can be interpreted as a compressed sensing problem. This interpretation comes
from signal processing. More specifically, we try to learn a sparse,
low-degree polynomial that approximates $$f$$.

My intrepretation is that to do better than random search, your hyperparam
optimization needs to learn something about the structure of the problem. By
doing a low-degree polynomial fitting, you can avoid having your polynomial
overfit to the data. (Remember that we're not going to have a lot of data points,
because each data point requires training a neural net to convergence.)
Sparsity helps with this too, by preventing the polynomial fitting from putting
a little bit of weight on thousands of different terms (which hurts interpretability
and also helps prevent overfitting.)

(Incidentally, this is one of the common complaints about deep learning - it's
hard to interpret the sum of 100 small scalars. But in deep learning, the problems
usually have a ton of capacity and a ton of data, and enforcing sparsity just
ends up hurting performance.)

Evaluating $$f(x)$$ for some fixed $$x$$ takes "a long time, but not too long". By this, we mean
it takes more than $$O(n^d)$$ time, for some reasonably small $$d$$, but it runs
in subexponential time.

To fit a low-degree polynomial, first note that functions $$f: \{-1,+1\}^n \to \mathbb{R}$$
form an [inner product space](https://en.wikipedia.org/wiki/Inner_product_space).
Define the inner product as

$$
    \langle f, g\rangle = \mathbb{E}_{x} [f(x)g(x)]
$$

where the expectation is over the uniform distribution. We can verify this
satisfies the inner product definitions.

* Symmetry:

$$
    \langle f, g\rangle = \mathbb{E}_{x} [f(x)g(x)] =\mathbb{E}_{x} [g(x)f(x)] = \langle g,f \rangle
$$

* Linearity: for some constant $$a$$,

$$
    \langle af, g \rangle = \mathbb{E}_{x} [af(x)g(x)] = a \mathbb{E}_x [f(x)g(x) = a\langle f, g\rangle
$$

For functions $$f_1, f_2$$,

$$
    \langle f_1+f_2, g\rangle = \mathbb{E}_x[(f_1(x) + f_2(x))g(x)] = \mathbb{E}_x [f_1(x)g(x)] + \mathbb{E}_x [f_2(x)g(x) = \langle f_1, g\rangle + \langle f_2, g\rangle
$$

* Positive definiteness.

$$
    \langle f, f\rangle = \mathbb{E}_x[f(x)^2] \ge 0
$$

For $$\langle f, f\rangle$$ to be $$0$$, we need the expectation of $$f(x)^2$$ over all
$$x$$ to be $$0$$, and since $$f$$ is real-valued, this can only happen when $$f(x) = 0$$ everywhere.


Next, we want to find an orthonormal basis for this inner product space. For
Boolean functions, there's a well known example. Let $$S \subset [n]$$ be a
subset of indicies $$1$$ to $$n$$. Define $$f_S(x)$$ as

$$
    f_S(x) = \prod_{i \in S} x_i
$$

The functions $$\{f_S\}$$ form an orthonormal basis. This is also known as
the set of parity functions.

Why is this an orthonormal basis? A set $$\{f_1, f_2, \ldots, f_n\}$$
is orthonormal if it satisfies two properties.

* For every $$f_i$$, $$\langle f_i, f_i \rangle = 1$$.
* For every $$f_i, f_j$$ where $$i \neq j$$, $$\lange f_i, f_j \rangle = 0$$.

Now, we show the parity functions have this property.

* By defintion, $$\langle f_i, f_i \rangle = \mathbb{E}[f_i(x)^2]$$. Note
that $$f_i(x) = -1$$ or $$f_i(x) = 1$$, depending on how many bits of $$x$$
match. In either case, $$f_i(x)^2 = 1$$ for all $$x$$, $$\langle f_i, f_i \rangle = 1$$.
* For any two different subsets $$S_1, S_2$$, there exists some $$i$$ in one,
but not the other. Without loss of generality, let $$i in S_1$$ and $$i \not\in S_2$$.
We can write $$f_{S_1}(x)$$ as

$$
    f_{S_1}(x) = x_i \prod_{j \in S_1 - \{i\}} x_j
$$

Take the expectation over $$x$$, and move the $$x_i$$ term out.

$$
    \langle f_{S_1}, f_{S_2} \rangle = \mathbb{E}[f_{S_1}(x)f_{S_2}(x)]
    = \mathbb{E}_{x_i}[\mathbb{E}_{x|x_i}[x_i \prod_{j \in S_1 - \{i\}} x_j f_{S_2}(x)]]
    = \mathbb{E}_{x_i}[x_i\mathbb{E}_{x|x_i}[\prod_{j \in S_1 - \{i\}} x_j f_{S_2}(x)]]
$$

The inner expectation equals $$c$$, for some constant $$c$$ that doesn't depend
on $$x_i$$. Thus the expectation
$$\mathbb{E}_{x_i}[x_i\mathbb{E}_{x|x_i}[\prod_{j \in S_1 - \{i\}} x_j f_{S_2}(x)]]$$ is

$$
    \frac{1}{2}\cdot c + \frac{1}{2} \cdot -c = 0
$$

Thus, the set is orthonormal. Any orthonormal set is linearly independent.
(The proof is easy to find, if you don't see why.) This leaves showing
they form a basis. For this, note that there's an isomorphism between functions
$$f: \{-1, +1\}^n \to \mathbb{R}$$ and vectors in $$\mathbb{R}^{2^n}$$, where
the mapping is

$$
    f \mapsto \begin{bmatrix}
        f(0) \\
        f(1) \\
        \cdots \\
        f(2^n - 1)
    \end{bmatrix}
$$
(Implicitly, we expand the decimal number to its binary representation when
evaluating $$f$$,)

Isomorphisms preserve dimensionality, so this shows the function space
must have dimension $$2^n$$. There are $$2^n$$ different subsets, so the
parity functions form a linearly independent set of size $$2^n$$, and therefore
must span the entire space. $$\blacksquare$$

Because the parity functions form an orthonormal basis, any function over $$\{-1, +1\}^n$$
can be decomposed into a sum of parity functions, where the coefficient comes
from the inner product. Let $$P(n)$$ be the set of all subsets of $$1$$ to $$n$$.
Then

$$
    f(x) = \sum_{S \in P(n)} \langle f, f_S \rangle f_S(x)
$$

At this point, we draw a comparison to Fourier series. Any periodic
signal $$s(t)$$ can be decomposed into a sum of sinusoids, because the sinusoids
$${1, \sin(t), \cos(t), \sin(2t), \cos(2t), \ldots \}$$ form an
orthonormal basis. Intuitively, the earlier terms represent low-frequency
components of the signal, and the later terms represent high-frequency
components. To reconstruct $$s(t)$$ exactly, we should do

$$
    s(t) = a_0 + \sum{n=1}^\infty a_n \sin(nx) + \sum_{n=1}^\infty b_n \cos(nx)
$$

However, we can approximate the signal by truncating the sum at some maximum $$N$$

$$
    s(t) \approx a_0 + \sum{n=1}^N a_n \sin(nx) + \sum_{n=1}^N b_n \cos(nx)
$$

This corresponds to dropping all the high frequency terms. If our signal
is reasonably structured, this should still be a pretty good approximation.

Now, apply the same motivation to modeling $$f(x)$$ as a sum of parity functions.
We assume that $$f(x)$$ is reasonably structured, and can be modeled well by
only the terms of degree at most $$d$$.

$$
    f(x) \approx \sum_{S \in P(n): |S| \le d} \langle f, f_S \rangle f_S(x)
$$

This reduces the number of terms from $$2^n$$ to $$O(n^d)$$, turning an exponentially
big problem into a polynomially big one.

We further assume that we can still model well if we require the representation
to be sparse, meaning at most $$s$$ coefficients can be nonzero. (EXPLANATION
WHY HERE)


Polynomial Recovery Algorithm
-------------------------------------------------------------------------------

Let's assume we have evaluations of $$f$$ at $$T$$ different points $$x_i$$.
We want to fit a sparse polynomial to these points. The main intuition
here is that we can view it as a giant linear regression problem. We have
a vector of values

$$
    y = \begin{bmatrix}
        f(x_1) \\
        f(x_2) \\
        \vdots \\
        f(x_T)
    \end{bmatrix}
$$

And input features

$$
    x_S = \begin{bmatrix}
        f_S(x_1) \\
        f_S(x_2) \\
        \vdots \\
        f_S(x_T)
    \end{bmatrix}
$$

And you're trying to find coefficient $$\alpha_S$$ to minimize

$$
    \|y - \sum_{|S| \le d} \alpha_S x_S\|_2
$$
