---
layout: post
title:  "Mystery Hunt 2016 Wrap-Up"
date:   2016-01-20 23:08:00 -0800
---

*Targeted towards people who did MIT Mystery Hunt 2016. I doubt you'll
care about this if you didn't participate. Some spoilers.*

Here's the thing about puzzle hunts: they bring together the strangest
people. Strange in a good way. The biggest reason puzzles are awesome is
because they provide concentrated bursts of problem solving euphoria,
but only the slightly unhinged are willing to destroy
their sleep schedules by working on puzzles for 3 days straight. Still,
any week where I get to hear proposals for sneakernet from space to Earth is
pretty awesome.

Normally, I hunt on bigger teams because they have better remote solver
support. Because I went in-person this year, I decided I should try out a
smaller team, so I hunted with ET Phone In Answer. It was definitely a
different dynamic. In
my previous Hunts, it felt like I wasn't a big contributor. (For context,
my first Hunt was with Sages.) When 10 people are looking at the same puzzle,
the math means it's unlikely you find the a-ha, because there's so many other
people working on it. On the other hand, I do like finishing
Hunt, and that's a lot easier on larger teams.
Something I'll need to think about for next year.

Thanks to sponsors, at the start of this Hunt every team got Google Cardboard,
Fitbit notebooks, and Fitbit pens. In a true display of Mystery Hunt paranoia, the first thing
we did was open the notebooks and disassemble a pen to verify none of them were
puzzles. I blame the first aid kit puzzle from the Alice hunt.

After kickoff, my first puzzle of the Hunt was [You Complete Me](http://huntception.com/puzzle/you_complete_me/).
We got the correct coefficients after some staring, but it took us a while to
get the next square a-ha. Once we did, we got stuck on extraction and abandoned it.
The next day, someone looked at it, did the obvious thing, and solved it in
five minutes. In hindsight, I have no idea how we missed it.

Had fun finding the answer to [Pictocryptolists](http://huntception.com/puzzle/pictocryptolists/). As with all substitution ciphers,
it took a while to get the first foothold, but once we got the theme it came
together like clockwork. Around five people cycled through it.
It was straightforward but tediuos, which made it a great cooldown puzzle
if you were frustrated at your current puzzle.

Oh, for once I identified a meta mechanism! It was for [Obedience Training](http://huntception.com/puzzle/obedience_training/).
We were very confident in ????PROOF BREEDERS, where exactly two of the ? were
consonants, but it took us until Sunday to guess the correct starting word.
(It was GOOFPROOF, for what it's worth. I know it's on theme, but FOOLPROOF
makes so much sense...)

[Meet the Loremipsumstanis](http://huntception.com/puzzle/meet_the_loremipsumstanis/) was frustrating. Everyone collected data for it once
we knew how the Bacon Ipsum worked, because it was too much fun to
justify working on anything else. It was all smooth sailing, until we
got to the final cryptic phrase. We knew the answer had to be eight letters long
from both the given numbers and the Rip Van Winkle meta constraint, but we
just couldn't get it, and the puzzle stayed unsolved for all of Hunt.
I'm still so disappointed TONY HAWK wasn't correct.

I finally found a use for my knowledge of Knuth up-arrow notation! ...Well, I
would have, if I hadn't looked at [Identify, SORT, Index, Solve](http://huntception.com/puzzle/identify_sort_index_solve/) five hours
after it was solved. As a fan of incredibly large numbers,
I'm sad I missed it.
Any puzzle involving Busy Beavers and Ackermann functions is automatically
awesome. Based on the Mystery Hunt subreddit, other people liked it too, so
hopefully I'll get another chance to reason about exponent towers.

Now, a slight digression. A ton of puzzles came out between Saturday night and Sunday
morning, but I didn't work on them. Instead, I was doing Round 1 of Facebook
Hacker Cup. Take it from me, don't start a programming competition at 2 AM after
doing puzzles all day. I briefly looked at
the problems, and decided to focus on the first 3. I did very minimal testing,
submitting my last solution 5 seconds before the contest ended.
Miraculously, they were all correct.
I expect to die in Round 2, and will be very surprised if I make
top 500 for the T-shirt, but at least I made it.

Back to puzzles! Shortly after coming into HQ, somebody called out ["Ponies!"](http://huntception.com/puzzle/missing_the_mark/).
I've always felt like Mystery Hunt had to have an My Little Pony puzzle at some point,
and this year someone on the writing team felt the same way.
We solved it in around forty minutes, seamlessly going from data
collection to a-ha to extraction. On point construction, clean theming, and
solvable without MLP knowledge but much faster with it.
My second most enjoyable solve of the Hunt.

But, my favorite solve of the Hunt has to go to [Sleeping Beauty meta](http://huntception.com/round/sleeping_beauty/). I
didn't know Nikoli created a logic puzzle with no numbers, but now I
do. Other people did the legwork of filling in the grid and solving
with incomplete info, but we didn't know what to do with the logic
puzzle solution. We abandoned it Sunday morning.
Around twenty-five minutes before Hunt HQ closed, I gave a final look, and
figured it out. I didn't actually do that much, but it feels really good to be
the guy (or gal) to figure out the final extraction, especially on a
metapuzzle.

We weren't close to finishing, but I never expected to finish, so that
was fine. I'm very curious to see what kind of hunt Setec will make.
After seeing *Sneakers*, I'll say only this: Setec can have Too Many Secrets,
as long as they don't have Too Many Puzzles.

Finally, for tradition's sake: this post is not a puzzle.

(Just kidding, it is. Yes, really. I promise it's short.
If something seems sketchy, look at the remainder.
You'll need more numbers to get the answer, and here they are:
-10, 5, -10, -3, 9, -1, -3.)

<button
    class="spoiler-control"
    title="Click to show answer"
    toggle1="Show Answer"
    toggle2="Hide Answer"
    affected="answer">
</button>
{: .centered }

<pre class="hidden answer">
The answer is DREAMER.
</pre>

<button
    class="spoiler-control"
    title="Click to show solution"
    toggle1="Show Solution"
    toggle2="Hide Solution"
    affected="solution">
</button>
{: .centered }

<pre class="hidden solution">
This is a barebones identify, sort, index, solve puzzle.
Not very interesting, but it gets the job done, and I didn't
want to make something too complicated.

There are 7 given numbers, and 7 puzzles are linked. Furthermore,
sometimes the post spells out numbers and sometimes it doesn't.
The comment that you'll need more numbers should also sound fishy.

If you read carefully, every paragraph linking a puzzle has exactly
one number spelled out in words. Every other paragraph uses digits.
The numbers are five, five, two, eight, five, forty, and twenty-five.
Index the number into each of those paragraphs to get the clue phrase

PUZZLE ANSWER FOR DATA USE SAME NUMBERS

From the links, look up the answer to each puzzle. As clued,
use the same paragraph numbers to index into the puzzle answers.
Some numbers won't work, but the comment to "look at the remainder"
should hopefully lead you to reducing the number if the answer
is too short. Doing so gives

NMODDFU

and shifting by the final numbers gives

DREAMER

as the answer.
</pre>
