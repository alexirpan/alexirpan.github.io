---
layout: post
title:  "Primes, Riemann Zeta, and Pi, Oh My!"
date:   2016-03-22 15:36:00 -0700
---

I've been working on other posts, but they've been harder
to write than expected. A quick recreational math post should help
fill the gap.

I'm targeting this towards
the high school math contest audience. That means I won't assume anything
past calculus, but I will assume many things up to calculus, and I
also assume people reading this will look up unfamiliar terms on their own.


Relatively Prime Random Numbers
---------------------------------------------------------------------

Let $$a$$ and $$b$$ be two uniformly random natural numbers.
What is the probability $$a$$ and $$b$$ are relatively prime?

First off, this problem isn't well formed. You can't define a
uniform distribution over the naturals, because such a distribution
would break probability theory axioms.
(See [here](http://math.stackexchange.com/questions/997173/can-you-pick-a-random-natural-number-and-a-random-real-number)
if curious.)
To make this formal, we should really be picking naturals
$$a,b$$ uniformly from $$1$$ to $$N$$, and ask what the
probability converges to as $$N$$ approaches $$\infty$$.

> Let $$P(n)$$ be the probability that two uniformly random
> natural numbers from $$1$$ to $$n$$ (inclusive) are relatively prime.
> What is $$P(\infty) = \lim_{n\to\infty} P(n)$$?

This was first solved by Dirichlet in 1849.
For this proof, I'm handwaving the limit and assuming that random natural numbers
act according to intuition.

Two numbers $$a,b$$ are relatively prime if they share
no common factors. This is true if and only if for every prime $$p$$,
$$a$$ and $$b$$ are not both divisible by $$p$$.

Since we pick uniformly at random, the probability $$p$$ divides
a random natural number is $$1/p$$. The probabillity both
numbers are divisible by $$p$$ is $$1/p^2$$, giving

$$
    P(\infty) = \left(1 - \frac{1}{2^2}\right)
                \left(1 - \frac{1}{3^2}\right)
                \left(1 - \frac{1}{5^2}\right)\cdots
              = \prod_{p\text{ prime}} \left(1 - \frac{1}{p^2}\right)
$$

Now, here's where you apply a neat trick. Take the reciprocal
of both sides.

$$
    \frac{1}{P(\infty)}
    = \frac{1}{1 - \frac{1}{2^2}}\cdot
      \frac{1}{1 - \frac{1}{3^2}}\cdot
      \frac{1}{1 - \frac{1}{5^2}}\cdots
$$

For each fraction, substitute the infinite series $$\frac{1}{1-r} = 1 + r + r^2 + \cdots$$.

$$
    \frac{1}{P(\infty)}
    = \prod_{p\text{ prime}} \left(
        1 + \frac{1}{p^2} + \frac{1}{p^4} + \frac{1}{p^6} + \cdots
    \right)
$$

I claim the right hand side is the same as

$$
    \sum_{n=1}^\infty \frac{1}{n^2}
$$

The argument follows from a clever factoring argument.
Suppose we expanded out the product of the infinite series.
We would get infinitely many terms, where each term is generated
by choosing one term from every infinite series and multiplying them together.
For example, take $$1/2^2$$ from the $$p = 2$$ series,
$$1/3^2$$ from the $$p = 3$$ series, and $$1$$ from the rest.
The term obtained is

$$
    \frac{1}{2^2\cdot 3^2} = \frac{1}{6^2}
$$

Now, take $$1/2^4$$ from the $$2$$ series,
$$1$$ from the $$3$$ series, $$1/5^2$$ from the $$5$$ series, and
$$1$$ from the rest. That gives

$$
    \frac{1}{2^4 \cdot 5^2} = \frac{1}{(2^2 \cdot 5)^2} = \frac{1}{20^2}
$$

We can pick terms such that they multiply to $$1/n^2$$ for any $$n$$.
For every prime
$$p_i$$, find the largest power $$p_i^{k_i}$$ that divides $$n$$.
($$k_i$$ could be $$0$$.) Then,
take $$1/p^{2k_i}$$ from the $$p_i$$ series.
By prime factorization, the product is

$$
    \prod_{p\text{ prime}} \frac{1}{p^{2k_i}} = \frac{1}{\left(\prod_{p\text{ prime}} p^{k_i}\right)^2} = \frac{1}{n^2}
$$

Every natural number has a unique prime factorization, so every
$$n$$ is generated once and exactly once.
Thus, the product expands to the sum of the reciprocal of the squares

$$
    \prod_{p\text{ prime}} \left(
        1 + \frac{1}{p^2} + \frac{1}{p^4} + \frac{1}{p^6} + \cdots
    \right)
    = \sum_{n=1}^\infty \frac{1}{n^2}
$$

(If you're like me, you may want to spend a moment admiring this argument.
It's a contender for my favorite proof ever.)

The final expression is

$$
    \frac{1}{P(\infty)} = \sum_{n=1}^\infty \frac{1}{n^2}
$$

Substituting

$$
    \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

gives that the probability is $$6/\pi^2 \approx 0.608$$.


Riemann Zeta And More Handwaving
-------------------------------------------------------------------------------

Now, unless you've seen it before, it should not be clear why

$$
    \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

This was first proved by Euler in 1734. His proof was a bit sketchy, and
it took another 7 years to make it rigorous.
Nevertheless, I'm presenting the sketchy proof.

To prove this result, we're going to start from something completely
different: the Taylor series for
$$\sin(x)$$. For all $$x$$,

$$
    \sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
$$

Divide through by $$x$$ to get

$$
    \frac{\sin(x)}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \cdots
$$

(If you don't know what Taylor series are, take this on faith. I don't
want to do calculus.)

The idea Euler used was to treat $$\frac{\sin(x)}{x}$$ as an infinite degree polynomial.
Any polynomial $$p(x)$$ with roots $$r_1,\ldots, r_n$$ can be written as

$$
    p(x) = a(x-r_1)(x-r_2)\cdots(x-r_n)
$$

where $$a$$ is some constant. For this proof, we're using a different
form. Divide each term by $$-r_i$$ to get

$$
    p\left(x\right) = a'\left(1 - \frac{x}{r_1}\right)\left(1 - \frac{x}{r_2}\right)\cdots\left(1-\frac{x}{r_n}\right)
$$

where $$a'$$ is some other constant.
Assuming this works for functions with infinitely many roots,
$$\frac{\sin(x)}{x} = 0$$ at $$x = \pm \pi, \pm 2\pi, \pm 3\pi, \ldots$$.

$$
    \frac{\sin(x)}{x} = a'\left(1-\frac{x}{\pi}\right)\left(1+\frac{x}{\pi}\right)\left(1-\frac{x}{2\pi}\right)\left(1+\frac{x}{2\pi}\right)\cdots
$$

Equate this with the Taylor series. To make the constant term match up,
we must have $$a' = 1$$.
(Try converting to the $$a(x-r_1)(x-r_2)\cdots$$ form and
you'll see why it's sketchy to assume $$\sin$$ acts like an
infinite degree polynomial.)

Group up the terms for roots $$k\pi$$ and $$-k\pi$$ to get

$$
    \frac{\sin(x)}{x} = \left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{4\pi^2}\right)\left(1-\frac{x^2}{9\pi^2}\right)\cdots
$$

Now, compare the coefficient of $$x^2$$.
To get an $$x^2$$ term, we have to choose $$x^2/(n^2\pi^2)$$
exactly once, and choose $$1$$ from the rest. This gives

$$
    -\frac{1}{3!}x^2 = \sum_{n=1}^\infty -\frac{x^2}{n^2\pi^2}
$$

Which gives the final answer of

$$
   \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

This sum of reciprocals is a special case of the [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function),
defined as

$$
    \zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}
