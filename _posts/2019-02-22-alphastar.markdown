---
layout: post
title:  "An Overdue Post on AlphaStar, Part 1"
date:   2019-02-22 01:52:00 -0800
---


In late January, DeepMind broadcasted a demonstration of their StarCraft II agent
AlphaStar. In Protoss v Protoss mirrors on a map used in pro play
([Catalyst LE](https://liquipedia.net/starcraft2/Catalyst_LE)), it successfully
beat two pro players from TeamLiquid, TLO (a Zerg player) and MaNa (a Protoss player).

This made waves in both the StarCraft and machine learning communities. I'm
mostly an ML person, but I played a lot of casual Brood War growing up and used
to follow the Brood War and SC2 pro scene.

As such, this is a two-part post. The first is a high-level overview of my
reactions to the AlphaStar match and other people's reactions to the match.
The second part, linked
[here]({% post_url 2019-02-22-alphastar-part2 %}), is a more detailed
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
planning to look at StarCraft. They've given talks at BlizzCon, helped develop
the [SC2 learning environment](https://deepmind.com/blog/deepmind-and-blizzard-open-starcraft-ii-ai-research-environment/), and published a few papers about training agents
in StarCraft II minigames. It was always a matter of time.

For this reason, it hasn't made as big an impact on me as OpenAI's
1v1 DotA 2 bot.
The key difference isn't how impressive the results were, it was how surprising
it was to hear about them. No one OpenAI was
looking at DotA 2, until they announced they had beaten a top player in 1v1
(with conditions).
Even for AlphaGo, DeepMind published a paper on Go evaluation
over a year before the AlphaGo Nature paper ([Maddison et al, ICLR 2015](https://arxiv.org/abs/1412.6564)).
It was on the horizon if you saw the right signs (see [my post on AlphaGo]({% post_url 2016-01-27-deepmind-go %}) if curious).

StarCraft II has had a steady stream of progress reports, and that's lessened the
shock of the initial impact. When you know a team has been working on StarCraft
for several years, and [Demis Hassabis tweets](https://twitter.com/demishassabis/status/1087774153975959552)
that the SC2 demonstration will be worth watching...well, it's hard not to expect *something* to happen.

In his post-match livestream, MaNa relayed a story about his DeepMind visit.
In retrospect, given how many hints there were, it's funny to hear how far they went to conceal how strong
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

To be fair, the question was never about whether DeepMind had positive results. It was
about how strong their results were. On that front, they successfully hid their
progress, and I was surprised at how strong the agent was.


How Did AlphaStar Win?
---------------------------------------------------

Here is an incredibly oversimplified explanation of StarCraft II.

* Each player starts with some workers and a home base. Workers can collect
  resources, and the home base can spend resources to build more workers.
* Workers can spend resources to build other buildings that produce stronger units, upgrade
  your existing units, or provide static defenses.
* The goal is to destroy all your opponent's buildings.

Within this is a large pool of potential strategy. For example, one thing
workers can do is build new bases. This is called expanding, and it gives you
more economy long run, but the earlier you expand, the more open you are to
aggression.

AlphaStar's style, so to speak, seems to trend in these directions.

* Never stop building workers, even when it delays building your first
  expansion.
* Build lots of Stalkers and micro them to flank and harass the enemy army until
  it's weak enough to lose to an all-in engagement. Stalkers are one of the first
  units you can build, and can hit both ground and air units from range. They
  also have a Blink ability that lets them quickly jump in and out of battle.
* Support those Stalkers with a few other units.

From the minimal research I've done, none of these strategies are entirely new,
but AlphaStar pushed the limits of these strategies to new places. Players have massed
workers in the past, but they'll often stop before hitting peak mining capacity,
due to [marginal returns on workers](https://liquipedia.net/starcraft2/Mining_Minerals#Optimizing_Mineral_Harvesting). Building workers all the way to the mining cap delays your first expansion, but it also provides redundancy against worker harass, so
it's not an unreasonable strategy.

Similarly, Stalkers have always been a core Protoss unit, but they eventually get
countered by Immortals. AlphaStar seems to play around this counter
by using exceptional Stalker micro to force early wins through a [timing push](https://liquipedia.net/starcraft2/Timing_Attack).

It's a bit early to tell whether humans should be copying these strategies.
The heavy Stalker build may only be viable with superhuman micro
(more on this later). Still, it's exciting that it's debatable in the first place.

Below is a diagram from the blog post, visualizing the number of each unit the
learned agents create as a function of training time. We see that Stalkers and
Zealots dominate the curve. This isn't surprising, since Stalkers and Zealots
are the first attacking units you can build, and even if you're planning to use
other units, you still need some Stalkers or Zealots for defense.

![Unit histograms](/public/alphastar/units.png)
{: .centered }

I believe this is the first StarCraft II agent that learns unit compositions.
The previous leading agent was one [developed by Tencent (Sun et al, 2018)](https://arxiv.org/pdf/1809.07193.pdf),
which followed human-designed unit compositions.


The StarCraft AI Effect
-------------------------------------------

One of the running themes in machine learning is that [whenever somebody gets an AI to do something new, others immediately find a reason to say it's not a big deal](https://en.wikipedia.org/wiki/AI_effect).
This is done either by claiming that the task solved doesn't require
intelligence, or by homing in on some inhuman aspect of how the AI works. For
example, the first chess AIs won thanks to large game tree searches and lots of
human-provided knowledge. So you can discount chess AIs by claiming that large
tree searches don't count as intelligence.

The same thing has happened with AlphaStar.
Thanks to the wonders of livestreaming and Reddit, I was able to see this live,
and boy was that a sight to behold. It reminded me of the routine
["Everything is Amazing, and Nobody's Happy"](https://www.youtube.com/watch?v=kBLkX2VaQs4).
(I understand that Louis C.K. has [a lot of baggage these days](https://en.wikipedia.org/wiki/Louis_C.K.#2017%E2%80%93present:_Sexual_misconduct_revelations_and_afterwards), but I haven't found
another clip that expresses the right sentiment, so I'm using it anyways.)

I do think some of the criticisms are fair. The criticisms revolved around two points: the global camera, and AlphaStar's
APM.

I'm deferring details of AlphaStar's architecture to
[part 2]({% post_url 2019-02-22-alphastar-part2 %}), but the short version is
that AlphaStar is allowed to observe everything within vision of units it
controls. By contrast, humans can only observe the minimap and the units on
their screen, and must move the camera around to see other things.

There's one match where MaNa tried building Dark Templars, and the instant they
walked into AlphaStar's range, it immediately started building Observers to
counter them. A human wouldn't be able to react to Dark Templars that quickly.
This is further complicated by AlphaStar receiving raw game state instead of the visual
render. Getting raw game state likely makes it easier
to precisely focus-fire units without overkill, and also heavily nerfs cloak
in general. The way cloaking works in StarCraft is that cloaked units are
untargetable, but you can spot faint shimmers wherever there's a cloaked unit.
With proper vigilance, you can spot cloaked units, but it's easy to miss them
with everything else you need to focus on.
AlphaStar doesn't have to spot the on-screen shimmer of cloak, since the raw
game state simply says "Dark Templar, cloaked, at position (x,y)."

The raw game state seems like an almost unfixable problem (unless you want to go
down the computer vision rabbit hole), but it's not that bad compared to the
global camera. For what it's worth, DeepMind trained a new agent without the
global camera for the final showmatch, and I assume the global camera will not
be used in any future pro matches.

The more significant controversy is around AlphaStar's APM. On average,
AlphaStar acts at 280 actions per minute, less than pro play, but this isn't the
full picture.
According to the [Reddit AMA](https://www.reddit.com/r/MachineLearning/comments/ajgzoc/we_are_oriol_vinyals_and_david_silver_from/eexs0pd/), the limitation is at most 600 APM every 5 seconds,
400 APM every 15 seconds, and 300 APM every 60 seconds. This was done to model
both average pro APM and burst APM, since humans can often reach high peak APM
in micro-intensive situations. During the match itself, viewers spotted that
AlphaStar's burst APM sometimes reached 900 or even 1500 APM, far above what
we've seen from any human.

These stats are backed up by the APM chart:
AlphaStar's average APM is smaller than MaNa's, but has a longer tail.

![APM Chart](/public/alphastar/apm.png)
{: .centered }

[From DeepMind blog post](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/)
{: .centered }

Note that TLO's APM numbers are inflated because the [key bindings he uses](https://www.reddit.com/r/starcraft/comments/4pnbv8/tlo_sometimes_has_12001600_apm/) leads to lots of phantom actions
that don't do anything. MaNa's numbers are more reflective of pro human APM,

I mentioned earlier that AlphaStar really likes Stalkers. At times, it felt like
AlphaStar was building Stalkers in pure defiance of common sense, and it worked
anyways because it had such effective blink micro. This was most on display in
game 4, where AlphaStar used Stalkers to whittle down MaNa's Immortals,
eventually destroying all of them in a game-ending victory. (Starts at 1:37:46.)

<p class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/cUTMhmVh1qs?start=5866" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

I saw a bunch of people complaining about the superhuman micro of AlphaStar, and
how it wasn't fair. And yes, it isn't.
But it's
worth noting that before AlphaStar, it was still an open question whether bots
could beat pro players at all, with no restrictions on APM. What, is
the defeat of a pro player in any capacity at all not cool enough? Did Stalker
blink micro stop being fun to watch? *Are you not entertained?*
Why is this such a big deal?


What's Up With APM?
-----------------------------------------------------------------

After thinking about the question, I have a few theories for why people care
about APM so much.

**First**, StarCraft is notorious for its high APM at the professional level.
This started back in Brood War, where people shared absurd demonstrations of how
fast Korean pro players were with their execution.

<p class="centered">
<iframe width="560" height="315" src="https://www.youtube.com/embed/YbpCLqryN-Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

It's accepted wisdom that if you're a StarCraft pro, you have to have high APM.
This is to the point where many outsiders are scared by StarCraft because they
think you have to have high APM to have any fun playing StarCraft at all.
Without the APM to make your units do what you want them to do, you won't have
time to think about any of the strategy that makes StarCraft interesting.

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

This execution difficulty is an important human element of gameplay. You can only go so fast, and
can't do everything at once, so you have to choose where to focus your efforts.

But a computer *can* do everything at once. I assume a lot of pros would find
it unsatisfying if supreme micro was the only way computers could compete with
pros at StarCraft.

**Second**, micro is *the* flashiest and most visible StarCraft skill.
Any StarCraft highlight reel will have a moment where one
player's ridiculous micro lets them barely win a fight they should have lost.
For many people, micro is what makes StarCraft a good competitive game,
because it's a way for the better player to leverage their skill to win. And
from a spectator perspective, these micro fights are the most exciting parts of
the game.

The fact that micro is so obvious matters for the **third** and final theory:
DeepMind started by saying their agent acted within human parameters for APM,
and then broke the implicit contract.

Everything DeepMind said was true. AlphaStar's average APM is under pro average
APM. They did consult with pros to decide what APM limits to use. When this is
all mentioned to the viewer, it comes with a bunch of implications. Among them
is the assumption that the fight will be fair, and that AlphaStar will not do
things that humans can't do. AlphaStar will
play in ways that look like a very good pro.

Then, AlphaStar does something superhuman with its micro. Now, the fact that
this is within APM limits that pros thought were reasonable doesn't matter.
What matters is that the implied contract was broken, and that's where people
got mad. And because micro is so
obvious to the viewer, it's very easy to see *why* people were mad.
I claim that if AlphaStar had used
thousands of APM at all times, people wouldn't have been upset, because DeepMind
never would have claimed AlphaStar's APM was within human limits, and everyone
would have accepted AlphaStar's behavior as the way things were.

We saw a similar thing play out in the OpenAI Five showcase. The DotA team said
that OpenAI Five had 250ms reaction times, within human limits. One of the humans
picked Axe, aiming for Blink-Call engages. OpenAI Five would insta-Hex Axe every
time they blinked into range, completely negating that strategy.
We would never expect humans to do this consistently, and questions about reaction time
were among the first questions asked in the Q&A section.

I feel people are missing the wider picture: **we can now train ML models that
can play StarCraft II at Grandmaster level.** It is entirely natural to ask for
more restrictions, now that we've seen what AlphaStar can do, but I'd ask people
not to look down on what AlphaStar has already done. StarCraft II is a hard
enough problem that any success should be celebrated, even if the end goal is to
build an agent more human-like in its behavior.

APM does matter. Assuming all other skills are equal,
the player with higher APM is going to win, because they can execute things with
more speed and precision. But APM is nothing without a strategy behind it.
This should be obvious if you look at existing StarCraft bots,
that use thousands of APM and yet are nowhere near pro level. Turns out
learning StarCraft strategy is hard!

If anything, I find it very impressive that AlphaStar is actually *making good decisions with
the APM it has*. "Micro" involves a lot of rapid, small-scale decisions about
whether to engage or disengage, based off context about what units are around,
who has the better position and composition, and guesses on where the rest of
your opponent's army is. It's *hard*.

For this reason, I didn't find AlphaStar's micro that upsetting. The
understanding displayed of when to advance and when to retreat was impressive
enough to me, and watching
AlphaStar micro three groups of Stalkers to simultaneously
do hit-and-runs on MaNa's army was incredibly entertaining.

At the same time, I could see it getting old. When fighting micro of that caliber,
it's hard to see how MaNa has a chance.

Still, it seems like an easy fix: tighten some of the APM bounds, maybe include
limitations at smaller granularity (say 1 second) to limit burst APM, and see
what happens. If Stalker micro really is a crutch that prevents it
from learning stronger strategies, tighter limits should force AlphaStar to
learn something new. (And if AlphaStar doesn't have to do this, then that would
be good to know too.)


What's Next?
------------------------------------------------------------------------

DeepMind is free to do what they want with AlphaStar. I suspect they'll try to
address the concerns people have brought up, and won't stop until they've
removed any doubt over ML's ability to beat pro StarCraft II players with
reasonable conditions.

There are times where people in game communities worry that big companies are
building game AIs purely as a PR stunt, and that they don't appreciate the
beauty in competitive play. I've found this is almost always false, and the same
is true here.

Let me put it this
way: one of the faces of the project is Oriol Vinyals. Based on a [35 Under 35](https://www.technologyreview.com/lists/innovators-under-35/2016/pioneer/oriol-vinyals/) segment
in the MIT Technology Review, Oriol used to be the best Brood War player in
Spain. Then, he worked on a StarCraft AI at UC Berkeley. Eventually, he joined
DeepMind and started working on AlphaStar.

So yeah, I don't think the AlphaStar team is looking at StarCraft as just another game to
conquer. I think they genuinely love the game and won't stop until AlphaStar is
both better than everyone and able to teach us something new about StarCraft II.

[Continue to Part 2]({% post_url 2019-02-22-alphastar-part2 %})
{: .centered }
