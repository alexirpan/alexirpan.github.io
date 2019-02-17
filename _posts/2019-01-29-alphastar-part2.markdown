---
layout: post
title:  "An Overdue Post on AlphaStar, Part 2"
date:   2019-01-29 01:41:00 -0800
---


*This is part 2 of my post about AlphaStar, focused on the machine learning
side. See [part 1]({% post_url 2019-01-28-alphastar %}) for high-level
impressions.*


A Quick Overview of AlphaStar's Training Setup
-----------------------------------------------------------------

It's impossible to talk about AlphaStar without briefly covering how it works.
Most of the details are vague right now, but more have been promised in an
upcoming journal article. This is based off of what's public so far.

AlphaStar is made of 3 sequence models, likely with some shared weights. Each
sequence model receives the same observations, the raw game state. There are
then three sets of outputs: where to click, what to build/train, and an outcome
predictor.

This model is trained in a two stage process. First, it is trained using
imitation learning on human games provided by Blizzard. My notes from the match
say that it takes 3 days to train the imitation learning baselines.

The models are then further trained using IMPALA and population-based training,
plus some other tricks I'll get to later. This is called
the AlphaStar League. Within the population, each agent is given a slightly
different reward function, some of which involve learning to beat specific agents
in the league. Each agent in the population is trained with 16
TPUv3s, which are estimated to be equivalent to about 50 GPUs each. The
population-based training was run for 14 days.

![AlphaStar MMR Chart](/public/alphastar/alphastar_mmr.png)
{: .centered }

(From original post)
{: .centered }

I couldn't find any references for the population size, or how many agents are
trained simulatenously. I would guess "big" and "a lot", respectively. Now
multiply that by 16 TPUs each and you get a sense of the scale involved.

After 14 days, they computed the
Nash equilibrium of the population, and for the showmatch, selected the top 5
least exploitable agents, using a different one in every game.

All agents were trained in Protoss vs Protoss mirrors on a fixed map, Catalyst
LE.


Takeaways
-------------------------------------------------------

## 1. Imitation Learning Did Better Than I Thought

I have always assumed that when comparing imitation learning to reinforcement
learning, imitation learning performs better when given fewer samples, but
reinforcement learning wins in the long run. We saw that play out here.

One of the problems with imitation learning is the way errors can compound over
time. I'm not sure if there's a formal name for this. I've always
called it the [DAgger](https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf) problem, because that's the paper that everyone cites when
talking about this problem ([Ross et al, AISTATS 2011](https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf)).

Intuitively, the argument goes like this: suppose you train an agent by doing
supervised learning on the actions a human does. This is called *behavior
cloning*, and is a common baseline in the literature. Let's say you train the
model and it has some error bounded by $$\epsilon$$ at each state $$s$$.
Then the worst case bound in performance is $$O(T\epsilon)$$, where $$T$$ is
the episode length, due to compounding errors. The learned model deviates from
the expert a bit, visiting a state where we have less expert supervision. Due to
having less supervision, it makes another bad move, deviating to a further
state with even less supervision. Soon, the agent is doing nonsense. In short,
mistakes are often not recoverable in imitation learning.

The temporal nature of the problem means that the longer your episode is, the
more likely it is that you enter this negative feedback loop, and therefore, we
expect long-horizon tasks to be harder for imitation learning. A StarCraft game
is long enough that I didn't expect imitation learning to work at all.
And yet, imitation learning was good enough to reach the level of a Gold player.

The first version of AlphaGo was bootstrapped by doing behavioral
cloning on human games, and that version was competitive against top open-source
Go engines of the time. But Go is a game with at most 200-250 moves, whereas
StarCraft has thousands of decisions points. I assumed that you
would need a massive dataset of human games to get past this, more than Blizzard
could provide. I'm surprised this wasn't the case.

My guess is that this is tied into another trend: despite the problems with
behavioral cloning, it's actually a pretty strong baseline. I don't do imitation
learning myself, but that's what I've been hearing. I suspect that's because
many of behavioral cloning's problems can be covered up with better data
collection. Here's the pseudocode for DAgger's resolution to the DAgger problem.

![DAgger code](/public/alphastar/dagger.png)
{: .centered }

Given expert policy $$\pi^*$$ and current policy $$\hat{\pi}_i$$, we iteratively
build a dataset $$\mathcal{D}$$ by collecting data from a mixture of the expert
$$\pi^*$$ and current policy $$\hat{\pi}_i$$. We iteratively alternate training
policies and collecting data, and by always collecting with a mixture of expert
data and on-policy data, we can ensure that our dataset will always cover parts
of state-space that are close enough to our current policy.

