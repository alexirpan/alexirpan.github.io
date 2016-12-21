---
layout: post
title:  "Deep Learning Philosophy"
date:   2016-01-03 23:14:00 -0700
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

* Generative models based on deep learning
* Make everything differentiable. (Neural net analogues of existing methods)
* Ways to prevent gradient vanishing/exploding.
* Apply neural nets to problems in the field you care about.
* Predictive models
* ???
* (Trying to focus this on neural nets in particular, not on applications to
specific fields.)

\* \* \*
{: .centered }

(Also rewrite this intro, it's shit.)

This post is my feelings on what principles deep learning is founded
on, how the field works, why people do research in the field and how, broad
topics in the field I find interesting, and future research directions that
look promising.

Target audience: someone with math background up through calculus.
That someone wants a high level overview of deep learning,
or is a researcher interested in seeing how other fields operate, or
a current deep learning researcher interested in seeing
new perspectives.
If I've done my job well, all those people should get something out this.

This post is technical, but it is **not** intended to be a tutorial
in deep learning. A ton of people have written much better tutorials than
I can, and I'd like to focus on motivations and, well, philosophy.

This post won't be very lyrical. I'm aiming for a brisk, dense pace.

What is Deep Learning?
-------------------------------------------------------------------------

Deep learning is a rapidly growing subfield of machine learning, that focuses
on applying deep neural networks to various problems, and on creating new
neural net architectures that could solve problems that were previously
out of reach.

Before going further, I need to unpack this a bit.

What is Machine Learning?
============================================================================

I wrote an answer for this in a previous blog post.

> Machine learning is the study of algorithms that let a computer learn insights from data in a semi-autonomous way.

But now, I have a different answer.

> Machine learning is the study of algorithms that learn functions from one
> type of data to another.

Suppose we had a set of points in the 2D plane, and wanted to fit a trendline that best
fits the data. We can use linear regression.
Linear regression takes a set of points, and outputs another function, which
is guaranteed to be a line, and which is guaranteed to be the best line
(according to the least squares metric.)

Image of points in a plane

Algorithm: linear regression.
What gets learned: a linear function.
Function's input: the x-coordinate
Functions's output: the y-coordinate.


Suppose the points were in 3D space instead. We can still use linear regression,
because in ML, linear doesn't mean "forms a line". It means "given $$d$$-dimensional
data, output a $$(d-1)$$-dimensional hyperplane." In 3D space, linear regerssion
gives a 2D plane. In 4D space, it gives a 3D plane. And so on.

Image of points in 3D space.

Algotihm: linear regression
What gets learned: a plane

Points in 3D space suck. Who cares about 3D points? Let's jump to pictures.
Say we really, really cared about corgis, and wanted to filter our album to
only pictures of corgis. (They're adorable. This is a totally valid request.)

Image of a corgi

A human can do this easily, classifying images as "has a corgi" and "doesn't
have a corgi". But we have a lot of photos, and want to do this automatically.
We want a function $$f$$ such that $$f(corgi) = YES$$ and $$f(not corgi = NO$$ (use pictures here.)

Suppose we had some English sentences, and wanted to translate them into
Spanish. We want a function $$f$$ such that $$f(How are you?) = TRANSLATION.$$
Now we're getting toward problems where there could be several valid outputs,
meaning several valid functions, but that's a detail we'll worry about later.

We have a gallery of images, and want to describe their content for the blind.
This is the image captioning problem, and Facebook cares about it for
accessbility reasons. In that case, the function could be $$f(picture of dog) = A dog in a field is jumping to catch a ball."

We have a design specification of an algorithm, and want to produce code that
implements that algorithm. The function is $$f(design doc text) = working implementation
in your favorite programming language.$$

Everything's functions in the end, and some are easier to learn than others.
The goal of ML research is to expand the set of functions
we can expect a computer to learn. We can (kind of) do image captioning.
Learning a line is easy. Learning a corgi/not-corgi classifer isn't too hard
if you have enough pictures of corgis and pictures of not-corgis (which is
already a big advancement that hides a ton of research effort). Image
captioning is still tricky, but it's getting there at a good pace. Text to
working code is very, very far off.

What Are Neural Nets?
============================================================================

(Try to work in the classical description of neural nets here.)

Lots of people like to describe neural nets as artificial brains. On one hand,
neural nets are definitely biologically inspired, and there's good work to be
done on pursuing them from a neuroscience perspective. On the other hand,
I think this is deceptive. Not because it doesn't have ground, but because
it's been repeated over and over in popular science, and the cavaets on the
original claim have been lost over time.

I prefer a math perspective, because I have more experience with math than
neuroscience.

> Neural nets are a family of differentiable functions that apply multiple
> layers of computation. Each layer applies a linear function, then a nonlinear
> activation.

What's So Special About That? (The Theoretical View)
============================================================================

Neural nets have a neat property - they're universal function approximators.
More formally, given any function $$f(x)$$, a sufficiently large neural net
with the right parameters can match $$f(x)$$ at all $$x$$ to arbitrary precision. And they can do this
while still being differentiable.

Why is differentiability important? If a function is differentiable, we can
find the gradient (the derivative) of the function at any point. In machine
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

(Find the old article about Brain.) This is why it's possible to unify researchers
all across machine learning under the banner of neural nets.
