---
layout: post
title:  "A Hot Take on Go-Explore"
date:   2018-11-26 21:47:00 -0800
---

This was originally going to be a Tweetstorm, but then I decided it would fit
better as a blog post.

Today, Uber AI Labs announced that they had solved
[Montezuma's Revenge with a new algorithm called Go-Explore](https://eng.uber.com/go-explore/).
Montezuma's Revenge is the classical hard example of difficult Atari exploration
problems. They also announced some results on Pitfall, a more difficult Atari
exploration problem. Pitfall is a less popular benchmark, and I suspect that's
because it's so hard to get a positive score at all.

These are eye-popping headlines, but there's controversy around the results,
and I have opinions here. For future note, I'm writing this before the official
paper is released, so although I believe I


What is the Proposed Approach?
-------------------------------------------------------------------------------

This is a summary of the [official release](https://eng.uber.com/go-explore/)
which you should read for yourself.

One of the common approaches to solve exploration problems is intrinstic
motivation. Roughly, if you provide bonus rewards for novel states, you can encourage
agents to explore more of the state space, even if they don't receive any external
reward from the environment.

The authors theorize that one problem with these approaches is that they do a
poor job at continuing to explore promising areas far away from the start state.
They call this phenomenon *detachment*.

![Detachment diagram](/public/go-explore/detachment.png)
{: .centered }

In this toy example, the agent is right between two rich sources of novelty.
By chance, it first explores the left spiral, then the right spiral. In the diagram
above, states that are no longer novel are colored white. We see that if all
neighbors of a novel state are boring, then it is impossible to reach that
novel state, and it's also impossible to reach any novel state bottlenecked by
that state.

The proposed solution to this problem is to maintain a memory of previously
visited novel states. When learning, the agent first randomly samples a previously
visited state, biased towards newer ones. It travels to that state, then explores
from that state. In the example above, by chance we will eventually resample a
state near the boundary of visited states, and from here it is easy to discover a
novel state.

DIAGRAM

In principle, you could combine this paradigm with an intrinstic motivation algorithm,
but the authors found it was enough to explore randomly from the previously visited
state.


Where is the Controversy?
-------------------------------------------------------------------------------

I think this motivation is sound, and I like the thought experiment. The controversy
lies within the details of the approach. Specifically,

1. How do you represent game states within your memory, in a way that groups similar
states while separating dissimilar ones?
2. How do you successfully return to previously visited states?
3. How is the final evaluation performed?

The first point is very mild. They found that simply downsampling the image to a smaller
image was sufficient to get a good enough code. (8 x 11 grayscale image with 8 pixel intensites).

![Downscaling](/public/go-explore/downscale.gif)
{: .centered }

Exact details are still pending, but presumably, if two images downsample to the same code,
then only one instance of that code is kept in memory.

The only controversy here is that the original post starts by saying that it can achieve
2,000,000 points on Montezuma's Revenge, well over 100 times the score of the previous
state-of-the-art ([Random Network Distillation](https://blog.openai.com/reinforcement-learning-with-prediction-based-rewards/)).
However, these scores are only achieved if the state representation is defined not by
down-sampling, but by this:

* The x-y position of the character.
* The current room.
* The current level.
* The number of keys held.

This is a lot of domain-specific knowledge for Montezuma's Revenge. However, the downsampling
approach still achieves 35,000 points, which is still three times larger than SOTA.

The more significant controversy comes for points 2 and 3. For returning to previous states,
three methods are proposed:

* reset the environment directly to that state
* memorize and replay the sequence of actions that take you to that state if you're in a deterministic environment
* learn a goal-conditioned policy if you're in a stochastic environment

The first two methods make the strong assumption that you are either using a simulator or using
a fully deterministic environment where memorization is possible. The third method makes a strong
implicit assumption: that it is possible to learn a good goal-conditioned policy.
For both Montezuma's Revenge and Pitfall, the authors use the first method and directly reload the game state.

The other controversy is that reported numbers use just the random warm start initialization for
randomness, where the first 30 actions are selected at random and then the agent takes over.
The reported numbers in previous state-of-the-art also uses sticky actions, recently
advocated by [(Machado et al, 2017)](https://arxiv.org/abs/1709.06009). With probability $$\epsilon$$,
the previous action is executed instead of the one the agent requests, to add randomness to
the dynamics.


Okay, So What's the Big Deal?
---------------------------------------------------------------------------------------

Those are facts. Now here are the opinions.

It's bad that the SOTA they compare against uses sticky actions, and the numbers quotes in the
blog post do not use sticky actions. However, this should be easy to resolve. Just add
sticky actions, rerun the learned agent, and see what the numbers are.

The controversy I care about much more is the one around the training setup. Go-Explore training is
divided into two phases. In phase 1, we do exploration in a fully deterministic Atari environment.
In phase 2, we do robustification by imitation learning with
the "backward" algorithm from [Learning Montezuma's Revenge from a Single Demonstration](https://blog.openai.com/learning-montezumas-revenge-from-a-single-demonstration/).
This backward algorithm relies on the ability to reset to arbitrary states along the demonstration,
from easy to hard.

![Backward algorithm](/public/go-explore/backward.png)
{: .centered }

(Diagram of the backward algorithm. The agent is initialized very close to the key, then is initialized
further back in the demonstration after it has learned how to reach the key. From original post.)
{: .centered }

This robustification step can be done in a stochastic environment, but requires learning a good policy
in the deterministic environment first, and it's hard to overstate how big of a deal this is.
This can matter a lot! One of the results shown by [(Rajeswaran & Lowrey et al, 2018)](https://arxiv.org/pdf/1703.02660.pdf)
is that for the MuJoCo benchmarks, the gains from a wider state initialization are more significant
than the gains from a different model architecture or from a different RL algorithm. If we think of
simulator initialization as a kind of designed state initialization, then it should be clear why
learning could be a lot easier.

If I was arguing for the Uber press release. I would say that this is part of the point. Yes,
Go-Explore makes many assumptions. *But look at the numbers!* It does very well on Montezuma's Revenge
and Pitfall, and the assumptions made may still be applicable to other environments.

To me, the core question is this: **what is the role of the Montezuma's Revenge benchmark?** This is
always a bit of a touchy subject, but in my view, benchmarks fall along a spectrum. On one end, you have
Chess, Go, and self-driving cars. These are grand challenges where we declare them solved when anybody
can solve them to human-level performance by any means necessary, and where few people will complain
if the final solution relies on assumptions about the benchmark.

On the other end, you have the MountainCar, Pendulums, and LQRs of the world. Benchmarks where if
you given even a *hint* about the environment, a model-based method will solve it almost instantly,
and the fun is seeing whether your model-free RL method can solve it too.

These days, most RL benchmarks are closer to the MountainCar end of the spectrum. We deliberately
keep ourselves blind to some aspects of the problem, to see how well our RL approaches can do. We then
use the best approaches in future environments that are compatible with what our learning
algorithm assumes.

In this respect, the fact that the current results rely on simulator initialization is a dealbreaker.
Yes, if your environment is deterministic, you don't need initialization, because you can memorize
good trajectories. But at that point, we might as well do what [(Seijen et al, 2017)](https://blogs.microsoft.com/ai/divide-conquer-microsoft-researchers-used-ai-master-ms-pac-man/)
did. This paper also announced a superhuman result on Atari: achieving 1 million points on Ms. Pac-Man,
compared to a human high score of 266,330 points. However, if you look at their methods section, you see
that this result relies on trajectory memorization. Whenever the agent completes a Pacman level, the
trajectory it executed it saved to memory, and then replayed that trajectory whenever it sees that level.
This guarantees that the RL algorithm only has to learn how to solve each level once. Without this trick,
the agent gets to about 25,000 points instead.

![Ms. Pac-Man results](/public/go-explore/mspacman.png)
{: .centered }

(Plots from [Hybrid Reward Architecture for Reinforcement Learning](https://blogs.microsoft.com/ai/divide-conquer-microsoft-researchers-used-ai-master-ms-pac-man/))
{: .centered }


