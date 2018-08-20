---
layout: post
title:  "Three Years Later"
date:   2018-08-18 01:22:00 -0700
---

*Sorta Insightful* turns three years old today! Whether you were here from the
beginning, or just discovered this blog, thanks for reading.

I normally write a sappy, self-reflective post for my blogging anniversary. This
year, I'm deciding to do a bunch of data analysis instead. It's still
self-reflective, just in a different vein.


Words Written
----------------------------------------

Last year, I wrote [22,409 words]({% post_url 2017-08-18-two-years %}).
How about this year?

I wrote **24,449** words. Here's the breakdown in chronological order.

{% highlight python %}
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
{% endhighlight %}

I wrote 12 posts this year, following my trend of 1 post a month on average.

Eagle-eyed readers may notice that the [reinforcement learning post]({% post_url 2018-02-14-rl-hard %})
was much, much longer than the rest, taking up almost 40% of the words I wrote for
*Sorta Insightful* this year.


View Counts
--------------------------------------------------------------------------

These view counts are aggregated from August 18, 2017 to today.

{% highlight python %}
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
{% endhighlight %}

Okay, I knew the RL post would be the outlier. I didn't think it would be the
outlier by that much. Jeeeez.


Time Spent Writing
--------------------------------------------------------------------------

For the past two years, I've been using [Gleeo Time Tracker](https://gleeo.com/index.php/en/)
to track my time. I track a few things: how long I sleep, the length of my commute,
how much time I spend reading books and [web fiction](/webfictionrecs),
what video games I play (and for how long), and how long I spend writing.

Despite having two years worth of data, I've never bother doing any analytics
on it. This post felt like a good excuse to start.

Excluding the time spent on this post, I spent **131 hours, 21 minutes** writing
for my blog this year.
At first, this felt like less than I expected, but this averages out to about
21-22 minutes a day, which feels correct.


When I Write
---------------------------------------------------------------------------

Most days, I don't do any writing. My motivation comes in bursts. I like
starting and finishing posts within a few days, and it feels like I do the most
writing on the weekends. Is that true?

Gleeo Time Tracker doesn't have the tools for this built-in, but you can
export your time tracking data as a CSV file. This makes it straightforward to
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

Turns out I was *super wrong!* I actually do most of my writing on Wednesday.
I guess blogging is my outlet for getting through the middle of the week?

Alright, so I was wrong about the day of the week. How about the time of day?
I've often joked that my most productive writing hours are between 11 PM and 2 AM.
Is that true?

| &nbsp;&nbsp;Time of Day&nbsp;&nbsp; | Hours |
|-------------|-------|
| 00:00-00:59 | 22.67 |
| 01:00-01:59 | 29.92 |
| 02:00-02:59 | 17.88 |
| 03:00-03:59 | 5.83  |
| 04:00-04:59 | 2.20  |
| 05:00-05:59 | 1.67  |
| 06:00-06:59 | 1.27  |
| 07:00-07:59 | 1.50  |
| 08:00-08:59 | 1.00  |
| 09:00-09:59 | 1.00  |
| 10:00-10:59 | 1.00  |
| 11:00-11:59 | 1.72  |
| 12:00-12:59 | 1.00  |
| 13:00-13:59 | 0.38  |
| 14:00-14:59 | 1.77  |
| 15:00-15:59 | 1.60  |
| 16:00-16:59 | 4.30  |
| 17:00-17:59 | 4.48  |
| 18:00-18:59 | 5.28  |
| 19:00-19:59 | 3.40  |
| 20:00-20:59 | 3.78  |
| 21:00-21:59 | 5.38  |
| 22:00-22:59 | 4.22  |
| 23:00-23:59 | 8.10  |
{: .centere5d-table }

Well, it's very close to true! I was an hour early, I'm most productive between
midnight and 3 AM.

The more impressive (and scary) thing is that I've written during literally
every hour of the day. Who's even awake at 5 AM? And given that I have 1.67
hours of writing at that time, I must have done it *at least twice*.


Time Spent Per Post
-------------------------------------------------------------------------------

My time tracker data doesn't store the post I was writing at the time. However,
thanks to the magic of Git, I can reconstruct what post I was writing on a given
day.

This blog is a [Github Pages](https://pages.github.com/) blog, so every change to this blog is done through
a Git commit, with timestamp. First, I exported all commits I've ever made.

With a few exceptions, the Git history for this blog is structured as a tree.
Every post starts by branching off of `master`. I work on the draft there,
building my site locally to preview how it looks. When the post is finished,
I go back to `master`, then run `git merge --squash <branch name>`. This
creates a single commit that's the sum of all changes made in that branch.

This workflow means that writing-wise, the only meaningful commits are on the
offshoot branches. These commits lie on exactly one branch, which corresponds
to exactly one post.

This gives me a list of commit times (from Git) and a list of `(start, end)`
intervals (from my time tracker).
If a commit lies within the interval, it's paired with that interval.
Not every interval contains a commit, since I didn't commit my work during
every writing session. but I can assign those intervals based on the closest
commit. Summing all the intervals paired with the commits on a given branch
gives me the time I've spent working on that post.

Here's the time spent for each post, ordered from most to least. For context, I
also include the number of words in that post.

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
commit timestamps, the first draft was started August 2017, most of it
was written between October 2017 and Christmas 2017, and editing based on
early feedback was done between Christmas 2017 and Valentine's Day 2018.

The time for that post actually lines up eerily well with the word count.
The RL post was almost 40% of the words I wrote this year, and the post took
almost 40% of my writing time. This correlation immediately falls apart for the
other posts.

You may have noticed the crazy outlier of "1.95 hours to write [155 words]({% post_url 2017-09-25-sim2real-grasping %})". It's
very misleading. Based on my commit messages, that post included updates to my
About page and Research page, which isn't reflected in the reported word count.

There are two other outliers. I spent 1.3 hours writing [1464 words]({% post_url 2018-06-27-dota-2-five %}) for the
OpenAI Five post. If you read that post, the lack of polish should be obvious.
I spent 5.28 hours writing 450 words for the [MLP Music Recs](/mlpmusicrecs)
page, but most of the work there was spent searching up songs on YouTube and
narrowing the list down to 1 song per artist.

As for the drafts: we'll see if I finish any of those. I believe it's
perfectly healthy to have lots of incomplete projects. You aren't obligated
to finish everything you start. Still, it feels weird to have 15 hours of work
on an unfinished draft, when most of my posts take less than 10.


What's Next?
----------------------------------------------------------------------------

Well, to be honest, I'm not really sure. Historically, if I say I'll write a
post in the upcoming year, I never get around to writing it. This year, I'm
deciding not to commit to writing anything. Instead, I'll write whatever I
have motivation to write. This isn't really a change, it's simply me being
more realistic about what's going to happen.

Although, to be honest, I do still want to write that post about
*Gunnerkrigg Court*. I've been talking about writing that post for over two
years. One day, it'll happen. It has to.
