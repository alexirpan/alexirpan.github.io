---
layout: post
title:  "I'm Switching Into AI Safety"
date:   2024-07-08 10:15:00 -0700
---

You can read the title. As of last month, I've been winding down my existing robotics projects,
and have switched to the AI safety team within Google DeepMind.

It took me a while to start writing this post, because my feelings on AI safety are complicated and take effort to
work through, but changing jobs is a big enough life update that I *have* to write this post. Such is the life of a blogger.


The Boring Reasons
-------------------------------------------

I've been working on the robotics team for 8 years now, and I just felt like I needed to mix it up.
It was a little unsettling to realize I had quietly become one of the most senior members of the team,
and that I had been in robotics longer than my manager, and my manager before that, and the one before *that*.
Really, this is something I thought about doing three years ago, but then my puzzlehunt team won MIT Mystery Hunt,
meaning we had to write next year's Mystery Hunt. Writing that hunt took up all of my 2022, and recovering from it took up much of my 2023.
(That and *Tears of the Kingdom*, but let's not talk about that.)

Making a change doesn't require changing research fields. Why do that? Well, part of me is just curious
to see if I can. I've always found the SMBC ["Seven Years"](https://www.smbc-comics.com/index.php?db=comics&id=2722#comic) comic inspiring, albeit a bit preachy.

![TODO](/public/switching-into-safety/smbc.gif)
{: .centered }

(Edited from original comic)
{: .centered }

When discussing careers with someone else, he said the reason he *wasn't* switching fields was
because capitalism rewards specialization, research especially so. Robotics was specialized enough
to make his comparative advantages better. I agree with this, and it does push against
switching fields. However,
as I've argued [before]({% post_url 2024-07-08-tragedies-of-reality %}), I expect my experience with
robotics to transfer to challenges that other parts of machine learning are now facing.
I'm also not starting completely from zero, with the goal of working on projects that can leverage
my past expertise.


The Slightly Spicier Research Interests Reasons
--------------------------------------------------

The way robot agents are trained can broadly be grouped into classical control theory, imitation learning,
and reinforcement learning. Of those, I am a fan of reinforcement learning the most, due to its generality
and potential to exceed human ability.

Exceeding human ability is not the current bottleneck of robot learning.

Reinforcement learning was originally a dominant paradigm in robot learning research, since it led
to the highest success rates.
Over the years, most of its lunch has been eaten by imitation learning methods that are easier
to debug.
I don't hate imitation learning, I've happily worked
on several imitation learning projects, it's just not the thing I'm *most* interested in.
Meanwhile, there are some
interesting applications of RL-style ideas to LLMs right now, from its use in RLHF to training value functions
for search-based methods like [AlphaProof](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/).

When I started machine
learning research, it was because I found learning and guiding agent behavior to be really interesting.
The work I did was in a robotics lab, but I always cared more about the agents than
the robots, the software more than the hardware.
The thing that kept me in robotics despite this was that in robotics, you cannot cheat the real world. It's gotta work
on the real hardware. This really focused research onto things that actually had real
world impact, rather than impact in a benchmark too artificial to be useful.

Over the past few years, software-only agents have started looming. This became an important
decision point for me - where will the real-world agents arrive first? Game playing AIs have
been around forever, but games aren't real. These LLM driven systems...those were more real.
In any world where general robot agents exist, software-only agents will have started working
first.
I saw a future where more of my time was spent learning the weaknesses and strengths
of the software-hardware boundary, rather than improving the higher-level reasoning of the agent,
and decided I'd rather work on the latter.
If multimodal LLMs are going to start having agentic behaviors, moving away from hardware would
have several quality of life benefits.

One view (from Ilya Sutskever, secondhand relayed by Eric Jang) is that
["All Successful Tech Companies Will be AGI Companies"](https://evjang.com/2022/04/25/rome.html).
It's provocative, but if LLMs are coming to eat low-level knowledge work, the valuable work
will be in deep domain expertise, to give feedback on whether datasets have the right information
and whether the AI's outputs are good.
If I'm serious about switching, I should do so when it's early, because it'll take time to
build expertise back up. The right time to have max impact is always earlier than the general
public thinks it is.

And, well, I talk a big game about impact, but I don't think I should need to do so to justify
myself. I'm not
sitting here crunching the numbers of my impact or utility.
"How do we create agents that choose good actions" is just a problem I'm really interested in.

![TODO](/public/switching-into-safety/neat.jpg)
{: .centered }

The Full Spice "Why Safety" Reasons
----------------------------------------------------

Hm, okay, where do I start.

There are a lot of different views on what AI safety is, as well as conflations between AI safety the research
field and AI safety the community. It is common for people to say they are attacking the field
when they are actually attacking the community.
The two are not the same, but are linked enough that it's not *totally* unreasonable to conflate them. Let's tackle the community first.

I find interacting with the AI safety community to be worthwhile, *in moderation*. It's a thing I like wading into, but not
diving into. I don't have a LessWrong account but have read posts sent to me from LessWrong. I don't read Scott Alexander but have read a few essays he's written.
I don't have much interaction with the AI Alignment Forum, but have been reading more of it recently.
I don't go to much of the Bay Area rationalist / effective altruism / accelerationist / tech bro / whatever it's called now scene, but I have been to some of it, mostly because I had a phase where I was pretty into effective altruism around 2015-2018. At the time, I saw it as a movement I wasn't part of, but which I wanted to support.
Now I see it as a movement that I know exists, where I don't feel much affinity towards it or hatred against it.
"EA has problems" is a statement I think even EAs would agree with, and "Bay Area rationalism has problems" is something rationalists would agree with too.

The reason AI safety the research topic is linked so much to that scene is because a lot of writing about the risks of AGI and
superintelligence originate from those rationalist and effective altruist spaces. And so approving of one can be seen as approving the other.
I don't like that I have to spill this much digital ink spelling it out, but me thinking AI safety is important is
not an endorsement for or against anything else in the broader meme space it came from.

Is that clear? I hope so. Let's get to the other half: why I think safety is worth working on.

\* \* \*
{: .centered }

I would say the core tenets of my views on AI safety are that:

1. It is easy to have an objective that is not the same as the one your system is optimizing, either because it is easier to
optimize a proxy objective (negative log likelihood vs 0-1 classification accuracy), or because your objective is hard to
describe. People run into this all the time.
2. It's easy to have a system that generalizes poorly because you weren't aware of some edge case of its behavior due to
insufficient eval coverage, poor model probing, etc.
3. The way people solve this right now is to just...pay close attention to what the model's doing, using humans in the loop
to inspect eval metrics, try small examples, reason about how trustworthy the eval metrics are, etc.
4. I'm not sold the current tooling scales to better systems, especially superhuman systems.
5. I'm not sold superhuman systems will do the right thing without better supervision than we can currently provide.
6. I expect superhuman AI in my lifetime.
7. There's a low chance the current paradigm gets all the way there...but it's higher than
I'm comfortable with.

There's a lot of other stuff surrounding it, but that's the core for me.

In so far as intelligence can be defined as the ability to notice patterns, pull together disparate pieces of information,
and overall have the ability to get shit done, then there's definitely room to be better than people. Evolution promotes things
that are better at propagating or replicating, but it works *slow*. The species that took over the planet (us) is likely
the least intelligent organism possible that can still create modern civilization. There's room above us for sure.

I then further believe in the instrumental convergence theory: that systems can evolve tendencies to promote their own
survival even if that is not directly what their loss function is. You need a **really** strong optimizer and model
for that to arise, but I think it would. At one point, I sat down and went through a list of questions for a
"P(doom)" estimate - the odds you think AI will wreck everything. How likely do you think transformative AI is by this date,
if it exists how likely is it to have its own goals, if it has goals how likely are they to be power-seeking, if it's power-seeking
how likely is it to be successful, and so on. I ended up with around 2%. I am just the kind of person who thinks I have some
ability to mitigate a 2% risk and that it's worth looking at risks of that size.

Anecdotally, my [AI timelines]({% post_url 2024-01-10-ai-timelines-2024 %}) are faster than the general public,
and slower than the people directly working on frontier LLMs. People have told me "10% chance in 5 years" is crazy, in both directions! And I think there
is a chance that alignment is overblown, existing common sense in LLMs will scale up, and OSHA / FDA style regulations will
slow down deploying AGI in high-risk scenarios. I also think there is a chance that doesn't happen. There are scenarios where you
want to allow some rule bending for the sake of innovation, but to me AI is a special enough technology
that I'm hesitant to support that.
I also don't think we have to get all the way to AGI for AI to be transformative. This is mostly
because I'm sympathetic to an argument from [Holden Karnofsky](https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/), that if a lab has the resources to train an AI, it has the resources to run millions of copies of that AI at inference time, enough to outnumber naive human supervision.
(His post claims "several hundred millions of copies" - I think this is an overestimate, but the
core thesis is correct.)

So far, a number of alignment problems have been solved by market forces. Companies need their
AIs to follow user preferences enough for their customers to use them. I used to have the view
that the best thing for alignment would be getting AI products into customer's hands in low stakes
scenarios, to get more data while making sure no one mistake was too dangerous. This happened
with ChatGPT, and as I've watched the space evolve, I...wish there was more safety research
than there has been.
Capitalism is great at solving the blockers to
profitability, but it's also very willing to define economic niches that ignore the hard
problems.
People are too [hungry]({% post_url 2024-07-19-ml-hurry %}) for the best models to do due
diligence. The level of paranoia I want people to have about LLMs is not
the level of paranoia the market has.

One of the original reasons I was less interested in AI safety was that the existing work on it looked incredibly theoretical.
It was very complexity theory style, studying the behavior of bounded Turing machines, analyzing
[AIXI](https://en.wikipedia.org/wiki/AIXI), and so on. That stuff is my jam, but I was quite pessimistic on any of it
mattering. I would like someone to be trying the theory angle, but I'm not looking for that someone to be me. There is now a lot
of non-theory work going on in AI safety, which better fits my skill set. You can argue whether that work is actually making
progress on aligning superhuman systems, but I think it is. I considered the
Fairness for Machine Learning side too, but a lot of existing literature focuses on fairness in
classification problems, like algorithmic bias in recidivism predictors and bank loan models.
Important work, but it didn't have enough actions, RL, or agent-like things to appeal to me.
The claims of a schism between the fairness and alignment communities feel overblown to me.
The average person I've met from either is not interested in trying to make a person "switch
sides", they're just happy someone's joining to make the field larger, because there is just
*so much* work to do.
Even if the sociology is quite different, at the fundamentals level both areas are about
when optimization goes wrong.

I'm aware of the arguments that historically, most AI safety work has not been that different from
broader AI work. Scaling laws came from safety-motivated people and are the core of current frontier
models. RLHF developments led to ChatGPT. Better evaluation datasets led to better hill climbing
of models without corresponding safety gains.
Even the recent wave of representation engineering came from interpretability, but
has been adopted most enthusiastically by the open-source community, due to its ability
to develop better [jailbreaks via intervening on layer activations](https://arxiv.org/abs/2401.06824).
People who don't think safety matters brands this as [typical Silicon Valley grandstanding](https://www.youtube.com/watch?v=B8C5sjjhsso) to pretend they're not trying to make money.
People who care about safety a lot call this [safetywashing](https://arxiv.org/abs/2407.21792):
the stapling of "safety" to work that does not advance safety.
But...like, you can claim people are insincere and confused about anything. It's hard to convince
people you aren't these things. I don't know, I think most people I talk about safety with
are confused rather than insincere, and aiming for safety while confused is better than not
aiming at all.

So, that's what I'm doing. It may not be permanent move, but it feels right based on the current
climate. If that climate turns to AI winter, then I'll reconsider. Right now, it is sunny
as all hell.
