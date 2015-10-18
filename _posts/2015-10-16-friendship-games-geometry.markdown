---
layout: post
title:  "DECIDE ON A TITLE"
date:   2015-10-16 22:04:00 -0800
---

(Very minor spoilers for *Friendship Games*, read at your own risk.)

*Friendship Games*, the third *Equestria Girls* movie, came out recently.
As with the rest of the high school spinoff
for *Friendship is Magic*, I have mixed
feelings about id. It's...well, it's definitely a movie.
The pacing's off, the plots aren't
neat and tidy, and it broke my suspension of disbelief by too much.

That being said, I still liked it. The animation is solid, the songs are catchy,
and the character development is still fun, no matter how cliche it is.

Here's one of the better segments. The backstory is that two rival high schools
are competing in and academic decathalon (the Acadeca.) Give it a watch.

VIDEO

(As an aside, I want to point out all the badass science and carpentry these
girls are doing. Hooray for breaking gender stereotypes without directly calling
it out, which makes it all feel normal!)

I like how the song gets animated, and the shot composition. But, that's not
what this post is about. My first reaction was on this frame, right before
Sunset and Twilight have a math-off.

PICTURE

Wait. Is that...

PICTURE

*It is.*

PICTURE

**It's Euclidean geometry.**

OPTIONAL PICTURE

Oh man, you don't even know. Euclidean geometry is the **best**. It's
my favorite topic from high school math.
What's notable here is that not only is this Euclidean geometry, the
animated text looks like a well formed geometry proof.

Which begs the question: is it?

(heading?)

To make this a bit more interesting, I'm going to unpack my thought process
and try to explain why I did the steps I did. (REPHRASE)

To investigate this, I first gave
the animating staff the benefit of the doubt, and assumed it was a real proof.
Well, the time travel episode from season 2 of *Friendship is Magic*
included the equation describing relativistic time dilation. So at this point,
including a geo proof wouldn't suprise me.

Now, let's chase that assumption for a bit. Assuming the chalkboard has both a real
geometry problem and its proof, I used the start and end of the math contest to
get data on what the problem could be.

PICTURE OF THE START

On a closer look, the diagram looked vaguely familiar. Let's set that aside for
now and ask what else we can figure out.

At the beginning, there's no text accompanying the diagram, so the problem
must be simple to state, and requires no additional detail.
At the end, the writing on
the chalkboard only involves lines, triangles, and angles. Notably, no trigonmetry
is used.
No side lengths are specified, so it's most likely an angle chasing problem.
Yet for an angle chasing problem, this is a surprisingly long proof. In my
experience, angle chasing is pretty short, but Sunset and Twilight have filled
an entire chalkboard with derivations.

(Again, at this point I still don't know this is a real proof. Everything
I'm concluding is under the assumption that the animating staff were detail-oriented
enough to do research for a 20 (CHECK) second clip.)

Based off those clues, a vague feeling, and the power of the Internet,
I found
the World's Hardest Easy Geometry Problem. (LINK). It's a problem that's simple
to state, requires only basic geometry, and is difficult to actually solve.
I had actually seen this problem several years agao, which explains why the diagram
looked so familiar. And more importantly, $$x = 20^\circ$$ is the solution to
the problem.

PICTURE

and the given angles match up

PICTURE

and there's something that looks like $$(180 - 80) / 2 = 50$$, which shows up
at the end of hte World's Hardest Easy Geometry Problem proof.

PICTURE

So, now we can upgrade that assumption to a fact. The only question left is how
accurate they were about it, and the only way to do that is to verify the rest of
the chalkboard.

Unfortunately (for me), the movie spends more time on its characters than its
geometry proof. There's a very brief montage which looks promising,

ANIMATED GIF?

so I downloaded the video and stepped through frame by frame, until I found
the money shot.

COPY PASTED PROOF (ALSO USE THAT IMAGE)

FULL PROOF FROM MOVIE HERE (side by side?)

This is the clearest shot of the chalkboard in the entire sequence. It's also only
shown for 0.2 seconds. A lot of work, for something that people will barely
notice. The text lines up perfectly with the second section of the proof.

ANOTHER SIDE BY SIDE IMAGE?

However, it's not perfect. For one, neither character draws the parallel to $$AB$$
through $$D$$, so there's no point $$F$$. Also, neither character draws segment $$AF$$,
so there's no point $$G$$. They're both pulling these points out of nowhere. And, the line
$$\angle CDF = \angle CAB = 70 + 10 = 80^\circ$$ has a small animation error;
they accidentally drew $$- 80^\circ$ instead of $$= 80^\circ$$.

The rest of the montage isn't there interesting. There's this shot

PICTURE

which is a closeup of the top line of the second section, and this shot

PICTURE

which is a closeup of the $$\angle DEF = 30 + x = (180 - 80)/2$$ line I noticed
previously.

The first section of the proof only appears in the final shot. It's a bit blurry,
but it reads

$$
\angle ACB = 180 - (10+70) - (60+20) = 20^\circ
$$

$$
\angle AEB = 180 - 70 - (60+20) = 30^\circ
$$

which again lines up.

The ending of the proof is best seen in the two closeups

PICTURES

which gives the final lines

$$\triangle ACG \cong CAE$$

$$FC - CE = FA - AG = \overbar{FE} = \overbar{FG}$$

Some points off here, for having Sunset deriving $$\angle CDF = \angle CAB = 70+10 = 80^\circ$$
after writing $$FE = FG$$; she's proving things out of order, and there's
no way she can justify $$FC - CE = FA - AG$$ before that line. (And points
to Twilight for proving things in the right order.)

Going back to the original proof, both characters skipped stating
triangles $$\triangle DFG$$ and $$\triangle AGB$$ are equilateral. However,
that's reasonable. They've shown the angles of $$\triangle DFG$$
and $$\triangle AGB$$ are all $$60^\circ$$. They also omitted justifying
$$FC = FA$$ from isosceles $$\triangle FCA$$, and $$CG$$ bisecting $$\angle C$$,
but these are also reasonable skips.

Overall, I'm impressed the animating staff actually included real math. It also
proves that Sunset almost, almost got it, if not for the arithmetic mistake at
the end. Sometimes that's how these things go.

