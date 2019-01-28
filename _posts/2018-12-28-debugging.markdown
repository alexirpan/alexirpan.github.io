---
layout: post
title:  "Sometimes You Have to Dive Into Bullshit"
date:   2018-11-27 03:00:00 -0800
---

I'd like to think I'm a good software engineer, or at least an okay one.
That's not to say I'm good at all parts of the job. There's a lot more to
software engineering than just coding.

Of all parts of software engineering, I only let myself take pride in one
aspect: debugging. Historically, my track record for this is pretty good.

In college, I was working on a class project for Operating Systems. Ostensibly,
this was a group project, but in practice I was basically doing it solo. There
was a very strange bug in my code, so I went to TA office hours to get help.
This was one of the final office hours before the project deadline, so we had to
wait in line to talk to the TA.
While waiting for my turn, I talked with a group that just finished talking to
the TA. The TA didn't figure out the problem, and since I was stuck anyways, I
offered to take a look. I ended up finding the exact line where it all
unravelled. I then showed my project to the TA, who also couldn't figure it out,
and so I left having fixed someone else's bug.

\* \* \*
{: .centered }

I don't have 

When debugging, my biggest strength is that I have literally no hesitation
at chasing code all the way down the call stack.

Oh, the argument for this function is passthroughed five functions before
it hits the function that errors? No problem - let's trace the whole chain.
Tracing that chain is usually a giant pile of bullshit, but I don't think
you can do software engineering unless you're willing to dive into bullshit.
I use Python in my day-to-day and have no idea how to do anything without
rampant `pdb.set_trace()` calls (to enter the Python debugger), `class()` calls
(to get the class name of an object for code searching), and `dir()` calls
(to list all attribute names to see if any of them exist.)

hesitations to chase the rabbit all the way down the hole of call stacks.
Just, none at all. I'll jump through ten functions scattered across
four files to see how a value gets propogated everywhere else, and doing
this will be a complete mess, but I'll just do it. Part of this is just
curiousity about how everything goes from point A to point B, but I feel
this is actually the core of debugging.

**Software bugs happen when your mental model of how the code works
is different from how the code actually works.** Maybe your model is wrong.
Or maybe it's correct, but isn't correct at a high enough level of
granularity. There's a Fog Creek post about this (FIND THE QUOTE)


and basically what this means is that if you can't find the issue at your
current level of abstraction, then you need to go deeper.

Here's a fun bug I found recently. As part of a paper I'm working on,
I'm running distributed evaluation of several agents trained with RL
in differing environments. In


I'll strip the details to make it
easier to explain. As part of a subroutine in a larger ML setup, we're
doing black-box optimization using the cross-entropy method. We have
4 parameters: X, Y, Z, and rotation. We noticed that the discovered solution
would often use a very small rotation of just a few degrees, even in
situations where a larger rotation looked better.

Now part of the difficulty here is that CEM is an approximate method and
we're combining this with optimizing the output of a deep neural net, so
there's all sorts of potential uncertainty. Maybe the network hasn't
learned that rotation is good. Maybe CEM is doing a poor job at
maximizing the function.

To debug this



The other aspect of debugging is mostly about noticing when things are
weird, and trying to figure out why.
