---
layout: post
title:  "Emergency Post Because OpenAI Just Revealed Their Dota 2 1v1 Bot And I Have Opinions"
date:   2017-08-11 01:56:00 -0700
---

See title!

The International is *the* tournament for Dota 2, and OpenAI just demoed
their bot that went undefeated against several pro players in 1v1.

Is this awesome? **Yes.**

Does this represent a step forward in what machine learning can do?
**Maybe.** That's where it gets more complicated.

\* \* \*
{: .centered }

Let's start with a broader question: why do machine learning researchers
make game AIs? They do so for two reasons.

* To prove it's possible for computers to beat humans at the game.
* To use the game as an environment for developing new machine learning
techniques.

I bring this up because a number of game AIs are very tailored to the game
they're trying to solve. For example, a while back there was some buzz about
a computer that beat an expert fighter pilot at an airplane fighting simulator.
Read the details, however, and you find the AI was using around 120 hand-tuned
rules. Similarly, there's a Pokemon speedrun bot that attempts to complete
Pokemon Red as quickly as possible. This bot learns nothing, and also follows
a human-defined flowchart. Neither of these are particularly impressive from
the standpoint of seeing what machine learning is capable of, because they
all use very specific domain knowledge.

Generally, the best games for research are ones where developing new
techniques is *necessary* to achieve superhuman performance. For DeepMind,
this used to be Go, until they threw convolutional neural nets and
Monte Carlo Tree Search together and showed it was enough to solve the game.

So far, OpenAI has not released any additional details behind the bot.
Because of this, we don't know how much domain knowledge the bot is given,
and speculating what this means for the field is *massively* irresponsible.

That being said...speculating how the bot might work is also **massively**
fun. So let's get into it!

(Aside: I have never played Dota 2, I used to play League, and I watched
TI4 and TI5.)

\* \* \*
{: .centered }

First, let's observe some limitations. The bot most likely only works
for 1v1, and only if both players are Shadow Fiend. Rule of thumb: when it
comes to research videos, assume that if something isn't demonstrated, it
isn't possible.

This is not a strike against the bot! There's no reason to make the problem
more difficult if you aren't even sure the problem is solvable. It's more
that I want to point out that this isn't a general 1v1 bot. (In many
ways, it reminds me of the SSBM bot that beat several pro players - except
only if both players were Captain Falcon and only on Battlefield.)



The header for the blog post states that

> The bot learned the game from scratch by self-play, and does not use imitation learning or tree search.

So most likely, it's reinforcement learning. Now, restricting the game
to only 1v1 Shadow Fiend gives you a ton of nice things.

* The model only needs to understand how a single character in the game works.
* The same policy can be used for both players. I'm assuming you can rotate
the screen to make the input the same whether you're Radiant or Dire.

Assuming it's an RL approach, there are several questions.

* How is game state getting represented?
* How are game actions getting represented?
* How often does the AI output actions? (Outputting faster gives more
fine-grained control, but makes learning more difficult.)
* How is reward defined?
* What reinforcement learning algorithm is used?
* How long does it take to train?

The impressiveness of the acheivement depends on the answer to these
questions, and once again, we don't know because details aren't out yet.

But, if I had to guess, I would say that it's most likely an off-the-shelf
RL algorithm, plus a lot of engineering work to set up the environment,
and that you probably don't need a lot of big RL advances to do well at
the 1v1 problem. It was risky to work on it, but not unreasonably so.

* **State representation:** The blog post says that it's done in collaboration with
Valve, the creators of the game. It looks like [Valve has an official
Dota 2 API](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Scripting/API).
So they're probably getting exact unit positions, health, and so on from the
API, instead of learning from raw pixel input. I mean, why wouldn't you?
If the bot gets that performance from raw pixels, I'd be very surprised.

Assuming it does get exact health and position, that could explain why it's so
much better at micro than human players.

* **Action repsentation:** I would guess that it's probably positions for mouse
clicks, the skill hotkeys, and special actions for clicking on units in
vision. That way your model doesn't have to how to learn how to click on units,
and can focus on learning when clicking on units is good.

* **Action frequency:** I actually have no idea. They say that their APM is
comparable to an average human player, which gives some indication of how often
the network can send commands. Either there's a lower limit on how often the
network is polled for commands, or the network outputs commands as quickly as it
can.

On one hand, real time problems are harder for RL because of the latency between
the environment asking for an action, the model computing one, and the model
sending it back. On the other hand, humans have to go through the same trouble,
and clearly we can deal with it fine.

* **Reward definition:** Here's where I get *really* curious. I assume the reward
isn't just "1 if you win, -1 if you lose." If it is, that would be *insane*.
I mean, it's not of the question - to me it just barely kisses the realm of
possibility. But I'd expect that the network gets partial reward for damaging
the opponent, getting more gold, and not taking damage, at minimum. In RL, we
say an environment has shaped reward if it gives partial reward for doing things
you expect to be useful.

Generally, shaped rewards are easier to learn from, because even if you don't
win the game, you can learn to make partial progress towards winning. The
problem with shaped reward is that tuning it properly can be a huge pain.

Maybe it's even using the system from the Learning from Human Preferences paper
in some way - I could see that being useful for rewarding things that are
hard to define.

* **Learning algorithm:** Probably PPO. Two reasons:

1. Accroding to the PPO blog post, it's the default RL algorithm at OpenAI.
2. PPO handles continuous control, which may be a better fit for mouse
position than discrete actions.

I don't think you need anything else to solve the 1v1 problem. For 5v5 you'd
have to look into multiagent systems, and that's a whole new set of problems.

* **Training time:** We don't know. I've heard "two weeks real time",
but that doesn't really say much at all. Note that DeepMind's Starcraft 2
API hits 2000 frames per second, and it could be using tons of machines
too.
