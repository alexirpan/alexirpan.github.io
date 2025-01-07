---
layout: post
title:  "Using AI to Get the Neopets Destruct-o-Match Avatar"
date:   2025-01-02 09:58:01 -0700
---

I have blogged about Neopets before, but a quick refresher: Neopets is a web game
from the early 2000s, which is still around today, with a small audience of millennials
who remember playing the game from childhood. It's a bit tricky to sum up the appeal of
Neopets, but I like the combination of Web 1.0 nostalgia and long-running progression systems.
There are a ton of intersecting achievement tracks you can go for,
some of which are exceedingly hard to 100%. There's books, pet training, stamp collecting,
rare foods, Kadoaties, and more.

The one I've been chasing the past few years is avatars.
Neopets has an onsite forum called the Neoboards, but you aren't allowed to use custom avatars due to
moderation reasons. So instead, you can only use avatars that have been created by TNT. Some are free
but most have unlock requirements. The number of avatars someone has is a quantification of how
much investment they've put into Neopets.
In my opinion, avatars are the best achievement track to chase, because their unlocks cover the widest
cross-section of the site. To get all the avatars, you'll need to do site events, collect stamps, play
games, do dailies, and more. There's a reason they get listed first in your
profile summary!

IMAGE

Avatars start easy, but can become fiendishly difficult. To give a sense of how far they can go, let me
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

I don't consider myself the Neopets top 1%, but since writing that post, I've bought all 3 Hidden Tower
books just to get the avatars...so yeah, they got me.

Avatars can be divided by category, and one big category is Flash games. These avatars all have the same
format: "get at least X points in this game." Most of their thresholds are *evil*, picked based on high-score tables
from 15-20 years ago, and require a mix of mastery and luck to achieve.

Of these avatars, I've been trying to get the Destruct-o-Match avatar for a long time.

![Destruct o match avatar](/public/destruct-o-match/dom_ava.gif)
{: .centered }

I played this a lot as a kid, and genuinely like it as a game. Destruct-o-Match is a block clearing game.
Given a starting grid, you can clear any group of 2 or more connected blocks of the same color. Each time
you do so, every other block falls according to gravity. Your goal is to clear as many blocks as possible.
You earn more points for clearing large groups at once, and having fewer blocks leftover when you run out
of moves.

IMAGE?

My best score as a kid was 1198 points. The avatar score is 2500.

Part of the reason this has always been a white whale for me is that there's no timer on the game and
it's almost entirely deterministic. You could, in theory, figure out the optimal sequence of moves for each
level to maximize your score. Actually doing so would take forever, but you *could*. There's RNG in the starting
layout, but there's also a heavy skill component.

Now that I'm an adult with AI experience, Destruct-o-Match starts looking like an ideal place to use game AI.
It is a turn based game, with no time pressure, and no randomness. That puts it in the camp of games like Chess
and Go, which we know AI is superhuman at. Surely we can get to sort-of-expert level in the much simpler game
of Destruct-o-Match if we try?

This is the story of me trying.

(Note: I assume some people reading this will know AI but not Neopets, and some will know Neopets but not AI,
so I will be explaining in greater detail than usual.)


Step 0: Is Making a Destruct-o-Match AI Against Neopets Rules?
-------------------------------------------------------------------------------

There's a gray area for what tools are allowed on Neopets.
*In general*, any bot or browser extension that does game actions or browser requests for you is 100% cheating.
Things that are quality-of-life improvements are mostly fine. Anything in-between may cross the line from quality-of-life
to excessive game assistance, but the line is hard to define.

