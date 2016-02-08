---
layout: post
title:  "A Gentle Introduction to Secure Computation"
date:   2016-02-03 18:19:00 -0800
---

In Fall 2015, I took CS 276, a graduate level introduction to theoretical
cryptography. For the final project, I gave a short presentation on secure
computation.

This blog post is adapted from my presentation notes.
The formal proofs of security rely on a lot of background knowledge,
but the core ideas are very clean, and I believe anyone interested
in theoretical computer science can understand them.


What is Secure Computation?
-------------------------------------------------------------------

In secure computation, each party has some private data.
They would like to learn the answer to a question based off everyone's
data. In voting, this is the majority opinion.
In an auction, this is the winning bid. However, they also want to maintain
as much privacy as possible. Voters want to keep their votes secret,
and bidders don't want to publicize how much they're willing to pay.

More formally, there are $$n$$ parties, the $$i$$th party has input $$x_i$$,
and everyone wants to know $$f(x_1, x_2, \cdots, x_n)$$ for some function
$$f$$.
The guiding question of secure computation is this: **when can we
securely compute functions on private inputs without leaking information
about those inputs?**

This post will focus on the two party case, showing that every function
is securely computable with the right computational assumptions. We'll show
this with Yao's garbled circuits.


Problem Setting
-------------------------------------------------------------------

Following crypto tradition, Alice and Bob are two parties.
Alice has private information $$x$$, and Bob has
private information $$y$$. Function $$f(x,y)$$ is a public function
that both Alice and Bob want to know, but
neither Alice nor Bob wants the other party to learn their input.

![problem setup](/public/secure-comp/setup.png)
{: .centered }

The classical example is Yao's Millionaire Problem.
Alice and Bob want to know who has more money.
It's socially unacceptable to brag about
your wealth, so neither wants to say how much money they have. Let
$$x$$ be Alice's wealth, and $$y$$ be Bob's wealth. Then securely computing

$$
    f(x,y) = \begin{cases}
        \text{Alice} & \text{if } x > y \\
        \text{Bob} & \text{if } x < y \\
        \text{same} & \text{if } x = y
    \end{cases}
$$

lets Alice and Bob learn who is richer.

Before going any further, I should explain what security guarantees we're
trying to acheive. We're going to make something secure against *semi-honest*
adversaries, also known as *honest-but-curious*. In the semi-honest model, Alice and Bob
never lie, following the specified protocol exactly.
However, after the protocol, Alice and Bob will analyze the messages received
to try to extract information about the other person's input.

Assuming neither party lies is naive and doesn't give a lot of security in
real life. However, it's still hard to create secure protocols assuming no
lying. Often, semi-honest protocols form a stepping stone towards the malicious
case, where we allow lying. Explaining protocols for malicious adversaries
is outside the scope of this post.


Informal Definitions
-------------------------------------------------------------------

To prove a protocol is secure, we first need to define what security means.
What makes secure computation hard is that Alice and Bob cannot trust
each other. Every message can be analyzed for
information later, so they have to be very careful in what they choose to
send to one another.

Let's make the problem easier.
Suppose there was a trusted third party named Faith.
With Faith, Alice and Bob could compute $$f(x,y)$$ without directly
communicating.

* Alice sends $$x$$ to Faith
* Bob sends $$y$$ to Faith
* Faith computes $$f(x,y)$$ and sends the result back to Alice and Bob

![ideal world](/public/secure-comp/ideal.png)
{: .centered }

This is called the *ideal world*, because it represents the best
case scenario. All communication goes through Faith, who never reveals
the input she received. She only replies with what the parties
want to know, $$f(x,y)$$.

If this is the best case scenario, we should define security by how close
we get to that best case. This gives the following.

**A protocol between Alice and Bob is secure if it is as
secure as the ideal world protocol between Alice, Bob, and Faith.**
{: .centered }

To make this more precise, we need to analyze the ideal world's
security.

Suppose we securely computed $$f(x,y) = x+y$$ in the ideal world.
At the end of communication, Alice knows
$$x$$ and $$x+y$$, while Bob knows $$y$$ and $$x + y$$. If Alice computes

$$
    (x+y) - x
$$

she learns Bob's input $$y$$. Similarly, if Bob computes

$$
    (x+y) - y
