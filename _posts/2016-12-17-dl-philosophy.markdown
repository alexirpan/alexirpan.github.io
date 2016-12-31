---
layout: post
title:  "Deep Learning Philosophy"
date:   2016-12-22 22:14:00 -0700
---

This post collects various thoughts I've had about deep learning.

This is **not** intended to be a tutorial in deep learning, because there are
a ton of those already. I haven't seen as much writing about the field itself,
and as a researcher in the field, I think it's important to understand why
the field is the way it is.

# Table of Contents

- Clobbered for auto generated table of contents
{:toc}

# Background

I know I said this wasn't going to be a tutorial in deep learning, but
I want this post to be self-contained. Here's the background I expect
people to have, before getting into the meat of the post.

## What is Machine Learning?

Here's a definition from a previous blog post, which is a paraphrase of
Wikipedia's description.

> Machine learning is the study of algorithms that let a computer learn insights from data in a semi-autonomous way.

For this post, I'll phrase it differently.

> Machine learning is the study of algorithms that can learn functions between
> two sets of data.

In many machine learning problems, we have examples of desired
inputs and desired outputs. Using those examples, we want to train a function
to map from those inputs to those outputs. After training is done, we evaluate
that function on new inputs to get a guess/approximation of the true output.
Or in short: every problem in ML is a function learning problem.

Examples!

Suppose we had a set of points in the 2D plane, and wanted to fit a trendline that best
fits the data. We can use linear regression.

Image of points in a plane

Input set: The x-coordinates of each point.  
Output set: The y-coordinate of each point.  
Algorithm: Linear regression.  
Function learned: a $$f(x)$$ of the form $$f(x) = ax + b$$ such that for every $$(x, y)$$, $$y$$ is close to
$$f(x)$$. (To be precise, linear regression minimizes $$\sum (x,y) (y - f(x))^2$$)

Suppose the points were in 3D space instead. Linear regression still works,
but in this case we're learning a 2D plane instead of a line.

Image of points in 3D space.

Input set: The (x,y)-coordinates of each point.  
Output set: The z-coordinate of each point.  
Algorithm: Linear regression.  
Function learned: a $$f(x,y)$$ of the form $$f(x, y) = ax + by + c$$
such that for every $$(x, y, z)$$, the sum
$$\sum (x,y,z) (z - f(x,y))^2$$ is minimized.

In the first example, we had two-dimensional data $$(x,y)$$, but the
data was clustered around a line, which is a one-dimensional object.
Similarly, in the second example we had three-dimensional data $$(x,y,z)$$,
but the data was clustered around a plane, a two-dimensional object.

(Something something manifold hypothesis)

Points in 3D space are boring. Who cares about those? Let's jump to
research-level problems.

Say we're really, really big fans of corgis.
We're such a big fan that we want to automatically
filter our album of photos to only the photos with corgis in them.

This is the textbook image classification problem. Each image falls into
two classes, "contains corgis" and "doesn't contain corgis".

PICTURE HERE

Input set: A collection of images.  
Output set: A prediction of corginess for each image.  
Algorithm: Something from computer vision. In the past, HOG features + support
vector machines. Now, a convolutional neural net.  
Function learned: A function $$f$$ such that $$f(corgi photo) = corgis$$
and $$f(not corgi) = NO$$

Suppose we had some English sentences, and wanted to translate them into
Spanish.

PICTURE HERE

Input set: A colleciton of English sentences.  
Output set: A translation of each sentence into Spanish.  
Algorithm: Something from natural language processing. Nowadays, that
means a big recurrent neural net or LSTM.  
Function learned: $$f(ENGLISH SENTENCE) = TRANSLATION$$

Say we're a site that hosts a lot of pictures (like Facebook), and we
want to cater to the visually impaired. These people use screen readers
to browse the Internet. Given an image, we want to write a caption for
that image.

PICTURE FROM KARPATHY'S PAPER

Input set: A collection of images.  
Output set: A description of each image.
Algorithm: Use a CNN to encode the data into some representation, then
have an RNN decode the representation into a setence.  
Function learned: $$f(corgi) = A dog is sitting on a rug.$$

