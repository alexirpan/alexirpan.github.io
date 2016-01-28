---
layout: post
title:  "Go: More Complicated than Go Fish"
date:   2016-01-27 23:08:00 -0800
---

*As something "hot off the presses", this may lack polish.*

Yesterday, Google DeepMind announced an expert level Go AI. Blog post announcement
[here](http://googleresearch.blogspot.com/2016/01/alphago-mastering-ancient-game-of-go.html),
and Nature paper [here](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html).


It got picked up by, well, almost everybody. See:
[MIT Technology Review](http://www.technologyreview.com/news/546066/googles-ai-masters-the-game-of-go-a-decade-earlier-than-expected/),
[Wired](http://www.wired.com/2016/01/in-a-huge-breakthrough-googles-ai-beats-a-top-player-at-the-game-of-go/),
[Ars Technica](http://arstechnica.com/gadgets/2016/01/googles-ai-beats-go-champion-will-now-take-on-best-player-in-the-world/),
[The New York Times](http://bits.blogs.nytimes.com/2016/01/27/alphabet-program-beats-the-european-human-go-champion/),
and others I don't have the patience to catalogue.
It's been filling my Facebook news feed all day.

Although computer Go isn't one of my interests,
Monte Carlo Tree Search (MCTS) is. The biggest application of MCTS is in
computer Go, and when you spend two semesters researching MCTS, you end up
reading a few computer Go papers too.


After downloading and reading the Nature paper, I've revised my opinion.
Their result still isn't that surprising, but it's even more impressive
than it sounds, and their combination of several AI approaches has a lot
of potential.


Prior Work
--------------------------------------------------------------------------

My first reaction was that AlphaGo was very impressive, but not that
surprising.

This is at odds with some of the reporting. The original blog post says

> Experts predicted it would be at least another 10 years until a computer
> could beat one of the world’s elite group of Go professionals.

The MIT Technology Review repeats this with

> Google’s AI Masters the Game of Go a Decade Earlier Than Expected

Wired has an actual quote.

> “It happened faster than I thought,” says Rémi Coulom, the French researcher
> behind what was previously the world’s top artificially intelligent Go player.

I entirely understand why it sounds like this result came out of nowhere,
but it didn't. Giant leaps are very rare in research. For big problems like
Computer Go, it's more like a dam. At first, the problem is a big unapproachable
wall. Over the years, people make incremental progress, chipping away bit by bit.
This works in a special case. This gets to amateur level play. This doesn't
get all the way there, but pushing in this direction could work.
Eventually, all the right ideas collect by the dam's side, some group puts
the pieces together in the right way, and finally breaks through.

Then reporters only talks about the final breakthrough and it
sounds like complete magic.

This isn't a dig at science reporters. I don't think there's a way around this,
because you have to be steeped in the culture of that research field to see
the signs. Even then, you could be wrong. I'm sure there are plenty of smart
professors who were (and maybe still are) pessimistic on neural nets and
optimistic on SAT solvers. It's very time consuming (and less attention
grabbing) to look for the prior work that built to the newest paper.

Back to Go. The reason I wasn't surprised was because I [read DeepMind's
first Go paper when it went on ArXiv in December 2014](http://arxiv.org/abs/1412.6564).
(Incidentally, [Clark and Storkey](http://arxiv.org/abs/1412.3409)
independently released a similar paper just 10 days earlier.
The day before Google announced AlphaGo's Nature paper, people from
Facebook AI Research [released a new preprint](http://arxiv.org/abs/1511.06410)
for their work. Seems like the old maxim holds true: if no one else is trying
the same thing, it's a bad sign.)

Before this paper, the best approach was Monte Carlo Tree
Search. In MCTS, the algorithm evaluates board positions by playing many random
games, or rollouts. It incrementally builds a search tree, using previous
results to focus the search on promising moves. Past progress came from tweaking
how rollouts were generated. A stronger rollout player gives better results,
but because MCTS runs hundreds of thousands of rollouts, the rollout method
needs to be very fast.

What made DeepMind's first paper so impressive was that it worked without
using any search at all. Pass in the board, wait a few milliseconds, return a move.
Compared to the 5 second search time other programs used, it was insane that
they could get a decent
Go program. The approach was simple. Using supervised learning, train a
convolutional neural net to predict the next move the expert makes.
That's it.
With a big enough CNN, they got to 55% accuracy, which beat all prior
move predictors.

At the end of their 2014 paper, there's a short section on combinining
their CNN with search. They didn't get very far, besides showing that it was
an obviously good idea if it could be made computationally feasible.

Ever since that paper, it's felt like the last thing Computer Go needed was a
way to combine heavy duty neural net move predictors with MCTS in a clever
way that doesn't make computation time explode.

With AlphaGo, that's finally happened. So no, it's not surprising that this
happened so quickly. There was a clear roadmap of what needed to be done,
and people took it.

To be fair to Rémi Coulom, his quoted remarks came before DeepMind's preprint
was sent to the computer-go mailing list. I'm sure he's been following
this closely, and it's an unfortunate citation without context.

If anything's surprising, it's that they pushed their preprint to AlphaGo
within a year. I would have guessed 2 years.


The New Stuff
---------------------------------------------------------------------------

I know I've been a bit down on this result, but I don't want that to fool
anybody. This is an exceptionally impressive result, and the approaches used
to integrate search are very interesting. If you have access, I highly
recommend reading the paper on your own. It's well
written, and the authors kept the main text as jargon-free as possible.

If you don't have access, here's the quick summary.

* Using the supervised dataset of expert level games. they train
two networks. One is a small rollout network, used in random games for MCTS.
The other is a large CNN, similar to the Dec 2014 paper. This is called
the policy network.
  * The rollout network is very small because it will be run millions of times.
* The policy network is further refined through self-play and reinforcement
learning. (The paper calls this the RL policy network.)
* Finally, they train a value network, which predicts the value of a board
if both players play according to the refined network.
  * The value network gives an approximation of what MCTS with the refined
  network would return. It's an approximation, but it's thousands of times
  faster.

The first part that piqued my interest was how many networks were trained
for AlphaGo. Each network was trained for a different subtask in
the MCTS. It makes sense: different tasks are better suited to different
network architectures, so you might as well use a different neural net for each one.

However, I found this side remark much more interesting.

> Using no search at all, the RL policy network won 85% of games against Pachi,
> [the strongest open source Go program]. In comparison, the previous state-of-the-art,
> based only on supervised learning of convolutional networks, won 11% of games
> against Pachi and 12% against a slightly weaker program, Fuego.

Before reading the paper, I thought all the improved performance came
from just search. The reality is much more exciting, because it suggests
there's still a gap we're failing to acheive for CNN-based agents. Furthermore,
we can bridge this gap by bootstrapping from the supervised data to
unsupervised self-play data.

Let me repeat that: *this paper shows that when labelled data is lacking
something about the problem, we can still learn from unlabeled data.*

This is huge. This is the kind of thing that makes people want to do research.

The one dream of anybody in ML is unsupervised learning.
It's harder, but it's so much cooler, and the potential feels unbounded.
Supervised learning will always be held back in part by whether
there's a large enough labeled dataset to capture all the information for a problem.
By constrast, unsupervised learning is held back by the sheer difficulty of
learning when you don't know what the answer's supposed to be. This is an idea
problem, not a dataset problem. It's easy to get more unsupervised data; just
look around the world more!

The AlphaGo paper doesn't do unsupervised learning, but it's a big step towards
that direction, and using supervised learning to pre-train unsupervised learning
sounds like a good idea anyways. If you look at the results table,
the final policy network (the one before self-play refinement) got 55.4%
move prediction accuracy, compared to 55.2% move accuracy from the December 2014
paper. It's almost all from self-play, folks. I'm sure plenty of people
are investigating whether a similar approach works on problems besides Go.

Compared to this, interfacing the neural net with search feels less
important. There are some neat ideas here: don't try to use something heavy-duty
in rollouts, pre-seed initial value estimates with the heavy-duty net because
you only need to call it once per node, average the rollout value with the
approximate value network value. And from an engineering perspective, they're
doing some crazy asynchronous CPU + GPU architecture to always keep the machine
busy with computation. Still, to me the story here is the unsupervised learning
capability.


Final Cavaets
-------------------------------------------------------------------------------

I'll close with the few downsides I see so far.

* This still uses a lot of computation time. When they announced results for
running AlphaGo on one machine, they mean a machine with 40 CPU threads and
8 GPUs. The version used against the European Go champion Fan Hui runs on
a distributed cluster of *1202 CPUs and 176 GPUs*. Let's just say this is
still out of the reach of the average enthusiast and move on.
* The reported 5-0 record against Fan Hui was in formal games, one game per
day. Each day, Fan also played an informal game, with shorter time controls.
In those games, AlphaGo won 3-2. This isn't malicious reporting. By my
understanding, both parties knew that only the formal games would count.
* This takes a **lot** of training time. From the Methods section:

> Updates were applied asynchronously on 50 GPUs using DistBelief [...]
> Training [for the supervised network] took around 3 weeks for
> 340 million training steps.

Then, for self-play refinement,

> The [RL policy] network was trained in this way for 10,000 mini-batches
> of 128 games, using 50 GPUs for one day.

And finally, for the value network,

> The value network was trained for 50 million mini-batches of 32 positions,
> using 50 GPUs, for one week.

That adds up to *a month*, even on 50 GPUs. So, for anyone looking to try
something similar, make sure to use a small problem, or a computing cluster,
or both.
