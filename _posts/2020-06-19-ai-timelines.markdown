---
layout: post
title:  "My AI Timelines Have Sped Up"
date:   2020-06-19 15:06:00 -0700
---

In 2015, I made the following forecasts about AGI

* 10% chance by 2045
* 50% chance by 2050
* 90% chance by 2070

Now that it's 2020, I'm updating my forecast to

* 10% chance by 2035
* 50% chance by 2045
* 90% chance by 2070

Or in short, I'm keeping the 90% line the same, but shifting everything else to
be faster. I go into my reasons below. I'm not going to claim they're great
reasons, the update is mostly by feel for what seems right.

First of all, the distribution is wider. Thinking back on the past 4 years, I
believe I was surprised by AI more than I expected to be. Unsupervised learning
got better way faster than I expected, deep RL got better a little faster than
I expected, and transfer learning was slower than expected. Combined, it made
me feel I should widen my forecast, so now 10% to 90% falls in a 35 year range
instead of a 25 year range.

Second, I noticed that in my 2015 forecast, I placed 10% to 50% in a 5 year
range, and 50% to 90% in a 20 year range. I think AGI is a long-tailed event,
there is a real possibility it's never viable. But this is an absurdly skewed
distribution, so I adjusted it to be less skewed.

That leaves the most important part - the shift to be closer. I've decided
things are progressing faster than expected.

1. Unsupervised Learning is Getting Quite Good

In the past few months, there have been a lot of unsupervised learning success
stories. The OpenAI results, the DeepMind results, the Microsoft results (I think?),
the Berkeley RL results, the contrastive learning results within our own group.

One of the reasons I was hesitant to believe AGI was coming soon was that I
wasn't sure dataset curation could keep up with dataset sizes. The big success
stories from 2015 came from large, labeled datasets. Those labels don't just
pop into existence from on high. They have to come from somewhere: specifically,
human labelers through Mechanical Turk and similar services. If ML needed
even larger labelled datasets, then you'd hit a problem where you just need
insane amounts of human supervision to push performance higher.

The reinforcement learning success stories did not need human labels.
They could succeed with a reward function stating what success *looked like*,
without needing to prescribe anything about how to get there. They were very
cool, but as I worked with it more, I got the impression they were working less
by understanding, and more by brute-forcing random exploration in an exponential
space until they stumbled upon a reward signal. This wasn't very scalable due
to the curse of dimensionality.
I expected this to
get solved by either learning a prior from several previous tasks (which would
take time to build), or from human demonstrations of the task (which would
require human labelers again.)

However, now that unsupervised learning is starting to get there, these challenges
could be going away soon. I'm not sure people appreciate the potential here.
What we've seen from GPT and AlphaStar is that at sufficient scale, it's okay
for your data to be messy. You'll have better results if you have the same
*quantity* of data, with better label accuracy, but because labels are not
things you are magically given, the size of your labeled dataset is limited
by the supervision you can pay for.

**Unsupervised learning matters because it lets you use larger datasets,
including ones that aren't even related to your target task.** Its main flaw
is that it hasn't worked very well in the past. The old folklore was that
unsupervised learning was cool, but [paying for labels was faster
and better](https://twitter.com/RichardSocher/status/840333380130553856).
Or in other words, the larger dataset didn't outweigh the inefficiency of
state-of-the-art unsupervised learning.

As this shifts, we may get a lot more "ImageNet moments" in several fields.
Informally, the "ImageNet moment" is the moment where everyone in computer
vision moved to using deep learning, and many papers
If this shifts, 

The difference is that unsupervised learning is actually starting to look very
good. I'm not sure people appreciate how big a deal this could be.



company
Meanwhile, for the
reinforcement learning successes, they 

For ML applications, the
common folklore is that clea
e
combination of dataset needs and curation needs.


OpenAI has been pushing how far giant Transformer architectures can go, and so
far the answer is "further than they've been pushed so far". They're getting
more coherent at language generation, which is their strong point, but have okay
results on music generation and image generation as well. Their music
generation and image generation is still weaker than other models, but whether they
are state-of-the-art isn't the point. What matters is the thesis that at
sufficient scale, a giant Transformer can handle different modalities without
completely failing.
