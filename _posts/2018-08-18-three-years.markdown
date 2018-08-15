---
layout: post
title:  "Three Years Later"
date:   2018-08-15 00:00:00 -0700
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
this year.


Time Spent Writing, and When I Do It
--------------------------------------------------------------------------

How long do I spend writing for my blog?

For the past two years, I've been using Gleeo Time Tracker to track my
time. I track a few things: how long I sleep, the length of my commute,
how much time I spend reading books and web fiction, what video games I play
(and for how long), and how long I spend writing.

Despite having two years worth of data, I've never bother doing any analytics
on it. This seems like a good excuse to dig into.

Gleeo Time Tracker exports its time as a CSV file, which makes it easy to write
some Python scripts to process it.

**Overall, I spent about 132 hours 30 minutes writing for my blog this year.**
At first, this felt like less than I expected, but this averages out to about
21-22 minutes a day on average, which feels correct. I don't write on most
days. My motivation comes in bursts, and I like starting and finishing posts
over the course of few days, usually the weekend.

Does that match the data? Here are the stats for how much time I spent
on a given day of the week.

| Day of the Week | Hours |
|-----------------|-------|
| Monday          | 21.78 |
| Tuesday         | 14.47 |
| Wednesday       | 33.53 |
| Thursday        | 24.98 |
| Friday          | 12.38 |
| Saturday        | 11.18 |
| Sunday          | 14.15 |

Okay, so I was *super* wrong. I actually spend the most time writing on
Wednesday. I guess blogging is my outlet for getting through the middle of the
week?

Alright, so I was wrong about the day of the week. How about the time of day?
I've often joked that my most productive writing hours are between 11 PM and
and 2 AM. Is that true?

| Time of Day | Hours |
|-------------|-------|
| 00:00-00:59 | 22.95 |
| 01:00-01:49 | 29.92 |
| 02:00-02:49 | 17.88 |
| 03:00-03:49 | 5.83  |
| 04:00-04:49 | 2.20  |
| 05:00-05:49 | 1.67  |
| 06:00-06:49 | 1.27  |
| 07:00-07:49 | 1.50  |
| 08:00-08:49 | 1.00  |
| 09:00-09:49 | 1.00  |
| 10:00-10:49 | 1.00  |
| 11:00-11:49 | 1.72  |
| 12:00-12:49 | 1.00  |
| 13:00-13:49 | 0.38  |
| 14:00-14:49 | 1.77  |
| 15:00-15:49 | 1.60  |
| 16:00-16:49 | 4.30  |
| 17:00-17:49 | 4.48  |
| 18:00-18:49 | 5.28  |
| 19:00-19:49 | 3.40  |
| 20:00-20:49 | 3.78  |
| 21:00-21:49 | 5.42  |
| 22:00-22:49 | 5.03  |
| 23:00-23:49 | 8.10  |

Yep, that's true! In fact I do a decent amount of writing *after* 2 AM as well.

I'm more impressed that I've written during literally every hour of the day.

Here's that table in bar graph form.

ADD GRAPH


Time Spent on Specific Posts
-------------------------------------------------------------------------------

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


