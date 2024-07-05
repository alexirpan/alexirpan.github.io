---
layout: post
title:  "The Tragedies of Robot Learning are Coming for You"
date:   2024-06-18 22:11:00 -0700
---

Once upon a time, in the ancient year of 2023, I was at an ML conference. The night was young, the drinks were flowing, and the topic turned to one question: "if you could take any machine learning subfield, and give all their
resources to a different one, what are you killing and what are you saving?"

One person there declared they'd kill robotics. I don't remember what they saved, but when I pushed them on it, they said nothing happens in robotics, relative to everything else.

I have two counterclaims:

* The reason it looks like nothing happens in robot learning is because you can't do anything without directly tackling the hard problems.
* The hard problems of robotics are not unique to robotics, and they're coming for you.

One of the very common refrains in robotics is "reality is messy".
My version is a bit longer: **reality is complicated, relative to code, and in robotics you're often pushing
a messy reality into an abstraction nice enough for code to act on it**.
As a field, computer science has spent decades creating abstraction
layers to let code drive electricity to your hard drive, processor,
and monitor in the way the code says. These abstraction layers are reliable enough
that you usually don't even think about them.

![xkcd comic](/public/tragedies-of-robot-learning/abstraction.png)
{: .centered }

There's a lot of benefit to doing this!
Code and digital data is incredibly replicable. I have copies of the file
representing the draft of this blog post synced across 3 devices, and don't even
think about it. I do not have the expertise to debug hardware errors, and usually just hope
a restart fixes them.

However, to quote Joel Spolsky,
[all abstractions are leaky to some degree](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions), and I've found those leaks tend to be bigger in robotics. There are many
ways for things to go wrong that have nothing to do with the correctness of your code.

Is that because of something fundamental to the subject? Sort of? A lot of robot
hardware is more experimental than a smooth-edged Macbook or well worn
Linux server, since consumer robots aren't as big an industry yet. "Experimental" tends to mean "weird, more frequent failure states".

