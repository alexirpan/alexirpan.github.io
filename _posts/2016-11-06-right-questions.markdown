---
layout: post
title:  "Asking The Right Questions: A Story of Failure"
date:   2016-11-08 01:54:00 -0800
---

This is the story of how I didn't get publishable results in time for a
Nov 8th NIPS workshop deadline.

It'll be light on details. One, I'm aiming for a broad audience.
Two, I do need to be somewhat confidential about my work, because although
my research is pretty open, I am working for a company.
Most importantly, three: the details don't matter for this story.

\*\*\*
{: .centered }

I first had my research idea in late September.

I was (and still am) generally interested in reinforcement learning, and more
specifically ways to make RL more sample efficient. I had a few ideas that
seemed like they had potential, so I decided to spend some time thinking it
through. This happened right after a CFAR workshop, so I tried to make it
as bulletproof as possible. What is the exact research question?
How does my idea differ from state of the art, and why are those
differences better. What is the fastest experiment that gives me useful data
to decide what to do next. Assume something goes wrong - what's the most
likely failure point? Am I surprised if it fails, and if I'm not surprised,
are there ways I can make it more surprising to fail that way?

Once I'm satisfied, I spent most of the next day writing it up into a research
proposal. To my surprise, the feedback is positive.

This is both incredibly exciting and incredibly terrifying. It's *my*
idea, and multiple experienced researchers thinks it has promise. This sets
off a ton of gut reactions.

* I own this idea, therefore the success of this idea is a measure of my
research ability.
* I came up with this idea, but that doesn't mean others can't come up with
the same idea. In fact, it is very likely another researcher has come up with
the same idea. It's a natural extension of existing work, and thoughts aren't
as novel as people think they are.

Believe whatever you want about these claims. They're what I believe, on
a structural level, and it leads to a simple conclusions.

* If I do not push on this idea right now, I'm going to get scooped, and
I'll continue to be a failure.

I should elaborate on the last point.

I haven't been through a PhD program, or even a masters program. I did undergrad
research for 2 years, then conned enough people into thinking I knew things
about neural nets, and now I have an industry job that lets me do research.
In all this time, I've never published a paper.

And now, I feel like the clock is ticking. Like I only got this position
because my professor put a good word in, which works for now, but will stop
working soon. If I want to keep doing research, I need to show,
unequivocally, that I'm qualified. And that means publishing a paper,
and getting it accepted into a top machine learning conference. Not all good
research leads to papers, but publication is the best way to signal good
research ability. If I can't publish after years of undergrad research,
how am I ever going to convince someone I can do deep learning research?
There's no shortage of people interested in deep learning. It's
up to me to grab the opportunities that have fallen into my lap and
**shove** them as far as I can.

This mindset is really stressful, and I hate it,
and I don't want it to go away, because it feels like I wouldn't be able
to do anything without it.

Okay, now here's the kicker. The next big conference deadline is ICLR, on
November 4th. I have just over a month to go from idea to paper, if I want to
hit that deadline, and if I miss it, the next big deadline is ICML in February.

Take all of that, and my first thought is *holy shit*, followed by **_holy shit_**.

Based on past history, the odds I get results in a month
are low. I need to put in a ton of work just to have a chance.

But the odds are bigger than zero.

*Alright. Let's do this.*

