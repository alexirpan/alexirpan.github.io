---
layout: page
title: A List of Reinforcement Learning Derivations
permalink: /rl-derivations/
---

I keep forgetting how to derive the famous reinforcement learning
results. Here's a place for me to store the proofs.


REINFORCE

Core policy gradient derivation.

Let $$X$$ be a random variable with known p.d.f. $$p_\theta(X)$$.
From here on, $$\theta$$ will be omitted.
Let $$J(\theta)$$ be some cost function defined as

$$
    J(\theta) = \mathbb{E}[f(X)] = \int_x f(x)p(x)\, dx
$$

for some arbitrary function $$f(x)$$. We want to compute
$$\nabla_\theta J(\theta)$$. Using the log derivative trick, we can
change the gradient of the expectation to the expectation of the gradient.

$$
    \nabla_\theta J(\theta) = \int_x f(x) \nabla_\theta p(x) \, dx
    = \int_x f(x) p(x) \nabla_\theta \log(p(x)) p(x) \, dx
    = \int_x f(x
$$
