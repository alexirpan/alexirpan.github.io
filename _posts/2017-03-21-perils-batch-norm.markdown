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

Guess what? It was batch norm! Good thing the bug from the last story was
still in my head, becuase who knows how long it would have taken me otherwise?


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

* We can't compute the distribution exactly, because the distribution depends
on all datapoints $$X$$.
* If we constrain the distribution of activations, we limit the kinds
of networks we can learn.

To solve this, batch norm does the following.

* 


IMAGE


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


Stories Revisited
-----------------------------------------------------------------------------

With batch norm background out of the way, let's revisit the stories from the
beginning, and see what exactly went wrong.

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

Due to implementation reasons, when sharing weights, the batch norm moving
averages were shared as well. In both approaches, the moving averages
converge to the mean and variance of the average of the two distributions.
But at training time, they differ.

* In the first approach, we train the network as if the true mean/variance
were the mean/variance of the mixture distribution.
* In the second approach, we train the network as if the true mean
was the mean of just the 1st distribution, or just the 2nd distribution,
and never the mixture. Same for the variance. So, at training time everything
works out okay, but at evalutation time, the mean/variance are different from
the ones the network was trained with.

IMAGE

Above is a graph of accuracy, where we ran the same hyperparameters 5 times to
get a measure of uncertainty. Not only does the batch norm issue hurt performance,
it also increases the variance in model performance.

(Note this is a general problem whenever you train the same parameters on
two different datasets. In particular, when training a GAN, if your discriminator
uses batch norm, you likely want to make sure your batches always have a mix
of real and fake data.)


Alternatives
--------------------------------------------------------------------------

I know I've said this already, but it bears repeating:
all of these issues happened because of what batch norm does to a model.

* Batch norm makes the computation change between train time and test time.
* Batch norm makes training depend on all the entries in the batch.

And if your code relies on assumptions that batch norm breaks, you're going
to have problems.

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

CONCLUSION HERE


After the fix, my model started working, but I got lucky here too. I was
applying batch norm directly on the input states when training. In supervised
learning, you'd never do this, because it's equivalent to whitening the data,
and presumably you've done that already. But in reinforcement learning, using
batch norm makes sense, because the state distribution is going to change as
your policy changes. Without batch norm, even inputs have the same covariate
shift problem.

But in the environment I was using, the states were the relative position of
the robot joints, and the velocities of each of those joints, concatenated
together. Because I naively applied normalization over the entire state,
the faster the robot moved, the lower the magnitude of the normalized joint
inputs. A better approach would be to normalize just the parts of the state
space corresponding to joint position. But I got lucky - reinforcement
learning was able to power through the issue.
