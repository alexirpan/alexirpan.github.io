---
layout: post
title:  "Title TBD"
date:   2019-01-28 01:41:00 -0800
---

Rough Goal
-----------------------------------------------------------------

The original blog post is actually quite complete and I want to add commentary
on top of it, not summarize it.


In late January, DeepMind broadcasted a demonstration of their Starcraft 2 agent
AlphaStar. It plays Protoss v Protoss mirrors on a map used in pro play
([Catalyst LE](https://liquipedia.net/starcraft2/Catalyst_LE)). It successfully
beat two pro players from TeamLiquid, TLO (a Zerg player) and MaNa (a Protoss player).

This made waves in both the Starcraft community and ML community. I fall
*mostly* in the ML community, since I've barely played Starcraft II and it's
been ages since I've played Brood War. However, as someone who's lightly
followed Brood War and early SC2 pro play, I can provide some commentary about
what this means for machine learning, with some Starcraft context added where
it's appropriate.

In other words, if you're interested about what AlphaStar means for Starcraft,
you may want to read something else. I recommend [the analysis video by Artosis](https://www.youtube.com/watch?v=_YWmU-E2WFc)
and [the commentary MaNa did over his own games](https://www.youtube.com/watch?v=zgIFoepzhIo).

The [DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
for AlphaStar is pretty extensive, and although I will cover some of what's
discussed there, I will not cover all of it, this is more of a companion piece.

ADD THE MANA STORY THAT WAS ACTUALLY PRETTY FUNNY



The Initial Impact
-------------------------------------------

It was never a secret that DeepMind was working on Starcraft II. One of the first
things mentioned after the Lee Sedol vs AlphaGo match was that DeepMind was
planning to look at Starcraft. They've given talks at Blizzcon, helped develop
the SC2 learning environment, and published a few papers about training agents
in Starcraft II minigames. It was always a matter of time.

For this reason, it hasn't made as big an impact on me as AlphaGo or OpenAI's
initial DotA 2 work. The key difference isn't the impressiveness of the result,
it was that for both those works, no one knew DeepMind or Open AI was even
looking at these games until they were officially announced.

(Okay, yes, there were signs that AlphaGo was on the horizon about a year before
it actually happened, but personally, it wasn't clear to me that DeepMind cared
about Go enough to push the results with sufficient gusto.)

Starcraft 2 has had a steady stream of progress reports, and that's lessened the
shock of the initial impact. When you know a team has been working on Starcraft
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

I told them that given that DeepMind was working on Starcraft 2, if they beat a
pro player within a year, I'd have to seriously revise my assumptions on the
pace of ML progress. I thought it would take more like five years, maybe ten.

The first win in the AlphaGo vs Lee Sedol match was on March 9, 2016, meaning it
took DeepMind just shy of three years to do the same in Starcraft.

I'll have to think about whether that means I'm undercalibrated. The tricky part
here is that the last time I took a questionnaire about AI predictions, it only
asked about moonshot AI projects, and accordingly almost all of my guesses were
at least 10 years in the future. Given that I took this questionnaire two years
ago, I've yet to have any positives, but I won't be able to *observe* any
correct guesses for at least another 8 years. It's all a waiting game.

This is probably why people don't like debating with futurists that refuse to
make short-term predictions. Luckily, I don't deal with people like that very
often.


The Starcraft AI Effect
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

CAPTION
{: .centered }

Yes, I would agree that this is an advantage in favor of AlphaStar. But it's
worth noting that before AlphaStar, it was still an open question whether bots
could beat pro players in the first place, with no restrictions on APM. What, is
the defeat of a pro player in any capacity at all not entertaining enough?

Here is my guess, which could be wildly off: these criticisms are not coming
from the belief that AlphaStar is not impressive. They are coming from the
belief that AlphaStar is not as impressive as it was advertised to be, nor as
impressive as what they believe other people think it is going to be.

The variant of
AlphaStar that beat MaNa does have an advantage in that it is allowed to
perceive the entire map at once, rather than use a camera to get views of
different parts of the map. (The model architecture does use attention layers,
which lets the model base its decision on specific parts of the map, but there
are subtle reasons this different from human play.)

This lets the bot do things that feel superhuman. For example, in one game
(FIND THIS), MaNa tried building Dark Templars, perpetually cloaked units that
are great for harassing, as long as they aren't detected. The moment the DTs
went into AlphaStar's vision, AlphaStar started building Observers.

Now, humans can do this too, but even at the pro level, I'd expect some delay
in spotting the shimmer of a cloaked unit.


On Actions Per Minute
-----------------------------------------------

Starcraft is notorious for its high APM at pro level. I almost said APM
requirement, but this isn't exactly true.

There's a video series by Day 9 about the basics of Starcraft: Brood War,
and although it's not the same as Starcraft 2, SOMETHING SOMETHING. The core
idea is still the same: even at the pro level, people will not micro their units
optimally, because doing so would detract from the macro of actually building
more units. This leads to something people call the economy of attention: given
what APM you can achieve, prioritizing where to concentrate your APM is itself
part of the game.
For example, a player may choose to engage the opponent's main army while doing
a drop on their worker line, to force their opponent to split their attention
across the two fronts. Doing so favors the player with more units, since in the
abscence of any micro, the person with more stuff wins.

You can think of this as matching average pro APM, medium-load pro APM, and burst pro APM.



The averages for this seem reasonable with what the best pros can do, and at the
same time, some of the micro AlphaStar does is incredible. Finetune
control of several groups of Stalkers at once, with almost perfect focus firing
to avoid overkilling units.

I personally have no problems with this. APM isn't everything. I've read a few
comments from people complaining that AlphaStar's APM is all 100% effective,
whereas pro players will make unnecessary clicks that don't do anything. This
is overlooking that AlphaStar is *making good decisions with the APM it has*.
If APM were the only thing that SC2 AIs needed to win, they should have beat pro
players ages ago. When we say "micro", it doesn't just mean controlling units
such that they win the fight, it also includes decisions on whether to engage
and disengage in the first place. Those are the sorts of decisions that i'd
expect bots to have trouble with, because it relies on context and intuition
about the value of different units, positioning, whether your opponents have
reinforcements, and so on.


On Reinforcement Learning and Imitation Learning
-------------------------------------------

Most of the details are still vague right now. More have been promised in a
peer-reviewed journal article, but here are my impressions for what's out right
now.

First off, the pure imitation learning baseline did better than I expected.
I expected the longer time horizons to be a problem for imitation learning from
human games, because I didn't think the dataset of human games was big enough to
learn useful game-wide behaviors. However, it seems like this wasn't an issue.
In retrospect, I shouldn't have been surprised, given that the baseline
supervised learning version of AlphaGo can be thought of as an imitation
learning baseline.

This seems very important for initial bootstrapping. It's true that with further
improvements, AlphaZero was able to surpass AlphaGo without using human
bootstrapping, but I assume getting this to work is harder than starting from a
reasonable baseline. This is something we observed in the robot grasping
project, learning is sped up a lot if your initial data is doing
somewhat-reasonable things.

Secondly, my suspicion is that population based training is the key to making
the whole learning system work. I haven't tried population based training
myself, but from what I heard, it tends to give more gains in unstable learning
settings. I would expect Starcraft to be one of those settings, because the
nature of the game is that some build orders counter other build orders, which
could lead to unstable equilibria if the population of agents isn't wide enough.

To put it another way, I believe the best Starcraft 2 strategy is more easily
representable by an ensemble of agents picking somewhat different strategies,
rather than a single agent that's trying to represent the Nash equilibrium by
itself.


On Training Time and Training Resources
----------------------------------------------------

REWORD

My notes from the match state that the imitation learning is trained for about 3
days, and the population-based training is then traiend for another 14 days.

Each agent is trained using 16 TPUs, which is estimated to be about the same as
50 GPUs. But it's worth noting this then gets multiplied by the number of agents
in the population.




On New Stratgies
---------------------------------------------------

Massing probes. Maybe a good strategy, maybe not? Still up in the air.


the game

apologies if i've missed something, but here's my understanding of how that
version of the agent worked.

* the game state of starcraft 2 is fed through an api. although the agent does
  not work directly from raw pixels, it does have some visual input - the
  regions of the minimap currently in vision of any units the agent has
  produced.
(do later).

at some level, the agent is able to observe everything within its vision. now,
in practice, the agent includes an attention layer that causes it to focus on
specific parts of the game state when deciding what actions to execute. in some
view, this is similar to how a human would play the game, but it's not exactly
the same.

the agent also comes with some limits on its APM. The average APM of the bot is
limited to that of a pro player, except with some allowances for much higher
burst APM, to model how pros handle especially micro-intensive fights.

Some people felt that AlphaStar was still using 




This has made some waves.

Notes
* The APM limits, is superhuman micro a big deal or not
* The economy of attention, link to Day-9 video, forcing high APM situations
* Cover macro vs micro and why good micro is hard,
** Microing assuming you continue the engagement is a mechanical thing computers
could be good at, but when you add in whether to engage or not, it gets much
harder
** "Learning to harass"
* Pretty good to really good is a smaller step than getting something pretty
  good in the first place.
* Citation of Observer getting built as soon as Dark Templars enter vision.
** Artosis commentary over games?
* Macro decisions of constant probe building (vs stopping probes to save up
  minerals for Nexus)
* Viewing whole map at once vs requiring camera movements
* Bring up older Starcraft AIs?
* 5-10 year prediction broken and discussion on that.


Notes from the match:

* Match 5 against TLO: proxy 4 gate vs proxy 4 gate
not using
* The top five agents from population based training are picked, where top 5
defined as least exploitable.
* Match against MaNa was against version of the agent wiht more trianing time
done
* Claim 350 ms reaction time (but check AMA I believe the numbers quoted there
  are different in some way)
* Averaged 310 APM in TLO match and APM = EPM
* worker over-saturation strats, transfer to natural when it finishes, the
  differnece is that it does not stop worker production after the main is
  saturated to save up money for the nat, it just keeps building
** Theory is that this defends against harass by building redundancy
** adopted by Mana as an expeirment
* Protoss mirror on 1 map
** although results on another map were not as bad as they expected.
* camera limitation rather than full map?
* peak of 900 APM visible, claims peaks of 1500 APM
done
* when estimating screens/min (from times attention changes?), does about 30
  screens per min (average 2 seconds per screen, seems reasonable)
* explicit camera moving agent was of only slightly worse / comparable strength
  according to their internal ELO estimates but ende dup playing worse due to
  weird collapse from MaNa's harassment patterns (or something)
* Agent architecture is 3 LSTMs, one for attention on location to look, one for
  outcome prediction, and a 3rd for deciding what to build / upgrade. Check blog
  post it mentions pointer nets / self-attention
* Early game acts with about 200 APM
** Pro players have more but this is because they are practicing keeping their
fingers moving fast to prep for latr parts of the game
* 16 TPUs per agent (estimate equivalent to 50 GPUs)
* Not sure how many agents are in each population, a guess of about 30 leads to
  about 1500 GPUs as equivalent?
* Train time: about 3 days to train the imitation learning baseline to
  bootstrap, then 7 days of "AlphaStar league" (population based training)
* Estimate 200 years of SC2 expeerience
* Is this the train time for the TLO agent or MaNa agent?
