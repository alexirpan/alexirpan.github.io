---
layout: post
title:  "Sometimes You Have to Dive Into Bullshit"
date:   2018-11-27 03:00:00 -0800
---

I'd like to think I'm a good software engineer. Is that actually true?

Well, I'm not sure. There are a few points in favor. It's tricky for
me to judge whether I'm overestimating from Dunning-Kruger or underestimating
from imposter syndrome. I'm employed at a Big Tech Company, which is a plus.
I haven't been coding for particularly long, which is a minus. Maybe you
think young people are better at programming - I disagree. This isn't
even getting into the aspects of good software engineering. There's more
to it than just programming, and it's not like I'm good at all of it.

There is one exception where I let myself take pride, and that's
debugging. Here's a short story that was painful before but funny now:
I was working on a class project for Operating Systems. This was
ostensibly a group project, but our group dynamic was dysfunctional and
I was basically doing it solo. I was stuck, so I went to TA office hours
to see if they could help me fix a bug.

This was one of the final office hours before the project deadline, so
there were a bunch of people, and we had to wait in turns to talk to the
TA.

While waiting for my turn, I talked with a group that just finished their
turn. The TA didn't figure out their issue, and since I had time to kill,
I offered to take a look. I ended up finding the bug and explained
what they had to fix.

When it was my turn, I showed my code to the TA. They didn't get the bug either!
So I left.

That's the story of how I came in with a bug, fixed someone else's bug, and
left with the same bug, which I ended up figuring out an hour before the
deadline.

\* \* \*
{: .centered }

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
