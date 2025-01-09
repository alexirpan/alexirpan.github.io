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

![Profile summary](/public/destruct-o-match/profile.png)
{: .centered }

(The avatar I'm using right now literally took me 5 years to get. I'm very glad that I have it.)
{: .centered }

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
Given a starting board, you can clear any group of 2 or more connected blocks of the same color. Each time
you do so, every other block falls according to gravity. Your goal is to clear as many blocks as possible.
You earn more points for clearing large groups at once, and having fewer blocks leftover when you run out
of moves. The game is made of 10 levels, starts with a 12 x 14 grid of 4 colors and ending with a 16 x 18 grid of 90 colors.

<div style="width:100%; display:flex; margin-bottom:15px;">
    <div style="width:30%">
        <img src="/public/destruct-o-match/blocks_before.png" alt="Initial grid">
    </div>
    <div style="width:4%">
    </div>
    <div style="width:30%">
        <img src="/public/destruct-o-match/blocks_during.png" alt="While clearing">
    </div>
    <div style="width:4%">
    </div>
    <div style="width:30%">
        <img src="/public/destruct-o-match/blocks_after.png" alt="After clear">
    </div>
</div>

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

<table class="centered-table" style="margin-bottom:15px;">
  <thead>
    <tr>
      <th style="padding:0 10px 10px 10px">Boulders Cleared</th>
      <th style="padding:0 10px 10px 10px">Points per Boulder</th>
      <th style="padding:0 10px 10px 10px">Bonus Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2-4</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>5-6</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <td>8-9</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <td>11</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <td>12-13</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <td>14</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <td>15</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <td>16+</td>
      <td>2</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

The end level bonus is 100 points, minus 10 points for every leftover boulder.

<table class="centered-table" style="margin-bottom:15px;">
  <thead>
    <tr>
      <th style="padding:0 10px 10px 10px;">Boulders Remaining</th>
      <th style="padding:0 10px 10px 10px;">Bonus Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>100</td>
    </tr>
    <tr>
      <td>1</td>
      <td>90</td>
    </tr>
    <tr>
      <td>2</td>
      <td>80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <td>4</td>
      <td>60</td>
    </tr>
    <tr>
      <td>5</td>
      <td>50</td>
    </tr>
    <tr>
      <td>6</td>
      <td>40</td>
    </tr>
    <tr>
      <td>7</td>
      <td>30</td>
    </tr>
    <tr>
      <td>8</td>
      <td>20</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <td>10+</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

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
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_timer.jpg"/></td>
<td>The <strong>Timer</strong> Boulder counts down from 15 seconds, and becomes unclearable if not removed before then.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_fill.jpg"/></td>
<td>The <strong>Fill</strong> Boulder will add an extra line of blocks on top when cleared.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_explode.jpg"/></td>
<td>The <strong>Explode</strong> Boulder is its own color and is always a valid move. When clicked, it and all adjacent boulders (including diagonals) are removed, scoring no points.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_overkill.jpg"/></td>
<td>The <strong>Overkill</strong> Boulder destroys all boulder of matching color when cleared, but you only get points for the group containing the Overkill.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_multiplier.jpg"/></td>
<td>The <strong>Multiplier</strong> Boulder multiples the score of the group it's in by 3x.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_morph.jpg"/></td>
<td>The <strong>Morph</strong> Boulder cycles between boulder colors every few seconds.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_wildcard.jpg"/></td>
<td>The <strong>Wild</strong> Boulder matches any color, meaning it can be part of multiple valid moves.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_shuffle.jpg"/></td>
<td>The <strong>Shuffle</strong> Boulder gives a one-shot use of shuffling boulder colors randomly. The grid shape will stay fixed. You can bank 1 shuffle use at a time, and it carries across levels.</td>
</tr>
<tr>
<td style="width:70px; padding-right:5px;"><img src="/public/destruct-o-match/dom3_boulder_undo.jpg"/></td>
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

