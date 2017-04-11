---
layout: page
title: "Appendix: A Batch Norm Overview"
---

What Is Batch Norm?
--------------------------------------------------------------------------------

Batch norm is motivated by "internal covariate shift". What does that mean?
Well, let's suppose we're training a neural network on some data. The input
will go through a few hidden layers, then go to the output.
{: .hidden }

![One hidden layer neural net](/public/perils-batch-norm/neural_net.jpeg)
{: .centered }

Adapted [from a picture from CS231N](http://cs231n.github.io/neural-networks-1/)
{: .centered }

During training, each layer has a different job.
The 1st layer's job is to learn good features from the input. The 2nd layer's
job is to learn good features from the 1st layer's features. The 3rd layer's
job is to learn good features from the 2nd layer. And so on up the network,
until we hit the last layer, whose job is to solve the task from the 2nd-to-last
layer's features.

Each of these jobs is going to interact with the other one, so they aren't
independent, but luckily backprop gives a way to compute the parameter update
for all layers at once. Easy, right?

As the parameters change, the distribution of each layer's activations
will change. This makes the next layer's job harder, because the distribution
it's learning from keeps changing underneath it. This forces the layer to
continually adapt to the distribution, which slows down learning.
The literature calls this
*covariate shift*, and generally it's been studied at the level of the data
(when the test set distribution differs from the training set distribution,
for example.) The observation buiding batch norm is that covariate shift
can be problematic at every layer of the network, and reducing it should
improve training.

To address this, batch norm normalizes every output unit to be mean $$0$$,
variance $$1$$. Well, kind of. There are a few important details.

* To center the distribution of output $$x$$, we need to compute the mean $$\mu$$, the variance
$$\sigma^2$$, and compute

$$
    \hat{x} = \frac{x - \mu}{\sqrt{\sigma^2}}
$$

Mean $$\mu$$ and variance $$\sigma^2$$ depend on the entire distribution, which
is impractical to compute. So instead, we compute the mean and variance for
just the minibatch $$\mathcal{B} = \{x_1, x_2,\ldots, x_m\}$$.

$$
    \mu_\mathcal{B} = \sum_{i=1}^m x_i
$$

$$
    \sigma^2_\mathcal{B} = \sum_{i=1}^m (x_i - \mu_B)^2
$$

$$
    \hat{x_i} = \frac{x_i - \mu_B}{\sqrt{\sigma_\mathcal{B}^2 + \epsilon}}
$$

(The $$\epsilon$$ is here to avoid division by zero problems.)

**Note $$\hat{x_i}$$ now depends on other $$\hat{x_j}$$ in the batch!**


* To make the output deterministic at eval time, we keep a moving average
of $$\mu_\mathcal{B}$$ and $$\sigma^2_\mathcal{B}$$. On every parameter
update, we also compute

$$
    \mu \gets (1-\alpha) \mu + \alpha * \mu_\mathcal{B}
$$

$$
    \sigma^2 \gets (1-\alpha) \sigma^2 + \alpha * \sigma^2_\mathcal{B}
$$

This is the exponential moving average, and it has a nice property: the
average places more weight on recent inputs. When the network converges,
this is usually a good estimate of the dataset-wide mean and variance.
At test time, We normalize with the averaged $$\mu$$ and $$\sigma$$
instead.

$$
    \hat{x} = \frax{x - \mu}{\sqrt{\sigma^2 + \epsilon}}
$$

* Finally, in practice we don't want to limit the output distribution to only
be mean $$0$$ and variance $$1$$. So we define

$$
    \hat{y_i} = \gamma_i\hat{x_i} + \beta_i
$$

to be the actual output, and let $$\beta$$ and $$\gamma$$ be learnable
parameters.

![Batch norm algorithm](/public/perils-batch-norm/batch-norm-alg.png)
{: .centered }

Note that at the end of the transform, the activations can still follow an
arbitrary distribution. However, that distribution's mean and variance depend
only on $$\gamma$$ and $$\beta$$. (To be specific, the mean is $$\beta$$ and
the variance is $$\gamma^2$$.) By concentrating the mean and variance into
a single variable, we make it easier for the network to learn the distribution
that makes solving the task easiest.

During the training process, we also keep a running average of minibatch means
and variances. Let $$\mu_B$$ and $$\sigma_B$$ be the minibatch mean and variance.
We update with an exponential moving average.

$$
    \mu \gets \beta \mu + (1-\beta) \mu_B
$$

$$
    \sigma \gets \beta \sigma + (1-\beta) \sigma_B
$$

The exponential moving average is a weighted average of all terms seen so far,
except it places more weight on recent terms. We use this to approximate
the true mean and variance over the entire dataset.

At evaluation time, instead of normalizing with the minibatch mean and variance,
we normalize with the averaged $$\mu$$ and $$\sigma$$. This makes the evaluation
independent of the examples in each minibatch.

[Back to original post]({% post_url 2017-03-21-perils-batch-norm %})
