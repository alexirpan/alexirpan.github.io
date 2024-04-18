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
I feel puzzles are much more about testing creativity, promoting curiosity,
and having fun than about trying to finish the fastest. Competition is more a way
to turn it into an event and encourage people to take them seriously.
There's really not much money in puzzlehunting and I suspect people like it this way.

Still, competition is fun and at minimum most people will have more fun if they
solve puzzles than if they don't. After doing
puzzlehunts for well over a decade, I've picked up some habits that could be
useful to share.

**If you are new to puzzlehunts, you are not the target audience.** I mean, feel
free to keep reading! But I will be assuming a bunch of background knowledge and
won't be trying to explain what a puzzle is or what a meta is and so forth. If
you're new, I recommend [Introduction to Puzzlehunts](https://blog.vero.site/post/puzzlehunts)
instead.

**If you've done many puzzlehunts, not everything I say here will work for you.**
Puzzlehunting systems are a little like productivity systems: everyone's is
different, not all pieces of them will click with you, and people can be very opinionated
about them even if they all share common themes. Your best bet is to try things out, take the parts that work,
and ignore the parts that don't.

**This will spoil a few puzzles.** I've tried to keep the spoilers as light as needed,
but it's much easier to give real-life examples than to construct new puzzles just for
the sake of this post. (Then again, imagine if this post was written entirely to seed content
for an upcoming puzzlehunt. Boy would that be interesting! Seriously though, it's not. Don't
try looking for it.)


The "If I Had One Minute Version"
-------------------------------------------------------------------

Puzzles are usually a collection of data that has hidden patterns and structure.
Solving a puzzle is about exploring the data to find those structures.

Puzzle solving can be divided into generating ideas for how a puzzle works,
and executing well on those ideas.

To generate more ideas, solve more puzzles to see what's shown up in
past puzzles.

To execute better, practice by solving more puzzles.


Wait This Seems Too Simple
-----------------------------------------------------------------

Nah that's pretty much it.

The very common story is that if you want to get good at a skill, just do
it a bunch. Like, go solve 100 puzzles. No, I don't mean 10, or 20. Stop reading and
go solve literally 100 puzzles.
You will learn things. You will get better. It'll just happen. It's part of the
magic of the human brain.

This is a very specific anecdote, but I play a platforming game called Dustforce.
There's one very hard level in the game which has a part called the Tera section.
It's almost exactly in the middle of the level, has a 2 frame window in a 60 FPS game,
and is easily the most difficult part of the level to beat consistently.

I complained about this in the Discord and was told that yes, it's awful, but then
shared "100 Teras", a custom map that's just 100 copies of the Tera section with a checkpoint between each one.
"If you're really having trouble, go beat 100 Teras". So I did, twice. And then I stopped
complaining.

If you go solve 100 puzzles, you may not need this post. I'm still going to explain the
solve strategies I've picked up, but puzzle solving is really an activity where you
learn by doing.

Okay, on to the actual post.



Starting a Puzzle - Generating Ideas
------------------------------------------------------------------------

Puzzles are often described as having "a-has" or break-ins, where it
suddenly becomes clear what you should do. How do you come up with a-has?
How do you break-in?

This is genuinely the hardest part to give advice about. If it was
easy to come up with good ideas, we wouldn't have puzzles in the first place!
So I've decided to interpret the question differently: how do you create
the best conditions that cause good ideas to arise?

#### Use monospace

