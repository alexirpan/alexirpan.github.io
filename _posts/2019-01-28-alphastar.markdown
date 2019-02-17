---
layout: post
title:  "An Overdue Post on AlphaStar, Part 1"
date:   2019-01-28 01:41:00 -0800
---


In late January, DeepMind broadcasted a demonstration of their StarCraft 2 agent
AlphaStar. It plays Protoss v Protoss mirrors on a map used in pro play
([Catalyst LE](https://liquipedia.net/starcraft2/Catalyst_LE)). It successfully
beat two pro players from TeamLiquid, TLO (a Zerg player) and MaNa (a Protoss player).

This made waves in both the StarCraft community and ML community. I fall
*mostly* in the ML community, but like StarCraft as a game. I've barely played
StarCraft II, but I played a lot of Brood War growing up, and I've
lightly followed Brood War and SC2 pro play,

As such, this is a two-part post. This part (Part 1) is a high-level overview of how I
feel about AlphaStar and the impact it's had on StarCraft. The second part
(LINK) is a more detailed discussion of what AlphaStar means for machine learning.

In other words, if you're interested in deep dives into AlphaStar's strategy,
you may want to read something else. I recommend [the analysis video by Artosis](https://www.youtube.com/watch?v=_YWmU-E2WFc)
and [the commentary MaNa did over his own games](https://www.youtube.com/watch?v=zgIFoepzhIo).

The [DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
for AlphaStar is pretty extensive, and although I will cover some of what's
discussed there, I will not cover all of it. Please read that first, if you
haven't already.


The Initial Impact
-------------------------------------------

It was never a secret that DeepMind was working on StarCraft II. One of the first
things mentioned after the Lee Sedol vs AlphaGo match was that DeepMind was
planning to look at StarCraft. They've given talks at Blizzcon, helped develop
the SC2 learning environment, and published a few papers about training agents
in StarCraft II minigames. It was always a matter of time.

For this reason, it hasn't made as big an impact on me as AlphaGo or OpenAI's
initial DotA 2 work. The key difference isn't the impressiveness of the result,
it was that for both those works, no one knew DeepMind or Open AI was even
looking at these games until they were officially announced.

(Okay, yes, there were signs that AlphaGo was on the horizon about a year before
it actually happened, but personally, it wasn't clear to me that DeepMind cared
about Go enough to push the results with sufficient gusto.)

StarCraft 2 has had a steady stream of progress reports, and that's lessened the
shock of the initial impact. When you know a team has been working on StarCraft
for several years, and [Demis Hassabis tweets](https://twitter.com/demishassabis/status/1087774153975959552)
that the SC2 demonstration will be worth watching...well, it's hard not to expect *something* to happen.
In retrospect it's funny to hear how far they went to conceal how strong
AlphaStar was in the days up to the event.

> Me [MaNa] and TLO are going to be representing TeamLiquid, right? They wanted to make
> sure there wasn't any kind of leak about the event, or what kind of show they
> are putting on. Around the office, we had to cover ourselves with DeepMind
> hoodies, because me and TLO are representing TeamLiquid, with the TeamLiquid
> hoodie and TeamLiquid T-shirt. We walk in day one
> and the project
> managers are like, "NOOOO, don't do that, don't spoil it, people will see!
> Here are some DeepMind hoodies, do you have a normal T-shirt?", and me and TLO
> are walking in with TeamLiquid. We didn't know they wanted to keep it that spoiler-free.

[From MaNa livestream about his experience (starts at
1:13:19)](https://youtu.be/zgIFoepzhIo?t=4399)
{: .centered }

To be fair, the question was never about whether DeepMind had positive results. It was
about how strong their results were. On that front, they successfully hid their
progress and I was surprised at how strong the agent was.


The Aftershock
-----------------------------------------------

A few months after the AlphaGo match, I got into a conversation with
someone about AGI timelines. (Because, of course, whenever ML does something
new, there are some people who like to ask what it means for AGI.) They thought
AGI was happening very soon, and I thought it wasn't, and as an exercise they
asked what would change my mind.

I told them that given that DeepMind was working on StarCraft 2, if they beat a
pro player within a year, I'd have to seriously revise my assumptions on the
pace of ML progress. I thought it would take more like five years, maybe ten.

The first win in the AlphaGo vs Lee Sedol match was on March 9, 2016, meaning it
took DeepMind just shy of three years to do the same in StarCraft.

I'll have to think about whether that means I'm undercalibrated. The tricky part
here is that the last time I took a questionnaire about AI predictions, it only
asked about moonshot AI projects, and accordingly almost all of my guesses were
at least 10 years in the future. Given that I took this questionnaire two years
ago, I've yet to have any positives, but I won't be able to *observe* any
correct guesses for at least another 8 years. It's all a waiting game.

This is probably why people don't like debating with futurists that refuse to
make short-term predictions. Luckily, I don't deal with people like that very
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
but AlphaStar pushed theses strategies more aggresively. Players have massed
probes in the past, but they'll often stop when the main is saturated, saving
their minerals for the new expansion. Similarly, Stalkers have always been a
core Protoss unit, but AlphaStar seems to play around its traditional counters
by using exceptional Stalker micro to force wins before too many Immortals can
get online.

It's a bit early to tell whether humans should be copying these strategies, but
it's exciting that it's debatable in the first place.


The StarCraft AI Effect
-------------------------------------------

One of the running themes in machine learning is that [whenever somebody gets an AI to do something new, others immediately find a way to discount it](https://en.wikipedia.org/wiki/AI_effect).

Thanks to the wonders of livestreaming and Reddit, I was able to see this live,
and boy was that a sight to behold. It reminded me of the routine
["Everything is Amazing and Nobody is Happy"](https://www.youtube.com/watch?v=kBLkX2VaQs4).
(I understand that Louis C.K. has [a lot of baggage these days](https://en.wikipedia.org/wiki/Louis_C.K.#2017%E2%80%93present:_Sexual_misconduct_revelations_and_afterwards), but I haven't found
another clip that expresses the right sentiment, so I'm using it anyways.)

"Oh, AlphaStar has superhuman micro. That's not fair." Sure, it isn't. The
average actions per minute of AlphaStar is 280 APM, although this isn't the full
picture. According to the [Reddit AMA](https://www.reddit.com/r/MachineLearning/comments/ajgzoc/we_are_oriol_vinyals_and_david_silver_from/eexs0pd/), the limitation is at most 600 APM every 5 seconds,
400 APM every 15 seconds, and 300 APM every 60 seconds. This was down to model
both average pro APM and burst APM, since players can often reach high peak APM
in micro-intensive situations. During the match itself, viewers spotted that
AlphaStar's burst APM sometimes reached 900 or even 1500 APM, far above what
we've seen from any human. These stats are backed up by the APM chart:
AlphaStar's average APM is smaller than MaNa's, but has a longer tail. (TLO's
numbers are inflated due to idiosyncracies in how he plays the game. MaNa's
numbers are more reflective of human performance.)

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
games, MaNa built Dark Templars. Normally, a human won't know they're there
unless they're looking at the right part of the map and see the shimmer for a
cloaked unit. AlphaStar knows there are Dark Templars the moment they walk into
AlphaStar's vision, because it's receiving raw game state and is observing
everything in vision at once. There's literally no surprise factor.
AlphaStar just immediately starts building Observers to counter the DTs.

Despite these obvious advantages that no human would ever have, I did not see
that many complaints about them in Twitch Chat, compared to the ones about APM.
Why?


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

**Second**, micro is one of the flashiest and most visible StarCraft skills.
Open any StarCraft highlight reel and you'll usually find a moment where one
player's ridiculous micro lets them barely win a fight they should have lost.
For many people, micro is what makes StarCraft a good game.

This is to the point where many outsiders are scared off of StarCraft because
they think that if you don't have high APM, you can't play StarCraft. You'll
be so busy trying to get your units to do what you want that you won't have time
to think about any of the strategy.

This is wrong, and the best argument against it is the one Day[9] gave on the
eve of the release of StarCraft: Brood War Remastered.

<p class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/EP9F-AZezCU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

> There is this illusion that in Brood War, you need to be excellent at your
> mechanics before you get to be able to do the strategy. There is this idea
> that if you practice for three months, you'll have your mechanics down and
> then get to play the strategy portion. This is totally false. [...] If you
> watch any pro play, stuff is going wrong **all the time.** They're losing
> track of drop ships and missing macro back at home and they have a geyser with
> 1 dude in it and they forget to expand. Stuff's going wrong all the time,
> because it's hard to be a commander.

This isn't saying that APM isn't important. Assuming all other skills are equal,
the player with higher APM is going to win, because they can execute things with
more speed and precision. I'm just saying that having high APM doesn't give you
a free win.

And in fact, this should be *obvious* if you look at existing StarCraft bots,
that have thousands of APM and yet are nowhere near pro level. If anything, I
find it very impressive that AlphaStar is actually *making good decisions with
the APM it has*. "Micro" involves a lot of rapid, small-scale decisions about
whether to engage or disengage, based off context about the value of different
units, the strength of each army's composition, and who has the better position.
It's *hard*, and AlphaStar can do it.

When I see AlphaStar microing three groups of Stalkers to simultaenously
do hit-and-runs on MaNa's army, it's hard to see how MaNa has a chance. But I'm
not particularly upset by it either, since I'm too busy appreciating that
AlphaStar can perform micro of this caliber.

That leads to the **third** theory: they broke the implicit contract. First, the
viewers are told that AlphaStar has restrictions to act with human APM. Saying
this adds a bunch of implications: this will be a fair fight, AlphaStar will
not do things that humans can't do. Then, AlphaStar does something superhuman
with its micro. Now the contract is broken, the match doesn't seem fair, and who
would believe they watched a fair match? We saw a similar thing when the OpenAI
Dota team told people that OpenAI Five
had human reaction times of 250 ms, and then auto-interrupted all of Axe's
Blink-Call attempts.

Again, no one cared when bots had thousands of APM. Perhaps because they weren't
beating pros in the first place, but I think it's also because there is no
attempt to claim it's human-like in any ways.

For what it's worth, DeepMind is free to do what they want, but I suspect they
will try to address the concerns that people have brought up. Let me put it this
way: one of the faces of the project is Oriol Vinyals. Oriol [used to be the top
Brood War player in Spain, then worked on a StarCraft AI at UC Berkeley, then
eventually made his way to DeepMind to work on AlphaStar](https://www.technologyreview.com/lists/innovators-under-35/2016/pioneer/oriol-vinyals/).
It's not like StarCraft is just a hill to conquer. People really like the game
as well.

