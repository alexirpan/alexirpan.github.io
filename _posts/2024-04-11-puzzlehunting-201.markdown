---
layout: post
title:  "Puzzlehunt 201"
date:   2024-03-07 01:41:00 -0700
---

I'm good at puzzlehunts. I thought about equivocating this, saying I think I'm
good at puzzlehunts, or relatively strong at puzzlehunts, but, no, I'm just good
at them. I've been on the winning MIT Mystery
Hunt team (twice), and most recently was on the 2nd place team for the
[Who Killed Ickey?](https://ickeytreasurehunt.com/leaderboard) treasure hunt.

Now, I have some misgivings about casting puzzlehunts as about the competition.
I feel they're much more about testing what you can do and having fun than about
trying to be first. There's really not much if any money in puzzlehunting.
From a community standpoint, I suspect people like it this way. Still, competition
can be fun. At minimum, solving puzzles to progress in a hunt is fun. After doing
puzzlehunts for well over a decade, I've picked up some habits that could be
useful to share.

**If you are new to puzzlehunts, you are not the target audience.** I mean, feel
free to keep reading! But I will be assuming a bunch of background knowledge and
won't be trying to explain what a puzzle is or what a meta is and so forth. I
recommend these posts (TODO) as better initial reading.

**If you've done many puzzlehunts, not everything I say here will work for you.**
Puzzlehunting systems are a little like productivity systems: everyone's is
different, not all pieces of them will click with you, and none of them are
clearly dominant. Your best bet is to try things out, take the parts that work,
and don't feel bad if some of them don't.

Last note: **this will have spoilers for some puzzles.** I've tried to keep
the spoilers light, but it's much easier to give examples than to construct
new puzzles just for the sake of this post. Imagine if this was all seeded
content for a puzzlehunt. Boy would that make this post hard to write!
(Seriously though, it isn't. Don't try looking for it.)


The "If I Had One Minute Version"
-------------------------------------------------------------------

Puzzles are a collection of data, that has hidden patterns or structure, and
solving a puzzle is about finding those structures.

Solving puzzles quickly breaks down into three categories: generating good
ideas about how a puzzle might work, quickly testing those ideas, and executing
on the ideas that appear most correct.

To generate more ideas, solve more puzzles to see what ideas have shown up in
past puzzles.

To test ideas faster, solve more puzzles to see what lets you conclude an
idea is wrong, and try to shortcut to that on the next puzzle.

To execute better, practice by solving more puzzles.


Wait This Seems Too Simple
-----------------------------------------------------------------

Nah that's pretty much it.

The very common lesson, is that if you want to get good at a skill, just do
it a bunch. Like, go literally solve 100 puzzles. Yes, literally 100.
You will learn things. You will get better. It'll just happen. It's part of the
magic of the human brain.

This is a very specific example, but I play this platforming game called Dustforce,
and one level in the game has this really annoying part called the Tera section.
It's almost exactly in the middle and is easily the hardest part to beat consistently.

I complained about this in the Discord and was told to go beat the 100 Teras
custom map for practice. So I did, twice. And then I stopped complaining.

Like, I'm not going to just stop here. I will say more things! Still there's a
lot you can learn by just doing more puzzles. That's where I learned most of
how I approach puzzlehunts.

Okay, on to the actual post.


Generating Ideas
------------------------------------------------------------------------

Puzzles are often described as having "a-has" or break-in points, where it
suddenly becomes clear what you should do. How do you come up with a-has?
How do you break-in?

This really is genuinely the hardest part to give advice about. If it was
easy to come up with good ideas, we wouldn't have puzzles in the first place!
The best advice I can give is to describe the conditions that promote
idea generation.


1. Transcribe puzzle content faithfully. Refer to the original even if you think
you did.

Before you have broken into a puzzle, any part of the puzzle could be relevant
information. The act of transcribing a puzzle from a website or PDF into a
spreadsheet is often slightly destructive. Coloring, styling, or spacing is often
the first casualty. Sometimes, the parts you destroy are important to the puzzle.

So, try to make your sheet look as much like the puzzle as you can. Certain puzzles
can make this hard or annoying (I am always annoyed at puzzles that use a hex grid).
In those scenarios, do your best, but remember to look at the original puzzle if
you've been stuck for a while. I like to add a note in the spreadsheet to "see original puzzle" if I can't transcribe something exactly.


2. Take bad ideas seriously.

In general, try to follow the ["yes, and..."](https://en.wikipedia.org/wiki/Yes,_and...) rule-of-thumb from improv comedy. It's okay to conclude that an idea seems unlikely
given the evidence, but avoid concluding an idea is totally wrong. Similarly,
avoid concluding an idea is totally right. Very often, you can have 90% of the right
idea but be missing the crucial 10% needed for extraction.


3. Count things!

Off the top of my head, this is something I do more than other puzzle-people I know,
and I have usually not regretted it.

Puzzle solving often involves relating one part of the puzzle to another part.
These relations often follow whole number ratios, so if you find two parts that
have matching counts, it can imply those two parts connect together. Or if you
find clues with counts in a 2:1 ratio, it suggests you want to pair up 2 clues
from one side with 1 clue on the other.

A very simple example is [Not Quite a Polka](https://www.puzzlesaremagic.com/puzzle/not-quite-a-polka.html) from Puzzles are Magic. There's two sections of clues, and 13 clues
in each section, so the puzzle is likely about solving both and combining the two
somehow.

Another example is [Oxford Children's Dictionary](https://puzzles.mit.edu/2022/puzzle/oxford-childrens-dictionary/) from MITMH 2022. We see there are an equal number
of clues in the Standard Dictionary Definitions column, and the Oxford Children's
Dictionary Definitions column (19 of each), so the two are likely related.
Each clue has a blank, meaning 38 blanks total. The grid below the clues has 38 words in
it, so this suggests we want to fill each blank with a word.

A more complicated example is [Cryptic Command](https://2018.galacticpuzzlehunt.com/puzzle/cryptic-command.html) from GPH 2018.
There are many steps to the puzzle, but we can start by noticing that for each
card, the number of cryptics on that card matches the number of circles in the
top right of that card. So we can start by solving the cryptics, and finding
some way to relate each cryptic to a circle. (If we know enough about the
Magic: the Gathering reference to know what appears in those circles on a real
card, it's a pretty helpful hint for the next step.)

Note that we can make all these guesses before doing any clue solving! In fact
this is how we solved Oxford Children's Dictionary during the actual hunt, it
took us 10 minutes to get a single clue solved but we correctly guessed all
the mechanics of the puzzle before doing so.

If you do decide to count things, make sure to follow through. When testsolving
[Light Show](https://2021.teammatehunt.com/puzzles/light-show) from Teammate Hunt 2021,
I decided to commit to counting every square, and broke in on finding there were
exactly 133 squares, which was exactly 7 * 19, and there happened to be a set of
19 7-long objects [elsewhere](https://2021.teammatehunt.com/puzzles/tumbled-tower).

4. Monospace and spreadsheet conventions are your friend.

A lot of puzzles will use length as part of the structure. For example, ADD EXAMPLES HERE.
Whenever you have a list of clues, I'd recommend putting the corresponding "answer"
column in monospace, to make it more visually clear if answers are the same length,
are all of unique length, etc.

The team I hunt with (teammate) goes a bit further with their spreadsheet conventions,
which are:

* Clues in non-monospace, answers in monospace, to keep it clearer which is which.
* Use bold or highlighting to indicates answers you think are important
* Answers in uppercase by default.
* Write answers in lowercase or add a question mark if you aren't confident in
the answer.
* Arrange items of the same "type" (clue, answer, etc.) in columns to make it
easier to sort by them later.

I don't *fully* agree with these conventions. (I prefer keeping everything in monospace,
on occasion lengths within clues are relevant and I broke into the last step
of [Sheep](https://puzzles.mit.edu/2020/puzzle/sheep/) from MITMH 2020 this way.)
However, they are generally helpful to have, since it makes the mental state of
the puzzle more visually apparent. If some clue answers are marked as uncertain,
you can feel more confident ignoring them when trying to generate ideas of how
extraction works.


Testing Ideas Efficiently
------------------------------------------------------------------------
