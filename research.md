---
layout: page
title: Research
permalink: /research/
---

*Last updated June 4, 2019.*

My current main research interest is deep reinforcement learning, with a bias towards its applications to robotics. Within that, I care about reducing real-world data needed for robot learning, improving reliability of RL systems, and thinking about problems that arise when applying reinforcement learning to real-world settings.

Papers:

- Clobbered for auto generated table of contents
{:toc}


---------------------------------------------

<p></p>

### Off-Policy Evaluation via Off-Policy Classification

*Alex Irpan, Kanishka Rao, Konstantinos Bousmalis, Chris Harris, Julian Ibarz, Sergey Levine*

Paper: [here](https://arxiv.org/abs/1906.01624)

Code: [here](https://gist.github.com/alexirpan/54ac855db7e0d017656645ef1475ac08)

*ICML 2019 Workshop, Reinforcement Learning for Real Life*

Proposes off-policy classification, an approach for off-policy evaluation based
on classifying $$(s,a)$$ with a Q-function estimate. The approach does not
require importance sampling or model learning, and works for image-based tasks.
Shows we can evaluate the transfer performance of models from simulation to a
real-world robot, without running the real-world robot.

### The Principle of Unchanged Optimality in Reinforcement Learning Generalization

*Alex Irpan\*, Xingyou Song\*. Asterisk indicates equal contribution.*

Paper: [here](https://arxiv.org/abs/1906.00336)

*ICML 2019 Workshop, Understanding and Improving Generalization in Deep Learning*

Discusses a principle for designing RL generalization benchmarks: changes to your
dynamics should be observable by your policy to make your problem well-founded.
Argues this using comparisons to supervised learning generalization. Additionally
discussses potential trade-offs between sample complexity and generalization in
model-based RL.

### Sim-to-Real via Sim-to-Sim: Data-efficient Robotic Grasping via Randomized-to-Canonical Adaptation Networks

*Stephen James, Paul Wohlhart, Mrinal Kalakrishnan, Dmitry Kalashnikov, Alex Irpan, Julian Ibarz, Sergey Levine, Raia Hadsell, Konstantinos Bousmalis*

Paper: [here](https://arxiv.org/abs/1812.07252)

Video: [here](https://sites.google.com/view/rcan/)

*CVPR 2019*

Proposes Randomized-to-Canonical Adaptation Networks to cross the sim2real
visual reality gap without real-world data. A pix2pix GAN is trained to transform domain randomized images to a canonical simulated image, which allows it to transform real images to canonical images without further training, and simplifies policy learning. Achieves comparable performance to QT-Opt system with 99% less real data.

### Reliable Uncertainty Estimates in Deep Neural Networks using Noise Contrastive Priors

*Danijar Hafner, Dustin Tran, Timothy Lillicrap, Alex Irpan, James Davidson*

Paper: [here](https://arxiv.org/abs/1807.09289)

*UAI 2019*

Trains Bayesian neural nets with noise contrastive priors (NCPs) to get better uncertainty estimates
for out-of-distribution data by generating OOD data and training the model to have high uncertainty for that data. Thanks to generalization, it's sufficient to predict high uncertainty at the boundary between in-distribution and out-of-distribution data, so OOD data is generated by adding noise to training data.

### QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

*Dmitry Kalashnikov, Alex Irpan, Peter Pastor, Julian Ibarz, Alexander Herzog, Eric Jang, Deirdre Quillen, Ethan Holly, Mrinal Kalakrishnan, Vincent Vanhoucke, Sergey Levine*

Paper and Video: [here](https://sites.google.com/view/qtopt)

Google AI Blog: [here](https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html)

*CoRL 2018, __Best Systems Paper__*

Trains a real-world grasping policy from monocular RGB images, using QT-Opt, a scalable deep reinforcement learning system. The learned policy reaches 96% grasp success on previously unseen objects, uses less data than supervised learning, and automatically learns to singulate objects and retry failed grasps, because they improve long-term grasp success.

### Can Deep Reinforcement Learning Solve Erdos-Selfridge-Spencer Games?

*Maithra Raghu, Alex Irpan, Jacob Andreas, Robert Kleinberg, Quoc V. Le, Jon Kleinberg*

Paper: [here](https://arxiv.org/abs/1711.02301)

Code: [here](https://github.com/rubai5/ESS_Game)

*ICML 2018*

Explores deep RL within Erdos-Selfridge-Spencer games, a class of combinatorial games
where there is a tunable difficulty parameter and a closed-form optimal linear policy. The environments are used to compare learning algorithms, analyze generalization, and compare imitation learning to reinforcement learning.

### Using Simulation and Domain Adaptation to Improve Efficiency of Deep Robotic Grasping

*Konstantinos Bousmalis\*, Alex Irpan\*, Paul Wohlhart\*, Yunfei Bai, Matthew Kelcey, Mrinal Kalakrishnan, Laura Downs, Julian Ibarz, Peter Pastor, Kurt Konolige, Sergey Levine, Vincent Vanhoucke. Asterisk indicates equal contribution.*

Paper and Video: [here](https://sites.google.com/view/graspgan)

*ICRA 2018*

Combines several domain adaptation techniques (both feature-level and pixel-level) to learn real-world grasping policies from monocular RGB images. Achieved same real-world grasp performance with 50x less data.


### Learning Hierarchical Information Flow with Recurrent Neural Modules

*Danijar Hafner, Alex Irpan, James Davidson, Nicolas Heess*

Paper: [here](https://arxiv.org/abs/1706.05744)

*NeurIPS 2017*

Proposes ThalNet, a network architecture inspired by the thalamus in the brain.
Shows the model can learn how to direct information flow between different modules, represented by neural networks.
