---
layout: post
title:  "OpenAI Finals"
date:   2019-04-13 21:27:00 -0800
---

OpenAI just beat OG, champions of The International 8, in a 2-0 series.
They also announced that in private, they had won three other pro series:
2-0 over Team Lithium, 2-0 over SG e-sports, and 2-0 over Alliance. Pretty cool!
I don't have a lot to add this time, but here are my thoughts.

1. OG Isn't the Top Team and That Doesn't Matter

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

2. Reaction Times Looked More Believable

I'm not sure if OpenAI added extra delay or not, but the bot play we saw felt
more fair and looked more like a player with really good mechanics, rather than
superhuman ones. There were definitely [some crazy outplays](https://clips.twitch.tv/PricklyHardOrcaBatChest)
but it didn't look impossible for a human to do it - it just looked very, very
difficult.

If I had to guess, it would be that the agent still processes input at the same
speed, but has some built-in delay between deciding an action and actually
executing it. That would let you get more believable reactions without compromising
your ability to observe environment changes that are only visible for fractions
of a second.

3. Limited Hero Pool is a Bit Disappointing

I think it's pretty awesome that OpenAI Five won, but one thing I'm interested
by is the potential for AI to explore the hero pool and identify strategies that
pro players have overlooked. We saw this in Go, we saw a little bit of this in
AlphaStar, but I'm not sure if we saw it from OpenAI Five. At best, we saw
that early buybacks may have value, but it seems like people think the bot was
just being weird.

The issue is that when you have a limited hero pool, you can't give insights
into the strengths of different hero strategies, because unimplemented heros
could have counters that make those straegies fail in full Dota 2.

It seems unlikely that we'll see an expansion of the hero pool. It's a lot
more compute for what is already a pretty heavy project. It would also require
learning how to draft, assuming draft works the same as the TI8 version. In the
TI8 version, the win rate of every possible combination of heros is evaluated,
and the draft is done by picking the least exploitable next hero. Given
a pool of 17 heros, there are $$\binom{17}{5}\binom{12}{5}\cdot 2 = 9801792$$
different hero combinations, which is large, but brute-forceable. A full hero
pool breaks this quick hack and requires doing something smarter.

4. A Million 3k MMR Teams at a Million Keyboards Have to Win Eventually

At the end of the match, OpenAI announced that they were opening signups to
allow everyone to play against or with OpenAI Five. It's only going to be up
for a few days, but it's still exciting nonetheless. I have no idea how much
the inference will cost in cloud credit (which is presumably why it's only
running for a few days.)

I fully expect somebody to figure out a cheese strategy that the bot has trouble
handling. I also expect every pro team to try beating it for kicks, because
if they can beat it consistently, can you imagine how much free PR they'd get?
If they don't beat it, they don't have to say anything, so it seems like a
win-win.

There is a chance that the bot is genuinely too good, in an "AlphaZero goes
50-0 against pros" kind of way, but that was 50 games, and way more than
50 people are going to try to beat OpenAI Five. Historically, people who
attended The International the year OpenAI released their 1v1 bot were able
to figure out ways to beat the bot, so I'm leaning more towards beatable than
not.
