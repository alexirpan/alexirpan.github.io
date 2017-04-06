---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

One day, I was training a neural network with reinforcement learning.
I was trying to reproduce the results of paper, with lots of difficulty.
Someone recommended I add batch norm, because
it was key to making some of the models train. I implemented it, but I
still couldn't reproduce the results.

A few days later, I found a bug with how I was doing batch norm, and after fixing
it, things started getting better.

\*\*\*
{: .centered }

Another day, somebody came to me with a very, very strange bug.
During training, the classification accuracy was fine. During evaluation, the
accuracy on the validation set was fine. But at inference time, the model
failed completely.

Hmmmmm. Well, that certainly smelled like a batch norm issue. About an hour
later, we finally tracked down the code that used batch norm incorrectly.

\*\*\*
{: .centered }

That same day (and I mean literally that same day), I was discussing
recent issues I was having with my own project.
I had two equivalent implementations of a neural net. I was using exactly
the same data, with exactly the same loss, and exactly the same hyperparameters,
and exactly the same optimizer, same number of GPUs,
*so why was my code 5% worse?*

Guess what? It was batch norm! Luckily, I had been thinking about batch norm
earlier that day. Who knows how long it would have taken me to figure it out
if I hadn't?


Batch Norm: The Cause of, And Solution To, All of Life's Problems
------------------------------------------------------------------------

By now, you may have noticed a pattern.

On the one hand, all of these problems were my fault. If I had been more careful,
none of these issues would have happened. So perhaps you could chalk this up
to inexperience.

On the other hand, these issues all happened because batch norm forces you to
keep track of things you normally don't need to care about. Suddenly, your model
runs different computation between train time and test time. Suddenly, entries
in the minibatch are no longer independent.
Yes, you can treat batch norm as black box normalization magic, and this'll even
work for a while, but in practice [the abstraction leaks](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/),
like all abstractions do. In batch norm's case, the abstraction leaks in ways
that other optimization tricks don't. It places more cognitive load on the
researcher to keep track of everything, to make sure it's all batch-norm-proof.

In short, the problems were my fault, but batch norm made it a lot easier to
make those mistakes.

That said, when batch norm works, my models definitely train a lot faster.
Like, a lot faster. No contest.

It's the Faustian bargain of optimization. I'll give you 2x faster training, 10x
faster training, 20x faster training! All I ask is that you increase your chance
of hitting some incredibly obtuse bug.

I keep signing it, like a sucker. And so do other people.
If they didn't, the batch norm paper wouldn't have gotten over 1000 citations.


Digression: What Does Batch Norm Do?
--------------------------------------------------------------------------------

Earlier, I mentioned that batch norm is a leaky abstraction. To solve bugs
caused by leaky abstractions, you have to pierce the abstraction barrier. Thus,
to explain my batch norm bugs, I first have to explain batch norm. Feel free
to jump to the next section if this is review.

Let's suppose we're training a neural network on some data. For the sake of the
example, let's say it's a 1 hidden layer network. Letting $$\sigma$$
be the nonlinearity, we have something like this.

$$
    h = f_1(x), F(x) = f_2(h) = f_2(f_1(x))
$$

where $$f_1(x) = \sigma(W_1x + b_1)$$ and $$f_2(h) = \sigma(W_2h + b_2)$$.

![One hidden layer neural net](/public/perils-batch-norm/neural_net.jpeg)
{: .centered }

