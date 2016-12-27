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
* Predictive models
* ???
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

What is Machine Learning?
============================================================================

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

What is Deep Learning?
-------------------------------------------------------------------------

Deep learning is a rapidly growing subfield of machine learning that focuses
on applying and developing neural networks.


What Are Neural Networks?
============================================================================

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

What Makes Neural Nets Special? (The Theoretical View)
----------------------------------------------------------------------------

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

However, this says nothing about how to actually 

Why is differentiability important? The dirty secret of machine learning is
that 90% of it is glorified optimization and gradient descent.
Machine learning algorithms can be divided into parametric and nonparametric
models.
and non-parametrized models. 
In machine
learning, we pick/define a type of function (linear, neural net, etc), which
is *parametrized* in some way, and our goal is to learn the parameters.

Equation of line with arrow pointing to parameters w and b

The dirty secret of machine learning is that everything eventually turns
into gradient descent. If we have a parametrized differentiable function,
and want to minimize it over a dataset $$X$$, there are 2 components to
the loss - the data and the parameters. Taking the partial derivative
with respect to the parameters gives a parameter update - the direction
in which to move the parameters to decrease the value of the function.

Classical parameter descent picture.



Neural nets have a neat property - they're universal function approximators.
More formally, given any function $$f(x)$$, a sufficiently large neural net
with the right parameters can match $$f(x)$$ at all $$x$$ to arbitrary precision. And they can do this
while still being differentiable.

There are non-parametric methods like nearest neighbor which are not
differentiable, and are therefore learned in a different way. They tend
to work well with very little data, but don't generalize as well as
data size grows. (But they will be important - keep them in mind.)

Now, let's go back to the original claim.

> Neural nets are a set of differentiable functions that can approximate any
> other function.

This lets us compute parameter updates over arbitrary datasets, as long
as we have an appropriate loss to minimize. Now, note the part in bold.

> Neural nets are a set of differentiable functions **that can approximate any
> other function.**

What are we trying to do in machine learning? We're trying to learn
functions. And neural nets can represent any possible function, and they're
differentiable, meaning we know how to train neural nets from scratch.

This is a big part of the recent hype, where people try neural nets on
literally every dataset they can think of. They do this because neural nets
actually can be applied on all those datasets.

What's So Special About That? (The Practical View)
===========================================================================

Here's the real truth: most people don't care about universal approximation.
Hell, I don't even know any statistical learning theory people who care
about universal approximation. It's neat to know it's possible, but generally
they care about convergence rates or regret in online learning.

It's nice to know that a sufficiently big neural net with the right parameters
can approximate any function. But that doesn't actually matter in practice.
What matters in practice is how well the neural net fits the data, and that's
where they shine.

Here is the classical picture from every talk Andrew Ng ever does about
deep learning.

PICTURE

In words: although other machine learning methods perform well with less
data, at a certain data threshold a neural net approach outperforms every
other method we have.

There's a tradeoff between model complexity and data efficiency.
More complex models can solve harder problems, but they also need more data
to train. Neural nets are squarely on the more complex side.

By itself, this still doesn't answer the question to my satisfication.
There will always be a state-of-the-art approach that performs the best
given enough data. At one point it was support vector machines. At another
point it was random forests. (Random forests are still alive and kicking,
by the way. I hear they're very popular on Kaggle.)

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

This **still** doesn't explain the picture. Humans still have influence over
how easy the model is to optimize. All we're doing is trading in expert
feature desiging for expert neural net architecture design.

**What makes neural nets different is that architecture design is significantly
easier and more general than feature design.** (Karpathy's slide)

IMAGE from Karpathy's slide from DLSS

Additionally, because neural nets are applicable to so many domains, it's much
easier for people across different subfields to share ideas. Computer vision
people use convolutional nets, and NLP people use LSTMS, but they're all still
neural nets, and that means a lot of latent intuition and knowledge is usable
across domains. And because different fields are sharing more techniques,
advances in one field can give ideas for advances in other fields.

Across several fields, we're starting to see a unification of methods, and I
think that's why progress has grown so quickly - people who used to do
computer vision can talk to someone in NLP, find out their using an attention
mechanism, and can try applying it to problems in computer vision. This would have
been ridiculous before deep learning proved itself.

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

Research Culture
------------------------------------------------------------------

The field moves very, very quickly.

Take Tensorflow for example. It turned 1 year old today. But the way people
talk about it, you'd think it was around forever. It's very quickly jumped to
one of the big machine learning frameworks.

Or consider ADAM. ADAM is an optimization algorithm that combines momentum
with adaptive learning rates (LOOK THIS UP.) The paper for ADAM came out in 2014.
It's since been implemented in Tensorflow and Torch, and it's the default
optimization algorithm to try.

Dropout has wide adoption. Batch normalization came out in early 2015. In just
under 2 years it's become widespread across image models, and has spawned two
followups, layer norm and weight norm.

I haven't done research in other fields, but I'm pretty sure this pace of
research is atypical. There are **a lot** of people doing machine learning
research right now, and because the cultural norm is putting papers on
arXiv, ideas spread very quickly. There's an understanding that open research
is good for the field. Many papers come with a source code release. In my experience,
when a paper doesn't come out with source code, it doesn't mean the authors
didn't want to release their code, it means the authors don't have time to
clean up their code for open release. (This happens distressingly often.)

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

Benchmark Standardization
========================================================================

People care a lot about open-sourced datasets. There are good reasons for this.

* A common dataset lets researchers agree on the exact nature of the problem. (idk if I like this)
* Working from a well-known dataset removes external variables.
* Building a large dataset can be costly because it requires human labels. If
datasets aren't standardized, each research group has to spend time recreating
their dataset, which slows down progress.


Research Directions
--------------------------------------------------------------------------

"Throw a Neural Net, See If It Works"
=========================================================================

Sometimes, throwing a neural net at the problem just makes it work out.

This kind of research happens in domains where people haven't tried using
neural nets before. For example, computational biology for gene sequencing,
or medical imaging.

In these domains, the neural net uses standard techniques. Most of the work
is in collecting a large, clean dataset. These are domains where people
have very high confidence the neural net will solve the problem, once you
get all the plumbing out of the way.

(Need to fit in the Andrew Ng quote here.)

"To Use Neural Nets on the Problem, We'll Need Some Cleverness"
======================================================================

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

Neural Nets for Their Own Sake
=========================================================================

Research in this area focuses entirely on extending our understanding of
neural nets and extending the problems that neural nets could be applied to.

Theoretical Justification for Neural Nets
----------------------------------------------------------------------------

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

Interpretability of Neural Nets
-----------------------------------------------------------------------------

This research explores ways to inspect neural nets to better understand how
they arrive at their final output. The most notable example is DeepDream.

IMAGES

It almost feels wrong to call this a research area, because I don't know of
anybody whose primary research focus is interpreting neural nets.
However, many papers include visualizations anyways, because it makes the
paper stronger.


Duplicating Neuroscience
-----------------------------------------------------------------------------

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

Make ALL The Things Differentiable!
-----------------------------------------------------------------------------

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

Meta-Learning
------------------------------------------------------------------------------

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


Conclusion
================================================================================

TODO: Make a conclusion

