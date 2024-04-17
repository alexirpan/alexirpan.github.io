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
ideas about how a puzzle might work, quickly testing those ideas to check how
well they fit, and executing well on the correct ideas.

To generate more ideas, solve more puzzles to see what ideas have shown up in
past puzzles.

To test ideas faster, solve more puzzles to see what lets you conclude an
idea is wrong, and try to shortcut to that on the next puzzle.

To execute better, practice by solving more puzzles, ideally with other
people so you can copy their tricks.


Wait This Seems Too Simple
-----------------------------------------------------------------

Nah that's pretty much it.

The very common story is that if you want to get good at a skill, just do
it a bunch. Like, go solve 100 puzzles. No I don't mean 10. Do literally 100 puzzles.
You will learn things. You will get better. It'll just happen. It's part of the
magic of the human brain.

This is a very specific example, but I play this platforming game called Dustforce.
I was trying to beat one very hard level, which has a part called the Tera section.
It's almost exactly in the middle, has the tightest timing window, and is easily
the least favorite part of the level.

I complained about this in the Discord and was pointed to the meme map of "100 Teras",
a custom map that copy-pastes the section 100 times in a row. "Go beat 100 Teras."
So I did, twice. And then I stopped complaining.

If you go solve 100 puzzles you may not need this post. I'm still going to write it
anyways, but puzzle solving is really an activity where you learn more by doing than
reading.

Okay, on to the actual post.



Starting a Puzzle - Generating Ideas
------------------------------------------------------------------------

Puzzles are often described as having "a-has" or break-in points, where it
suddenly becomes clear what you should do. How do you come up with a-has?
How do you break-in?

This is genuinely the hardest part to give advice about. If it was
easy to come up with good ideas, we wouldn't have puzzles in the first place!
So I've decided to interpret the question differently: how do you create
the best conditions that cause good ideas to arise?


1. Use monospace

