---
layout: post
title:  "Deep Learning Philosophy"
date:   2016-01-03 23:14:00 -0700
---

This, unfortunately, is not a post where I apply deep learning to philosophy
texts to see if I can generate new ones. (Although that does sound fun.)

Instead, this is about my feelings on what principles deep learning is founded
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

Lots of people like to describe neural nets as artificial brains. On one hand,
neural nets are definitely biologically inspired, and there's good work to be
done on pursuing them from a neuroscience perspective. However, my brain is
better at the math perspective, which is why I think of neural nets like this.

> Neural nets are a set of differentiable functions that can approximate any
> other function.

Why is differentiability important? If a function is differentiable, we can
find the gradient (the derivative)

What makes neural nets different from previous approaches is that

This is a huge, huge