But importantly, the final optimization loop is still based on maximizing the
likelihood of actions in your dataset. The only change is on how the data is
generated. So, if you have a very large dataset, from a wide variety of experts
(like, say, a corpus of StarCraft games from anyone who's ever played the game), then it's
possible that your data already has enough variety to let your agent learn how
to recover from the majority of incorrect decisions it could make.

This is something I've anecdotally noticed in my own work. Adding a small amount
of exploration noise to a handcoded policy at collection time can give you
significant gains at training time.
The fact that imitation learning gives a good baseline seems important for
bootstrapping learning. It's true that AlphaZero was able to avoid this, but the
AlphaGo version with imitation learning bootstrapping was developed first. I
suspect AlphaZero-based techniques are trickier to get working in the first
place.


## 2. Population Based Training is Worth Keeping an Eye On

StarCraft II is inherently a game based around strategies and
counter-strategies. My feeling is that in DoTA 2, a heavy portion of your
strategy is decided in the drafting phase. Certain hero compositions will only
work best for certain styles of play. Because of this, once the draft is done,
each team has an idea of what to expect.

However, StarCraft II starts out completely unobserved. Builds can go from heavy
early aggression to greedy expansions for long-term payoff. It seems more likely
that StarCraft could devolve into unstable equilibria if you try to represent
the space of strategies within a single agent.

Population-based training does a lot to avoid this problem. A simple [self-play
agent "gets stuck", but a population-based approach reaches Grandmaster
level](https://twitter.com/OriolVinyalsML/status/1094670648042012673). One of
the intuitive traps in self-play is that if you only play against the most
recent version of yourself, then you could endlessly walk around a
rock-paper-scissors loop, instead of discovering the trick that beats rock,
paper, *and* scissors.

I haven't tried population based training myself, but from what I heard,
it tends to give more gains in unstable learning settings, and it seems likely that
StarCraft is one of those games with several viable strategies. If you expect
the game's Nash equilibria to turn into an ensemble of strategies, it seems way
easier to maintain an ensemble of agents.


## 3. Once RL Does Okay, It's Not Too Hard to Make It Great

In general, big RL projects seem to fall into two buckets.

1. They don't work at all.
2. They work and become very good with sufficient compute, which may be very
   large due to diminishing returns.

I haven't seen many in-betweens where things start to work, and then hit a
disappointly low plateau.

One model that would explain this is that algorithmic and training tricks are
all about improving the rate of change for an RL agent. Early on, everything
fails, but with enough tuning, the gradient of improvement starts pointing
upwards enough that the agent can actually learn something. From there, it's not
like the agent forgets how to learn, it's just a question of whether there are
things that are hard to learn or not. This means the gap between blank-slate and
pretty-good is actually much larger than the gap between pretty-good and
pro-level. The first requires finding what makes learning work. The second just
needs more data and training time.

The agent that beat TLO on his offrace was trained for about 7 days. Giving
it another 7 days was enough to beat MaNa on his main race. Sure, double the
compute is a lot of compute, but the first success took almost three years of
research time and the second success took seven days. (On a similar front,
[OpenAI's DoTA 2 agent hit 80% win rate against the model they demoed at The
International, with 10 days of training. Wonder where it's at now...](https://twitter.com/openai/status/1037765547427954688?lang=en).


## 4. We Should Be Tossing More Techniques Together

One thing I found surprising about the AlphaStar architecture is how much
*stuff* goes into it. Here's a list of papers referenced for the model
architecture. I've added links to everything that's non-standard.

* A transformer is used to do self-attention ([Vaswani et al, NIPS 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)).
* This self-attention is used to add inductive biases to the architecture for
  learning relations between objects ([Zambaldi et al, to be presented at ICLR
  2019](https://openreview.net/forum?id=HkxaFoC9KQ)).
* The self-attention layers are combined with an LSTM.
* The policy is auto-regressive, meaning it predicts each action dimension
  conditionally on each previous action dimension.
* This also uses a pointer network ([Vinyals et al, NIPS 2015](https://papers.nips.cc/paper/5866-pointer-networks.pdf)),
  which more easily supports variable length outputs for variable length inputs.

![PointerNet diagram](/public/alphastar/pointer.png)
{: .centered }

Diagram of PointerNet from original paper. A conventional RNN-based seq2seq model
condtionally predicts output from the latent code. A PointerNet outputs
attention vectors over its inputs.
{: .centered }

  I'm not sure why this is helpful. My current guess is that because StarCraft
  involves controlling many units in concert, and the number of units changes
  over the game, a pointer network is a more natural network architecture.
* The model then uses a centralized value baseline, linking a counterfactual
  policy gradient algorithm for multi-agent learning ([Foerster et al, AAAI
  2018](https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/foersteraaai18.pdf)).

![COMA diagram](/public/alphastar/coma.png)
{: .centered }

Diagram of counterfactual multi-agent (COMA) architecture, from original paper,
{: .centered }

  Roughly, instead of having a separate actor-critic pair for each agent, all
  agents share the same critic and get per-agent advantage estimates by
  marginalizing over the appropriate action.

This is just for the model architecture. There are a few more references for the
training itself.

* It's trained with IMPALA ([Espeholt et al, 2018](https://arxiv.org/pdf/1802.01561.pdf)).
* It also uses experience replay.
* And self-imitation learning ([Oh et al, ICML 2018](http://proceedings.mlr.press/v80/oh18b/oh18b.pdf)).
* And policy distillation in some way ([Rusu et al, ICLR 2016](https://arxiv.org/pdf/1511.06295.pdf)).
* Which is trained with population-based training ([Jaderberg et al, 2018](https://arxiv.org/abs/1807.01281)).
* and a reference to Game-Theoretic Approaches to Multiagent RL ([Lanctot et al,
  NIPS 2017](https://arxiv.org/pdf/1711.00832.pdf)). I'm not sure where this is
  used. Possibly for adding new agents to the AlphaStar league that are tuned to
  learn the best response to existing agents?

Many of these techniques were developed just in the last year. Based on the
number of self-DeepMind citations, it's possible much of this was developed just
for the StarCraft project.

When developing ML research for a paper, there are heavy incentives for
changing as little as possible, and concentrating all risk on your proposed
improvement. There are many good reasons for this. It's good science to change
just one variable at a time. By sticking closer to existing work, it's easier to
find previously run baselines, and it's easier for other to validate your work.
However, this means that there are good reasons *not* to incorporate prior
state-of-the-art techniques into your research project. The risk added makes the
cost-benefit analysis unfavorable.

This is a shame, because with how prolific the machine learning field is, there
isn't a lot of cross-paper pollination. I've always liked the Rainbow DQN paper
([Hessel et al, AAAI 2018](https://arxiv.org/abs/1710.02298)),
just because it asked what would happen if you tossed everything together.
AlphaStar feels like something similar: several promising ideas that combine
into a significantly stronger state-of-the-art.

These sorts of papers are really useful for verifying what techniques are worth
using and which ones aren't, because distributed evaluation across tasks and
settings is really the only way we get confidence that a paper is actually
useful. But if the incentives discouraging adding more risk to research
projects, where does that leave us? It is 100% certain that the existing pieces
of machine learning can do something we think it can't, and the only blocker is
that no one's figured out how the Lego blocks go together.

I wonder if the endgame is that research will turn into a two-class structure.
One class of research will be bottom-up, studying well-known baselines, without
a lot of crossover with other papers, proposing many ideas of which 90% will be
useless. The other class will be top-down, done for the sake of achieving
something new on an unsolved problem, finding the 10% of useful ideas with
trial-and-error and using scale to punch through any barriers that only need
scale to solve.

Maybe we're already in that endgame. If so, I don't know how I feel about that.


Predictions
------------------------------------------------------------------------------

The results trained so far were only on a single map and a single PvP match. I
see no reason why a similar technique wouldn't generalize to other maps or races
if given more time. The [Reddit AMA](https://www.reddit.com/r/MachineLearning/comments/ajgzoc/we_are_oriol_vinyals_and_david_silver_from/eexs0pd/) suggests
that AlphaStar already does okay on maps it wasn't trained on.

I've read some theories that claimed DeepMind started at Terran, but moved to
Protoss because their agents would keep lifting up their buildings early on in
training. That seems like a tricky problem that's entirely fixable.

If no further restrictions are added to AlphaStar, I think within a year they'll
be able to beat any pro, in any matchup, on any set of maps in a best-of-five
series. If restrictions
are added to make AlphaStar's gameplay look more human, it's less certain, it
would depend on what those restrictions were. Overall, nothing I saw made me
believe we've seen the limit of what AlphaStar can do.
