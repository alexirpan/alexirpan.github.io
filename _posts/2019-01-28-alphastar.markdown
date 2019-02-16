---
layout: post
title:  "Title TBD"
date:   2019-01-28 01:41:00 -0800
---


In late January, DeepMind broadcasted a demonstration of their Starcraft 2 agent
AlphaStar. It plays Protoss v Protoss mirrors on a map used in pro play
([Catalyst LE](https://liquipedia.net/starcraft2/Catalyst_LE)). It successfully
beat two pro players from TeamLiquid, TLO (a Zerg player) and MaNa (a Protoss player).

This made waves in both the Starcraft community and ML community. I fall
*mostly* in the ML community, but like StarCraft as a game. I've barely played
Starcraft II, but I played a lot of Brood War growing up, and I've
lightly followed Brood War and SC2 pro play,

As such, this is a two-part post. The first is a high-level overview of how I
feel about AlphaStar and the impact it's had on Starcraft, and the second is a
more detailed discussion of what AlphaStar means for machine learning.

In other words, if you're interested in deep dives into AlphaStar's strategy,
you may want to read something else. I recommend [the analysis video by Artosis](https://www.youtube.com/watch?v=_YWmU-E2WFc)
and [the commentary MaNa did over his own games](https://www.youtube.com/watch?v=zgIFoepzhIo).

The [DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
for AlphaStar is pretty extensive, and although I will cover some of what's
discussed there, I will not cover all of it. Please read that first, if you
haven't already.


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

**First**, Starcraft is notorious for its high APM at the professional level.
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

And in fact, this should be *obvious* if you look at existing Starcraft bots,
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
Brood War player in Spain, then worked on a Starcraft AI at UC Berkeley, then
eventually made his way to DeepMind to work on AlphaStar](https://www.technologyreview.com/lists/innovators-under-35/2016/pioneer/oriol-vinyals/).
It's not like StarCraft is just a hill to conquer. People really like the game
as well.


*This is part 2 of my post about AlphaStar, click [here] for part 1. ADD
BACKLINK.*


A Quick Overview of AlphaStar's Training Setup
-----------------------------------------------------------------

Most of the details are vague right now, but more have been promised in an
upcoming journal article. This is based off of what's been revealed so far.

AlphaStar is made of 3 sequence models, likely with some shared weights. Each
sequence model receives the same observations, the raw game state. There are
then three sets of outputs: where to click, what to build/train, and an outcome
predictor.

LINKS?

This model is trained in a two stage process. First, it is trained using
imitation learning on human games provided by Blizzard. My notes from the match
say that it takes 3 days to train the imitation learning baselines.

The models are then further trained using IMPALA and population-based training,
plus some other tricks I'll get to later. This is called
the AlphaStar League. Each agent in the population is trained with 16
TPUv3s, which are estimated to be equivalent to about 50 GPUs each. The
population-based training was run for 14 days. I couldn't find any references
for the size of the population, or how many agents were trained at once.

After 14 days, they computed the
Nash equilibrium of the population, and for the showmatch, selected the top 5
least exploitable agents, using a different one in every game.

All agents were trained in Protoss vs Protoss mirrors on a fixed map, Catalyst
LE.


Takeaways
-------------------------------------------------------

1. Imitation Learning Did Better Than I Thought
=========================================================

I have always assumed that when comparing imitation learning to reinforcement
learning, imitation learning performs better when given fewer samples, but has a
lower ceiling in performance. Additionally, it can have problems dealing with random
perturbations. I'm not sure if there's a formal name for this. I've always
called it the [DAgger](https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf) problem, because that's the paper that everyone cites when
talking about this problem.

Intuitively, the argument goes like this: suppose you train an agent by doing
supervised learning on the actions a human does. This is called *behavior
cloning*, and is a common baseline in the literature. Let's say you train the
model and it has some error bounded by $$\epsilon$$ at each state $$s$$.
Then the worst case bound in performance is much larger than $$\epsilon$$ due to
compounding errors. The learned model deviates from the expert a bit, visits a
state where we have less expert supervision, deviates to a further state where
we have even less supervision, and soon the agent is doing nonsense.

The temporal nature of the problem means that the longer your episode is, the
more likely it is that you enter this negative feedback loop, and therefore, we
expect long-horizon tasks to be harder for imitation learning. A StarCraft game
is long enough that I didn't expect imitation learning to work at all.
And yet, imitation learning was good enough to do reasonable things, reaching
the level of a Gold player.

In the first version of AlphaGo, the agent was bootstrapped by doing behavioral
cloning on human games, and that was able to play competitive games against top
Go engines of the time. But Go is a game with at most 200-250 moves, whereas
StarCraft has thousands of decisions points. I assumed that you
would need a massive dataset of human games to get past this, more than Blizzard
had on hand. Turns out you don't.

My guess is that this is tied into another trend: despite the problems with
behavioral cloning, it's actually a pretty strong baseline. I don't do imitation
learning myself, but that's what I've been hearing. I suspect that's because
many of behavioral cloning's problems can be covered up with better data
collection. Here's the pseudocode for DAgger's resolution to the DAgger problem.

![DAgger code](/public/alphastar/dagger.png)
{: .centered }

Given expert policy $$\pi^*$$ and current policy $$\hat{\pi}_i$$, we iteratively
build a dataset $$\mathcal{D}$$ by collecting data from a mixture of the expert
$$\pi^*$$ and current policy $$\hat{\pi}_i$$. We iteratively alternate training
policies and collecting data, and by always collecting with a mixture of expert
data and on-policy data, we can ensure that our dataset will always cover parts
of state-space that are close enough to our current policy.

But importantly, the final optimization loop is still based on maximizing the
likelihood of actions in your dataset. The only change is on how the data is
generated. So, if you have a very large dataset, from a wide variety of experts
(like a corpus of StarCraft games from anyone who's played the game), then it's
possible that your data already has enough variety to let your agent learn how
to recover from the majority of incorrect decisions it could make.

This is something I've anecdotally noticed in my own work. Adding a small amount
of exploration noise to a handcoded policy at collection time can give you
significant gains at training time.

The fact that imitation learning gives a good baseline seems important for
bootstrapping learning. It's true that AlphaZero was able to avoid this, but the
AlphaGo version with imitation learning bootstrapping was developed first. I
suspect AlphaZero-based techniques are trickier to get working in the first
place.


2. Population Based Training is Worth Keeping an Eye On
================================================================

StarCraft II is inherently a game based around strategies and
counter-strategies. My feeling is that in DoTA 2, a heavy portion of your
strategy is decided in the drafting phase. Certain hero compositions will only
work best for certain styles of play. Because of this, once the draft is done,
each team has an idea of what to expect.

However, Starcraft II starts out completely unobserved. Builds can go from heavy
early aggression to greedy expansions for long-term payoff. It seems more likely
that StarCraft could devolve into unstable equilibria if you try to represent
the space of strategies within a single agent.

Population-based training does a lot to avoid this problem. A simple [self-play
agent "gets stuck", but a population-based approach reaches Grandmaster
level](https://twitter.com/OriolVinyalsML/status/1094670648042012673). One of
the intuitive traps in self-play is that if you only play against the most
recent version of yourself, then you could endlessly walk around a
rock-paper-scissors loop, instead of discovering the trick that beats rock,
paper, *and* scissors.

I haven't tried population based training myself, but from what I heard,
it tends to give more gains in unstable learning settings, and it seems likely that
StarCraft is one of those games with several viable strategies. If you expect
the game's Nash equilibria to turn into an ensemble of strategies, it seems way
easier to maintain an ensemble of agents.


3. Once RL Does Okay, It's Not Too Hard to Make It Great
===============================================================

In general, big RL projects seem to fall into two buckets.

1. They don't work at all.
2. They work and become very good with sufficient compute, which may be very
   large due to diminishing returns.

I haven't seen many in-betweens where things start to work, and then hit a
disappointly low plateau.

One model that would explain this is that algorithmic and training tricks are
all about improving the rate of change for an RL agent. Early on, everything
fails, but with enough tuning, the gradient of improvement starts pointing
upwards enough that the agent can actually learn something. From there, it's not
like the agent forgets how to learn, it's just a question of whether there are
things that are hard to learn or not. This means the gap between blank-slate and
pretty-good is actually much larger than the gap between pretty-good and
pro-level. The first requires finding what makes learning work. The second just
needs more data and training time.

The agent that beat TLO on his offrace was trained for about 7 days. Giving
it another 7 days was enough to beat MaNa on his main race. Sure, double the
compute is a lot of compute, but the first success took almost three years of
research time and the second success took seven days. (On a similar front,
[OpenAI's DoTA 2 agent hit 80% win rate against the model they demoed at The
International, with 10 days of training. Wonder where it's at now...](https://twitter.com/openai/status/1037765547427954688?lang=en).


4. We Should Be Tossing More Techniques Together
=============================================================================

One thing I found surprising about the AlphaStar architecture is how much
*stuff* goes into it.

FILL OUT


Notes from the match:

* although results on another map were not as bad as they expected.
* explicit camera moving agent was of only slightly worse / comparable strength
  according to their internal ELO estimates but ende dup playing worse due to
  weird collapse from MaNa's harassment patterns (or something)
* Agent architecture is 3 LSTMs, one for attention on location to look, one for
  outcome prediction, and a 3rd for deciding what to build / upgrade. Check blog
  post it mentions pointer nets / self-attention
* Estimate 200 years of SC2 expeerience
