---
layout: post
title:  "My AI Timelines Have Sped Up"
date:   2020-06-19 15:06:00 -0700
---

(For this post, I'm going to take artificial general intelligence to mean
an AI system that matches or exceeds humans at economically valuable work.)

In 2015, I made the following forecasts about artificial general intelligence
(AGI).

* 10% chance by 2045
* 50% chance by 2050
* 90% chance by 2070

Now that it's 2020, I'm updating my forecast to:

* 10% chance by 2035
* 50% chance by 2045
* 90% chance by 2070

I'm keeping the 90% line the same, but shifting everything else to
be faster. Now, if you're looking for an argument of why I picked these particular
years, and why I shifted by 10 years instead of 5 or 15, you're going to be
disappointed. Both are driven by a gut feeling.
What's important is why parts of my thinking have changed - you can choose
your own timeline adjustment based on that.

Let's start with the easy part first.


I Should Have Been More Uncertain
-------------------------------------------------------------------------------

It would be incredibly weird if I was never surprised by ML research.
Historically, it's very hard to predict the trajectory a research field will
take, and if I were never surprised, I'd take that as a personal failing to
not consider large enough ideas.

At the same time, when I think back on the past 5 years, I believe I was
surprised more often than I expected. It wasn't all in a positive direction.
Unsupervised learning got better way faster than I expected, deep RL got better
a little faster than I expected, and transfer learning was slower than
expected. Combined, I've decided I should widen the distribution of outcomes,
so now I'm allocating 35 years to the 10%-90% interval instead of 25 years.

I also noticed that my 2015 prediction placed 10% to 50% in a 5 year range,
and 50% to 90% in a 20 year range. AGI is a long-tailed event, and there's
a real possibility it's never viable, but a 5-20 split is absurdly skewed.
I'm adjusting accordingly.

Now we're at the hard part. Why did I choose to shift the 10% and 50% lines
closer to present day?


I Didn't Account for Better Tools
----------------------------------------------------------------------------