A programmer is bored of implementing design docs. They have a document
describing the design of the system, and want to produce code that matches
the design spce.

PICTURE

Input set: Documents that describe what the program should do, in English text.  
Output set: Implementations of each of those design docs.  
Algorithm: N/A. The research isn't there yet.

\* \* \*
{: .centered }

## What is Deep Learning?

Deep learning is a rapidly growing subfield of machine learning that focuses
on applying and developing neural networks.

### What Are Neural Networks?

In neuroscience, we model a neuron in the brain as a unit that computes some
value from its input. If the value passes a certain threshold, the neuron
"activates". That activation (or lack of activation) is fed as input to
later neurons in the brain.
Neural nets are a implementation of this idea in code. They chain several
artificial neurons into layers of computation. Given examples of true data, we can train
the neurons to fire or not fire apporpriately.

PICTURE of perceptron and neural net

This is the way many, many people introduce neural nets, and I hate it.

Yes, neural nets are biologically inspired. Yes, neuroscience matters to
deep learning. I hate it not because it's incorrect, but because the narrative
of neural nets as artificial brains is a huge popular science meme that
breeds misconceptions about the field.
Anthropomorphizing neural nets and explaining what they aim to be is
much easier than explaining what they actually are.

I prefer a bottom-up explanation that starts from the math level.
Unfortunately, it's not as accessible, but it has fewer dreams of grandeur.

> Neural nets are a differentiable family of functions.
> Each layer has a weight matrix $$W$$ and bias parameters $$b$$. These layers
> alternate between applying a linear function and applying a nonlinear
> activation function.

$$
    \ell_1(x) = \sigma(W_1x + b_1)
$$

$$
    \ell_2(x) = \sigma(W_2\ell_1(x) + b_2)
$$

$$
    f(x) = \ell_3(x) = \sigma(W_2\ell_2(x) + b_3)
$$

(For emphasis: describing neural nets as artifical brains isn't *wrong*,
but the approximation between neural nets and brains is very very crude.
Even the neuroscience researchers in deep learning admit this is true.
In fact, that's why they're interested in the field;
they want to push neural nets closer to their real world inspiration.)

# What Makes Neural Nets Special?

Why are neural nets in particular growing so fast? What differentiates them
from other approaches?

## A Theoretical View

