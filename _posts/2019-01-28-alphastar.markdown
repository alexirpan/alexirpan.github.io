---
layout: post
title:  "An Overdue Post on AlphaStar, Part 1"
date:   2019-01-28 01:41:00 -0800
---


In late January, DeepMind broadcasted a demonstration of their StarCraft 2 agent
AlphaStar. In Protoss v Protoss mirrors on a map used in pro play
([Catalyst LE](https://liquipedia.net/starcraft2/Catalyst_LE)), it successfully
beat two pro players from TeamLiquid, TLO (a Zerg player) and MaNa (a Protoss player).

This made waves in both the StarCraft and machine learning communities. I'm
mostly an ML person, but I played a lot of casual Brood War growing up and
followed the Brood War and SC2 pro scene for a bit.

As such, this is a two-part post. The first is a high-level overview of my
reactions to the AlphaStar match and other people's reactions to the match.
The second part, linked
[here]({% post_url 2019-01-29-alphastar-part2 %}), is a more detailed
discussion of what AlphaStar means for machine learning.

In other words, if you're interested in deep dives into AlphaStar's StarCraft
strategy, you may want to read something else. I recommend [this analysis video by Artosis](https://www.youtube.com/watch?v=_YWmU-E2WFc)
and [this VOD of MaNa's livestream about AlphaStar](https://www.youtube.com/watch?v=zgIFoepzhIo).

The [DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
for AlphaStar is pretty extensive, and I'll be assuming you've read that
already, since I'll be referring to sections of it throughout the post.


The Initial Impact
-------------------------------------------

It was never a secret that DeepMind was working on StarCraft II. One of the first
things mentioned after the AlphaGo vs Lee Sedol match was that DeepMind was
planning to look at StarCraft. They've given talks at Blizzcon, helped develop
the SC2 learning environment, and published a few papers about training agents
in StarCraft II minigames. It was always a matter of time.

For this reason, it hasn't made as big an impact on me as OpenAI's
1v1 DotA 2 bot.
The key difference isn't how impressive the results were, it was how surprising
it was to hear about them. No one knew DeepMind was looking at Go, or OpenAI was
looking at DotA 2, until they were officially announced.
Even for AlphaGo, DeepMind published a paper on Go evaluation
over a year before the AlphaGo Nature paper ([Maddison et al, ICLR 2015](https://arxiv.org/abs/1412.6564)).
It was on the horizon if you saw the right signs (see [my post on AlphaGo]({% post_url 2016-01-27-deepmind-go %}) if curious).

StarCraft 2 has had a steady stream of progress reports, and that's lessened the
shock of the initial impact. When you know a team has been working on StarCraft
for several years, and [Demis Hassabis tweets](https://twitter.com/demishassabis/status/1087774153975959552)
that the SC2 demonstration will be worth watching...well, it's hard not to expect *something* to happen.

In his post-match livestream, MaNa relayed a story about his DeepMind visit.
In retrospect it's funny to hear how far they went to conceal how strong
AlphaStar was in the days up to the event.

> Me [MaNa] and TLO are going to be representing TeamLiquid, right? They wanted to make
> sure there wasn't any kind of leak about the event, or what kind of show they
> were putting on. Around the office, we had to cover ourselves with DeepMind
> hoodies, because me and TLO are representing TeamLiquid, with the TeamLiquid
> hoodie and TeamLiquid T-shirt. We walk in day one
> and the project
> managers are like, "NOOOO, don't do that, don't spoil it, people will see!
> Here are some DeepMind hoodies, do you have a normal T-shirt?", and me and TLO
> are walking in with TeamLiquid gear. We didn't know they wanted to keep it that spoiler-free.

[(Starts at 1:13:19)](https://youtu.be/zgIFoepzhIo?t=4399)
{: .centered }

It's funny, because the cat was already partly out of the bag.

To be fair, the question was never about whether DeepMind had positive results. It was
about how strong their results were. On that front, they successfully hid their
progress and I was surprised at how strong the agent was.


The Aftershock
-----------------------------------------------

In 2016, shortly after the AlphaGo vs Lee Sedol match, I got into a conversation with
someone about AGI timelines. (Because, of course, whenever ML does something
new, some people will immediately debate what it means for AGI.) They thought
AGI was happening very soon. I thought it wasn't, and as an exercise they
asked what would change my mind.

I told them that given that DeepMind was working on StarCraft II, if they beat a
pro player within a year, I'd have to seriously revise my assumptions on the
pace of ML progress. I thought it would take five to ten years.

The first win in the AlphaGo vs Lee Sedol match was on March 9, 2016, and the
MaNa match was announced January 24, 2019. It took DeepMind just shy of three
years to do it.

I'll have to think about what that means for my calibration. It's tricky,
because
the last AI predictions questionnaire I took only asked about
moonshot AI projects. Accordingly, almost all of my guesses were
at least 10 years in the future. Therefore, even if many guesses were right, I
won't be able to observe they were right until 10 years have passed.
It's all a waiting game.

This is probably why people don't like debating with futurists who only make
long-term predictions. Luckily, I don't deal with people like that very
often.


Novel Strategies
---------------------------------------------------

AlphaStar's style, so to speak, seems to trend in the following directions.

* Never stop building probes, even when your main is saturated and your natural
  hasn't finished building yet.
* Build lots of Stalkers and micro them to flank and harass the enemy army until
  it's weak enough to lose to all-in engagement.
* Use a few other units to support those Stalkers.

From the minimal research I've done, none of these strategies are entirely new,
but AlphaStar pushed the limits of these strategies to new places. Players have massed
probes in the past, but they'll often stop when their main is saturated, since
you need to save 400 minerals for the new expansion.
Similarly, Stalkers have always been a
core Protoss unit, but AlphaStar seems to play around its traditional counters
by using exceptional Stalker micro to force early wins through a [timing push](https://liquipedia.net/starcraft2/Timing_Attack).

It's a bit early to tell whether humans should be copying these strategies, but
it's exciting that it's debatable in the first place.


TOUCH ON LEARNED UNIT COMPOSITIONS


The StarCraft AI Effect
-------------------------------------------

One of the running themes in machine learning is that [whenever somebody gets an AI to do something new, others immediately find a way to discount it](https://en.wikipedia.org/wiki/AI_effect).

Thanks to the wonders of livestreaming and Reddit, I was able to see this live,
and boy was that a sight to behold. It reminded me of the routine
["Everything is Amazing and Nobody is Happy"](https://www.youtube.com/watch?v=kBLkX2VaQs4).
(I understand that Louis C.K. has [a lot of baggage these days](https://en.wikipedia.org/wiki/Louis_C.K.#2017%E2%80%93present:_Sexual_misconduct_revelations_and_afterwards), but I haven't found
another clip that expresses the right sentiment, so I'm using it anyways.)

"Oh, AlphaStar has superhuman micro. That's not fair." Yes, it isn't. The
average actions per minute of AlphaStar is 280 APM, which is less than pro play,
but this isn't the full
picture. According to the [Reddit AMA](https://www.reddit.com/r/MachineLearning/comments/ajgzoc/we_are_oriol_vinyals_and_david_silver_from/eexs0pd/), the limitation is at most 600 APM every 5 seconds,
400 APM every 15 seconds, and 300 APM every 60 seconds. This was done to model
both average pro APM and burst APM, since players can often reach high peak APM
in micro-intensive situations. During the match itself, viewers spotted that
AlphaStar's burst APM sometimes reached 900 or even 1500 APM, far above what
we've seen from any human. These stats are backed up by the APM chart:
AlphaStar's average APM is smaller than MaNa's, but has a longer tail. (TLO's
numbers are inflated due to idiosyncracies in how he plays the game. MaNa's
numbers are more reflective of pro human APM.)

![APM Chart](/public/alphastar/apm.png)
{: .centered }

[From DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
{: .centered }

Yes, I would agree that this is an advantage in favor of AlphaStar. But it's
worth noting that before AlphaStar, it was still an open question whether bots
could beat pro players in the first place, with no restrictions on APM. What, is
the defeat of a pro player in any capacity at all not cool enough? *Are you not
entertained?*

AlphaStar has other advantages. It is given the raw
state instead of the visual one, which likely makes it easier to do precise
focus-firing of units. It is allowed to observe everything it has in vision at
once, which is undeniably an advantage on human players. To me, this
seems like a bigger advantage than any of the APM constraints. In one of the
games, MaNa built Dark Templars. Normally, a human won't spot DTs because of the
perpetual cloaking, unless they're looking at the right part of the map and spot
the shimmer for cloaked units.
AlphaStar spots Dark Templars the moment they walk into
AlphaStar's vision, because it's receiving raw game state and is observing
everything in its vision at once. There's literally no surprise factor.
AlphaStar can immediately start building Observers and they'll be ready by the
time the DTs cross the map.

Despite these obvious advantages that no human would ever have, I saw fewer
complaints about this, compared to the APM complaints. Why?


What's Up With APM?
-----------------------------------------------------------------

After thinking about the question, I have a few theories for why people care
about APM so much.

**First**, StarCraft is notorious for its high APM at the professional level.
This started back in Brood War, where there were absurd demonstrations of how
fast Korean pro players were playing the game.

<p class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/YbpCLqryN-Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

**Second**, micro is *the* flashiest and most visible StarCraft skills.
Any StarCraft highlight reel will have a moment where one
player's ridiculous micro lets them barely win a fight they should have lost.
For many people, micro is what makes StarCraft a good competitive game,
because it's a way for the better player to leverage their skill to win.

This is to the point where many outsiders are scared by StarCraft.
They think that if you don't have high APM, you can't play StarCraft. You'll
be so busy trying to get your units to do what you want that you won't have time
to think about any of the strategy.

This is wrong, and the best argument against it is the one Day[9] gave on the
eve of the release of StarCraft: Brood War Remastered (starts at 4:30).

<p class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/EP9F-AZezCU?start=270" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

> There is this illusion that in Brood War, you need to be excellent at your
> mechanics before you get to be able to do the strategy. There is this idea
> that if you practice for three months, you'll have your mechanics down and
> then get to play the strategy portion. This is totally false. [...] If you
> watch any pro play, stuff is going wrong **all the time.** They're losing
> track of drop ships and missing macro back at home and they have a geyser with
> 1 dude in it and they forget to expand. Stuff's going wrong all the time,
> because it's hard to be a commander.

Of course, APM does matter. Assuming all other skills are equal,
the player with higher APM is going to win, because they can execute things with
more speed and precision. I'm just saying that having high APM doesn't give you
a free win, and is nothing without a strategy behind it.

And in fact, this should be *obvious* if you look at existing StarCraft bots,
that have thousands of APM and yet are nowhere near pro level. Turns out
learning
StarCraft strategy is hard! If anything, I
find it very impressive that AlphaStar is actually *making good decisions with
the APM it has*. "Micro" involves a lot of rapid, small-scale decisions about
whether to engage or disengage, based off context about what units are around,
who has the better position and composotion, and guesses on where the rest of
your opponent's army is. It's *hard*, and AlphaStar can do it.

When I see AlphaStar microing three groups of Stalkers to simultaenously
do hit-and-runs on MaNa's army, it's hard to see how MaNa has a chance, but I'm
more impressed that AlphaStar can perform micro of this caliber.

This matters because of the **third** and final theory: they broke the implicit contract.

First, the viewers are told that AlphaStar has restrictions to act with human APM. Saying
this adds a bunch of implications: this will be a fair fight, AlphaStar will
not do things that humans can't do.

Then, AlphaStar does something superhuman with its micro.
Now the contract is broken. The match doesn't seem fair.

Soon, it evolves. The match *wasn't* fair. "Oh, it's just microing."
We saw a similar thing in the OpenAI Five showcase. The DotA team said that
OpenAI Five had 250ms reaction times, within human limits. One of the humans
picked Axe, aiming for Blink-Call engages. OpenAI Five would insta-Hex every
time as soon as they blinked within range, completely negating that strategy.
We would never expect humans to do this consistently, and now the match isn't
fair, and people start discounting the results.

No one cared when bots had thousands of APM, perhaps because they weren't
beating pros in the first place. And I claim that if AlphaStar had used
thousands of APM at all times, people would have been upset, but not nearly as
upset as they felt when their implicit contract was broken and the
human-restrictions weren't as restricting as they thought they would be.


What's Next?
------------------------------------------------------------------------

DeepMind is free to do what they want with AlphaStar. I suspect they'll try to
address the concerns people have brought up, and won't stop until they've
removed any doubt over ML's ability to beat pro StarCraft II players with
reasonable conditions.

Let me put it this
way: one of the faces of the project is Oriol Vinyals. Based on a [35 Under 35](https://www.technologyreview.com/lists/innovators-under-35/2016/pioneer/oriol-vinyals/) segment
in the MIT Technology Review, Oriol used to be the best Brood War player in
Spain. Then, he worked on a StarCraft AI at UC Berkeley. Eventually, he joined
DeepMind and started working on AlphaStar.

I don't think the AlphaStar team is looking at StarCraft as just another game to
conquer. I think they genuinely love the game and won't stop until AlphaStar is
both better than everyone and able to teach us something new about StarCraft II.

[Continue to Part 2]({% post_url 2019-01-29-alphastar-part2 %})
{: .centered }
