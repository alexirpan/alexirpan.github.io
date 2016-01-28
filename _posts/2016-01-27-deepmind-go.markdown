---
layout: post
title:  "Go: More Complicated Than Go Fish"
date:   2016-01-28 03:15:00 -0800
---

*As something "hot off the presses" (hot off the keyboard?), this is a bit unpolished.*

Yesterday, Google DeepMind announced [they had developed an AI called AlphaGo
that reached expert level in Go](http://googleresearch.blogspot.com/2016/01/alphago-mastering-ancient-game-of-go.html),
beating the European Go champion.

It got picked up by, well, everybody. I don't want to catalog every article,
so here's a sample:
[MIT Technology Review](http://www.technologyreview.com/news/546066/googles-ai-masters-the-game-of-go-a-decade-earlier-than-expected/),
[Wired](http://www.wired.com/2016/01/in-a-huge-breakthrough-googles-ai-beats-a-top-player-at-the-game-of-go/),
[Ars Technica](http://arstechnica.com/gadgets/2016/01/googles-ai-beats-go-champion-will-now-take-on-best-player-in-the-world/),
and [The New York Times](http://bits.blogs.nytimes.com/2016/01/27/alphabet-program-beats-the-european-human-go-champion/),
Posts from friends and famous AI researchers have been filling my news feed,
and it's all along the lines of "Well done" or "Holy shit" or "I for one welcome our
new robot overlords." .

Although computer Go isn't one of my main interests,
Monte Carlo Tree Search (MCTS) is. The biggest application of MCTS is in
computer Go, and when you spend two semesters researching MCTS, you end up
reading a few computer Go papers along the way. So, I figure my perspective is
at least slightly more informed.


Prior Work
--------------------------------------------------------------------------

My first reaction was that AlphaGo was very impressive, but not surprising.

This is at odds with some of the reporting. The original blog post says that

> Experts predicted it would be at least another 10 years until a computer
> could beat one of the world’s elite group of Go professionals.

The MIT Technology Review repeats this with

> Google’s AI Masters the Game of Go a Decade Earlier Than Expected

Wired has an actual quote by said expert, Rémi Coulom.

> In early 2014, Coulom’s Go-playing program, Crazystone, challenged grandmaster Norimoto Yoda at a tournament in Japan. And it won. But the win came with caveat: the machine had a four-move head start, a significant advantage. At the time, Coulom predicted that it would be another 10 years before machines beat the best players without a head start.

I entirely understand why it sounds like this result came out of nowhere,
but it didn't. Giant leaps are very rare in research. For problems like computer
Go, it's more like trying to punch through a thick wall. At first, the problem
is unapproachable. Over the years, people make incremental progress,
chipping away bit by bit, building prototype chisels, exploring blueprints for
hypothetical pile drivers, and so on.
Eventually, all the right ideas collect by the wall, some group puts
the pieces together in the right way, and finally breaks down the wall.

Then reporters only talks about the final breakthrough, and it
sounds like complete magic to outsiders.

This isn't a dig at science reporting.
You have to be steeped in a research field to see
the signs of a breakthrough, and asking reporters to do that for every field
is unreasonable. Even then, people close to breakthroughs are often wrong.
I'm sure there are plenty of
professors who were (and maybe still are) pessimistic on neural nets and
optimistic on SAT solvers. It's also often in the interest of authors to
play up the strengths of their research.

Back to Go. I wasn't surprised because [DeepMind released a preprint of
their previous Go paper on December 2014](http://arxiv.org/abs/1412.6564).
(Incidentally, [Clark and Storkey](http://arxiv.org/abs/1412.3409)
released a similar paper 10 days before them, with worse results.
The day before Google announced AlphaGo,
Facebook AI Research [updated a preprint](http://arxiv.org/abs/1511.06410)
for their computer Go work. Funny how that goes.)

Before this paper, the best approach was Monte Carlo Tree
Search. In MCTS, the algorithm evaluates board positions by playing many random
games, or rollouts. Using previous results, it focuses the search on more
promising moves. Progress in MCTS strategies came from tweaking the rollout
policy. A stronger rollout player gives more accurate results,
but because MCTS runs hundreds of thousands of rollouts, even small increases
in computing cost get magnified.

What made DeepMind's first paper so impressive was that it achieved good performance
with zero search. Pass in the board, get a move in a few milliseconds.
Compared to the 5 second search time other programs used, this was radically
different. It didn't beat existing bots, but it didn't have to.

The approach was simple. Using supervised learning, they trained a
convolutional neural net to predict the next move from a database of expert
level games.
With a big enough CNN, they got to 55.2% accuracy, which beat all prior
move predictors.

At the end of their 2014 paper, there's a short section on combining
their CNN with search. They didn't get very far, besides showing it was
an obviously good idea if it could be made computationally feasible.

Ever since that paper, it's felt like the last thing Computer Go needed a
combination of heavy duty neural net move predictors with MCTS, done such
that computation time didn't explode.

With AlphaGo, that's finally happened. So no, these results aren't that
crazy. There was a clear roadmap of what needed to happen, and people
figured it out.

To be fair to Rémi Coulom, his quoted remarks came before DeepMind's preprint
was sent to the computer-go mailing list. I'm sure he's been following
this closely, and it's an unfortunate citation without context.


The New Stuff
---------------------------------------------------------------------------

I know I've been a bit down on AlphaGo, but I don't want that to fool
anybody. AlphaGo is exceptionally impressive.
If you have access, I highly recommend reading the [Nature](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)
paper on your own. It's very well written, and the key ideas are conveyed well.

If you don't have access, here's the quick summary.

* Using the supervised dataset of expert level games. they train
two networks. One is a small rollout network, used for rollouts in the MCTS.
The other is a large CNN, similar to the Dec 2014 paper. This is called
the policy network.
* The policy network is further refined through self-play and reinforcement
learning. (The paper calls this the RL policy network.)
* Finally, they train a value network, which predicts the value of a board
if both players play according to the RL policy network.
  * The value network gives an approximation of rollout values with the
  larger network. It's an approximation, but it's thousands of times
  faster.

The first part that piqued my interest was how many networks were trained
for AlphaGo. It makes sense: different tasks in MCTS are better suited to different
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
It's very hard, but it's so much cooler when it works, and the potential of
unsupervised learning feels unbounded.
Supervised learning will always be held back in part by whether
there's a large enough labeled dataset to capture all the information for a problem.
Labels need to be provided by humans, so constructing large datasets takes
a lot of manpower.

By contrast, unsupervised learning is held back only by the sheer difficulty of
learning when you don't know what the answer is supposed to be. This is an idea
problem, not a dataset problem. It's easy to get more unsupervised data; just
look around the world more!

The AlphaGo paper doesn't do unsupervised learning, but it's a big step towards
that direction, and using supervised learning to pre-train unsupervised learning
sounds like a good idea anyways. If you look at the results table,
the final policy network (the one before self-play refinement) got 55.4%
move prediction accuracy, compared to 55.2% move accuracy from the December 2014
paper. The improved performance doesn't come from the CNN, it all comes from
self-play. Remember that the 85% win rate against Pachi doesn't even use search.
I'm sure plenty of people
are investigating whether a similar approach works on problems besides Go.

Compared to this, interfacing the neural net with search feels less
important. There are some neat ideas here: train a special small network for
rollouts, pre-seed initial value estimates with the heavy-duty net (which you can afford
because you only need it once per node), and combine the approximate value from
the policy network with the true value from the weaker rollout network.
From an engineering perspective, they're
doing a crazy asynchronous CPU + GPU architecture that sounds like a nightmare to
manage. There are plenty of ideas here, but to me the story is proving the
capability of unsupervised learning.


Final Caveats
-------------------------------------------------------------------------------

I'll close with the few downsides I see on skimming the paper.

* This still uses a lot of computation time. When they announced results for
running AlphaGo on one machine, they mean a machine with 48 CPUs and
8 GPUs. The version used against the European Go champion Fan Hui runs on
a distributed cluster of *1202 CPUs and 176 GPUs*. Let's just say this is
out of the reach of the average enthusiast and move on.
* The reported 5-0 record against Fan Hui was in formal games, one game per
day. Each day, Fan also played an informal game, with shorter time controls.
In those games, AlphaGo won 3-2.
* This takes a **lot** of training time. From the methods section:

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
