---
layout: post
title:  "Emergency Post Because OpenAI Just Revealed Their Dota 2 1v1 Bot And I Have Opinions"
date:   2017-08-11 01:56:00 -0700
---

See title!

The International is *the* tournament for Dota 2, and
[OpenAI just demoed
their bot that went undefeated against several pro players in 1v1.](https://blog.openai.com/dota-2/).

Is this awesome? **Yes.**

Does this represent a step forward in what machine learning can do?
**Maybe.** That's where it gets more complicated.

\* \* \*
{: .centered }

Let's start with a broader question: why do machine learning researchers
make game AIs?

I claim they do so for two reasons.

* To prove it's possible for computers to beat humans at the game.
* To use the game as an environment for developing new machine learning
techniques.

Now, there's a healthy intersection between gamers and ML researchers, so
these objectives certainly aren't mutually exclusive.
I bring it up because a number of game AIs are very tailored to the game
they're trying to solve. To judge whether a game AI is impressive or not,
you need to know details behind how it works.

For example, there's [a Pokemon speedrun bot](https://github.com/jonese1234/PokeBotBad)
that tries to complete Pokemon Red as quickly as possible. It's achieved
record times, but it didn't learn how to do it. Rather, a human designed a
flowchart of what the bot should do, and it follows it until it achieves
success.

Similarly, a while back there was some buzz about
[a computer that beat an expert fighter pilot at an aerial combat simulator.](http://magazine.uc.edu/editors_picks/recent_features/alpha.html)
It rather predictably spawned many alarmist headlines.
Read the [details](https://www.omicsgroup.org/journals/genetic-fuzzy-based-artificial-intelligence-for-unmanned-combat-aerialvehicle-control-in-simulated-air-combat-missions-2167-0374-1000144.pdf),
however, and you find it's mostly a rule-based AI (if this then that),
learned through genetic algorithms, with some expert knowledge added to the
training process. Still cool, but a lot of domain specific knowledge went
into the problem.

Neither of these are super impressive from the standpoint of seeing what
machine learning is capable of, because they both rely on a human
providing specific domain knowledge.

In contrast, AlphaGo was impressive because it both solved a new game,
and did so by combining supervised pretraining + reinforcement
learning + Monte Carlo Tree Search in a way that hadn't been done before.
Generally, the best games for research are ones where developing new
techniques is *necessary* to achieve superhuman performance, and Go was
an example of this.

Now, DeepMind cares about StarCraft, because real-time is hard, partial
information is hard, the wide variety of units means you have lots to learn,
and most importantly the long-term strategy and planning is something that
RL systems tend to lack.

Dota 2 fills a similar niche - also real-time, also partial information,
also has tons of heroes, and also requires long-term planning to play well.
With current approaches, we can't solve StarCraft, and we can't solve Dota 2.
We need new ideas to teach computers to play these games at a competent
level.

That's why people care.

\* \* \*
{: .centered }

So far, OpenAI has not released many details behind the bot.
Speculating on what the bot means for the field would be *massively*
irresponsible, until more info comes out to provide context.

That being said...speculating how the bot might work is also **massively**
fun. So let's get into it!

First of all, the bot most likely only know how to play 1v1, Shadow Fiend
vs Shadow Fiend. Rule of thumb: for demos and for papers, assume that if something
isn't mentioned or shown, it isn't proven to work yet.
This is not a strike against the work! There's no reason to make the problem
more difficult if you aren't even sure the problem is solvable.

Next, from the header:

> The bot learned the game from scratch by self-play, and does not use imitation learning or tree search.

So most likely, it's reinforcement learning. Restricting the game
to only 1v1 Shadow Fiend gives you a ton of nice things.

* The model only needs to understand how a single character in the game works.
* The same policy can be used for both players.

In many ways, this reminds me of the [Super Smash Brothers Melee bot](https://github.com/vladfi1/phillip)
that beat several pro players - it can beat pros, but only if both players
are Captain Falcon, and only if the players are P1 and P2, and only if they
play on Battlefield. Cool? Yes. Limited? Also yes.

The existence of that SSBM bot makes me suspect there weren't many breakthroughs behind
this bot, just some grunt work on getting the system together and getting
an off-the-shelf RL algorithm to train. I don't play Dota (used to play
League), but from what I've heard 1v1 laning is much more about character
micro. I can see RL learning to deal with that - it's the macro level play
that I expect to be hard.

Assuming it's an RL approach, there are several follow-up questions.

* How is game state getting represented?
* How are game actions getting represented?
* How often does the AI output actions?
* How is reward defined?
* What reinforcement learning algorithm is used?
* How long does it take to train?

The impressiveness of the achievement depends on the answer to these
questions. Once again, we don't know details yet. But I'm going
to throw out some guesses. Hopefully they aren't completely wrong, I'll update
when more information comes out.

* **State representation:** I assume OpenAI is collaborating with Valve
on this. [Valve has an official Dota 2 API](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Scripting/API),
and I assume they're using it, because why wouldn't you? I mean, you could
try to learn from raw pixels, but that would be ridiculously impressive,
almost too much so. It's much more plausible that it's getting exact positions
and health of all units within its vision, which certainly helps on the micro
front. Human players have all that info too, but humans don't have the attentional
bandwidth to know everything down to the precision that an API could give you.

* **Action representation:** I would guess raw (x, y) locations for mouse clicks,
the skill hotkeys, and special actions for clicking on units. In theory
you only need mouse clicks, but if you're already getting information from
the game API, you might as well use the API for targeting functionality too.
That way your model doesn't have to how to learn how to click on units, it
can focus on learning when clicking units is good and when clicking units is bad.

* **Action frequency:** No idea. They say that their APM is
comparable to an average human player, which gives some indication of how often
the network can send commands. I'm mostly curious on whether there are limits on
APM, or if the neural net is slow enough to give human-level APM automatically.

This is one way real time problems can be more difficult - in the latency
between polling for an action, computing an action, and sending it back to the
game, the environment could be in a very different state. On the other hand,
humans have the same problem - we have to process the game visuals, decide
on an action, then send the command to our hands. Clearly we can deal with it
fine, so maybe I'm overestimating how important this is.

Aside: in StarCraft, you can make much better usage of APM because you have
an entire army to command. Let a StarCraft bot do thousands of actions per minute
and you can get ridiculous things like [this](https://www.youtube.com/watch?v=0BS8Mbqbnmk).
In Dota 2, because there's just one controllable character, there's a cap on
how much APM can improve your gameplay. This is mentioned in the blog post too,
but I want to emphasize it. Whenever people post StarCraft bots, people
invariable say they'll wait for human level APM. In Dota 2's case, I think
it actually won't matter that much - what matters is precision of movement
and knowledge of health bars down to a single hit point. That's where
computers have the advantage.

* **Reward definition:** Here's where I get *really* curious. I assume the reward
isn't just "1 if you win, -1 if you lose." If it is, that would be *insane*.
I mean, it's not of the question - I think that barely kisses the realm of
possibility. But I'd expect that the reward is shaped, giving partial reward
based on EXP, gold, or health. (In RL, we say a reward is shaped if it gives
small reward for doing things you expect to be useful. Reward shaping is one
of the big ways to add domain knowledge to your problem.)

Generally, shaped rewards are easier to learn from than the pure "win/loss"
signal, but only if the shaping is done well, and tuning the reward
can be a huge pain. I'd actually rather have it be the win/loss reward, because
if it was, it would be even cooler that the bot can learn so many complex
behaviors from purely win/loss.

It could even be using the system from the [Learning from Human Preferences](https://blog.openai.com/deep-reinforcement-learning-from-human-preferences/)
paper - I could see it being useful for given partial signal to behaviors
that are hard to define.

* **Learning algorithm:** Probably [PPO](https://blog.openai.com/openai-baselines-ppo/).
It works well, and it supports continuous control, which may be good for
mouse movement.

* **Training time:** "Two weeks real time", except that says basically
nothing for how many machines they used, whether they were able to run the
game faster than real time, etc. For context, DeepMind says they got up
to 2000 frames per second in a single thread for [their StarCraft API](https://deepmind.com/blog/deepmind-and-blizzard-open-starcraft-ii-ai-research-environment/).
Let's just say it took "a while" and leave it at that.