A lot of puzzles will use length as part of the structure. For example, [Human Pyramid](https://2021.teammatehunt.com/puzzles/human-pyramid) from Teammate Hunt 2021.
Patterns in length (matching length, exactly one letter longer, etc.)
are easy to subconsciously notice if you put content in monospace, so if you put your spreadsheet
in monospace by default, you'll spot those patterns faster.

(In fact, the monospace font
in Human Pyramid was added during testsolving to push solvers to consider length. A similar trick
was used in [Pestered](https://puzzles.mit.edu/2018/full/puzzle/pestered.html) from MIT Mystery Hunt 2018.)

Personally I like to put literally everything in monospace, but I know some solvers
who prefer only putting clue answers in monospace and leaving clues in sans serif,
to create a subconscious visual boundary between clue and answer. You can pick which one
works for you.


2. Transcribe puzzle content faithfully. Refer to the original puzzle even if the sheet
looks complete.

Before you have broken into a puzzle, any part of the puzzle could be relevant
information. The act of transcribing a puzzle from a website or PDF into a
spreadsheet is often slightly destructive. Text styling and spacing are often
the first casualties. Usually this is fine, but every now and then the parts lost during
transcription are important to breaking in.

So, try to make your sheet look as much like the puzzle as you can. Certain puzzles
can make this hard (shoutouts to every puzzle with a triangular or hex grid).
In those scenarios, do your best, but add a note to "see original puzzle" in the spreadsheet.
And remember to look at the original puzzle if
you've been stuck for a while, to see if there's something about the presentation you
missed.


3. Speak your bad ideas aloud and take them seriously

Puzzle solving is a collaborative activity, and people won't know what ideas you have if you
don't speak up. It's okay to caveat that your idea is bad if you say it anyways.
In general, try to follow the ["yes, and..."](https://en.wikipedia.org/wiki/Yes,_and...) rule-of-thumb from improv comedy,
and avoid entirely ruling out ideas. Just mentally mark them as unlikely.
Sometimes you will have 90% of the right idea and be missing the last 10%. Other
times you will have the half-baked 10% of the right idea, and someone else will have the 90%.
To get to 100% of the idea, one person needs to communicate, and you want to have a culture
where the 10% person is willing to volunteer ideas.


4. Count things!

Off the top of my head, I do this a ton, I feel I do this more than most puzzle-people, and I
haven't regretted it.

Puzzle solving often involves relating two parts of the puzzle together.
These relations often follow whole number ratios. If there are N items in both parts,
it suggests matching between those parts. If there's N items in one and 2N in another,
that could mean matching 1 item from the first part with 2 items from the second.

A very simple example is [Not Quite a Polka](https://www.puzzlesaremagic.com/puzzle/not-quite-a-polka.html) from Puzzles are Magic. There's two sections of clues, and 13 clues
in each section, so the puzzle is likely about solving both and combining the two.

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
this is how we solved Oxford Children's Dictionary during the actual hunt. It
took us 10 minutes to get a single clue solved, but we correctly guessed all
the mechanics of the puzzle before doing so.

Counts can also let you draw negative conclusions. If you have 7 clues in one
part and 10 clues in the other, you are not going to do a 1:1 matching, so you can
immediately discard puzzle ideas along those lines.

I'd call this the numerology of the puzzle. At the start of a puzzle,
quickly count the most salient parts of the puzzle, and keep any interesting
correspondences in mind. This can be surprisingly powerful.
When testsolving
[Light Show](https://2021.teammatehunt.com/puzzles/light-show) from Teammate Hunt 2021,
we knew it corresponded to [Tumbled Tower](https://2021.teammatehunt.com/puzzles/tumbled-tower)
in some way, but weren't sure on the rules for how it'd do so. So after we did
some work I decided to commit to counting every square in the Light Show grid,
found there were 133 of them, noted this equaled 7 * 19, and there were 19 septaminos
in Tumbled Tower. This let us conclude not only that we should try using those
septaminos, it also let us know we shouldn't allow overlaps or gaps.


5. Search everything

Honestly, a lot of puzzle solving is about taking random parts of the puzzle and throwing it
into a search engine. Search the flavor text. Search just half of the flavor text. Add quotation
marks to do exact phrase searches. Pick one key word from each part of the puzzle, search that, and
if that fails randomly drop out some words and try again.

There are a lot of variables you can tweak in your search engine queries, and the heuristic I use is
that if there aren't obvious starting points, I will search the puzzle title, the flavortext, all proper nouns, and
anything that doesn't read like typical English. I'll also mix the theme of the puzzlehunt into search queries if
I think it could turn up something new.


6. Ask if an idea's overconstrained

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


Middle of a Puzzle - Moving Faster
----------------------------------------------------------------------

By this point, we have some idea of how the puzzle works, and are in the phase of answering clues and making
deductions. Our goal is to get enough data to continue the puzzle. This section is about
the mechanics of how to progress through clues quickly.


1. Consider extraction or the next step early.

In my opinion this is the major thing that separates experienced puzzlehunters from new ones.
New puzzlers tend to solve puzzles in a waterfall style. When given a list of clues, they fully solve the clues, then
start thinking about what to do with those answers.
Whereas experienced puzzlers lookahead more, thinking about what to do next while solving the clues.

I don't want to imply new puzzlers are wrong to solve this way. It's hard to lookahead if you don't have
experience to know how puzzles tend to work. But in general, I think it's helpful to consider *what you're aiming for*
when you have enough data to potentially figure it out. My rough heuristic is look into this after having 50% of the work
done, but this depends a lot on how much I know about the structure of the puzzle from my initial counting.

The reason it's worth looking for the next step early is because sometimes it gives you extra constraints that helps you
solve clues. It's a bit like backsolving a metapuzzle, but at smaller scale. Sometimes you can entirely skip clues if
you figure out extraction early enough to get the answer to show up in nutrimatic or Qat. One way to solve puzzles
faster is to just do less work to solve them.

I should also mention that you don't *have* to do this. I know some very strong solvers who will 100% puzzles
by default. They'll still look ahead, but will solve all the clues before doing the next step they figured out
10 minutes ago. Several puzzle solvers derive enjoyment from seeing how it all comes together, with
emphasis on the **all**. Personally, I only do this if I'm having a ton of fun with the puzzle, otherwise I'll
move on.


2. Look for pieces of confirmation early

In sudoku puzzles, there's this idea called "the deadly pattern".

SUDOKU

In this image, we can switch the assignment of digits to get 2 valid solutions, no matter what the rest of the grid
looks like. Since sudoku puzzles are constructed to have a unique solution, if we see such a deadly pattern, we
know we've made a mistake somewhere and should back up. Generally, you do not need to assume a unique solution
to solve a logic puzzle, but assuming there is one can act as a guardrail.
(There are exceptions - see this [sudoku featured on Cracking the Cryptic](https://www.youtube.com/watch?v=qJliK881Leo).)

There's analogue in puzzlehunting too. A common convention in puzzles is to have answers be in alphabetical order.
Usually I will check if data's consistent with alphabetical order *very* early (when ~20% of clues are solved), because
knowing this early speeds up the solve.

To draw an analogy to transportation, traffic lights and rules don't exist to slow you down, they exist to speed you up.
Guardrails are there to make your solve more streamlined - search them out and use them!


3. Do the easy parts first.

When I see a crossword puzzle, I like to solve the proper nouns first. With a search engine, these are usually both
easy and unambiguous. Some parts of a puzzle will yield more easily than others, and it's usually worth doing a quick
once-over of a puzzle to see if anything stands out.

(In fact, many puzzles are constructed to have a foothold like this, empirically it's more fun if solvers can make some
progress before breaking in.)


4. Prioritize important clues

If you see an extraction like ?N?WE???????, many solvers I know will assume the first 6 letters are going to spell
ANSWER and will stop extracting any of the first 6 letters unless they get stuck.

This is a special case of trying to direct work towards the "high information" areas. Some general wheel-of-fortune
skills are helpful here: if I see an extraction like ?????I?G, I'll usually assume it's going to end "-ing" and skip extracting the blank between the I and G.
This can be especially
powerful when combined with word search tools like Qat or nutrimatic. In general, these tools have trouble with
long runs of blanks, but are very good at filling short gaps, so if you know what order things will extract, it's
good to target letters towards the middle of long runs of blanks.

There are a lot of downstream effects of this idea. For example, after breaking into a puzzle, I'll often declare
that I'll work from the bottom, because most people will start from the top, and it's better to distribute work
throughout a cluephrase rather than concentrate it all at the start. Similarly, if I get stuck on a clue,
I'm very willing to skip it for the next one, trusting nutrimatic or Qat will fill in the blank.

Importantly, **you can't tell which parts of a puzzle are important unless you have guesses on how you're going to use them**. Which
is another reason I value looking ahead on extraction so highly - you need to do some of it to priotize in the first place.


5. Use spreadsheet formulas for extraction

I spent a very long period of my puzzling career indexing entries by hand. Eventually I decided to learn spreadsheet
formulas and now I can't go back.

Spreadsheet formulas have several advantages:

* They're consistent. You can't mess up a count or typo a letter. (You can typo a spreadsheet formula, but usually spreadsheet formula typos lead to errors rather than incorrect letters.)
* They're automatic. Once you have extraction driven by spreadsheet formula, you can stay in a flow of IDing and
solving without detouring into extracting, reducing time lost to context switching.
* Due to being automatic, they can show you partial cluephrases you weren't looking for.

Also, being good at spreadsheet formulas is by far the most transferrable skill to real life.
The business world runs on Excel. The very basic actions you'll do over and over in puzzlehunts:

* `=MID(A1, k, 1)` takes the $k$th letter of A1
* `=REGEXREPLACE(A1, "[^A-Za-z]", "")` removes all non A-Z characters.
* `=CHAR(A1 + 64)` will convert 1 to 26 into A to Z.
* `=CODE(A1) - 64` will convert A to Z into 1 to 26.
    * If you can't remember 64, you can do `CODE('A') - 1` instead

It's also worth understanding relative references vs absolute references. If I typed
`=MID(A1, B1, 1)` into cell C3, this is a relative reference. Internally, the spreadsheet
stores `=MID(the cell 2 left + 2 up, the cell 1 left + 2 up, 1)`. Dragging a formula will
copy-paste that logic to every cell, but will visually display the cell it refers to in
the highlighted cell.

IMAGE

and drag the formula down, it will auto adjust for each row.

ANIMATION

If you want a formulate to always refer to a specific cell, you can use $ to indicate an absolute
reference. This can be applied to either the column, row, or both.

Examples:

Indexing many columns with the same indices: `=MID(A1, $B1, 1)`. When dragged, this always uses
column B for indexing, but will allow the row to change.

ANIMATION

Indexing the same word with many indices: `=MID($A$1, B1, 1)`.

ANIMATION

The spreadsheet rabbit hole goes very deep. I recommend
[You Suck at Excel](https://www.bilibili.com/video/BV1734y187KS/) by Joel Spolsky as a classic
spreadsheet introduction, and [Yet Another Puzzlehunt Spreadsheet Tutorial](https://docs.google.com/spreadsheets/d/1-KmLvmcydguI_RBJJqHihbewZmssmdNtlWFJIJZVXLk/edit#gid=0)
by betaveros for a more puzzlehunt-focused guide. (You Suck at Excel recently disappeared off
YouTube - the link above is a bilibili mirror.)


6. Use code for more complicated extraction.

(If you can't program, ignore this.)

Sometimes, you hit the limits of what spreadsheets can do. In these scenarios, it can be pretty
helpful to write code trying more complex extractions or searches. If you know how to program,
I recommend downloading a wordlist (Scrabble dictionary is a good target), and writing some basic
functions for A1-Z26, morse, and so on. I have a codebook where I save all code snippets I've
written from past hunts that I think could be reused later, but if you're new to puzzlehunt
coding a good starting place is [solvertools](https://github.com/rspeer/solvertools).

You won't need to pull out Python to do A1-Z26 conversion if you know spreadsheet formulas,
but the power of having basic encodings implemented in code is that **it makes it possible
to write brute force searches**. Once, I was solving a metapuzzle from a now-offline hunt.
Based on flavor, we were very confident it was going to be about Morse code, each of our feeder
answers would be a dot or dash, and we'd read out a message from doing so. We couldn't figure
out how to do so, but the round had 7 puzzles, so I decided to write a script to brute force
the Morse for all 2^7 = 128 possibilities. This worked.

One advantage of code is that although it's higher up-front cost, if you write code that
exhaustively checks all possibilities, and it still fails to extract the puzzle, then you
know for sure that your extraction idea is wrong and it's time to try something else.


Getting Unstuck
------------------------------------------------------------------------

Everyone gets stuck on puzzles. The question is what to do about it.


1. Do a different puzzle.

There's no shame in abandoning a puzzle for now and coming back to it later. It's very
easy to tunnel vision too hard on a problem.

However, there is a certain art to this. Puzzles are normally done in teams. If you abandon
a puzzle, it's good to make a clean copy of the sheet, where you organize and explain the work
done so far. In this clean copy, you should try to remove all the speculative half-baked ideas
you had. Given that you're stuck, it's more likely you're in the wrong rabbit hole, and you should
try to avoid biasing future solvers into the same rabbit hole. If those future solvers come to the
same conclusions you did, then you can treat it as evidence you're on the right track.

2. Check your work.

I have seen so, *so* many times where a puzzle was stuck because of a silly mistake. **Check your
work.** Cannot overstate this enough.

3. Look for unused information

Not all puzzles will use all channels of information, but most puzzles will try to do so.
Try enumerating everything that has and hasn't been used yet.

4. Look for missing information.

To me, this is slightly distinct from unused information. Unused information is when you know there
are aspects of the puzzle dataset you haven't used yet. Missing information is when the information
you need doesn't even exist in your spreadsheet, and needs an a-ha to figure out.

The longer a sheet stays unextracted, the more likely it is that the sheet is fundamentally missing
the information needed to extract. I'm a big fan of [qhex's extraction basher](https://tools.qhex.org/),
which will try a wide battery of indexing and ordering mechanisms. It's not that robust to errors, but
it's a good way to check the likelihood your spreadsheet is missing a column. If you're confident your
sheet is clean, without errors, and qhex doesn't extract it, you're missing a column of info.


5. Consider what would be thematic

Puzzlehunts usually have a theme, and although most puzzles will not rely on that theme for their a-ha,
some of them will. Consider ideas in line with the title or theme of the hunt.


5. Assume a few errors

To err is to be human. If you don't like a few letters, you can always pretend those were solved wrong
and switch them to wildcards in nutrimatic.

It's important not to overdo this, but getting good at error correction can really take you quite far.
This can extend past the single letter case as well. Sometimes I Caeser shift gibberish text to check
if our indices are all off-by-one.


6. Cheese

For the uninitiated, cheesing a puzzle means to solve it through an unintended path. This comes from
video game slang, where it usually means you're breaking the game's design or intended play experience.

This can be a little controversial...it's a bit subversive, and in my opinion hardening a puzzle
against cheese can sometimes make it worse. I view it the same as backsolving - it's a ton of fun
if it works, but it wouldn't be nearly so fun if it worked all the time.

Here are common cheese tactics:

* If you don't know how to order, you can try random anagramming. (too many to name)
* If you have an ordered list of words, but don't know the indices, you can construct a regular expression
to take one letter from each word and see what possibilitiese show up in nutrimatic.
(2020 coding puzzle)
* Similarly, if you have an ordered list of indices, know what words you're indexing, but don't know how they
match up, you can also construct a regex. If the index is (3), you make a regex of every 3rd letter among your set.
(shard hunt) (I broke [Mouth Mash](https://2020.teammatehunt.com/puzzles/mouth-mash) this way in testsolving
and the puzzle was redesigned to make that harder.)
* If enumerations are given for a multi-word phrase, sometimes the enumeration itself is enough to constrain
the phrase. You can use OneLook or nutrimatic to check for this.
For example, (2 2 2 3 2 2 4 2 3 8) only has [one notable match](https://nutrimatic.org/2024/?q=%22AA+AA+AA+AAA+AA+AA+AAAA+AA+AAA+AAAAAAAA%22&go=Go).
