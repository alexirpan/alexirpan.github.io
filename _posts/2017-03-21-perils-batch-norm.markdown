---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

*This post assumes you know what batch norm is.
A brief overview of batch norm can be found[here](/public/perils-batch-norm/batch_norm_appendix.html).*

Let's talk about batch norm. To be more specific, let's talk about why
I'm starting to hate batch norm.

One day, I was training a neural network with reinforcement learning.
I was trying to reproduce the results of paper, with lots of difficulty.
Someone recommended I add batch norm, because
it was key to making some of the models train. I implemented it, but I
still couldn't reproduce the results.

A few days later, I found out I always collected experience by feeding
a batch of size $$1$$, with just the current state. That collect always
ran in train mode. Combined, I was always normalizing to $$\vec{0}$$.

\*\*\*
{: .centered }

Another day, somebody came to me with a strange bug in his transfer
experiments. We had been using TensorFlow's
[MetaGraph](https://www.tensorflow.org/programmers_guide/meta_graph#import_a_metagraph)
tools for finetuning pretrained models. These tools take a model
checkpoint and reconstruct it in the current session, which makes finetuning
a lot easier. After a few hours of digging, we realized those tools
weren't compatible with batch norm.

Why? Well, the MetaGraph import reconstructs the model exactly the way it
was defined at train time. Normally this isn't an issue, but in models with
batch norm, the computation at train time is different from the computation
at test time. The loaded pretrained model was stuck in train mode forever,
and in particular it meant we couldn't do inference for the same reason
as the previous bug - we'd always normalize the input to $$\vec{0}$$.

\*\*\*
{: .centered }

That same day (and I mean literally that same day), I was discussing
recent issues I was having with my own project.
I had two implementations of a neural net. At each step, I was feedin gthe
same input data. The networks had exactly the same loss
and exactly the same hyperparameters, with exactly the same optimizer (RMSProp),
trained with exactly the same number of GPUs, *and yet one version had 5%
less classification accuracy?*

It was clear that something had to be different about the two implementations,
but what could it be? Well, turns out it was very lucky I had been thinking
about batch norm because of the MetaGraph stuff. If I hadn't, I have no idea
how long it would have taken me to figure it out.

Let's dig into this one a bit, because the problem is actually pretty general.
I was training a model to classify two datasets, for some domain adaptation
experiments. For the sake of the example,
let's pretend it they were both digit datasets, MNIST and SVHN.

I have two implementations of this.
In the first, I sample a batch of MNIST data and a batch of SVHN data, join
them into one big batch of twice the size, then feed it through the network.

IMAGE

In the second, I create two copies of the network with shared weights. One
copy gets MNISt data, and the other copy gets SVHN data.

IMAGE

Note that in both cases, half the data is MNIST and half the data is SVHN.
Naively, we'd expect the gradient to be the same in both versions of the
model. And this is true - until batch norm comes into play. In the first
approach, the batch statistics and normalization are computed on both
MNIST and SVHn data. In the second approach, each tower computes
batch statistics on just one dataset, MNIST or SVHN.

At training time, everything's fine. But remember that the two networks
have shared weights? **The moving averages for dataset mean and variance
were also shared, getting updated on both datasets.**
So in the second approach, we train as if the mean
was the MNIST mean or SVHN mean, but at test time we normalized as if
the mean was the MNIST + SVHN mean. When the test-time normalization is
different from the train time normalization, we get results like this.

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


So...Why Haven't You Ditched Batch Norm Already?
--------------------------------------------------------------------------

The problem with batch norm is that it works.

No, I mean, it **works.** When you do everything right, models train a lot
faster. No contest. It's well-tested, it's part of tons of pretrained models,
and it's shockingly general. There's a reason the batch norm paper has
so many citations.

It's the Faustian bargain of deep learning. Faster training, in exchange
for a slice of your sanity. And I keep signing it, because I'm working on problems
where previous state of the art used batch norm, and I'm loathe to move too far
off someting that works.

Now, that being said, I'm somewhat optimistic about the other normalization
techniques. I've had some success with layer norm, although I hear the jury
is still out for adding it to conv layers. Weight norm and cosine norm
sound interesting, although I haven't thought about them that much. All
three do the same thing at train time and test time, and all three are minibatch
independent. If you're working on a problem from scratch (no known-working
neural net architectures), it's probably worth trying one of the above.
You'll need to do hyperparam tuning anyways.
