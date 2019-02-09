---
layout: post
title:  "Title TBD"
date:   2019-01-28 01:41:00 -0800
---

(N) days ago, DeepMind broadcasted a demonstration of their Starcraft 2 agent
AlphaStar. It successfully beat two pro players from TeamLiquid, TLO (a Zerg
player) and MaNa (a Protoss player). There are several analysis videos and thinkpieces
about what this means, both from the Starcraft side and machine learning side.
Here's my loosely organized take on things.


The Role of Surprise
-------------------------------------------

It was never a secret that DeepMind was working on Starcraft 2. One of the first
things mentioned after the Lee Sedol AlphaGo series was that they were looking
at Starcraft 2. Furthermore, they've given talks at Blizzcon and helped develop
a Starcraft 2 learning API. It was always a matter of time.

This is why I feel it hasn't made as big an impact on me as AlphaGo or OpenAI
Five. Yes, there were signs that AlphaGo was on the horizon about a year before
it actually happened, but we didn't know DeepMind was working on it until they
announced it had beat Fan Hui. Similarly, we didn't OpenAI was working on DotA 2
until they did. For Starcraft 2, there's been a slow stream of progress reports
that suggested something like this was happening, and therefore I felt less
shock from the initial impact.

However, I am a bit surprised at how fast they got an agent on par with top
players. A few months after the AlphaGo match, I got into a conversation with
someone about AGI timelines. (Because, of course, whenever ML does something
new, people start asking about AGI.) They thought it was close and I thought it
wasn't, and as an exercise they asked what would change my mind.

I told them that given that DeepMind was working on Starcraft 2, if they beat a
pro player within a year, I'd have to seriously revise my assumptions on the
pace of ML progress. I thought it would take more like five years, maybe ten.

DeepMind did it in about two and a half years.

It's something that I'll have to think about more. On one hand, this is not the
first time AI's been shown to solve something I thought it couldn't solve yet.
On the other hand, I made most of my AI predictions about two years ago, and
they were all at least 5 years out. The fact that some of these predictions were
wrong two years out doesn't actually mean anything, because I won't know which
predictions were right until another five years have passed. It's all a waiting
game.


On Moving the Goalposts
-------------------------------------------

The way AlphaStar played its games against TLO and MaNa is not the way that a
human plays the game. Some people are upset by this.

I'm reminded of the routine "Everything's Great, and Nobody's Happy". In the
past, it was still an open question whether bots could beat pro players at all,
with no restrictions on APM or perception of the game state. The variant of
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
more units.

This leads to what's known as the economy of attention: given what APM you can
achieve, how do you prioritize where to concentrate your APM on?

As an aside, this is why players in Starcraft will often attack on several
fronts at once - doing so deliberately overloads the attention of the opponent
and stretches out what they can manage.

Now, this being said, 

Alright, so let's bring this back to AlphaStar. The current implementation does
include APM limits, defined in three stages. GET LIMITS. You can think of this
as matching average pro APM, medium-load pro APM, and burst pro APM.

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

My notes from the match state that the imitation learning is trained for about 3
days, and the population-based training is then traiend for another 7 days. I
wasn't able to track down whether this was the training time for the TLO agent,
or the one for the MaNa agent, since they said the version that beat MaNa was
trained for longer.


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
