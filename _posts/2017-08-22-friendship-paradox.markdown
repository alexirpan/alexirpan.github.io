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

Now, that being said, looking at just the mean doesn't say anything about the
distribution of friends, or the distribution of friends of friends. In some
special cases, it could be the case that most people have more friends than their
friends, and there are a minority of really lonely people. (Construct this?)

\* \* \*
{: .centered }

A natural extension is whether a similar result holds in directed graphs.

Let's suppose we have a producer-consumer model. There is an edge from a producer
to a consumer if the consumer processes something the producer makes. A given
person produces content and consumes content.

What is the average number of works a producer makes? Let $$d_v^{out}$$ be the number
of edges leaving $$v$$.

What is the average number of works a producer's