$$

It turns out that analyzing this function for complex $$s$$ has deep connections
to the primes. I can't explain why because I don't know analytic
number theory, but if you consider that we started from relatively
prime numbers and got to here, I don't think a connection is too strange.


$$\pi$$ By Prime Products
---------------------------------------------------------------------------

I'll close with a fun identity that relates the prime numbers to $$\pi$$.
This identity was also discovered by Euler.

Every odd prime $$p$$ is either $$1 \text{ mod } 4$$ or $$3 \text{ mod } 4$$.
Take the negative reciprocal if it's $$1 \text{ mod } 4$$ and the positive
reciprocal if it's $$3 \text{ mod } 4$$. Add $$1$$, take the product over
all odd primes, and you get the identity

$$
    \frac{4}{\pi} = \left(1+\frac{1}{3}\right)\left(1-\frac{1}{5}\right)\left(1+\frac{1}{7}\right)\left(1+\frac{1}{11}\right)\left(1 - \frac{1}{13}\right)\cdots
$$

The proof borrows from both previous
sections. First, take the reciprocal.

$$
    \frac{1}{1+\frac{1}{3}}\cdot
                    \frac{1}{1-\frac{1}{5}}\cdot
                    \frac{1}{1+\frac{1}{7}}\cdot
                    \frac{1}{1+\frac{1}{11}}\cdot
                    \frac{1}{1-\frac{1}{13}}\cdots
$$

Replace each term with an infinite series

$$
    \prod_{p \equiv 1 \text{ mod }4} \left(1 +\frac{1}{p} + \frac{1}{p^2}+\cdots\right)
    \prod_{p \equiv 3 \text{ mod }4} \left(1 - \frac{1}{p} + \frac{1}{p^2}-\cdots\right)
$$

And again, expand out the infinite product. Ignoring the signs, this is
exactly the same as the product for relatively prime random numbers, except
without an infinite series for $$2$$. When expanded, we'll get exactly
one term for every odd number.

(I love this factoring trick so much. It's great, even if it's difficult
to apply on other problems.)

Now, consider the signs of those terms. Term $$1/n$$ is positive if and
only if
$$n$$ is the product of an even number of (not necessarily distinct) $$3\text{ mod } 4$$ primes.
If you multiply an even number of $$3\text{ mod }4$$ primes, you
get a number that's $$1 \text{ mod } 4$$. If you multiply
an odd number of those primes, you'll get a $$3 \text{ mod } 4$$ number.

So, the sign is negative at every other odd number, giving an expansion
of

$$
    1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots
$$

which - surprise - is [Leibniz's formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
for $$\pi$$. (It follows from the Taylor series for $$\arctan$$ evaluated at $$1$$.)

$$
    \frac{\pi}{4} =
    \frac{1}{1+\frac{1}{3}}\cdot
                    \frac{1}{1-\frac{1}{5}}\cdot
                    \frac{1}{1+\frac{1}{7}}\cdot
                    \frac{1}{1+\frac{1}{11}}\cdot
                    \frac{1}{1-\frac{1}{13}}\cdots
$$

$$
    \Rightarrow
$$

$$
    \frac{4}{\pi} = \left(1+\frac{1}{3}\right)\left(1-\frac{1}{5}\right)\left(1+\frac{1}{7}\right)\left(1+\frac{1}{11}\right)\left(1 - \frac{1}{13}\right)\cdots
$$


Oh My! That's All, Folks!
-------------------------------------------------------------------------------

That's all I've got. See you next time, for something less mathy.
