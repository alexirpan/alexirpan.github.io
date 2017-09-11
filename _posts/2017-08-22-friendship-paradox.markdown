---
layout: post
title:  "The Friendship Paradox And You"
date:   2017-08-23 00:00:00 -0700
---

The friendship paradox is a nice rule of thumb that actually has mathematical
justification. I think it's not as well known as it should be, so here's an
explanation.

The paradox states that on average, your friends have more friends than you do.
At first glance, this may seem strange, because it can't be true for everybody
at once. And that's true - it can't! That's why it says that *on average* your
friends are more popular than you. There will be people who are more popular
than all their friends.

To justify why this could be true, let's model friendship as an undirected graph.
In this graph, people are vertices, and an edge connects two people if they're
friends with one another.

IMAGE

Now let's introduce some notation. $$V$$ is the set of all vertices, $$n$$ is
the number of vertices, $$v$$ is a single vertex, and $$d_v$$ is the degree of vertex $$v$$. The average
number of friends a person has is

$$
    \text{Average number of friends} = \frac{\sum_{v \in V} d_v}{n}
$$

What is the average number of friends that a person's friends will have?
To count this, let's imagine that every person $$v$$ creates $$d_v$$ lists, one list
for each of their friends. Every list is titled with that friend's name $$u$$,
and the list for $$u$$ has the list of all of $$u$$'s friends.

IMAGE

The average number of friends that $$v$$'s friends have is the average length of
the $$d_v$$ lists that $$v$$ created. The average number of friends that an
average person's friends have is the average length of all such lists written by
anybody.

How many lists are there? Person $$v$$ makes $$d_v$$ lists, so there are
$$\sum_{v \in V} d_v$$ lists.

What is the total length of the lists? A list titled $$v$$ has $$d_v$$ names on
it because $$v$$ has $$d_v$$ friends.
We get one list titled $$v$$ for each friend of $$v$$, giving $$d_v$$ such lists.
Thus, every person $$v$$ contributes $$d_v^2$$ to the total length.

Overall, this gives

$$
    \text{Average number of friends of friends} = \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v}
$$

Now, apply the Cauchy-Schwarz inequality. This inequality states that for any
vectors $$a$$, $$b$$,

$$
    (\langle a, b \rangle)^2 \le \|a\|^2\|b\|^2
$$

Let $$a$$ be the vector of all ones, and $$b$$ be the vector of degrees. This
gives

$$
    \left(\sum_{v \in V} d_v\right)^2 \le n \sum_{v \in V} d_v^2
$$

which rearranges to

$$
    \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v} \ge \frac{\sum_{v \in V} d_v}{n}
$$

Thus, the average number of friends of friends is greater than or equal to the
average number of friends. $$\blacksquare$$

At a high level, the friendship paradox happens because the popularity of
popular people spreads through the network - they have lots of friends, each of
whom sees that some of their friends are very popular.

**Importantly, this only says something about the overall average.** To argue
anything more concrete, you need to make assumptions about how people interact
and how friendships work.

A natural extension is to ask whether a similar result holds in directed graphs.
A lot of interactions aren't symmetric, and if a similar result holds, it makes
the principle more general.

It turns out such a result does exist.
Let's model a directed edge as a producer-consumer relationship. An edge goes
from A to B if B consumes something that A produces. A given person acts as both
a producer and a consumer (represented by out-edges and in-edges respectively.)

Again, some notation: $$d_v^{out}$$ and $$d_v^{in}$$ are the number of out-edges
and in-edges for $$v$$. Let's consider two quantities, the average number of things
people make, and the average number of things people consume from producers they
follow. The average number of things somebody makes is

$$
    \sum_{v \in V} d_v^{out} / n
$$

On average, how prolific are the content producers for the content the consumer consumes?
Again, for each incoming edge, create a list for the source of that edge,
writing down every person that's consumed their content.

Now, apply similar logic as the undirected case. There is exactly one list for
each edge, giving $$\sum_v d_v^{out}$$ lists. A producer $$u$$ is the title
of $$d_u^{out}$$ lists, one for each person whose consumed their content. Each
of those lists will have $$d_u^{out}$$ items on it.

Applying Cauchy-Schwarz again gives that on average, the content producers you
follow make more things than you do.

You can perform a similar argument with edges in the opposite direction. This
gives that on average, people who consume your content consume more things than
you do.

**Again, this argument only says something about the average, and you need
assumptions about graph connectivity to argue anything stronger.** In fact, despite
its mathematical underpinnings, I would hesitate on treating the friendship
paradox as a truth about the world. I see it more like a principle, that's
useful for flavoring different arguments, but not quite strong enough to form
an argument on its own.

\* \* \*
{: .centered }

In the derivation, nothing was specific about friendship. The only requirement
was that we can model something as a graph.

There's a branch of mathematics called category theory. I don't know it very
well, but the impression I get is that you let objects represent something, you
let arrows represent some relation between symbols, and then you interpret
all of mathematics as special cases of those objects and arrows. Like, say,
finance.

As a shoutout to the category theory fans reading this, let's make a bunch of
wild claims about society, based on different interpretations of vertices and
edges!

Let vertices be Twitter accounts. An edge connects $$u$$ to $$v$$ if $$u$$
follows $$v$$. These are directed edges. On average, the accounts you follow
have more followers than you do.

Let's have vertices be people again, except instead of friendship, let's say
there's an edge from $$u$$ to $$v$$ if $$u$$ has a crush on $$v$$. These
are also directed edge. On average, the people you crush on receive more
attention than you do. Awww, that's kinda sad. But let's consider the other
direction. On average, people who have crushes on you crush on more people
than you do. Uhhhh, okay, that didn't really help.

Again, let vertices be people. This time, there is an edge from $$u$$ to
$$v$$ if $$v$$ read something that $$u$$ wrote.
On average, the writers whose works you read get more readers than you do.
We could substitute writing with any form of communication.
Blogs, articles, Facebook posts, Youtube videos, tweets, research papers,
memes...in general, anyone who prolifically creates content not only makes lots
of things, but becomes well-known *for* making lots of things.
Their reputation precede them and outgrows them too.

\* \* \*
{: .centered }

Why do I think this is important?

These kinds of arguments are *fantastic* for addressing imposter syndrome
issues. Several times I've felt like I should be writing more. But when I poke
at it, it often turns into this.

1. I should write more.
2. Why do I think that? It's partly because I read cool things from people that write more than me.
3. But by friendship paradox, it's expected that the writers of thigns I like reading write more than I do.
4. So hey, maybe it's not so bad after all!

This also get at another important idea: the things you see don't have to reflect
what reality is actually like. The friendship paradox is one example of this. If
you base your assumptions of popularity on how popular your friends are, on
average you'll see more popularity than you should. The more common example is
how memetic ideas are, in that things you hear people talking about don't have
to match what people are actually talking about.
