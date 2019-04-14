---
layout: post
title:  "OpenAI Finals"
date:   2019-04-13 21:27:00 -0800
---

OpenAI just beat OG, champions of [The International 8](https://liquipedia.net/dota2/The_International/2018),
in a 2-0 series. They also announced that in private, they had won three other pro series:
2-0 over [Team Lithium](https://liquipedia.net/dota2/Team_Lithium), 2-0 over [SG e-sports](https://liquipedia.net/dota2/SG_e-sports), and 2-0 over [Alliance](https://liquipedia.net/dota2/Alliance).
Pretty cool! I don't have a lot to add this time, but here are my thoughts.

OG Isn't the Top Team and That Doesn't Matter
-----------------------------------------------------------------------

After pulling off an incredible Cinderella story and winning TI8, OG went
through some troubles. My understanding is that they've started to recover, but
are no longer the consensus best team.

To show this, we can check the [GosuGamers DotA 2 rankings](https://www.gosugamers.net/dota2/rankings).
This assigns an lo rating to the top DotA 2 teams, based on their match history in tournaments.
At the time of this post, OG is estimated as the 11th best team.

I don't think this really matters, because as we've seen with the 1v1 bot, the
previous OpenAI Five match, and with AlphaStar, once your at the level of semi=pro,
reaching pro is more a matter of training time and steady incremental training
improvements than anything else. Going into the match, I thought the only way OG
would have a chance was if the restrictions were radically different from the ones
used at TI8. They weren't. Given that OpenAI Five beat a few other pro teams, I
believe this match wasn't a fluke and there's no reason they couldn't beat Secret
or VP or VG with enough training time.

Reaction Times Looked More Believable
-----------------------------------------------------------------------

I'm not sure if OpenAI added extra delay or not, but the bot play we saw felt
more fair and looked more like a player with really good mechanics, rather than
superhuman mechanics. There were definitely [some crazy outplays](https://clips.twitch.tv/PricklyHardOrcaBatChest)
but it didn't look impossible for a human to do it - it just looked very, very
difficult.

If I had to guess, it would be that the agent still processes input at the same
speed, but has some fixed built-in delay between deciding an action and actually
executing it. That would let you get more believable reactions without compromising
your ability to observe environment changes that are only visible for fractions
of a second.

Limited Hero Pool is a Bit Disappointing
-----------------------------------------------------------------------

I think it's pretty awesome that OpenAI Five won, but one thing I'm interested
by is the potential for AI to explore the hero pool and identify strategies that
pro players have overlooked. We saw this in Go with the [3-3 invasion followup](https://senseis.xmp.net/?44Point33InvasionJoseki).
We saw this in [AlphaStar]({% post_url 2019-02-22-alphastar %}), with the
strength of well microed Stalkers, although the micro requirements seem
very high.
With OpenAI Five, we saw that perhaps early buybacks have value, although again,
it's questionable whether this makes sense or whether the bot is just playing
weird. (And the bot does play weird, even if it does win anyways.)

When you have a limited hero pool, you can't learn about unimplemented heroes,
and therefore the learned strategies may not generalize to full DotA 2, which
limits the insights humans can take away from the bot's play. And that's a real
shame.

It seems unlikely that we'll see an expansion of the hero pool, given that this
is the last planned public event. It's a lot more compute for what is already
a compute heavy project. It would also require learning how to draft, assuming
draft works the same as the TI8 version. In the
TI8 version, the win rate of every possible combination of heroes is evaluated,
and the draft is done by picking the least exploitable next hero. Given
a pool of 17 heroes, there are $$\binom{17}{5}\binom{12}{5}\cdot 2 = 9801792$$
different hero combinations, which is large, but brute-forceable. A full hero
pool breaks this quick hack and requires using a learned approach instead. I'm
sure it's doable (there's [existing work for this](https://arxiv.org/pdf/1806.10130.pdf)),
but it's another hurdle that makes it look even more unlikely.

A Million 3k MMR Teams at a Million Keyboards Have to Win Eventually
-----------------------------------------------------------------------

At the end of the match, OpenAI announced that they were opening signups to
allow everyone to play against or with OpenAI Five. It's only going to be up
for a few days, but it's still exciting nonetheless. I have no idea how much
the inference will cost in cloud credit (which is presumably why it's only
running for a few days).

I fully expect somebody to figure out a cheese strategy that the bot has trouble
handling. I also expect every pro team to try beating it for kicks, because
if they can beat it consistently, can you imagine how much free PR they'd get?
If they don't beat it, they don't have to say anything, so it seems like a
win-win.

There is a chance that the bot is genuinely too good, in an
["AlphaGo Master goes 60-0 against pros"](https://deepmind.com/research/alphago/match-archive/master/) kind of way,
but that was 60 games, and way more than
60 people are going to try to beat OpenAI Five. They're not all going to be pros,
but scale is going to matter more than skill here.

When OpenAI let TI attendees play their 1v1 bot that beat several pros, people
were able to find [all sorts of cheese strategies that worked](https://www.theflyingcourier.com/2017/9/11/16285390/elon-musk-open-ai-esports-bot-dota-2-defeated-beaten).
It was an older version of the bot, so perhaps history doesn't have precedence,
but I'm going to guess somebody is going to figure out something sufficiently
out-of-distribution.

We Still Take Pride in Few Shot Learning
-------------------------------------------------------------------------

In the interview with Purge after the match, OG N0tail had an interesting comment

> Purge: If you guys got to play 5 matches right now against them, do you think you
> could take at least 1 win?
>
> N0tail: Yeah, for sure. For sure 1 win. If we played 10, we'd start winning more, and if
> we could play 50 games against them, I believe we'd start winning very very reliably.

[Source](https://www.twitch.tv/videos/410533063?t=03h12m28s)
{: .centered }

He later elaborated that he felt the bot had exploitable flaws in how it played
around vision, but I think the more important note is that we take pride in
our ability to actively try new things based on very few examples. The debate
over how to do this is endless, but it makes me think that if somebody manages
to demo impressive few-shot learning, we'll have a lot of trouble finding a new
thing we're better than AIs at.
