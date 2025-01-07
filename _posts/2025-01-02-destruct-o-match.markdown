---
layout: post
title:  "Using AI to Get the Neopets Destruct-o-Match Avatar"
date:   2025-01-02 09:58:01 -0700
---

I have blogged about Neopets before, but a quick refresher: Neopets is a web game
from the early 2000s, which is still around today, with a small audience of millennials
who remember playing the game from childhood. It's a bit tricky to sum up the appeal of
Neopets, but I like the combination of Web 1.0 nostalgia and long-running progression systems.

To expand on the latter, there are a ton of intersecting achievement tracks you can go for,
some of which are exceedingly hard to 100%. There's books, pet training, stamp collecting,
rare foods, Kadoaties, and more, but the one I've been chasing the past few years is avatars.

Neopets has its own onsite forum, the Neoboards, where you can pick among a list of unlockable
avatars. But really, it's most important for "number goes up" reasons. They're a quantification of how
much investment you've put into Neopets, and in my opinion, avatars are the best one to chase
because they cover a wide cross-section of the site. There's a reason they get listed first in your
profile summary!

IMAGE

Avatars start easy, but can quickly become fiendishly difficult. To give a sense of how far they can go, let me
quote a post I wrote before.

> The Hidden Tower Grimoires are books, and unlike the other Hidden Tower
> items, they're entirely untradable. You can only buy them from the Hidden
> Tower, with the most expensive one costing 10,000,000 NP.
> Each book grants an avatar when read, disappearing on use.
> 
> ![100,000 NP book](/public/neopets-economy/book1.gif)
> ![1,000,000 NP book](/public/neopets-economy/book2.gif)
> ![10,000,000 NP book](/public/neopets-economy/book3.gif)
> {: .centered }
> 
> ![100,000 NP ava](/public/neopets-economy/ava1.gif)
> ![1,000,000 NP ava](/public/neopets-economy/ava2.gif)
> ![10,000,000 NP ava](/public/neopets-economy/ava3.gif)
> {: .centered }
> 
> Remember the story of the [I Am Rich](https://en.wikipedia.org/wiki/I_Am_Rich)
> iOS app, that cost $1000, and did literally nothing? Buying the most expensive
> Grimoire for the avatar is just pure conspicuous consumption. [...] They target the
> top 1% by creating a new status symbol.

I don't consider myself the Neopets top 1%, but since writing that post, I've bought
all 3 Hidden Tower books just for the avatars...so yeah, they got me.

Although some avatars are literally pay-to-win, many of them are not. The main ones I've
been chasing recently are the game avatars. Each one has the same format: "get at least X points in this game".
The thresholds were picked 15-20 years ago, and some of them are ruthless.

However, one I've always had an eye on is the Destruct-o-Match avatar.

IMAGE

I played this game a lot as a kid, and genuinely like it as a game. In Destruct-o-Match, you're given
a grid of blocks, and can clear any group of 2 or more connected blocks of the same color. Each time you
do, the rest of the blocks fall down. Your goal is to clear as many blocks as you can, earning points for
the size of the groups you clear and how many singleton blocks you have left when you finish the level.

IMAGE?

My best score as a kid was XXXX points. The avatar score is 2500.

Part of the reason this has always been a white whale for me is that there's no timer on the game and
it's almost entirely deterministic. You could, in theory, figure out the optimal sequence of moves for each
level to maximize your score. Actually doing so would take forever, but you *could*.

Fast forward to current year, and Destruct-o-Match starts looking like an ideal application of game AI.
If we can be superhuman at chess and Go, surely we can get to sort-of-expert level in this much simpler
game if we try.

This is the story of the attempt to write a Destruct-o-Match game AI.


Step 0: Is This Against Neopets Rules?
-------------------------------------------------------------------------------

There's a bit of gray area for what tools are allowed on Neopets, and which ones are considered cheating.
*In general*, any bot or browser extension that does game actions or browser requests for you is 100% cheating.
Things that are quality-of-life improvements are mostly fine. Anything in-between that's considered game
assistance is against the rules, but what counts as "assitance" is hard to define.

For Destruct-o-Match at least, I believe I'm in the clear. There is a long precedent of off-site tools
being allowed for Flash games. The anagram solver for [Castle of Eliv Thade](https://www.jellyneo.net/?go=castle_of_eliv_thade#:~:text=Anagram Solver)
is considered legal. The [Mysterious Negg Cave Puzzle Solver](https://thedailyneopets.com/articles/negg-solver) is
also fine, along with using a Sudoku solver to get fast [Roodoku](https://www.jellyneo.net/?go=roodoku) times.
So I can't make a bot that will interact with the browser for me, but it should be kosher for me to transcribe
the game state to the AI, have it recommend a move, then relay the click myself.


Step 1: Rules Engine
------------------------------------------------------------------------------

Like many AI applications, the AI is the easy part, and engineering everything around it is the hard part. To
write a game AI, we first need to implement the rules of the game in code. For doing this, we'll be using the
HTML5 version of the game, since it's easier to get a higher score in that version.

Any game environment is typically
divided into 4 pieces: the state, the possible actions, the reward for each action, and the future state if
each action is taken.

In Destruct-o-Match, the state is the color of each block. The possible actions are the different groups
of matching color. The reward is how many points are earned for clearing that group, and the future state is
where the blocks will be after that group is removed and the remaining blocks fall.

The core logic of finding the possible actions can be done by repeatedly
applying the [flood-fill](https://en.wikipedia.org/wiki/Flood_fill) algorithm, to partition the board into
different pieces of matching color. The run time is linear in the number of vertices and edges, and for a 2D
grid that's the same as the number of total squares. However, it's not quite that simple, thanks to one part
of Destruct-o-Match: powerups.

During the game, random power-ups can appear in the grid. These affect scoring, so it's important to model
them accurately. Going through them in order:

(Add images here?)

* The *Timer* Boulder counts down from 15 seconds, and becomes unclearable if not removed before then.
* The *Fill* Boulder will add an extra line of blocks on top when cleared. This introduces randomness, because we
don't know what blocks will be added until we clear it.
* The *Explode* Boulder is its own color, but can always be clicked. When clicked, it removes all adjacent boulders, including diagonally adjacent.
* The *Overkill* Boulder destroys all boulder of matching color when cleared, but only providing points for the boulders in the group containing the Overkill.
* The *Multiplier* Boulder multiples the score of the group it's in by 3x.
* The *Morph* Boulder switches between boulder colors every few seconds.
* The *Wild* Boulder matches any color. In the game, when you click a boulder, it highlights the group of
connected boulders of matching color. A Wild boulder is never clickable, but is highlighted if you click any of
its neighbors. (IMAGE?)
* The *Shuffle* Boulder gives you a one-shot use to shuffle boulders randomly. The shape will stay the same,
but the colors will be rearranged among them. This is most useful when you're near the end of a level, have cleared
almost all blocks, and figure a random point will be worth more points than what you have left.
You can save up to 1 Shuffle usage and it carries over across levels. (IMAGE?)
* The *Undo* Boulder gives a one-shot use to undo the last move you made, as long as that move did not involve
a power-up. (Unique to the HTML5 version, you keep points if you undo a move, so you can earn extra points by
constructing a high-scoring move, then undoing it and doing it again.) You can save up to 1 Undo and it carries
over across levels.

To simplify the game and keep the game fully deterministic, I decided to ignore Timer, Fill, Shuffle, and Undo
in my implementation of the game. Ignoring Timer lets me ignore time pressure. Ignoring Fill and Shuffle lets me
ignore randomness, since those are the only two powers that involve RNG. Undos could be handled, but requires
maintaining state on the previous action taken and whether an Undo is available, which is more complexity than
I wanted to deal with.

Ignoring all those power-ups is fine, because when I play the game for real, I can simply clear the Timer and Fill blocks
on my own, then delegate back to the AI. As for shuffles and undos, I still plan to use them, because they help earn more
points, but I'll use them according to my own judgment. This simplification means my AI will be earning fewer points than
it could, but that's fine. Remember, we're not targeting perfect play, we're targeting "good enough" play to hit the avatar score.

With these powers removed, there are still some small details to handle for the flood-fill. Consider the overkill powerup.

Overkill

If I click the group with the Overkill powerup, it will remove other disconnected blocks. But if I click those blocks,
it won't clear the Overkill group. So, for every group we identify via flood-fill, we need to track an *also-removed* set,
for blocks that aren't connected but will be removed if this action is taken. This is enough to capture the Explode case too.
We also need to support single blocks being part of multiple different groups, thanks to how Wilds work.

For the reward, we can use two tables from JellyNeo, the one for points per group size, and the one for end scoring.

TABLES

You get more points if you assemble bigger groups, and every block you fail to clear costs you 10 points at the end (up to a limit
of 10 penalities.) Ideally you both form large groups and clear every block to get the 100 bonus, but that may not be possible.

Finally, the block falling is pretty straightforward. Each column falls on its own, and if any column is now empty, the columns
slide together to fill the extra space.


Step 2: Initial State
-----------------------------------------------------------------------------------------------------

The rules engine is now complete. However, there's one important bit of randomness that I can't pretend does not exist: the
initial distribution of powerup boulders.

Powerups are *critical* to achieving high scoring runs, so I want to model them accurately, but I couldn't find any information
about them on the fan sites. So I did what any reasonable person would do, and made a spreadsheet of power-up appearances over
50 levels I played myself.

LINK (or table?)

Based on this data, I hypothesized that power-ups worked like so:

* **The game first selects a number of 0-3 for how many powerups to play on the board.** I never observed more than 3 power-ups.
If power-ups were selected by some fixed probability per block, we would expect to see a smooth bell-curve of outcomes, but we don't.
I observed 0 powerups 3% of the time, 1 powerup 23% of the time, 2 powerups 34% of the time, and 3 powerups 40% of the time. I rounded this to
0 = 5%, 1 = 20%, 2 = 35%, 3 = 40%, since I suspect it's more likely the original programmers picked nice round numbers.
* **All powerups except Fill, Explode, and Multiplier are equally likely**. I observed 15 +/- 2 occurrences of each.
* **Explodes are 2x as likely, Fill is 2/3rd as likely, and Multiplier is 1/3rd as likely**. I observed 35 occurrences of
Explode, 2.33x more than the base rate of 15 occurrences for the other powerups, but here I'm applying "nice number bias" again.
The symmetry of 2x more explodes getting offset by less likely Fills and Multipliers feels elegant enough that I can see the original
programmer making that choice.


Step 3: Sanity Check
------------------------------------------------------------------------------------------------------

Before going too fan down the rabbit hole, let's check if skill has much impact on Destruct-o-Match scores. If it doesn't,
then trying to write an AI for it wouldn't matter.

To check this, I implemented 3 basic strategies:

* Random. Removes a random block.
* Top-Down, Left-Right. This removes the top-most group, breaking ties by the left-most group.
* Bottom-up, Right-Left. This removes the bottom-most group, breaking ties on the right.

The idea with these strategies is that random is a simple baseline, that maps to a human player spamming clicks without thinking. (I have done this many, many times when I'm sick of playing.) Top-down and bottom-up are two strategies from the JellyNeo fan page. Top-down biases towards clearing known groups over trying to create groups by making other boulders fall down, and bottom-up biases towards trying to make new groups from other falling boulders. 

For each strategy, I simulated 100 random games and plotted the distribution of results.

IMAGE

The good news is that yes, strategies make a lot of difference, and there's value to gain from building an AI.
Bottom-up is worse than random, and top-down is better. In practice, this lets us know that **usually, disrupting existing groups is bad**, and it's better to take the guaranteed points.

Now, one last recommended human strategy is to remove blocks in order of color. If you remove all the blue blocks first, the remaining groups will connect more often and be bigger in size, earning more points.
We can try this strategy, picking by color first, then tiebreaking with the top-down left-right heuristic.

IMAGE

Using color let's us eke out another 100 points on average. My target before using this for real is to average around 2400 points. I figure I can make up the remaining 100 point difference to the avatar by using undos and shuffles, as well as aggressive resets for good scores on the first level.


Step 4: The AI
-------------------------------------------------------------------------------------

If I were trying to max out score, I would do the AlphaZero or MuZero thing. I'd run a very large number of simulated games,
to train a neural net to predict the value of boards, that would be further refined by extra self-play.

I don't want to invest that much compute into this project, so instead we're using handcoded heuristics. The value of a board
can be conservatively estimated as the value of every group within the board, plus the end-level points we get for the number of remaining boulders. This assumes that we will never form new groups
during the removal of old groups, and that there's a way to order the groups such that removing one doesn't impact any of the future ones.
This is true *most* of the time. There are some edge cases where that isn't true, such as this double-C example.

IMAGE

For the purposes of the AI though, the value estimate doesn't have to be perfect. It just needs to be "good enough" to not
mislead the rest of the search. Computing this value is easy, because we already have to find every clearable group when finding the
list of actions, so we can just reuse that logic.

So, here is our new method for choosing actions.

1. From the current state, compute every possible action.
2. For each action, find the reward and value of the resulting state.
3. Pick the action with best reward + value.
4. In cases of a tie, pick according to the color then top-most heuristic that's worked best before.

Even this 1-step lookahead is quite effective. By like, a **lot**.

IMAGE

This one step search is enough to bring the average from 1850 to 2250, a 400 point boost. In fact
it's big enough that I tried playing a game with the 1-step lookahead. After reseting for a good
level 1, I got tantalizing close to a winning score.

IMAGE

To get the rest of the way there, we need to crank up the search. Instead of only looking 1 move
ahead, let's look multiple moves ahead.

1. From the current state, compute every possible action.
2. For each action, find the reward and next state.
3. For each of those future states, compute the possible next actions and rewards.
4. (Repeat steps 2 and 3 N times.)
5. At the end, compute the total reward of the N actions, and the value of the state after doing the N actions.
6. Pick the 1st action of the best scoring sequence, with the same tiebreak as before.

Doing so quickly runs into problems. In search, the branching factor of a game is the number of
average actions available from a given start position. The branching factor is important because the size of the search tree grows exponentially with depth, and the exponential is faster if the branching factor is higher. (Given a branching factor of $$b$$, a depth $$d$$ tree is $$O(b \cdot b^{d-1})$$ in size.)

In Destruct-o-Match, this starts at an
average of 34, which is actually on-par with Chess's branching factor of 31 to 35 legal moves.
If people can dedicate their life to Chess, surely I can dedicate a week to Destruct-o-Match.
My game engine is not particularly fast (this is what I get for doing it in Python), so fully
expanding the search tree for larger depth quickly makes it too difficult to evaluate.

To get around this, we can use search tree pruning. This is an approximation to exhaustive depth-N search,
where instead of expanding every possible action, we only expand the most promising actions and prune (discard) the rest. This
remove the guarantee that you'll identify the best action, but the hope is that looking further ahead
makes up for overlooking other promising action. There are strong similarties between this and beam search, the method that used to dominate language generation (before LLMs got powerful enough for beam search to be more of a hindrance than a benefit. See XXX.)

(Quick aside: the reason I jumped to this is because I've seen it work before. In college, I once
went to a coding competition where we split into groups of 3-4, and had to code the best Tetris
bot we could in 4 hours. I handled game logic while a teammate handled the search, and their pruned search
tree destroyed everyone. We won $500 in gift cards, it was pretty cool.)

Here's the new algorithm, assuming we prune all but the top $$p$$ actions.

1. From the current state, compute every possible action.
2. For each action, find the reward, next state, and value of the next state.
3. Sort and find the $$p$$ best actions so far, discarding the rest.
4. For each of the $$p$$ future states, repeat steps 1-3. When doing so, we maintain history of the rewards seen so far, so that we can sort by $$r_1 + r_2 + ... + r_t + V$$.
5. At the end, compute the total reward of each search tree path.
6. Pick the 1st action of the best scoring sequence.

Given a branching factor of $$b$$, depth $$d$$, and pruning factor $$p$$, this runs in time $$O(b\cdot p^{d-1})$$. The search tree is of size $$O(p^d)$$ and there are $$b$$ actions to evaluate for each
node in the tree.

This introduces an extra hyperparameter (choice): how much pruning to do, and what depth to search for. To understand the trade-off better, I did 3 runs. One with `Depth=2, Expand=3`, one with `Depth=2, Expand=9`, and one with `Depth=3, Expand=3`. The first is to verify there are gains from increasing search depth at all, and the second two are 2 compute-equivalent variants training depth for larger expansion factor.

IMAGE

The gains are getting harder to spot, so here are more exact averages.

Depth 1: 2233.38  
Depth 2, Expand 3: 2318.32  
Depth 2, Expand 9: 2343.34  
Depth 3, Expand 3: 2373.37  

Increasing depth is a bit more effective than increasing width, with a gain of 140 points.

This started to hit the limit of what I can reasonably evaluate (the last run took 3 hours to simulate), but it's close enough to the 2400 target that I felt comfortable running it for real. For the final real run, I cranked up the expansion factor to 6. At depth 3 expand 6, it takes around 1.5 seconds to pick an action on my laptop, which is right at the edge of an annoying wait time.


Step 5: Board Input
----------------------------------------------------------------------------------------

My original plan for transcribing the board to my AI was to use basic computer vision. There are
only 10 different boulder colors that can appear, and each boulder uses the same image, so in theory,
it should be possible to do a search for the matching image in the overall image.

IMAGE

This is, theoretically, pretty straightforward. Unfortunately, I kept messsing it up. I debugged it for a while, but then quickly realized it would be faster for me to input it by hand, given that
I would likely only need to play the game 1-2 times.

To make it interactive, I set up a Jupyter Notebook, to display the board after I input all the
colors. This was to let me quickly verify if I'd made any mistakes in data entry. After manual
corrections from there, I ran my AI in the depth 3 expand 6 configuration, having it pause after each move to give me time to enter it.

The end result?

IMAGE

An avatar score! Hooray!

Some final commentary, based on studying games played by the AI:

* *Most points are earned by getting near-perfect clears on early levels.* At depth 3, the AI frequently clears the first few levels with 0-3 blocks left, earning a ton of points. In later levels,
the AI ends with more than 10 missing blocks and gets no clear bonus.
* *Early fill powerups are bad.* Although Fill powerups give you more boulders to clear, they primarily cause you to end games with more blocks left over, and losing 10 points per block is not worth the extra group. So fill powerups are only good when you don't expect to get any clear bonus.
* *Early undos are very strong.* I reset until I saw a Multiplier powerup in level 1, but what reall y made my run was getting 2 undos in level 2. The AI is very consistent at assembling groups of 16+ boulders. Groups of that size are worth 2 points per boulder, so an undo can often be cashed in for 32-44 points.
* *Whoever designed the Flash game was a monster.* In the original Flash game, you only get to proceeed to the next level if you earn enough points, with the point thresholds increasing each level. But it actually gets *harder* to earn points as you go through the levels. Although you get more blocks to work with, the added colors make it hard to form the large groups required for points. My AI averages 203 points in level 7, which needs 220 points to clear. In level 9 it averages 185 points, when 260 points are needed to beat it.
* *The AI is nowhere near the ceiling of human play.* Top scores on the Flash game are often in the 2900+ range. The absolute highest score I've seen my AI achieve over 100 games is 2606. I have no interest in pushing farther on this now that I've gotten the avatar, but someone with more free time may be interested.
