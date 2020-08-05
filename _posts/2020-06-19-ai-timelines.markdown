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

But, you aren't here for that. You're here to learn why I shifted everything
up a few years. Below is the list of things that made me Change My Mind.


1. I Didn't Account for Better Tools

Three years ago, I was talking to someone about AGI, and they mentioned
that [there was no fire alarm for AGI](https://intelligence.org/2017/10/13/fire-alarm/).
I told them I knew Eliezer Yudkowsky had written a post, but I hadn't gotten
around to reading it. They summarized it as, "it will never be obvious when
AGI is going to occur, and there will never be a point where everyone in ML
knows that AI safety is the most important thing to work on." And my reaction
was, "Yes, I've heard the stories of people predicting chess AIs would
never exist, Fermi predicting [a nuclear chain reaction was very likely
to be impossible](https://books.google.com/books?id=aSgFMMNQ6G4C&pg=PA813&lpg=PA813&dq=weart+fermi&source=bl&ots=Jy1pBOUL10&sig=c9wK_yLHbXZS_GFIv0K3bgpmE58&hl=en&sa=X&ved=0ahUKEwjNofKsisnWAhXGlFQKHbOSB1QQ6AEIKTAA#v=onepage&q=%22ten%20per%20cent%22&f=false), and even more recently we had
[Rémi Coulom state that superhuman Go-players was about 10 years away](https://www.wired.com/2014/05/the-world-of-computer-go/), two years before AlphaGo beat Lee SeDol 4-1."
The historical lesson is that nobody's long-term prediction is very good. I
decided it wasn't worth my time to read it.

I got around to reading it, and although that summary is *correct*, the ideas
that were new to me were in everything outside that summary. The historical
references, discussions of common knowledge, and forecasting discussion was
old. But the useful part was where Eliezer Yudkowsky proposed guesses for
why people predict AGI is impossible. One of his guesses was that researchers
extrapolated what could be done with their current tools in N years, and they
decided their current tools could never create AGI.

This is incorrect, because research tools are also improving over time, and your
extrapolation needs to account for that.
I'm a big advocate for research tools - I think on average people underestimate
their impact. In the more empirical sides of ML, the obvious factors of progress
are your ideas and computational budget. The less obvious ones are what libraries
you use, your software engineering and debugging skills, how you manage data,
and how efficiently you can use the computational budget you do have. I'm sure
I'm missing some more factors as well.

Improvements are continually happening across this entire stack, their impact
is roughly multiplicative, and on reflection, my gut predictions did not account
for this as much as it should have. Multiplicative factors are very powerful:
one simple example is that to get 10x better results, you can either make one
thing 10x better, or you make ten things [26% better](https://www.google.com/search?&q=1.26^10).
The latter is much easier, especially if you get 10 people who are each good
at a different part of the stack to work together on a common goal. (This is
how corporations get created.)


2. Semi-Supervised and Unsupervised Learning is Getting Better

I have been pretty impressed with the semi-supervised and unsupervised learning progress in the
past few months. Momentum Contrast from [He et al, CVPR 2020](https://arxiv.org/abs/1911.05722)
did pretty good, SimCLR from [(Chen et al, ICML 2020)](https://arxiv.org/abs/2002.05709) improved
on that, and Bootstrap Your Own Latent [(Grill, Strub, Altché, Tallec, Richemond et al, 2020)](https://arxiv.org/abs/2006.07733)
has improved on that. And then there's [GPT-3](https://arxiv.org/abs/2005.14165),
but I'll get to that later.

In 2015, the deep learning boom was mostly powered by supervised learning on
large, labeled datasets. Meanwhile, self-supervised and unsupervised learning
were sort of working, but not
in a meaningful way. Richard Socher had a notable tweet at the time:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Rather than spending a month figuring out an unsupervised machine learning problem, just label some data for a week and train a classifier.</p>&mdash; Richard Socher (@RichardSocher) <a href="https://twitter.com/RichardSocher/status/840333380130553856?ref_src=twsrc%5Etfw">March 10, 2017</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Of course, unsupervised learning was the right way to do learning. Humans
don't have labels for most things they learn how to do, they just get their
eyes and ears and have to figure it out. But, well, the main example of general
behavior at the time was from ImageNet features, learned through labeled
classification. (Admittedly, self-supervised word vectors like GloVe and
word2vec were doing interesting things around the same time.)

When I combined this with the scaling laws observed by
[(Hestness et al, 2017)](https://arxiv.org/abs/1712.00409), I concluded that
ML progress would be bottlenecked the most by labeling requirements. Let's take
the scaling law numbers from
[(Kaplan and Candlish, 2020)](https://arxiv.org/abs/2001.08361) as an example.
They find that for language modelling, performance follows a power law in the
number of parameters $$N$$, and then saturating that model requires a dataset of
size proportional to $$N^{0.74}$$. Now of course, this is just language modelling,
and you don't need to saturate model performance, but the trendline is that your
dataset size follows a power law relationship, and if that data needs to be
labelled, you're going to have a bad time. Making a 10x bigger model doesn't
require 10x as many people to work on it. Getting 10x as many human labels for
a task does. There are fewer ways for software to speed up labelling speed.

Large labeled datasets don't just appear out of nowhere. They take deliberate,
sustained effort to generate. There's a reason ImageNet won the Test of Time
award at CVPR 2019. Silicon gets faster, changing numbers in code lets you
affect the entire model with a few keystrokes, but human labels eventually
have to come from somewhere: specifically, human labelers hired through
Mechanical Turk and similar services.
If ML needed
ever larger labelled datasets to push performance, then you'd hit a problem
where you'd just need
insane amounts of human supervision to make more progress.

As for reinforcement learning, although they did not need human labels, they
did need reward functions. As I worked with RL more, I got the impression they
were working less by understanding, and more by brute-forcing random exploration
in an exponential space until they stumbled upon a reward signal, which wasn't
very scalable due to the curse of dimensionality. To fix this, I expected
that you'd either need to learn a prior from previous tasks (which is effectively
unsupervised learning with extra steps), or you need human demonstrations (which
requires human labelers agains). And this isn't even getting into defining the
reward functions, which will likely also need to be learned from human labels
after you pass the threshold of easy tasks most people work with right now.

However, now that unsupervised learning is starting to get there, these challenges
are getting a lot easier. I'm not sure people appreciate the potential here.
At sufficient scale, it looks okay for your data to be messy. You'll have better
results if you have the same quantity of labeled data, but because labels are
not thing you are magically given, the size of your labeled dataset is limited by
the supervision you can afford.

That core idea is the key: better unsupervised learning makes it easier to use
larger datasets, including data that doesn't even look relevant to your target
task, and as that gets better, I expect to see more "ImageNet moments", where
most applications are solved by tuning pretrained models instead of training
from scratch.


3. GPT-3 Results are Qualitatively Better than I Expected

I had already updated my timeline estimates before people started toying
with GPT-3, but GPT-3 was what motivated me to write a blog post explaining why.

What we're seeing with GPT-3 is that language is an incredibly flexible input
space. People have known this for a while. I know that NLP researchers like to
say language understanding is an AI-Complete task, because a hypothetical
machine that perfectly understands and replies to all questions might as well
be the same as a person. People have also argued that compression is a proxy
for intelligence. Compressing data requires understanding patterns in that data,
and if you accept that pattern recognition is a key component of intelligence, then
a better compressor should be more intelligent. (This is the thesis behind
the [Hutter Prize](http://prize.hutter1.net/).)

It is one thing to have the theoretical arguments. It is another thing to see
it happen for real. Because what is GPT-3? It's a system that uses lots of
training time to compress a very large corpus of text into a smaller set of
Transformer weights, and the end result is able to do a wide variety of tasks
if you can turn that task into a prompt of text to seed the model. Those tasks
include translation, summarization, generating simple React UIs and functions
from documentation, Q&A sessions, and so on. (REMEMBER TO ADD LINKS TO EXAMPLES.)
There are definitely flaws in thes
model, but the sheer breadth of tech demos is kind of absurd.

GPT-3 is a concrete example of both points 1 and 2, better tooling and better
unsupervised learning. The code generation demonstrations are especially interesting
to me, since they look like early signs of a "Do What I Mean" programming tool.
IDEs currently handle a lot of the grunt work, but if the existing tech demos
could be made 5x better, I wouldn't be surprised if they become critical
productivity boosters for nuts-and-bolts programming. Systems design and
debugging will likely stick to humans, but a lot of programming is just
coloring inside the lines. Even a simple do-what-I-mean tool should be a big
boon. And overall, it's pretty remarkable that most of this behavior is
emergent from getting good at predicting the next character of text a human would
write.

There's currently no way for the prompt-based GPT-3 to learn anything it hasn't
seen before, but if it's seen a massive crawl of the Internet, that might not
be that big of a problem...


4. It's Clear There's Still Room for Larger Models

One of the common proxies people use when reasoning about AGI is the availability
of compute resources. They play an undeniable role in ML progress, but how much
can be done from scaling up existing model architectures, without other ideas?

In 2015, I was not convinced that compute would fix everything. Models were
getting better, but only at simple tasks. As Andrew Ng put it, "a good approximation
is that machine learning can do most things a human can do in 1 second". There
were several things missing between 2015
models, and something that put the "general" in artificial general intelligence.
Compute would help fix that, but of the remaining AGI progress, I guessed 50%
would come from compute, and 50% would come from algorithms and ideas.

In the years since then, there have been lots of successes powered by scaling
fairly simple models to larger datasets. I've since been convinced that compute
will play a larger role, and that many human-like learning behaviors could just
be emergent properties of larger models. I'm now guessing about 65% compute
and 35% algorithms for the split between the two.

If you are not sold on this, let's go back to GPT-3 for a moment. At minimum,
we haven't seen the limits of GPT-3 scaling yet. If the performance of large
Transformers has scaled for 3 orders of magnitude (1 billion params to 175
billion params), then it wouldn't be too weird if they scaled for another 3
orders of magnitude. Of course, it might not - but is there a good argument
why it shouldn't? And 3 orders of magnitude was enough to drive more coherent
text generation, better long-term dependencies, and new kinds of tasks, like
rudimentary code generation.

Presumably, the
aim is to take streams of audio, video, and text, shove them all into a single
model, and see what happens. And for a while, my reaction was, "Cool, but that's
much easier said than done." Multimodal learning has historically been a tricky
problem.

Additionally, the focus on GPT-3's text generation is missing the real plot
thread.
If you believe [the rumors](https://www.technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality/),
OpenAI has been working on large scale, multi-modal learning. Much of the recent
work OpenAI has put out is consistent with this.
There was [MuseNet](https://openai.com/blog/musenet/), a generative model for
audio based on large transformers. More recently, there was [Image GPT](https://openai.com/blog/image-gpt/),
a generative model for images also based on large transformers.

ML techniques have become increasingly general, and employees at OpenAI see
this as a big deal. (They have said as much [when I criticized their decision
to discuss their robotics research at a DotA 2 event](https://twitter.com/jackclarkSF/status/1026813527850450944).)
Why does this matter?

Consider the state of machine learning before deep learning started taking
over several fields. Computer vision models were based on [SIFT features](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform).
Machine translation was based on [parse trees](https://en.wikipedia.org/wiki/Parse_tree).
Speech recognition was based on recognizing [phonemes](https://en.wikipedia.org/wiki/Phoneme)
and composing them together.

I'll be honest - I have very little experience with any of the 3 things I just
linked. But I could still start work in any of those fields today? Why? Because
state-of-the-art models for all three have been taken over by neural nets, and
I understand neural nets.

This is one of the deep learning trends that people didn't appreciate at the time.
When lots of fields converge to using the same set of techniques, it's easier
for people across fields to share progress and ideas. A convolutional neural
net is a model with a heavy prior towards considering nearby values. That's good
for image recognition, but ended up having implications for genomics and music
generation. A transformer is a sequence model, which is good for understanding
language, but also can be applied to video understanding.

You can't entirely ignore prior work or experience. Intuition in the target
domain can be very powerful. AlphaGo was a victory for
CNNs and RL, but it was developed by people who had been working on Computer Go
for years, with the consulting help of pro-level Go players. However, much
of the intuition for how *neural nets* work can be carried over between projects,
and that's very useful.


Story for how AGI happens.

Expanded capabilities of research-level ML drives demands for more hardware
to enable large-scle inference of those models. (Have seen this already for
TPUs for image recognition and speech recognition).

Excess capacity leftover is used to drive new research (there is some OpenAI
post that makes this argument too.)

We scale up transformers, or other better model architectures, to be of larger
size. These transformers are not just trained on text. They are also trained
on audio and video, and we've seen that transformers are able to handle these
inputs as well.

Somewhere in here, it is important to emphasize that transformers are worse
than other generative models for images, and MuseNet was worse than other
more dedicated audio generation models, but the important part here is that
the architecture can handle it *well enough* that compute massages the
difficulties. It also means that improvements to transformers improve the
processing of all modalities, in the same way that improvements to CNN
training have implications for any spatial recognition task.

Once these models are trained on text, audio, and images, if this works
better than expected, if fewer unexpected issues show up, then the dataset
size is much bigger. There should be old industry slide decks for Big Data,
talking about how Big Data scales bigger than Moore's law, and the classic
problem with those slide decks is that they never explained how to use
the data effectively. Historically, targeted, well-designed data extraction
has been necessary to get good performance, but unstructured data is
everywhere.

And then, if it's handling audio, images, and text, then pretty much the
only sensor modality you're missing from humans is touch sensing and
embodiment in the world.


One of the common arguments around AGI is intelligence explosion - that a
more capable system will be able to improve itself faster, which will let it
improve itself even faster than before, and so on. Machine learning is in
many ways the field of automating decision making, and people have been trying
to apply ML to ML for years, most recently with neural architecture search
and black-box hyperparameter optimization.

These approaches have long had a key limitation: someone must implement the
code that enables a clean API between requested hyperparameter or model
architecture, to implemented model, to final performance, and the search
space you can explore is fundamentally limited by what search space humans
feel are important. In robot learning, sim-to-real transfer via domain
randomization has the same problem.

Approaches like neural architecture search and black-box
optimization of hyperparameters have long tried to automate more of the ML
iteration process, but one of their key limitations is that someone must
implement all the code that provides a clean API from "hyperparam / model architecture",
to the actual model, to the final performance. Simulator randomizations for
sim-to-real robot learning has a similar limitation - at a certain point,
simulators are cheap enough that you aren't bottlenecked on how many sims you
can run. You're bottlenecked by whether you have implemented all possible paths
you want the model to explore. Your architecture search can't try dropout if
you haven't implemented dropout as an option. It can't try layer norm or
instance norm instead of batch norm if you haven't added that as a configurable.
And so on.



OpenAI has been pushing how far giant Transformer architectures can go, and so
far the answer is "further than they've been pushed so far". They're getting
more coherent at language generation, which is their strong point, but have okay
results on music generation and image generation as well. Their music
generation and image generation is still weaker than other models, but whether they
are state-of-the-art isn't the point. What matters is the thesis that at
sufficient scale, a giant Transformer can handle different modalities without
completely failing.
