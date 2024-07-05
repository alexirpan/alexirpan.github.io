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
* The hard problems of robotics are not unique to robotics. They are universal to real-world agents in general, and if you're aiming in that direction, they're coming for you.


What Makes Robotics Hard?
-----------------------------------

There are a few perpetual pain points.

1. Robots are embedded in the real world.

Code and digital data is incredibly replicable. I have copies of the file
representing the draft of this blog post synced across 3 devices, and don't even
think about it. As a field, computer science has spent decades creating abstraction
layers that let you manipulate logical constructs with code, with enough
reliability that you normally don't need to consider the hardware that lies underneath.

Robotics has a nasty habit of piercing those veils. To quote Joel Spolsky,
[all abstractions are leaky to some degree](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions),
but the leaks tend to be bigger in robotics.

Is that because of something fundamental to the subject? Well, maybe. A lot of robot
hardware is a lot more experimental than a smooth-edged Macbook or well worn
Linux server, and "experimental" tends to mean "weird failure states". But,
I don't think this is the primary driver of friction.

To me, the friction is that **reality is complicated, and you're trying to push
it into an abstraction nice enough for code to act on it**. Like, it just is. One
common defense of cartoons as a medium is that because cartoons are a more abstract
medium, it is easier for people to project themselves in the work.

IMAGE

And one of the common replies to this is that cartoons are great at bombastic
emotion, but are bad at subtle emotion. Asking a good actor to portray this is much
easier than



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
