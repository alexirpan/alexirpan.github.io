---
layout: post
title:  "A Gentle Introduction to Secure Computation"
date:   2016-02-03 18:19:00 -0800
---

In Fall 2015, I took CS 276, a graduate level introductio to theoretical
cryptography. For the final project, I gave a short presentation on secure
computation.

This blog post is adapted from my presentation notes.
Although proving security formally relies on a lot of background knowledge,
the core ideas are very clean, and I believe anyone with a passing interest
in theoretical computer science can understand them.

\*\*\*
{: .centered }


What is Secure Computation?
-------------------------------------------------------------------

In secure computation, parties have some private information.
They would like to learn the answer to a question based off everyone's
information, while keeping their information private.
For example, in cryptographic voting, every party
has a private vote for a candidate. Everyone wants to know who the
majority winner is, but everyone also wants to keep their vote secret.

The guiding question of secure computation is this: **under what assumptions
is it possible to compute functions without leaking private input?**
This post will focus on showing any function is securely computable
in the two party case, through Yao's garbled circuits.

Problem Setting
-------------------------------------------------------------------

Following crypto tradition, Alice and Bob are two parties.
Alice has private information $$x$$, and Bob has
private information $$y$$. Function $$f(x,y)$$ is a public function
that both Alice and Bob want to know, but
neither Alice nor Bob wants the other party to learn their private inputs.

PICTURE HERE

The classical example from the first paper exploring this is Yao's
Millionaire Problem. In this example,
Alice and Bob are both very rich, and want to know who has
more money. At the same time, it's socially unacceptable to brag about
your wealth, so neither wants to say how much money they have. Let
$$x$$ be Alice's wealth, and $$y$$ be Bob's wealth. Then they want
to securely compute

$$
    f(x,y) = \begin{cases}
        \text{Alice} & \text{if } x > y \\
        \text{Bob} & \text{if } x < y \\
        \text{same} & \text{if } x = y
    \end{cases}
$$

