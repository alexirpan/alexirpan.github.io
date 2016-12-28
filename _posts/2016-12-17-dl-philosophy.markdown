---
layout: post
title:  "Deep Learning Philosophy"
date:   2016-12-22 22:14:00 -0700
---

OUTLINE

INTRODUCTION

* Define what deep learning is
* Introduce machine learning as a field of learning functions

WHY ARE NEURAL NETS A BIG DEAL?

* Emphasize that neural nets are best thought of as a very expressive
family of functions
* Emphasize that they actually work, and how important this is.
* Emphasize they can be thought of as modular computation blocks,
* Unification of methods means expertise transfers easily - it makes
sense for CV people to sit next to NLP people and robotics people.

FIELD AXIOMS

* Given enough data and a large enough neural net, you can train the
neural net to solve the problem.
* Neural nets can be treated as computation blocks that will learn
the proper behavior (if tuned well)
* (Emphasize abstraction barriers in the above.)
* Given enough data, end-to-end architecture will perform best.
* Neural nets aren't the answer to everything, but they're the answer to
many things.
* We have not hit the limits of neural nets (yet).

CULTURE

* Conferences are the key venues. Workshops are okay too. The rest don't matter as much.
* but arXiv is perfectly acceptable for publication
* The field moves very, very fast - something can be old news within a few months.
* Open research is better for the field - if you want people to use your work,
don't make them reproduce it first.
* Standardizing on benchmarks is good for progress.

RESEARCH DIRECTIONS

* Generative models based on deep learning (this is getting bundled into applications)
* Make everything differentiable. (Neural net analogues of existing methods)
* Ways to prevent gradient vanishing/exploding.
* Apply neural nets to problems in the field you care about.
* (Trying to focus this on neural nets in particular, not on applications to
specific fields.)

Make sure to add a table of contents!

\* \* \*
{: .centered }

Summary: This post collects various thoughts I've had about deep learning.
It gives a justification for why deep learning is such a big deal,
then broadly classifies research in the field into a few buckets.

This is **not** intended to be a tutorial in deep learning. There are a ton
of those already - see LINKS HERE. However, it will be somewhat technical.
I won't do proofs, but I won't be afriad to drop a little bit of math.

# Table of Contents

- Clobbered for auto generated table of contents
{:toc}

# Background

## What is Machine Learning?

I can't explain deep learning if I don't explain what machine learning is.

(Note: if you know what features and classification are, you can skip this
section.)

Here's a definition from a previous blog post, which is a paraphrase of
Wikipedia's description.

> Machine learning is the study of algorithms that let a computer learn insights from data in a semi-autonomous way.

This definition is valid, but I'll phrase it in a different way.

> Machine learning is the study of algorithms that learn functions between
> two sets of data.

In basically every machine learning problem, we have examples of desired
inputs and desired outputs. Using those examples, we want to train a function
to map from those inputs to those outputs. After training is done, we evaluate
that function on new inputs to get a guess/approximation of the true output.

Or in short: every problem in ML is a function learning problem, because every
problem's solution can be described as a function.

Examples!

Suppose we had a set of points in the 2D plane, and wanted to fit a trendline that best
fits the data. We can use linear regression.

Image of points in a plane

Input set: The x-coordinates of each point.  
Output set: The y-coordinate of each point.  
Algorithm: Linear regression.  
Function learned: a $$f(x)$$ of the form $$f(x) = ax + b$$ such that for every $$(x, y)$$, $$y$$ is close to
$$f(x)$$. (To be precise, linear regression minimizes $$\sum (x,y) (y - f(x))^2$$)

Suppose the points were in 3D space instead. We can still use linear regression.
The "linear" in linear regression doesn't mean "forms a line", it's meant in
the mathematical sense of the word.

Image of points in 3D space.

Input set: The (x,y)-coordinates of each point.  
Output set: The z-coordinate of each point.  
Algorithm: Linear regression.  
Function learned: a $$f(x,y)$$ of the form $$f(x, y) = ax + by + c$$
such that for every $$(x, y, z)$$, the sum
$$\sum (x,y,z) (z - f(x,y))^2$$ is minimized.

In general, when our input set is $$d$$-dimensional data, we say the data has
$$d$$ **features**.

Points in 3D space are boring. Who cares about those? Let's jump to image data.
Say we're really, really big fans of corgis. (They're adorable. This is a
totally valid opinion.) We're such a big fan that we want to automatically
filter our album of photos to only the photos with corgis in them.

Image of a corgi

This is the textbook image classification problem. Each image falls into
two classes, "contains corgis" and "doesn't contain corgis".

