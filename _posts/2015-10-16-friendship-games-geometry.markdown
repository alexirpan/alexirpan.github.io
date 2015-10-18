---
layout: post
title:  "DECIDE ON A TITLE"
date:   2015-10-16 22:04:00 -0800
---

(Very minor spoilers for *Friendship Games*, read at your own risk.)

The third Equestria Girls movie (the high school spinoff for Friendship
is Magic) came out recently. Honestly, it wasn't that good. It was definitely okay,
but like the previous two movies the pacing and plotting are a bit suspect. It
also broke my suspension of disbelief a bit too much.

That being said, I still liked it. As always, the animation is solid and the
songs are catchy. (My head knows they're pop songs, and not even good pop songs,
but it's still fun.) Here's an example. The backstory is that two rival high schools
are competing in the academic decathalon (acadeca).

VIDEO

First off, I just want to point out all the badass science and carpentry these
girls are doing. Hooray for breaking gender stereotypes without making it obvious!

However, if I'm honest, my first reaction was on this frame

PICTURE

Wait. Is that...

PICTURE

*It is.*

PICTURE

**It's Euclidean geometry.**

OPTIONAL PICTURE

Oh man, you don't even know. Euclidean geometry is my favorite topic frmo high
school math, and I've spent a correspondingly long time messing around in it.
What's notable here is that not only is this Euclidean geometry, the text
animated on the chalkboard looks like a well formed geometry proof.

And that begs the question: is it?

(heading?)

To make this a bit more interesting, I'm going to unpack my thought process
and try to explain why I did the steps I did. (REPHRASE)

First, I gave the animating staff the benefit of the doubt,
and assumed the proof was valid. Why? Well, one of the episodes from season
2 was based around time travel, and they added the equation describing
relativistic time dilation as an Easter egg (link.) It's entirely reasonable
that they would animate more math Easter eggs.

Let's chase that assumption for a bit. Assume the chalkboard has both a real
geometry problem and its proof. When watching casually, the starting and ending
shots are most prominent.

PICTURE OF THE START

At the beginning, there's no text accompanying the diagram, so the problem
must be simple to state, and requires no additional detail.
At the end, the writing on
the chalkboard only involves lines, triangles, and angles. Notably, no trigonmetry
is used.
Since no side lengths are specified, the problem is most likely an angle chasing
problem. Yet for an angle chasing problem, this is a surprisingly long proof. Normally,
these proofs are a few lines of reasoning at most, but Sunset and Twilight have filled
an entire chalkboard with derivations. (Again, at this point we don't know the
chalkboard actually has derivations, or that this problem even exists.
We're assuming it does, and need to be prepared
to completely discard this line of reasoning.) Plus, there's one more clue: this
problem felt vaguely familiar to me.

Based off these clues and some Googling, I found a reasonable candidate:
the World's Hardest Easy Geometry Problem. (LINK). It's a problem that both
only requires a diagram to state and basic geometry to solve.
I had actually seen this problem several years agao, which explains the feeling
I had. As verification, the answer of $$x = 20^\circ$$ is correct,

PICTURE

the diagrams match up

PICTURE

and the final line $$\angle DEF = 30 + x = (180 - 80) / 2 = 50$$ shows up in
both places.

PICTURE

At this point, we can conclude the animators have included this problem into
the movie. Why? At this stage, there are two possibilities for what we will observe.

- The rest of the chalkboard will be the rest of the proof.
- The rest of the chalkboard will not be the rest of the proof.

There is a reasonable explanation for the first outcome: the animators looked up
a geometry problem and included it in the movie. However, there are no reasonable
explanations for the latter. What world states would lead to the animators
inclding geometry from one problem, and filling the rest with junk? There are some
explanations (i.e. everything matched so far was by dumb luck), but these are
too unlikely.)

So, we know the animators are working in good faith. But, we don't know how accurate
they were, or how well they succeeded. The only way to do that is to verify the
rest of the chalkboard. I stepped through
the video frame by frame until I found the money shot.

COPY PASTED PROOF (ALSO USE THAT IMAGE)

FULL PROOF FROM MOVIE HERE (side by side?)

This is the clearest shot of the chalkboard in the entire sequence. It's only
shown for 0.2 seconds of the montage, but it matches up with the second section
of the proof.

ANOTHER SIDE BY SIDE IMAGE?

However, it's not perfect. For one, they didn't draw the line parallel to $$AB$$
through $$D$$, so there's no point $$F$$. Also, the line $$\angle CDF = \angle CAB =
70 + 10 = 80^\circ$$ has a small animation error, the rightmost equals sign is a
minus sign instead.

This verifies up to the line $$\angle DGF = 180 - 60 - 60 = 60^\circ = \angle ACB$$.
The next picture in the montage is

PICTURE

which doesn't give much new information (although the line before $$\triangle DCF ~ \triangle ACB$$
is a bit visible and matches $$\angle AEB = 180 - 70 - (60+20)$$.)

And, a few frames after that comes this shot.

PICTURE

This includes the $$\angle DEF = 30 + x = (180-80)/2$$ line that appeared in the
ending shot. There's also something about $$FE$$, and something about the ratio
between two sides.




1. Calculate some known angles:

    ACB = 180-(10+70)-(60+20) = 20°
    AEB = 180-70-(60+20) = 30° 

2. Draw a line from point D parallel to AB, labeling the intersection with BC as a new point F and conclude:

    DCF ACB
    CFD = CBA = 60+20 = 80°
    DFB = 180-80 = 100°
    CDF = CAB = 70+10 = 80°
    ADF = 180-80 = 100°
    BDF = 180-100-20 = 60° 

3. Draw a line FA labeling the intersection with DB as a new point G and conclude:

    ADF BFD
    AFD = BDF = 60°
    DGF = 180-60-60 = 60° = AGB
    GAB = 180-60-60 = 60°
    DFG (with all angles 60°) is equilateral
    AGB (with all angles 60°) is equilateral 

4. CFA with two 20° angles is isosceles, so FC = FA

5. Draw a line CG, which bisects ACB and conclude:

    ACG CAE
    FC-CE = FA-AG = FE = FG
    FG = FD, so FE = FD 

6. With two equal sides, DFE is isosceles and conclude:

    DEF = 30+x = (180-80)/2 = 50 

Answer: x = 20°
