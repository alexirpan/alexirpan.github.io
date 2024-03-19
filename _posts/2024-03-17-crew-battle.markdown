---
layout: post
title:  "The Crew Battle Problem"
date:   2024-03-17 01:41:00 -0700
---

In fighting game tournaments, there's occasionally an event called a crew battle. Two teams of players compete
in a series of 1v1 matches. For the first match, each team picks their starter simultaneously.
After the first match, the winning player stays in, and the losing player is eliminated. The losing team
picks a player to go in, and it repeats until one team runs out of players.

These events are always pretty hype. People like team sports!
They're also often structured in a regional way (i.e. US vs Canada, West Coast vs East Coast), which
can emphasize and play up regional rivalries.

The strategy for these events can be pretty involved! Some of the considerations are discussed
in [this video](https://www.youtube.com/watch?v=Q_yteloGGJo). Briefly,

* Fighting game character matchups are asymmetric. If it's a Melee crew battle and you send out
a Jigglypuff player, you're probably getting replied with a Fox player, because Fox is a good counter.
So you might avoid sending in your Jigglypuff player in until the Fox players are eliminated.
* *Players* can be asymmetric. Usually the strongest player on a team is saved for last, because
they have to face the highest pressure, but some people's play styles may match up unusually well
against others.

I don't play fighting games myself that much, I just watch them. My impression is that
unless counterpicks are in play, the losing team usually sends in someone that's *close* in skill-level
to the current player. Informally, you want to save your best player for their best player. This makes
intuitive sense, and it's exciting for spectators because close matches are more fun to watch,
but I've always wondered if it's actually correct. **What is the optimal crew battle strategy?**


Theory
-------------------------------------------------------------------------------------

Let's formalize the problem a bit.

There are $$N$$ players on each team. I've used Smash Bros. as an example, where each player
has multiple stocks (lives), and stocks carry over between fights. For simplicity, let's ignore
this and assume players can't get "partially defeated".

In that case, we can describe the win probabilities between players as an $$N x N$$ matrix $$A$$,
where $$A_{ij}$$ is the probability player $$i$$ from team 1 beats player $$j$$ of team 2. Since
player strength varies, note this matrix doesn't need to be symmetric, or have its rows / columns
sum to 1.

EXAMPLE

Each team's goal is to maximize the probability their team wins.

First off: should we expect there to be an efficient algorithm that solves this?

I have not thought about it that much, but my suspicion is, probably not. Maximizing win probability
here sounds very similar to picking an optimal order of the $$N$$ players, which immediately
sets off [travelling salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) alarms
in my head. I hadn't looked into complexity of game theory before this post, but this crew
battle problem is essentially a more complex version of a typical game where you'd be allowed
to send in the same player multiple times. Finding the Nash equilbrium of even those games
is part of a complexity class called PPAD, which isn't quite NP-complete but expected to hold
hard problems within it. See [Daskalakis, Goldberg, Papadimitriou 2009](https://people.csail.mit.edu/costis/simplified.pdf)
for more.


Example: RPS Crew Battle
----------------------------------------------------------------------------

Let's consider this rock-paper-scissors crew battle again.

MATRIX

Each team has three players: rock, paper, and scissors. Rock beats paper, paper
beats scissors, and scissors beats rock. Since retries aren't part of a crew
battle, let's say that if both teams send out the same player, then the winner
is random with 50% probability.

Just due to the symmetry, I'd expect the optimal strategy to be for each team
to randomly pick who they send in first. That's what you're supposed to do
in standard rock-paper-scissors. As an example, let's say team 1 sent in rock, team 2
sent in scissors. Now what happens?

* Rock stays in, scissors is eliminated.
* Team 2 can send in paper or rock.
* If team 2 sends in paper, team 1 replies with scissors. Team 2 replies with rock. Team
1 replies with paper, and the crew battle's over for team 1. So paper is a 100% losing
move for team 2.
* If team 2 sends in rock, and loses the 50-50, then team 2 loses 100% of the time again.
(They'd have just paper left - which is strictly worse than having both paper + rock left.)
* If team 2 wins the 50-50, then the game state looks like this:

team 1: paper, scissors
team 2: rock (in play), paper

Team 1 will send in paper (and win). Team 2 will send in paper and either win or lose. If they
lose, it's over. If they win, team 1 can still send in scissors and guarantee the win.

So in other words, the fate of team 2 was sealed as soon as they lost the first match. The problem
is that once team 1 wins the first match, they're happy to just trade players 1-for-1 until team
2 runs out of players, and team 2 doesn't enough wild card potential to make up the deficit.

Still, this does reveal an important point: **each team's strategy is dynamic, and depends on
the current state of the game.** You could imagine a version of the game where each team
secretly writes down an order of (rock, paper, scissors), they both reveal their player order, and
they follow it to the end. It's a valid strategy but it loses the power of a dynamic order.
(From a control theory perspective, it's the differencee between an open-loop controller that
never re-plans and a closed-loop controller that does.)


Okay Time to Generalize
--------------------------------------------------------------------------

Earlier I argued there probably wasn't an efficient algorithm for solving crew battles. How
about inefficient ones?

Let's say there's some function $$f$$ that computes the win probability for team 1, assuming
both teams play optimally. After the first match, the state of a crew battle is:

* The current player $$a_{i}$$ or $$b_{j}$$.
* The set of players left for teams A and B, $$S_A$$ and $$S_B$$. These sets do not include the current player.
* Whose turn it is to send in a player, $$team_A$$ or $$team_B$$. (Technically this is redundant,
since the current player defines whose turn it is, but it'll be easier to explain this way.)

Such an $$f$$ can be defined recursively. We have the following base cases.

* $$f(a_i, S_A, \emptyset) = 1$$. (Team A wins if team B has no players left and the player left is from team A.)
* $$f(b_j, \emptyset, S_B) = 0$$. (The reverse.)

We then have these recursive cases:

* $$f(a_i, S_A, S_B) = \min_j p_{ij} f(a_i, S_A, S_B - \{b_j\}) + (1-p_{ij}) f(b_j, S_A, S_B - \{b_j\})
(It is Team B's turn. They want to play the player $$b_j$$ that minimizes the probability that team A wins.
The current player will either stay $$a_i$$ or change to $$b_j$$, depending on how the match goes.)
* $$f(b_j, S_A, S_B) = \max_i p_{ij} f(a_i, S_A - \{a_i\}, S_B) + (1-p_{ij}) f(b_j, S_A - \{a_i\}, S_B)
(The reverse, where it's team A's turn and they want to maximize win probability.)

One question you may have is that this definition assumes each player acts deterministically.
The important distinction is that after the 1st match, each player takes turns picking a player, and there's
no hidden information. The full state is perfectly known.
In such a perfect information turn-based scenario, it's always optimal to act deterministically. To make this
more concrete, say we have three players left. We compute that if we send in player 1, then everyone plays
perfectly afterwards, then we have a 30% chance. Sending in player 2 gives a 40% chance, and player 3 gives
a 50% chance. Then we should just always send in player 3. Randomly sending in player 1 or 2 does nothing
except bleed win probability.

The only time randomness is relevant is when deciding which player to send in at the start. Assuming
both players know the values of $$f$$ for all possible states, we can reduce the original matrix into
a pure 1-round win-probability matrix.

MATRIX

Thus, our game that initially looked more complicated that a payoff matrix can be turned into a
payoff matrix, as long as you can compute $$f$$. Computing $$f$$ is a different story, but based on the
equations above it can be done with dynamic programming in $$O(n^22^n)$$. It's not going to work at big scales,
but if teams are like, 3-5 players, this is totally doable.

So I coded up a random generator of 4-player crew battles (generate random win matrices), computed $$f$$ for
each of them, and dug in to see what strategies were there.
