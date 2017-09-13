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

![Friendship Graph](/public/friendship-paradox/graph.svg)
{: .centered }

Now let's introduce some notation. $$V$$ is the set of all vertices, $$n$$ is
the number of vertices, $$v$$ is a single vertex, and $$d_v$$ is the degree of vertex $$v$$. The average
number of friends a person has is

$$
    \text{Average number of friends} = \frac{\sum_{v \in V} d_v}{n}
$$

Alright. But what's the average number of friends that someone's friends have?
To count this, let's imagine that every person $$v$$ creates $$d_v$$ lists, one
for each of their friends. Every list is titled with that friend's name. Say their
friend is named $$u$$, for sake of example. On that list, $$v$$ writes down all of $$u$$'s
friends.

![Friendship Graph With Lists](/public/friendship-paradox/graph_list.svg)
{: .centered }

The average number of friends that $$v$$'s friends have is the average length of
the lists that $$v$$ created, not counting the title. The average number of friends that
someone's friends have is the average length of all these lists.

Each $$v$$ creates $$d_v$$ lists, giving a total of $$\sum_{v \in V} d_v$$ lists.
There are $$d_v$$ lists titled $$v$$, because we get one such list whenever a
friend of $$v$$ creates lists. Each of those lists has $$d_v$$ names on it.
Thus, each person $$v$$ contributes $$d_v^2$$ to the total length.

Overall, this gives

$$
    \text{Average number of friends of friends} = \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v}
$$

Now, apply the [Cauchy-Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality).
This inequality states that for any two vectors $$a$$ and $$b$$, their dot product
is at most the product of their norms. We'll use the version where we square
both sides.

$$
    \langle a, b \rangle^2 \le \|a\|^2\|b\|^2
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
whom sees that some of their friends are popular.

**Importantly, this only says something about the average.** Arguing anything
more requires making assumptions about how people interact and how friendships
work.

A natural extension is to ask whether a similar result holds in directed graphs.
A lot of relationships aren't symmetric, so if a similar result holds, it makes
the principle more applicable.

It turns out such a result does exist.
Let's model a directed edge as a producer-consumer relationship. There's an
edge from $$u$$ to $$v$$ if $$u$$ produces something that $$v$$ consumes.

![Directed Graph](/public/friendship-paradox/directed_graph.svg)
{: .centered }

People both produce things and consume things, represented by out-edges and in-edges respectively.
Let $$d_{v,out}$$ and $$d_{v,in}$$ be the number of out-edges and in-edges for $$v$$.

Let's consider the average number of outgoing edges. This is the average number
of things that people produce.

$$
    \frac{\sum_{v \in V} d_{v,out}}{n}
$$

For a given $$v$$, let's compare this to the number of things produced by
content producers that $$v$$ follows.
For each **incoming** edge, create a list for the source of that edge,
writing down every consumer of that source. (This list will be the endpoint of
every outgoing edge from that source.)

![Directed Graph List](/public/friendship-paradox/directed_graph_list.svg)
{: .centered }

From here we can apply similar logic. Each person creates
one list for each outgoing edge, giving $$\sum_v d_{v,out}$$ lists total.
Each $$v$$ is the title of $$d_{v,out}$$ lists, one for each consumer.
Each of those lists will have $$d_{v,out}$$ items on it. All together, the average
across all $$v$$ is

$$
    \frac{\sum_{v \in V} d_{v,out}^2}{\sum_{v \in V} d_{v,out}}
$$

which we can once again apply Cauchy-Schwarz too. The conclusion?

**On average, the content producers you follow make more things than you do.**
{: .centered }

I call this the *producer* view, because you're always counting the edges that
leave each vertex. We can also take the *consumer* view, counting the edges that
are entering each vertex instead. By performing a similar argument, you get this
conclusion instead.

**On average, the people who follow your work follow more things than you do.**
{: .centered }

Both views are valid, and give different interpretations of the same graph.

**Again, this argument only says something about the average, and you need
assumptions about graph connectivity to argue anything stronger.** In fact, despite
its mathematical underpinnings, I would hesitate on treating the friendship
paradox as a truth about the world. I see it more like a principle, that's
useful for flavoring different arguments, but not strong enough to hold an
argument on its own.

\* \* \*
{: .centered }

In the derivation above, the only requirement was that we could model interactions
as a graph.

There's a branch of mathematics called [category theory](https://en.wikipedia.org/wiki/Category_theory).
I don't know it very well, but the impression I get is that you let objects represent something, you
let arrows represent some relation between objects, you draw arrows between
different objects, and then you interpret all of mathematics as special cases of
those objects and arrows. This lets you do things
like [explain finance by drawing a bunch of arrows](https://hoj201.wordpress.com/2016/04/03/finance-explained-in-commutative-diagrams/).

For some reason I know $$\epsilon > 0$$ fans of category theory are going to read
this post, so as an homage to them, let's make a bunch of wild claims about
society by generating different interpretations of vertices and edges.

Let vertices be Twitter accounts. An edge connects $$u$$ to $$v$$ if $$u$$
follows $$v$$. In the producer view, on average the accounts you follow have
more followers than you. In the consumer view, the people who follow you are
more likely to follow more people than you do.

Let vertices be people. Instead of friendship,
say there's an edge from $$u$$ to $$v$$ if $$u$$ has a crush on $$v$$. To the
disappointment of many people, crushes aren't symmetric. In the producer
view, on average the people you crush on have more admirers than
you do. In the consumer view, on average people who have crushes on you have
crushes on more people than you do. I don't know if this makes anyone feel
better about their love life, but there you go?

Again, let vertices be people. This time, there is an edge from $$u$$ to
$$v$$ if $$u$$ writes something that $$v$$ reads. In the producer view,
on average your readership is smaller than the readerships of writers you follow.
In the consumer view, on average your readership reads more things than you do.
Now, not everybody writes, but we could substitue writing
with any form of communication. Blogs, articles, Facebook posts, speeches,
Youtube videos, research papers, memes...

In general, any prolific person not only makes lots of things, they become
well-known *for* making lots of things. Their reputation both precedes them and
outgrows them.

\* \* \*
{: .centered }

I like the friendship paradox a lot. Why?

Well, for one, it's great for addressing imposter syndrome issues. For example,
sometimes I feel like I should be writing more. When I poke at the feeling, it
often turns into this.

1. I should write more.
2. Why do I think that? It's partly because I read cool things from people that write more than I do.
3. But by friendship paradox, it's expected that those writers are writing more than me.
4. So hey, maybe I shouldn't feel too bad.

More importantly, the friendship paradox touches on another, more important
idea: the things you see don't have to reflect reality. If you base your assumptions
of popularity on the popularity of your friends, on average you'll come up
short. If you base your assumptions of productivity by things you read online, it's
easier to see evidence of productivity from people who are very productive.
If you base your views of somebody by things you hear them say, it's warped by
the chances you would have heard their views in the first place. And so on down.
Not all of these are applications of the friendship paradox, but it's easy to
forget about these things, and thinking about the paradox is a nice reminder.