Input set: A collection of images.  
Output set: A prediction of corginess for each image.  
Algorithm: Something from computer vision. In the past, HOG features + support
vector machines. Now, a convolutional neural net.  
Function learned: A function $$f$$ such that $$f(corgi photo) = corgis$$
and $$f(not corgi) = NO$$

PICTURE HERE

Suppose we had some English sentences, and wanted to translate them into
Spanish. This problem differs from the previous one, because there could be
several valid translations.

Input set: A colleciton of English sentences.  
Output set: A translation of each sentence into Spanish.  
Algorithm: Something from natural language processing. Nowadays, that
means a big recurrent neural net or LSTM.  
Function learned: $$f(ENGLISH SENTENCE) = TRANSLATION$$

The image captioning problem. Given an image, generate a description of
that image. (This is important for the blind and visually impaired -
Facebook cares about this quite a bit.)

PICTURE FROM KARPATHY'S PAPER

The leading approach uses a combination of convnets and RNNs.

The programming problem. We have a nautral language description of what
the program should do, and we want to produce code that implements that algorithm.

PICTURE

Right now, the best approach is "hire a team of software engineers". No one
knows how to do this through machine learning. At least, not yet.

\* \* \*
{: .centered }

## What is Deep Learning?

Deep learning is a rapidly growing subfield of machine learning that focuses
on applying and developing neural networks.

### What Are Neural Networks?

Here is the common description.

We can model a neuron in the brain as a unit that activates depending on
what input it receives. Neural nets connect several of these artificial
neurons into a block of compute that can be learned from data.

PICTURE of perceptron and neural net

Neural nets are definitely biologically inspired. But I think the narrative
of neural nets as artificial brains is too big in popular science.
Anthropomorphizing neural nets and explaining what they aim to be is
much easier than explaining what they actually are.

> Neural nets are a particularly useful differentiable family of functions.
> They apply multiple layers of computation, each of which applies a linear
> function, then a nonlinear activation.

I heavily, heavily prefer this viewpoint. But I'm a math person, not a
neuroscience person, so my bias should be obvious.

(For emphasis: describing neural nets as artifical brains isn't *wrong*,
but it heavily underplays how crude the approximation is. Not even the
neuroscience researchers in deep learning would claim neural nets
replicate the brain. In fact, that's why they're interested in the field;
they want to push in that direction.)

# What Makes Neural Nets Special?

## The Theoretical View

Neural nets are differentiable universal function approximators.