An aside here: in testing on the Flash version, I've seen more than 3 powerups appear, so the algorithm used there differs in some way.


Step 3: Sanity Check
------------------------------------------------------------------------------------------------------

Before going too far down the rabbit hole, let's check how much impact skill has on Destruct-o-Match scores. If the scores are mostly driven by RNG, it's not worth developing the AI more.

I implemented 3 basic strategies:

* **Random:** Removes a random block.
* **Top-Down, Left-Right:** This removes the top-most group, breaking ties by the left-most group.
* **Bottom-up, Right-Left:** This removes the bottom-most group, breaking ties on the right.

The idea with these strategies is that random is a simple baseline, that maps to a human player spamming clicks without thinking. (I have done this many, many times when I'm sick of playing.) Top-down and bottom-up are two suggested strategies from the JellyNeo fan page. Top-down will usually clear most currently available groups, but tends to not create new groups.
Bottom-up can create groups by causing more blocks to fall, but it can also break apart existing larger groups, which hurts bonus points.

For each strategy, I simulated 100 random games and plotted the distribution of scores.

![Baseline distribution scores](/public/destruct-o-match/baseline_distributions.png)
{: .centered }

The good news is that yep, there's a lot of difference to be had from skill. The average score already differs by 100 for these different strategies. This also lets us know that **usually, disrupting  existing groups is bad**. It's better to take the guaranteed points and not cause excessive block
falls unless you have a good reason to.

One last recommended human strategy is to remove blocks in order of color. The idea is that the reamining groups will connect more often, giving you more bonus points from removing large groups at once. We can try this strategy too, removing groups in color order, tiebreaking with the top-down left-right heuristic.

![Baseline distribution scores 2](/public/destruct-o-match/baseline_distributions2.png)
{: .centered }

Introduce color gives us another 100 points on average. We can try one more idea: if bottom-up is bad because it breaks apart large groups, maybe it'd be good to remove large groups first. Let's remove groups first in order of color, then in order of size, then in order of which is on top.

![Baselines 3](/public/destruct-o-match/baseline_distributions3.png)
{: .centered }

This doesn't seem to improve things, so let's not use it.

These baselines are all quite far from the avatar score of 2500. Even the luckiest game out of 100 attempts only gets to 2100 points. It is now finally time for the AI.


Step 4: The AI
-------------------------------------------------------------------------------------

I estimate that between resetting for a good level 1 and using shuffles + undos, I can get an extra 100 points, so my target is to average 2400 points in my Destruct-o-Match engine before playing for
real.

To truly max out score, it would be best to follow the example of AlphaZero or MuZero. Those methods
work by running a very large number of simulated games with MCTS, training a neural net to predict the value of boards, that would be iteratively refined by playing billions of games against itself.

I don't want to invest that much compute or time, so instead we're going to use something closer to the first chess AIs: search with a handcoded value function. We're going to evalute what's typically called the Q-value. Given the current state $$s$$ and a possible action $$a$$, the Q-value $$Q(s,a)$$ is defined as

$$
    Q(s,a) = reward(a) + Value(\text{next state})
$$

We then take the action $$a$$ that has largest Q-value.

As mentioned earlier, the reward in Destruct-o-Match is the points earned from the removed block.
How about the value? We can conservatively estimate a board's value as the sum of points we'd get from
every group that exists within it, plus the end-level bonus for every boulder that isn't in one of
those groups. This corresponds to removing every existing group and assuming no new groups will be
formed by the remaining blocks. Doing so should be hypothetically possible on most boards, if we
order the groups such that a group is removed only after every group above it has been removed.

IMAGE

There are some edge cases where this isn't possible, such as this double-C example, where groups
depend on each other in a cycle.

IMAGE

Additionally, this value function overestimates value when wilds are on the board, because the wild
will appear in multiple groups, but can only be removed once.

IMAGE

For the purposes of the AI though, the value estimate estimate just has to be "good enough" to not
mislead the search, so we'll just ignore these issues. Computing this value is easy, because we
already have to find every clearable group when finding the list of actions,

$$
    Value(state) = \sum_{\text{a possible}} reward(a)
$$

So, here is our new method for choosing actions.

1. From the current state, compute every possible action.
2. For each action, find the Q-value $$Q(s,a)$$.
3. Pick the action with best Q-value.
4. Break ties with the color then top-most heuristic that did best earlier.

Even though this only looks 1 move ahead, it's quite effective. By like, a **lot**.

![Search performance](/public/destruct-o-match/search.png)
{: .centered }

This is enough to give a **400** point boost on its own. This gain was big enough that I decided to
try playing a game with this AI, and I actually got pretty close to winning on my first try, with 2433 points.

![Score 1](/public/destruct-o-match/score1.png)
{: .centered }

The reason I got so many points is because something is buggy in the logic for end-level bonuses. I don't know how, but I got an extra 50 points in levels 3 and 4 that I should not have gotten. This is likely tied to a second beneficial bug, where levels 3 and 4 are only 12 x 15 instead of 13 x 15.

Still, this means we only need to crank out 70 more points! If we can get this close with looking 1 move ahead, let's do more.


Step 5: Just Go Harder
------------------------------------------------------------------------------------------

Early, we defined the Q-value as

$$
    Q(s,a) = reward(a) + Value(\text{next state})
$$

This is sometimes called the 1-step Q-value, because we check the value after doing 1 timestep.
We can generalize this to the n-step Q-value by defining it as

$$
    Q(s,a_1,a_2,\cdots,a_n) = r_1 + r_2 + \cdots + r_n + Value(\text{state after n moves})
$$

where each reward $$r_i$$ is the points we get from doing action $$a_i$$. We take the max over
all sequences of n actions, run the 1st action in the best sequence, then repeat.

One natural question to ask here is, why are we only running the 1st action from the best sequence? Why not run all n actions from that sequence? The reason is because our value estimate is only an
approximation of the true value. The further we project out, the more likely it is that our projected values are wrong. Taking just the 1st action and replanning from there mitigates this.

Unfortunately, doing an exhaustive search of 2 moves ahead is already too slow for my engine.
This is partly my fault, for doing it in single-threaded Python, but Destruct-o-Match is genuinely a rough game for exhausive search. The branching factor $$b$$ of a game is the number of valid moves
available per state. It's important because a depth $$d$$ lookahead will require considering
$$b^d$$ sequences of actions, which is exponential in $$b$$.

As a comparison point, the branching factor of Chess averages 31 to 35 legal moves.
Destruct-o-Match has an average branching factor of 34 moves. **Destruct-o-Match is as expensive to search as Chess.** This is actually so crazy to me, and makes me feel less bad about
spending a week on this project. If people can dedicate their life to Chess, I can dedicate a week
to a Neopets flash game.

To make things worse, the value function I'm using runs in $$O(b)$$ time, since I need to compute every group, so the run time is more like $$O(b^{d+1})$$. To get around this, we can use search tree
pruning. Instead of considering every possible action, at each timestep, we should consider only the $$k$$ most promising actions. This
will miss some potentially high reward sequences, but makes it more practical to search deeper,
which is often a worthwhile trade-off.

(Quick aside: the reason I jumped to pruning first is because I've seen it work before.
In college, I once went to a coding competition where we split into groups, and
had to code the best [Ntris](https://www.youtube.com/watch?v=hSp4E6EYA74) bot in 4 hours.
I handled game logic, while a teammate handled the search, and their pruned search
tree algorithm destroyed everyone. We won $500 in gift cards, it was pretty cool.)

Here's the new algorithm, assuming we prune all but the top $$k$$ actions.

1. From the current state, compute every possible action.
2. For each action, find its 1-step Q-value, $$r + Value$$.
3. Sort the Q-values and discard all but the top $$k$$ actions $$a_1, a_2, \cdots, a_k$$.
4. Repeat steps 1-3, only considering sequences that start with actions $$a_1$$ to $$a_k$$.
For each future state, evaluate all $$b$$ possible actions then take just the top $$k$$.
5. When we get to max depth $$d$$, stop, and take the first action of the best sequence.

There are now only $$k^d$$ different possible sequences, with $$k$$ choosable by us. The main choices now are how to set the number of expansions $$k$$ and max depth $$d$$ while still being efficient enough to be usable.

To understand the trade-off better, I did 3 runs. One with `Depth=2, Expand=3`, one with
`Depth=2, Expand=9`, and one with `Depth=3, Expand=3`. The first is to verify there are gains from
increasing search depth at all, and the second two are 2 compute-equivalent configurations,
one searching wider and the other searching deeper.

![Final Search Distributions](/public/destruct-o-match/final_search_distributions.png)
{: .centered }

The gains are getting harder to spot, so here are more exact averages.

Depth 1: 2233.38  
Depth 2, Expand 3: 2318.32  
Depth 2, Expand 9: 2343.34  
Depth 3, Expand 3: 2373.37  

From this, I concluded that searching deeper was better than searching wider, and we've gotten a gain
of 140 points compared to the original Depth 1 model. This should be enough for an avatar score! It's also near the limit of what I can reasonably evaluate. The plot above took 7 hours to simulate.

For the final real run, I decided to use a $$k$$ of 6 instead of 3. In local testing, Depth 3 Expand 6 took 1.5 seconds on average to pick an action on my laptop, which was short enough for my manual
inputting of the move to be the bottleneck, and this would be strictly better.

After setting it up, I played a game over the course of 3 hours, of which about 2 hours 45 minutes was entering boards into my script and 15 minutes was CPU processing time.

![Score 2](/public/destruct-o-match/score2.png)
{: .centered }

An avatar score! Hooray!


Outtakes and Final Thoughts
----------------------------------------------------------------------------------------

You may have noticed most of my time was spent on transcribing the board state. My original plan was to use computer vision to auto-translate
a screenshot of the webpage into the game state. I know this is possible, but unfortunately
I messed something up in my logic and haven't been able to debug it. I eventually decided that
fixing it would take more time than entering boards by hand.

After I got the avatar, I ran a full evaluation of the $$depth = 3, k = 6$$ configuration overnight.
It averages 2426.84 points, another 53 points over the $$depth = 3, k = 3$$ setup I evaluated earlier.
Based on this, you could definitely squeeze more juice out of more search compute, but I have no interest in doing so. I'm just here for the avatar.

Some final commentary, based on studying games played by the AI:

* **Most points are earned by getting near-perfect clears on early levels.** The AI frequently clears the first few levels with 0-3 blocks left, earning a ton of points. The AI fails to get any clear bonus by around level 5. Based on this, I suspect **early Fill powerups are bad**, because although
you could get more points due to having more boulders, it doesn't make up for losing 10 points per uncleared block.
* The AI jumps all over the board, constantly switching between colors, clearing groups near the top, and clearing groups near the bottom. Imitating it with human play would require doing continual group size calculations, which is definitely possible but seems very annoying.
* The AI consistenly assembles groups of 16+ boulders in the early levels. **This makes early undos very strong**, since they are easily worth 32-40 points. My winning run was partly from a Multiplier in level 1, but was really carried by getting 2 Undos in level 2.
* **Whoever designed the Flash game was a monster.** In the original Flash game, you only get to proceeed to the next level if you earn enough points, with the point thresholds increasing each level.
But it actually gets *harder* to earn points as you go through the levels.
My AI averages 203 points in level 7 and 185 points in level 9. If the point thresholds were enforced in the HTML5 version, the AI would regularly fail at level 7 or 8.