$$

he learns Alice's input $$x$$. **Even the ideal world can leak information.**
In an extreme case like this, possibly even the entire input!
If Alice and Bob want to know $$f(x,y) = x + y$$, they have to give up
any hope of privacy.

This is an extreme example, but most functions leak something about
each party.
Going back to the millionaire's problem, suppose Alice has $$10$$
dollars and Bob has $$8$$ dollars. They securely compute who has the
most money, and learn Alice is richer. At this point,

* Alice knows Bob has less than $$10$$ dollars because she's richer.
* Bob knows Alice has more than $$8$$ dollars because he's poorer.

However, there is still some privacy: neither knows the exact wealth of the other.

Since $$f(x,y)$$ must be given to Alice and Bob, the best we can do is
learn nothing more than what was learnable from $$f(x,y)$$. This
gives the final definition.

**A protocol between Alice and Bob is secure if Alice learns
only information computable from $$x$$ and $$f(x,y)$$, and Bob learns only
information computable from $$y$$ and $$f(x,y)$$**
{: .centered }

(Side note: if you've seen zero-knowledge proofs, this may seem familiar.
If you haven't, don't worry, it won't show up in later sections.)

Armed with a security definition, we can start constructing the
protocol. Before doing so, we'll need a few cryptographic assumptions.


Cryptographic Primitives
--------------------------------------------------------------------

All of theoretical cryptography rests on assuming some problems are harder
than other problems. These problems form the cryptographic primitives,
which can be used for constructing protocols.

For example, one cryptographic primitive is the one-way function. Abbreviated
OWF, these functions are easy to compute, but hard to invert, where easy
means "doable in polynomial time" and hard means "not doable in polynomial
time." Assuming OWFs exist, we can create secure encryption, pseudorandom
number generators, and many other useful things.

No one has proved one-way functions exist, because proving that would
prove $$P \neq NP$$, and that's, well, a really hard problem, to put it
mildly. However, there are several functions that people believe to be
one-way, which are the ones used in practice.

For secure computation, we need two primitives: oblivious transfer, and symmetric
encryption.


Oblivious Transfer
==========================================================

*Oblivious transfer* (abbreviated OT) is a special case of secure computation.
Alice has two messages $$m_0, m_1$$. Bob has a bit $$b$$.
For now, we treat oblivious transfer as a black box method where

* Alice gives $$m_0, m_1$$
* Bob gives bit $$b$$, 0 or 1
* If $$b = 0$$, Bob gets $$m_0$$. Otherwise, he gets $$m_1$$. In
both cases, Bob does not learn the other message.
* Alice does not learn which message Bob received.
She only knows Bob got one of them.

![Oblivious transfer](/public/secure-comp/ot.png)
{: .centered }

You can think of the OT box as a trusted third party, like Faith.
Letting Alice send messages without knowing which message was
received will be key to the secure computation protocol. I don't want to get into
the details of implementing OT with just Alice and Bob, since they aren't
that interesting.
If you're curious, [Wikipedia has a good example based on RSA](https://en.wikipedia.org/wiki/Oblivious_transfer#1-2_oblivious_transfer).


Symmetric Encryption
===========================================================

*Symmetric encryption* allows two people to send encrypted messages that cannot
be decrypted without the secret key. Formally, a symmetric encryption scheme
is a pair of functions, encrypter $$E$$ and decrypter $$D$$, such that

* $$E_k(m)$$ is the encryption of message $$m$$ with key $$k$$.
* $$D_k(c)$$ is the decryption of ciphertext $$c$$ with key $$k$$.
* Decrypting with the same secret key gives the original message, or
$$D_k(E_k(m)) = m$$,
* Given just ciphertext $$c$$, it is hard to find a key $$k$$ and message $$m$$
such that $$E_k(m) = c$$. (Where again, hard means not solvable in polynomial
time.)

For garbled circuits, we'll need one more property.

* Decrypting $$E_k(m)$$ with a different key $$k'$$ results in an error.

With all that out of the way, we can finally start talking about the protocol
itself.


Yao's Garbled Circuits
------------------------------------------------------------------------

Secure computation was first formally introduced by Andrew Yao in the early
1980s. His introductory paper demonstrated protocols for a few examples,
but did not prove every function was securely computable. That didn't
happen until 1986, with the construction of Yao's garbled circuits.

To prove every function was securely computable,
Yao proved every circuit was securely computable.
Every function can be converted to an
equivalent circuit, and we'll see that working in the circuit model of
computation makes the construction simpler.


A Quick Circuit Primer
========================================================================

For any function $$f(x,y)$$, there is some circuit $$C$$ such that
$$C(x,y)$$ gives the same output.
That circuit $$C$$ is made up of logic gates and wires connecting them.
Each logic gate has two input wires and one output wire, and computes
a simple Boolean function, like AND or OR.

The wires in a circuit can be divided into three categories: inputs for
the circuit, outputs for the circuit, and intermediate wires between gates.

![example circuit](/public/secure-comp/circuit.png)
{: .centered }


Garbling Circuits
========================================================================

Here is a very obviously insecure protocol for computing $$f(x,y)$$

* Alice sends circuit $$C$$ to Bob.
* Alice sends her input $$x$$ to Bob.
* Bob evaluates the circuit to
get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

![First protocol](/public/secure-comp/protocol1.png)
{: .centered }

This works, but Alice has to send $$x$$ to Bob.

This is where garbling comes in. Instead of sending $$C$$, Alice will
send a garbled circuit $$G(C)$$. Instead of sending $$x$$, she'll
send $$x$$ encoded in a certain way.
It will be done such that Bob can evaluate $$G(C)$$ with Alice's
encoded input, without learning what Alice's original input $$x$$ was, and
without exposing any wire values except for the final output.

Number the wires of the circuit as $$w_1, w_2, \cdots$$.
For each wire $$w_i$$, generate two random encryption keys
$$k_{i,0}$$ and $$k_{i,1}$$. These will represent $$0$$ and $$1$$.

A garbled circuit is made of *garbled logic gates*. Garbled gates act
the same as regular logic gates, except they operate on the sampled encryption
keys instead of bits.

To give a concrete example, suppose we want to garble an OR gate.
It has input wires $$w_1,w_2$$, and output wire $$w_3$$.

![OR gate](/public/secure-comp/or.png)
{: .centered }

The logic gate table is

$$
    \begin{array}{ccc}
        w_1 & w_2 & w_3 \\
        0 & 0 & 0 \\
        0 & 1 & 1 \\
        1 & 0 & 1 \\
        1 & 1 & 1
    \end{array}
$$

The garbled OR gate instead takes $$k_{1,0}, k_{1,1}$$ for $$w_1$$, and
$$k_{2,0}, k_{2,1}$$ for $$w_2$$. The output is $$k_{3,0}$$ or $$k_{3,1}$$,
depending on which bit the gate is supposed to return.
For example, $$0 \text{ OR } 1 = 1$$, so inputs $$k_{1,0}, k_{2,1}$$ should
give output $$k_{3,1}$$. Using symmetric encryption, encrypt the correct
output with both keys. Doing this for all possible inputs gives the
*garbled table*.

$$
    \begin{array}{c}
        E_{k_{1,0}}(E_{k_{2,0}}(k_{3,0})) \\
        E_{k_{1,0}}(E_{k_{2,1}}(k_{3,1})) \\
        E_{k_{1,1}}(E_{k_{2,0}}(k_{3,1})) \\
        E_{k_{1,1}}(E_{k_{2,1}}(k_{3,1}))
    \end{array}
$$

The garbled table has a few nice properties.

* Without a secret key for each input wire, Bob cannot read any of the given
values, because he can't break the encryption.
* With one secret key for each wire, Bob can get the correct output
by attempting to decrypt all 4 values. Going back to the $$0 \text{ OR } 1 = 1$$
example, assume Bob has $$k_{1,0}$$ and $$k_{2,1}$$. Bob first decrypts with
$$k_{1,0}$$. He'll successfully decrypt exactly two values, and will get
an error on the other two.

    $$
    \begin{array}{c}
        E_{k_{2,0}}(k_{3,0}) \\
        E_{k_{2,1}}(k_{3,1}) \\
        \text{error} \\
        \text{error}
    \end{array}
    $$

    Decrypting the two remaining messages with $$k_{2,1}$$ gives

    $$
    \begin{array}{c}
        \text{error} \\
        k_{3,1} \\
        \text{error} \\
        \text{error}
    \end{array}
    $$

    getting the key corresponding to output bit $$1$$ for wire $$w_3$$.

(To be fully correct, we also shuffle the garbled table, to make sure
the position of the decrypted message doesn't leak anything.)

Creating the garbled table for every logic gate in the circuit gives the
garbled circuit. Informally, here's why the garbled circuit can be
evaluated securely.

* Given the input keys, Bob can evaluate the garbled gates in turn.
Each garbled gate can return only the correct value, so when Bob
gets to the output wires, he must have the correct output.
* Both $$k_{i,0}$$ and $$k_{i,1}$$ are generated randomly. Given just
one of them, Bob has no way to tell whether the key he has represents
$$0$$ or $$1$$. (Alice knows, but Alice isn't the one evaluating the circuit.)

Thus, from Bob's perspective, he's evaluating the circuit by passing gibberish
to each garbled gate and getting gibberish out. He's still doing the
computation - he just has no idea what bits he's actually looking at.

(The one minor exception is key generation for the output wires of the
circuit. Instead of generating random keys, Alice uses the raw bit
$$0$$ or $$1$$, since Alice needs Bob to learn the circuit output bits.)


The Last Step
==============================================================================

Here's the new protocol, with garbled circuits

* Alice garbles circuit $$C$$ to get garbled circuit $$G(C)$$
* Alice sends $$G(C)$$ to Bob.
* Alice sends the keys for her input $$x$$ to Bob.
* Bob combines them with the input keys for $$y$$, and
evaluates $$G(C)$$ to get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

![Second protocol](/public/secure-comp/protocol2.png)
{: .centered }

There's still a problem. How does Bob
get the input keys for $$y$$? Only Alice knows the keys created for each wire.
Bob could give Alice his input $$y$$ to get the right keys, but then
Alice would learn $$y$$.

One solution is to have Alice send both keys for each of $$y$$'s input
wires to Bob. For each wire, Bob can then pick the key corresponding to
the correct bit of $$y$$. That way, Bob doesn't have to give
Alice $$y$$, but can still run the circuit.

However, this has a subtle bug: by giving Bob both keys for his input
wires, **Bob can run the circuit with an arbitrary $$y$$.**
Letting Bob evaluate $$f(x,y)$$ many times gives Bob more information.
Going back to the millionaire's problem, let $$x = 10$$
and $$y = 8$$. At the end, Bob learns Alice is richer, meaning $$x > 8$$.
But, if he later evaluate $$f(x, 9)$$, he'll learn $$x > 9$$, which is more
than he should know.

Thus, to be secure, Bob should only get to run the circuit on exactly
$$x,y$$. To do so, he needs to get the keys for $$y$$, and only the keys
for $$y$$, without Alice learning which keys he wants. If only there was a way
for Alice to obliviously transfer those keys...

Alright, yes, that's why we need oblivious transfer. Using oblivious transfer
to fill in the gap, we get the final protocol.

* Alice garbles circuit $$C$$ to get garbled circuit $$G(C)$$
* Alice sends $$G(C)$$ to Bob.
* Alice sends the keys for her input $$x$$ to Bob.
* Using oblivious transfer, for each of Bob's input wires,
Alice sends $$k_{i,y_i}$$ to Bob.
* With all input keys, Bob can evaluate the circuit to get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

![Final protocol](/public/secure-comp/protocol3.png)
{: .centered }

This lets Alice and Bob compute $$f(x,y)$$ without leaking their
information, and without trusted third parties.


Conclusion
------------------------------------------------------------------------

This protocol is mostly a theoretical exercise. However, there has been
[recent work](https://www.cs.uic.edu/pub/Bits/PeterSnyder/Peter_Snyder_-_Garbled_Circuits_WCP_2_column.pdf)
to make it fast enough for practical use. It's still tricky to use, because
the desired function needs to be converted into an equivalent
circuit.

Despite this difficulty, Yao's garbled circuits are still a very important
foundational result. In a post-Snowden world, interest in cryptography
is very high, and there's a lot of usefulness to designing protocols
with decentralized trust, from Bitcoin to [secure cloud storage](https://css.csail.mit.edu/cryptdb/). It's all very interesting,
and I'm sure something cool is just around the corner.

