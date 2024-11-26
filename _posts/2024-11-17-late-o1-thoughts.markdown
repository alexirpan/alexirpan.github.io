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
asked and got a press embargo. If treu, that makes this video especially useful for understanding
OpenAI o1, and reasoning LLMs in general.

https://www.youtube.com/watch?v=eaAonE58sLU

unlike many talks in the lecture series, the video was not uploaded until several months later
post o1 release

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
