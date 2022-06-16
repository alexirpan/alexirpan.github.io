---
layout: post
title:  "Are Blockchains Good for the World?"
date:   2022-05-28 11:56:00
---

[Betteridge's law of headlines](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) says that
any headline that ends in a question mark can be answered with "no". That's not going to apply here.

Cryptocurrency is weird. I don't necessarily hate it - back in 2013 I spent several hours figuring out
how to turn my student AWS credits into crypto. But the ecosystem's changed from a curiosity to something
where billboards and ads are blasted to every space biased towards young adult males. It's a mess, and
to me, cryptocurrency (and blockchains by extensions) are the poster child of a technology that's grown
too big to argue that other people will decide the ethics.


Blockchains vs Cryptocurrency
-------------------------------------------------------------------------------------------------

First, it's important to draw a distinction between blockchains and cryptocurrency. I think 3Blue1Brown's
[explanation of Bitcoin](https://www.youtube.com/watch?v=bBC-nXj3Ng4) is quite good, and I'm just going
to repeat the highlights.

Blockchains are a technology that let you store information with distributed consensus. Information is
packaged into blocks, that are connected in a sequence (a chain). The commonality is that the blocks
are stored in a distributed manner. In principle, anyone can propose new blocks of information to
attach to the chain, as long as they pass the consensus mechanism.

The consensus mechanism, protocol, whatever, are the rules that define whether a block is valid or
not. The common ones are proof-of-work (Bitcoin, Ethereum), and proof-of-stake (Ethereum 2, Cardano).
In proof-of-work, you burn many CPU / GPU / custom ASICs to find a sequence of extra bits that makes
the block hash start with enough 0s. This is considered secure because assuming the hash function isn't
broken, no attacker can reliably create fake blocks unless they control 51% of the total hash power
in the world. In proof-of-stake, you become a validator by putting enough money up for
collateral. Validators can then have their money deleted if they act in bad faith. Intuitively,
if you have put up money to validate blocks, then you should be invested in keeping the chain
alive, and based on this intuition, the more money you put up for collateral the more blocks you
are asked to validate.

In both of these approaches, there doesn't have to be a central authority that decides what is
and isn't valid to add to the blockchain. It's all distributed. This is one of the main draws
and selling points of blockchain approaches.

For pretty much the entire rest of the post, I'm just going to talk about cryptocurrency, but
I think it's important to make this distinction: **blockchains and cryptocurrency are separate
in theory, but the same things in practice.**

There is no rule that says a blockchain has to involve distributing a digital token. There are
plenty of distributed, peer-to-peer services! BitTorrent is distributed file-serving that
relies on volunteers seeding files for
other people. Tor is a private browser that also runs on volunteers running relays to
disguist traffic. You could imagine a blockchain that exists without attaching a token to
the whole endeavor.

However, the most popular blockchain is the one back by Bitcoin, and the Bitcoin protocol
is designed such that blocks represent transactions of Bitcoin, and the computer that
validates a block is allowed to give themselves some Bitcoin as a reward. The blockchain
that backs Bitcoin is inseparable from the cryptocurrency itself. Basically every blockchain
afterwards has been set up similarly. The ethos of the crypto world is that every service
must be attached to some digital token of monetary value to incentivize good behavior,
as opposed to nebulous concepts like "do the right thing". And, you know, it's probably true
that giving away money is more likely to get people to do what you want, but it sometimes feels like
crypto spheres can only view things through that lens.

I have yet to see any substantial blockchain that is independent of a cryptocurrency distributed
by that blockchain. Sure, I see lots of people talking about blockchains that *could* be used in these
ways. But it is almost always just talk, by people who are substantially invested in crypto. There's just very
few use cases that need every property that blockchains offer. Creating a decentralized source of
trust that anyone can contribute to comes at real cost. Most problems are perfectly happy with making
some concessions and implementing something else.

Blockchains are kind of like reinforcement learning: a solution in search of a problem. Except,
I expected reinforcement learning to get better as hardware improves and more research is done on better
learning algorithms. Blockchains don't feel like they have the same level of innovation left to them. They're
trying to solve a problem of trust, and it's hard to innovate protocols for better trust that don't
hit some fundamental floor of the problem.


Proof-of-Work and the Carbon Argument
--------------------------------------------------------------------------------------------------------

The most popular argument by far against cryptocurrency is that they burn the planet by contributing to
CO2 emissions and global warming.

This...is kind of false? And also kind of true? Look let's just get into it.


