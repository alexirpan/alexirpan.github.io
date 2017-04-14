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

The problem with batch norm is that it **works.** When batch norm works
right, my models train a lot faster. A *lot* faster. No contest. But now
I'm not sure it's worth it, and my reasoning comes from the engineering side.

Broadly, when code does the wrong thing, it happens for one of three reasons.

1. You make a stupid typo, and it gets caught by static analysis, the compiler,
or a runtime error when that code runs for the first time.
2. You make a silly mistake with the implementation, one that doesn't stop the
code from crashing. It silently does the wrong thing until someone fixes it.
When you find the mistake, you feel really dumb, because you know what the
problem is.
3. You implement everything correctly, catching all the corner cases you can
think of. But it turns out your code is implicitly expecting certain
thing about the behavior, things you don't even know about.
When those implicit assumptions break, the code breaks.
When you fix the bug, you feel dumb, but you also feel proud, because
you've learned something new about your code.

(I'm sure I've missed some cases, but this covers almost all bugs I've
experienced.)

The first two reasons are unavoidable. People make stupid mistakes, it happens.
The third is also unavoidable, but you can mitigate it through testing, design
reviews, and so on.

Back to batch norm.
When you add batch norm to a model, it changes it in two fundamental ways.

* The output for a single input $$x_i$$ depends on the other $$x_j$$ within
the minibatch.
* The model does different computation between train time and test time.

Almost no other optimization trick has these properties. And it's *infuriating*,
because that means batch norm is very, very likely to break an assumption
your code implicitly holds.

The problem
is that I keep making small, subtle mistakes, and I invariably lose days
of my life to debugging one stupid issue or another.


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