Adapted [from a picture from CS231N](http://cs231n.github.io/neural-networks-1/)
{: .centered }

During the training process, we can think of each layer as having its own job.
The 1st layer's job is to learn good features from the input. The 2nd layer's
job is to solve the task from the 1st layer's features. These jobs are going
to depend on one another, but backprop gives us a way to update everything
at once. Easy, right?

However, as the weights change, the distribution of each layer's activations
will change too. This makes the next layer's job harder, because the distribution
it's learning from keeps changing underneath it. In the literature, this is
known as *covariate shift*. The key motivation behind batch norm is that covariate
shift can be problem at every layer of the network.

Wouldn't it be nice if we could keep the distribution of activations fixed
during training?
That way, layers in the network wouldn't need to compensate for the shift in
distribution for their inputs.

That would be nice, but in practice there are some problems with it.

* It is expensive to compute the distribution exactly, because the distribution
depends on all datapoints $$X$$.
* If we constrain the distribution of activations, we limit the kinds
of networks we can learn.

To solve this, batch norm does the following.

* We approximate the normalization, by assuming every neuron can be normalized
independently, and that normalizing over a minibatch of points from $$X$$ is
sufficient.
* After normalizing the distribution, we scale by a learned $$\gamma$$ and
shift by a learned $$\beta$$.

The algorithm below (copied from the paper) is the transform done for a single
activation $$x$$, given that we have a batch of activations $$\{x_1,\ldots,x_m\}$$
A small $$\epsilon$$ is added to the normalization to avoid division by $$0$$.

![Batch norm algorithm](/public/perils-batch-norm/batch-norm-alg.png)
{: .centered }

Note that at the end of the transform, the activations can still follow an
arbitrary distribution. However, that distribution's mean and variance depend
only on $$\gamma$$ and $$\beta$$. (To be specific, the mean is $$\beta$$ and
the variance is $$\gamma^2$$.) By concentrating the mean and variance into
a single variable, we make it easier for the network to learn the distribution
that makes solving the task easiest.

During the training process, we also keep a running average of minibatch means
and variances. Let $$\mu_B$$ and $$\sigma_B$$ be the minibatch mean and variance.
We update with an exponential moving average.

$$
    \mu \gets \beta \mu + (1-\beta) \mu_B
$$

$$
    \sigma \gets \beta \sigma + (1-\beta) \sigma_B
$$

The exponential moving average is a weighted average of all terms seen so far,
except it places more weight on recent terms. We use this to approximate
the true mean and variance over the entire dataset.

At evaluation time, instead of normalizing with the minibatch mean and variance,
we normalize with the averaged $$\mu$$ and $$\sigma$$. This makes the evaluation
independent of the examples in each minibatch.


Batch Norm Oddities
-----------------------------------------------------------------------------

I know I've said this already, but it bears repeating:

* Batch norm makes the computation change between train time and test time.
* In train mode, the network's output now depends on the minibatch.

If your code relies on an assumption that batch norm breaks, you're going
to have problems. And annoyingly, batch norm is unique in what assumptions it
breaks, and therefore is much more likely to break something you never expected
to fail.

The following is a list of things I have to keep in mind whenever I use batch norm:

* When using batch norm in a reinforcement learning policy, I must always run
in test mode when collecting experience in the environment. (Because it's easiest
to get an action by feeding a batch of size 1, and in train mode the activations
will get normalized to all zeros.)
* If I'm using batch norm on the inputs to RL, I should normalize each input
modality separately. For example, if the input state is the concatenation of
robot joint positions and robot joint velocities, I don't want the velocities to
affect the normalization of the positions. (Batch norm on the inputs can make
sense for RL because your input distribution changes as your policy changes,
which gives the same covariate shift problem.)
* Never use TensorFlow's meta_checkpoint() functions to load a pretrained model
that uses batch norm. Those functions load the model exactly the way it was
defined at train time - which makes all batch norms in that model frozen in
train mode.
* When finetuning a pretrained model, make sure the moving averages only run
for layers with trainable variables.
* When training a model on a mixture of two datasets, make sure batches
are representative of the mixture. For example, suppose I'm training a model
to classify digits, and I give it both MNIST and SVHN,

IMAGE

In one approach, I randomly give a batch of MNIST data or SVHN data. In
the second, batches have both MNIST and SVHN examples.

IMAGE

The 2nd approach works much better, because the minibatch mean and variance
are closer to the dataset-wise mean and variance. In fact, it's best to
have 2 copies of batch norm, one for each dataset.

IMAGE

Above is a graph of accuracy, where we ran the same hyperparameters 5 times to
get a measure of uncertainty. Not only does the batch norm issue hurt performance,
it also increases the variance in model performance.
* For a similar reason, if you use batch norm in a discriminator in a GAN, always
balance the input batch to be half fake data and half real data - batches of
all fake or all real data makes training more unstable.


Alternatives
--------------------------------------------------------------------------

Batch norm isn't going away. It's ingrained very heavily, it's part of several
famous model architectures, and that means at some point you'll either
train a model with batch norm to compare an old approach, or will use a pretrained
model with batch norm.

But, if neither of those are true, I would recommend using layer norm instead.
It works along similar lines, without breaking the assumptions that batch norm
does.

* The computation in layer norm happens at both train and test time.
* Training is independent from other entries in the batch.

You'll have to do hyperparam tuning anyways, and when tuned I would be surprised
if the difference in performance between layer norm and batch norm was that big.

If you're confident you've considered all the consequences of batch norm, then
sure, you can keep using it. But the whole reason software is hard is because
of the unknown unknowns, the bugs that happen because you don't expect them to
happen.

