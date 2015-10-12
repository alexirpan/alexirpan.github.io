---
layout: post
title:  "A Proposition For The Formula to Humor"
date:   2015-10-10 01:24:00 -0800
---

*DISCLAIMER*

*Wrote this only to remind myself to keep practicing my writing. Persons
criticizing the stodgy language or lack of polish will be prosecuted; persons pointing out the copious
bullshit will be banished; persons noticing this disclaimer's unoriginality
will be shot.*

*By Order of the Author, Per G.G., Chief of Ordnance*

*Also, I am at most 50% serious about all of this.*


Abstract
---------------------------------

Humor and jokes have experienced a great surge in popularity, which can attributed
to the creation of more efficient delivery systems, like the Internet. However,
the field of humor analysis is still notably underdeveloped.
We posit a hypothesis on a formula describing the humor of a joke as a product of
factors that depend on the speaker, the joke's content, and the listener, in the hopes
that this will inspire society to think about why it considers something to be funny, instead
of taking it as a given. As evidence, we use material from professional comedians,
and math puns that have made the rounds in  mathematician subculture folklore.


Clearing Misconceptions
----------------------------------

One common criticism against the field of humor analysis is that explaining a joke
ruins the joke. Thus, much like the goto statement, detractors say that analyzing
humor should be considered harmful. This misconception is misguided and often forms
the bases of most criticism against the field,
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
post. For further discussion, see [\[1\]](#cite1)

We admit that this argument for humor analysis is informal, and that there are other complicating
factors, To be frank, we will not give a shit,
and will proceed with the analysis regardless.


Notation
-----------------------------------

It is a well known fact that including unneeded mathematical notation makes
text more persuasive and legitimate. Thus, we formalize some notation that will
be used in later sections.

$$J$$ will represent the set of all jokes, and $$j$$ will represent a joke
from that set. $$P$$ will represent the set of all people, and $$p$$ represents
a person from that set. $$H: P \times J \times P \rightarrow R$$ denotes the humor function.
We assume humor depends on the person saying the joke, the
joke's content, and the person hearing the joke. This will often be written
as $$H(p_s, j, p_l)$$, where the subscripts indicate "speaking" and "listening"
respectively. The output is a real value, denoting how funny $$p_l$$
finds joke $$j$$ when it is delivered by $$p_s$$.

Lest people worry about drowning in notation, we have endeavored to explain all
further equations with English as well.


Proposed Humor Formula
------------------------------------

We propose that humor is the product of three factors: the inherent funniness
of the joke when delivered by the speaker, the amount of education needed to understand the joke.
and the amount of sleep deprivation the listener has.

More formally, let $$I(j, p_s)$$ be the inherent humor joke $$j$$ has
when delivered by $$p_s$$, $$E(j)$$ be the amount of education needed,
and $$S(p_l)$$ be the amount of sleep deprivation the listener
has. Then

$$
    H(p_s, j, p_l) = I(j,p_s)E(j)S(p_l)
$$

We spend the rest of the post explaining the reasoning behind these terms.


The Inherent Humor Term, $$I(j,p_s)$$
-----------------------------------

Clearly, different people will find different jokes funny.
Given the wide variability, it doesn't seem reasonable to talk about
inherent humor. However, professional comedians are a counterexample
to this line of reasoning. These people make a living doing stand-up or creating
comedy sketches that a wide range of people enjoy. They can do this because
most of their jokes are inherently funny. Behind the scenes, show hosts
like Jon Stewart and Stephen Colbert spend hours crafting jokes that are likely
to work on a wide audience (that have high inherent funniness), then spend more
hours rehearsing their material (improved delivery makes a joke funnier. Note
this is why this term depends on the speaker as well as the joke.)


The Education Term, $$E(j)$$
------------------------------------

![PhD comics](/public/humor-analysis/phdhumor.gif)
{: .centered }

Fig 1. Prior work on the link between education and humor. [\[2\]](#cite2)
{: .centered }

Consider the following example jokes from math.

> Q: "What's purple and commutes?"
>
> A: "An abelian grape!"

> Q: "What's sour, yellow, and equivalent to the Axiom of Choice?"
>
> A: "Zorn's lemon!"

The first joke requires knowing abstract algebra, since it is a play on "abelian group".
The second requires knowing some foundational mathematics, as it is a play on "Zorn's lemma".
Both of these jokes have **terrible** inherent humor. (Should you disagree, we
advise getting a second opinion immediately.) But, because they use obscure concepts
from math at the university level,
they still demand a chuckle from people "in the know". We call this the phenomenon
**privileged shared knowledge**. People with privileged knowledge know something that
the average person does not know. A group with privileged shared knowledge knows
they all know something the average person does not know.
When someone delivers a joke,
it is implied that person knows the background required to understand the joke as well.
Thus, listeners "in the know" have privileged shared knowledge with the speaker.
This triggers a deep seated tribal mentality, where the tribe is everyone who knows
abstract algebra, or everyone who knows about the Zorn's Lemma. Once included in this
tribe, the listener gives the speaker and joke much more leeway, and will consider what the
speaker says to be considerably funnier than it actually is.

As further evidence, consider this especially extreme case.

> It's an old joke that a mathematician is a device for turning coffee into
> theorems. However, it's also true that a comathematician is a device for
> turning cotheorems into ffee.

The first joke is slightly funny on its own, and is further elevated because
it mentions "mathematicians" and "theorems" in passing. However,
the second joke has no inherent humor at all. It is only funny if you
know a little bit of category theory (link). Then, as if by magic, it suddenly
becomes humorous. Not only do you need to
know category theory, you need to know that there is an old joke that
mathematicians are coffee -> theorem converters. By this point, anyone
who has all the requisite background information *must* find it funny.

This also
explains why people feel "left out" when they "don't get" a joke.
Because they do not have the privileged shared knowledge, they are excluded (or "left out"))
from the tribe.
They are forced to rely on the inherent humor, and unfortunately jokes like these
math puns have terrible scores in that department.

As a side note, this observation seems naturally extendable to Internet memes
and in-jokes. For memes, the privileged shared knowledge is knowledge of the
meme itself. For in-jokes, the privileged shared knowledge is the context in which
the in-joke was first created. We leave finding examples of this to the reader,
but suggest Reddit threads as a good starting point.


The Sleep Deprivation Term, $$S(p_l)$$
---------------------------------

The final term we propose is the tiredness of the listener. When especially
tired, people are more likely to find things funny than they normally would be.
One possible explanation for this is that it is a subcategory of the privileged
shared knowledge, where living through the context of no sleep is the common
information. However, this does not accurately why a joke that is funny at 3 AM is no longer funny the next morning, as everyone
involved should still have the shared context. Somehow, the joke becomes less funny,
even when said from the same speaker to the same listener.

Therefore, humor must depend on some temporal structure.
We propose that sleep deprivation makes jokes funnier because the
brain is less able to judge a joke due to stress and fatigue. When we are told we
are about to hear a joke, our brains start expecting humor, and primes our
mental state with a baseline level of funniness.
As the brain hears and considers the joke,
further adjustments are made to this value, and eventually we decide on the humor level
and laugh/facepalm appropriately.
When tired, the listener's brain gets less computation time, giving less time to
adjust the baseline value. In this scenario, the final humor output relies more
on the primed state, explaining why jokes can be funnier deep into the night;
the joke itself was awful, and we simply did not have the time to realize it.

Note this also suggests that especially good jokes are not as funny when tired,
since our brains have less time to adjust the internal humor value upwards.
This lines up with our anecdotal experience, and therefore must be true.


Conclusion
-----------------------------

The great surge in viral videos and memeing, as fueled by the Internet, has made
humor analysis an exceptionally useful field. Should the trend continue, we
believe considering questions like this one will continue to be useful in the
future. We hope this incredibly dumb post inspires future work, which will ideally
be much more insightful.


References
----------------------------

1. <a name="cite1" href="http://tvtropes.org/pmwiki/pmwiki.php/Main/DontExplainTheJoke">Don't Explain the Joke - TVTropes</a>
2. <a name="cite2" href="http://www.phdcomics.com/comics/archive.php?comicid=868">PhD Comics - Your Shrinking Sense of Humor</a>
