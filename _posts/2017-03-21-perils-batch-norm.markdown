---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

*This post is written for deep learning practitioners, and assumes you
know what batch norm is and how it works.*

*If you're new to batch norm,
or want a refresher, a brief overview of batch norm can be found
[here](/public/perils-batch-norm/batch_norm_appendix.html).*

\* \* \*
{: .centered }

Let's talk about batch norm. To be more specific, let's talk about why
I'm starting to hate batch norm.

One day, I was training a neural network with reinforcement learning.
I was trying to reproduce the results of a [paper](https://arxiv.org/abs/1603.00748),
and was having lots of trouble. (Par for the course in RL.)
The first author recommended I add batch norm if I wasn't using it already,
because it was key to solving some of the environments. I did so, but it
still didn't work.

A few days later, I found out that when running my policy in the environment,

* I fed the current state in a batch of size $$1$$.
* I ran the policy in train mode.

So I was normalizing my input to $$\vec{0}$$ all the time. Which sounds a pretty
obvious issue, but thanks to reinforcement learning's inherent
randomness, it wasn't obvious my input was always $$\vec{0}$$.

I fixed it, and started getting the results I was supposed to get.

\* \* \*
{: .centered }

A few months later, an intern I was working with
showed me a *fascinating* bug in his transfer learning experiments.
He was using my code, which used TensorFlow's
[MetaGraph tools](https://www.tensorflow.org/programmers_guide/meta_graph#import_a_metagraph).
They let you take a model checkpoint and reconstruct the TF graph
exactly the way it was at the time the checkpoint got saved. This makes it
really, really easy to load an old model and add a few layers on top of it.

Unfortunately, MetaGraph ended up being our downfall. Turns out it doesn't play
well with batch norm! Model checkpoints are saved while the model is training.
Therefore, the model from the meta checkpoint is always stuck in train mode.
Normally, that's fine. But batch norm turns it into a problem, because
the train time code path differs from the test time code path.
We couldn't do inference for the same reason
as the previous bug - we'd always normalize the input to $$\vec{0}$$. (This
is avoidable if you make the `is_training` flag a placeholder, but for
structural reasons that wasn't doable for this project.)

I estimate we spent at least 6 hours tracking down the batch norm problem,
and it ended with us concluding we needed to rerun all of the experiments
we had done so far.

\*\*\*
{: .centered }

That same day (and I mean literally the same day), I was talking to my mentor
about issues I was having in my own project.
I had two implementations of a neural net. I was feeding the
same input data every step. The networks had exactly the same loss
and exactly the same hyperparameters, with exactly the same optimizer,
trained with exactly the same number of GPUs, *and yet one version had 5%
less classification accuracy, and consistently so.*
It was clear that something had to be different about the two implementations,
but what?

It was very lucky all the MetaGraph stuff got me thinking about batch norm.
Who knows how long it would have taken me to figure it out otherwise?

Let's dig into this one a bit, because this problem was the inspiration
for this blog post.
I was training a model to classify two datasets.
For the sake of an example, let's pretend I was classifying two digit
datasets, MNIST and SVHN.

I had two implementations.
In the first, I sample a batch of MNIST data and a batch of SVHN data, merge
them into one big batch of twice the size, then feed it through the network.

![First version of network](/public/perils-batch-norm/version1.svg)
{: .centered }

In the second, I create two copies of the network with shared weights. One
copy gets MNIST data, and the other copy gets SVHN data.

![Second version of network](/public/perils-batch-norm/version2.svg)
{: .centered }

Note that in both cases, half the data is MNIST and half the data is SVHN.
Naively, we'd expect the gradient to be the same in both versions of the
model. And this is true - until batch norm comes into play. In the first
approach, the batch statistics are computed on both
MNIST and SVHN data. In the second approach, each tower computes
batch statistics on just one dataset, MNIST or SVHN.

At training time, everything's fine. But you know how the two networks
have shared weights? **The moving averages for dataset mean and variance
are also shared, getting updated on both datasets.**
In the second approach, we train as if the normalization was MNIST mean and variance,
or SVHN mean and variance, but at test time we normalize with the mean
and variance of the merged MNIST + SVHN dataset.
And because the test-time normalization differs from the average train
time normalization, we get results like this.

IMAGE

This is a plot of accuracy on my two datasets. The plot is of the top, median,
and worst performance over 5 random seeds. Note the higher variance of the
incorrect approach.

Also, note that this problem isn't specific to domain adaptation. It's a
problem whenever minibatches aren't representative of your data
distribution. The big example is GANs. If your discriminator uses batch
norm, then the minibatches should always be half fake and half real.
If you alternate batches of fake data and real data, you're going to
have a bad time.


Batch Norm: The Cause of, And Solution To, All of Life's Problems
------------------------------------------------------------------------

By now, you may have noticed a pattern to these problems.

I've thought about this quite a bit, and I've concluded that I'm never
touching batch norm again if I can get away with it.

My reasoning comes from the engineering side.
Broadly, when code does the wrong thing, it happens for one of two reasons.

1. You make a silly mistake, like a mistyped variable line or a missing line
of code.
2. You implement everything correctly, catching all the corner cases you can
think of. But it turns out your code is implicitly expecting certain
thing about the behavior, things you don't even know about.
When those implicit assumptions break, the code breaks.
When you fix the bug, you feel dumb, but you also feel proud, because
you've learned something new about your code.

The first is unavoidable. People make stupid mistakes, it happens.
The second is also unavoidable, but it's mitigatable by unit testing, favoring
simpler solutions, and reusing battle-tested code, among other things.

Now, when you add batch norm to a model, it changes it in two fundamental ways.

* The output for a single input $$x_i$$ depends on the other $$x_j$$ within
the minibatch.
* The model does different computation between train time and test time.

Almost no other optimization trick has these properties. That makes it
easier to write code which accidentally assumes inputs in a minibatch are
independent, or accidentally assumes the same thing happens at train time and
test time, because those are sane properties of any model that
doesn't use batch norm. *Which makes it even more infuriating to run into
batch norm bugs!*

One broken invariant here, another there, and next thing you know you've
lost days to debugging subtle issues.

Yes, you can treat batch norm as black box normalization magic. This can work
for a while. But in practice,
[the abstraction leaks](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/),
like all abstractions do, and keeping track of the details is tiring. And in
my experience, although every deep learning abstraction leaks, batch norm
leaks a lot more than the rest.


So...Why Haven't People Ditched Batch Norm?
--------------------------------------------------------------------------

At this point, I'll admit I'm being a bit unfair. Minibatch dependence is
indefensible - no one is going to argue that it's a good quality for
models to have. Given all the annoyances of batch norm, why is it so
ubiquitous?

There's a famous letter in computer science:
Dijkstra's [Go To Statement Considered Harmful](http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html).
In it, Dijkstra argues that the goto statement should be avoided, because it
makes code harder to read, and any program that uses goto can be rewritten
to avoid it.

Deep learning isn't programming.
The unfortunate truth is that batch norm works really, really well.
Yes, it has issues, but when you do everything right, models train a lot
faster. No contest. There's a reason the batch norm paper has so many citations.
(Over 1400 citations, as of this post.)
It's well-tested and shockingly general.

It's the Faustian bargain of deep learning. Faster training, in exchange
for minor insanity. And I keep signing it. And so does everybody else.
(In my case, I'm comparing to prior work that used batch norm, and
I don't want to stray too far from a proven solution.)

I'm somewhat optimistic that other normalization techniques can compete.
I've had some success with layer norm, although I hear the jury
is still out for how well it works with convolutions.
Weight norm and cosine norm sound interesting, although I haven't thought about
them very much, and they work in different ways. Importantly, all three
avoid the main pain points of batch norm. They do the same thing at train time and
test time, and they're all minibatch independent.
If you're working on a new problem, and want to be brave, it might be worth
trying one of those alternatives. Look, you'll need to do hyperparam tuning anyways.
A tuned layer norm model probably shouldn't be much worse than a tuned batch norm
model, so why not give it a shot.

(If you want to stay closer to batch norm's motivation, you could also try
batch renormalization. I haven't tried it, but it's supposed to handle non-independent
minibatches better. Still has train vs test and minibatch dependence though.)
