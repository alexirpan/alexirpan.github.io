---
layout: post
title:  "Asking The Right Questions"
date:   2016-11-06 01:35:00 -0700
---

This is the story of how I didn't get publishable results in time for a
Nov 8th NIPS workshop deadline. Astute readers will note that deadline is
two days from now, but I'm very confident it isn't happening.

It'll be very light on details. One, I'm trying to target a broader audience.
Two, I do need to be somewhat confidential
about what I'm working on. Most importantly, three: the details
don't matter.

\*\*\*
{: .centered }

I first had my research idea in late September.

I was (and still am) generally interested in reinforcement learning, and more
specifically ways to make RL more sample efficient. There were some research
threads I was keeping an eye on, and it felt like I was on the cusp of
something. So, I spent two days thinking it through. This was happening
a few weeks after a CFAR workshop, and therefore I tried to make it as bulletproof
as possible. What is the exact research question I'm trying to solve?
How does my idea differ from state of the art methods? Why are those
differences going to make it perform better?
What is the fastest experiment I can set up to get useful data to adjust my
research trajectory?
Assume something goes wrong - what's the most likely failure point, and how
surprised am I if it fails?

After spending most of a day thinking it through, I spent most of the next day
writing it up into a research proposal. Sent it out end of Friday, come back
next Monday, and to my surprise, the feedback is positive. People have
suggestions, but experienced researchers all believe in the idea.

This is both incredibly exciting and incredibly terrifying. It's *my*
idea, and they all think it has promise. This sets off a ton of alarm
bells.

* I own this idea, therefore the success of this idea is a measure of my
research ability.
* I came up with this idea, but that doesn't mean others can't come up with
the same idea. In fact, it is very likely another researcher has come up with
the same idea. It's a natural extension of existing work, and thoughts aren't
as novel as people think they are.

Believe whatever you want about these claims. They're what I believe, on
a structural level, and it leads to a simple conclusions.

* If I do not push on this idea right now, I'm going to get scooped, and
I'll continue to be a failure of a researcher.

The last point needs some elaboration.

I did undergraduate research for 2 years, then somehow conned enough people
into thinking I knew enough about neural nets to land an industry job that
lets me do research. In all this time, I've never published a paper.

And now, I feel like the clock is ticking. Like I only got this position
because my professor put a good word in - which works for now, but I can't
coast on that for long. If I want to keep doing research, I need to show,
unequivocally, that I'm qualified for this. And that means publishing a paper,
and getting it accepted into a top machine learning conference. If I can't do
that after that many years of research, how am I ever going to convince someone
I can do deep learning research? Everyone wants to get into deep learning; it's
up to me to grab the opportunities that have fallen into my lap and **shove**
them as far as I can.

This mindset is really stressful, and I hate it, and I don't want it to go away,
because it feels like I wouldn't be able to do anything without it.

Okay, now here's the kicker. The next big conference deadline is ICLR, which is
November 4th. That gives me just over a month to turn my idea into a paper.

*Holy shit.* I reflect on my research speed. The odds I get results in a month
are quite low.

But they're bigger than zero.

*Alright. Let's do this.*

