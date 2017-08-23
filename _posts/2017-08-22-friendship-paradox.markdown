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
list for each of their friends. On the list for friend $$v$$, they write
down all of $$v$$'s friends. The average number of friends that a person's
friends will have is the average length of these lists.

How many lists are there? Since each person $$v$$ makes $$d_v$$ lists,
there are $$\sum_{v \in V} d_v$$ lists.

What is the total length of each list? A person $$v$$ appears on a list
if 