A family of functions $$F$$ is a universal approximator if for any continuous
function
$$f$$, there is an $$f' \in F$$ that's close to $$f$$ at every point
(for any $$\epsilon > 0$$, there exists an $$f' \in F$$ such that
$$|f(x) - f'(x)| < \epsilon$$ for all $$x$$)

(Technically the proof only holds when the domain is a compact subset
of the reals, but it's not a big detail.)

Recall that machine learning is all about learning the right function.
Universal approximation tells in principle, it's always possible to learn
a neural net for that function.

However, this doesn't tell us how to find an appropriate neural net.
This is where differentiablity comes in.
The dirty secret of machine learning is that 90% of it reduces to gradient
descent on some loss function.

* Define a loss function $$\ell_\theta(x,y)$$, where $$\theta$$ is the parameters
and $$x$$ is the input and $$y$$ is the desired output.
* Find $$\nabla_\theta \ell_\theta(x, y)$$, the gradient with respect to $$\theta$$.
The gradient is the direction of steepest descent for the loss function.
* Apply an update rule to move $$\theta$$ to $$\theta'$$, and repeat.

Differentiability is key in the 2nd step. The core idea is that if the function
is differentiable, we can always find a good update direction, and because we're
optimizing over a continuous range, we can take arbitrarily small steps in that direction.

Classical parameter descent picture.

(Not all ML reduces to this. Nearest neighbor and random forests are two big
methods with non-differentiable components.)

The takeaway from this entire transgression is that differentiability gives
us a way to search parameter space ($$\theta$$-space) towards regions with
smaller losses. As long as the loss is differentiable and minimized when $$f_\theta$$
is what we want, we're set.

Therefore, the combination of differentiabilty and universal approximation makes
neural nets applicable to any problem.


## The Practical View

Now here's the real truth: most people don't care about universal approximation.

Oh, sure, it's nice that the result holds up, but all the proof of universal
approximation shows is that neural nets can represent a lookup table. Constructing
a neural net the way the theorem tells you to will very quickly require more computing
power than the entire world has.

In practice, neural nets don't use all the compute power in the world. (Citation
needed.)
What matters is how well neural nets fit the data, and that's
where they shine.

Here is the classical picture from every talk Andrew Ng ever does about
deep learning.

PICTURE

The pattern so far is that above a certain data threshold, neural net approaches
outperform every other approach. Which is weirdly fascinating, when you think about it.
This claim is almost an axiom in the deep learning community; the only counterexamples
I know of are pathological ones.

When you have a hammer, everything looks like a nail. And so far, neural nets are
a big hammer that turns a ton of problems into nails.


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

Also, there are a ton of people in the field, Cultural norm is to publish on
arXiv, submit to conferences over journals, publish your conference submission
on arXiv as soon as you're allowed to, publish often,
and release source code if you have the time to clean it up.
This is great for sharing ideas, but it pushes researchers to put their work
out early. That doesn't lead to well-written papers that flip your research
worldview. It leads to papers that are obvious to your world view. Of course,
researchers understand that the paper hides all the work that went into it,
because they've been busy trying to get their own papers to work.

So yes, it is all very open, and the ideas are often very simple. But getting
things to work at all (and work well) is a big enough achievement to overshadow
the simplicity of the explanation. (Besides, simple explanations should be
rewarded. The best papers are ones where you wonder why you didn't think of
it first.)

## Why is Deep Learning Progressing So Fast?

I've made a big show of explaining how quickly the field moves. But why is
deep learning in particular growing so fast, compared to other subfields in
machine learning?

There isn't a single answer. It's more like a collection of answers.

### Resurrecting Old Ideas With Big Data

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

### Financial Incentives

Image recognition, speech transcription, machine translation, and other areas
have become so good that they're practical enough for companies to care
about the research. There's a ton of money in machine learning, so companies
are throwing a lot of funding at machine learning researchers in industry
research labs, which speeds up progress.


### Avoiding Feature Engineering

Here is the other diagram people always bring up in deep learning.

FEATURE ENGINEERING PICTURE

Traditionally, when people have wanted to apply machine learning to a problem,
they take the raw data and create *features* of the data. These are human-designed
heuristics of what's important about the data. For example, in spam detection,
the raw text is the original email text, and your features could be the number of
typos, relative word frequency, etc. This transforms the data into what experts
think is important. A function is then fit to the transformed data.

The feature engineering step is needed because many machine learning
methods often aren't expressive enough to work with the raw data. Well, to be more
exact, they sometimes do - but they don't do so often enough.

Neural nets seem to get around this issue - in more domains than previous methods,
they get better performance without feature engineering.

DEEP LEARNING PICTURE

Once again, this is true, but I feel it still misses something. You can think
of features as biases humans place on what the model should optimize over.
That human bias is still present in neural nets, but it gets offset to the
neural net architecture chosen for the problem. Convolutional nets are
good at translation invariant patterns, RNNs are good for sequential data,
dropout is good if you want better regularization of the model, and so on.
These choices are made before training begins, just like feature engineering.
All we've done is trade expert feature design for expert neural net
architecture design.

This leads to th next points.


### Simplicity/Unification

(Note: planning to make this just unification, and moving the simplicity
part to the previous heading.)

**What makes neural nets different is that architecture design is easier and
more general than feature design.**

Credit goes to Andrej Karpathy for putting these thoughts into words, because
when I read them the first time, a ton of incomplete ideas I had clicked into place.

Consider computer vision. Compared to what people did before, describing
convnets is easy! Throw some conv layers together, add some pooling and
fully connected layers to glue it all together, and done.

IMAGE from Karpathy's slide from DLSS

Similarly, there used to be a ton of linguistics-specific knowledge in machine
translation. Recent papers suggest that word embeddings and large LSTMs let
you sidestep all of that knowledge.

Across several fields, we're starting to see a unification of methods. Convnets
are good at pattern recognition, which is good for computer vision, but it's also
good for Computer Go. RNNs are good at sequential data, which is good for
language models, but it's also good for reinforcement learning, and even image
generation if you view image generation as a sequence of pixel outputs. (Link PixelRNN here.)

They're all unifed under the banner of neural nets. It made sense for Google to
throw all their neural net researchers onto one team, even if they were working on
different problems, because they all knew how to talk about neural nets. And
even if they weren't directly related, sometimes an idea from one domain can
spark an idea in another. Everything's connected, through the neural net
bridge.

PICTURE

Progress in one domain pushes progress in the others. You could see this as
neural nets rising, and pulling everything along with it. But I see it the other
way around: everything is rising, and neural nets are along for the ride.

PICTURE

(I want to make some point about neural net knowledge becoming more important than
domain specific knowledge but I can't get the phrasing right so screw it.)

### The Standardized Benchmarks
Benchmark Standardization
========================================================================

People care a lot about open-sourced datasets. There are good reasons for this.

* A common dataset lets researchers agree on the exact nature of the problem. (idk if I like this)
* Working from a well-known dataset removes external variables.
* Building a large dataset can be costly because it requires human labels. If
datasets aren't standardized, each research group has to spend time recreating
their dataset, which slows down progress.


Neural Nets as Computation Blocks
================================================================

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

FOOOOOOO

The field is also very, very experimentalist. Deep learning has found its
biggest niche in applications, and in applied problems, you care about
final performance first and why it works second. Or to be more precise: in
applied problems you only care about why it works because it lets you try
new ideas in a more principled way, so even fuzzy inprecise explanations
with empirical evidence in their favor is good enough.

This makes deep learning deeply unsatisfying for theoretically oriented people.
Some people are working on theoretical explanations for why deep learning
should work, but we're not there yet.

This can also make the field appear shallower than it really is. Ideas are cheap,
execution is hard. Many papers in deep learning have fairly natural extensions,
and in other fields authors may spend the time exploring those extensions very
carefully. But because there are so many authors, and because everyone procrastinates,
researchers often run out of time to implement and hyperparam tune those
extensions. There's a strong bias to release early. Submissions bunch up around
conference deadlines, but arXiv papers are perfectly acceptable too.


# Research Directions

## "Throw a Neural Net, See If It Works"

Sometimes, throwing a neural net at the problem just makes it work out.

This kind of research happens in domains where people haven't tried using
neural nets before. For example, computational biology for gene sequencing,
or medical imaging.

In these domains, the neural net uses standard techniques. Most of the work
is in collecting a large, clean dataset. These are domains where people
have very high confidence the neural net will solve the problem, once you
get all the plumbing out of the way.

(Need to fit in the Andrew Ng quote here.)

## "To Use Neural Nets on the Problem, We'll Need Some Cleverness"

In these domains, applying known neural net methods won't improve performance, usually because
people have already applied known methods to get the current state of the art.
Prime examples are image classification, speech recognition, machine translation,
and my personal favorite of reinforcement learning.

People in these domains aren't interested in neural nets for the sake of
neural nets. They're interested in neural nets for the sake of solving their
problem better. Better translation, better image segmentation, etc. If you gave
these researchers a black box method that worked better, but didn't use neural
nets, they would switch to that method without much regret.

That doesn't mean they're not interested in developing neural net architectures.
It just means they're embedded into the feedback loop of research. In our
specific problem, current neural net architectures are lacking. So we develop
new ones that solve the issues we've noticed. Those architectural ideas go upstream,
and can get used in other fields.

PUT A PICTURE EXPLANING THIS HERE

ImageNet led to the development of highway networks and residual networks.
Language problems led to bidirectional RNNs. Audio generation led to WaveNet.

## Neural Nets for Their Own Sake

Research in this area focuses entirely on extending our understanding of
neural nets and extending the problems that neural nets could be applied to.

### Theoretical Justification for Neural Nets

This research focuses on devising theoretical explanations for the power of neural
nets. This work is entirely about devising theories that fit existing
empirical evidence; it isn't directly applicable to current problems of the day.

(That's not a knock against the research. Pretty much every science has gone
through something similar, and theory always lags behind practice. (LINK HERE).)

Some results from this area: a proof that there are functions whose appoximations
require an exponentially large 1 hidden layer neural net, but only a polynomially
large deep neural net. Works that try to link algebraic topology to deep learning.
A view of neural nets through a spin glass model, which I don't understand very
well. An argument that models with history are required for sequence data, based
on an information theory argument between symbols in the sequence.

### Interpretability of Neural Nets

This research explores ways to inspect neural nets to better understand how
they arrive at their final output. The most notable example is DeepDream.

IMAGES

It almost feels wrong to call this a research area, because I don't know of
anybody whose primary research focus is interpreting neural nets.
However, many papers include visualizations anyways, because it makes the
paper stronger.


### Duplicating Neuroscience

Let me go on a tangent for a bit.

I don't like it when people explain neural nets as approximating neurons in
the brain. At a very approximate level, it's true, but every time a researcher
talks about neuroscience inspiration, ten spectators of the research walk away
with inflated misconceptions.

That being said, neural nets have undeniable influence from neuroscience, and
several researchers in the field have neuroscience background. At the Brains & Bits
workshop at NIPS this year, Demis Hassabis had a succinct justification. We
know the brain works for intelligence. If we can understand the brain and
reproduce it in software, it's guaranteed to work. 5 year or 10 year projects
based on neuroscience are easier to justify.

I'm less familiar with this due to my biases, but I'll list some work.

* Feedback alignment (a more biologically plausible backprop)
* Energy based models (ML algorithm that could run better on analog hardware)
* Count-based exploration (can be motivated by the hippocampus)
* Modulated locomotor controllers (a fast reflex "spinal cord" and slower LOOK UP THE PAPER)

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

