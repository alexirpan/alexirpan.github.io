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
"How do we create agents that take the right actions" is just a problem I'm really interested in.
I think it's neat.

![TODO](/public/switching-safety/neat.jpg)
{: .centered }

The Full Spice "Why Safety" Reasons
----------------------------------------------------

Hm, okay, where do I start.

There are a lot of different views on what AI safety is, as well as conflations between AI safety the research
field and AI safety the community. It is common for people to say they are attacking the field but actually attack
the community, yet that's not *totally unreasonable* because of how linked the two are. Let's tackle the community first.

I find interacting with the AI safety community to be worthwhile, *in moderation*. It's a thing I like wading in, but not
diving into. I don't have a LessWrong account but have read posts sent to me from LessWrong. I don't read Scott Alexander
regularly but have read a few essays he's written.
I don't have much interaction with the AI Alignment Forum, although that's been increasing recently for obvious
reasons.

I also don't go to much of the Bay Area rationalist / effective altruism / accelerationist / tech bro / whatever it's called now scene.
I've been to some of it, but that is mostly because I had a phase where I was pretty into effective altruism around 2015-2018,
and then kept in touch with some people from there afterwards. At the time, I saw it as a movement I wasn't part of, but which I wanted to support.
Now I see it more as a movement that I know exists, where I don't feel much affinity towards it or hatred against it.
"EA has problems" is a statement I think even EAs would agree with. "Bay Area rationalism has problems" is something I assume
rationalists would agree with too.

The reason AI safety the research topic is linked so much to that scene is because a lot of writing about the risks of AGI and
superintelligence originate from those rationalist and effective altruist spaces. And so approving of one can be seen as approving the other.
I don't like that I have to spill this much digital ink spelling it out, but me thinking AI safety is important is
not an endorsement for or against anything else in the broader meme space it came from.

Is that clear? I hope so. Let's get to the other half: why I think it's worth working on.

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
and slower than people working in AI. People have told me "10% chance in 5 years" is crazy, in both directions! And I think there
is a chance that alignment is overblown, existing common sense in LLMs will scale up, and OSHA / FDA style regulations will
slow down deploying AGI in high-risk scenarios. I also think there is a chance that doesn't happen. There are scenarios where you
want to allow some rule bending for the sake of innovation, but to me AI is special enough that I'm hesitant to support that.
I originally expected that most alignment problems would get solved by market forces, by companies needing to make their AI trustworthy
enough for their customers to use. Now that I have seen the AI hype of 2023, seen Twitter comments declaring "alignment is solved" because
of one process supervision paper on one dataset...I no longer believe this. Instead I now expect companies to do the bare minimum
of alignment work needed, and skip the hard parts.

One of the original reasons I was less interested in AI safety was that the existing work on it looked incredibly theoretical.
It was very complexity theory style, studying the behavior of bounded Turing machines, analyzing
[AIXI](https://en.wikipedia.org/wiki/AIXI), and so on. That stuff is my jam, but I was quite pessimistic on any of it
mattering. I would like someone to be trying the theory angle, but I'm not looking for that someone to be me. There is now a lot
of non-theory work going on in AI safety, which better fits my skill set. You can argue whether that work is actually making
progress on aligning superhuman systems, but I think it is. Meanwhile, there was interesting work going on in the Fairness for
Machine Learning side, but it somehow didn't call to me as much. A lot of existing literature focuses on fairness in
classification problems, like algorithmic bias in recidivism predictors and bank loan models. Important work, but it didn't
have enough actions, RL, or agent-like things to call to me.

I'm aware of the arguments that historically, most AI safety work has just pushed people to build AI faster. Scaling laws came from
safety-motivated people and have encouraged investing more money. RLHF developments inspired ChatGPT. Even the recent wave
of representation engineering has been adopted most enthusiastically by the open-source community, who use them to develop better
[jailbreaks via intervening on layer activations](https://arxiv.org/abs/2401.06824).
But...what do these arguments mean? Like, you can claim people are insincere and confused
about anything. I think aiming for safety while being confused is better than not aiming for it
at all.

I'm also aware of the claims that work on longterm AI safety is distracting from work on near-term
harms. First of all, I'm not that longtermist of a person. Second, I'm not sure that's actually true.
It might be true of the conversation surrounding AI, but when it comes to the actual work, I think
some people are just more interested in some kinds of questions than other ones. The average person working on fairness or alignment is not interested in trying to make a person "switch sides" from one to the other. They want people
to join and make the field larger, because there is just *so much* work to do in both, and not
a lot of people doing it.
At the fundamentals level, both areas are about when optimization goes wrong, even if the sociology
above it is quite different.

I'm not treating AI safety as a permanent move. It's a move I'm making because of the current climate and potential.
If the potential of LLMs does not pan out, if we end up in another winter, if progress looks to be far away, then I'll reconsider.
