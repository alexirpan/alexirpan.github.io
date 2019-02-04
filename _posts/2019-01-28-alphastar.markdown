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
human plays the game.

Apologies if I've missed something, but here's my understanding of how that
version of the agent worked.

* The game state of Starcraft 2 is fed through an API. Although the agent does
  not work directly from raw pixels, it does have some visual input - the
  regions of the minimap currently in vision of any units the agent has
  produced.
(Do later).

At some level, the agent is able to observe everything within its vision. Now,
in practice, the agent includes an attention layer that causes it to focus on
specific parts of the game state when deciding what actions to execute. In some
view, this is similar to how a human would play the game, but it's not exactly
the same.

(This point is subtle and hard to explain.)

This leads to some behaviors that feel superhuman. For example, in one game
against MaNa, MaNa tried building Dark Templars. These units are perpetually
cloaked, and can't be targeted unless you have a detector unit nearby. However,
if you look closely, there is a noticeable shimmer that appears where a cloaked unit is.

The moment that a cloaked unit appeared in AlphaStar's vision, it immediately
started building an Observer. This is something that a pro could do if they
watched their base entrances closely enough, but I wouldn't expect a human to
notice a DT immediately.

The agent also comes with some limits on its APM. The average APM of the bot is
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
