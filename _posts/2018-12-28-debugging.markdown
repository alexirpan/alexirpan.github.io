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

If your code has a bug, then your model of how the code works is wrong.
Everyone tries to write working code. If all the code worked the way it should,
then you wouldn't have a bug. So somewhere, at least one piece of code *must*
be working in a different way.

When I write it out, it seems obvious, but it's actually a very foundational
insight, because it means that if you have the bandwidth and time to dig
through the code, then you are eventually guaranteed to find something weird.
You may not be able to *explain* the problem right away, but you'll find it,
because it has to exist. This makes programming reassuring in a way that
research isn't.

Blame starts at the code you just wrote. The longer code has sat in a codebase,
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

If you find code that relies on a config file, check that config.
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

Documentation and docstrings should be treated as "trust, but verify". I feel
one of the biggest reasons I've grown as a programmer is that I have zero
hesitation to jump through horribly long stack traces if I think it'll be
useful. Sure, tracing the genesis of an argument's value is usually a giant pile
of bullshit, where you have to jump through five or ten functions before you
find the one that actually matters, but I don't think you can do software
engineering unless you're willing to dive into bullshit.

Because of this, the more time I've spent on a bug, the less I trust the
existing documentation. Again, remember that code is either written by
programmers, or by a tool that programmer wrote, and in either case, no one
deliberately tries to write incorrect code (except in unit testing). For the
same reasons, no one deliberately tries to write incorrect documentation. In
practice, documentation is wrong because

* It was written in the past, the code has changed, and the documentation was
not changed to match.
* The documentation only correct documents some of the behavior, and your error
traces to undocumented behavior.

In either case, there is no remedy besides opening the source code and verifying
the logic for yourself.

I use Python in my day-to-day and have no idea how to do anything without
rampant `pdb.set_trace()` calls (to enter the Python debugger), `class()` calls
(to get the class name of an object for code searching), and `dir()` calls
(to list all attribute names to see if any of them exist.)

Or maybe it's correct, but isn't correct at a high enough level of
granularity. There's a Fog Creek post about this (FIND THE QUOTE)



Case Studies
--------------------------------------------------------------------

In college, I was working on a class project for Operating Systems. One part of
the project was to implement a ThreadPool. We weren't told we couldn't use
existing libraries, and scoring of the project was done exclusively on how many
unit tests we passed, so we found a built-in ThreadPool and used that.

We later hit an incredibly strange bug where threads were getting removed from
our ThreadPool when they weren't supposed to be removed. The given unit test
spawned several threads that would run forever, added them to the ThreadPool,
then verified a newly added thread would not run. Except, it did.

I went to TA office hours to get help on debugging it, but the TA couldn't
figure it out. I was so stuck that I spent those office hours helping another
group debug their project (which I did succeed at, but it didn't fix *my*
problem).

The error eventually traced to the built-in ThreadPool - on reading its
documentation, it had some smart logic to auto-evict threads that were known to
do nothing.

Principles here:

* The requested project spec for the ThreadPool did not mention the behavior
  that the final unit test relied on. Looking at the unit test code was the
  only way to discover this.
* The error was either in the custom Thread class, or the ThreadPool class.
  The reason this bug was hard to find was because the ThreadPool was very, very
  likely to be correct - it's part of the standard library! It's only after
  exhausting the Thread logic that it makes sense to inspect the ThreadPool's
  behavior. But, it made sense to inspect the standard library, because
  something had to be wrong, and that something was likely in the ThreadPool.

\* \* \*
{: .centered }

As part of a paper I'm working on, I'm running distributed evaluation of
several agents trained with reinforcement learning in a differing environments.
The exact details of training don't matter for this bug, because this bug has
nothing to do with the training process/

The environments we're using are a bit slow, so evaluation is done in a
distributed manner. Roughly, it works like so. Each evaluation has 1
coordinator and 100 evaluators. Whenever an evaluator finishes an episode, it
emits "Done, reward = $$R$$" to the coordinator. The coordinator reports the
running average of all messages its received so far.

DIAGRAM

We were finding that a few of our training algorithms had almost exactly the
same performance across our different evaluation setups. This was good, it
meant our learning algorithms were correctly generalizing across environments.
But, as
it meants we

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
