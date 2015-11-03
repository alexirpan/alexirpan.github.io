---
layout: post
title:  "Math in Movies: The Friendship Games Geometry Problem"
date:   2015-10-16 22:04:00 -0800
---

(Very minor spoilers for *Friendship Games*. Read at your own risk.)

I imagine most people outside the fandom don't know this, but *My Little Pony: Friendship is Magic*
has a high school spinoff called *Equestria Girls*. It's a movie series that exists
only because of the merchandise potential. Reception to the films is mixed,
but it's widely agreed that they're nowhere near as good as the show.

The most recent entry, *Friendship Games*, came out September of this year.
It's...well, it's definitely a movie.
The pacing is off, the plot is silly, and the world stretches suspension
of disbelief way too much. (Magic is real, people are growing wings,
the high school has a portal to an alternate universe, AND NO ONE
FREAKS OUT ABOUT IT. Really?)

That being said, I still enjoyed it. The animation is solid, and the songs are
catchy. Here's one of those songs.

<div class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ww8TDQ03qlk" frameborder="0" allowfullscreen></iframe>
</div>

ADD TRANSCRIPT IN SPOILER

First off, I dig this animation a lot. It gets so much mileage out of facial
expressions and body language.
I'd also
like to point out all the badass science and carpentry these
girls are doing. Hooray for casually breaking gender stereotypes!

But, that's not what this blog post is about. It's about this frame.

![first scene](/public/geo-proof/first.png)
{: .centered }

Wait. Is that...

![second scene](/public/geo-proof/second.png)
{: .centered }

*It is.*

![third scene](/public/geo-proof/third.png)
{: .centered }

**It's Euclidean geometry.**

OPTIONAL PICTURE

Let me explain why I'm freaking out so much.

