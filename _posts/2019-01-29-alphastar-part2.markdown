---
layout: post
title:  "An Overdue Post on AlphaStar, Part 2"
date:   2019-02-22 01:53:00 -0800
---


*This is part 2 of my post about AlphaStar, which is
focused on the machine learning implications.
Click [here]({% post_url 2019-01-28-alphastar %}) for part 1.*


A Quick Overview of AlphaStar's Training Setup
-----------------------------------------------------------------

It's impossible to talk about AlphaStar without briefly covering how it works.
Most of the details are vague right now, but more have been promised in an
upcoming journal article. This summary is based off of what's public so far.

AlphaStar is made of 3 sequence models that likely share some weights. Each
sequence model receives the same observations: the raw game state. There are
then three sets of outputs: where to click, what to build/train, and an reward
predictor.

This model is trained in a two stage process. First, it is trained using
[imitation learning](https://sites.google.com/view/icml2018-imitation-learning/) on human games provided by Blizzard. My notes from the match
say it takes 3 days to train the imitation learning baseline.

The models are then further trained using [IMPALA](https://arxiv.org/abs/1802.01561) and [population-based training](https://arxiv.org/abs/1807.01281),
plus some other tricks I'll get to later. This is called
the AlphaStar League. Within the population, each agent is given a slightly
different reward function, some of which include rewards for exploiting other
specific agents in the league. Each agent in the population is trained with 16
TPUv3s, which are estimated to be equivalent to about 50 GPUs each. The
population-based training was run for 14 days.

![AlphaStar MMR Chart](/public/alphastar/alphastar_mmr.png)
{: .centered }

(From original post)
{: .centered }

I couldn't find any references for the population size, or how many agents are
trained simultaneously. I would guess "big" and "a lot", respectively. Now
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
supervised learning on the actions a human does. This is called *behavioral
cloning*, and is a common baseline in the literature. At $$t=0$$, your model acts with small error
$$\epsilon_0$$. That's fine. This carries it to state that's modelled less well,
since the expert visited it less often. Now at $$t=1$$, it acts with slightly
larger error $$\epsilon_1$$. This is more troubling, as we're in a state with even
less expert supervision. At $$t=2$$, we get a larger error $$\epsilon_2$$, at
$$t=3$$ an even larger $$\epsilon_3$$, and so on. As the errors compound over time, the
agent goes through states very far from expert behavior, and because we don't have
labels for these states, the agent is soon doing nonsense.

This problem means mistakes in imitation learning often aren't recoverable,
and the temporal nature of the problem means that the longer your episode is, the
more likely it is that you enter this negative feedback loop, and the worse
you'll be if you do. You can prove
that if the expected loss each timestep is $$\epsilon$$, then the worst-case
bound over the episode is $$O(T^2\epsilon)$$, and for certain loss functions
this worst-case bound is tight.

Due to growing quadratically in $$T$$, we expect long-horizon tasks to be harder
for imitation learning.
A StarCraft game
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
data and on-policy data, we can ensure that our dataset will always include both
expert states and states close to ones our current policy would visit.

But importantly, the core optimization loop (the "train classifier" line)
is still based on maximizing the
likelihood of actions in your dataset. The only change is on how the data is
generated. If you have a very large dataset, from a wide variety of experts
of varying skill levels
(like, say, a corpus of StarCraft games from anyone who's ever played the game), then it's
possible that your data already has enough variation to let your agent learn how
to recover from several of the incorrect decisions it could make.

This is something I've anecdotally noticed in my own work. When collecting
[robot grasping data](https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html),
we found that datasets collected with small amounts of exploration noise led to
significantly stronger policies than datasets without it.

The fact that imitation learning gives a good baseline seems important for
bootstrapping learning. It's true that AlphaZero was able to avoid this, but
AlphaGo with imitation learning bootstrapping was developed first. There
usually aren't reasons to discard warm-starting from a good base policy, unless
you're deliberately doing it as a research challenge.


## 2. Population Based Training is Worth Watching

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
the game's Nash equilibrium to turn into an ensemble of strategies, it seems way
easier to maintain an ensemble of agents, since you get a free inductive prior.


## 3. Once RL Does Okay, Making It Great Is Easier

In general, big RL projects seem to fall into two buckets.

1. They don't work at all.
2. They work and become very good with sufficient compute, which may be very
   large due to diminishing returns.

I haven't seen many in-betweens where things start to work, and then hit a
disappointingly low plateau.

One model that would explain this is that algorithmic and training tricks are
all about adding constant multipliers to how quickly your RL agent can learn new
strategies. Early in a project, everything fails, because the learning signal is
so weak that nothing happens.
With enough tuning, the multipliers become large enough for agents to show signs
of life. From there, it's not like the agent ever forgets how to learn. It's always
capable of learning. It's just a question of whether the things needed for the
next level of play are hard to learn or not.

Humans tend to pick up games easily, then spend forever mastering them. RL seems
to have the opposite problem - they pick up games slowly, but then master them
with relative ease.
This means the gap between blank-slate and
pretty-good is actually much larger than the gap between pretty-good and
pro-level. The first requires finding what makes learning work. The second just
needs more data and training time.

The agent that beat TLO on his offrace was trained for about 7 days. Giving
it another 7 days was enough to beat MaNa on his main race. Sure, double the
compute is a lot of compute, but the first success took almost three years of
research time and the second success took seven days. Similarly, although
OpenAI's DotA 2 agent lost against a pro team,
[they were able to beat their old agent 80% of the time with 10 dats of
training. Wonder where it's at now...](https://twitter.com/openai/status/1037765547427954688?lang=en)


## 4. We Should Be Tossing Techniques Together More Often

One thing I found surprising about the AlphaStar architecture is how much
*stuff* goes into it. Here's a list of papers referenced for the model
architecture. I've added links to everything that's non-standard.

* A transformer is used to do self-attention ([Vaswani et al, NeurIPS 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)).
* This self-attention is used to add inductive biases to the architecture for
  learning relations between objects ([Zambaldi et al, to be presented at ICLR
  2019](https://openreview.net/forum?id=HkxaFoC9KQ)).
* The self-attention layers are combined with an LSTM.
* The policy is auto-regressive, meaning it predicts each action dimension
  conditionally on each previous action dimension.
* This also uses a pointer network ([Vinyals et al, NeurIPS 2015](https://papers.nips.cc/paper/5866-pointer-networks.pdf)),
  which more easily supports variable length outputs for variable length inputs.

    ![PointerNet diagram](/public/alphastar/pointer.png)
    {: .centered }
  
    Diagram of PointerNet from original paper. A conventional RNN-based seq2seq model
    condtionally predicts output from the latent code. A PointerNet outputs
    attention vectors over its inputs.
    {: .centered }
  
    My guess for why a pointer net helps is that StarCraft
    involves controlling many units in concert, and the number of units changes
    over the game. Given that you need to output an action for each unit, a pointer
    network is a natural choice.

* The model then uses a centralized value baseline, linking a counterfactual
  policy gradient algorithm for multi-agent learning ([Foerster et al, AAAI
  2018](https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/foersteraaai18.pdf)).

    ![COMA diagram](/public/alphastar/coma.png)
    {: .centered }
    
    Diagram of counterfactual multi-agent (COMA) architecture, from original paper.
    Instead of having a separate actor-critic pair for each agent, all
    agents share the same critic and get per-agent advantage estimates by
    marginalizing over the appropriate action.
    {: .centered }

This is just for the model architecture. There are a few more references for the
training itself.

* It's trained with IMPALA ([Espeholt et al, 2018](https://arxiv.org/pdf/1802.01561.pdf)).
* It also uses experience replay.
* And self-imitation learning ([Oh et al, ICML 2018](http://proceedings.mlr.press/v80/oh18b/oh18b.pdf)).
* And policy distillation in some way ([Rusu et al, ICLR 2016](https://arxiv.org/pdf/1511.06295.pdf)).
* Which is trained with population-based training ([Jaderberg et al, 2018](https://arxiv.org/abs/1807.01281)).
* And a reference to Game-Theoretic Approaches to Multiagent RL ([Lanctot et al,
  NeurIPS 2017](https://arxiv.org/pdf/1711.00832.pdf)). I'm not sure where this is
  used. Possibly for adding new agents to the AlphaStar league that are tuned to
  learn the best response to existing agents?

Many of these techniques were developed just in the last year. Based on the
number of self-DeepMind citations, and how often those papers report results on
the StarCraft II Learning Environment, it's possible much of this was developed
specifically for the StarCraft project.

When developing ML research for a paper, there are heavy incentives to
change as little as possible, and concentrate all risk on your proposed
improvement. There are many good reasons for this. It's good science to change
just one variable at a time. By sticking closer to existing work, it's easier to
find previously run baselines. It's also easier for other to validate your work.
However, this means that there are good reasons *not* to incorporate prior
state-of-the-art techniques into your research project. The risk added makes the
cost-benefit analysis unfavorable.

This is a shame, because ML is a very prolific field, and yet
there isn't a lot of cross-paper pollination. I've always liked the Rainbow DQN paper
([Hessel et al, AAAI 2018](https://arxiv.org/abs/1710.02298)),
just because it asked what would happen if you tossed everything together.
AlphaStar feels like something similar: several promising ideas that combine
into a significantly stronger state-of-the-art.

These sorts of papers are really useful for verifying what techniques are worth
using and which ones aren't, because distributed evaluation across tasks and
settings is really the only way we get confidence that a paper is actually
useful. But if the incentives discourage adding more risk to research
projects, then very few techniques get this distributed evaluation. Where does that leave us?
It is incredibly certain that the existing pieces
of machine learning can do something we think it can't, and the only blocker is
that no one's tried the right combination of techniques.

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

In 2016, shortly after the AlphaGo vs Lee Sedol match, I got into a conversation with
someone about AGI timelines. (Because, of course, whenever ML does something
new, some people will immediately debate what it means for AGI.) They thought
AGI was happening very soon. I thought it wasn't, and as an exercise they
asked what would change my mind.

I told them that given that DeepMind was working on StarCraft II, if they beat a
pro player within a year, I'd have to seriously revise my assumptions on the
pace of ML progress. I thought it would take five to ten years.

The first win in the AlphaGo vs Lee Sedol match was on March 9, 2016, and the
MaNa match was announced January 24, 2019. It took DeepMind just shy of three
years to do it.

The last time I took an AI predictions questionnaire, it only asked about
moonshot AI projects. Accordingly, almost all of my guesses were
at least 10 years in the future. None of what they asked has happened yet, so
it's unclear to me if I'm poorly calibrated on moonshots or not - I won't be able
to know for sure until 10 years have passed!

This is probably why people don't like debating with futurists who only make
long-term predictions. Luckily, I don't deal with people like that very
often.

To try to avoid this problem with AlphaStar, let me make some one-year
predictions.

**If no restrictions are added besides no global camera, I think within a year
AlphaStar will be able to beat any pro, in any matchup, on any set of maps in a best-of-five
series.**

So far, AlphaStar only uses a single map and a single PvP match. I
see no reason why a similar technique wouldn't generalize to other maps or races
if given more time. The [Reddit AMA](https://www.reddit.com/r/MachineLearning/comments/ajgzoc/we_are_oriol_vinyals_and_david_silver_from/eexs0pd/) says
that AlphaStar already does okay on maps it wasn't trained on, suggesting the
model can learn core, generalizable features of StarCraft.

Other races are also definitively on DeepMind's roadmap. I've read some theories
that claimed DeepMind started at Terran, but moved to
Protoss because their agents would keep lifting up their buildings early on in
training. That could be tricky, but doesn't sound impossible.

The final showmatch against MaNa did expose a weakness where AlphaStar didn't
know how to deal with drops, wasting time moving its army back and forth across
the map. Now that this problem is a known quantity, I expect it to get resolved
by the next showmatch.

If restrictions are added to make AlphaStar's gameplay look more human, I'm less
certain what will happen.
It would depend on what the added restrictions were. The most likely restriction is one
on burst APM. Let's say a cap of 700 burst APM, as that seems roughly in line with MaNa's
numbers. **If a 700 burst APM restriction is added, it's less likely
AlphaStar will be that good in a year, but it's still at least over 50%**.
My suspicion is that existing strategies will falter with tighter APM limits. I also
suspect that with enough time, population-based training will find strategies
that are still effective.

One thing a few friends have mentioned is that they'd like to see extended games
of a single AlphaStar agent against a pro, rather than picking a different agent
every game. This would test whether a pro can quickly learn to exploit that
agent, and whether the agent adapts its strategy based on its opponent's
strategy. I'd like to see this too, but it seems like a strictly harder problem
than using a different agent from the ensemble for each game, and I don't see reasons
for DeepMind to switch off the ensemble. I predict we won't see any changes on
this front.

Overall, nothing I saw made me believe we've seen the limit of what AlphaStar can do.

*Thanks to the following people for reading drafts of this post:
Tom Brown,
Jared Quincy Davis,
Peter Gao,
David Krueger,
Bai Li,
Sherjil Ozair,
Rohin Shah,
Mimee Xu,
and everyone else who preferred staying anonymous.*