A family of functions $$F$$ is a universal approximator if for any continuous
function
$$f$$, there is an $$f' \in F$$ that's close to $$f$$ at every point
(for any $$\epsilon > 0$$, there exists an $$f' \in F$$ such that
$$|f(x) - f'(x)| < \epsilon$$ for all $$x$$)

**Neural nets are universal function approximators.**

Recall that machine learning is all about learning the right function.
Universal approximation tells us that in principle, it's always possible to
learn a neural net close to the true function.

## A Practical View

It's neat that this is true. However, when you look at the proof for
universal approximation, all it proves is that we can hardcode a neural
net's output at a specific $$x$$, and if we hardcode the output at enough
different $$x$$ we can approximate any function.

Doing this construction in practice would require a ridiculously large neural
net.

Neural nets matter for a different reason: in practice, modestly sized neural
nets are 
**they are differentiable, they
generalize well in practice, and given enough data they outperform every
other approach.**

Here is the classical picture from every talk Andrew Ng ever does about
deep learning.

PICTURE

The pattern so far is that above a certain data threshold, neural net approaches
outperform every other approach. Which is weirdly fascinating, when you think about it.
This claim is almost an axiom in the deep learning community; the only counterexamples
I know of are pathological ones.

When you have a hammer, everything looks like a nail. And so far, neural nets are
a big hammer that turns a ton of problems into nails.


Why does differentiability matter?
The dirty secret of machine learning is that 90% of it reduces to gradient
descent on some loss function.

* Define a function $$f_\theta(x) = \hat{y}$$, where $$\theta$$ are the
parameters, $$x$$ is the desired input, and $$\hat{y}$$ is the predicted
output.
* Define a differentiable loss function $$\ell(\hat{y},y)$$, which is 0 when
$$\hat{y} = y$$ and positive otherwise.
* Find $$\nabla_\theta \ell(\hat{y}, y)$$, the gradient with respect to $$\theta$$.
With multivariable calculus, you can show this is the direction of steepest
descent in parameter space (in $$\theta$$-space.)
* Update $$\theta$$ with $$\theta \gets \theta - \alpha * \nabla_\theta \ell(\hat{y}, y)$$,
where $$\alpha$$ is the learning rate, which decides how quickly the model is
allowed to update. This brings us to a region of lower loss.
* Repeat until loss stops going down.

Classical parameter descent picture.

Different parameters (different $$\theta$$) give different functions $$f_\theta(x)$$.
Gradient descent gives us a way to search the function space in a way that
guides us towards functions with smaller loss...as long as the function family
is differentiable. And neural nets are differentiable.


# What's the Field Like?

The field is very exciting. Everything's moving ridiculously quickly, which is
painful if you're trying to keep up with current research, but it feels like
there's a new surprising result every month.

To emphasize how fast the field is moving, here are a few examples.

* The public release of [TensorFlow](https://www.tensorflow.org/) was just
over a year ago. (On my birthday! Hooray!) It's become one of the big
machine learning frameworks.
* [The paper for Adam](https://arxiv.org/abs/1412.6980), a new gradient optimization
method, came out about two years ago. It's since become the optimization
algorithm of choice for a ridiculous number of papers. Google Scholar
says it has almost 1300 citations.
* [Dropout](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf) debuted in
2014, and has over 1700 citations.
* [Batch norm](https://arxiv.org/abs/1502.03167)
came out in 2015, and it's since become the default for image models - many
models don't train at all if you don't use batch norm.
* [ResNets](https://arxiv.org/abs/1512.03385)
came out a year ago, became the new big thing in image recognition after they
beasted ImageNet 2015, and now they already feel like old news.

Maybe I'm unintentionally cherrypicking here, but it feels weird that a ton of
important papers came out just in the past three years. It's impossible to keep
up with everything. [Arxiv Sanity Preserver](http://www.arxiv-sanity.com/)
helps, but there's just so much to read.

To quote one of my friends,

> Is everything [in deep learning] SUPER DUPER OPEN or is it just me?

In some ways, it is. The core idea in many papers can be shockingly
simple to describe. Dropout is literally a few sentences.

> To train a neural net with dropout, for each neuron, multiply the output
> by $$1/p$$ with probability $$p$$, and otherwise set it to $$0$$. This keeps
> the expected sum of outputs the same as without dropout, but the random
> dropping ensures that the neural net's output is more robust.

When I read papers in the field, most of time I think, "Wait, that's it?
That's so simple!"

As a guy who took grad level theoretical computer
science courses for **fun**, this can be deeply unsatisfying.
The TCS papers I've read have a collection of core ideas that branch into
proof details. The deep learning papers I've read have a single core idea
that branches into the details of the paper's experiments. (This excludes
the small set of theoretical deep learning papers, for obvious reasons.)

The field is very, very experimentalist. Deep learning has found its
biggest niche in applications, and in applied problems, you care about the
final performance first and foremost. If it doesn't beat state-of-the-art, the
paper needs to have a very compelling argument for why this doesn't matter.

It's not that we don't care about explanations. It's that [theory lags practice](http://lemire.me/blog/2015/01/07/theory-lags-practice/) so much that we don't have the tools to build anything
besides empirical explanations. Even fuzzy, imprecise arguments with empirical
evidence are good enough, as long as they allow for intuitive extensions of the
work.

And there are almost always intuitive extensions. In deep learning, ideas
are cheap, and execution is hard. To quote Andrew Ng, "90% of machine learning
is dirty work." People have ideas all the time; the glory is in getting them
to work.

In many paper stories, I've heard the same story: we tried something, and
it failed. We tried again, and it failed. We tried, again and again, and
it finally worked. By the time it worked, we had 3 days to write the paper.

![Graph of NIPS submissions vs time to deadline](/public/dl-philosophy/nips_submission.png)
{: .centered }

[(This is one of my favorite graphs.)](http://homepages.inf.ed.ac.uk/imurray2/nips_submission_times/)
{: .centered }

It's not that the authors didn't think of those extensions. They
just ran out of time, because everyone procrastinates and research is hard and
deadlines are brick walls that force you to aim for completion instead of
perfection.

Also, there are a ton of people in the field. No, like, a ton. Do you know how
big NIPS was this year? It was about 5800 people. For a research conference.
Cultural norm is to publish on arXiv, submit to conferences over journals,
publish your conference submission on arXiv as soon as you're allowed to,
and publish often, with source code if you have the time to clean it up.
This is great for sharing ideas, but it pushes researchers to put their work
out early, because of how easy it is to get scooped. When that many people
are working on similar problems, solutions tend to arise at the same time.

This isn't the best environment for well-written papers that flip your research
worldview. It leads to papers that feel very incremental and obvious, after
the fact.

So yes, it is all very open, and the ideas are often very simple. But getting
things to work at all (and work well) is a big enough achievement to justify
publication.

# Why is Deep Learning Progressing So Fast? A Few Arguments

I've made a big show of explaining how quickly the field moves. But why is
deep learning in particular growing so fast, compared to other subfields in
machine learning?

There isn't a single answer. It's more like a collection of answers.

## Big Data Lets Us Retry Old Ideas

Neural nets aren't new. They've been around since the 1980s. The argument
goes like this: the old guard of neural net researchers always knew it was
a matter of time before neural nets would rise again. Now that we have
large datasets and the compute power to process them, many ideas we
theorized about in the past can be tested for real. The empirical results
let us refine our ideas and get better performance, through the scientific
method.

This explains why neural nets started working, but it doesn't explain why
the field is growing so quickly. Besides, a lot of researchers in the new wave
haven't read the old papers anyways. Yann LeCun has lamented that many new papers
are rediscovering ideas from the 80s and 90s, and Schmidhuber...well, his
citation claims are a meme in the ML community by this point.

Besides, there's always been a state-of-the-art machine learning method.
Support vector machines, random forests, etc. As far as I know, they've never
blown up like neural nets have. (But I'm new to the field - maybe my folklore
is out of date.)

## Strong Financial Incentives

Image recognition, speech transcription, machine translation, and other areas
have become so good that they're practical enough for companies to care
about the research. There's a ton of money in machine learning, so companies
are throwing a lot of funding at machine learning researchers in industry
research labs, which speeds up progress.


## Architecture Engineering is Easier and Simpler Than Feature Engineering

![Features vs neural nets](/public/dl-philosophy/features.svg)
{: .centered }

(From Andrej Karpathy's presentation at Bay Area Deep Learning School 2016)
{: .centered }

Traditionally, when people have wanted to apply machine learning to a problem,
they take the raw data and create *features* of the data. These are
human-designed heuristics of what's important about the data.
In spam detection, features could be relative word frequency, number of typos,
etc.

You can think of features as biases humans place on the training process.
Ideally, we wouldn't need features, but for a long time, feature engineering was required to
learn anything, because the existing machine learning
methods just weren't expressive enough.

Neural nets are challenging this paradigm. Computer vision used to use many heuristically
designed features that were specific to image-based datasets. Here's a slide
where Karpathy points out how it used to be in 2011.

![Features old](/public/dl-philosophy/old_features.svg)
{: .centered }

**This doesn't remove human design entirely.** Features are biases on what
the model should optimize over, but a similar thing happens with neural net
architectures. Different architectures are better at representing different
datasets. CNNs are good for translation invariant patterns,
RNNs are good for sequential data,
fully convolutional models may beat models that mix convolutions with pooling,
and so on.
Architecture choices are made before training starts, just like feature
engineering.
All we've done is trade expert feature design for expert neural net
architecture design.

**The key is that architecture design is easier and
more general than feature design.**

You don't need to know all the image
statistics tricks if you want to do computer vision. Similarly, neural machine
translation lets you skip the linguistics-specific knowledge that rules previous
systems. Screw sentence alignment, just shove it all into a single hidden state
vector, or do some attention mechanism. Key words? Eh, just change everything into
word vectors, they'll do the right thing.

(Sometimes, it feels insane that we can wave our hands while shouting neural
nets, and then get state-of-the-art translation results.)

Simpler model design means lower barrier to entry and fewer places to have bugs.
Which means more researchers, and faster implementation. There's no single
reason deep learning is growing quickly. It's all interconnected.

## Unification of Approaches

Across several fields, we're starting to see a unification of methods. Convnets
are good at pattern recognition, which is good for computer vision, but it's also
good for Computer Go. RNNs are good at sequential data, which is good for
language models, but it's also good for reinforcement learning problems, and
even image generation, if you formulate image generation as a sequence of
pixel outputs. (Link DRAW here)

They're all unifed under the banner of neural nets, and that gives a common
language for sharing ideas. This is why Google Brain exists. By making all
the neural net researchers work in the same building, they all start working
faster. It's easier for ideas in one domain to spark ideas in another
when the research is founded on the same principles.

To use an analogy: it's as if neural nets are an open source repository of
information. People play around with them on the problem of their choice,
and when they discover something that could generalize outside their problem,
they send what they learned back upstream. Someone else can then pull that
change, modify it to fit the problem they're working on, and
push what *they* learned back upstream.

MAYBE HAVE A DIAGRAM HERE?

(Yes I did just use source control as an analogy for research. This might be
the most computer-sciency analogy I've ever done.)

# Neural Nets as Computation Blocks

(Note: This section repeats a lot of things I said before. I'm still figuring out where
I want the new ideas to go. The modularity/composability stuff is actually
pretty important.)

(I'm actually not happy with this section in general, needs a rewrite.)

Andrew Ng has a nice quote about why deep learning is so flexible. Most machine
learning approaches map numbers to other numbers. Deep neural nets are different -
they let us map arbitrary data into a smaller numerical space, which can then
be interpreted as another form of data. Images into numbers into text.
Text into numbers into text in another language. Words into numbers into...music?
Sure, why not?

Convnets are neural networks good at learning patterns invariant to location
in the input. That's good for computer vision, and that's also good for music
generation, and also for computational biology.

RNNs are good for sequence data, making them good for language models, which
need to carry dependencies through time. But they're also good for
video prediction, and for reinforcement learning, both of which rely on
outputting a good trajectory instead of a good image.

LSTMs are more complicated RNNs. They use more parameters, but generally
have better capacity and avoid graidnet issues that RNNs have. LSTMs have replaced
RNNs in many (but not all!) applications.

We're entering this weird regime, where we can daisy-chain a ton of neural net
layers together, and the system is still trainable and will still do the right
thing. Some conv layers to process an image, maybe an RNN if you want to process
text, some fully connected layers to glue the whole thing together.
Moreover, this end-to-end approach actually work better than training
each component individually - if you have enough data. (Intuitively, by
making everything end-to-end, the entire network is optimized for the final
task you want to solve. If you train every component individually, each
component is optimized for its own objective, which may not be exactly aligned
with the final objective.)

# Research Directions

## The Sliding Scale of Deep Learning Research

I know I've been talking about "the field of deep learning" a lot in this post,
but for many people neural nets are more like a tool than a field.
When I think about the research, it divides into roughly three categories.

Note that when I say roughly, I mean roughly. Researchers slide up and down
the spectrum very often. Projects can start in one category and slide to
another depending on how the experiments go.

(Note: below is all somewhat incomplete.)

## Standard Architectures on New Problems

In this work, people strongly believe vanilla neural net methods will work out
of the box. They don't care about neural nets in particular, they just want
to solve the problem they're working on, using neural nets as a subroutine.
This research has no novelty from the deep learning side (besides learning
that neural nets can solve this problem too.)

The struggle in this research is often in obtaining a large, clean dataset
to run existing methods on. After all the plumbing is done, the training itself
is straightforward.

[Computational biology](http://onlinelibrary.wiley.com/doi/10.15252/msb.20156651/full).

[Medical imaging (diabetic retinopathy)](http://jamanetwork.com/journals/jama/article-abstract/2588763)

[Premise selection for Theorem Provers (DeepMath)](https://arxiv.org/abs/1606.04442)

My research area of deep reinforcement learning, falls into this bucket.
Sometimes there are new architecture ideas, but much of the research is
about developing new RL algorithms. These algorithms are usually independent
of the function representation, and the only difference in deep RL is that
the function representation happens to be a neural net. I have another post
planned for deep reinforcement learning, so I'll leave the details for another
time.

Sometimes, standard approaches don't work out. This leads into the next
category.

## New Architectures Developed for Existing/New Problems

In the flagship deep learning problems (image classification, speech
recognition), people have run the simple ideas into the ground. Even some
novel problems stand up to the neural net hammer more than you'd expect.

In those cases, people need to develop new architectures ideas or new
loss functions. The goal is still on solving the current problem - any
advances to neural nets themselves are incidental. (Note: maybe link to
the section about unification? Or maybe I don't need to hammer this point
home.)

Here, aspects of the problem solution depend or heavily assuume the function
representation is a neural net. They may also use custom loss functions
that had to be developed for the problem at hand.

[Residual networks](https://arxiv.org/abs/1505.00387) were developed by
Microsoft Research Asia for ImageNet, but could be applicable in other fields.

In [Stochastic Neural Networks for Hierarchical Reinforcement Learning](https://openreview.net/pdf?id=B1oK8aoxe),
the network is mostly standard, but a mix of random inputs and mutual
information reward encourages the main goal: automatic learning of low
level skills in the environment.

[WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) by
Deepmind was developed to improve audio generation. Although the focus was
audio generation, the approach is general enough to be applicable to other
problems.

In [Towards End-to-End Speech Recognition with Recurrent Neural Networks](http://www.jmlr.org/proceedings/papers/v32/graves14.pdf),
they used bidirectional LSTMs, which actually were first developed over a decade
ago, but they needed to be combined with many speech recognition specific
loss functions to give good performance.

[Progressive Neural Networks](https://arxiv.org/abs/1606.04671) are an approach
for transfer learning and avoiding catastrophic forgetting in reinforcement
learning. The architecture used is general enough to be applied to image
recognition too, as seen in [this ICLR 2017 submission](https://openreview.net/pdf?id=ryZqPN5xe).


## Research Exclusively on Neural Nets

Research in this area has the primary goal of extending our understanding of
neural nets and extending the problems that neural nets could be applied to.
Although the papers run benchmarks from other problems, doing well on those
benchmarks isn't the point.

### Theoretical Justification for Neural Nets

This research focuses on devising theoretical explanations for the power of neural
nets. To tell the truth, I only have passing knowledge of the theory work, so
don't trust my comments too much.

* [The Loss Surface of Multilayer Networks (AISTATS 2015)](https://arxiv.org/pdf/1412.0233.pdf).
Relates neural networks to spherical spin-glass models.
* [On the Number of Linear Regions of Deep Neural Networks (NIPS 2014)](http://papers.nips.cc/paper/5422-on-the-number-of-linear-regions-of-deep-neural-networks).
Proves number of linear regions of the network can grow exponentially with
depth.
* [Critical Behavior from Deep Dynamics: A Hidden Dimension in Natural Language](https://arxiv.org/abs/1606.06737).
Shows that empirically, mutual information between symbols in language data
decays by a power law. Proves simple Markov models cannot have this property,
but RNNs and LSTMs can.

If you're interested in this flavor of research, [Yoshua Bengio gave a good talk
about this Bay Area Deep Learning School 2016](https://www.youtube.com/watch?v=11rsu_WwZTc).
The talk also covered the next research area of...

### Duplicating Neuroscience and Biological Plausibility.

Demis Hassabis, co-founder of DeepMind, was part of a panel at the NIPS 2016
Brains & Bits workshop. He gave a succinct justification for why neuroscience
matters. We know the brain works for intelligence. If we can understand the
brain and reproduce it in software, it has to work. That lets us commit to
5 year or 10 year projects with more confidence than we'd normally have.

Again, I'm not that familiar with neuroscience
I'm less familiar with this due to my biases, but I'll list some work.

* Feedback alignment (a more biologically plausible backprop)
* Energy based models (ML algorithm that could run better on analog hardware)
* Count-based exploration (can be motivated by the hippocampus)
* Modulated locomotor controllers (a fast reflex "spinal cord" and slower LOOK UP THE PAPER)


### Interpretability of Neural Nets

This research explores ways to inspect neural nets to better understand how
they arrive at their final output. The most notable example is DeepDream.

IMAGES

It almost feels wrong to call this a research area, because I don't know of
anybody whose primary research focus is interpreting neural nets.
However, many papers include visualizations anyways, because it makes the
paper stronger.

### Make ALL The Things Differentiable!

For all gradient-based ML models (which includes neural nets), we need the model
to be differentiable. In continuous problems, this is usually straightforward,
but in discrete problems we start running into issues.

The most common way to deal with this is making the neural net output a distribution
over the discrete choices. We then take the weighted average, or sample from
the distribution. This lets us relax the problem from discrete output to
continuous output. Initially, the distribution will be uniform, but over
time we expect the distribution to converge to putting all weight on a single
choice.

DIAGRAM

The thinking process goes like so.

* Neural nets don't apply to X because it's not differentiable.
* Let's make the problem differentiable, then use a neural net to see what happens.

Recent work in this area includes:

* Variational autoencoders
* Gumbel-Softmax / Concrete distribution
* Straightthrough estimator
* Neural Turing Machines, Neural GPU
* Pointer networks.

These papers often don't outperform the work they're inspired from, but they
do demonstrate what problems we can solve just through gradient descent.

Speaking of solving by gradient descent...

### Meta-Learning

Recall that machine learning is all about learning functions. Functions are
everywhere, including machine learning. What if we applied neural nets to the
functions we use to optimize neural nets?

There's been tentative steps in this direction. In Learning to "learn by
gradient descent" by gradient descent, the authors note that people rarely use
vanilla SGD. They always use a function of the gradient instead (momentum, Adagrad, etc.)

EQUATION

Instead of having a human describe the function, we can have NAME be represented
by a neural net. To train the neural net, we generate a large set of functions,
and use gradient descent to update the neural net to minimize those functions as
quickly as possible.

PICTURE

A related work is RL^2. Remember RNNs can be thought of as representing
algorithms. Every RL algorithm has the same interface - obtain a sample from the
environment, and return the next action to take in the environment. Instead of
doing this with a known RL algorithm, the agent can use an RNN that persists
history across multiple episodes.

PICTURE

Both of these results have large cavaets. They've only been tested on toy problems.
The metalearned in RL^2 in particular isn't very robust (but to be fair a lot
of deep RL isn't very robust.)

Still, it's a bit fascinating that this metalearning actually works. In
principle, it's supposed to work. It's just surprising that parts of it are
already working.

Before people get too scared, I think we're still a ways off from recursive
self-improvement. The positive results show that if you learn an algorithm
on one class of problems, they generalize a bit outside of that class, but there's
no guarantee the optimizer or RNN learned will outperform human methods on
all problems we care about. It's more likely they'll outperform human
methods near the region they were trained, and they'll decay outside that region.

(That being said, they don't have to outperform existing algorithms on all problems.
They just have to outperform existing methods on the real world problems we care
about.)

(THIS ISN'T EXPLAINED THAT WELL, ADD SOME PICTURES HERE.)

Sometimes, people
describe RNNs as learning algorithms, not functions. Intuitively, algorithms
are methods that update their internal state over time, eventually outputting
an answer. The hidden state of an RNN can be interpreted as an algorithm's
internal state, and the weight matrix can be interpreted as the computation
we apply at each step of the algorithm.


# Conclusion

TODO: Make a conclusion