I did math contests in high school. My favorite subject was Euclidean
geometry. I took a course on Euclidean geometry for math contests. I made
honorable mention in Bay Area Math Olympiad because I knew about [radical axes](https://en.wikipedia.org/wiki/Radical_axis).
This is an animation of two high school students competing on a
geometry problem. THIS WAS ACTUALLY MY LIFE. One huge part of my life got
animated into another huge part of my life. It's so wondeful.

And the animators didn't half-ass it either. These chalkboards look like
valid geometry proofs. There's no immediate reason to believe they aren't.
I wonder if the proof's valid...

Cue the nerdsniping.

\*\*\*
{: .centered }

To investigate this, I first gave
the animators the benefit of the doubt and assumed it was real. There's a good
reason to assign a high prior on this.
The time travel episode from season 2 of *Friendship is Magic*
included equations from special relativity describing time dilation.
The 100th episode had a free body diagram and several equations from Newtonion physics.
I give the team a lot of respect on attention to detail. At this point, they could
add Fermat's Last Theorem as an Easter egg and I wouldn't bat an eye.

Let's chase that assumption for a bit. It's easiest to see the diagram
at the start and end of the contest.

![second scene](/public/geo-proof/second.png)
{: .centered }

![ninth scene](/public/geo-proof/ninth.png)
{: .centered }

On a closer look, the diagram looked vaguely familiar. Let's set that aside for
now and ask what else we can figure out.

At the beginning, there's no text accompanying the diagram, so the problem
must require no additional detail.
At the end, the writing on
the chalkboard only involves lines, triangles, and angles. Notably, no
trigonometry and no side lengths. If it is a real problem, then it's an
angle chasing problem.
Yet for an angle chasing problem, this is a surprisingly long proof. In my
experience, angle chasing is pretty short, but Sunset and Twilight have filled
an entire chalkboard with derivations.

(Again, at this point it's only likely this is a real proof. What I'm doing
here is finding out what a real proof would imply to help narrow down the
problem. Based on how easy/hard it is to find the problem, I can use that to
adjust how likely I believe the proof is real. It's possible the animators
made a new geometry problem just for this movie, but I don't think they're
crazy enough to do that for 20 seconds (CHECK) of animation.)

After some searching, I found
[the World's Hardest Easy Geometry Problem](https://www.duckware.com/tech/worldshardesteasygeometryproblem.html).
It hits all the key details: it uses only angles, requires only basic
geometry, and has a difficult solution.
I had actually seen this problem several years ago, which explains why the problem
looked so familiar. The solution is $$x = 20^\circ$$, which matches the answer
from the movie.

![side by side answer](/public/geo-proof/sbs_answer.png)
{: .centered }

and the given angles match up

![side by side diagram](/public/geo-proof/sbs_diagram.png)
{: .centered }

and $$(180 - 80) / 2 = 50$$ shows up in both proofs.

![side by side 50](/public/geo-proof/sbs_50.png)
{: .centered }

Jackpot.

Verification
------------------------------

It's certain this is a real geometry problem and proof.
The only question left is to see how accurate the animators were.

Unfortunately for geometry enthusiasts, the movie spends very little time on
the proof. There's a montage, but it's hard to verify anything at a glance.
(ANIMATED GIF?) I downloaded the video and stepped through frame by frame, until I found
the money shot.

![fifth scene](/public/geo-proof/fifth.png)
{: .centered }

This is the clearest shot of the chalkboard in the entire sequence. It's also only
shown for 0.2 seconds. A lot of work, for something that people will barely
notice. The text lines up exactly with the second section of the proof.

![side by side proof](/public/geo-proof/sbs_full_proof.png)
{: .centered }

However, it's not perfect. Neither character draws the parallel to $$AB$$
through $$D$$, so there's no point $$F$$. Also, neither character draws segment $$AF$$,
so there's no point $$G$$. They're both pulling these points out of nowhere. And, the line
$$\angle CDF = \angle CAB = 70 + 10 = 80^\circ$$ has a small animation error;
they accidentally drew $$- 80^\circ$ instead of $$= 80^\circ$$.

The rest of the montage has nothing new. There's this shot

![sixth scene](/public/geo-proof/sixth.png)
{: .centered }

which is a closeup of the top line of the second section, and this shot

![seventh scene](/public/geo-proof/seventh.png)
{: .centered }

which is a closeup of the $$\angle DEF = 30 + x = (180 - 80)/2$$ line.

The first section of the proof only appears in the final shot. I had to zoom
to see it, so it's a bit blurry.

![proof start](/public/geo-proof/proof-start.png)
{: .centered }

It reads

$$
\angle ACB = 180 - (10+70) - (60+20) = 20^\circ
$$

$$
\angle AEB = 180 - 70 - (60+20) = 30^\circ
$$

which again lines up.

The ending of the proof is best seen in the two closeups

![third scene](/public/geo-proof/third.png)
{: .centered }

![fourth scene](/public/geo-proof/fourth.png)
{: .centered }


which gives the final lines

$$\triangle ACG \cong CAE$$

$$FC - CE = FA - AG = \overbar{FE} = \overbar{FG}$$

There are some more errors here. Sunset derives $$\angle CDF = \angle CAB = 70+10 = 80^\circ$$
after writing $$FE = FG$$; she's proving things out of order. There's
no way she can justify $$FC - CE = FA - AG$$ before that line. (Points
to Twilight for proving things in the right order. It could be a subtle way to
show Twilight has more talent, but I'm more inclined to believe it's an error.)

Going back to the original proof, both characters skipped stating
triangles $$\triangle DFG$$ and $$\triangle AGB$$ are equilateral. However,
that's reasonable. They've shown the angles of $$\triangle DFG$$
and $$\triangle AGB$$ are all $$60^\circ$$, so the equal side lengths are implied.
They also skipped justifying $$FC = FA$$ from isosceles $$\triangle FCA$$, and
didn't prove $$CG$$ is the angle bisector of $$\angle C$$,
but these are also reasonable skips given the diagram.

Overall, I'm impressed the animating staff actually included real math. It also
proves that Sunset almost, almost got it, since her only error is an
arithmetic mistake at the end. Sometimes that's how these things go.
Now that I've done all of this, this actually makes the scene better.
Sunset Shimmer's fall to villainy was based around a desire to be
the best at all costs, and her redemption is about her anxiety at failing to
make up for all the damage she caused. With all the self-loathing, it's easy
to forget that she's almost as good as Twilight.