But, I don't think the hardware is the primary driver of friction. It's **reality** that's
the friction. Benjamin Holson put it really well in his ["Mythical Non-Roboticist"](https://generalrobots.substack.com/p/the-mythical-non-roboticist) post:

> The first kind of hard part is that robots deal with the real-world, imperfectly sensed and imperfectly actuated. Global mutable state is bad programming style because it's really hard to deal with, but to robot software the entire physical world is global mutable state, and you only get to unreliably observe it and hope your actions approximate what you wanted to achieve.

**Nothing about this is specific to robotics.** Any software that measures reality will have imperfect sensing. Any software that tries to affect real world change has to deal with the global mutable state of the real world. Any software whose actions depend on what's going on in reality is inviting
an entirely new type of noise and complexity.

There's been a recent wave of hype around LLMs - what they can do, where they can apply. Implicit in all of this is the belief that LLMs can make significant changes to how people interface with technology, in their work and in their free time. In other words, *that LLMs will change our reality*.
I'm actually on board this hype wave, but that means all those pain points of reality are coming
for a field that historically does a bad job at considering reality.

At the same ML conference where this person said robotics was a waste of resources, I mentioned
that [we were experimenting with foundation models in real robots](https://robotics-transformer2.github.io/). I was told this seemed a bit scary, and after pointing out it was a research prototype,
I asked why they thought LLMs generating and executing code wasn't scary. Silicon Valley types
have a bit of a paradox them. They both believe that software can power amazing transformational startups, and that *their* software doesn't merit contemplation or introspection.

I've
noticed (with some schadenfreude) that LLM practitioners keep discovering pain points that would fit right in a roboticist's mouth. "We can't reproduce these training runs because it's too capital-intensive." Yeah, welcome to not having the same robot platform. "I can't get [Bing to gaslight me about Avatar 2's release date](https://x.com/MovingToTheSun/status/1625156575202537474), since it keeps pulling up news article written about the gaslighting and self-corrects." Welcome to the globally mutable state of text on the Internet.

It's never been easier to get access to cutting-edge research, or understand what an LLM demo is attempting to do. But there's a reason the saying is "all robot demos lie". All LLM demos lie to. What's important is evaluating the type, size, and importance of the lie.
Correctly evaluating hype videos is often an exercise in being an asshole. Did they show how it could generalize? If they didn't, it probably can't. Did they mention how cherry-picked the examples were? You're probably looking at the top 10% of its behavior if they didn't.
Not every top 10% behavior can be promoted to a behvior that occurs all the time. Not every sign
of life leads to actual life. (At some level, research is about proving which signs of life
are real and which is fake.)

Being this relentless isn't always correct. It's like saying [Lionel Messi's hadn't proven he was good because he hadn't done it on a cold rainy night in Stoke](https://onefootball.com/en/news/origins-of-can-they-do-it-on-a-cold-rainy-night-in-stoke-38867246). At some point you concede the man's proven himself, or the model's proven itself.

As LLMs get better, as AI becomes more common in daily life - we, as a society, will need to get
increasingly good at deciding if the model's proven itself. One of my main worries about the future is
that we get bad at evaluating if the model's proven itself. So if anything, I expect roboticists
to be ahead of the curve. We were complaining about evaluation 4 years before everyone agreed evaluating LLMs were hard. We were trying to get enough data to capture the long tail of self-driving long
before "we need data for rare use cases" became the rallying cry of foundation model pretraining teams. All of us are running into the same walls of reality that robotics has tried to fight through for years and years. Welcome to the pain.


One of the common
defenses of comics as a medium is that because they are drawn in a more abstract style,
it is easier for people to project a bit of themselves into the work, giving them more
appeal than more photorealistic works.

![A side-by-side comparison of a cartoon version of the author, and a photorealistic author](/public/tragedies-of-robot-learning/36last2.png)
{: .centered }

From *Understanding Comics*, by Scott McCloud
{: .centered }

A similar principle holds true in applying ML / AI methods. The fewer assumptions they make,
the more generally they can apply, but the harder your problems are.
In practice, ML tends to make many *implicit* assumptions.
Sometimes you can ignore latency, because you're acting in a turn based environment. Sometimes you
can assume nothing outside your camera's field of view exist, because object permanence isn't a requirement.


Sometimes your dataset is biased towards a certain demographic. When evaluating a paper, the common
question you should ask yourself is what assumptions the paper is making, and when evaluating
a demo, you should ask yourself what assumptions the demo is hiding. There's a reason the saying
is "all robot demos lie".



backing across 3 different
devices


The Default Does Not Reproduce
-----------------------------------

A lot of digital ink has been spilled about the replication crisis, and machine learning is no different. Yet, relative to other fields, machine learning
has had it pretty good.
In many subfields, the standard evals are just a dataset of input-output pairs, easily copyable from computer to computer, sometimes with open-source code that runs the analysis for you.

Meanwhile half the papers I've helped write cannot be evaluated anymore, since we either don't have the same lab space or it got repurposed for a new project.
One of them was run in a building that was demolished - good luck running that again.

There is always a question of whether benchmarks measure real research progress. There's idiosynchraticizes in every dataset. ImageNet is 10% dogs. The "photographer's bias" makes the object of interest usually centered in the frame (because real images come from people taking photos, and people tend not to upload photos with motion blur). (FIND SOURCE) Some of the common translation benchmarks are 10 years old and won't cover modern slang.

The part that's different about robotics is that your robot is embodied in the real world.
You're using abstract math to move a real, concrete thing, and that invites
all sorts of uncontrollable noise into your system. The computer science field and industry has spent many decades trying to hide the messiness of reality behind a less messy coding interface, and in many ways it's **succeeded*. But once that barrier breaks, you're in trouble.

(elaborate more here, it needs more context)
When LLMs and retrieval augmented generation was rising, especially with the articles about Microsoft Sydney, one of the notes I saw from researchers was that they
could no longer reproduce the Avatar gaslighting behavior that was reported.
Sydney was pulling news articles about itself during the retreival, which changed the generation. And well, that's just the reality you need to deal with. There were complaints that OpenAI changed the model they deployed, making several research papers based on davinci obsolete. Be thankful that there is still a company to complain to - a number of research labs have robots whose manufacturers went bankrupt years ago.

(What is the goal of this post? Is it to rant? I think it's to rant that progress in some domains is hard, but it's not getting at the core claim that making agents work is hard due to the explosion in the interaction surface.)

(Okay, maybe i should restructure this whole thing as, what makes robot learning hard, and what parts of that problem exist elsewhere, that may be better.)
