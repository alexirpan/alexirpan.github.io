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
arne't compatible with batch norm.

Why?

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

When you add batch norm to a model, it changes it in two fundamental ways.

* For a single input $$x_i$$, the output depends on other $$x_j$$ in the
minibatch.
* The evaluation at test time is different from the evaluation at train time.

Almost no other optimization trick has this property. And it's *infuriating*,
because that means batch norm is very, very likely to break an assumption
your code implicitly holds.

Alright, but that was just a one-off thing, right? Well, then the second
bug happened. I was using TensorFlow's [MetaGraph](https://www.tensorflow.org/programmers_guide/meta_graph#import_a_metagraph)
utils, which reconstructs the model exactly the way it was at train time.
(This is useful if you want to take a pretrained model, then finetune it on
a new dataset.) Well, guess what? It plays poorly with batch norm!
The computation batch norm runs at train time is different from the
computation it runs at test time, so the loaded pretrained
model was forever stuck in train mode, even at inference time.

Now, let's look at the third batch norm issue I had. I was training a model
on a mixture of two datasets. (For the sake of the example, let's pretend it
they were both digit datasets, MNIST and SVHN.) I had two versions of the model.
In the first, I take a batch of MNIST and a batch of SVHN, then join them into
one giant batch and feed it through the network.

IMAGE

In the second, I create two copies of the network with shared weights, giving
one copy MNIST and the other copy SVHN.

IMAGE

In both cases, every gradient is computed on a batch of 32 MNIST examples and
32 SVHN examples. Yet the performance was significantly different.

After a big search to find bugs, I eventually figured out that batch norm
was the issue. In the first approach, we normalize the MNIST and SVHN data
together. In the second approach, each tower normalizes just MNIST data, or
just SVHN data. The moving averages were shared as well, and get updated
with both MNIST and SVHN data.

* In the first approach, we train as if the batch statistics were half MNIST
half SVHN, and test as if the batch statistics were half MNIST half SVHN.
* In the second approach, we train as if the batch statistics were MNIST *or*
SVHN, but test as if the batch statistics were half MNIST half SVHN.

In the latter case, because we're normalizing differently than we were at
train time, performance drops drastically.

IMAGE

Above is a graph of accuracy. (Not on MNIST + SVHN - on the datasets I was
actually doing experiments on.) I ran the exact same hyperparameters with
5 random seeds for both methods. Note that not only did it hurt performance,
it also increased the variance.

Batch Norm: The Cause of, And Solution To, All of Life's Problems
------------------------------------------------------------------------

By now, you may have noticed a pattern.

When you add batch norm to a model, it changes it in two fundamental ways.

* For a single input $$x_i$$, the output depends on other $$x_j$$ in the
minibatch.
* The evaluation at test time is different from the evaluation at train time.

Almost no other optimization trick has this property. And it's *infuriating*,
because that means batch norm is very, very likely to break an assumption
your code implicitly holds. Take the first issue I had, where batch norm + RL
was failing. Turns out I was collecting experience with `is_training=True`.
The easiest way to do that was to give an input of batch size $$1$$,
and batch norm normalized it to $$\vec{0}$$.





The problem with batch norm is that it **works.** When I do batch norm
right, my models train a lot faster. A *lot* faster. No contest. The problem
is that I keep making small, subtle mistakes, and I invariably lose days
of my life to debugging one stupid issue or another.



Let me br

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

