---
layout: post
title:  "o1 Takes That Are Better Late Than Never"
date:   2024-11-17 11:19:01 -0700
---

Before o1 got announced, there were rumors going around that OpenAI's next model would follow
a fundamentally different paradigm. For once, the rumors live up to the hype. Even now, there isn't
quite a public model that does things the same way o1 does. But is that important?

The big thing that sets o1 apart is its "thinking" or "reasoning" tokens. As explained in the
[launch post](https://openai.com/index/learning-to-reason-with-llms/), OpenAI o1 is deliberately
trained to spend time generating long, internal chains of thought before responding. This means
it takes much longer to generate an answer compared to other models, but it is better able to
handle complex queries.


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

Expect to see more hunting for things like this: modifications that increase the affordances
of where compute can be pushed into the LLM, and then push compute into those affordances.


# Scaling Laws View

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
training times. I'm not in pretraining. But I bring it up because it's the kind of optimization you only
do when you are no longer doing things for science's sake, and have to eke out performance in a real,
practical compute budget.

To me, test-time compute feels similar.
