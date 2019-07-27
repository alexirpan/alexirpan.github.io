---
layout: post
title:  "A Langrange Multipliers Refresher, For Idiots Like Me"
date:   2019-07-11 23:58:00 -0700
---

A while back, I was relearning how Lagrange multipliers worked, and was upset
that all the resources I found online were written for someone taking their
first multivariate calculus course. I wanted an explanation that got to the
point, and couldn't find one, so I decided to write one.


What Are Lagrange Multipliers?
-----------------------------------------------------------------------

Lagrange multipliers are a tool for doing constrained optimization. The common
way they are described is like so. Say we are trying some function $$f(x)$$
subject to the constraint $$g(x) = 0$$.

$$
\min f(x) \breqn
\text{subject to} g(x) = c
$$

To solve this, you define a new function

$$
    \mathcal{L}(x, \lambda) = f(x) - \lambda (g(x) - c)
$$

then find a stationary point of this function (a point where the partial
derivative in $$x$$ and $$\lambda$$ is zero).

This is all true, but it doesn't explain why this works.


Why Do Lagrange MUltipliers Work?
------------------------------------------------------------------------

Let's consider a more general version of the problem. We want to minimize
$$f(x)$$ subject to $$g(x) \ge 0$$.

$$
\min f(x) \breqn
\text{subject to} g(x) \ge 0
$$

Let's define the following min-max optimization problem.

$$
    \min_x \max_{\lambda \ge 0} f(x) - \lambda g(x)
$$

I claim the minimum of this optimization problem occurs at the smallest
$$f(x)$$ that satisfies the constraint $$g(x) \ge 0$$. Why?

Suppose
we are violating the constraint $$g(x) \ge 0$$. Then we have $$g(x) < 0$$.
At such an $$x$$, because $$-\lambda g(x)$$ is positive, the
$$\lambda$$ that maximizes the objective is $$\lambda = \infty$$, and
the objective value at that region would be $$\infty$$.

If we are not violating the constraint, then $$-\lambda g(x) \le 0$$,
and since $$\lambda$$ is constrained to $$\lambda \ge 0$$, the optimal
$$\lambda$$ is $$\lambda = 0$$, and the objective value is $$f(x)$$.

In other worse, the solution of this unconstrained problem is the same
solution as the constrained problem.

This handles the $$g(x) \ge 0$$ case. What if we have multiple constraints?

$$
\min f(x) \breqn
\text{subject to} g_1(x) \ge 0 \breqn
g_2(x) \ge 0
$$

We can define a similar min-max problem by adding a Lagrange multiplier
$$\lambda_i$$ for each constraint $$i$$.

$$
    \min_x \max_{\lambda_1,\lambda_2 \ge 0} f(x) - \lambda_1 g_1(x) - \lambda_2 g_2(x)
$$

By a similar argument, the optimal solution to this min-max problem occurs at
$$\lambda_1 = 0, \lambda_2 = 0$$, and $$x$$ at the solution of the original
constrained optimization problem (assuming it exists).

What if we have a constraint $$g(x) \ge c$$? We can rearrange it to the
constraint $$g(x) - c \ge 0$$, then solve it the same way as before.

$$
\min f(x) \breqn
\text{subject to} g(x) - c \ge 0
$$

$$
    \min_x \max_{\lambda \ge 0} f(x) - \lambda_1 g_1(x) - \lambda (g(x) - c)
$$

If we have a constraint $$g(x) \le 0$$, we can negate both sides to get $$-g(x) \ge 0$$,
and if we have a constraint $$g(x) \le c$$, we can rearrange it to $$c - g(x) \ge 0$$.
I won't write out the equations this time, but essentially we're reducing
each case to constraints of the form $$g(x) \ge 0$$.

Bringing it back to the equality case, let's say we have a constraint $$g(x) = c$$.
How do we reduce this to the previous cases? This equality is the same as
the pair of constraints $$g(x) \ge c, g(x) \le c$$. This time I'll write
the Lagrange multipliers as $$\lambda_+$$ and $$\lambda_-$$

$$
\min f(x) \breqn
\text{subject to} g(x) = c
$$

$$
    \min_x \max_{\lambda_+, \lambda_- \ge 0} f(x) - \lambda_+ (g(x) - c) - \lambda_- (c - g(x))
$$

Like before, if we ever have $$g(x) \neq c$$, then we can choose a $$\lambda_+, \lambda_-$$ such
that the objective value shoots up to $$-\infty$$. But, since $$g(x) - c$$ and $$c - g(x)$$
are just negations of each other, we can simplify this further.
