---
layout: post
title:  "Read-through: Hyperparameter Optimization: A Spectral Approach"
date:   2017-06-18 00:52:00 -0700
---

Similar to Wasserstein GAN, this is another theory-motivated paper with neat
applications to deep learning. Once again, if you are looking for details on
all the proofs, you are better off reading the original paper. The goal
of this post is to give background and motivation for the approach.


Why Is This Paper Important?
----------------------------------------------------------------------

For one, I really don't like doing hyperparam optimization. It has to be done,
but that doesn't mean I have to like it. So, I like to keep an eye on
hyperparam optimization papers. Even if I never have the time to implement
them, they're usually fun to think about - you get a lot of interesting problems
when point queries take hours or days to compute. It's like a version of the
robotics problem - real world robot data is ridiculously expensive to generate.

Additionally, there's been a growing trend towards metalearning recently. The
Neural Architecture Search paper made a big splash, and although we aren't at
the point where meta-learned models always outperform hand-tuned models, it's
looking more likely.


Some Quick Background on Hyperparam Optimization
---------------------------------------------------------------------

For two approachable introductions to the subject, I highly recommend two blog
posts from Ben Recht's blog, linked [here](http://www.argmin.net/2016/06/20/hypertuning/)
and [here](http://www.argmin.net/2016/06/23/hyperband/). The key takeaways are

* Random search is a simple, deceptively strong baseline.
* Bayesian optimization (i.e. fitting a Gaussian mixture model)
can outperform random search by a bit.
* However, Random Search run twice as fast beats a lot of Bayesian optimization
methods. Yes, it's more compute time, but sometimes buying more machines is
easier than implementing clever ideas.
* Successive halving (SH) is a nice extension of random search that lets you try
many more hyperparams in the same amount of time. It does this by pruning
runs that have poor performance early on. You have to be a little careful with
how aggressively you prune, but in practice it's pretty easy to beat Random
Search.
SH was later extended to the
Hyperband algorithm, described [here](https://arxiv.org/abs/1603.06560).


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
* For every $$f_i, f_j$$ where $$i \neq j$$, $$\langle f_i, f_j \rangle = 0$$.

Now, we show the parity functions have this property.

* By defintion, $$\langle f_i, f_i \rangle = \mathbb{E}[f_i(x)^2]$$. Note
that $$f_i(x) = -1$$ or $$f_i(x) = 1$$, depending on how many bits of $$x$$
match. In either case, $$f_i(x)^2 = 1$$ for all $$x$$, $$\langle f_i, f_i \rangle = 1$$.
* For any two different subsets $$S_1, S_2$$, there exists some $$i$$ in one,
but not the other. Without loss of generality, let $$i \in S_1$$ and $$i \notin S_2$$.
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
$$\{1, \sin(t), \cos(t), \sin(2t), \cos(2t), \ldots \}$$ form an
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
We want to fit a sparse polynomial to these points. The main trick is a classic:
fitting a sparse low-degree polynomial is the same as fitting a sparse linear
regression problem in a larger space. We have a dataset of values

$$
    \{y_1,y_2,\ldots y_n\} = \{ f(x_1), f(x_2), \ldots, f(x_n) \}
$$

There are $$O(n^d)$$ features, one for each subset $$S$$ with $$|S| \le d$$.
We want to find $$\alpha_S$$ that minimizes

$$
    \sum_{i=1}^T (y_i - \sum_{|S| \le d} \alpha_S f_S(x_i))^2
$$

We also want to have the solution be sparse, which once again has a classical
solution - add L1 regularization.

$$
    \min_{\alpha_S} \lambda * \|\alpha\|_1 + \sum_{i=1}^T (f(x_i) - \sum_{|S| \le d} \alpha_S f_S(x_i))^2
$$

This gives the main subroutine, called Polynomial Sparse Recovery.

![PSR algorithm](/public/hyperparam-spectral/psr.png)
{: .centered }

When called, it returns a sparse polynomial, and all variables that are used
in the sparse polynomial.


Runtime Bound For Subalgorithm
----------------------------------------------------------------------------

To be honest, I only skimmed the proof for the runtime bound. It looks like a
mix of Chebyshev's inequality, Parseval's identity, clever rearrangement,
prior work on sparse recovery.

More relevantly, here is the theorem statement.

> Let $$f$$ be an $$(\epsilon, d, s)$$-bounded function. Let $$\{H_S\}$$ be
> an orthonormal polynomial basis bounded by $$K$$. Then the PSR algorithm
> finds a $$g$$ that's within $$\epsilon$$ of $$f$$ in time $$O(n^d)$$ with
> sample complexity $$T = \tilde{O}(K^2s^2 \log N/\epsilon)$$.

In this statement, $$N$$ is the size of the polynomial basis. For the special
case of parity functions, we have $$K = 1$$ and $$N = O(n^d)$$, requiring
$$T = \tilde{O}(s^2 d \log n / \epsilon)$$.


Harmonica: The Full Algorithm
----------------------------------------------------------------------------

The full algorithm runs the polynomial sparse recovery algorithm in stages.
At each stage, sample some values $$f(x_i)$$ by training some models, then
fit a sparse polynomial $$g$$.

Let's suppose $$f$$ represents the error %, and we want it to be as low as
possible. Given $$g$$, it's straightforward to find the settings that minimize
it, because $$g$$ is sparse and low-degree. Note that there are at most
$$sd$$ different variables $$x_i$$ can appear in $$g(x_1,x_2,\ldots,x_n)$$,
because each parity function contributes at most $$d$$ variables and $$g$$
is the sum of $$s$$ of these. So we can simply brute-force assignments
to all $$2^{sd}$$ assignments if we have to - note that $$(2^s)^d$$ should
be heavily dwarfed by the $$O(Tn^d)$$ time it takes to get $$g$$, for an
appropriate sparsity choice $$s$$.

Note, however, that this only gives settings for the variables that $$g$$
depends on. This doesn't cover all the hyperparams. So, we apply the
algorithm in stages. At each stage, we use the sparse polynomial to get
settings for some of the hyperparams, freeze those, then apply the algorithm
to get settings for the remaining hyperparams. After enough stages, the
hyperparam space is small enough that we can use a baseline hyperparam
search algorithm. Random search, successive halving, Hyperband, whatever.

(Empirically, it looks like the authors found that freezing the hyperparam
setting from the first stages was too aggressive. Instead, the proposed
algorithm says to find the $$t$$ settings that minimize $$g$$, and to sample
the setting from those $$t$$ in future stages. For example, say we have 30
hyperparams, and at stage 1 we retrieved a $$g(x)$$ that depends on 10 of
those hyperparams. With $$t = 4$$, when optimizing over the 20 remaining
hyperparams, instead of having only 1 setting for the 10 hyperparams seen
before, we sample one of the four.)

![Harmonica algorithm](/public/hyperparam-spectral/harmonica.png)
{: .centered }


Experiments
----------------------------------------------------------------------------

The problem used is Cifar-10, trained with a deep Resnet model. The model
has 39 hyperparams, deciding everything from learning rate to L2 regularization
to connectivity of the network, batch size, and non-linearity. Then, to make
the problem more difficult, 21 dummy hyperparams are added, giving 60 hyperparams
total. All hyperparams are binary, but some variables span multiple hyperparams.
For example, there are 8 learning rate options, which are decided by 3 binary
hyperparams.

Harmonica is evaluated with 300 samples at each stage (meaning 300 trained models),
with maximum degree $$d = 3$$, sparsity $$s=5$$, and restriction size $$t=4$$.
PSR is done for 2 stages, then successive halving is used for the final
hyperparam optimization.

Importantly, the full model is a 56 layer ResNet. In the first two stages,
Harmonica is run on a smaller 8 layer network, and the full network is only trained
in the final stage. The argument is that hyperparams
tend to have a consistent effect as you make the model deeper, so tuning
on a small network still gives you good settings for the full size network.
It's unclear whether a similar trick was used in the methods they compared against.
I assume they weren't, for pessimism's sake.


Results Summary
------------------------------------------------------------------------------

Harmonica outperforms random search, Hyperband (extension of successive halving),
and Spearmint (a Bayesian optimization approach.)

![Test error](/public/hyperparam-spectral/results1.png)
{: .centered }

In this plot, the different between Harmonica 1 and Harmonica 2 is that in Harmonica 2,
the final stage is given less time.

In terms of runtime, the fastest version (Harmonica 2) runs 5x faster than Random
Search and outperforms it. The slower version (Harmonica 1) is still competitive
with other approaches in runtime while giving much better results.

![Run time](/public/hyperparam-spectral/results2.png)
{: .centered }

As Harmonica discovers settings for the important hyperparams, the average test
error in the restricted hyperparam space drops. Each stage gives another drop in
performance.

![Average test error](/public/hyperparam-spectral/results3.png)
{: .centered }

As a side effect of the sparse recovery, we get weights on which features (which
hyperparams) are most important. Results are shown for a 3-stage Harmonica
experiment, where sparsity $$s = 8$$ for the first 2 stages and $$s = 5$$ for the
3rd stage.

![Table of important hyperparams](/public/hyperparam-spectral/results4.png)
{: .centered }

Many of the important hyperparams line up with convention - batch norm should be
one, the activation function should be ReLU, and Adam is a better optimizer than
SGD. Check the original paper for definitions of the hyperparams listed here.