(A small part of me yells ["Leeeeeeroy!"](https://www.youtube.com/watch?v=hooKVstzbz0)
in reply, but I ignore it.)

\*\*\*
{: .centered }

October is month of long hours. I took this job in part to avoid the horror
stories I kept hearing about work-life balance in grad school, but around
this time I realize that isn't innate to grad school, it's innate to research.

Like always, there are twists and turns, unexpected issues, the
works. However, all things considered, progress is surprisingly smooth.
Every week, I have more to show for my work.

Just one problem. The work isn't fast enough.

One week before the deadline, I make the call - I can't hit ICLR.
If I did a bunch of research pivots, and got really lucky, maaaaybe I could 
make it. But I wouldn't be proud of that paper. I throw in the towel
right before Halloween weekend, and use the commitment to feel better
about spending my whole weekend visiting friends around the Bay.

Monday arrives faster than I expect, which is par for the course. Then, I hear
a NIPS workshop got its deadline pushed from November 1st to November 8th.
Standards for a workshop paper are lower. Four pages instead of eight.
Preliminary results are more likely to get accepted.

If I start ramping up right now, do another week of late hours, and all of
my experiments go well, I could do it. The odds are low. But just like last
time, they'd be better than zero.

I declare bankruptcy on everything else. Self reflection time turns into
coding time. Blogging turns into relaxation to prepare for another long day at
work. Meta-level goals for improving my workflow get thrown out. I cancel
my meetings, I throw out code quality, I ignore best practice.
There are hundreds of lines of copy-pasted code
that continue to haunt me, and the worst part is that breaking all
those pesky software engineering rules was the right call, because I didn't
have time to do it right. There is only the deadline, there is only the
potential paper, and in the face of that idol everything else fades away.

\*\*\*
{: .centered }

It's Friday. It's not looking good.

I share my results with my research mentor, and he thinks it isn't worth writing
a paper. I agree. This paper was always going to be a sell of tentative work
instead of a presentation of compelling work, but there's no way to sell these
learning curves.

So I give up. I slot everything I threw out back in. Now that I have more time
to think about how my week went, I decide to think it through one more time,
just for kicks.

"Let's assume I made a paper in three days time. What has to happen?

"That can't happen. I'm rate-limited, my experiments take three days to run
and I need to run at least two of them, sequentially. Six days can't fit in
three days. It's actually impossible, unless I can magically make my experiments
run several times faster.

"Hang on a second."

Within ten minutes, I discover four quick changes that let me run experiments
ten times faster.

Do you understand how idiotic I felt in that moment? The realization that I
could have asked the same questions three weeks ago and discovered the same
answers? And that if I had, my odds of hitting a paper would have skyrocketed?

If you've read Methods of Rationality, I had a real-life Final Exam
moment. It felt like I was somebody who was pretending to consider all possibilities,
but I was secretly still in a mental box. I only broke out of that box when
staying in the box made success not just virtually impossible, but actually
impossible, and it's only after exiting that box that I'm able to wonder why I
was inside it in the first place.

\*\*\*
{: .centered }

If you were expecting this story to have a happy ending, I'm sorry to disappoint.
Like I said, this is a story about how I didn't get results in time.

I implemented all the changes I come up with, checked the results over the
weekend, and they're still bad. Now it's truly impossible. But because it worked
so well last time, I think it through anyways. This time, I decide it actually
is impossible, and that's that. Here we are.

I have some regret, but given the odds I gave myself, I'm okay with not making
the deadline. The work I did was all relevant to my research, and I know what
parts I want to keep building on.

Still, I wonder where I would be if I didn't declare bankruptcy so hard, and
let myself continually question my research trajectory, instead of doubling
down on it and paying the price when I failed.

Now that I have time to do meta-level planning again, I sit down to think.

"It's okay to fail. It isn't okay to fail in as stupid a way as I did.
What can I do to make sure I never fail in this way again?"

The answer comes almost by reflex.

"Write what you learned, and share it with others. It's the only way anything
manages to stick in your brain. Make the idea unforgettable, because you've
just realized the importance of [Hamming questions](http://www.cs.virginia.edu/~robins/YouAndYourResearch.html)
at a visceral level, and shifts that strong don't come every day, maybe not
even every year. You need to capture the insight before it flies away. So
write, write, write."

I do just that. Not too much editing, because I want it done quickly.
I know I won't be able to convey all the feelings I want because the barrier
between reading something and living it is huge. But I do it anyways,
because I need to do it for me.

In total, I write 1723 words. (That includes the sentences you're reading
right now.)

There will certainly be other failures in my life. But if I get a say, they
won't be similar this one.
