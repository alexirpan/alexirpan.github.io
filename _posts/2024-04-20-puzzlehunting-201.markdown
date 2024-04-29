---
layout: post
title:  "Puzzlehunting 201"
date:   2024-04-20 01:41:00 -0700
---

I'm good at puzzlehunts. I thought about equivocating this, saying I *think* I'm
good at puzzlehunts, or relatively good at puzzlehunts, but I've been on a winning
MIT Mystery Hunt team twice and recently was on the 2nd place team for the
[Who Killed Ickey?](https://ickeytreasurehunt.com/leaderboard) treasure hunt.
These were definitely team efforts, but I know I made significant contributions to both.

Those hunts
cover the spectrum between puzzlehunts where the bottleneck is
break-ins (Mystery Hunt), and ones where it's more about pure execution speed (Ickey).
After doing puzzlehunts for well over a decade, I've picked up some habits I'd like
to share.

**If you are new to puzzlehunts, you are not the target audience of this post.** I mean, feel
free to keep reading! But I will be assuming a bunch of background knowledge and
won't be trying to explain what a puzzle is or what a meta is and so forth. If
you're new, I recommend [Introduction to Puzzlehunts](https://blog.vero.site/post/puzzlehunts)
instead.

**If you've done many puzzlehunts, not everything I say here will work for you.**
Puzzlehunting systems are a little like productivity systems: everyone's is
different, and people can be very opinionated
about them even if they all share common themes. Your best bet is to try things out, take the parts that work,
and ignore the parts that don't.

**You don't have to get faster at puzzles.**
I like going fast because I've solved enough puzzles that I want to quickly get through
grunt work to see the next a-ha.
To a lesser extent, I find
it fun to see how little information I can get away with when solving a puzzle.
That's not a universal opinion.
Most people will have
more fun if they solve puzzles than if they don't, but you don't have to solve puzzles
*quickly* to have fun.

**This will spoil a few puzzles.** I've tried to keep the spoilers as light as needed,
but it's much easier to give real-life examples than to construct new puzzles just for
the sake of this post. (Then again, imagine if this post was written entirely to seed content
for an upcoming puzzlehunt. Boy would that be interesting! Seriously though, it's not.
You're welcome to look, but you won't find anything.)


The One Minute Version
-------------------------------------------------------------------

Puzzle solving can be divided into generating ideas for how a puzzle works,
and executing well on those ideas.

To generate more ideas, solve more puzzles to see what's shown up in
past puzzles, and try similar things.

To execute better, practice by solving more puzzles.


Wait, This Seems Too Simple
-----------------------------------------------------------------

Nah, that's pretty much it.

The very common story is that if you want to get good at a skill, just do
it a bunch. Like, go solve 100 puzzles. No, I don't mean 10, or 20. Stop reading and
go solve literally 100 puzzles.
You will learn things. You will get better. It'll just happen. It's part of the
magic of the human brain.

This is a very specific anecdote, but I play a platforming game called *Dustforce*.
There's one very hard level in the game which has a part called the Tera section.
It's almost exactly in the middle of the level, and is easily the most difficult part to clear.

I complained about this in the Discord and was told that yes, it's awful, but was
then directed to "100 Teras", a custom map that's just 100 copies of the Tera section with a checkpoint between each one.
"If you're really having trouble, go beat 100 Teras". So I did, twice. And then I stopped
complaining.

If you go solve 100 puzzles, you may not need this post. I'm still going to explain the
solving strategies I've learned, but puzzle solving is really an activity where you
learn by doing.

Okay, on to the real post.


Starting a Puzzle - Generating Ideas
------------------------------------------------------------------------

Puzzles are often described as having "a-has" or break-ins, where it
suddenly becomes clear what you should do. How do you come up with a-has?
How do you break-in?

This is genuinely the hardest part to give advice about. If it was
easy to break-in, we wouldn't have puzzles in the first place!
So I've decided to interpret the question differently: how do you create
conditions that cause good ideas to arise? And how do you decide if those
ideas are actually good?

#### Use spreadsheets

Collaboratively editable spreadsheets (typically Google Sheets) are the lingua fraca of
puzzlehunting. Please use them.

#### Keep clean spreadsheets

We're going to immediately start with a point of contention, because what "clean"
means is never the same person-to-person, and people can be very opinionated on
sheet hygiene.

![xkcd comic about mess](/public/puzzlehunting-201/mess.png)
{: .centered }

[(From xkcd)](https://xkcd.com/1267/)
{: .centered }

The bare minimum that I think is unobjectionable is:

* Make a new sheet for each puzzle
* Put info of the same type in the same locations
* Use a monospace font

The first two are just common sense.
As for monospace, a lot of puzzles will use word length as part of the structure. [Human Pyramid](https://2021.teammatehunt.com/puzzles/human-pyramid) from Teammate Hunt 2021 is
a good example of this.
Patterns in length (matching length, exactly one letter longer, etc.)
are easier to notice if you put content in monospace, so using those fonts can help you
break-in on those patterns faster.

(As an aside, Human Pyramid is displayed in monospace font specifically to encourage solvers to consider length. A similar trick
is used in [Pestered](https://puzzles.mit.edu/2018/full/puzzle/pestered.html) from MIT Mystery Hunt 2018.)

Personally, I like to put everything in monospace, but I know some solvers
who prefer only putting clue answers in monospace and leaving clues in sans serif, since
they value the visual boundary between clue and answer. Pick whichever works for you.


#### Transcribe puzzle content faithfully

Before you have broken into a puzzle, any part of the puzzle could be relevant
information. The act of transcribing a puzzle from a website or PDF into a
spreadsheet is slightly destructive. Text styling and spacing are often
the first casualties. Usually this is fine, but every now and then the parts lost during
transcription are important to breaking in.

So, try to make your sheet look as much like the puzzle as you can. Certain puzzles
can make this hard (shoutouts to every puzzle with a triangular or hex grid).
In those scenarios, do your best, but add a note to "see original puzzle" in the spreadsheet.
And remember to look at the original puzzle if
you've been stuck for a while, to see if there's something about the presentation you
missed.


#### Share your bad ideas

Puzzle solving is a collaborative activity, and people won't know what ideas you have if you
don't share them. It's okay to caveat that your idea is bad, but share it anyway.
Try to follow the ["yes, and..."](https://en.wikipedia.org/wiki/Yes,_and...) rule-of-thumb from improv.
Sometimes you will have 90% of the right idea and be missing the last 10%. Other
times you will have the half-baked 10% of the right idea, and someone else will have the 90%.
To get to 100% of the idea, one person needs to communicate, and you want to have a culture
where both the 10% person and 90% person can be the one who communicates first.


#### Count things!

Off the top of my head, I do this a ton, I feel I do this more than most solvers, and I
haven't regretted it.

Puzzle solving often involves relating two parts of the puzzle together.
These relations often follow whole number ratios. If there are N items in both parts,
it suggests matching between those parts. If there's N items in one and 2N in another,
that could mean matching 1 item from the first part with 2 items from the second.
If there's 26 of something, it could mean A1-Z26.

A very simple example is [Not Quite a Polka](https://www.puzzlesaremagic.com/puzzle/not-quite-a-polka.html) from Puzzles are Magic. There's two sections of clues, and 13 clues
in each section, so the puzzle is likely about solving both and combining the two.

Another example is [Oxford Children's Dictionary](https://puzzles.mit.edu/2022/puzzle/oxford-childrens-dictionary/) from MIT Mystery Hunt 2022. There
are 19 clues in both the Standard Dictionary section and Oxford Children's section, so we
likely relate the two, and there are 38 words in the bottom grid to fit into 38 blanks
in the clues, suggesting we fill each with a word.

A third example is [Cryptic Command](https://2018.galacticpuzzlehunt.com/puzzle/cryptic-command.html) from GPH 2018.
There are many steps to the puzzle, but we can start by noticing that for each
card, the number of cryptics on that card matches the number of circles in the
top right of that card. So we should probably relate each cryptic to a circle.
(If we know enough about the *Magic: the Gathering* reference, this already provides
some hint for what the cryptics will resolve to.)

Note that we can make all these guesses before doing any clue solving! During
Mystery Hunt, it took us about 10 minutes to get our first clue in Oxford Children's
Dictionary, but we already correctly guessed all the mechanics of the puzzle
before doing so.

Counts can also let you draw negative conclusions. If you have 7 clues in one
part and 10 clues in the other, you are not going to do a 1:1 matching, so you can
immediately discard trying a 1:1 match and think of doing something else.

I call this the numerology of the puzzle. At the start of a puzzle,
quickly count the most salient parts of the puzzle, and keep any interesting
correspondences in mind.
When testsolving
[Light Show](https://2021.teammatehunt.com/puzzles/light-show) from Teammate Hunt 2021,
we knew it corresponded to [Tumbled Tower](https://2021.teammatehunt.com/puzzles/tumbled-tower)
in some way, but weren't sure on the rules for how it would work. So
I decided to count every square in the Light Show grid.
There were 133 of them, which was 7 * 19, matching the 19 [heptominos](https://en.wikipedia.org/wiki/Heptomino)
in Tumbled Tower. We already suspected we'd use the heptominos in some way, but counting let
us conclude that they should fit exactly with no overlaps or gaps.


#### Search everything

Honestly, a lot of puzzle solving is about taking random parts of the puzzle and throwing them
into a search engine. Search the flavor text. Search just half of the flavor text. Add quotation
marks to do exact phrase searches. Search all your answers together and see if something shows up.
Randomly drop out words from all of the previous searches and try again. Experiment with more than one tool - anecdotally,
I've found LLMs are amazing at pop culture ID, despite the hallucinations.

There are a lot of variables you can tweak in your search engine queries. The heuristic I use is
that if there aren't obvious starting points, I will search the puzzle title, the flavortext, all proper nouns, and
any phrases that don't read like typical English. I'll also mix the theme of the puzzlehunt into
search queries if I think it could turn up something new.


#### Ask if an idea's overconstrained

Puzzles do not arise spontaneously, they are created by people to have a solution.
As you come up with ideas on how a puzzle
works, each of those ideas applies a constraint to the puzzle. For example, if we see a
rows garden puzzle, it's a safe bet that answers for the blooms (the colored hexagons) are 6 letters long.

![Rows garden grid](/public/puzzlehunting-201/rows-garden.png)
{: .centered }

(This might not be the case if the puzzle is doing something funny for extraction, but let's ignore that.)

We say an idea is *overconstrained* if it would be impossible or very difficult to construct a puzzle
that worked that way. All answers being 6 letters is easy. All answers being 6 letter words for colors
is harder, but maybe possible. If all answers had to be 6 letter words of colors that start with Y, that's
definitely overconstrained, because after YELLOW you really don't have many options.

The logic goes like this:

* The puzzle is constructible, because I'm looking at it.
* If this overconstrained theory X is how the puzzle works, it would not be possible to construct this puzzle.
* Therefore, X can't be how the puzzle works.

Applying this can speed up your solves by letting you skip checking ideas that are implausible.

Now, sometimes this bites you badly, if you assume a construction is impossible when it isn't.
This happened to my team when solving [Highway Patrol](https://darocaro.github.io/puzzles/highwaypetrol/highwaypetrol)
from the DaroCaro hunt. In this puzzle, you solve a Sudoku puzzle, and eventually get to the cluephrase MIDDLES.
This suggests using the middle cells of each 3x3, and we failed to extract from this for a long time. It turned
out the answer was to convert each middle number using A1-Z26. The reason our team got stuck here was that
we all assumed that was impossible, as doing A1-Z26 on Sudoku digits forces your cluephrase to only use letters from A to I,
and surely there's no way you could do something with that, right? We kept trying to index things instead. Apply
this with caution - sometimes a constructor is just insane and figures out how to make a very constrained construction
work.


Executing Faster
----------------------------------------------------------------------

By this point, we have some idea of how the puzzle works, and are in the phase of answering clues and making
deductions. Our goal is to get enough data to continue the puzzle. This section is about
the mechanics of how to progress through clues quickly.


#### Look ahead to how the next step will work

In my opinion this is **the** major thing that separates experienced puzzlehunters from new ones.
New puzzlers tend to solve puzzles in a waterfall style. When given a list of clues, they fully solve the clues, then
start thinking about what to do with those answers.
Whereas experienced puzzlers look ahead more, thinking about what to do next while solving the clues.

I don't think new puzzlers are wrong to solve this way. It's hard to look ahead if you don't have the
experience to know how puzzles tend to work. But in general, knowing what you're aiming for can make
it easier to solve the step you're currently on, and will let you jump ahead faster.
My rough heuristic is to consider how the puzzle will work at the start of the puzzle, then again at about the
50% mark. (Although, I will adjust depending on how much fun I'm having. If I'm not having fun I will definitely
try to extract earlier to save myself from having to do more work.)

The reason it's worth looking ahead is that knowing the next step often gives you extra constraints that can make clue solving easier.
It's a bit like backsolving a metapuzzle, but at a smaller scale. Sometimes this lets you skip large chunks of
a puzzle, if you figure out extraction early enough to get the answer to show up in [nutrimatic](https://nutrimatic.org) or [Qat](https://www.quinapalus.com/qat.html).
One way to solve puzzles faster is to just do less work. I know some very strong solvers who can solve quickly
while 100%ing puzzles, but it's undeniably true that you don't need to 100% puzzles to finish them.
Personally, I only 100% a puzzle if I'm having a ton of fun, otherwise I'll move on.


#### Look for pieces of confirmation

In sudoku puzzles, there's this idea called "the deadly pattern".

![Deadly pattern](/public/puzzlehunting-201/deadly.jpg)
{: .centered }

[(Source)](http://manifestmaster.com/Sudoku_Articles/DeadlyRectangle/)
{: .centered }

Consider the red rectangle above. The corners of the rectangle are 59-95 or 95-59. Both are valid solutions, no
matter what gets placed in the rest of the grid, as switching between the two does not change the set of digits in
any of the affected rows, columns, or 3x3 boxes. Since Sudoku puzzles are constructed to have a unique solution,
if we ever see the deadly pattern, we know we've made a mistake and should backtrack.
You usually do not need to assume uniqueness to solve a logic puzzle, but assuming uniqueness can give you a guardrail.

The same is true in puzzlehunting. Answers are often alphabetical as a confirmation step, and I will usually
check alpha order *very* early (when ~20% of the clues have been solved), since knowing this early can speed up
clue answering and fix mistakes for later extraction.

To draw a transportation analogy, traffic lights and rules don't exist to slow you down, they exist to speed you up.
Guardrails are there to make your solve more streamlined - search them out and use them!


#### Do the easy parts first

When I see a crossword puzzle, I like to solve the proper nouns first. With a search engine, these are usually both
easy and unambiguous.
Clue difficulty is not uniform, and
sometimes constructors will deliberately create an easy clue to provide a foothold for the puzzle.
It's usually worth doing a quick
once-over of a puzzle to see if anything stands out. If I get stuck on a clue, I will immediately jump to the next one
and only revisit the trickier clue if needed, rather than forcing myself to do it.


#### Prioritize important clues

If you see an extraction like `?N?WE???????`, many solvers I know will assume the first 6 letters are going to spell
`ANSWER` and will stop extracting any of the first 6 letters unless they get stuck.

This is a special case of trying to direct work towards the "high information" areas. Some general wheel-of-fortune
skills are helpful here: if I see an extraction like `?????I?G`, I'll usually assume it's going to end `-ing` and skip
solving the clue for the blank between the `I` and `G`.

When combined with word search tools like Qat or nutrimatic, this can be ridiculously strong.
In general, word search tools have trouble with long runs of blanks, but are very good at filling short gaps. If I know
ordering, I'll often jump around to solving clues that reduce runs of blanks, rather than going in order.
Or, I'll declare that I'm working from the bottom when solving with a group, because most people start from the top
and it's better to distribute work throughout a cluephrase.

Importantly, **you can't tell what to prioritize if you haven't tried extracting yet**, which is why I value looking
ahead on extraction so highly.

At the hunt-wide level, this also means trying to push solves in rounds where you think it'll be important to get
more solves, either to unlock the meta or get more data for a meta.


#### Automate or find tools for common operations

Solve logic puzzles with [Noq](https://www.noq.solutions/). Use browser extensions that make it easy to take screenshots
and search images by right click (there are a few of them, I use [Search by Image](https://chromewebstore.google.com/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci?pli=1)). [Wordplays](https://www.wordplays.com/crossword-solver/) is a solid crossword clue searcher. There are too
many tools to list all of them, but the one on [puzzlehunt.net](https://www.puzzlehunt.net/tools) is pretty good.

One I would highlight is **spreadsheet formulas**.
I spent a very long period of my puzzling career not using formulas. Eventually I decided to learn spreadsheet
formulas and now I can't go back.

Spreadsheet formulas have several advantages:

* They're consistent. You can't miscount or typo a letter. (You can typo a spreadsheet formula, but usually spreadsheet formula typos lead to errors rather than incorrect letters.)
* They're automatic. Once you have extraction driven by spreadsheet formula, you can stay in a flow of IDing and
solving without detouring into extracting, reducing time lost to context switching.
* Due to being automatic, you can see exactly how much partial progress you've made on extraction, which makes
it easier to prioritize clues and check if an extraction looks promising.

Also, being good at spreadsheet formulas is by far the most transferable skill to real life.
The business world runs on Excel. The very basic actions you'll do over and over in puzzlehunts:

* `=MID(A1, k, 1)` takes the *k*-th letter of A1.
* `=REGEXREPLACE(A1, "[^A-Za-z]", "")` removes all non A-Z characters from A1.
    * If you only want to ignore spaces to worry about, `=REGEXREPLACE(A1, " ", "")` or `=SUBSTITUTE(A1, " ", "")` may be easier to remember. You usually do not need the full power of regular expressions.
* `=LEN(A1)` gives the length of the word in A1.
* `=CHAR(A1 + 64)` will convert 1 to 26 into A to Z.
    * If you can't remember 64, you can do `=CHAR(A1 - 1 + CODE('A'))` instead.
* `=CODE(A1) - 64` will convert A to Z into 1 to 26.
* `=UPPER(A1)` will put the contents in uppercase.

It's also worth understanding relative references vs absolute references. Consider this
example I just made up.

![Sheets example](/public/puzzlehunting-201/sheets1.png)
{: .centered }

The `=MID(B2, C2, 1)` in cell D2 here is a relative reference. Although the cell displays
`=MID(B2, C2, 1)`, what is actually stored internally is `=MID(2 cells left, 1 cell left, 1)`.
Dragging a formula will copy-paste that relative offset to each cell, which is usually exactly what we want.

<div class="centered">
<video width="640" controls muted>
    <source src="/public/puzzlehunting-201/drag1_muted.mp4">
    Your browser does not support .mp4 files.
</video>
</div>

In some cases, you will want to refer to a fixed position. This is called an absolute reference,
and you can do so by prepending $ to the column, row, or both.
`$B2` is an absolute ref to column B and a relative ref to row 2,
whereas `B$2` is a relative ref to column B and an absolute ref to row 2.

Examples:

Indexing multiple columns of indices: `=MID($A1, B1, 1)` locks the word to always be
from column A, while letting the word change per row.

<div class="centered">
<video width="640" controls muted>
    <source src="/public/puzzlehunting-201/drag2_muted.mp4">
    Your browser does not support .mp4 files.
</video>
</div>

Indexing a single word many times: `=MID($A$1, B1, 1)` locks the indexed word to be a specific cell.

<div class="centered">
<video width="640" controls muted>
    <source src="/public/puzzlehunting-201/drag3_muted.mp4">
    Your browser does not support .mp4 files.
</video>
</div>

As I've become more fluent in spreadsheets, I've started using them in more complex ways. For example, if the clues for a puzzle include enumeration, I'll quickly add
`=LEN(REGEXREPLACE(A1, "[^A-Za-z]", ""))` next to each answer column, to make it easier
to verify our words are matching the given lengths.
If you find you use a formula often,
you can use [named functions](https://support.google.com/docs/answer/12504534?hl=en)
to save them and import them elsewhere. (Although I confess I always forget to
set this up.)

The spreadsheet rabbit hole goes very deep. I recommend
[You Suck at Excel](https://www.bilibili.com/video/BV1734y187KS/) by Joel Spolsky as a classic
spreadsheet introduction, and [Yet Another Puzzlehunt Spreadsheet Tutorial](https://docs.google.com/spreadsheets/d/1-KmLvmcydguI_RBJJqHihbewZmssmdNtlWFJIJZVXLk/edit#gid=0)
by betaveros for a more puzzlehunt-focused guide. (You Suck at Excel recently disappeared off
YouTube - the link above is a bilibili mirror.)


#### Use code for more complicated extractions or searches

(If you can't program, ignore this.)

Sometimes, you hit the limits of what public tools can do. In these scenarios, it can be pretty
helpful to write code trying more complex extractions or searches.
I recommend downloading a wordlist (Scrabble dictionary is a good target), and writing some basic
functions for A1-Z26, morse, and so on. Any time you write one-off code, check if you think it'll
be useful for a future hunt, and save it somewhere. A good starting place is
[solvertools](https://github.com/rspeer/solvertools) for generic operations and [grilops](https://github.com/obijywk/grilops) for logic puzzles.

The power of having basic encodings implemented in code is that **it makes it possible
to write brute force searches**. Once, I was solving a metapuzzle from a now-offline hunt.
Based on flavor, we were very confident it was going to be about Morse code, each of our feeder
answers would convert to a dot or dash, and we'd read out a message. We couldn't figure
out how to do the conversion, but the round only had 7 puzzles, so I decided to write a script to brute force
the Morse for all $$2^7 = 128$$ possibilities. This worked. I did something similar for the
[Silph Puzzle Hunt metameta](https://silphpuzzlehunt.com/puzzle/a-turn-for-the-worse). We solved the
first and last group, but couldn't figure out the answer to the (4 7) group in the middle. Doing a word
search in my phrase list, I found there were around 2500 reasonable phrases of enumeration (4 7) in it,
so out of despair I decided to brute force a list of all possible extractions and scrolled through it until
I noticed something that looked like the answer.

One advantage of code is that if it exhaustively checks all possibilities, and it still
fails to extract the puzzle, then you know you should try something different from the extraction
you attempted, rather than checking for errors. (Once again, this has burned me before, when I
concluded an extraction method was wrong because the answer didn't appear in my local wordlist. Proceed with caution!)


#### When picking what to work on, check what's underinvested

Most people solve puzzlehunts in a team, and it's usually not good for everyone on the team to pile onto
one puzzle. Instead it's better for people to spread out. When looking for a puzzle to work on, it can be helpful to check which ones have enough people to push it to the finish without you,
and which ones need assistance.

In general, puzzles with big lists of clues (e.g. crosswords) can absorb lots of people, and puzzles with many serial
a-has (e.g. logic puzzles) see diminishing returns. It's not always clear
if a puzzle is more serial or parallel. One quick hack is to **just ask the people working on the puzzle** if
they want help or think they have it under control.

In especially big hunts (i.e. Mystery Hunt), you can also strategize at the round level, picking rounds based on how many people are working in that round and how many solves they've gotten so far.


Getting Unstuck
------------------------------------------------------------------------

Everyone gets stuck on puzzles. The question is what to do about it.

#### Check your work

I have seen so, *so* many times where a puzzle was stuck because of a silly mistake. **Check your
work.** Cannot overstate this enough. I know one friend who's joked that their puzzle
solving tips guide would just be "check your work" repeated 50 times.

#### Do a different puzzle

There's no shame in abandoning a puzzle for now and coming back to it later. It's very
easy to tunnel vision too hard on a problem.

However, there is a certain art to this. Puzzles are normally done in teams. If you abandon
a puzzle, it's good to make a clean copy of your sheet first. Keep your scratch work as is, but
in the clean copy, organize your work and explain what you've found. Importantly, *remove all the speculative half-baked ideas you had.*
Given that you're stuck on the puzzle, it's more likely your half-baked ideas are wrong, and you
should avoid biasing future solvers into the same rabbit hole.

#### Look for unused information

Most puzzles will try to use all channels of information they can, and will not have extraneous info.
That doesn't mean every puzzle will use 100% of its info, but extra info is the first place to look.
Try listing everything that has and hasn't been used yet.

#### Look for missing information

To me, this is slightly distinct from unused information. Unused information is when you know there
are aspects of the puzzle dataset you haven't used yet. Missing information is when the information
you need doesn't even exist in your spreadsheet, and needs an a-ha to figure out.

The longer a spreadsheet stays unextracted, the more likely it is that the spreadsheet is fundamentally missing
the information needed to extract. I'm a big fan of [qhex's extraction basher](https://tools.qhex.org/),
which will try a wide battery of indexing and ordering mechanisms. It doesn't actually work that often
in my experience, but when I see it fail, it does encourage me to consider if there's a way to derive
another column of data we could be extracting from.

#### Assume a few errors

To err is human. If you don't like a few letters, you can always pretend those were solved wrong
and switch them to wildcards in nutrimatic.

It's important not to overdo this, but getting good at error correction can really take you quite far.
This extends to other forms of errors as well. For example, sometimes I'll assume our indices were
derived incorrectly, and try Caesar shifting in case they're all off by one.


#### Cheese

> A game designer painstakingly carves a beautiful sculpture out of wood, first chiselling it out of a
> raw block, and then gradually rounding off any rough edges, making sure it works when it's viewed from
> any angle.
>
> The speedrunner takes that sculpture and they look it over carefully, from top to bottom, from every angle, and
> deeply understand it. They appreciate all the work that went into the design, all the strengths or the weak points, and then, having understood it perfectly, they
> break it over their knee.

[Getting Over it Developer Reacts to speedrun of Getting Over It](https://www.youtube.com/watch?v=dGU5_UUalPA)
{: .centered }

For the uninitiated, cheesing a puzzle means to solve it through an unintended path. It comes from video game slang, and usually implies solving with less work than intended.

Cheesing can be a little controversial...it's a bit subversive, and as tools for cheesing have gotten stronger,
puzzle design has had to adapt in ways that sometimes makes a puzzle worse. Hardening a puzzle against
nutrimatic sometimes makes it less friendly to new solvers who don't know how to exploit nutrimatic.

I view cheesing the same as backsolving - it's a ton of fun if it works, but it wouldn't be nearly so fun if it worked all the time.

Here are common cheese tactics:

* If you don't know how to order, you can try random anagramming.
* If you have an ordered list of words, but don't know the indices, you can construct a regular expression
to take one letter from each word and see what possibilities show up in nutrimatic. For example, this works on the list of words
in the spreadsheet video earlier up.

    ![Nutrimatic results for extracting from WOW, WHAT, EXCITING, WORDS, VERY, and WONDERFUL](/public/puzzlehunting-201/nutrimatic_results.png)
    {: .centered }

    Another puzzle where I remember it working was [Hackin' the Beanstalk](https://puzzles.mit.edu/2020/puzzle/hackin_the_beanstalk/) from MIT Mystery Hunt 2020.

* If you have an ordered list of indices, know what words you're indexing, but don't know how they
match up, you can also construct a regex. If the index is (3), and we know the word we'd index is one of CAT, DOG, or HORSE,
then we know that letter can only be `[tgr]`.
This was how our team solved the [Flexibility](https://shardhunt.com/puzzle/flexibility.html) meta from
Shardhunt. We understood the last section was forming a path going back and forth between six 6-letter words, indexing
the face seen at each step of the path, but we couldn't figure out the interpretation. So we tried a cheese in hopes we could
skip that step, and it worked. (Albeit with having to look at page 2 of nutrimatic results.)

    ![Shardhunt sheet](/public/puzzlehunting-201/shardhunt.png)
    {: .centered }

    In testsolving, I solved [Mouth Mash](https://2020.teammatehunt.com/puzzles/mouth-mash) from Teammate Hunt 2020 this way as well, and the puzzle was redesigned to make this cheese less effective.

* If enumerations are given for a multi-word phrase, and the phrase is long enough, sometimes the enumeration itself is enough to constrain
the phrase. You can use OneLook or nutrimatic to check for this.
For example, (2 2 2 3 2 2 4 2 3 8) only has [one notable match](https://nutrimatic.org/2024/?q=%22AA+AA+AA+AAA+AA+AA+AAAA+AA+AAA+AAAAAAAA%22&go=Go).
This cheese is usually better done in OneLook, since it has fewer phrases and a higher fraction are valid puzzle answers.

To draw an analogy to [engineering solutions to high school math contest problems](https://cjquines.com/files/engineering.pdf), cheesing is not a replacement to learning how to solve puzzles,
but it can be very effective. If you cheese a puzzle, you should go read how it was supposed
to work after solutions are released, or try to reverse engineer the extraction from the puzzle
answer.

You should also make sure other solvers are okay with you cheesing a puzzle
before trying to do so. Cheesing is a way to skip ahead of the struggle, but
sometimes people in the struggle are having lots of fun.


#### Get in the constructor's mindset

If you get really stuck, it can help to ask why a puzzle was constructed the way it is. Why was this information
provided to you? Why is this clue phrased the way it is?

A very recent top-of-mind example is [Goodreads](https://www.brownpuzzlehunt.com/puzzle/goodreads) from Brown
Puzzlehunt 2024. There is a point in the puzzle where you extract a bunch of numeric library classifications (i.e. Language = 400 in Dewey Decimal).
We were confused on whether to extract using "Language" or "400". One clue comes with a note saying "in base 63", so
the eventual argument made was:

> Saying "base 63" is so random. This has to only exist because they couldn't make extraction work with
> standard library classes. So we should leave the class as the number, since there's no great way to interpret
> base 63 otherwise.

In general, weird, strange, or obscure clues tend to indicate that there's a very specific reason
that clue *had* to be weird, strange, or obscure, and you should consider what that reason is.
For example, I once wrote a puzzle where I needed to clue [EOGANACHTA](https://en.wikipedia.org/wiki/E%C3%B3ganachta), which was a travesty, but it was the most reasonable option that fit the letter constraints I needed.
A sharp-eyed solver that got that clue should be immediately suspicious that future extraction will be based on syntax rather than semantics.
To give a non-puzzle example, in the board game Codenames, you are trying to clue words for your team
and not the opposing team. If I get a clue like "TOMATO: 2", and
see RED and FRUIT on the board, I'll mention RED and FRUIT fits, but I'll also start wondering why we got
"TOMATO" as a clue instead of a more typical red fruit like APPLE, CHERRY, or STRAWBERRY. Perhaps
a word like PIE is on the board, and they were trying to avoid it.

How much getting into the constructor's mindset helps you will depend on how well you understand typical puzzle design. This is one reason
people who write puzzles tend to get better at solving them. Like, maybe the reason ✈✈✈Galactic Trendsetters✈✈✈ is so
strong is because parts of their team have been writing hunts every year for 7 years.


Bringing This Together
---------------------------------------------------------------------------------------------------

To showcase these strategies together, here is a puzzle I remember speedrunning especially quickly: [The Three Little Pigs](https://hunt20.com/puzzle/three-little-pigs.html)
from Hunt 20 2.1 Puzzle Hunt. This hunt was designed to be on the easier side, so this made it more susceptible to
speedrunning.

<div class="shaded" markdown="1">
#### The Three Little Pigs
{: .centered }

<p class="centered"><i>It's all about 3</i></p>

<div><p><i>This puzzle uses cryptic clues. If you are new to cryptic clues, <a href="https://puzzling.stackexchange.com/questions/45984/cryptic-clue-guide" target="_blank" class="link">a guide such as this</a> may help.</i></p></div>

<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4)<br>
Shatter quick for pancakes? (9)<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5)<br>
Cease the odd sets of pi (4)<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6)<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6)<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3)<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4)<br>
Unpleasant drug lyrics within (4)
</p></div></div>
<br>
</div>

Below is a reproduction of the solve path based on Google Sheets history, annotated
with strategies mentioned earlier.

<hr/>
<br/>

There are 9 clues in each half **(counting)**.

The puzzle is very strongly hinting 3, so my guess is that either we
will form 3 groups of 3 from each column, or we'll pair the columns and use 3 some other way
**(looking ahead)**.

Clues in the right column are ordered alphabetically, clues in the left column are not
**(looking for confirmation)**.
That suggests ordering by the left column. If only one column is ordered, that also suggests
pairing between columns, because **(constructor mindset)** it wouldn't make sense to change
the ordering between columns if each column was used identically.

Since it seems likely we'll do pairing, let's solve a few from both columns,
since having progress on both will make it easier to find a pair
**(prioritize important clues)**.

<div class="shaded" markdown="1">
<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = SNAP<br>
Shatter quick for pancakes? (9)<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5)<br>
Cease the odd sets of pi (4) = STOP<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6)<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6)<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = POP<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4)<br>
Unpleasant drug lyrics within (4)
</p></div></div>
<br>
</div>

Hey, SNAP and POP could form a group with CRACKLE. Perhaps this is how we use 3 - we get clues for two parts
of a set of 3. STOP could be the start of STOP DROP ROLL, so let's see if we can find DROP or ROLL in the right column, and
otherwise focus on solving the left column since that provides ordering **(prioritize important clues)**.

<div class="shaded" markdown="1">
<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = SNAP<br>
Shatter quick for pancakes? (9) = BREAKFAST<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5)<br>
Cease the odd sets of pi (4) = STOP<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6) = BRICKS<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6)<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = POP<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4) = ROLL?<br>
Unpleasant drug lyrics within (4)
</p></div></div>
<br>
</div>

With BREAKFAST on the left, we should try to find LUNCH or DINNER, and with BRICKS on the right, we should try to find STRAW or STICKS. At this point, we can provisionally pair those target words to cryptics by just looking for a definition that matches **(cheese)**. In the real solve, we did
do the wordplay, but only after we knew what word we wanted it to resolve to.

<div class="shaded" markdown="1">
<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = SNAP<br>
Shatter quick for pancakes? (9) = BREAKFAST<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5) = STRAW<br>
Cease the odd sets of pi (4) = STOP<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6) = BRICKS<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6) = DINNER?<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = POP<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4) = ROLL?<br>
Unpleasant drug lyrics within (4)
</p></div></div>
<br>
</div>

<br>
Let's try extracting from the missing words for each group of 3 **(looking ahead)**. So far, we have:

```
???
CRACKLE
LUNCH
???
???
???
???
STICKS
DROP
```

Having 4/9 is enough to try nutrimatic. First instinct is to read first letters, but ending in
SD seems bad. If I were making this puzzle **(constructor mindset)**, I'd want to put the theme of
3 everywhere, so let's try indexing the 3rd letter.

This gives `.an....io`, and if we
scroll down [the list](https://nutrimatic.org/2024/?q=AanAAAAio&go=Go) of nutrimatic results a bit, we see `DANCE
TRIO`, which was the answer.

During the hunt, some teams solved this puzzle in 5 minutes. My team was not that fast (13 minutes), but you can
see how applying a few tricks let us focus directly on the solve path and reduced unnecessary effort. This solve was a very extreme case, and the tricks I've described are usually not *this* effective, but try them out sometime.

*Thanks to Eugene C., Evan Chen, Jacqui Fashimpaur, Cameron Montag, Nishant Pappireddi, Olga Vinogradova for giving feedback on earlier drafts of this post.*
