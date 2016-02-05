---
layout: post
title:  "A Gentle Introduction to Secure Computation"
date:   2016-02-03 18:19:00 -0800
---

In Fall 2015, I took CS 276, a graduate level introduction to theoretical
cryptography. For the final project, I gave a short presentation on secure
computation.

This blog post is adapted from my presentation notes.
Formal proofs of security rely on a lot of background knowledge,
but the core ideas are very clean, and I believe anyone interested
in theoretical computer science can understand them.

\*\*\*
{: .centered }


What is Secure Computation?
-------------------------------------------------------------------

In secure computation, each party have some private information.
They would like to learn the answer to a question based off everyone's
information. In cryptographic voting, this is the majority opinion.
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
is securely computable with the right computational assumptions. We'll do
this through Yao's garbled circuits.


Problem Setting
-------------------------------------------------------------------

Following crypto tradition, Alice and Bob are two parties.
Alice has private information $$x$$, and Bob has
private information $$y$$. Function $$f(x,y)$$ is a public function
that both Alice and Bob want to know, but
neither Alice nor Bob wants the other party to learn their private inputs.

PICTURE HERE

The classical example is Yao's
Millionaire Problem.
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

Before going any further, we need to set up ground rules on
what security guarantees we want to acheive. We're
going to assume adversaries are *semi-honest*, also known as
*honest-but-curious*. In the semi-honest model, Alice and Bob
never lie, following the specified protocol exactly. (That's the "honest" part.)
However, after they finish communicating, Alice and Bob can go back over the
messages received, and try to extract information about the other person's input.
(That's the "curious" or "semi-honest" part.)

Assuming neither party lies sounds naive, but it's good enough for some settings.
From a historical perspective, Yao's garbled circuits were the first protocol
that showed secure computation was possible at all. They form a stepping stone
towards protocols safe against malicious adversaries; explaining those protocols
is above the scope of this post.


Informal Definitions
-------------------------------------------------------------------

To prove a protocol is secure, we first need to define what security means.
What makes secure computation hard is that Alice and Bob cannot trust
each other. Every message can be analyzed for
information later, so they have to be very careful in what they choose to
send to each other.

For now, secure computation looks tricky, so let's make the problem easier.
Suppose there was a trusted third party named Faith.

PICTURE HERE

With a trusted third party, Alice and Bob can compute $$f(x,y)$$ without
ever talking to one another.

* Alice sends $$x$$ to Faith
* Bob sends $$y$$ to Faith
* Faith computes $$f(x,y)$$, and send the result back to Alice and Bob

PICTURE HERE.

This is called the *ideal world*, because it represents the best
case scenario. All communication goes through Faith, who never reveals
input received to the other party. She only replies with what the parties
want to know, $$f(x,y)$$.

If this is the best case scenario, we should try to define security by how close
we get to the optimum. This gives the following.

**A protocol between Alice and Bob is secure if it is as
secure as the ideal world protocol between Alice, Bob, and Faith.**
{: .centered }

This is a good first step, but now we need to look at how secure the
ideal world protocol is.

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

he learns Alice's input $$x$$. **Even the ideal world can leak information,
possibly even the entire input.** If they want to know $$f(x,y) = x + y$$,
neither Alice nor Bob can hide $$x$$ or $$y$$.

This is an extreme example, but most functions leak *something*.
Going back to the millionaire's problem, suppose Alice has $$10$$
dollars and Bob has $$8$$ dollars. They securely compute who has the
most money, and learn Alice is richer. At this point,

* Alice knows Bob has less than $$10$$ dollars because she's richer.
* Bob knows Alice has more than $$8$$ dollars because he's poorer.

However, there is still some privacy: neither knows the exact wealth of the other.

If the ideal world with Faith is the best we can do, then we should expect a
world without Faith to act the same. $$f(x,y)$$ must be given to Alice and
Bob, giving the final definition.

**A computation protocol between Alice and Bob is secure if Alice learns
only information computable from $$x$$ and $$f(x,y)$$, and Bob learns only
information computable from $$y$$ and $$f(x,y)$$**
{: .centered }

(Side note: this is an informal defintion. The true definitions use
simulators, like zero-knowledge proofs. Don't worry if this doesn't make sense,
it won't show up in later sections.)

Armed with a security definition, we can start constructing the
protocol. Before doing so, we'll need a few cryptographic assumptions.


Cryptographic Primitives
--------------------------------------------------------------------

All of theoretical cryptography rests on assuming there exist problems that
cannot be solved in polynomial time. These form the cryptographic primitives,
which can be used when constructing protocols.

For example, one common cryptographic
primitive is one-way functions, or OWFs. These functions are easy to compute, but
hard to invert. We have to assume OWFs exist because proving they exist would
let us prove $$P \neq NP$$, and that's, well, a really hard problem, to put it
mildly.

For secure computation, we need two primitives: oblivious transfer, and symmetric
encryption. For both, we have candidates for how to implement them, but we cannot
prove their security, and I don't want to get into the details of how to
construct them. You'll have to take it on faith that these exist.


Oblivious Transfer
==========================================================

*Oblivious transfer* is a special case of secure computation.
Alice has two messages $$m_0, m_1$$. Bob has a bit $$b$$.
In oblivious transfer,

* Alice offers $$m_0, m_1$$
* Bob offers $$b$$
* If $$b = 0$$, Bob receives $$m_0$$. Otherwise, he receives $$m_1$$. In
both cases, Bob does not learn the message he didn't take.
* Alice does not learn which message Bob took. She only learns that Bob
took one of them.

With oblivious transfer, Alice can send a message to Bob without knowing
which message Bob picked, and Bob can choose between messages while only
learning about the message he eventually picks.

Again, I won't explain the details, but [Wikipedia has a good example
of oblivious transfer based on RSA](https://en.wikipedia.org/wiki/Oblivious_transfer#1-2_oblivious_transfer).


Symmetric Encryption
===========================================================

*Symmetric encryption* allows two people to send messages that cannot
be decrypted without the secret key. There is an encryption function $$E$$
and a decryption function $$D$$, such that

* $$E(k, m)$$ is the encryption of message $$m$$ with key $$k$$.
* $$D(k, c)$$ is the decryption of ciphertext $$c$$ with key $$k$$.
* Decrypting with the same key used to encrypt gives the original message, or
$$D(k, E(k, m)) = m$$,
* Given just ciphertext $$c$$, it is hard to find a key $$k$$ and message $$m$$
such that $$E(k, m) = c$$. (In cryptography, hard means
not solvable in polynomial time.)

For garbled circuits, we'll need one more property.

* Decrypting $$E(k,m)$$ with a different key $$k'$$ results in an error.

To save on notation, I'll use $$E_k(m)$$ to mean $$E(k, m)$$ from here on out.


A Quick Circuit Primer
------------------------------------------------------------------------

Yao's garbled circuits were the first protocol showing every function
was securely computable. They were first developed in 1982.

To prove every function is securely computable, we instead prove every
circuit is securely computable. Working with the circuit model of
computation makes the construction much easier.

For any function $$f(x,y)$$, there is some circuit $$C$$ such that
$$C(x,y)$$ gives the same output.
That circuit $$C$$ is made up of logic gates and wires connecting them.
Each logic gate has two input wires and one output wire, computing a simple Boolean function,
like AND or OR. Those outputs are then fed as inputs to another gate
in the circuit.

PICTURE HERE

The wires in a circuit can be divided into three categories: inputs for
the circuit, outputs for the circuit, and intermediate wires between gates.

PICTURE?


Garbled Circuits
------------------------------------------------------------------------

Here is a very obviously insecure protocol for computing $$f(x,y)$$

* Alice sends circuit $$C$$ to Bob.
* Alice sends her input $$x$$ to Bob.
* Bob takes $$x$$, adds his input $$y$$, and evaluates the circuit to
get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

This works, but Alice has to send $$x$$ to Bob.

This is where garbling comes in. Instead of sending $$C$$ to Bob, Alice will
send the garbled circuit $$G(C)$$, then her input $$x$$ encoded in a certain
way. It will be constructed such that Bob can evaluate $$G(C)$$ with Alice's
encoded input, without learning what Alice's original input $$x$$ was, and
without exposing any wire values except for the final output $$f(x,y)$$.

Let $$W = \{ w_1, w_2, \cdots, w_n \}$$ be the set of wires in the circuit.
For each wire $$w_i$$, generate two random encryption keys
$$k_{i,0}$$ and $$k_{i,1}$$. These will represent $$0$$ and $$1$$.

A garbled circuit is made of *garbled logic gates*. Garbled gates act
the same as regular logic gates, except they operate on the sampled encryption
keys instead of bits.

To give a concrete example, suppose we want to garble an OR gate.
It has input wires $$w_1,w_2$$, and output wire $$w_3$$.

PICTURE HERE

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

REDO THIS TABLE

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
values because they have been encrypted.
* With one secret key for each wire, Bob can get the correct output
by attempting to decrypt all 4 values. Going back to the $$0 \text{ OR } 1 = 1$$
example, assume Bob has $$k_{1,0}$$ and $$k_{2,1}$$. Bob first decrypts with
$$k_{1,0}$$. He'll successfully decrypt exactly two values, and will get
an error on the other two.

$$
    \begin{array}{c}
        E_{k_{2,0}}(k_{3,0})) \\
        E_{k_{2,1}}(k_{3,1})) \\
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

Creating the garbled table for every logic gate in the circuit gives the
garbled circuit. I don't want to formally prove it's secure, but
here's the intuition.

* Given the input keys, Bob can unpack the correct output key, and
only the correct output key.
* Both $$k_{i,0}$$ and $$k_{i,1}$$ are generated randomly. Given just
one of them, Bob has no way to tell whether the key he has represents
$$0$$ or $$1$$. (Alice knows, but Alice isn't the one evaluating the circuit.)

Thus, from Bob's perspective, he's evaluating the circuit by passing gibberish
to each garbled gate and getting gibberish out. He's still doing the
computation - he just has no idea what bits he's actually looking at.

The one minor exception is key generation for the output wires of the
circuit. Instead of generating random keys, Alice encrypts $$0$$ or $$1$$.
This lets Bob learn the output of the circuit, and nothing else.


Input Key Transfer
-----------------------------------------------------------------------

Here's the new protocol, with garbled circuits

* Alice garbles circuit $$C$$ to get garbled circuit $$G(C)$$
* Alice sends $$G(C)$$ to Bob.
* Alice sends the keys for her input $$x$$ to Bob.
* Bob takes the input keys for $$x$$, adds the input keys for $$y$$, and
evaluates $$G(C)$$ to get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

Again, this is a good step, but there's still an issue. How does Bob
get the input keys for $$y$$? Only Alice knows the keys created for each wire.
Bob could give Alice his input $$y$$ to get the right keys, but then
Alice learns Bob's input.

One solution is to have Alice send both keys for each of $$y$$'s input
wires to Bob. For each wire, Bob can pick the key corresponding to his
input $$y$$. This lets Bob run the circuit without giving Alice his input
bits.

However, this has a subtle bug: by giving Bob both keys for his input
wires, **Bob can evaluate $$f(x,y)$$
with Alice's $$x$$ for an arbitrary $$y$$.**
This lets Bob get more information.
Going back to the millionaire's problem, let $$x = 10$$
and $$y = 8$$. At the end, Bob knows $$x > 8$$. If Bob later evaluates
$$f(x, 9)$$, he'll learn $$x > 9$$, which is more information than
he should know.

Thus, to be secure, Bob should only be able to run $$G(C)$$ on exactly
$$x,y$$. To do so, he needs to get only the keys for $$y$$, without
Alice learning which keys he wants. If only there was a way for Alice to
obliviously transfer that data...

So yes, that's why oblivious transfer is necessary. using oblivious transfer
to fill in the gap, we get the final protocol.

* Alice garbles circuit $$C$$ to get garbled circuit $$G(C)$$
* Alice sends $$G(C)$$ to Bob.
* Alice sends the keys for her input $$x$$ to Bob.
* Using oblivious transfer, for each of Bob's input wires,
Alice sends $$k_{i,y_i}$$ to Bob.
* With all input keys, Bob can evaluate the circuit to get $$f(x,y)$$
* Bob sends $$f(x,y)$$ back to Alice.

And now Alice and Bob can compute $$f(x,y)$$ without leaking their
information and without trusted third parties.


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
is a client, and Bob is a Google or Amazon data center. Alice can leverage
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
the Vickrey auction. Everyone submits a bid simultaneously, and whoever bid
the highest wins. But, they only pay the second-highest bid (the reasoning being
that it is more fair to the buyer if they pay as little above the second-highest
bid as possible.) Secure computation lets bidders place bids secretly without
a trusted third party.
