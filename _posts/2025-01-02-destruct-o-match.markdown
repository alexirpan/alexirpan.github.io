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
points, but I'll use them according to my own judgment.

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


Step 2: Sanity Check
-----------------------------------------------------------------------------------------------------
