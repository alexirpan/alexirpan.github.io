---
layout: post
title:  "A Langrange Multipliers Refresher, For Idiots Like Me"
date:   2019-07-11 23:58:00 -0700
---


What Are Lagrange Multipliers?
-----------------------------------------------------------------------

Lagrange multipliers are a tool for doing constrained optimization. Say we
are trying to minimize a function $$f(x)$$,
subject to the constraint $$g(x) = c$$.

$$
\begin{aligned}
\min &\, f(x) \\
\text{subject to} &\, g(x) = c
\end{aligned}
$$

To solve this, you define a new function

$$
    \mathcal{L}(x, \lambda) = f(x) - \lambda (g(x) -c)
$$

then find a stationary point of this function (a point where the partial
derivative in $$x$$ and $$\lambda$$ is zero).

This is all true, but it doesn't explain why this works.


Why Do Lagrange Multipliers Work?
------------------------------------------------------------------------

Let's consider a more general version of the problem. We want to minimize
$$f(x)$$ subject to $$g(x) \ge 0$$.

$$
\begin{aligned}
\min &\, f(x) \\
\text{subject to} &\, g(x) \ge 0
\end{aligned}
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
\begin{aligned}
\min &\, f(x) \\
\text{subject to} &\, g_1(x) \ge 0 \\
&\, g_2(x) \ge 0
\end{aligned}
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
constraint $$g(x) - c \ge 0$$,

$$
\begin{aligned}
\min &\, f(x) \\
\text{subject to} &\, g(x) - c \ge 0
\end{aligned}
$$

which is solved the same was as before.

$$
    \min_x \max_{\lambda \ge 0} f(x) - \lambda (g(x) - c)
$$

If we have a constraint $$g(x) \le 0$$, we can negate both sides to get $$-g(x) \ge 0$$.
If we have a constraint $$g(x) \le c$$, we can rearrange it to $$c - g(x) \ge 0$$.
This reduces everything to the $$g(x) \ge 0$$ case we know how to solve.

Bringing it back to the equality case, let's say we have a constraint $$g(x) = c$$.
How do we reduce this to the previous cases? This equality is the same as
the pair of constraints $$g(x) \ge c, g(x) \le c$$, which are only both
satisfied at $$g(x) = c$$. This time, I'll write
the Lagrange multipliers as $$\lambda_+$$ and $$\lambda_-$$

$$
\begin{aligned}
\min &\, f(x) \\
\text{subject to} &\, g(x) \ge c \\
\text{subject to} &\, g(x) \le c
\end{aligned}
$$

$$
    \min_x \max_{\lambda_+, \lambda_- \ge 0} f(x) - \lambda_+ (g(x) - c) - \lambda_- (c - g(x))
$$

Like before, if we ever have $$g(x) \neq c$$, then we can choose a $$\lambda_+, \lambda_-$$ such
that the objective value shoots up to $$-\infty$$. But, since $$g(x) - c$$ and $$c - g(x)$$
are just negations of each other, we can simplify this further.

$$
    \min_x \max_{\lambda_+, \lambda_- \ge 0} f(x) - (\lambda_+ - \lambda_-) (g(x) - c)
$$

It's possible to make $$\lambda_+ - \lambda_-$$ equal
any real number while still satisfying $$\lambda_+ \ge 0, \lambda_- \ge 0$$, so
let's just replace it with $$\lambda = \lambda_+ - \lambda_-$$, and let
$$\lambda$$ be any real number instead of just nonnegative ones.

$$
    \min_x \max_{\lambda} f(x) - \lambda (g(x) - c)
$$

And now, we're back where we started, where the solution to this must lie at a
saddle point where the gradient with respect to $$x$$ and $$\lambda$$ is 0.


Why Do I Like This Explanation?
-------------------------------------------------------------------------------

When I was relearning Lagrange multpliers a while back, I was upset that all
the most populare results were targeted towards people taking their first
multivariate calculus course. These explanations exclusively covered the
$$g(x) = c$$ case, and the constraints I wanted to add were more like
$$a \le g(x) \le b$$.

It's a shame that most people's first introduction to Lagrange multipliers is
just the equality case, because inequality constraints are more general, and
the concepts needed to understand that case aren't much harder.

The fact that you can turn unconstrained optimization into constrained
optimization doesn't tell you anything about how to solve these problems. But
like all other min-max problems (GANs, actor-critic RL, etc.), doing
alternating gradient descent updates on $$x$$ then $$\lambda$$ seems
to work out fine. This procedure doesn't guarantee that your constraint
$$a \le g(x) \le b$$ is met over the entire optimization process, but it
does quickly penalize the optimization for violating the constraint, since
the $$\lambda$$ for that constraint will quickly rise and keep rising until
the constraint is satisfied again.

There is one final detail. To handle inequalities, we require optimization
over $$\lambda \ge 0$$. The common trick is to rewrite $$\lambda$$
as $$\lambda = \exp(w)$$ or $$\lambda = \text{softplus}(w)$$, then do gradient
descent over variable $$w$$ instead.