For Destruct-o-Match, I believe it is okay to make an AI. There is a long precedent of off-site tools
being allowed for Flash games. Solvers exist for a number of existing games, such as an anagram solver for
[Castle of Eliv Thade](https://www.jellyneo.net/?go=castle_of_eliv_thade#:~:text=Anagram Solver),
Sudoku solvers for [Roodoku](https://www.jellyneo.net/?go=roodoku), and a [Mysterious Negg Cave Puzzle Solver](https://thedailyneopets.com/articles/negg-solver)
if you cannot solve that puzzle. None of these solvers input things into the game for you, but they are all
considered fair game.

This means I can't make a bot that will click things in game for me, but I can write an AI that recommends
moves, and enter those moves manually.


Step 1: Rules Engine
------------------------------------------------------------------------------

Like most AI applications, the AI is the easy part, and engineering everything around it is the hard part. To
write a game AI, we first need to implement the rules of the game in code. We'll be implementing the HTML5
version of the game, since it has a few changes from the Flash version that make it much easier to get a high
score. The most important one is that you can earn points in Zen Mode, which lets you always play to the end,
rather than causing a Game Over if you don't get enough points.

Most games can be described as a **Markov decision process (MDP)**. A Markov decision process is made of 4
components:

* The state space, covering all possible states of the game.
* The action space, covering all possible actions from a given state.
* The transition dynamics. Given a state and an action, what is our next state?
* The reward, how much we get rewarded for taking an action. We assume that reward depends only on the current state and action.

Translating Destruct-o-Match in these terms,

* The state space is the shape of the grid and the color of each block in that grid.
* The possible actions are the different groups of matching color.
* The transition dynamics are where blocks will be after removing a group and applying gravity.
* The reward is the number of points the removed group is worth, and the end score bonus if no more moves are possible.

The reward is the easiest, and follows this scoring table.

| Boulders Cleared | Points per Boulder | Bonus Points |
|------------------|--------------------|--------------|
| 2-4              | 1                  | -            |
| 5-6              | 1                  | 1            |
| 7                | 1                  | 2            |
| 8-9              | 1                  | 3            |
| 10               | 1                  | 4            |
| 11               | 1                  | 6            |
| 12-13            | 1                  | 7            |
| 14               | 1                  | 8            |
| 15               | 1                  | 9            |
| 16+              | 2                  | -            |

The end level bonus is 100 points, minus 10 points for every leftover boulder.

| Boulders Remaining | Bonus Points |
|------------------|--------------------|
| 0              | 100 |
| 1              | 90 |
| 2              | 80 |
| 3              | 70 |
| 4              | 60 |
| 5              | 50 |
| 6              | 40 |
| 7              | 30 |
| 8       | 20 |
| 9              | 10 |
| 10+              | 0 |

Gravity is also not too hard to implement. The most complicated and expensive logic is on identifying the possible
actions. To identify the groups of connected colors, we can repeatedly
apply the [flood-fill](https://en.wikipedia.org/wiki/Flood_fill) algorithm, until all boulders are grouped.
This runs in time proportional to the size of the board. However, it's not quite that simple, thanks to one important
part of Destruct-o-Match: powerups.

## Powerups

Powerups are very important to scoring in Destruct-o-Match, so we need to model them accurately. Going through them
in order:


<table>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_timer.jpg"/></td>
<td>The <strong>Timer</strong> Boulder counts down from 15 seconds, and becomes unclearable if not removed before then.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_fill.jpg"/></td>
<td>The <strong>Fill</strong> Boulder will add an extra line of blocks on top when cleared.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_explode.jpg"/></td>
<td>The <strong>Explode</strong> Boulder is its own color and is always a valid move. When clicked, it and all adjacent boulders (including diagonals) are removed, scoring no points.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_overkill.jpg"/></td>
<td>The <strong>Overkill</strong> Boulder destroys all boulder of matching color when cleared, but you only get points for the group containing the Overkill.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_multiplier.jpg"/></td>
<td>The <strong>Multiplier</strong> Boulder multiples the score of the group it's in by 3x.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_morph.jpg"/></td>
<td>The <strong>Morph</strong> Boulder cycles between boulder colors every few seconds.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_wildcard.jpg"/></td>
<td>The <strong>Wild</strong> Boulder matches any color, meaning it can be part of multiple valid moves.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_shuffle.jpg"/></td>
<td>The <strong>Shuffle</strong> Boulder gives a one-shot use of shuffling boulder colors randomly. The grid shape will stay fixed. You can bank 1 shuffle use at a time, and it carries across levels.</td>
</tr>
<tr>
<td><img src="/public/destruct-o-match/dom3_boulder_undo.jpg"/></td>
<td>
The <strong>Undo</strong> Boulder gives a one-shot use of undoing your last move, as long as it did not involve a power-up. Similar to shuffles, you can bank 1 use at a time and it carries across levels. Unique to the HTML5 version, you keep all points from the undone move,
so you want to build up a large group of boulders, clear it for a bunch of points, then undo it so you can clear it again.
</td>
</tr>
</table>

We can keep the game simpler by ignoring the Shuffle and Undo powerups. These are worth points, but Shuffle would require implementing randomness, which tends to be harder for AI to handle, and Undo requires maintaining whether we have access to an undo across levels, which I'd rather not do so that we can optimize each level independently. I can use
these powerups manually when I think they're worth it.
Remember, we're not targeting perfect play, we're targeting "good enough" play to hit the avatar score, so introducing some slack is okay if we make up for it later.

Then, to avoid introducing time pressure, we can ignore the Timer powerup, as long as we commit to
immediately removing the Timer Boulder before inputting the state into the AI. Similarly, we can ignore the Fill powerup if we commit to immediately removing it as well, which lets us avoid randomness in what blocks get added.

This leaves Explode, Overkill, Multiplier, Morph, and Wild. Morph can be treated as identical to Wild, as long as we wait long enough for the Morph boulder to become whatever color we want it to be.
So we only have to implement 4 powerups. The complexity these powers add is that after identifying
a connected group, we may remove boulders outside that group. A group of blue boulders with an Overkill needs to remove every other blue boulder. So, for every group identified via flood-fill, we also
need to track an "also-removed" set. (There were then a lot of annoying edge-cases, of which my favorite was bugs that occurred only when two Explode blocks were next to each other.)

With that, we're done with the rules engine!

...Almost done.


Step 2: Initial State
-----------------------------------------------------------------------------------------------------

Although I tried to remove all randomness, one source of randomness I can't ignore is how powerups are initially distributed.

Of the powerups, the Multiplier Boulder is clearly very valuable. Multiplying score by 3x can be worth a lot, and avatar runs are typically decided by how many Multipliers you see that run. So for my AI to be useful, I need to know how often each powerup appears.

I couldn't find any information about this on the fan sites, so I did what any reasonable person would do and created a spreadsheet to track powerup appearances across 65 random levels.

![Spreadsheet of results](/public/destruct-o-match/spreadsheet.png)
{: .centered }

Based on this data, I believe Destruct-o-Match first randomly picks a number from 0-3 for how many
powerups will be on the board. If powerups were randomly selected per block, I would have seen more than 3 powerups at some point. I observed 0 powerups 3% of the time, 1 powerup 23% of the time, 2 powerups 34% of the time, and 3 powerups 40% of the time. For reverse engineering, I'm applying "programmer's bias" - someone made this game, and it's more likely they picked round, "nice" numbers.
In my implementation of Destruct-o-Match, I use 0 = 5%, 1 = 20%, 2 = 35%, 3 = 40% for powerup counts.

Looking at the counts of each powerup, Explode clearly appears the most and Multiplier appears the least. Again applying some nice number bias, I assume that Explodes are 2x more likely, Fills are 2/3rd as likely, and Multipliers are 1/3rd as likely.

Two asides here. One, my rules engine does not implement some powerups. If those powerups are picked, I pretend the block has no powerup. Two, the powerup logic differs between the HTML5 and Flash version. In a few levels of the Flash version, I've seen more than 3 powerups appear.


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
