---
layout: post
title:  "A New Online Dominion Client Approaches"
date:   2021-05-23 02:30:00 -0700
---

Online Dominion is getting yet another online implementation!

It's by [Temple Gates Games](https://www.templegatesgames.com/), and they're
aiming to release it for Android, iOS, and PC. It's unclear what will happen
to the existing Shuffle IT implementation, but my guess is that they will coexist.
Based on the [press articles](https://www.polygon.com/22440924/dominion-app-neural-network-ai-release-date-price),
the aim of this version is to provide the casual-friendly features that
Shuffle IT promised but never delivered on, like a mobile app, and better
single player experiences.
Somehow, this is the first time Dominion's
IP has been given to a developer with a proven track record of mobile app development,
so I'm looking forward to seeing what they do.

The part that caught my eye is that they'll have a "neural network
based AI". Now this could mean a lot of things, and the press articles predictably
don't clarify thigns very well.
Luckily, some devs are in the Dominion Discord and they answered questions others and I had
about how the AI works.

Their broad approach is inspired by [AlphaZero](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go).
There's a value network and policy network. The neural net is a Transformer-based architecture,
that takes in just the current game state. They've tried providing previous buys and didn't see
much improvement.
They then do self-play rollouts with Monte Carlo Tree Search to update the model.
They've said that with their current computation
budget, the rollouts tend to reach a few turns ahead. The model only trains against itself, no
attempts at seeding with human gameplay, and for now they've been training with a limited number
of Dominion expansions. Over time, they've been introducing new expansions, restarting
training from scratch whenever they add a new one. You can think of this as slowly increasing
the difficulty of the game, as the developers get better at tuning their AI.

Overall, this makes a lot of sense to me. I've long
believed that a strong Dominion AI is *doable*, but nontrivial to get right. Despite landing
perfectly in the intersection of my interests, I've never tried starting a side project for
Dominion AI because the difficulty seemed like it would require too much time investment.
(The other main reason is
that step 0 of any Dominion AI effort is to implement an efficient Dominion rules engine, and
I *really* didn't want to debug that.)

There have been a few attempts at Dominion AI.
Ian Davis [found some success with RL](https://ianwdavis.com/dominion.html), but
only played a version of the game with Province/Duchy/Estate/Gold/Silver/Copper. There was a [Stanford class project](http://cs230.stanford.edu/projects_fall_2019/reports/26260348.pdf)
that also used reinforcement learning on the Base set, successfully beating some of the bots
in [Dominiate](https://github.com/rspeer/dominiate-python).
In my mind, the one that got furthest along
is [Provincial](https://graphics.stanford.edu/~mdfisher/DominionAI.html) from 2014, which
was a genetic algorithm searching over different buy strategies, along with hardcoded play
rules.

There are a few reasons I believe the Temple Gates bot could do better than these projects.

* Since it is part of a bigger Dominion app, the project will be around for longer.
Dominion AIs are doable, but hard enough that you should expect it'll take at least
a few months to figure out, probably more in practice. Most of the side projects don't sustain themselves for that long.

* As far as I know, the Temple Gates implementation is the first one that doesn't use
hardcoded play rules. Instead, it allows the agent to choose what to do at every choice
point. This is *really* important at high-level Dominion. It's important enough that
[I wrote an article about it](https://dominionstrategy.com/2018/08/16/five-ways-to-get-more-out-of-your-turns/)
that barely scratches the surface of tactical play. One of the main reasons Dominion simulators
fell out of favor was that their hardcoded card-playing heuristics stopped matching up with
high level play, and this placed hard limitations on how realistic the simulations could be. Every AI attempt
since then has ignored play order and had the same problem. This new approach seems like the first one
that operates at a lower level of granularity, and therefore makes it the first method with the
*potential* to match expert humans. (Doing so is a different matter entirely!)

* In general, they are doing things that make sense for game AIs. Like, seriously, why has
no one tried AlphaZero-style methods to Dominion before? Pure RL without any search is
going to take forever to learn anything, whereas pure search doesn't interact well with the
randomness within Dominion. Something in between like AlphaZero seems good.

* They have some game AI expertise already. The keldon [Race for the Galaxy AI](http://keldon.net/rftg/)
is supposed to be quite good (I've never gotten into RftG strategy), and keldon is helping out
on this project too. So I think they already have an appreciation for some common pitfalls
in game AI development. For example, laypeople like to propose tons of game heuristics that
game AIs should use, but I think anyone who's worked with game AI knows that a *lot*
of reasonable-sounding heuristics don't actually help for inexplicable reasons.

So, color me interested. The main dangers I see is that although Dominion doesn't have the
bluffing mechanics of poker, it does have the heavy amounts of randomness that could make it hard to
get low variance estimates of win rate, creating very noisy updates during the learning process.
Additionally, although
they could potentially learn the engine play that dominates high-level gameplay, it seems like
it could be tricky for the bot to successfully explore those options. I think it is doable, if the bot learns
to play obvious engines (like Village-Wharf), and then slowly learns the less obvious engines. But
that seems like the threshold that will be trickiest to cross. They've mentioned the bot is already
quite good at Big Money + a few action card strategies, which is a good sign, but these strategies
are the easiest to discover. We'll see how it does.

Beta signups are [open now](https://twitter.com/Temple_Gates/status/1395073608297242625), so if
you like Dominion, go check it out!
