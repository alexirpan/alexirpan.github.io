---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

One day, I was training a model with a reinforcement learning.
(NAF, to be specific.) Someone recommended I tried batch norm, because
it was key to making some of the models train. I implemented it, but I
still couldn't reproduce the results.

A few days later, I figured out the issue: when running the policy in
the environment, my model was running in train mode instead of test mode.
With batch norm, that made the whole thing fail.

\*\*\*
{: .centered }

Another day, somebody came to me with a very, very strange bug.
Their model was working fine at training time, slowly increasing in
accuracy. When evaluated on a batch of data, the accuracy was still good.
But when evaluated on a single example, it failed completely.

This sounded suspiciously like a batch norm issue, but I had no idea how
it could have happened, because I'd been using similar code without issue.
After several hours of digging in the code, we found out half of his
model was running in train mode, and half was running in test mode.

\*\*\*
{: .centered }

That same day (and I mean literally that same day), I was discussing the
recent issues I was having with my model. I was training a model on
two datasets at once. In one implementation, I merged the two datasets
into one big one. In another implementation, I had two copies of the
same network, with shared weights, and fed one dataset into each.

IMAGE

In both approaches, we feed in the same data, and we have the same loss,
and we run the same optimization function, and we use the same hyperparams.
*So why is one 5% better than the other?*

If you guessed that batch norm was the issue, congratulations. It's almost
lucky I had to deal with batch norm earlier that day, because if I hadn't
dealt with that bug, I would have been suck for way longer.


Batch Norm: The Cause of, And Solution To, All of Life's Problems
------------------------------------------------------------------------

By now, you may have noticed a pattern.

On the one hand, all of these problems were my fault. If I had been more careful,
none of these issues would have happened. So perhaps you could chalk this up
to inexperience.

On the other hand, these issues all happened because batch norm forces you to
keep track of things you normally don't need to care about. Suddenly, your model
runs different computation between train time and test time. Suddenly, you have
to care about what kind of data is given in each minibatch, because entries in
the batch are no longer independent. Yes, you can treat batch norm as black box
normalization magic, but in practice, [the abstraction leaks](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/),
like all abstractions do. In batch norm's case, the abstraction leaks in ways
that other optimization tricks don't, and it places more cognitive load on the
researcher to keep track of everything.

In short, it was all my fault, but batch norm sure made it easier to make those
mistakes in the first place.

That said, when it works, my models definitely train a lot faster with batch norm.
Like, a lot faster. No contest.

It's almost like a Faustian bargain. I'll give you 2x faster training, in exchange
for increasing your chances of hitting some incredibly obtuse bug that'll plague
you for days. And I keep signing it, like a sucker. And so do other people.
If they didn't, it wouldn't have gotten over 1000 citations.


What is Batch Norm?
--------------------------------------------------------------------------------

Earlier, I mentioned that batch norm is a leaky abstraction. To understand
batch norm issues, and to avoid them in the future, it's important to know what
batch norm is doing. (Feel free to skip this section if you're comfortable
with batch norm.)

Let's suppose we're training a neural network on some data. Like all of machine
learning, this is formalized by saying we have some data distribution $$D$$.

IMAGE

Now, consider a single output unit in one of the layers.

IMAGE

This unit's output is some linear combination of its inputs. **The unit's output
is itself going to follow some distribution, which depends on the weights of
the network at the current point in time.** If it helps, think of $$f(x)$$ as the
computation that feeds into this unit. Because data $$x$$ follows distribution
$$D$$, the unit's output is a distribution $$f(D)$$.

Now, during the training process, that distribution $$f(D)$$ is going to change,
just because of updates to the model. The next layer in the network has to
learn to effectivelt use this output unit, and that's more difficult if the
distribution is continually shifting. (DOUBLE CHECK: covariate shift?)

The goal of batch norm is to normalize the output distribution to always be mean
0, variance 1. This has two benefits.

* By constraining the distribution, we make it easier for the next layer to learn
how to use this layer's features.
* By normalizing the scale, we stop activations from growing too large or too
small, which helps prevent exploding or vanishing gradients.

This leaves implementing the normalization.
When training neural nets, we feed small batches (minibatches) of data at a time.
To make this example concrete, let's say our batch size is 32. We compute the
average within the batch, the variance within the batch, then normalize all the
outputs based on the batch average. This ensures the network is trained with
exactly a mean 0 variance 1 distribution.

However, at evaluation time, it's impractical to eval on a batch of data,
since we often want models to be evaluated on single examples at a time. So,
we keep a running average of the minibatch means and variance during the
training process. We use an exponential average (EQUATION HERE): this has
the property of placing more weight on recent data. Recall that over time,
each output unit distribution will change, so we want the moving average
to be computed primarily over the most recent data.


The Problems with Batch Norm
-----------------------------------------------------------------------------

In general, machine learning is harder to debug than traditional software
engineering.

In normal software, when something goes wrong, it most likely means there's
a bug in the code. It may be hard to find that bug, but something's wrong,
and that's that.

In machine learning, when a model doesn't train, there could be a bug in the
code, or you might not have enough data, or your hyperparameters may need
to be tuned more, or your model may be too large or too small. There are
many more dimensions of ways things can go wrong.

Batch norm adds to this, because it adds two unpleasant things to the model.

1. The code path at training time differs from the code path at eval time.
2. The model's behavior at training is batch-dependent, meaning that given
some $$x$$ in the batch, $$f(x)$$ depends on the other entries in the batch.

Together, this opens out an entire new class of problems to keep in mind.