(A small part of me starts yelling ["Leeeeeeroy!"](https://www.youtube.com/watch?v=hooKVstzbz0),
but I ignore it.)

\*\*\*
{: .centered }

I start working longer and longer hours. I took this job in part to avoid working
late hours, but around this time I realize the late hours are hard to avoid if
I want to research. I turn around and embrace them instead, as long as they're
within limits.

As with all research, there are twists and turns, unexpected issues, the whole
works. However, all things considered, progress is surprisingly smooth.

Just one problem. It's not fast enough. One week before the deadline, I make
the call - an ICLR paper isn't happening this cycle. If I did a bunch of
reserach pivots, and got really lucky, I could get a paper, but I wouldn't
be proud of it. I throw in the towel right before Halloween weekend, and use
the mental commitment to feel better about spending my whole weekend visiting
friends around the Bay.

Monday arrives faster than I expect, which is par for the course. Then, I hear
a NIPS workshop got its deadline pushed from November 1st to November 8th.
Standards for a workshop paper are lower. Four pages instead of eight, and
initial results are okay.

If I start ramping up right now, do another week of late hours, and all of
my experiments go well, I can hit that deadline.

The odds of all my experiments going well are pretty low. But once again,
they're better than zero. The same thoughts are running through my head.
*You need a paper. Need need need a paper. How else are you going to get
validation?* I know how to answer that question, but the part of me
that's egging me on doesn't care whether it gets an answer or not.

In the face of having one more week to get results, I declare bankruptcy
on everything else. Self reflection time gets converted to coding time.
Any thoughts of thinking about my blog turn into relaxation to prepare
for another day at work. Any metalevel goals for improving my workflow
get thrown out. I cancel my meetings, I throw out code quality,
I ignore best practice. There are hundreds of lines of copy-pasted code
that continue to haunt me, and the worst part is that breaking all
those pesky software engineering rules was the right call. There is only
the deadline, there is only the potential paper, and in the face of
that idol there can be nothing else.

\*\*\*
{: .centered }

It's Friday. It still doesn't look good.

I share my results with my research mentor, and he thinks it isn't worth writing
a paper. I agree. This paper was always going to be a sell of tentative work
instead of a presentation of compelling work, but there's no way to sell these
learning curves.

So I give up. I slot everything I threw out back in. And just for kicks, on
Friday night, I think it through one more time.

"Let's assume I've managed to get a paper. What had to happen? Well, I need to
do two successful experiment cycles. That's non-negotiable. Each cycle takes
three days, and I have three. It can't happen, the deadline's too soon.

"The paths are all blocked. Is there a path I'm not seeing? The rate limiter is
the experiment cycle time. Can I make it faster? I'm doing 200 episodes and it
isn't learning anything, and I can't make the episode shorter because if it's
any shorter I won't be able to simulate enough time to solve the problem.

"Wait. What's my simulation time step?"

In 20 seconds, I discover 1 step = 0.01 seconds.

Five seconds after that, I realize if I make my timestep bigger, it solves a ton
of problems at once. I can make my episodes shorter. I can run fewer physics
calculation to simulate the same amount of time. It even makes it easier for any
real world experiments I want to run, because sending control at 100 Hz isn't
happening.

It takes me a minute to identify the one line of code I need to change to fix
all these problems.

The whole process took about ten minutes. If I had asked the right questions
three weeks ago, I could have run 3-4x as many experiments. It's not guaranteed
I would have had a paper because of that, but the odds are massively, massively
higher.

If you've read Methods of Rationality, I had an equivalent of the Final Exam
moment, in real life. **It was really bizarre.** As I'm preparing the code for
my 3rd and final attempt to get results over the weekend, I'm marvelling at
just how strange it was, to see a wall go from an unknown unknown to something
I could walk over with ease.

Walt Disney has a famous quote about deadlines. "Everyone needs deadlines. If
we didn't have deadlines, we'd stagnate." And he's absolutely right. It's one thing
to say you understand the deadline is two weeks away. It's another to look at
a three-day deadline, with no extensions possible, and truly understand where
you stand.

\*\*\*
{: .centered }

If you were expecting this story to have a happy ending, I'm sorry to disappoint.
Like I said, this is a story about how I didn't get results in time. I looked
at my results last weekend, and they're not good enough.

There's some regret, but I'm mostly over it. I knew my odds going in were bad,
and I didn't make it, so there we go, validation of the hypothesis. The work I
did was all relevant to my research, and I know what threads I want to keep
pushing. I didn't get a paper, but I got a lot of work done.

Still, there's a part of me that wonders where I would have been if I didn't
declare bankruptcy so hard, and let myself continually question my research
trajectory, instead of doubling down on it and paying the price when I failed.

"Man, this sucks. What can I do, to make sure I always remember to take a
step back and question my research assumptions? It's okay to fail if the
problem is harder than expected, but it isn't okay to fail because of
problems that are secretly easy to fix. What is the first step towards
getting to a place where I can work on things with no regrets?"

The answer comes almost by reflex.

"Write it down. Write it down everywhere, and share it. Make it impossible to
forget the idea, because you've just understood how important Hamming questions
are, and you need to capture the insight before it flies away."

So I do. And just like before, I rush it out. Not too much editing, because
I want it done quickly. Not too many details, because I want to convey what
I understood to as many people as I can, while understanding that I actually
can't, because the barrier between reading something and living it is
so huge.

In total, I write one thousand nine hundred words, including this sentence.

There will certainly be other failures. But if I have a say in it, they won't
be failures for the same reason.
