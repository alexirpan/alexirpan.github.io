---
layout: post
title:  "Things I Wish Everyone Knew About Debugging"
date:   2018-11-27 03:00:00 -0800
---

Everyone's software development experience is a bit different, and people think
about code in different ways. Here's how I think about it. I think it's a useful
frame to look through, and it's worked well for me, but I'm not going to claim
it's the correct one, especially when I've only been working full-time for a
few years.

\* \* \*
{: .centered }

At its core, software development is about using code to take existing systems
and combine them into new ones. We have a set of tools and libraries available
to use. Programming languages, web frameworks, machine learning libraries, and
others, all implemented in code, all combinable with other things through code.

Inevitably, these systems break down and have bugs. This shouldn't be
surprising. Bugs are the natural state of code, and it's by concerted effort
that they go away.

I get incredibly nitpicky about bugs, where they come from, how to fix them, and
how to reduce the chances they appear in the future. I don't know why I'm like
this, it's just a thing I like doing.

Earlier, I said programming was about using code to connect existing systems
for the goal of creating new systems. This is something that every programmer
has been doing for decades. You're not going to know what all the systems are
doing. You're just not. Eventually, there is some point where you need to
construct a model that assumes this subsystem does what it's supposed to do,
and that's where everything starts going wrong.

**Software bugs happen when your mental model of how the code works differs
from how the code actually works.** There's a good reason that one of the first
lessons in any CS curriculum is that the computer does exactly what it is told
to do and no more - computers will do exactly what the code tells them to do,
and your mental models about the code aren't going to change that.

This has a few important corollaries.

1. If your code has a bug, then your model of how the code works is wrong.
Everyone tries to write working code. If all the code worked the way it should,
then you wouldn't have a bug. So somewhere, at least one piece of code *must*
be working in a different way.

When I write it out, it seems obvious, but it's actually a very foundational
insight, because it means that if you have the bandwidth and time to dig
through the code, then you are eventually guaranteed to find something weird.
You may not be able to *explain* the problem right away, but you'll find it,
because it has to exist. This makes programming reassuring in a way that
research isn't.

2. Blame starts at the code you just wrote. The longer code has sat in a codebase,
the more likely it is to be correct. Roughly, I think of other programmers as
attaching blobs to whatever existing behaviors the current codebase supports.
This implicitly adds several chains of dependencies on the behavior of that
code. The newer your code is, the less implicit testing it's gotten.

(The exception is if you're using old, abandoned code that hasn't been deleted
from the code base, in which case, good luck.)

If you can't find the error in your code, the error may be in the functions
your code calls. If it isn't there, it may be in the functions those functions
call, and so on down. Generally, you want to go breadth-first until you find
something weird (and remember, you *have* to find something weird), then you
go depth-first to understand why it's weird so that you can fix it.

As for how to do this, print statement debugging is surprisingly powerful.
Debuggers are better. I use vim and mostly code in Python for my job and hobby
projects. I have a custom vim command that adds `import pdb; pdb.set_trace()`
to the current location in the file, to fall into the Python debugger when
execution hits that line. I use it all the time for local testing.

Why are debuggers better than print statements? When you add print statements
to code, you print things that you believe will help you solve the issue. But
if your model of the code is wrong, then there's a good chance that you're wrong
about what will solve the issue! Debuggers let you inspect everything about
the current state of the code, including things you didn't know you wanted to
inspect at the time you added the debugger breakpoint.

Print statements are good for small bugs where you have a good idea what the
problem is and simply want to verify. If it starts to look like that isn't true,
favor debuggers.

3. If you find code that relies on a config file, check that config.
In my experience, config files are the source of a *lot* of bugs. They're easy
to add to, and they're supposed to "just work". This leads to a lot of
dead or redundant config options, which disguises which options are critical
and which aren't. The ease of addition makes it easier to implicitly depend
on behavior that the interface isn't supposed to support, making everything
break when the underlying implementation changes in a way that breaks that
implicit behavior.

Ideally, you have snapshots of the exact config used for every job, at the moment
in time it was working and failing. If you don't, then it is worth moving towards
making this available.

Documentation and docstrings should be treated as "trust, but verify". Again,
in my experience, documentation and docstrings are usually correct, because no
one tries to write incorrect documentation. But sometimes, documentation is out
of date, or is incomplete about the behavior you actually care about. They help,
but eventually you'll have to follow the stack trace and read the actual source code.



Case Studies
--------------------------------------------------------------------

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
