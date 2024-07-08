---
layout: post
title:  "The Tragedies of Reality Are Coming for You"
date:   2024-06-18 22:11:00 -0700
---

In 2023, I was at an ML conference. The night was young, the drinks were flowing, and the topic turned to a question: "if you could take any machine learning subfield, and give all their
resources to a different one, what are you killing and what are you boosting?"

I don't remember what they boosted, but one person said they'd kill robotics. When I pushed
them on it, they said robotics progress is too slow and nothing happens relative to everything else.

I think they were correct that robotics progress was slower than software-only machine learning
subfields. But I would also add two things:

* The reason robot learning progress is slower is because it's very hard to do anything without tackling the hard problems.
* The hard problems of robotics are not unique to robotics.

One of the very common refrains in robotics is "reality is messy".
I would extend it to **reality is complicated, relative to code, and in robotics you're
often pushing a messy reality into an abstraction nice enough for code to act on it**.
As a field, computer science has spent decades creating nice abstraction
layers between hardware and software. Code describes how to drive electricity to my
hard drive, processor, and monitor, reliably enough that I don't have to even think
about it.

![xkcd comic](/public/tragedies-of-robot-learning/abstraction.png)
{: .centered }

[From xkcd](https://xkcd.com/676/)
{: .centered }

There's a lot of benefit to doing this! Once you've done the hard work, and moved your
progress towards acting in abstract logical space, everything's easier.
Code and data is incredibly replicable. I have copies of the file
representing the draft of this blog post synced across 3 devices, and don't even
think about it.

However, to quote Joel Spolsky,
[all abstractions are leaky to some degree](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions), and I've found those leaks tend to be bigger in robotics. There are many
ways for things to go wrong that have nothing to do with the correctness of your code.

Is that because of something fundamental to the subject? A little bit. A lot of robot
hardware is more experimental than a laptop or
Linux server. Consumer robots aren't as big an industry yet. "Experimental" tends to mean "weird, easier to reach failure states".

But, I don't think the hardware is the primary driver of friction. It's **reality** that's
the friction. Benjamin Holson put it really well in his ["Mythical Non-Roboticist"](https://generalrobots.substack.com/p/the-mythical-non-roboticist) post:

> The first kind of hard part is that robots deal with the real-world, imperfectly sensed and imperfectly actuated. Global mutable state is bad programming style because it's really hard to deal with, but to robot software the entire physical world is global mutable state, and you only get to unreliably observe it and hope your actions approximate what you wanted to achieve.

Robotics research relies on building new bridges between reality and software, but **that happens outside of robotics too**. Any software that interfaces with reality will have imperfect knowledge of that reality. Any software that tries to affect real world change has to deal with reality's global mutable state.
Any software whose actions depend on what's going on in reality invites adversarial
sources of noise and complexity.

Game AI is an instructive example here. Chess AIs are reliably superhuman.
However, some superhuman Go AIs are beatable if you play in a specific way, as discovered by
[Wang and Gleave et al, ICML 2023](https://arxiv.org/abs/2211.00241). Adversarial
techniques found a strategy legible enough for humans to reproduce.

> In Appendix G.2 one of our authors, a Go expert, was able
> to learn from our adversary’s game records to implement
> this [cyclic] attack without any algorithmic assistance. Playing in
> standard human conditions on the online Go server KGS
> they obtained a greater than 90% win rate against a top
> ranked KataGo bot that is unaffiliated with the authors. The
> author even won giving the bot 9 handicap stones, an enormous advantage: a human professional with this handicap
> would have a virtually 100% win rate against any opponent,
> whether human or AI. They also beat KataGo and Leela
> Zero playing with 100k visits each, which is normally far
> beyond human capabilities. Other humans have since used
> cyclic attacks to beat a variety of other top Go AIs.

Meanwhile, a few years ago OpenAI created a system that defeated the reigning world champions at
Dota 2. After making the system available to the public to test its robustness, [a team engineered a strategy that achieved a 10 game win streak](https://web.archive.org/web/20200306003104/https://arena.openai.com/#/results).

![OpenAI Five leaderboard](/public/tragedies-of-robot-learning/dota.png)
{: .centered }

Based on this, one pessimistic view you could hold is that connecting even a simple "reality" of a 19 x 19 Go board or Dota 2 is enough additional complexity to make robust behavior challenging.
I think this view is unfair, because neither of these systems had robustness as a top-level
objective, but I do think they're an interesting case study.

There's been a recent wave of hype around LLMs - what they can do, where they can apply. Implicit in all of this is the belief that LLMs can make significant changes to how people interface with technology, in their work and in their leisure. In other words, *that LLMs will change how we mediate with reality*.
I'm actually on board this hype wave, to be specific I suspect foundation models are overhyped short-term
and underhyped long term.
However, that means all the messiness of reality is coming
for a field that historically does a *bad* job at considering reality.
At the same ML conference where this person said robotics was a waste of resources, I mentioned
that [we were experimenting with foundation models in real robots](https://robotics-transformer2.github.io/). I was told this seemed a bit scary, and I reassured them it was a research prototype.
But I also find LLMs generating and executing software a little scary, and thought it was
interesting they implicitly worried about one but not the other.
Silicon Valley types
have a bit of a paradox to them. They both believe that software can power amazing transformational startups, and that *their* software doesn't merit contemplation or introspection. I consider the world
of bits to be as much a part of reality as the world of atoms. Operating on a different level, but
a part of it nonetheless.

I've
noticed (with some schadenfreude) that LLM practitioners keep discovering pain points that robotics
has hit before.
"We can't reproduce these training runs because it's too capital-intensive." Yeah, this has been
a discussion point in robotics for at least a decade.
"I can't get [Bing to gaslight me about Avatar 2's release date](https://x.com/MovingToTheSun/status/1625156575202537474), since it keeps pulling up news articles written about itself, and self-corrects before generation." We're now in a world
where any publicly available Internet text can irrecoverably influence retrieval-augmented
generation. Welcome to globally mutable state. Every time I see someone claim there's a regression
in ChatGPT's behavior, I'm reminded of the conspiracies I and others have come up with to explain
sudden, inexplicable drops in robot performance, and whether the problem is the model, the environment, or us extrapolating too much from anecdata.

There's a saying that "all robot demos lie", and people are discovering all LLM demos lie too.
I think this is fundamentally impossible to avoid, because of the limitations of human attention.
What's important is evaluating the type, size, and importance of the lie.
Did they show how it could generalize? Did they mention how cherry-picked the examples were?
These questions become more complicated once you connect reality into the mix.
Sure, Messi's looked like a good player so far, but
["can he do it on a cold rainy night in Stoke"?](https://onefootball.com/en/news/origins-of-can-they-do-it-on-a-cold-rainy-night-in-stoke-38867246)

What makes it complicated is that the answer to these questions isn't always "no". Messi *could*
do it on a cold rainy night in Stoke. He *was* good enough. And that makes it hard, because being correct on a "yes"
matters much more than being correct on a "no".
As LLMs get better, as AI becomes more common in daily life - we, as a society, will need to get
increasingly good at deciding if the models have proven themselves. One of my main worries about the future is
that we get bad at evaluating if the models have proven themselves. But, I expect roboticists
to be ahead of the curve. We were complaining about evaluation years before claims of LLMs gaming
common benchmarks.
We were trying to get enough data to capture the long tail of self-driving long
before "we need better data coverage" became the rallying cry of foundation model pretraining teams.
Machine learning has lived in a bubble that was the envy of roboticists and chemists and biologists and
neuroscientists, and as it starts to *actually work*, we'll all be running into the same walls
of reality that others have dealt with for years and years.
These challenges can be overcome, but it'll be hard.
Welcome to the real world. Welcome to the pain.