Before going any further, we first need to set up ground rules on
what security guarantees we have. We're
going to assume adversaries are *semi-honest*, or
*honest-but-curious*. In the semi-honest model, Alice and Bob
will never lie, following protocol exactly. (That's the "honest" part.)
After they finish communicating, Alice and Bob will attempt to learn
about the other party's input by analyzing the messages they received.
(That's the "curious" or "semi-honest" part.)

Assuming neither party lies sounds hopelessly naive, but it's still
tricky to show secure computation is possible for semi-honest
adversaries. It turns out many semi-honest protocols can be extended to ones
that are safe against lying adversaries; proving how to do that
is above the scope of this post.


Information Leakage
-------------------------------------------------------------------

To prove a protocol is secure, we first need to define what it means to be
secure.

The hard part of secure computation is that Alice and Bob cannot trust
each other. Every message sent between the two can be analyzed for
information later. How are Alice and Bob supposed to share enough to
evaluate $$f$$ without giving up something about their inputs?

Well, let's make the problem easier.
Suppose there was a trusted third party named Faith.

PICTURE HERE

With a trusted third party, secure computation is easy.

* Alice sends $$x$$ to Faith
* Bob sends $$y$$ to Faith
* Faith computes $$f(x,y)$$, and send the result back to Alice and Bob

PICTURE HERE.

This is called the *ideal world*, because it represents the best
case scenario. Note that Alice and Bob never communicate to each other
directly. All communication goes through Faith, and Faith gives back
only what that party should know. (That is, Faith only gives back
$$f(x,y)$$.)

This gives the first attempt at a definition.

**A computation protocol between Alice and Bob is secure if it is as
secure as the ideal world protocol between Alice, Bob, and Faith.**
{: .centered }

This is a good first step, but now we need to look at how secure the
ideal world protocol is.

There's a very important subtlety here. **Even the ideal world can leak
information about Alice and Bob's inputs.** Suppose we tried to securely
compute $$f(x,y) = x+y$$. At the end of communication, Alice knows
$$x$$ and $$x+y$$, while Bob knows $$y$$ and $$x + y$$. If Alice computes

$$
    (x+y) - x
$$

she learns Bob's input $$y$$. Similarly, if Bob computes

$$
    (x+y) - y
$$

he learns Alice's input $$x$$. **If Alice and Bob want to compute
$$x + y$$, no protocol can hide their original inputs.** Any secure computation
protocol has to give Alice and Bob $$x+y$$, and that's all they need.

This is an extreme example, but simiar things can happen for other functions too.
Going back to the millionaire's problem, suppose Alice has $$10$$
dollars and Bob has $$8$$ dollars. They securely compute who has the
most money, and both learn Alice is richer. At this point,

* Alice knows she has more money than Bob. Therefore, Alice knows Bob has less than $$10$$ dollars.
* Bob knows he has less money than Alice. Therefore, Bob knows Alice has more than $$8$$ dollars.

However, there is still some privacy: neither knows the exact wealth of the other.
They only have upper and lower bounds on the other's wealth.

Computing $$f(x,y)$$ may leak information about $$x$$ and $$y$$, but it's a
necessary evil if Alice and Bob want to compute $$f$$.

If the ideal world with Faith is the best we can do, thenthen we should expect the real protocol
(the one where Faith doesn't exist) to act the same.
This gives the following definition of security.

**A computation protocol between Alice and Bob is secure if Alice learns
only information computable from $$x$$ and $$f(x,y)$$, and Bob learns only
information computable from $$y$$ and $$f(x,y)$$**
{: .centered }

(Side note: if you're familiar with zero-knowledge proofs, security is formally
defined in a similar way, using simulators. If you aren't familiar with
zero-knowledge proofs, don't worry, this won't show up in later sections.)

Now that we have a definition of security, we can start constructing the
protocol. Before doing so, we'll need to assume the existence of a few cryptographic
primitives.


Cryptographic Primitives
--------------------------------------------------------------------

Pretty much all of theoretical cryptography rests on assuming specific
primitive operations are possible. For example, many things assume the existence
of one-way functions. These functions are computable in polynomial time, but
cannot be inverted in polynomial time. The reason the field assumes OWFs
exist instead of proving them is because their existence is equivalent to
proving $$P \neq NP$$, and that's, well, really really hard.

There are two primitives we need: oblivious transfer, and symmetric
encryption with a few extra properties. For both, I do not plan to explain
how to implement these. You'll have to assume or take it on faith that it's
possible to do this.


Oblivious Transfer
==========================================================

*Oblivious transfer* is a way for one party to send information to
the other party without knowing what they're sending. Alice has two
messages $$m_0, m_1$$, and Bob has a bit $$b$$. In oblivious transfer,

* Alice offers $$m_0, m_1$$
* Bob offers $$b$$
* If $$b = 0$$, Bob receives $$m_0$$. Otherwise, he receives $$m_1$$. In
either case, Bob does not learn the other message.
* Alice does not learn which message Bob took.

At the end of the protocol, Alice knows Bob took one of the messages, but
doesn't know which one. And Bob knows Alice had two messages, but only got
to see one.

Again, I won't explain how to construct OT. If you want, Wikipedia has
an example that works assuming RSA is secure. (LINK)


Symmetric Encryption
===========================================================

In *symmetric encryption*, there is an encryption function $$E$$
and a decryption function $$D$$, such that

* $$E(k, m)$$ is the encryption of message $$m$$ with key $$k$$.
* $$D(k, c)$$ is the decryption of ciphertext $$c$$ with key $$k$$.
* $$D(k, E(k, m)) = m$$, meaning the same key is used for encyrpting and
decrypting
* Given just ciphertext $$c$$, it is hard to find a pair
$$(m, k)$$ such that $$E(k, m) = c$$.

The above is part of all standard definitions. For garbled circuits, we'll
need one more property.

* Decrypting $$E(k,m)$$ with a different key $$k'$$ results in an error.
(In principle, an attacker could try keys until they found the one that didn't
cause an error, but there are exponentially many keys, so this attack doesn't
matter.)

To save on notation, I'll use $$E_k(m)$$ to mean $$E(k, m)$$ from here on out.


Yao's Garbled Circuits
------------------------------------------------------------------------

To prove an arbitrary function is securely computable, we need a proof method
that is independent of the function. There are infinitely many computable
functions, so trying to do anything on a case by case based is doomed
to failure.

The solution is to prove things based on a specific model of computation.
For instance, every computable function is representable by a Turing machine.
If we showed a Turing machine can be computed securely, then every computable
function can be computed securely. It turns out the easiest model of
computation to prove security for is the circuit model.

Garbled circuits were the first construction showing secure computation
was possible. They were first developed by Yao in (CHECK).

For any function $$f$$, there is some circuit $$C$$ that evaluates it.
Every circuit $$C$$ is made up of logic gates, like AND gates, OR gates,
NOT gates, etc. These gates are connected by wires. Some are input wires,
and some are output wires. When given input, the logic gates take their
inputs, compute their outputs, and send them to the next gate, until
all output wires are decided.

PICTURE HERE

Given the circuit $$C$$ for $$f$$, Alice could send $$C$$ and input bits
$$x$$ to Bob. Bob could then set the input wires for $$x$$, add his own
input $$y$$, and evaluate $$C$$.
However, this obviously lets Bob learn what $$x$$ is, and isn't secure.

This is where garbling comes in. Instead of sending $$C$$, Alice will
send a garbled circuit $$G(C)$$. This garbled circuit will return the
same outputs as $$C$$, but can be computed by Bob while
hiding information about its computation.

Let $$W = \{ w_1, w_2, \cdots, w_n \}$$ be the set of wires in the circuit.
For each wire $$w_i$$, generate two random encryption keys
$$k_i^0$$ and $$k_i^1$$, which will represent $$0$$ and $$1$$.

A garbled circuit is made of *garbled logic gates*. Garbled gates act
the same as regular logic gates, except they operate on sampled encryption
keys instead of bits.

To give a concrete example, take an OR gate.

PICTURE HERE

It has input wires $$w_1,w_2$$, and output wire $$w_3$$. The gate table
is

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

The garbled OR gate instead takes $$k_1^0, k_1^1$$ for $$w_1$$, and
$$k_2^0, k_2^1$$ for $$w_2$$. The output is $$k_3^0$$ or $$k_3^1$$,
and the output returned is based on what the gate is supposed to return.
For example, because $$0 OR 1 = 1$$, inputs $$k_1^0, k_2^1$$ should
give output $$k_3^1$$. Doing this for all input pairs gives
these 4 values.

$$
    \begin{array}{c}
        E_{k_1^0}(E_{k_2^0}(k_3^0)) \\
        E_{k_1^0}(E_{k_2^1}(k_3^1)) \\
        E_{k_1^1}(E_{k_2^0}(k_3^1)) \\
        E_{k_1^1}(E_{k_2^1}(k_3^1))
    \end{array}
$$

This is known as the *garbled table* for the logic gate.
The garbled table has a few nice properties.

* If the receiver has no secret keys, the 4 values will all be gibberish,
because they have been encrypted.
* If the receiver has one secret key for each wire, they can get the correct output
by attempting to decrypt all 4 values. Going back to the $$0 OR 1 = 1$$
example, the receiver has $$k_1^0, k_2^1$$. They first decrypt with
$$k_1^0$$. They'll be able to decrypt exactly two values, and will fail
on the rest because decrypting with the wrong key gives an error.

$$
    \begin{array}{c}
        E_{k_2^0}(k_3^0)) \\
        E_{k_2^1}(k_3^1)) \\
        \text{error} \\
        \text{error}
    \end{array}
$$

Decrypting the two remaning messages with $$k_2^1$$ gives

$$
    \begin{array}{c}
        \text{error} \\
        k_3^1 \\
        \text{error} \\
        \text{error}
    \end{array}
$$

So, exactly one value is decryptable, and the final message received
is the correct key $$k_3^1$$. That key can then be used to decrypt the next
gate wire 3 leads to. The one exception is if the output wire
of a gate is an output wire of the circuit. In that case, instead of
generating a random key, set $$k_i^0 = 0$$ and $$k_i^1 = 1$$. (This makes
sure the output is public.)

This garbled circuit is secure. I don't want to prove it formally, but
here's the intuition.

* For every wire, we randomly generate $$k_i^0$$ and $$k_i^1$$.
Both keys are generated independently, so learning $$k_i^0$$ tells you
nothing about $$k_i^1$$, and vice versa. It also doesn't tell you
whether your key repesents bit $$0$$ or $$1$$; the only one who knows
that is the person who makes the garbled circuit.
* When evaluating each garbled gate, every garbled table will have
exactly 4 values. Of those 4, exactly 2 are decyrptable by the first key,
and exactly 1 of those 2 is decryptable by the second. So, given just
the garbled table, you cannot tell whether the original gate was an
AND gate or an OR gate.


By giving a garbled circuit the correct input gibberish, we can evalute each
logic gate, seeing gibberish on every intermediate wire. The only meaningful
messages we see are the final output bits. Thus, Bob can
evaluate $$C$$ without exposing any intermediate values, as long as Bob
gets the right input keys.


Input Key Transfer
-----------------------------------------------------------------------

The protocol will start with Alice generating the garbled circuit and
sending it to Bob. Alice will also send the keys for her input $$x$$.

However, for Bob to evaluate the garbled circuit, he needs the keys for
his input $$y$$. One way for Bob to get his keys without sending $$y$$
to Alice is to have Alice send both keys for each of $$y$$'s input
wires to Bob. That way, Bob can pick the keys he needs to run
the circuit, and Alice doesn't know which key Bob picked.

However, this has a subtle bug: **it lets Bob evaluate $$f(x,y)$$
with Alice's $$x$$ for any $$y$$.** This could let Bob learn more
information. Going back to the millionaire's problem, where $$x = 10$$
and $$y = 8$$, Bob could run $$f(x,1), f(x,2), f(x,3), \cdots$$, until
he found the threshold where Bob's input is larger. That lets Bob
find Alice's exact wealth, which breaks security.

Bob should only be able to run the circuit for his fixed $$y$$, and
nothing else. This is why oblivious transfer is necessary. With oblivious
transfer, Bob can ask for exactly the keys he needs for $$y$$. Alice
can provide the keys without knowing which one Bob takes, and Bob cannot
take more keys than he needs for exactly one evaluation.

This gives the final protocol.

* Alice garbles the circuit, sending it to Bob
* Alice sends the keys for her input wires.
* For each of Bob's input wires, Alice sends Bob the correct input
key with oblivous transfer
* Bob evalutes the garbled circuit, getting $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

And now Alice and Bob can learn whose richer, without publicizing their
wealth, and with no trusted third parties.


Implications
------------------------------------------------------------------------

This protocol has a few nice properties, the nicest being that this uses
a constant number of messages (or rounds). The actual network cost is big,
because Alice needs to send the entire garbled circuit, but this means there
is minimal connection overhead.

Although this protocol is mostly a theoretical exercise, it is usable in practice.
Current implementations can securely compute circuits with about a billion gates.
However, you do need to build the ciruit for the evaluated function, which is its
own can of worms.

The most important part of this protocol is not its real world usability. It's
important *because it shows secure computation is possible for arbitrary functions.*
Before Yao's garbled circuits, it wasn't clear the problem was even solvable.
From general secure computation, you can get many interesting corollaries.

* In the circuit model of computation, there is a universal circuit $$U$$ such that
given circuit $$C$$ and input $$x$$, $$U(C,x)$$ returns $$C(x)$$. Have Alice
give $$C, x$$, and Bob give nothing. Bob can now securely compute $$C(x)$$,
learning as little about $$C$$ or $$x$$ as possible. Now, Alice could have
evaluated $$C(x)$$ by herself, because she knows both inputs. But, suppose Alice
is a client, and Bob is a Google or Amazon datacenter. Alice can leverage
the power of cloud computing, *without telling the cloud provider what she
wants to compute*.
* This is the two-party computation (2PC) case. There are protocols for the
multiparty computation (MPC) case, which has its own useful conclusions. Suppose
a group of $$n$$ people want to elect one of two candidates. This gives the
function

$$
    f(x_1, x_2, \ldots, x_n) = \begin{cases}
        0 & \text{ if more votes are for candidate} 0 \\
        1 & \text{ if more votes are for candidate} 1
    \end{cases}
$$

This lets the group find the majority opinion, without leaking anyone's vote.
As you might imagine, voter privacy is a really big deal.
* Although the millionaire problem is quite silly, there's a similar problem
that's actually useful: electronic auctions. One common auction format is
the Vickrey auction. Everyone submits a bid simulatenously, and whoever bid
the highest wins. But, they only pay the second-highest bid (the reasoning being
that it is more fair to the buyer if they pay as little above the second-highest
bid as possible.) Secure computation lets bidders place bids secretly without
a trusted third party.
