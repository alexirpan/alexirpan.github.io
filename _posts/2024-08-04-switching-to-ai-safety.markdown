---
layout: post
title:  "I'm Switching Into AI Safety"
date:   2024-07-08 10:15:00 -0700
---

Well, you can read the title. As of last month, I've been winding down my existing robotics projects,
and have switched to the AI safety team.

I have been slightly dreading writing this post, because my feelings on AI safety are complicated and take effort to
work through, but it is a big enough life update that I *have* to write this post. Such is the life of a blogger.


The Boring, Personal Reasons
-------------------------------------------

I've been working on the robotics team for 8 years now, and I just felt like I needed to mix it up.
It was a little unsettling to realize that I had quietly become one of the most senior members of the team,
and that I had been in robotics longer than my manager, and my manager before that, and the one before *that*.
Really, this is something I thought about switching up back in 2021, but then my puzzlehunt team won MIT Mystery Hunt,
meaning we had to write next year's hunt. Writing it took up all of my 2022 and recovering from it took up much of my 2023.
(That and *Tears of the Kingdom*, but let's not talk about that.)

Still, such a change-up doesn't require changing research fields too. Why do that? Well, part of me is just curious
to see if I can do this. I've always found the SMBC ["Seven Years"](https://www.smbc-comics.com/index.php?db=comics&id=2722#comic) comic inspiring, albeit a bit preachy.

IMAGE

When discussing careers with someone else, he said the reason he *wasn't* switching fields was
because capitalism rewards specialization, research especially so, and robotics was specialized enough to make
his comparative advantages better. Which is all true, and pushes against this line of argument, but
as I've argued [before]({% post_url 2024-07-08-tragedies-of-reality %}), I expect some of the
my experience dealing with challenges in robotics to transfer to challenges other fields are facing.
I'm not starting from zero, and am aiming to work on projects that leverage my past expertise while
learning new things.


The Slightly Spicier Research Interests Reasons
--------------------------------------------------

The way that agents are learned in robotics can broadly be grouped into classical control theory, imitation learning,
and reinforcement learning. Of those, I am a fan of reinforcement learning the most, due to its generality
and potential to exceed human ability.

Reinforcement learning was originally a dominant paradigm in robot learning research, but has had more of its
lunch eaten by imitation learning in the past few years. I don't hate imitation learning, I've happily worked
on several imitation learning projects, it's just not the thing I'm *most* interested in.

When I got started in machine
learning research, it was because I found learning and guiding agent behavior to be really interesting.
It just so happened that I got started in a robotics lab, but I always cared more about the agents than
the robots, the software more than the hardware.
The thing that kept me in robotics despite this was that in robotics, you cannot cheat the real world. It's gotta work
on the real hardware, and I appreciated the way this focused research onto things that actually had real
world impact, rather than impact in a benchmark too artificial to be useful.

Then

In any future where robot agents work, software-only agents will have started working
before the robots did.
If multimodal LLMs are going to start having agentic
behaviors, then I'd rather work on those software-only use cases for quality of life reasons.

The vision I have of the next few years is that AI companies will differentiate themselves by the
quality and specificity of their data. Eric Jang has expressed this view in his [All Roads Lead to Rome](https://evjang.com/2022/04/25/rome.html)
post. Companies are either creating data moats to train their own models, or licensing their data to the
companies that can.

IMAGE

But, a corollary of this view is that companies will reward specializing in determining what good data
looks like. Even if the models can be trained to determine what good data is, a human still needs to verify
the model's judgment is correct.
As robotics becomes more real, I see a future where more of my time is spent learning the low-level weaknesses of
the software-hardware interface, rather than the higher-level reasoning of the agent, and I'm more interested in
the latter.
