---
layout: post
title:  "A Modest Proposal for The Humor Formula"
date:   2015-10-10 01:24:00 -0800
---

*DISCLAIMER*

*Wrote this only to remind myself to keep practicing my writing. Persons
criticizing the polish will be prosecuted; persons pointing out the copious
bullshit will be banished; persons noticing this disclaimer's unoriginality
will be shot.*

*By Order of the Author, Per G.G., Chief of Ordnance*


Abstract
---------------------------------

Humor and jokes have experienced a great surge in popularity, which can attributed
to the creation of more efficient delivery systems like the Internet. However,
the field of humor analysis is still notably underdeveloped.
We posit a hypothesis on a formula describing the humor of a joke as a function
of the speaker, the joke's content, and the listener, in the hopes that this
will prompt society to think about why it considers something to be funny, instead
of taking it as a given. As evidence, we use material from professional comedians,
and math puns that have made the rounds in  mathematician subculture folklore.


Clearing Misconceptions
----------------------------------

One common criticism against the field of humor analysis is that explaining a joke
ruins the joke, which renders the analysis of humor as harmful. This misconception
is actively harmful and often forms the seeds of most criticism against the field,
so we would like to briefly explain away these worries.

First of all, humor analysis is the study of humor *in general.* This involves
making grand, sweeping statements about why we consider jokes to be funny, without
leaking or exposing any information about the jokes themselves, and this indirect
analysis is what lets us make progress while minimizing joke destruction.

Secondly, it is arguable whether explaining a joke is harmful at all. Suppose
a listener hears a joke, gets it immediately, then hears an explanation of the joke.
That listener's enjoyment is not ruined by hearing that explanation, because the listener
already has an implicit representation of that explanation in their head. Now,
suppose a listener hears a joke, and does not get it. Then that listener has so
far received zero entertainment from the joke, and hearing an explanation can only
increase that entertainment. And in some rare cases, explaining the joke can itself
be a joke. This is known as *meta humor*, and is outside the purview of this
proposal.

We admit that this argument is informal, and that there are other complicating
factors, most notably ones that arise in group settings. Frankly, we do not
give a shit, and will proceed with the analysis regardless.


Notation
-----------------------------------

Although our analysis is not especially rigorous, we nevertheless will include
some notation to make this appear more legitimate.

$$J$$ will represent the set of all jokes, and $$j$$ will represent a joke
from that set. $$P$$ will represent the set of all people, and $$p$$ represents
a person from that set. $$H: P \times J \times P \rightarrow R$$ denotes the humor function.
We assume humor depends on three arguments: the person saying the joke, the
joke's content, and the person hearing the joke. This will often be written
as $$H(p_s, j, p_h)$$, where the subscripts help identify between saying and
hearing. The value of this function is a real value, denoting how funny $$p_h$$
finds joke $$j$$ when it is delivered by $$p_s$$.

Lest people worry about drowning in notation, we endeavor to explain all
further equations with English as well, and only introduce it here to formalize
the assumptions we are making.


Proposed Humor Formula
------------------------------------

We propose that humor is the product of three factors: the inherent funniness
of the joke and speaker, the amount of education needed to understand the joke.
and the amount of sleep deprivation the listener has.

More formally, let $$I(j, p_s)$$ be the inherent humor joke $$j$$ has
when delivered by $$p_s$$, $$E(j)$$ be the amount of education needed,
and $$S(p_h)$$ be the amount of sleep deprivation the listener
has. Then

$$
    humor = H(p_s, j, p_h) = I(j,p)E(j)S(p_h)
$$

We spend the rest of the post explaining the reasoning behind these terms.


Inherent Humor Term
-----------------------------------

Clearly, different people will like a given joke more
or less, and given the wide variability, it doesn't seem reasonable to talk about
inherent humor. However, we claim professional comedians are a counterexample
to this line of reasoning. These people make a living doing stand-up or creating
comedy sketches that a wide range of people enjoy. They can do this because
their delivery is strong enough to give a good starting funniness.

A joke is also inherently funny when it is especially clever. For example,
song parodies by Weird Al are usually considered funny because he creates an
entire new set of lyrics that parodies the old ones. Thus, the inhereneet
humor must depends on both the deliverer and the joke itself.


Education Term
------------------------------------

(PhD comics image)

Consider the following examples from math.

> Q: "What's purple and commutes?"
> A: "An abelian grape!"

> Q: "What's sour, yellow, and equivalent to the Axiom of Choice?"
> A: "Zorn's lemon!"

The first joke requires knowing abstract algebra, since it is a play on "abelian group".
The second requires foundational mathematics, as it is a play on "Zorn's lemma".
Both of these jokes have terrible inherent humor, but because they use obscure concepts,
they still demand a chuckle from people "in the know". We call this
*privileged shared knowledge*. People with privileged knowledge know something that
the average person does not know. The key insight is that when someone delivers a joke,
it is implied that person knows the background required to understand the joke as well.
Thus, listeners "in the know have privileged shared knowledge with the speaker.
This triggers deep seated tribal mentality, where the tribe is everyone who knows
abstract algebra, or everyone who knows about the Zorn's Lemma. Once included in this
tribe, the listener gives the spekaer much more leeway, and will consider what the
speaker says to be considerably funnier than it actually is. (Note this also
explains why people who do not know the background do not enjoy the joke. Because
they do not have the privileged shared knowledge, they are excluded from the tribe for
that joke, and therefore rely only on the inherent humor. Usually, the
inherent humor of jokes like this is abysmal.


(As a side note, this observation seems naturally extendable to internet memes
and in-jokes. For memes, the privileged shared information is knowledge of the
meme itself. For in-jokes, the privileged shared information is the context in which
the in-joke was first created. We leave finding examples of this to the reader,
but suggest Reddit threads as a good starting point.)


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
