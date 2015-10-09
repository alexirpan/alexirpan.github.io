---
layout: post
title:  "A Modest Proposal for The Humor Formula"
date:   2015-10-10 01:24:00 -0800
---

*Disclaimer: Not very polished, bullshitted on the fly, mostly for fun.*

Abstract: We claim discovery of a formula that computes the humor level of
a joke $$J$$. Although we do not have a formal proof, we suggest a few examples
that fall in line with the formula, and hope this inspires further research into this area.

Update KaTEX

Notation:

Let $$J$$ be a joke from the set of all jokes, and let $$P$$ be a person
from the set of all people. The humor function $$H: J \times P \rightarrow R$$
is defined as the function such that $$H(j, p)$$ is how much person $$p$$ enjoys joke
$$j$$.

We feel that although it's important to lay down the ground notation, it gets in
the way of the key ideas, and therefore will transition into English in a bid for
better understanding. However, for the rest of the proposal, please remember
that when we say "this person finds this joke funny", we actually mean
"For this choice of $$p$$ and $$j$$, $$H(p, j)$$ is especially large."

Why Analyze Jokes? Doesn't Explaining a Joke Sap Away All Its Humor?
------------------------------------

Yes, it does.

Frankly, I have no sense of humor, and thus don't give a shit.

Proposed Formula
------------------------------------

humor = ((amount of background/context required to understand the joke) * (inherent
funniness of the joke)) * (amount fo sleep deprivation)
{: .centered }

The notation $$1_{X}$$ is borrowed from indicator random variables, and means
"$$1$$ if $$X$$ is true and $$0$$ otherwise."  So for example,
$$1_{2=2}$$ equals $$1$$.

I'll spend the rest of this post explaining why this formula makes sense.

Inherent Humor Term
-----------------------------------

Every joke has some baseline level of humor.

This may be controversial. Clearly, different people will like a given joke more
or less, and given the wide variability, it doesn't seem reasonable to talk about
inherent humor. However, I claim professional comedians are a counterexample.
There are people who make a living doing stand-up or creating comedy sketches,
and the reason they can do so is because most of their jokes have high
inherent baselines.

Note that a joke's baseline humor depends on many factors, including the content,
the complexity/cleverness, the delivery, and so on.
For this analysis, we'll assume these factors are all rolled into the humor term.


The Background Term
------------------------------------

It's a well observed effect across several disciplines that highly topical,
obscure jokes can be carried by their exclusivity.

(PhD comics image)

For instance, consider the following examples from math.

> Q: "What's purple and commutes?"
> A: "An abelian grape!"

> Q: "What's sour, yellow, and equivalent to the axiom of choice?"
> A: "Zorn's lemon!"

The first joke requires abstract algebra since it's a play on "abelian group".
The second requires foundational mathematics since it's a play on "Zorn's lemma".
**Both of these jokes have terrible baselines, but because they use obscure concepts,
they still demand a chuckle from people "in the know"** This becomes especially
apparent in the following joke

> "A server set up with RAID 5 walks into a bar..."

I don't even have to finish this sentence, because readers who know what RAID 5
is will immediately give this joke a free pass. RAID 5! I understood that
reference! And thus, you realize your sense of humor is forever ruined.

These examples have been focused towards educational knowledge, which may be breeding
some misconceptions. When I say background, I mean any level of privileged knowledge
that not everyone has. Consider internet memes. If someone suddenly shouts
"ALWAYS, I WANNA BE WITH YOU, AND MAKE BELIEVE WITH YOU", someone not in the know
is going to be very confused. However, someone who's spent enough time on the
Internet to know the reference is going to continue with "AND LIVE IN HARMONY
HARMONY OH LOOOOVE". (This is most obvious in Reddit threads; in real life,
people have enough restraint to leave the joke alone.)

Note that we can't roll this into the baseline humor term because it depends on the
joke's receiver, and we assume the baseline humor depends only on the
speaker and the joke itself.


Combining These Two Terms
---------------------------------

Now, it's clear a joke's funniness relies on both of these terms. The question
is how to combine the terms. Here, I claim Occam's Razor and only consider
the two basic binary operations, addition and multiplication. Is there a
compelling argument for one over the other?

After thinking about it, I settled on multiplication. The reason for this
ties back to the examples of professional comedians and math puns.
Multiplicative behavior implies that an especially well delivered joke
can be funny even without being in the know, and a joke that requires
especially obscure knowledge can be carried by its exclusivity.
The former is true of most professional comedians; I'll cite
the "cup of dirt" story and move on. For the other direction,
consider the following joke.

> It's an old joke that a mathematician is a device for turning coffee into
> theorems. However, it's also true that a comathematician is a device for
> turning cotheorems into ffee. In fact, by similar reasoning, every
> nut is a coconut.

The first joke has some inherent funniness to it, with some light
carrying because it mentions "mathematicians" and "theorems". However,
the second joke has no inherent humor at all. It's only funny if you
know a little bit of category theory (link), and then, by magic, it suddenly
becomes funny. Note that this is a double whammy; not only do you need to
know category theory, you need to know that there is an old joke that
mathematicians are coffee -> theorem converters. By this point, anyone
who has all the requisite background information *must* find it funny,
or at least worthy of a chuckle.


The Final Factor
------------------------------

Together, these explain most of the observed data, but there is one
notable scenario that is not covered. Nothing triggers delirium quite
like sleep deprivation, and in states of extreme tiredness people can
find the most arbitrary things funny. The stress placed on the brain by
lack of sleep acts as a general amplifying factor, making all jokes funnier
by default. Deciding whether
something is funny or not is an actual cognitive decision; when the brain
is too tired to make that decision, it will default to the general
assumption that jokes are supposed to be funny.

Unfortunately, there aren't any good examples of this, because demonstrating
the effect requires the reader (you) to be sleep deprived already.


Conclusion
-----------------------------

This formula goes a long way towards explaining the factors that go into
humor. It falls remarkably in line with anecdotal evidence, and therefore
must be true. We hope it inspires future work in the growing field of
humor analysis.


References
----------------------------
TODO
