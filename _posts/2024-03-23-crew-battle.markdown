---
layout: post
title:  "Solving Crew Battle Strategy With Math"
date:   2024-03-23 22:11:00 -0700
---

In Super Smash Bros tournaments, there's occasionally an event called a crew battle. (They show up in other
fighting games too, but I mostly watch Smash.) Two teams of players compete in a series of 1v1 matches.
For the first match, each team picks a player simultaneously. They fight, and the loser is eliminated, while
the winner stays in. The losing team then picks a player to go in. Elimination matches repeat until one team
is out of players.

These events are always pretty hype. People like team sports!
They're also often structured in a regional way (i.e. US vs Japan, West Coast vs East Coast), which
can emphasize and play up regional rivalries. The strategy for deciding who to send in can be complicated,
and although it's usually done by intuition, I've always wondered what optimal strategy would be.

The reason it's complicated is that fighting game character matchups aren't perfectly balanced. Some
characters counter other characters. Sometimes players are unusually good at a specific matchup - a Fox v Fox
matchup is *theoretically* 50-50 but some players have earned a reputation for being really good at
Fox dittos. And how about generic player strength? Typical rule of thumb is to keep your strongest player
(the anchor)
for last, because the last player faces the most psychological pressure. But if we ignored those factors,
is that actually correct? When do you send in your 2nd strongest player, or weakest player?
**What is the optimal crew battle strategy?**


Theory
-------------------------------------------------------------------------------------

Let's formalize the problem a bit. For the sake of simplicity, I will ignore that Smash games have
stocks, and assume each match is a total win or loss. I expect the conclusions to be similar anyways.

Let's call the teams $$A$$ and $$B$$. There are $$n$$ players on each team, denoted as $$\{a_1, a_2, \cdots, a_n\}$$
and $$\{b_1, b_2, \cdots, b_n\}$$. Each player has a certain chance of beating each other player
which can be described as an $$n \times n$$ matrix of probabilities, where row $$i$$ column $$j$$ is
the probability $$a_i$$ beats $$b_j$$. We'll denote that as $$\Pr(a_i > b_j)$$.
This matrix doesn't need to be symmetric, or have its rows or columns sum to 1.

$$
\begin{bmatrix}
    \Pr(a_1 > b_1) & \Pr(a_1 > b_2) & \cdots & \Pr(a_1 > b_n) \\
    \Pr(a_2 > b_1) & \Pr(a_2 > b_2) & \cdots & \Pr(a_2 > b_n) \\
    \vdots & \vdots & \ddots & \vdots \\
    \Pr(a_n > b_1) & \Pr(a_n > b_2) & \cdots & \Pr(a_n > b_n)
\end{bmatrix}
$$

We'll call this the **matchup matrix**. Each team knows the matchup matrix, and has a goal of
maximizing their team's win probability. To make this concrete, we could take the example
of a rock-paper-scissors crew battle. Each team has 3 players: a rock player, a paper player,
and a scissors player. That would give the following matchup matrix.

$$
\begin{array}{c|ccc}
    & \textbf{rock} & \textbf{paper} & \textbf{scissors} \\ \hline
    \textbf{rock} & 0.5 & 0 & 1 \\
    \textbf{paper} & 1 & 0.5 & 0 \\
    \textbf{scissors} & 0 & 1 & 0.5
\end{array}
$$

Normally, in RPS you'd play again on a tie. Since there are no ties in crew battles, we'll instead
say that if both players match, we pick a winner randomly. Here's an example game:

<pre>
A picks rock, B picks scissors
A rock beats B scissors
B sends in paper
A rock loses to B paper
A sends in scissors
A scissors beats B paper
B sends in rock
A scissors loses to B rock
A sends in paper
A paper beats B rock
B is out of players - A wins.
</pre>

This is a pretty silly crew battle because of the lack of drama, but we'll come back to this
example later.

First off: given a generic matchup matrix, should we expect there to be an efficient algorithm that solves the crew battle?