Three years ago, I was talking to someone about AGI, and they mentioned
that [there was no fire alarm for AGI](https://intelligence.org/2017/10/13/fire-alarm/).
I told them I knew Eliezer Yudkowsky had written another post about AGI, and
I'd seen it shared among Facebook friends, but I hadn't gotten around to reading it.
They summarized it as, "It will never be obvious when AGI is going to occur.
Even a few years before it happens, it will be possible to argue AGI is far
away. By the time it's common knowledge that AI safety is the most
important problem in the world, it'll be too late."

And my reaction was, "okay, that's the same story I got from my Facebook
timeline. I already know the story of
Fermi predicting [a nuclear chain reaction was very likely
to be impossible](https://books.google.com/books?id=aSgFMMNQ6G4C&pg=PA813&lpg=PA813&dq=weart+fermi&source=bl&ots=Jy1pBOUL10&sig=c9wK_yLHbXZS_GFIv0K3bgpmE58&hl=en&sa=X&ved=0ahUKEwjNofKsisnWAhXGlFQKHbOSB1QQ6AEIKTAA#v=onepage&q=%22ten%20per%20cent%22&f=false), and even more recently we had
[Rémi Coulom state that superhuman Go was about 10 years away](https://www.wired.com/2014/05/the-world-of-computer-go/),
one year before [the first signs it could happen](https://arxiv.org/abs/1412.6564),
and two years before [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) made it official."
I decided it wasn't worth my time to read it.

I now need to retroactively complain to all my Facebook friends who only
discussed historical events and common knowledge. Although
that summary is *correct*, the ideas I found useful were all
*outside that summary*. I trusted you, filter bubble! How could you let me
down like this?

Part of the fire alarm post proposes hypotheses for why people claim AGI is
impossible. One of the hypotheses is that researchers pay too much attention
to the difficulty of getting something working with their current tools,
extrapolate that difficulty to future, and conclude they could never create
AGI.
This is a bad argument because your extrapolation needs to account for
research tools also improving over time.

What "tool" means is a bit vague,
but one example is feature engineering for computer vision. When was the
last time anyone talked about SIFT features for computer vision? Ages ago,
they're obsolute. But model tuning didn't disappear, it just turned into
CNN architecture tuning instead. SIFT features were the old tool,
convolutional neural nets are the new tool, and computer vision is the application
that's been supercharged by the better tool.

Whereas for me, I'm not a computer vision person. I think ML for control is a much
more interesting problem. However, you have to do computer vision to do control
in image-based environments, and if you want to handle the real-world, image-based
inputs are the most flexible input space. So for me, computer vision is the tool, robotics
is the application, and the improvements in computer vision have driven many
promising robot learning results.

I'm a big advocate for research tools. I think on average, people underestimate
their impact. So after reading that hypothesis that people don't forecast
tool improvement properly, I thought for a bit, and decided I hadn't properly
accounted for it either. That deserved shaving off a few years.

In the more empirical sides of ML, the obvious components of progress are your
ideas and computational budget, but there are less obvious ones too, like
your coding skills, debugging skills, and ability to utilize your compute.
It doesn't matter how many processors you have per machine, if your code doesn't
use all the processors available.
There are a surprising number of ML applications where the main value-add is
better data management and data summarization, rather than any learned model,
because those tools free up decision making time for the rest of the
research.

In general, everyone's research tools are deficient in some way.
Research is
about doing something new, which naturally leads to discovering new problems,
and it's highly unlikely someone's already made the perfect tool for a problem
that didn't exist 3 months ago. So, your current
research tools will *always* feel janky, and you shouldn't be using that to
argue anything about timelines.

Improvements continually happen across the entire research stack, and most of
these improvments have multiplicative benefits. Multiplicative factors
can be very powerful.
One simple example is that to get 10x better results, you can either make one
thing with a 10x better paradigm shift, or you can make ten different things
[1.26x better](https://www.google.com/search?&q=1.26^10), and they'll combine to
a 10x total improvement. The latter is just as transformative, but can be much
easier, especially if you get 10 experts with different skill sets
to work together on a common goal. This is how corporations become a thing.


Semi-Supervised and Unsupervised Learning are Getting Better
-------------------------------------------------------------------------------

I have been pretty impressed with semi-supervised and unsupervised learning progress in the
past few months. Momentum Contrast from [He et al, CVPR 2020](https://arxiv.org/abs/1911.05722)
was quite nice, SimCLR from [(Chen et al, ICML 2020)](https://arxiv.org/abs/2002.05709) improved
on that, and Bootstrap Your Own Latent [(Grill, Strub, Altché, Tallec, Richemond et al, 2020)](https://arxiv.org/abs/2006.07733)
has improved on that. And then there's [GPT-3](https://arxiv.org/abs/2005.14165),
but I'll get to that later.

Unsupervised learning has historically been in this weird position where it is
obviously the right way to do learning, and also a complete waste of time if
you want something to work now.
On the one hand, humans don't have labels for most things they learn,
so ML systems shouldn't need labels either. On the other hand, the
deep learning boom of 2015 was mostly powered by supervised learning on
large, labeled datasets.
Richard Socher had a notable tweet at the time:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Rather than spending a month figuring out an unsupervised machine learning problem, just label some data for a week and train a classifier.</p>&mdash; Richard Socher (@RichardSocher) <a href="https://twitter.com/RichardSocher/status/840333380130553856?ref_src=twsrc%5Etfw">March 10, 2017</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Not to say that unsupervised learning was never useful. Even in 2010, it was
common wisdom that deep networks should go through an unsupervised pre-training
step before starting supervised learning. See [(Erhan et al, JMLR 2010)](https://jmlr.csail.mit.edu/papers/volume11/erhan10a/erhan10a.pdf).
Self-supervised word vectors like [GloVe](https://nlp.stanford.edu/projects/glove/)
and [word2vec](https://en.wikipedia.org/wiki/Word2vec) were also doing
interesting things around 2015. These felt like exceptions to the rule, and I held ImageNet
features as the main example of general behavior - and those features were
learnt through labeled classification.

When I was thinking through what made ML hard, the trendlines were pointing to larger
models and larger labeled datasets. They're still pointing that way now.
I concluded that future ML progress would be bottlenecked by labeling requirements.
Defining a 10x bigger model is easy. *Training* a 10x bigger model is harder, but
it doesn't need 10x as many people to work on it. Getting 10x as many labels
does. And yes, data labeling tools are getting better, and there are even
startups whose missions are to provide fast data labeling as a service.
But labels are fundamentally
a question about human preferences, and that makes it hard to escape human
labor.

Reward functions in reinforcement learning have a similar issue. In principle, the model
figures out a solution after you define what success looks like. In practice, you need
a human to check the model isn't hacking the reward, or your reward function
is implicitly defined by human raters, which just turns into the same labeling
problem.

Large labeled datasets don't appear out of nowhere. They take deliberate,
sustained effort to generate. There's a reason [ImageNet won the Test of Time
award at CVPR 2019](https://www.computer.org/publications/tech-news/events/ieee-cvpr-conference-on-computer-vision-and-pattern-recognition-2019-awards-records) -
the authors of that paper went out and did the work.
If ML needed
ever larger labelled datasets to push performance, and models kept growing
by orders of magnitude, then you'd hit a point where the amount of human
supervision needed to make progress would be insane.

(This isn't even getting into the problem of labels being imperfect. We've
found that a lot of labeled datasets carry lots of bias within them. That
isn't surprising, but now that it's closer to common knowledge,
a laissez-faire labeling system isn't going to fly anymore.)

Okay. Well, if 10x labels is a problem, are there ways around that problem?
One way is if you don't need 10x as many labels.
It turns out that's true, at least according to
[(Hestness et al, 2017)](https://arxiv.org/abs/1712.00409), which found that
image classification models have followed a trendline of "$$N$$ parameters,
$$N^{0.57}$$ examples", Up to constant factors.
So a 10x larger model doesn't need 10x as many labels, it just needs 3.7x as
many labels. That's certainly better, but a 3.7x factor for every order
of magnitude you want to scale still felt like a lot...

Enter unsupervised learning. These labelling challenges are getting a lot
easier, because what "label" means is starting to shift to something easier
to obtain.
At sufficient scale, it's looking like its okay for your labels to noisy and
your data to be messy.
I'm not sure people appreciate the potential here. If you have $$N$$
unsupervised examples, then yes, $$N$$ labeled examples will be better,
but remember that labels take effort -
the size of your labeled dataset is limited by the supervision you can afford,
and you can get much more unlabeled data for the same amount of effort.
The scaling numbers for unsupervised language modelling from
[(Kaplan and Candlish, 2020)](https://arxiv.org/abs/2001.08361) suggest a
$$N^{0.74}$$ relationship, or 5.5x as much data per order of magnitude, but
since that data is much easier to obtain, it's less effort than the 3.7x
factor above.

A lot of Big Data hype was driven by plots showing data was getting created
faster than Moore's Law. Much of the hype fizzled out because uninformed
executives didn't understand that having data is not the same as having *useful*
data for machine learning.
The true amount of usable data was much smaller
than at first glance. The research community had a big laugh, but the joke will
be on us if unsupervised learning gets better and even junk data becomes marginally useful.

Is unsupervised learning there already? Definitely not. 100% not. It *is* closer than
I expected it to be. I expect to see more papers use data sources that aren't
relevant to their target task, and more "ImageNet moments" where applications
are built by standing on the shoulders of someone else's GPU time.


GPT-3 Results are Qualitatively Better than I Expected
-------------------------------------------------------------------------------

I had already updated my timeline estimates before people started toying
with GPT-3, but GPT-3 was what motivated me to write this blog post explaining why.

What we're seeing with GPT-3 is that language is an incredibly flexible input
space. People have known this for a while. I know an NLP professor who
said language understanding is an AI-Complete task, because a hypothetical
machine that perfectly understands and replies to all questions might as well
be the same as a person. People have also argued that compression is a proxy
for intelligence.
As argued on the [Hutter Prize](http://prize.hutter1.net/) website, to compress
data, you must understand patterns in that data, and if you view pattern recognition
as a key component of intelligence, then better compressors should be more
intelligent.

It is one thing to have the theoretical arguments. It is another thing to see
it happen for real. GPT-3 is many things, but its core is a system that uses lots of
training time to compress a very large corpus of text into a smaller set of
Transformer weights. The end result demonstrates a surpisingly wide breadth
of knowledge that can be narrowed into many different tasks, as long as
you can turn that task into a prompt of text to seed the model's output. It
definitely has flaws, but the sheer breadth of tech demos people have shared is kind of
absurd.
It's also remarkable that most of this behavior is
emergent from getting good at predicting the next token of text.

GPT-3 is a concrete example of the previous section (better unsupervised learning)
and it's a sign of the first section (better tooling).
Although there's a lot of fun stuff in story generation, I'm most interested
in the [code generation demonstrations](https://twitter.com/sharifshameem/status/1282676454690451457).
They look like early signs of a "Do What I Mean" programming interface.
If the existing tech demos could be made 5x better, I wouldn't be surprised if
they become critical productivity boosters for nuts-and-bolts programming.
Systems design and debugging will likely stick to humans, but a lot of
programming is just coloring inside the lines. Even low levels of capability
could be a game changer, in the same way as pre-2000 search engines.
(For reference: [AltaVista](https://en.wikipedia.org/wiki/AltaVista) was the
11th most visited website in 1998, and it's certainly worse than what
Google/Bing/DuckDuckGo can do now.)

One specific way I could see code generation being useful is for ML for ML
efforts, like
neural architecture search and black-box hyperparamter optimization. One of
the common arguments around AGI is intelligence explosion, and that class
of black-box methods has been viewed as a potential intelligence explosion mechanism.
However, they've long had a key limitation: even if you assume infinite
compute, someone has to implement
the code that provides a clean API from experiment parameters
to final performance. The explorable search space is fundamentally
limited by what dimensions of the search space humans think of. If you don't
envision part of the search space, machine learning can't explore it.

Domain randomization
in robot learning has the same problem.
This was my
main criticism of the [OpenAI Rubik's Cube result]({% post_url 2019-10-30-openai-rubiks %}) -
the paper read like a year long discovery of the Rubik's Cube
domain randomization search space, rather than any generalizable robot
learning lesson. The end result is based on a model exploring
randomly generated simulations, but it only got there because of lots of effort
determining which randomizations were worth implementing.

Now imagine that whenever you discovered a new unknown unknown, you could
very quickly implement the code changes that add that dimension to the search
space. Well, those methods sure look more promising!

There are certainly problems with GPT-3. It has a fixed attention
window, it doesn't have a way to learn anything it doesn't already know, and
determining what it does know requires learning how to prompt GPT-3 to give
the outputs you want. But, again, this reminds me a lot of early search engines.
As a kid, I was
taught ways to structure my search queries to make good results appear more
often. Avoid short words, place important key words first, don't enter full
sentences, etc. We dealt with it because the gains were worth it. GPT-3 feels
similar.

I don't know where this leads, but there's *something* here.


I Now Expect Compute to Play a Larger Role, and See Room for Models to Grow
------------------------------------------------------------------------------

For reasons I don't want to get into in this post, I don't like arguments where
people make up a compute estimate of the human brain, take a Moore's Law curve,
extrapolate the two out, and declare that AGI will happen when the two curves
intersect. I believe they oversimplify the discussion.

However, it's undeniable that compute plays a role in ML progress. But how much
are AI capabilities driven by scaling up existing models, and how much is driven
by new ML ideas? In 2015, my guess was that 50% of AGI progress would come from
compute and 50% would come from better algorithms. There were several things
missing between 2015 models, and something that put the "general" in
artificial general intelligence. I was not convinced more compute would fix that.

Since then, there have been many successes powered by scaling up models, and I
now think the balance is more like 65% compute, 35% algorithms. I suspect that
many human-like learning behaviors could just be emergent properties of larger
models. I also suspect that many things humans view as
"intelligent" or "intentional" are neither. We just want to think we're
intelligent and intentional. We're not, and the bar ML models need to cross is
not as high as we think. That speeds up timelines, because ML ideas are bottlenecked
by the size of the ML community, whereas faster hardware is powered by
worldwide consumer demand.

Let's go back to GPT-3 for a moment. GPT-3 is not the largest Transformer
you could build, and there are reasons to build a larger one.
If the performance of large Transformers scaled for 2 orders of magnitude
(1.5B params for GPT-2, 175B params for GPT-3), then it wouldn't be too weird
if they scaled for another 2 orders of magnitude. Of course, it might not,
but I don't see a good argument why it shouldn't. Such a 100x model could
once again have qualitative differences in behavior.

There's certainly enough data for this.
Focusing on GPT-3's text generation is missing the main plot thread.
If you believe [the rumors](https://www.technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality/),
OpenAI has been working towards large scale multi-modal learning. So far, their
research output is consistent with that.
[MuseNet](https://openai.com/blog/musenet/) was a generative model for
audio, based on large transformers. More recently, [Image GPT](https://openai.com/blog/image-gpt/)
was a generative model for images, also based on large transformers.

Was MuseNet state-of-the-art at audio synthesis when it came out? No. Is Image-GPT state-of-the-art
for image generation? Also no. Models with more inductive priors did better
than both.
However, these questions miss the point OpenAI is making:
*a large enough Transformer is not state-of-the-art, but it does well enough
on these very different data formats.* By default I assume it's hard
to learn across multimodal inputs, but processing audio + image + text
simultanenously should be easier if it all goes through a similar neural net
architecture. It helps that OpenAI can leverage any intuition they already have
about very large Transformers. Once you add in other data streams, there should
definitely be enough data to train much larger unsupervised models, assuming
scaling laws hold up.

Are large Transformers the last model architecture we'll use? No, probably not.
But I do see room for them to do more than they've done so far.
Model architectures are only
going to get better, so the capabilities of scaling up current models must be
a lower bound on what could be possible 10 or 20 years from now - and what looks
possible right now is already interesting and slightly worrying.


The Big Picture
----------------------------------------------------------------------------

In ["You and Your Research"](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html),
Richard Hamming has a famous piece of advice: "what are the important problems
in your field, and why aren't you working on them?" Surely AGI is one of the
most important problems for machine learning.

So, for machine learning, the natural version of this question is, "what
problems need to be solved to get to artificial general intelligence?" What
waypoints do you expect the field to hit on the road to get there, and how
much uncertainty is there about the path between those waypoints?

I feel like more of those waypoints are coming into focus.
If you asked 2015-me how we'd build AGI, I'd tell you I have no earthly idea.
I didn't feel like we had meaningful in-roads on any of the challenges I'd
associate with human-level intelligence.
If you ask 2020-me how we'd build AGI, I still see a lot of gaps, but I have
*some* idea how it could happen, assuming you get lucky. That feels like the
biggest shift.

Assuming AGI is possible without many more new ideas (and that's a big
assumption), here is one way it could happen:
someone eventually develops an app so useful that
models of GPT-3's size or larger are huge productivity multipliers. Imagine
the first computers, or Lotus Notes, or Microsoft Excel taking over the
business world.
It's valuable enough that the economics actually work out, and people are
willing to pay enough to cover the inference costs and turn a profit.
That funds buying more hardware, which enables even larger training runs.
As we've seen with cloud computing, you buy excess hardware to anticipate spikes in
consumer demand, but can then sell access to the extra hardware to earn money -
except in this scenario, instead of a cloud computing service, you just give
the excess compute capacity to research.

Meanwhile, cross-modality learning turns out to be easier than expected at scale,
and we discover similar emergent properties. Object tracking and intuitive
physics turn out to be naturally occuring phenemenon that are learnable just
from images, without direct environment interaction. With more tweaks, even
larger models, and even more data, you end up with a rich feature space for
images, text, and audio. It quickly becomes unthinkable to train anything from
scratch. Why would you? Much of the prior work in several fields gets obsoleted,
going the way of
[SIFT features](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)
for vision, [parse trees](https://en.wikipedia.org/wiki/Parse_tree) for
machine translation, and
[phoneme decoding steps](https://en.wikipedia.org/wiki/Phoneme) for speech
recognition. People who don't know any of those techniques are working on
neural nets that solve the task anyways, and that's faintly sad, but it is what
it is.

As models grow larger, and continue to demonstrate improved performance,
research coalesces around a small pool of methods that have been shown to scale
with compute. That's still happening with deep learning. When lots of fields
use the same set of techniques, you get more knowledge sharing and that
drives better research. CNNs have heavy priors towards considering nearby
values, were first useful for image recognition, but now have implications for
genomics and music generation. Transformers are a sequence model that first
happened for language modelling, but can also be applied to video understanding.
That trend is likely to continue.

At that point, what sensor inputs do humans have, that this hypothetical model
doesn't? I believe it's mostly the sensors tied to physical embodiment,
like taste, touch, and smell. I think it's entirely plausible that intelligence
doesn't require any of that. That starts looking eerily close to AGI to me.

There's a lot that has to go right for that path to work. You need multimodal
learning to be easier than expected. You need to continue to have more behaviors
emerge out of scaling, because your researcher time is primarily going into
ideas that help you scale. Hardware has to match pace, which includes funding,
energy usage, and maintenance. The scaling hypothesis has to keep being true,
and unsupervised learning has to keep performing better.

The most likely issue I see is if unsupervised learning is harder for domains
besides language. In 2015, unsupervised learning was given word vectors for
text, and nothing at that level for images. Perhaps the compositional properties
of language make it well suited to unsupervised learning, in a way that isn't
as true for image data. In other words, I may be overestimating research by
only looking at problems where it's more likely to succeed.

I entirely expect something to go wrong in the research agenda. That's why I'm
only adjusting my estimates by a few years. But so far, I have mostly seen reasons
to speed up my estimates, rather than slow them down.
