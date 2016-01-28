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

*Oblivious transfer* is a way for one party to send information to
the other party without knowing what they're sending. Alice has two
messages $$m_0, m_1$$, and Bob has a bit $$b$$. In oblivious transfer

* Alice offers $$m_0, m_1$$
* Bob offers $$b$$
* Bob receives $$m_0$$ for $$b = 0$$, and $$m_1$$ for $$b = 1$$.
  * Bob does not learn what the other message was
* Alice does not learn which message Bob took.

To use an analogy, imagine oblivious transfer as a pair of black boxes.
Alice puts her two messages into the boxes, and gives them to Bob.
When Bob opens one box, the other box immediately collapses and deletes
its data.

PICTURE HERE

Symmetric Encryption
===========================================================

In *symmetric encryption*, there is an encryption function $$E$$
and a decryption function $$D$$.
For secure function evaluation, we expect $$(E, D)$$ to act like this.

* $$E(k, m)$$ is the encryption of message $$m$$ with key $$k$$.
* $$D(k, c)$$ is the decryption of ciphertext $$c$$ with key $$k$$.
* $$D(k, E(k, m)) = m$$, meaning the same key is used for encyrpting and
decrypting
* Decrypting $$E(k,m)$$ with a different key $$k'$$ results in an error.
* Given ciphertext $$c$$, it is hard to find a pair $$(m, k)$$ such that
encrypting $$m$$ with $$k$$ gives $$c$$.

For notation, I'll sometimes use $$E_k(m) = E(k, m)$$.


Yao's Garbled Circuits
------------------------------------------------------------------------

Garbled circuits were the first construction showing secure computation
was possible. They were first developed by Yao in (CHECK).

Any function $$f$$ has a corresponding circuit $$C$$ which evaluates
it. Every circuit $$C$$ is made up of logic gates, like AND gates, OR gates,
NOT gates, and so on. These gates are connected by wires, which take
values $$0$$ or $$1$$.

PICTURE HERE

We could have Alice send circuit $$C$$ and input $$x$$ to Bob.
Bob could then set the input wires for $$x$$, set the input wires for his own input $$y$$, then
evalute the logic gates of the circuit until all outputs were found.
However, this obviously lets Bob learn what $$x$$ is.

This is where garbling comes in. Instead of sending $$C$$, Alice will
send a garbled circuit $$G(C)$$. This garbled circuit will compute the
same thing as $$C$$ while hiding information about its computation.

Let $$W = \{ w_1, w_2, \cdots, w_n \}$$ be the set of wires in the circuit.
For each wire $$w_i$$, generate two random encryption keys
$$k_i^0$$ and $$k_i^1$$, which will represent $$0$$ and $$1$$.

A garbled circuit is made of *garbled logic gates*. Garbled gates act
the same as regular logic gates, except they use the sampled encryption
keys to represent bits.

For example, suppose we have an OR gate. It has input wires $$w_1,w_2$$
and output wire $$w_3$$. The inputs are bits $$0$$ or $$1$$, and the gate
outputs $$0$$ or $$1$$.

PICTURE HERE

$$
    \begin{array}{ccc}
        w_1 & w_2 & w_3 \\
        0 & 0 & 0 \\
        0 & 1 & 1 \\
        1 & 0 & 1 \\
        1 & 1 & 1
    \end{array}
$$

REDO THIS TABLE

The garbled OR gate instead takes $$k_1^0, k_1^1, k_2^0, k_2^1$$ as input,
and outputs $$k_3^0$$ or $$k_3^1$$. This is done by creating the following
4 values.

$$
    \begin{array}{c}
        E_{k_1^0}(E_{k_2^0}(k_3^0)) \\
        E_{k_1^0}(E_{k_2^1}(k_3^1)) \\
        E_{k_1^1}(E_{k_2^0}(k_3^1)) \\
        E_{k_1^1}(E_{k_2^1}(k_3^1))
    \end{array}
$$

For each pair of input bits, lookup the key for what the output bit should be,
and encrypt it with the keys for both input bits. (This is also known as the
*garbled table* for the logic gate.)

The garbled table has a few nice properties.

* If the receiver has no secret keys, the four values will all be gibberish,
because they have been encrypted.
* If the receiver has the secret keys for the input bits, they can decrypt
exactly one of the four values. (For example, if they have $$k_1^0$$ and
$$k_2^1$$, they can only fully decrypt the $$E_{k_1^0}(E_{k_2^1}(k_3^1))$$
entry.) Furthermore, every other value will decrypt into an error, because
of assumptions on the encryption scheme.
* The one decrypted value holds the key representing the correct output
bit.

And most importantly,

* For every wire, we randomly generate the keys $$k_i^0$$ and $$k_i^1$$.
Both keys are sampled from the same probability distribution. Thus,
given just one key, there is no way to predict the value of the other key.
And, given just one key, there is no way to tell whether it represents
bit $$0$$ or bit $$1$$, because the generating process is identical.

By putting the correct gibberish into a garbled gate, we can get the
correct gibberish out, while having no idea what the bits are like.
This is almost there, with one exception. We want to know what the
circuit outputs are! For the final output wires, we set $$k_i^0 = 0$$
and $$k_i^1 = 1$$. This way, the evaluator will learn only the outputs.

Putting it all together, here is how we can evaluate a garbled circuit.

* We are given a garbled circuit and the keys for the correct input
bits.
* While there is an unevaluated gate where both input keys are known,
take an unevaluated gate.
* Decrypt all four values for that gate. Set the output wire to the
one successfully decrypted value.
* Repeat until all circuit outputs are known (REWRITE)


Putting Together The Protocol
-----------------------------------------------------------------------

The protocol will start with Alice generating the garbled circuit and
sending it to Bob. Alice will also send the keys for her input $$x$$.

However, for Bob to evaluate the garbled circuit, he needs the keys for
his input $$y$$. One way for Bob to get his keys without sending $$y$$
to Alice is to have Alice send both keys for each of $$y$$'s input
wires. For example, if $$y$$ is 3 bits long, and the wires for the
circuit are $$w_4, w_5, w_6$$, Alice could send

$$
    \{ k_4^0, k_4^1, k_5^0, k_5^1, k_6^0, k_6^1 \}
$$

to Bob. However, this has a subtle bug: **it lets Bob evaluate $$f(x,y)$$
with Alice's $$x$$ for any $$y$$.** This could let Bob learn more
information. Going back to the millionaire's problem, where $$x = 10$$
and $$y = 8$$, Bob could run $$f(x,1), f(x,2), f(x,3)$$, and so on
to find the exact wealth of Alice.

Allowing Bob to run the circuit twice is insecure. So, Bob needs to get
only the keys for $$y$$. This is where oblivious transfer comes in.
For each wire $$w_i$$, Alice and Bob do an oblivious transfer. Alice
offer $$k_i^0, k_i^1$$, and Bob offers $$y_i$$, where $$y_i$$ is the
$$i$$th bit of $$y$$.

This gives the final protocol.

* Alice garbles the circuit, sending it to Bob
* Alice sends her input keys
* Alice sends Bob's input keys with oblivous transfer
* Bob evalutes the garbled circuit, getting $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

And thus, it's possible to securely compute any function.

