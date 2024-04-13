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


Evaluating and Testing Ideas
------------------------------------------------------------------------

Although I've separated the sections into idea generation and idea testing, in most
solve experiences you are doing both at the same time. Generally it's easier to figure out
what to do if you have more data, and it's very fine to do work (solve clues) without
knowing exactly what you're looking for, on faith that you will figure out the next step
later.

ADD DIAGRAM FOR THIS

1. If you can't extract, look for unused information

Not all puzzles will use all channels of information they present to you. This is true of
good puzzles too! But many puzzles will *try* to use all information presented, because puzzles
that do so tend to be higher quality with cleaner solve paths.

So when trying to understand what the puzzle's asking you to do, it can help to take a step back
and consider if you haven't used some part of the puzzle yet.

2. If you can't extract, look for missing information

To me, this is slightly distinct from unused information. Unused information is when you know there
are aspects of the puzzle dataset you haven't used yet. Missing information is when the information
you need doesn't even exist in your spreadsheet, and needs an a-ha to figure out. An example would be if,
say, you needed to realize that every paragraph of text was secretly referencing a movie from pop-culture.

If you're having trouble getting something to extract, then it's likely you're missing something that's
needed for extraction. The longer you're stuck, the more likely it is that's true. This is where tools like
qhex's extraction helper, spreadsheet formulas, and code can help a lot. Once you transcribe the dataset once,
using formulas for indexing makes it easy to try many permutations or variants of indexing (index column B
instead of A, reverse the ordering, etc). And that makes it easier to exhaust the possibility space, which
brings you to the "we need to find something new" step faster.



2. Overconstrained

This is a concept that's common to a lot of mindsports: **puzzles do not arrive spontaneously,
they are created by people to have a solution.** As you come up with ideas on how a puzzle
works, each of those ideas applies a constraint to the puzzle. For example, if we see a
rose garden puzzle, it's a safe bet that answers for the roses are 6 letters long.

IMAGE

(This might not be the case if the puzzle is doing something funny for extraction, but let's ignore that for now.)

We say a working theory is **overconstrained** if it would be impossible or very difficult to
construct the puzzle such that the working theory is true. All answers being 6 letters is fine.
If the constraints were something like, "all clue answers are 6 letter and are names of colors", that's
harder, but possible. If it went up to "all clue answers are 6 letters, names of colors, and start with the letter Y",
that theory is probably wrong, since it's overconstrained - the only option is like, YELLOW.

Essentially, the logic is:

* This puzzle is constructable, because I'm looking at it.
* If this overconstrained theory X is how the puzzle works, it would not be possible to construct this puzzle.
* Therefore, that theory X shouldn't be how the puzzle works.

Applying this correctly can let you avoid checking ideas that are implausible in the first past, which lets
you move faster.

Now, sometimes this bites you badly, if you assume a construction is impossible when it isn't.
This happened to my team when solving [Highway Patrol](https://darocaro.github.io/puzzles/highwaypetrol/highwaypetrol)
from the DaroCaro hunt. In this puzzle, you solve a Sudoku puzzle, and eventually get to the cluephrase MIDDLES.
This indicated using the middle cells of each 3x3, but we failed to extract from this for a long time. It turned
out the answer was to convert each middle number using A=1 Z=26. The reason our team got stuck here was
that we were a bit *too* experienced. Since the sudoku digits range from 1 to 9, doing A=1 Z=26 would have forced
a message only using letters from A to I, and that just seemed impossible, so we ignored that idea and kept trying
to interpret the values as indices instead.


3. Prioritize important clues

If you see an extraction like ?N?WE???????, many solvers I know will assume the first 6 letters are going to spell
ANSWER, they're on the right track, and will stop work extracting any of the first 6 letters unless they get stuck.

This is a special case of trying to find the "high information" letters. If I see an extraction like ?????I?G,
I'll usually assume it's going to end "-ing" and skip extracting the blank between the I and G. This can be especially
powerful when combined with word search tools like Qat or nutrimatic. In general, long runs of blanks lead to
more valid words, so it's good to target letters near the middle of long runs. (This also means that if I run into
trouble solving a given blank, I'm *very* likely to immediately jump to the next blank, since I trust nutrimatic to
wheel-of-fortune around that missing letter most of the time.)

One more specific thing I like to do is that when I see a crossword puzzle, I'll try to solve the proper nouns first,
because they're easy with a search engine, and are just a little more likely to involve constrained letters that forced
the constructor to use a proper noun.


4. Look for pieces of confirmation early.

In sudoku puzzles, there's this idea called "the deadly pattern".

SUDOKU

In this image, we can switch the assignment of digits to get 2 valid solutions, no matter what the rest of the grid
looks like. Since sudoku puzzles are constructed to have a unique solution, if we see such a deadly pattern, we
know we've made a mistake somewhere and should back up. Generally, you do not need to assume a unique solution
to solve a logic puzzle, but assuming there is one can act as a guardrail.
(There are exceptions - see this [sudoku featured on Cracking the Cryptic](https://www.youtube.com/watch?v=qJliK881Leo).)

There's analogue in puzzlehunting too. A common convention in puzzles is to have answers be in alphabetical order.
Usually I will check if data's consistent with alphabetical order *very* early (when ~20% of clues are solved), because knowing this early
speeds up the solve.

To draw an analogy to transportation, traffic lights and rules don't exist to slow you down, they exist to speed you up.
Guardrails are there to make your solve more streamlined - find them and use them!


Executing Faster
----------------------------------------------------------------------

1. Look for the next step early.

In my opinion this is the major thing that separates experienced puzzlehunters from new ones.
New puzzlers tend to solve puzzles in a waterfall style. They solve all the clues, then figure out the next steps.
Whereas experienced puzzlers tend to lookahead more, thinking about what to do next or how to extract pretty early.

I don't want to imply new puzzlers are wrong to solve this way. It's hard to lookahead if you don't have
the experience to know how puzzles tend to work. But in general, I think it's helpful to consider *what you're doing*
when you have enough data to potentially figure it out. My rough heuristic is to try doing this after doing 50%-70%
of the work, although this will adjust depending on how much error correction is possible.

The reason it's worth checking early is because sometimes it gives you extra constraints that helps you
solve clues. It's a bit like backsolving a metapuzzle, but at smaller scale. Sometimes you can entirely skip clues if
you figure out extraction early enough to get the answer to show up in nutrimatic or Qat. One way to solve puzzles
faster is to just do less work to solve them.

I should also mention that you don't *have* to do this. I know some very strong solvers who will 100% puzzles
by default. They'll still look ahead, but will solve all the clues before doing the next step they figured out
10 minutes ago. A lot of the time, puzzle solvers derive enjoyment from seeing how it all comes together, with
emphasis on the **all**. I do too!
