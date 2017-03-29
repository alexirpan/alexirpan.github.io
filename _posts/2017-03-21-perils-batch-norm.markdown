---
layout: post
title:  "On The Perils of Batch Norm"
date:   2017-03-21 00:13:00 -0700
---

> To batch norm, the cause of and solution to all of life's problems!

Okay, that's not the real quote, but after 2-3 weeks of dealing with issues with
batch norm, it's how I feel about the subject.

On the one hand - some models literally do not train without batch norm, and
the ones that do can train in half the time.

On the other hand, it leads to a lot of subtle changes in behavior for
your models. When batch norm works, sure, it's great, you can treat it as
black box normalization magic. In practice, [the abstraction leaks](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/),
like all abstractions do. In batch norm's case, it changes behavior on different
axes, and it ends up placing more cognitivie load on the researcher to get
it right.


What is Batch Norm?
--------------------------------------------------------------------------------

[Batch norm](https://arxiv.org/abs/1502.03167) is one of the seminal optimization
tricks for deep learning models. To put things into perspective: it came out
two years ago, and has over 1000 citations.

What does batch norm do? For the sake of an example, suppose we have a fully
connected neural network. (The intuition will extend to convolutional networks
as well. CNNs are just special cases of fully connected networks, after all.)

Consider some layer of that net, and one specific
output unit of that layer.

IMAGE

Given our data distribution, the output of this unit is itself going to follow
some distribution. That distribution depends on the weights and
biases that feed into this unit.

During the training process, the distribution of this unit's output is
going to change. The next layer in the network has to learn how to effectively
use that unit's activation, which is made harder if the distribution of those
activations is continually shifting. The motivation behind batch norm is to
normalize the output distribution to always be mean 0, variance 1.

When training neural nets, we feed small batches (minibatches) of data at a time.
To make this example concrete, let's say our batch size is 32. Then, depending
