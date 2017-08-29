---
layout: post
title:  "The Friendship Paradox And You"
date:   2017-08-23 00:00:00 -0700
---

The friendship paradox states that on average, your friends have more friends
than you do. This is a strange statement, but it's true, and it has several
implications.

Let's model friendship as an undirected graph. People are vertices, and there
is an edge between two people if they're friends with each other.

IMAGE

At a high level, the friendship paradox holds because not only do popular
people have lots of friends, each of those friends is also friends with that
popular person who has more friends than they do. This makes the popular
person get counted more often when people are figuring out how many friends
their friends have. If this intuition works for you, feel free to skip the math,
but we'll now give a more formal intuition.

The average number of friends a person has is the average degree of a vertex.
Let $$V$$ be the set of all vertices, $$v$$ be a single vertex, and $$d_v$$
be the degree of vertex $$v$$. We get

$$
    \text{Average number of friends} = \frac{\sum_{v \in V} d_v}{|V|}
$$

What is the average number of friends that a person's friends will have?
To compute this, let's imagine that every person creates $$d_v$$ lists, one
list for each of their friends. For each friend $$v$$, they title the list as
$$v$$, then write down all of $$v$$'s friends. The average number of friends that a person's
friends will have is the average length of these lists.

How many lists are there? Since each person $$v$$ makes $$d_v$$ lists,
there are $$\sum_{v \in V} d_v$$ lists.

What is the total length of each list? If a list is titled $$v$$, it has $$d_v$$
names on it, because $$v$$ has $$d_v$$ friends. We get one list titled $$v$$
for every friend of $$v$$, so there are $$d_v$$ lists title $$v$$. Thus, each
$$v$$ contributes $$d_v^2$$ to the total length.

Overall, this gives

$$
    \text{Average number of friends of friends} = \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v}
$$

Now, we apply Cauchy-Schwarz. The Cauchy-Schwarz inequality says that given any
vectors $$a$$, $$b$$,

$$
    (\langle a, b \rangle)^2 \le \|a\|^2\|b\|^2
$$

Let $$a$$ be the vector of all ones, and $$b$$ be the vector of degrees. Then
we get

$$
    \left(\sum_{v \in V} d_v\right)^2 \le n \sum_{v \in V} d_v^2
$$

which rearranges to

$$
    \frac{\sum_{v \in V} d_v^2}{\sum_{v \in V} d_v} \ge \frac{\sum_{v \in V} d_v}{|V|}
$$

Thus, the average number of friends of friends is greater than or equal to the
average number of friends. Equality happens only if the graph is regular (if everyone
has exactly the same number of friends.)

**Importantly, this doesn't say anything about the friendships of a specific person,
or a specific person's friends.** It only says something about the overall average.

\* \* \*
{: .centered }

A natural extension is whether a similar result holds in directed graphs.

Let's suppose we have a producer-consumer model. There is an edge from a producer
to a consumer if the consumer processes something the producer makes. A given
person produces content and consumes content.

What is the average number of works a producer makes? Let $$d_v^{out}$$ be the number
of edges leaving $$v$$.

In the consumer view, on average how prolific are the content producers for the
content the consumer consumes? For each incoming edge, create a list for the source
of that edge. On that list, write down every person whose consumed their content.

Now, apply similar logic as the undirected case. There is one list for every
edge in the graph, giving $$\sum_v d_v^{out}$$. A producer $$u$$ is the title
of $$d_u^{out}$$ lists, one for each person whose consumed their content. Each
of those lists will have $$d_u^{out}$$ items on it.

This gives the same expression, apply Cauchy-Schwarz again, and so on.

The end result is that yes, the same result holds in directed graphs - on average,
the content producers you follow produce more than you do.

\* \* \*
{: .centered }

In the argument above, nothing was specific about friendship. The only requirements
was that we could model it as an undirected graph, where some object is a vertex,
vertices are related by edges, and those relations are symmetric.

There's a branch of mathematics called category theory. I don't actually
understand it, but the impression I get is that you let symbols represent something,
you let arrows representing something between symbols, and then you interpret
all of mathematics as special cases of those symbols and arrows.

As a shoutout to all the category theory fans reading this, let's make a bunch
of claims about society, based on different interpretaitons of vertices and edges.

Let vertices be Twitter accounts. An edge connects $$u$$ to $$v$$ if $$u$$
follows $$v$$. Then on average, the accounts you follow have more followers than
you do.

Let vertices be people. There is an edge from Alice to Bob if Bob has read
a book Alice wrote. Then on average, fewer people have read Bob's books than
the authors of the books Bob has read. Now, most people haven't written a book,
but again this principle applies to any form of communication - blogs, articles,
Facebook posts, Youtube videos, research papers, memes...

Let's abstract this even further. Say there's an edge from Alice to Bob if
Alice is a friend of Bob's and she said something Bob found interesting. Then
on average, your friends generate more interesting ideas than you do.

These realizations are all *fantastic* for dealing with imposter syndrome
issues. And in general, it's a useful principle to keep in mind: in whatever
social / intellectual circle you keep, popular things will be overrepresented (?)
