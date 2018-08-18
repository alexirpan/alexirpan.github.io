---
layout: post
title:  "Three Years Later"
date:   2018-08-15 00:00:00 -0700
---

*Sorta Insightful* turns three years old today! Whether you were here from the
beginning, or just discovered this blog, thanks for reading.

I normally write a sappy, self-reflective post for my blogging anniversary. This
year, I'm deciding to do a bunch of data analysis instead. It's still
self-reflective, just in a different vein.


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

A little bit more, 24449 words. I wrote 12 posts this year, following my
trend of 1 post a month on average. (Although some months are certainly
busier than other ones.)

Eagle-eyed readers may notice that the reinforcement learning post was much, much
longer than the rest, taking up almost 40% of the words I wrote for
*Sorta Insightful* this year.


View Counts
--------------------------------------------------------------------------

These view counts are aggregated from August 18, 2017 to today.

```
    302 2017-08-18-two-years.markdown  
    530 2017-09-13-friendship-paradox.markdown  
    552 2017-09-25-sim2real-grasping.markdown  
    279 2017-11-18-research-tax.markdown  
    209 2017-12-30-mlp-italy.markdown  
    907 2018-01-18-mh-2018.markdown  
145,502 2018-02-14-rl-hard.markdown  
  1,376 2018-03-07-blog-paper.markdown  
    744 2018-03-29-magic-arena.markdown  
  3,311 2018-06-06-iclr-icra.markdown  
    579 2018-06-27-dota-2-five.markdown  
    154 2018-08-06-five-seconds-to-midnight.markdown  
```

Okay, I knew the reinforcement learning post would be the outlier. I didn't
think it would be the outlier by that much.


Time Spent Writing
--------------------------------------------------------------------------

For the past two years, I've been using Gleeo Time Tracker to track my
time. I track a few things: how long I sleep, the length of my commute,
how much time I spend reading books and web fiction, what video games I play
(and for how long), and how long I spend writing.

Despite having two years worth of data, I've never bother doing any analytics
on it. This post is a good excuse to start.

Excluding the time spent on this post, **I spent 131 hours 21 minutes writing
for my blog this year.**
At first, this felt like less than I expected, but this averages out to about
21-22 minutes a day, which feels correct.


When I Write
---------------------------------------------------------------------------

Most days, I don't do any writing. My motivation comes in bursts, and I like
starting and finishing posts witihn a few days. I feel like I get the most
writing done on the weekend. Is that true?

Gleeo Time Tracker doesn't have the tools for this built-in, but you can
export your timetracking data as a CSV file. This makes it straightforward to
do further analytics. I used Python for this, since that's my go-to programming
language.

Here's how much time I've spent writing on a given day of the week.

| &nbsp;&nbsp;Day of the Week&nbsp;&nbsp;  | Hours |
|-----------------|-------|
| Monday          | 20.93 |
| Tuesday         | 14.18 |
| Wednesday       | 33.53 |
| Thursday        | 24.98 |
| Friday          | 12.38 |
| Saturday        | 11.18 |
| Sunday          | 14.15 |
{: .centered-table }

Turns out I was *super wrong*! I actually do most of my writing on Wednesday.
I guess blogging is my outlet for getting through the middle of the week?

Alright, so I was wrong about the day of the week. How about the time of day?
I've often joked that my most productive writing hours are between 11 PM and
and 2 AM. Is that true?

| &nbsp;&nbsp;Time of Day&nbsp;&nbsp; | Hours |
|-------------|-------|
| 00:00-00:59 | 22.67 |
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
| 21:00-21:49 | 5.38  |
| 22:00-22:49 | 4.22  |
| 23:00-23:49 | 8.10  |
{: .centered-table }

Well, it's very close to true! I was an hour early, I'm most productive between
midnight and 3 AM.

The more impressive (and scary) thing is that I've written during literally
every hour of the day. Who's even awake at 5 AM? And given that I have 1.67
hours of writing at that time, I must have done it *at least twice*. I never
claimed to be good at managing my time.


Time Spent Per Post
-------------------------------------------------------------------------------

My time tracker data doesn't store the post I was writing at the time. However,
thanks to the magic of Git, I can reconstruct what post I was writing on a given
day.

This blog is a Github Pages blog, so every change to this blog is done through
a Git commit, with timestamp. First, I exported all commits I've ever made.

With a few exceptions, the Git history for this blog is structured as a tree.
EVery post starts by branching off of `master`. I work on the draft there,
building my site locally to preview how it looks. When the post is finished,
I go back to `master`, then run `git merge --squash <branch name>`. This
creates a single commit that's the sum of all changes made in that branch.

This workflow means that writing-wise, the only meaningful commits are on the
offshoot branches. These commits lie on exactly one branch, which corresponds
to exactly one post.

My time tracker data doesn't store the post I was writing
at the time, but by cross-reference this data with my Git commit timestamps,
I can figure out how long I spent writing each post.

Meanwhile, my time tracker data is a list of non-overlapping (start, end)
intervals. If a commit lies within the interval, it's definitely paired with
the same post as that commit. Not every interval contains a commit, since
I didn't commit my work during every writing session. but I can assign
these intervals based on the closest commit.

Here's the time spent for each post, from most to least. For context, I also
include the number of words in that post.

| &nbsp;&nbsp;Post&nbsp;&nbsp;                | Hours | &nbsp;&nbsp;Word Count&nbsp;&nbsp; |
|---------------------|-------|------------|
| rl-hard             | 53.33 | 9426       |
| (Draft)             | 15.27 | N/A        |
| iclr-icra           | 10.68 | 1790       |
| blog-paper          | 8.22  | 1319       |
| friendship-paradox  | 7.72  | 1542       |
| five-seconds        | 6.43  | 1872       |
| mlp-music           | 5.28  | 450        |
| magic-arena         | 5.23  | 1280       |
| mlp-italy           | 4.32  | 957        |
| mh-2018             | 3.68  | 2112       |
| 2year               | 3.38  | 1256       |
| research-tax        | 2.82  | 1276       |
| sim2real-grasping   | 1.95  | 155        |
| dota2-five          | 1.3   | 1464       |
| (Draft)             | 1.02  | N/A        |
| (Draft)             | 0.72  | N/A        |
{: .centered-table }

A few people have asked me how long it took me to write my reinforcement
learning post. Well, there's your answer: 53 hours, 20 minutes. Based on
commit timestamps, the first word was written August 2017, regular writing
started October 2017, the first draft was done Christmas 2017, and editing
based on early feedback was done between Christmas and Valentine's Day,
with the post releasing February 14, 2018.

The time for that post actually lines up eerily well with the word count.
The RL post was almost 40% of the words I wrote this year, and the post took
almost 40% of my writing time. This correlation immediately falls apart for the
other posts.

You may have noticed the crazy outlier of "1.95 hours to write 155 words". It's
very misleading. Based on my commit messages, that post included updates to my
About page and Research page, which isn't reflected in the reported word count.

There are two other outliers. I spent 1.3 hours writing 1464 words for the
OpenAI Five post. If you read that post, the lack of polish should be obvious.
I spent 5.28 hours writing 450 words for the MLP Music Recs page, but for that
page, most of my time was spent digging up songs and making judgment calls
on what to share.

As for the draft posts: we'll see if I finish any of those. I believe it's
perfectly healthy to have lots of incomplete projects. You aren't obligated
to finish everything you start. Still, it feels weird to have 15 hours of work
on a draft when most of my posts take less than 10.
