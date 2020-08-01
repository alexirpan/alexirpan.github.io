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

I had already decided to update my timeline estimates before GPT-3 was
announced. You have GPT-3 to thank for motivating me to actually write a blog
post about it.

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
if you can translate that task into a prompt of text to seed the model.
There are definitely flaws in the model, but the sheer breadth of tech demos
shown so far

However, it is one thing to have the theoretical
argument, and another thing to see tech demos showing the breadth of tasks that
are possible whe

you have a machine
that perfectly understands and answers all ques
that perfectly answers all questions

GPT-3 is a concrete example of both points 1 and 2, better tooling and better
unsupervised learning. There have been 
and better unsupervised learning.

post about it.
motivating me to write a blog post about
it.


announced,
Based on the 1st two points
I had already

OpenAI has been pushing how far giant Transformer architectures can go, and so
far the answer is "further than they've been pushed so far". They're getting
more coherent at language generation, which is their strong point, but have okay
results on music generation and image generation as well. Their music
generation and image generation is still weaker than other models, but whether they
are state-of-the-art isn't the point. What matters is the thesis that at
sufficient scale, a giant Transformer can handle different modalities without
completely failing.


CUT CONTENT

(From Section 1.)

Now, if you are basing your predictions by looking back on prior AI accomplishments,
finding the time between milestones, and estimating that curve forwards, then
you don't need to account for tools, because they are already priced into your
historical curve, and your extrapolation will implicitly continue to extrapolate
better tooling as well. However, I find this Kurzweil-style prediction deeply
unsatisfying, because it doesn't give a reason *why* the trendline should or
shouldn't continue. It simply asks you what you believe about it, and if you
don't believe in the model, then, well, that's it, there's nothing in the short
term that makes the model falsifiable. It's pretty easy to define a list of
historical milestones that fits a clean exponential if you cherry-pick the
milestones.
[Juergen Schmidhuber](https://www.reddit.com/r/MachineLearning/comments/2xcyrl/i_am_j%C3%BCrgen_schmidhuber_ama/cp47cf3/?context=8&depth=9) did this for fun in his Reddit AMA. He could have
just as easily cherry-picked other human accomplishments, to get a different
trendline that would be equally unfalsifiable. How would we choose? We can't.

If, historically, technological improvement is hard to predict, then 

has its flaws. You have
to decide what counts as a milestone and what doesn't, and it doesn't give any
actionable foothold by which you can prove or disprove the trendline. It
simply presents it and asks what you believe of it.
actionable evidence to 
not give arguments for why the curve should follow its trendline, besides "it
has in the paste

and you're implicitly assuming that they'll 


. Any improvement wi
While people are having better ideas,
there are places all over the stack where things are getting better as well.


and the At least within deep learning, the idea is a fairly small