A lot of puzzles will use length as part of the structure. For example, [Human Pyramid](https://2021.teammatehunt.com/puzzles/human-pyramid) from Teammate Hunt 2021.
Patterns in length (matching length, exactly one letter longer, etc.)
are easy to subconsciously notice if you put content in monospace, so if you put your spreadsheet
in monospace, you'll break-in on these patterns faster.

(In fact, the monospace font
in Human Pyramid was added during testsolving to push solvers to consider length. A similar trick
was used in [Pestered](https://puzzles.mit.edu/2018/full/puzzle/pestered.html) from MIT Mystery Hunt 2018.)

Personally I like to put everything in monospace, but I know some solvers
who prefer only putting clue answers in monospace and leaving clues in sans serif, since
they value the visual boundary between clue and answer. Pick whichever works for you.


#### Transcribe puzzle content faithfully

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


1. Look ahead to extraction or the next step early.

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
Another advantage is that code can be carried between hunts.


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

5. Assume a few errors

To err is to be human. If you don't like a few letters, you can always pretend those were solved wrong
and switch them to wildcards in nutrimatic.

It's important not to overdo this, but getting good at error correction can really take you quite far.
This can extend past the single letter case as well. Sometimes I Caeser shift gibberish text to check
if our indices are all off-by-one.


6. Cheese

> A game designer painstakingly carves a beautiful sculpture out of wood, first chiselling it out of a
> raw block, and then gradually rounding off any rough edges, making sure it works when it's viewed from
> any angle.
>
> The speedrunner takes that sculpture and they look it over carefully, from top to bottom, from every angle, and
> deeply understand it. They appreciate all the work that went into the design, all the strengths or the weak points, and then, having understood it perfectly, they
> break it over their knee.

[Getting Over it Developer Reacts to speedrun of Getting Over It](https://www.youtube.com/watch?v=dGU5_UUalPA)
{: .centered }

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


7. Get in the constructor's mindset

If you get really stuck, it can help to ask why a puzzle was constructed the way it is. Why was this information
provided to you? Why is this clue phrased the way it is?

A very recent top-of-mind example is [Goodreads](https://www.brownpuzzlehunt.com/puzzle/goodreads) from Brown
Puzzlehunt 2024. There is a point in the puzzle where you extract a bunch of numeric library classifications (i.e. Language = 400 in Dewey Decimal).
Except, we were confused on whether to extract using "Language" or "400". One clue 
Except, one comes with a note saying "in base 63". We were pretty confused on how to use this, and on whether
we were supposed to use "Language" or "400" in extraction. The eventual argument made was:

> Saying "base 63" is so random. This has to only exist because they couldn't make extraction work with
standard library classes. So we should leave this as "400" instead of "Language".

How much this helps you will depend on how well you understand typical puzzle design, and this is one reason
people who write puzzles tend to get better at solving them. Like, maybe the reason Galactic Trendsetters is so
strong is because parts of their team have been writing hunts every year for 7 years.


Bringing This Together
---------------------------------------------------------------------------------------------------

To show this coming together, here is a puzzle I remember speedrunning especially quickly: [The Three Little Pigs](https://hunt20.com/puzzle/three-little-pigs.html)
from Hunt 20 2.1 Puzzle Hunt. This hunt was designed to be on the easier side, so this made it more susceptible to
speedrunning. I've reproduced the solve path based on Google Sheets history.

**The Three Little Pigs**

<main>

    <p class="flavor">It's all about 3</p>

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
</main>

(counting)

There are 9 clues in each half.

(look ahead)

The puzzle is very strongly hinting 3, so my guess is that either we
will form 3 groups of 3 from each column, or we'll pair the columns and use 3 some other way.

(look for confirmation)

Clues in the second half are ordered alphabetically, clues in the first half are not.
We'll probably pair and order by the 1st half.

(prioritize useful information)
Since it seems likely we'll do pairing, let's solve a few from both columns,
that'll make it more likely we find a pair first.

<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = `SNAP`<br>
Shatter quick for pancakes? (9)<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5)<br>
Cease the odd sets of pi (4) = `STOP`<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6)<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6)<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = `POP`<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4)<br>
Unpleasant drug lyrics within (4)
</p></div></div>

Hey, SNAP and POP could get groupd with CRACKLE. Perhaps this is how we use 3 - we get clues for two parts
of a set of 3. STOP could be the start of STOP DROP ROLL, so let's see if we can find ROLL in the right column, and
otherwise focus on solving the left column since that provides ordering.

<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = `SNAP`<br>
Shatter quick for pancakes? (9) = `BREAKFAST`<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5)<br>
Cease the odd sets of pi (4) = `STOP`<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6) = `BRICKS`<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6)<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = `POP`<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4) = `ROLL?`<br>
Unpleasant drug lyrics within (4)
</p></div></div>

With BREAKFAST on the right, we should try to find LUNCH or DINNER, and with BRICKS on right we should try to
find STRAW or STICKS on the left.

<div style="width:100%"><div style="float:left;width:50%;padding-right:15px"><p>
Nice hug in deity (4)<br>
Break small round pan (4) = `SNAP`<br>
Shatter quick for pancakes? (9) = `BREAKFAST`<br>
Head of public relations takes primate document (5)<br>
Little matter from master weight (6)<br>
Among a hubbub blessing, spheres (7)<br>
Plain vehicle turns everything and one (7)<br>
Southern team leader's uncooked fodder  (5) = `STRAW`<br>
Cease the odd sets of pi (4) = `STOP`<br></p></div><div style="float:left:width:45%"><p>
Bachelor's around Astley blocks (6) = `BRICKS`<br>
Cisgender in Social Security, or small tools (8)<br>
Diamond inside a meal (6) = `DINNER?`<br>
Flower mob coming back around failure (7)<br>
Particle misuses one turn (7)<br>
Soda bubble result (3) = `POP`<br>
Sweet delayed after cold homecoming (9)<br>
Turn an official list of bread (4) = `ROLL?`<br>
Unpleasant drug lyrics within (4)
</p></div></div>

For the middle words, we have

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

Having 4/9 is enough to try nutrimatic. First letters doesn't look good (ending in SD is rough).
There's no other indices around, but given all the 3s around, let's try indexing with 3.

https://nutrimatic.org/2024/?q=AanAAAAio&go=Go

Scrolling down the list a bit, we see DANCE TRIO. Now there's a lot of reasonable phrases here, but
"trio" suggests 3 strongly enough that it's worth trying. This was in fact the answer.


