---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

One day, I was training a model with a reinforcement learning.
(NAF, to be specific.) Someone recommended I tried batch norm, because
it was key to making some of the models train. I implemented it, but I
still couldn't reproduce the results.

A few days later, I figured out the issue. Batch norm was the culprit.

\*\*\*
{: .centered }

Another day, somebody came to me with a very, very strange bug.
Their model was working fine at training time, slowly increasing in
accuracy. When evaluated on a batch of data, the accuracy was still good.
But when evaluated on a single example, it failed completely.

This sounded suspiciously like a batch norm issue, but I had no idea how
it could have happened.
After several hours of digging in the code, we found it was indeed
a batch norm issue.

\*\*\*
{: .centered }

That same day (and I mean literally that same day), I was discussing the
recent issues I was having with my own project. I had branched from a
working model to implement a domain adaptation technique, and was running
regression tests to verify I didn't make a bug in the port. I used exactly
the same data, with exactly the same loss, and exactly the same hyperparameters,
*so why was my code 5% worse in performance?*

It is very lucky I was dealing with batch norm issues earlier that day, because
if I hadn't, it would have taken me much longer to figure out it was Yet
Another Batch Norm Issue.


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

Earlier, I mentioned that batch norm is a leaky abstraction. To solve bugs
caused by leaky abstractions, you have to pierce the abstraction barrier. Thus,
to explain my batch norm bugs, I first have to explain batch norm. Feel free
to jump to the next section if this is review.

Let's suppose we're training a neural network on some data. For the sake of the
example, let's say it's a 1 hidden layer network. Letting $$\sigma$$
be the nonlinearity, we have something like this.

$$
    F(x) = f_2(f_1(x))
$$

where $$f_1(x) = \sigma(W_1x + b_1)$$ and $$f_2(x) = \sigma(W_2x + b_2)$$.

IMAGE

Now, consider a single output unit in one of the layers.

IMAGE

Like all of machine learning, we assume input data follows some distribution
$$D$$. The output of each layer is itself going to follow some distribution,
which is defined by $$D$$ and the weights and biases for that layer. For
conveincence, letl $$f_1(D)$$ be the distribution of the 1st layer's activations.

Now, during the training process, each layer is going have its own job.
The 1st layer is trying to learn good features from the input. The 2nd layer's
job is to learn good features from the 1st layer's output. The 3rd layer learns
from the 2nd layer, the 4th from the 3rd, and so on down, with the final layer
learning how to solve the desired task. Then, through the magic of backprop,
we can update everything appropriately. Easy, right?

However, as the weights change, the distribution of each layer's activations
will follow suit. This makes the next layer's job harder, because the distribution
it's learning from keeps changing underneath it. (The paper calls this
the covariate shift problem.)

Wouldn't it be nice if we could keep the distribution fixed during training?
That way, layers in the network wouldn't need to compensate for the shift in
distribution for their inputs.

This is the problem batch norm addresses. We can't keep the distribution
entirely fixed, but we can reduce the covariate shift, by normalizing the
output to always be mean $$0$$, variance $$1$$. (More formally, we restrict
only the 1st and 2nd moment, instead of the entire distribution.)

(As a side effect, normalizing the outputs can help stop exploding or
vanishing gradients, but the covariate shift is the main motivation.)

So, how do we make sure the output is always mean $$0$$, variance $$1$$?
At training time, we train the network on batches of data (say 32 inputs at
a time for the sake of an exmaple.) For each output unit, we can compute the
mean and variance over this batch, which lets us normalize exactly.

EQUATIONS HERE?

However, at test time, we want to run the network on single examples at a time.
To ensure consistent evaluation, when we compute the mean and variance above,
we also update a moving average of the means and variance of each batch.
When the network has converged, the moving average should have converged
to the average mean and variance over the entire dataset. We then normalize
with the moving average, instead of the true mean and variance.


What Exactly Went Wrong?
-----------------------------------------------------------------------------

> One day, I was training a model with a reinforcement learning.
> Someone recommended I tried batch norm, but but I
> still couldn't reproduce the results.

I eventually discovered that when computing actions to take, my model
was running in train mode. Because I was feeding a batch of size 1 (the last
state from the environment), batch norm forced the input to always be all
zeroes. I never needed to change to test mode in the middle of training before,
but batch norm makes the train mode eval differ from the test mode eval.

> Another day, somebody came to me with a very, very strange bug.
> Their model was working fine at training time, slowly increasing in
> accuracy. When evaluated on a batch of data, the accuracy was still good.
> But when evaluated on a single example, it failed completely.

In this model, we loaded a pretrained network, froze all its weights, then
added extra layers and trained just the new layers on the new task.
It turned out we had accidentally loaded the pretrained network in train
mode. This was fine before, because we had made extra sure that all variables
in that network were not trainable, but not anymore. To fix it, we
ended up having to make extra sure that the model was loaded in test mode,
with moving average updates disabled for layers we wanted to freeze.


> I had branched from a working model to implement a domain adaptation
> technique, and was running regression tests to verify I didn't make a bug in
> the port. I used exactly the same data, with exactly the same loss, and
> exactly the same hyperparameters,
> *so why was my code 5% worse in performance?*

In this setup, I was training a model on two datasets. In one implementation,
I sampled one batch from each dataset, and merged them into one big one.

IMAGE

In the second, I had two copies of the network, with shared weights between
them, feeding one batch to each copy.

IMAGE

In both approaches, we're feeding a mixture of
In both approaches, we feed in the same data, and we have the same loss,
and we run the same optimization function, and we use the same hyperparams.
*So why is one 5% better than the other?*

