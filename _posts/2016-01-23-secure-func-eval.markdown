---
layout: post
title:  "A Gentle Introduction to Secure Function Evaluation"
date:   2016-01-23 18:19:00 -0800
---

As a final project in a theoretical cryptography course I took last semester,
we had to give a short presentation on a crypto research paper. This blog
post is adapted from my presentation notes. Although the proofs
rely on a lot of background knowledge, the core ideas are very clean and
elegant.

Note: this field is more commonly known as secure computation, but I like
secure function evaluation more because it's more specific.

\*\*\*
{: .centered }

What is Secure Function Evaluation?
-------------------------------------------------------------------

In secure function evaluation, we have the following setting. Alice and
Bob are two parties. Alice has private information $$x$$, and Bob has
private infromation $$y$$. There
is some function $$f(x,y)$$ that both Alice and Bob want to know, but
neither Alice nor Bob wants the other party to learn their private inputs.

PICTURE HERE

The classical example of this is Yao's Millionaire Problem. In this
problem, Alice and Bob are both very rich, and want to know who has
more money. At the same time, it's socially unacceptable to brag about
your wealth, so neither wants to say how much money they have. In
this example, $$x$$ is Alice's wealth, $$y$$ is Bob's wealth, and

$$
    f(x,y) = \begin{cases}
        \text{Alice} & \text{if } x > y \\
        \text{Bob} & \text{if } x < y \\
        \text{same} & \text{if } x = y
    \end{cases}
$$

The question of secure function evaluation is this: **does there exist
a protocol where Alice and Bob can both learn $$f(x,y)$$, and neither
learns anything more than they should?**

It turns out the answer is yes. Before explaining how this is doable,
we first need to set up a few ground rules. In this protocol, we're
going to assume adversaries are *semi-honest*, also known as
*honest-but-curious*. In this adversary model, we assume both Alice
and Bob follow protocol exactly (hence why it's honest). After they
finish communicating, Alice and Bob will attempt to extract
information based on the messages they received (hence why it's semi-honest,
or honest-but-curious).

One reasonable question is to ask why we're limiting the power of the
adversary. Assuming neither party lies to each other sounds hopelessly
naive. It's true that a stronger adversary gives a stronger protocol,
but it also makes it harder to design such a protocol. Historically,
the semi-honest protocol was proved first, and later work extended it
to malicious adversaries. Explaining how to do that is above the scope
of this post.


Information Leakage
-------------------------------------------------------------------

To prove a protocol doesn't leak any additional information, we first
need to explain what that actually means. What makes secure function
evaluation tricky is that Alice and Bob cannot trust each other.
Suppose there was a 3rd person, named Faith, who both Alice and Bob
trust. Then, we have a very simple protocol.

* Alice sends $$x$$ to Faith
* Bob sends $$y$$ to Faith
* Faith computes $$f(x,y)$$, and send it back to Alice and Bob

PICTURE HERE.

This is called the *ideal world*, because it represents the best
case scenario. At the end of the protocol, Alice knows $$x$$ and
$$f(x,y)$$, while Bob knows $$y$$ and $$f(x,y)$$.

There's an important subtlety here. **Even in the ideal world, Alice
and Bob may leak information about their inputs.** For example,
suppose $$f(x,y) = x+y$$. At the end of computation, Alice knows
$$x$$ and $$x+y$$. By computing

$$
    (x+y) - x = y
$$

Alice can learn Bob's original input. Bob can do the same thing.

Going back to the millionaire's problem, suppose Alice has $$10$$
dollars and Bob has $$8$$ dollars. They securely compute who has the
most money, and both learn Alice is richer. Now Alice knows Bob
has less than $$10$$ dollars, and Bob knows Alice has more than
$$8$$ dollars. However, there is still some privacy: neither knows
the exact wealth of the other.

Computing $$f(x,y)$$ may leak information, but we assume that Alice
and Bob recognize this is a necessary evil if they want to compute
$$f$$.

If the ideal world is the best we can do, then we should expect the real protocol
(the one where Faith doesn't exist) to act the same.
This gives the following definition of security.

**A function evaluation protocol is secure if it leaks no more
information than the ideal world protocol.**
{: .centered }

(Side note: if you're familiar with zero-knowledge proofs, this
may seem familiar. To formally prove security, you need to show
there are simulators for both Alice and Bob that can simulate the
entire protocol from only the information they know. I don't want
to get into the details, and this won't show up in the later sections.)


Cryptographic Primitives
--------------------------------------------------------------------

The construction of a SFE protocol is going to rely on a few
cryptographic primitives. Again, explaining how to construct these
primitives is very detail heavy, and not worth getting into.

There are two primitives we need: oblivious transfer, and a symmetric
encryption scheme with a few extra properties.

Oblivious Transfer
==========================================================

Oblivious transfer is a way for one party to send information to
the other party without knowing what they're sending. Alice has two
messages $$m_0, m_1$$, and Bob has a bit $$b$$. In oblivious transfer

* Alice offers $$m_0, m_1$$
* Bob offers $$b$$
* Bob receives $$m_0$$ for $$b = 0$$, and $$m_1$$ for $$b = 1$$.
  * Bob does not learn what the other message was
* Alice does not learn which message Bob took.

PICTURE HERE