My suspicion is, probably not. Finding the optimal strategy is at some level similar to picking
the optimal order of the $$N$$ players on each team, which immediately
sets off [travelling salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) alarm
bells in my head. Solving crew battles seems like a strictly harder version of solving regular
matrix payoff games, where you only have 1 round of play, and a quick search I did indicates those
are already suspected to be hard to solve generally.
(See [Daskalakis, Goldberg, Papadimitriou 2009](https://people.csail.mit.edu/costis/simplified.pdf) if
curious.)

(July 2024 correction: This isn't exactly relevant. The Daskalakis result is about general matrix payoffs, but
crew battles are zero-sum. The Nash equilibria in zero-sum games are efficiently computable via linear programming in time
polynomial in the number of actions. Thanks [Jon Schneider](https://jschnei.github.io/) for the correction. Both he and I
believe crew battles are still hard in general, but more because of the exponentially large action space than matrix payoff
hardness.)

Even though there isn't an efficient algorithm, there definitely is **an** algorithm.
Let's define a function $$f$$, where $$f(p, team, S_A, S_B)$$ is the probability team $$A$$ wins if

* The player who just won is $$p$$.
* The team deciding to who to send in is $$team$$ (the team that $$p$$ is **not** on).
* $$S_A$$ is the set of players left on team A, ignoring player $$p$$.
* $$S_B$$ is the set of players left on team B, ignoring player $$p$$.

Such an $$f$$ can be defined recursively. Here are the base cases.

* If $$team = A$$ and $$S_A$$ is empty, then $$f(p, team, S_A, S_B) = 0$$, since A has lost due to having 0 players left.
* If $$team = B$$ and $$S_B$$ is empty, then $$f(p, team, S_A, S_B) = 1$$, since A has won due to B having 0 players left.

(One clarification: the crew battle is not necessarily over if $$S_A$$ or $$S_B$$ is empty. When a team is on their last player,
they will have 0 players left to send in, but their last player could still beat the entire other team if they play well enough.)

Here are the recursive cases.

$$
\begin{align*}
f(a_i, B, S_A, S_B) = \min_{j \in S_B} & \Pr(a_i > b_j) f(a_i, B, S_A, S_B - \{b_j\}) \\
& + (1-\Pr(a_i > b_j)) f(b_j, A, S_A, S_B - \{b_j\})
\end{align*}
$$

(It is Team B's turn. They want to play the player $$b_j$$ that minimizes the probability that team A wins.
The current player will either stay as $$a_i$$ or change to $$b_j$$.)

$$
\begin{align*}
f(b_j, A, S_A, S_B) = \max_{i \in S_A} & \Pr(a_i > b_j) f(a_i, B, S_A - \{a_i\}, S_B) \\
& + (1-\Pr(a_i > b_j)) f(b_j, A, S_A - \{a_i\}, S_B)
\end{align*}
$$

(The reverse, where it's team A's turn and they want to maximize the probability A wins.)

Computing this $$f$$ can be done with dynamic programming, in $$O(n^22^{2n})$$ time. That's not going to work
at big scales, but I only want to study teams of like, 3-5 players, so this is totally doable.

One neat thing about crew battles is that after the first match, it turns into a turn-based perfect
information game. Sure, the outcome of each match is random, but once it's your turn, the opposing team is locked
into their player. That means we don't have to consider strategies that randomly pick among the remaining players - there
will be exactly one reply that's best. And that means the probability of winning the crew battle assuming optimal
play is locked in as soon as the first match is known.

This means we can reduce all the crew battle outcomes down to a single
$$n \times n$$ matrix, which I'll call the **crew battle matrix**. Let $$C$$ be that matrix. Each entry $$C_{ij}$$ in the crew battle
matrix is the probability that team A wins the crew battle, if in the very first match A sends in $$a_i$$
and B send in $$b_j$$.

$$
\begin{align*}
C_{ij} = &\Pr(a_i > b_j) f(a_i, B, S_A - \{a_i\}, S_B - \{b_j\}) \\
&+ (1-\Pr(a_i, b_j)) f(b_j, A, S_A - \{a_i\}, S_B - \{b_j\})
\end{align*}
$$

$$
C =
\begin{bmatrix}
    C_{11} & C_{12} & \cdots & C_{1n} \\
    C_{21} & C_{22} & \cdots & C_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    C_{n1} & C_{n2} & \cdots & C_{nn}
\end{bmatrix}
$$

This turns our original more complicated problem into exactly a 1 round matrix game like
[prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma) or [stag hunt](https://en.wikipedia.org/wiki/Stag_hunt)...assuming
we have $$f$$. But computing $$f$$ by hand is really annoying, and likely does not have a closed form.
There's no way to get $$f$$ computed for arbitrary crew battles unless we use code.


So I Wrote Some Python Code to Compute $$f$$ for Arbitrary Crew Battles
----------------------------------------------------------------------------

Let's consider the RPS crew battle again. Here's the matchup matrix:

$$
matchup: \begin{array}{c|ccc}
    & \textbf{rock} & \textbf{paper} & \textbf{scissors} \\ \hline
    \textbf{rock} & 0.5 & 0 & 1 \\
    \textbf{paper} & 1 & 0.5 & 0 \\
    \textbf{scissors} & 0 & 1 & 0.5
\end{array}
$$

and here's what my code outputs for the crew battle matrix, assuming optimal play.

$$
crew battle: \begin{array}{c|ccc}
    & \textbf{rock} & \textbf{paper} & \textbf{scissors} \\ \hline
    \textbf{rock} & 0.5 & 0 & 1 \\
    \textbf{paper} & 1 & 0.5 & 0 \\
    \textbf{scissors} & 0 & 1 & 0.5
\end{array}
$$

No, that's not a typo. The two are identical! Let's consider a crew battle of "noisy RPS", where
rock is only favored to beat scissors, rather than 100% to win, and so on.

$$
matchup: \begin{array}{c|ccc}
    & \textbf{rock} & \textbf{paper} & \textbf{scissors} \\ \hline
    \textbf{rock} & 0.5 & 0.3 & 0.7 \\
    \textbf{paper} & 0.7 & 0.5 & 0.3 \\
    \textbf{scissors} & 0.3 & 0.7 & 0.5
\end{array}
$$

$$
crew battle: \begin{array}{c|ccc}
    & \textbf{rock} & \textbf{paper} & \textbf{scissors} \\ \hline
        \textbf{rock} & 0.500 & 0.399 & 0.601 \\
            \textbf{paper} & 0.601 & 0.500 & 0.399 \\
                \textbf{scissors} & 0.399 & 0.601 & 0.500 \\
                \end{array}
                $$

Intuitively, I feel it makes sense that this pulls towards the original RPS matrix - in some sense,
the crew battle is like playing 3 rounds of RPS instead of 1, just with more complicated restrictions.

Here's the log of a sample game.

<pre>
Game start, A = rock B = scissors
Win prob for A is 0.601
A = rock beats B = scissors
If B sends in paper: A wins 0.729
If B sends in rock: A wins 0.776
B sends in paper
A = rock beats B = paper
If B sends in rock: A wins 0.895
B sends in rock
A = rock beats B = rock
B has no more players
A wins
</pre>

Bad beat for team B here, getting entirely swept by rock.

For good measure, here's a random matchup matrix and the corresponding game matrix.

$$
matchup: \begin{array}{c|ccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 \\ \hline
        \textbf{a}_1 & 0.733 & 0.666 & 0.751 \\
            \textbf{a}_2 & 0.946 & 0.325 & 0.076 \\
                \textbf{a}_3 & 0.886 & 0.903 & 0.089 \\
                \end{array}
$$

$$
crew battle: \begin{array}{c|ccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 \\ \hline
        \textbf{a}_1 & 0.449 & 0.459 & 0.757 \\
            \textbf{a}_2 & 0.748 & 0.631 & 0.722 \\
                \textbf{a}_3 & 0.610 & 0.746 & 0.535 \\
                \end{array}
$$

Alright. Let's try something new. What if all player matchups are transitive? Suppose each
player has a certain power level $$p$$, and if players of power levels $$p$$ and $$q$$
fight, the power level $$p$$ player wins $$p/(p+q)$$ of the time. Below is a random matchup
matrix following this rule.
I've sorted the players such that $$a_1$$ and $$b_1$$ are weakest, while $$a_3$$ and $$b_3$$
are strongest. Since the matchup matrix is the win probability of A, the values go down
when reading across a row (fighting better B players), and up when going down a column
(fighting better A players)

$$
matchup: \begin{array}{c|ccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 \\ \hline
        \textbf{a}_1 & 0.289 & 0.199 & 0.142 \\
            \textbf{a}_2 & 0.585 & 0.462 & 0.365 \\
                \textbf{a}_3 & 0.683 & 0.568 & 0.468 \\
                \end{array}
$$

$$
crew battle: \begin{array}{c|ccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 \\ \hline
        \textbf{a}_1 & 0.385 & 0.385 & 0.385 \\
            \textbf{a}_2 & 0.385 & 0.385 & 0.385 \\
                \textbf{a}_3 & 0.385 & 0.385 & 0.385 \\
                \end{array}
$$

...Huh. This suggests *it doesn't matter who each team sends out first*. The probability
of winning the crew battle is the same. Trying this with several random 3x3s reveals the same pattern.

Maybe this is just because 3-player crew battles are weird? Let's try this on a 5-player crew battle.

$$
matchup:
\begin{array}{c|ccccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 & \textbf{b}_4 & \textbf{b}_5 \\ \hline
        \textbf{a}_1 & 0.715 & 0.706 & 0.564 & 0.491 & 0.340 \\
            \textbf{a}_2 & 0.732 & 0.723 & 0.584 & 0.511 & 0.358 \\
                \textbf{a}_3 & 0.790 & 0.782 & 0.659 & 0.591 & 0.435 \\
                    \textbf{a}_4 & 0.801 & 0.794 & 0.675 & 0.608 & 0.453 \\
                        \textbf{a}_5 & 0.807 & 0.800 & 0.682 & 0.616 & 0.461 \\
                        \end{array}

                        $$

$$
crew battle:
\begin{array}{c|ccccc}
    & \textbf{b}_1 & \textbf{b}_2 & \textbf{b}_3 & \textbf{b}_4 & \textbf{b}_5 \\ \hline
        \textbf{a}_1 & 0.731 & 0.731 & 0.731 & 0.731 & 0.731 \\
            \textbf{a}_2 & 0.731 & 0.731 & 0.731 & 0.731 & 0.731 \\
                \textbf{a}_3 & 0.731 & 0.731 & 0.731 & 0.731 & 0.731 \\
                    \textbf{a}_4 & 0.731 & 0.731 & 0.731 & 0.731 & 0.731 \\
                        \textbf{a}_5 & 0.731 & 0.731 & 0.731 & 0.731 & 0.731 \\
                        \end{array}
$$

Same thing occurs! Let's play a sample game. Even if the win probability is the same no matter
who starts, surely the choice of who to send out in the future matches matter.

<pre>
Game start, A = 1 B = 2
Win prob for A is 0.731
A = 1 beats B = 2
If B sends in 0: A wins 0.804
If B sends in 1: A wins 0.804
If B sends in 3: A wins 0.804
If B sends in 4: A wins 0.804
B sends in 0
A = 1 beats B = 0
If B sends in 1: A wins 0.836
If B sends in 3: A wins 0.836
If B sends in 4: A wins 0.836
B sends in 1
A = 1 loses B = 1
If A sends in 0: A wins 0.759
If A sends in 2: A wins 0.759
If A sends in 3: A wins 0.759
If A sends in 4: A wins 0.759
A sends in 0
A = 0 beats B = 1
If B sends in 4: A wins 0.800
If B sends in 3: A wins 0.800
B sends in 4
A = 0 beats B = 4
If B sends in 3: A wins 0.969
B sends in 3
A = 0 beats B = 3
B has no more players
A wins
</pre>

The probability of A winning the crew battles shifts as matches are decided in favor of A or B, but the
win probability *does not change* for any of the choices.

I found this pretty surprising! Going into this I assumed there would be some rule of thumb
tied to difference in skill level. I certainly didn't expect it to not matter at all.
This result does depend on how we've modeled skill, that player with skill $$p$$ beats player with skill $$q$$ with probability $$p/(p+q)$$.
However, this model is very common. It's called the [Bradley-Terry model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model) and
is the basis of Elo ratings. (And the basis for tuning AI chatbot responses based on human feedback.)

Let's write up this observation more formally.

**Conjecture:** Suppose you have an $$N$$ player crew battle, with players $$A = \{a_1, a_2, \cdots, a_N\}$$ and $$B = \{b_1, b_2, \cdots, b_N\}$$. Further suppose each
player has a non-negative skill level $$p$$, and every matchup follows $$\Pr(a_i > b_j) = p_{a_i} / (p_{a_i} + p_{b_j})$$. Then the probability $$A$$
wins the crew battle does not depend on strategy.

I haven't proved this myself, but it feels very provable. Consider it an exercise to prove it yourself.


So...What Does This Mean?
------------------------------------------------------------------------

Assuming this conjecture is true, I believe it means **you should entirely
ignore player strength when picking players, and should only focus on factors that aren't tied to skill, like character matchups**.
In *Super Smash Bros. Melee*, Fox is favored against Puff, so if you're playing against Hungrybox (the best Puff player of all time),
this suggests you should send in Generic Netplay Fox even though they'll most likely get wrecked.
And conversely, it suggests a crew should *avoid* sending Hungrybox in if Generic Netplay Fox
is in the ring, even though Hungrybox would probably win.

This is a pretty extreme conclusion, and I wouldn't blindly follow it.
Psychologically, it's good for team morale if everyone can
contribute, and sending people into matchups with a big mismatch in skill hurts that. But also, this
suggests that crew battle strategy really isn't that important in the first place! At the top level, it's
rare to see very lopsided character matchups. Pro players tend to pick strong characters that have good
matchups against most of the field. Given that the lopsided matchups are the only ways to get edges via
strategy, the math suggests that team captains actually don't have much leverage over the outcome of
the crew battle.

If your crew loses, you don't get to blame bad crew battle strategy. Your crew is just worse. Deal with it, take the L.

July 2024 edit: [Jon Schneider](https://jschnei.github.io/) reached out to let me know the conjecture above is true and is
a folklore result in some math circles. To prove it, you can model fights as independent exponential random variables,
where each player starts with a lifespan sampled from their distribution, and expend life until one player runs out.
If two players sample lifespans from exponentials with mean $$\mu_1, \mu_2$$, then the probability player 1 wins is $$\mu_1 / (\mu_1+\mu_2)$$.
The result then follows from the memoryless property of exponentials - the expected lifespan of a player is always the same no matter
how long they've been fighting. From here you can show that the win probability is the probability team A's total lifespan exceeds
team B's total lifespan, and memoryless properties guarantee that total doesn't depend on ordering.
