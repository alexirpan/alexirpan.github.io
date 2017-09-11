---
layout: post
title:  "The Friendship Paradox And You"
date:   2017-08-23 00:00:00 -0700
---

The [friendship paradox](https://en.wikipedia.org/wiki/Friendship_paradox) is a
cute rule of thumb. Unlike other rules of thumb, it actually has some mathematical
justification behind it.

The paradox states that on average, your friends have more friends than you do.
At first glance, this may seem strange, because it can't be true for everybody.
Someone has to be more popular than everybody else. And that's true - somebody
has to be on top. That's why the statement says *on average*. A small fraction
of people are more popular than their friends, and a large fraction are
less popular than their friends.

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

What is the average number of friends that a person's friends have?
To count this, let's imagine that every person $$v$$ creates $$d_v$$ lists, one
for each of their friends. Every list is titled with that friend's name - say it's
$$u$$, for sake of example. On that list, $$v$$ writes down all of $$u$$'s
friends.

IMAGE

The average number of friends that $$v$$'s friends have is the average length of
the lists that $$v$$ created. The average number of friends that any
person's friends have is the average length of all created lists.

Each person $$v$$ makes $$d_v$$ lists, so there are
$$\sum_{v \in V} d_v$$ lists total. A list titled $$v$$ has $$d_v$$ names on
it, because $$v$$ has $$d_v$$ friends. We get one list titled $$v$$ whenever a
friend of $$v$$ creates lists, so there are $$d_v$$ such lists.
Thus, every person $$v$$ contributes $$d_v^2$$ to the total length.

Overall, this gives

$$
    \text{Average number of friends of friends} = \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v}
$$

Now, apply the [Cauchy-Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality).
This inequality states that for any vectors $$a$$, $$b$$, their dot product
is at most the product of their norms. We'll use the version where we square
both sides.

$$
    (\langle a, b \rangle)^2 \le \|a\|^2\|b\|^2
$$

Let $$a$$ be the vector of all ones, and $$b$$ be the vector of degrees $$d_v$$.
Since there are $$n$$ vertices, we get

$$
    \left(\sum_{v \in V} d_v\right)^2 \le n \sum_{v \in V} d_v^2
$$

which rearranges to

$$
    \frac{\sum_{v \in V} d_v}{n} \le \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v}
$$

The left hand side is the average number of friends, and the right hand side is
the average number of friends of friends. That concludes the proof. $$\blacksquare$$

At a high level, the friendship paradox happens because the popularity of
popular people spreads through the network - they have lots of friends, each of
whom sees that some of their friends are very popular.

**Importantly, this only says something about the average.** Arguing anything
more requires making assumptions about how people interact and how friendships
work.

A natural extension is to ask whether a similar result holds in directed graphs.
A lot of relationships aren't symmetric, so if a similar result holds, it makes
the principle more applicable.

It turns out such a result does exist.
Let's model a directed edge as a producer-consumer relationship. There's an
edge from $$u$$ to $$v$$ if $$u$$ produces something that $$v$$ consumes.
People both produce things and consume things, represented by out-edges and in-edges respectively.
Let $$d_{v,out}$$ and $$d_{v,in}$$ be the number of out-edges and in-edges for $$v$$.

Let's consider the average number of things people produce.
The average number of things somebody produces is

$$
    \frac{\sum_{u \in V} d_{u,out}}{n}
$$

Compare this to the number of things produced by the content producers that
people follow. Again, for each incoming edge, create a list for the source of that edge,
writing down every person that's consumed their content.

Now, apply similar logic as the undirected case. There is exactly one list for
each edge, giving $$\sum_v d_{v,out}$$ lists. A producer $$v$$ is the title
of $$d_{v,out}$$ lists, one for each person whose consumed their content. Each
of those lists will have $$d_{v,out}$$ items on it. The average length of
those lists is

$$
    \frac{\sum_{v \in V} d_{v,out}^2}{\sum_{v \in V} d_{v,out}}
$$

Applying Cauchy-Schwarz again gives that on average, the content producers you
follow make more things than you do.

I call this the *producer* view, because you're always counting the edges that
are leaving each vertex. We can also take the *consumer* view. In this view,
we count the edges that are entering each vertex. By performing a similar argument,
you get that on average, people who consume your work consume more than you do.
Both views are valid, and sometimes one view gives an easier interpretation than
the other.

**Again, this argument only says something about the average, and you need
assumptions about graph connectivity to argue anything stronger.** In fact, despite
its mathematical underpinnings, I would hesitate on treating the friendship
paradox as a truth about the world. I see it more like a principle, that's
useful for flavoring different arguments, but not strong enough to form an
argument on its own.

\* \* \*
{: .centered }

In the derivation, nothing was specific about friendship. The only requirement
was that we can model something as a graph.

There's a branch of mathematics called category theory. I don't know it very
well, but the impression I get is that you let objects represent something, you
let arrows represent some relation between objects, and then you interpret
all of mathematics as special cases of those objects and arrows. This lets
you do things like [explain finance with commutative diagrams](https://hoj201.wordpress.com/2016/04/03/finance-explained-in-commutative-diagrams/).

I know at least one fan of category theory is going to read this, so as an homage,
let's make a bunch of wild claims about society by forming different
interpretations of vertices and edges.

Let vertices be Twitter accounts. An edge connects $$u$$ to $$v$$ if $$u$$
follows $$v$$. In the producer view, on average the accounts you follow have more followers than you.
In the consumer view, the people who follow you are more likely to follow more people than you.

Let vertices be people. Instead of friendship,
say there's an edge from $$u$$ to $$v$$ if $$u$$ has a crush on $$v$$. To the
disappointment of many people, crushes aren't symmetric. In the producer
view, on average the people you crush on have more admirers than
you do. In the consumer view, on average people who have crushes on you have
crushes on more people than you do. I don't know if this makes anyone feel
better about their romantic life, but there you go?

Again, let vertices be people. This time, there is an edge from $$u$$ to
$$v$$ if $$u$$ writes something that $$v$$ reads. In the producer view,
on average your readership is smaller than the readerships of other writers.
In the consumer view, on average the people who read your work read more things
than you do. Now, not everybody writes, but we could substitue writing
with any form of communication. Blogs, articles, Facebook posts, speeches,
Youtube videos, research papers, memes...in general, anyone who
prolifically creates content not only makes lots
of things, but becomes well-known *for* making lots of things.
Their reputation both precedes them and outgrows them.

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
