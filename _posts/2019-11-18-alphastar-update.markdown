---
layout: post
title:  "Brief Update on AlphaStar Predictions"
date:   2019-11-18 00:20:00 -0700
---

Around the end of October, the [Nature paper for AlphaStar](https://www.nature.com/articles/s41586-019-1724-z)
was released. The Nature version has more significant restrictions on APM and
camera movement, is able to play as all three races instead of just Protoss,
can play the same maps that humans play on the competitive ladder, and
reached Grandmaster level. However, it hasn't done the "go 50-0
against pros" that AlphaZero did. It won some games against pros, but lost games
as well. The rough consensus I've seen is that
AlphaStar still has clear gaps in game knowledge, but is able to win anyways
through very good mechanics.

I haven't read the Nature paper yet,
and I'm not going to do a detailed post like I did [last time]({% post_url 2019-02-22-alphastar %}),
since I've been a bit busy.
This is just to follow-up on the predictions I made.
I believe that if you make a public prediction, it's very
important to revisit it, whether you were right or wrong.

I made two sets of predictions. The first set came from [February 2019]({% post_url 2019-02-22-alphastar-part2 %}), shortly
after the TLO and MaNa showmatches.

> If no restrictions are added besides no global camera, I think within a year AlphaStar will be able to beat any pro, in any matchup, on any set of maps in a best-of-five series.

> If [APM restrictions] are added, it’s less likely AlphaStar will be that good in a year, but it’s still at least over 50%.

Since restrictions were added, the first prediction isn't relevant anymore. As
for the second prediction, there are still a few months before Feburary 2020,
but I'm a bit less confident. Maybe before I was 55% and now I'm more like 45%,
and this is assuming DeepMind keeps pushing on AlphaStar. I've honestly lost track
of whether that's happening or not.

In [July 2019]({% post_url 2019-07-11-still-here %}), I made this comment:

> In AI for Games news, Blizzard announced that AlphaStar will be playing on the live SC2 competitive ladder, to evaluate agent performance in blind trials. AlphaStar can now play as all three races, has more restrictive APM limits than their previous version, and has been trained to only observe information from units within the current camera view. Should be fun - I expect it to beat everyone in blind games by this point.

This prediction was rather decidedly wrong. AlphaStar was very strong, but was not
stomping every opponent it played against. Here, my mistake was overcorrecting
for announcement bias. Historically, DeepMind only announces something
publicly when they're very confident in its result. So, when they disclosed
that AlphaStar would be playing games on the EU ladder, I assumed that meant
it was a done deal. I'm now thinking that the disclosure was partly driven by
legal reasons, and that although they were confident it was worth doing human
evaluation, that didn't necessarily mean they were confident it would beat
all pro players. It only meant it was worth testing if it could.

Two concluding remarks. First, I personally found it interesting that I had
no trouble believing AlphaStar was going to be ridiculously superhuman just
6 months after the original showmatch. For what it's worth, I still think that
was reasonable to believe, which is a bit strange given how short 6 months is.

Second, we got spoiled by Chess, Go, and other
turn-based perfect information games. In those games, superhuman game AIs always ended up teaching us
some new strategy or new way to view the game, and that was because the only
way they could be superhuman was by figuring out better moves than humans
could. Starcraft is different. It's part finding the right move, and part
executing it, and that opens up new strategies in the search space. The fact
that AlphaStar can win with subhuman moves executed well is less a problem with
AlphaStar, and more a problem with the strategy space of APM-based games. If
it's an available and viable option, it shouldn't be surprising that AlphaStar
ends up picking a strategy that works. It's disappointing if you expected
something different, but most things are disappointing when they don't match
your expectations. So it goes.
