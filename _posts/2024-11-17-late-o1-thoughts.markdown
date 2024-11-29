---
layout: post
title:  "OpenAI o1 Takes That Are Better Late Than Never"
date:   2024-11-17 11:19:01 -0700
---

I realize how late this is, but for various reasons, I didn't get a post out while o1 was "fresh",
and one advantage of cold takes is that you get to see which hot takes have held up.

OpenAI o1 is a model release widely believed (but not confirmed) to be a post-trained version
of the GPT-4o checkpoint. It is directly trained to spend more time generating long, internal
chains of thought before responding.

Why would you do this? Some questions may fundamentally require more partial work or "thinking time"
to arrive at the correct answer. This is considered especially true for domains like math and
automated research. So, if you train a model to specifically use tokens for thinking, it may be able
to reach a higher ceiling of performance, at the cost of taking longer to generate an answer.

Based on the [launch post](https://openai.com/index/learning-to-reason-with-llms/), system card,
uses later, etc., this has been the case. OpenAI-o1 is not preferred over typical LLMs on simple
queries, but is able to solve queries that other models aren't able to do.


# The Compute View

When GPT-4 was first announced, OpenAI did not disclose how it was implemented. Over time, the
broad consensus (from leaks and other places) is that GPT-4 was a mixture-of-experts model,
mixing 8 copies of a 220B parameter model.

This was a bit disappointing to learn. To quote George Hotz, ["mixture[-of-experts] models are what you do when you run out of ideas"](https://www.youtube.com/watch?v=WJWHIZoBOj8).
In many ways, a mixture of experts model is "supposed" to work. I say "supposed" in quotes because
things are never quite that easy in machine learning, but for some time mixture-of-experts models
were viewed as a thing you used if you had too much compute and wanted a funnel to push it through.

I think this view is a bit too simplistic. The original [Switch Transformers paper](https://arxiv.org/abs/2101.03961)
showed MoE models had different scaling properties and could be more compute efficient. There are
a bunch of nontrivial properties of mixture-of-experts models. But, broadly, yes you can view
mixture models as a way to add another dimension to multiply your effective compute usage.

o1 feels similar to me. This time, the dimension is the amount of compute you use at test-time - how
many response tokens you generate for each user query. One way to describe o1 is that it's not as
good if you gave it the same 1-shot budget as a standard LLM, but it's been trained to be better
at spending *larger* compute budgets in useful ways. So, as long as you commit to giving o1 more
compute at test-time, it can do better than just rolling out an equivalent GPT-4o many times.

(CHART SHOWING THAT HERE)

In many ways this is a fundamentally different paradigm from prior models, because it places
more focus on test-time compute. Is that new paradigm a good one? When
LLMs first entered public consciousness, one big advantage was how *fast* they generated text that
a human would have trouble generating. Attention spans tend to only go down. Creating a paradigm
where you ask users to wait longer is certainly a bold choice.

I think it is an important paradigm shift, but probably not one the average user will appreciate
or need for some time. You can view o1 as increasing the affordances of where compute can be pushed
into the LLM. If you believe compute is the bottleneck of LLMs, then you ought to be looking for
all the places where compute could impact model capabilities, and then push compute into those
places. Methods that enable using test-time compute better are now just another example of that.


# Scaling Laws View

In May 2024, Noam Brown from OpenAI gave a talk at the University of Washington on the power of planning and search algorithms
in AI, covering his work on expert-level systems playing Texas Hold'em and Diplomacy. Notably,
most talks in the lecture series have their recordings uploaded within a few days. This one
was not uploaded until September, after o1's release. The current guess is that Noam or OpenAI
asked and got a press embargo. If true, that makes this video especially useful for understanding
OpenAI o1, and reasoning LLMs in general.

https://www.youtube.com/watch?v=eaAonE58sLU

In this talk, Noam mentions an old paper on [Scaling Laws in Board Games](https://arxiv.org/abs/2104.03113). This
paper was from a hobbyist (Andy Jones), studying scaling laws in toy environments. I remember reading this paper when it came out,
and I liked it. I then proceeded to not *fully* roll out the implications. Which I suppose is part of why I'm talking about o1 rather
than building o1.

Among other results, Jones found that there was a log-linear trade-off between train time compute and
test time compute. To achieve a given fixed Elo target, each 10x of train-time compute could be exchanged for 15x test-time compute.
(Of course, the best model would use both.)

CHART HERE

This is a nice chart and all, it's a cool relationship. Now let's rescale this such that they both start at 0 instead

CHART

See, if you're going to spend a ton of FLOPS training a model...then allocating 0.0000001% of that budget to running the model
more at test time to simulate getting 10x more training FLOPS is just totally worth it. Especially if you change this from FLOPS to dollars.
Compute isn't exactly linear in dollars (there are big fixed costs), but, I would totally pay an extra 1 cent per inference call to save
$XXX. (Get the real numbers here)

The ratios for real problems are a good deal worse than this (see https://arxiv.org/pdf/2408.03314), but when cast this way,
it is just so obvious that spending time on search is the correct strategy to max out the performance of an LLM.

But do people actually need that?

# User View

I am not the best at leveraging LLMs for productivity. I tend to underestimate the things I can offload to a model, and
treat LLMs as a way to get quick lossy answers to certain types of questions, when in reality they are probably less
lossy than I think they are.

Now, that's relevant because the way I use LLMs is heavily biased to speed. I just want an answer now to stick into my
existing workflow - I am not trying to get the LLM to do as well as it can without human assistance. And for most of my
use cases, the leading Gemini / Claude / ChatGPT checkpoints are good enough. I haven't needed the potential power of
reasoning models yet.

Based on the released stats, this is true in user testing as well, where o1 is only preferred on certain kinds of queries.

CHART

My guess is that the average person doesn't care too much about chasing the absolute frontier of models. They're okay with
something that's good enough. They would be willing to pay 1 cent less per inference call because they don't need more than that.
I have no firsthand experience with Character.AI models, but my vague impression was that a lot of users don't need their AI
characters to have a ton of reasoning power, or ability to do research across many disciplines. They just want good roleplay and
good conversation - and LLMs crossed that point a while ago. Based on the AMA on the r/chatgpt subreddit, most users just want
bigger context windows rather than more intelligence.

This ties into a concept from Dario's Machines of Loving Grace essay: that as AI becomes better, we need to think in terms of
marginal returns on intelligence. There's plenty of domains where the marginal returns flatten out pretty quick!

# Safety View

>     We seem to have been given lots of gifts⁠(opens in a new window) relative to what we expected earlier: for example, it seems like creating AGI will require huge amounts of compute and thus the world will know who is working on it, it seems like the original conception of hyper-evolved RL agents competing with each other and evolving intelligence in a way we can’t really observe is less likely than it originally seemed, almost no one predicted we’d make this much progress on pre-trained language models that can learn from the collective preferences and output of humanity, etc.

https://openai.com/index/planning-for-agi-and-beyond/

I am now working on safety, so it feels like my duty to comment on the safety implications.

CUT CONTENT
-------------------------------------------------------

This paper 

specifically Hex. This was a toy
environment where an AlphaZero algorithm was used to train an agent to play games, controlling for
the amount of compute used to train the policy, and the compute used to do search. 


One of the 

Mentally, I bucket deep learning
developments into a few eras:

1. The Wild West Era, where people just made whatever models they could fit in their GPUs. This
is where you get ResNet-50. It isn't 50 layers because that's the correct compute-efficient number to pick.
It's 50 layers because that's a nice round number.
2. The Early Scaling Laws Era, where people started fitting curves of model performance given a fixed
parameter, data, or compute budget, but when the models were not doing any useful work. Metrics focused on
things like the pretraining loss curve, often assuming you were only going to run a model eval once.
3. The Current Scaling Laws Era, where the models are actually getting used in products, real-world
usage shapes the scaling research, and people fit curves to as many aspects of the system they can
reasonably measure.

So, for example: no pretraining team directly follows the Chinchilla recommendations
anymore. Chinchilla laws were derived assuming a fixed compute budget, where you'd run a long model training run then
evaluate it once. In our current world, a given model will be deployed to millions of users. So instead of
your eval being negligible, your model inference is now a meaningful fraction of your compute
budget. Now, at a mechanical level, I don't know what that does to the empirical solutions for model sizing and
training times. I'm not in pretraining. But I bring it up because it's an example of an idea changing
the model under which you try to fit your empirical curves.

To me, test-time compute feels similar. Before

In general, the current models for AI are that an industry company spends a long time training a model, then sells access to run it on their GPUs or TPUs. Meanwhile, a hobbyist can use an open source model running on their local hardware
if they don't want to trust big companies, want to control everything themselves, etc.
If test-time computation becomes more necessary to achieving best performance, the rigs needed to run local models may
become increasingly impractical.

After reflecting on it, I don't think that consideration is too important. The trendline has already been for
local models to become harder to run.

A refrain common in the safety community is that we don't really understand the process LLMs use to generate tokens. We can describe the loss function, and the distribution over tokens, but we don't have as good a handle on
the inner computations that lead to those next-token distributions.
