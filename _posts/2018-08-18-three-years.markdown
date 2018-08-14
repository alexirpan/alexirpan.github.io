---
layout: post
title:  "Three Years Later"
date:   2017-08-18 00:00:00 -0700
---

*Sorta Insightful* turns three years old today! Whether you were here from the
beginning or started recently, thanks for reading.

I normally write a sappy, self-reflective post for my blogging anniversary. This
year, I'm deciding to shake things up a bit, and to do a bunch of data analysis
instead. It's still self-reflective, just in a different vein.


Words Written
----------------------------------------

Last year, I wrote [22409 words]({% post_url 2017-08-18-two-years %}).

```
 1244 2016-09-07-contradictions.markdown  
 1936 2016-10-18-politics.markdown  
 1750 2016-11-08-right-questions.markdown  
  895 2016-11-12-hybrid-argument.markdown  
 1384 2017-01-20-mh-2017.markdown  
  931 2017-01-25-research-comm.markdown  
  592 2017-02-12-default-arguments.markdown  
 4035 2017-02-22-wasserstein-gan.markdown  
 1827 2017-03-18-we-have-a-problem.markdown  
  834 2017-04-19-acss.markdown  
 1925 2017-04-26-perils-batch-norm.markdown  
 3443 2017-06-27-hyperparam-spectral.markdown  
 1613 2017-08-12-openai-dota-2.markdown  
22409 total  
```

How about this year?

```
 1256 2017-08-18-two-years.markdown  
 1542 2017-09-13-friendship-paradox.markdown  
  155 2017-09-25-sim2real-grasping.markdown  
 1276 2017-11-18-research-tax.markdown  
  957 2017-12-30-mlp-italy.markdown  
 2112 2018-01-18-mh-2018.markdown  
 9426 2018-02-14-rl-hard.markdown  
 1319 2018-03-07-blog-paper.markdown  
 1280 2018-03-29-magic-arena.markdown  
 1790 2018-06-06-iclr-icra.markdown  
 1464 2018-06-27-dota-2-five.markdown  
 1872 2018-08-06-five-seconds-to-midnight.markdown  
24449 total  
```

A little bit more, 24449 words. I wrote 12 distinct posts this year, and 13
posts last year. Looks like I'm following my trend of 1 post a month on average,
although some months are busier than other months.

Eagle-eyed readers may notice that the reinforcement learning post was much
longer than the rest, forming almost 40% of the words I wrote for *Sorta Insightful*
this year. Did it take 40% of my writing time as well?


Time Spent
--------------------------------------------------------------------------

For about the past two years, I've been using Gleeo Time Tracker to track my
time. I use this to track these things:

* How long I sleep each night.
* How long my morning and evening commute are. Taking the difference between
commute times lets me figure out how many hours I've worked. (I don't track
work itself for a few complicated reasons that are better suited for another post.)
* How long I play specific video games.
* How long I spend reading books or web fiction.
* How long I spend writing.

EDIT THIS.

Despite having two years worth of data, I've never bother doing any analytics
on it. Let's dig into that now!

This blog is a Github Pages blog. Every change to this blog
is done by a Git commit. Every post is drafted on a separate branch. The upshot
of all this is that I have the timestamps for all the drafts of every post.
Cross-referencing these timestamps with my Gleeo Time Tracker data lets
me figure out how long I spent on writing each post.

At least, that's the theory. The exact way I'm doing this is a bit complicated.
The short version is that the mapping is a bit inexact.

My Git history is structured to be as close to a tree as possible. All posts
are created in a new branch. When I want to publish a post, I collapse all the
commits in that branch into a single commit, adding that to `master`. First,
I need to get a list of all commits I've made, along with their timestamp. I'm
doing this with `git log --all`. I then need to assign these commits to the
appropriate branch. Luckily, `git branch` has a `--contains` flag that lists
every branch a commit is on. A commit can be on multiple branches, but because
master is one unbroken line that never gets merged into anything else, we can
label commits as "on master" or "not on master".

This mapping isn't exact. I write most of my posts serially, but sometimes I
abandon a draft, finish a different post, then revisit the draft later. To account
for this, I assume that every block of writing time is devoted to only 1 post.
I assign the block to a post based on the earliest commit that lies within that block of
time.


