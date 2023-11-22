---
layout: post
title:  "A Neopoints Making Guide For The Busy Adult"
date:   2023-11-08 00:02:16 -0700
---

The new management of Neopets is trying to start a Neopets Renaissance. They've brought back Flash games, thanks to [Ruffle](https://ruffle.rs/), a Flash emulator written in Rust.
New content is coming out, with an acknowledgement that the playerbase is mostly nostalgic adults rather than new kids.
Although the site aims to maintain its kid-friendly exterior, the inside has changed. The most recent Faerie
Festival was incredibly queer coded and I think that was intentional.
These days, the typical Neopets user is a mid 20s woman that's more likely to be LGBT than straight. See
this [unofficial demographics survey](https://www.reddit.com/r/neopets/comments/zft93c/neopets_user_base_demographics_survey_results/) for more.

This has all come with change, and I have slightly mixed feelings.
I like Neopets as a time capsule of the early 2000s Internet, and every change erodes that image. Still, expecting it to stay the
same forever was never a realistic assumption to have.

It's too early to tell if the Neopets Renaissance is real, but a decent number of people are coming back,
many with the same question: how do I afford anything?

**Buddy do I have the post for you!**

You know how much time I have spent studying how to squeeze Neopoints water out of the Neopets stone? WAY TOO MUCH TIME. Like really it's too much. I should stop.

Part of your duty to humanity is that if you spend a bunch of time learning something, you should teach what you've learned so that other people
don't have to go through the same struggle. Yes, even if it's about Neopets.

Most mega-rich Neopians made money from playing the item market. Figure out the cost of items, buy low sell high,
read trends based on upcoming site events, and so forth.
When done properly, this will make you more Neopoints than anything else. Like real-world finance, if you have the right idea before anyone else,
you can turn it into lots of Neopoints. Also like real finance, doing so requires a baseline level of dedication and activity to keep up-to-date
on item prices, haggle for good deals, and get a sense for when a price spike is real or someone trying to manipulate the market.
There is no regulation, with all the upsides and downsides that implies.

This post is *not* about that.

![Ain't nobody got time for that](/public/np-guide/notime.gif)
{: .centered }

Instead, this post is about ways to extract value from the built-in site features of Neopets.
Everything here is doable without having to directly interact with another Neopets user, aside from selling items for profit.

I have ordered this post from most to least impactful. This means I am leaving out *tons* of site actions that give you free stuff, because a lot of
it just isn't worth your time. Still, even many of the things in this post aren't worth your time.


# Daily Quests

These are super new, just a few weeks old, and are the reason I started writing this post at all.

Each day, you get five daily quests. These are small, tiny tasks, like "play a game" or "feed a pet".
Each quest gives a reward, either Neopoints or an item from the daily quest pool.
Doing all 5 dailies gives a 20k NP bonus. I'd say you can expect to get about 25k NP a day, depending
on how many NP rewards you get.

The weekly reward is the thing that made the news. If you do all daily quests 7 days in a row, you get a
weekly reward, and the weekly rewards are *insane*. The prices are still adjusting rapidly, but at time of
launch, my weekly reward was a book valued at 40 million NP. By the time I got it, the price had dropped
considerably, and I ended up selling it for 450k NP, but that was still 64.2k NP / day of profit for very little work.

As you might imagine, this caused a lot of upheavel in the economy. That book I sold for 450k NP is now selling
for 200k NP, and the price will likely keep dropping. My guess is that prizes will end up somewhere around 150k NP,
and if we include the daily reward in that, we get an estimate of

$$
    25,000 + 150,000/7 \approx 46,400 NP/day
$$

Neopets has an inflation problem. For various reasons, money doesn't leave the Neopets ecosystem as fast as it should. It's not a total disaster, but
it is bad. There are some nice plots made by [u/UniquePaleontologist on Reddit](https://www.reddit.com/r/neopets/comments/16madug/lets_talk_about_inflation/) charting
item prices going back to 2008, which is almost 15 years of data! To quote the post,

> my background is in biology and data science not economics but I do love my broken html pet simulator

![Chart of prices](/public/np-guide/inflation.webp)
{: .centered }

This is a plot of paintbrush prices over time. Prices are in log scale, paintbrush prices are the red curve,
and a random basket of 1000 items is the gray curve. We see that random items have trended down over time, but
paintbrushes have gone crazy. Looking from 2014 to 2023, paintbrush prices have increased by 7.4x, corresponding
to almost a 25% year-over-year increase.

The weekly reward is the thing that makes daily quests so appealing.. Wjem TNT launched the weekly pool, they aimed SUPER HIGH on the item pool. The weekly reward I had when they launched was a book that had market price of 40 million.

Or rather, I should say it used to be 40 million, by the time I got it they were selling for only around 400k. This is TNT's direct shot against item inflation. A large set of items are expensive because of scarcity rather than demand. Not that there's zero demand, just that the demand is small but  supply is even smaller.

It's unclear where exactly the prices of weekly reawrd items will land, but right now I'd estimate it averages as about 50k-100k NP per day averaged over the entire item pool if you get to the weekly reward every day.

# Food Club

We move to the exact oposite of Daily Quests. Daily Quersts were created right now, to directly combat inflation, via a daily system straight out of a mobile gaming playbook to increase retention.

Food Club is a dumb system made 20 years made 20 years ago, with no long term planning, and is now the major source of inflation on its own.

I'm getting ahead of myself. How does this work?

Think of food club as like horse racing. it's like horse racing. There are 5 arenas, where 4 pirates compete in each for who can eat the most food. There is some hidden formula defining win rate that I'm sure you could derive from data if you wanted to, but, in general, you can assume the odds for a pirate corresponds to its win probabilitiy.
A 4:1 pirate will have a win rate of about 25% and on average, betting on them will neither win nor lose Neopoints.

However, Neopets does something weird. The payout for a Pirate is always rounded to the nearest integer, cannot go lower than 2:1, and cannot go higher to 13:1. So, suppose you have an arena like this:

2:1
8:1
10:1
13:1

We know that (math goes here). The end result is that, the 2:1 pirate has win probability much higher than 50%.

Food club allows you to make 10 bets, and strategy corresponds to identifying these positive expected value pirates, and exploiting them as much as possible. There are varied strategies for how to do this, but typical strategies average a 70%-90% profit on average. If you don't want to learn strategy, there are plenty of "Food Club influencers" who publicly post their
bets each day, and you can just copy one of them.

The maximum bet size you can make is 50, pluse 2 for every day your account has been on Neopets. Who knows why they picked this?Now, suppoose that many accounts on Neopets are over 15 years old, such that people can regularly make 10k+ sized bets. At 10 bets per day, this gets you to 40k-90k of profit a day.

This is a pretty insane amount of money, because it's pure NP. It's not driven by the market price of items. It's just, money flowing into the economy.
It's also incredibly easy to automate. u/neo_truths is a grey had hacker who has access to Neopets source code, and oaccsionally does deep dives into Neopets database logs. They've disclosed that there is a Food Club botter,.
Using one of the (many) Neopets data breaches, they've built a bot net of several thousand Neopets users, using old abandoned accounts, then had them all play Food Club.

It's a real problem, but I'm not sure TNT has an easy way pout of it. Food Club is basically the recommended NP making tool for anyone who comes back to the site, and
I think there'd be riots if they got rid of it. For now, go bet on those pirates.

# Trudy's Surprise

This feature was added a few years ago, and is basically a pure NP giveeaway. Like other dailies released recently, it rewards frequent play. If you visit Trudy's Surprise every day, you are guaranteed to get a 100k payout on day 25. Even before then, you get around 16k per day at minimum once you get to the 7 day streak. See JellyNeo's table.

# Wishing Well

We now get into the more pure gambling aspects of the site.

The Wishing Well is a place where you can toos in Neopeoints and wish for a specific item. All items of rarity below (XX) are allowed, and you can make 14 swishes per day (7 in the morning and 6 in the evening). Each wish costs 21 NP and throwing in more doesn't affect the odds at all.

Each day the well picks 240 winners. The winning item

What makes the wishing well profitable is that the most expensive rarity XX item is usuallly way, way more epensive than the wishing cost. In the past teh cost of such items was around 300k. Now the most expensive items are around 1 million. You can usually find what to wish for by seeing whats most common in the winner list from yesterday.

Given that it only costs 140 NP a day, you only need a 1 in 3000 (CHECK MATH)) chance of winning to make this worth it. What are your true odds of winning?
Well, I haven't done the math or stats tracking, but at current user activity, I usually win a few times per year.

This is naturally something that will get less profitable wiif more peopel know about it, and I have genuinelye considered not mentioning it, but I figure the effect isn't that big a deal and I have enough NP that I don't mind telling the secret.
(It's not even much of a secret anyways.)

Assuming a hit rate of 2 prizes per year, this averages out to TODO profit per day on average. Expect to get less profit if you're trying to quick-sell items to convert them into pure cash (Neopoints) though.

# Battledome

Ah, the Battledome. You play long enough, you end up with one high-end outlet. For me that was the Battledome. Top tier items can literally extend up to over a billion Neopoints.

The Battledome went through a revamp in XXXX, which diehard fans usually don't like because it both removed HP increase and introduced a bunch of broken abilities that need to be banned in competitive play for balance purposes. However, it did introduce a new way to get rewards from fighting CPU opponents - that's what we're focusing on here.

The exact mechanics and drop rates from challengers is not fully known, but here's what is known. There is a global pool of items, that all challengers drop. That pool depends on the
arena a challenger is in. There's a challenger specific pool, which gets added to that pool. The drop rates vary but it appears that certain arenas are more likely to drop from the global pool than other ones. (Link the reddit post here.)

(Link the neo truths post here too)

The only valuable items in the global pool are codestones, the currency used for battledome training. The Water Dome also drops dubloons, which can also be used for training but are pretty marginal. **Most** challenger specific pools do not have good items, so the recommendation is usually to fight

* Koi Warrior, any difficulty
* Giant Mutant Spectral Walrein, medium difficulty

since they have the smallest pool of specific items and therefore are most likely to give codestones. However, on occasion it's worth fighting other challengers for their specific drops.

* The Kreludor Robot, which rarely drops Armored Neggs. Those Neggs are a stat
boosting item and often sell for a lot. The Kreludor Robot is also one of the easiest
challengers in the battledome and is a common "starter" challenger to fight
while training for tougher ones.
* The premium challengers (Space Faerie, CHECK), which are only available to
Neopets premium users, but which drop Nerkmids and Giant Bubbling Space Fungus, both valuable items.
The first can be gambled for paint brushes at the Alien Vending Machine, and the
latter is a stat-boosting item for Battledome trainers.
* The Snowager, which is by far strongest enemy you could fight, but which has a
small chance of dropping Frozen Neggs. These can be directed traded for Negg points,
which essentially makes them as valuable as the most expensive Negg. The most
expensive Negg is usally the Snegg, since top 1% rich Neopians compete on who
can get the most HP, and Sneggs are one of the few effective ways to do so if
money is no object.

The profit depends on market prices of the items, but on average,

Snowager > Premium Challengers > Walrein > Koi Warrior > Kreludor

This, coincidentally, is also the order of difficulty for how hard they are to fight.

Fighting the Snowager is the highest variance, since your profit is all based on
Frozen Negg drops. You get 15 item drops per day, and based on stats, you can
expect to see around 10 Frozen Neggs per **month**. But right now, Frozen Neggs
cost 450k. Assuming you can sell for that much, it should average 150k NP per day,
and this is ignoring the random Codestone drops along the way.

If you can't beat the Snowager, and don't pay for premium, you can still get NP from
Codestone drops. Codestone prices change but right now (put in the math here) and
you can expect to get N codestones a day.

Unfortunately you'll need to train a Neopet for several months to get to the point
of fighting the Snowager. Training a Neopet takes a lot of time and money (see Codestone
prices above), but if you want to train for other reasons, you might as well set a goal
of getting to the Snowager tier. I recommend using the "rush to level 250" strategy
described here. It has more set-up time but is more efficient at getting to max stats
in both time and money.

TABLE

# Bank Interest

In real life, the interest rate you get in a savings account is driven by the Treasury's
interest rate, which is based on a bunch of complicated factors over what they want the
economy to look like.

In Neopets it's driven by how many Neopoints you deposit. The more you store, the more interest
you get. At the top-most bracket (10 million Neopoints), you earn 12.5% interest per year.

You may be thinking "doesn't this promote rich-get-richer?" and yep you're entirely right. You
may also be thinking "isn't 12.5% interest per year a lot?" and yep, you're also right.

This is never going to be a big part of your daily income unless you have a ton of money already,
and if you already have a ton of money I don't know why you're reading this guide. I mention it because
it is the floor for any investments made (where usually this means "rare items").

# The Stock Market

Ahh, the stock market. According to legend, stock prices used to be driven by user behavior.
Then some users coordinated a stock pump and dump, so it got changed to be entirely random.
This doesn't stop people from posting "to the mooooon", especially during the Gamestop
craze of 2020.

Each day, you can buy up to 1000 shares of stock. You're only allowed to buy stock that's
15 NP/share (or 10 NP/share if you have the Battleground boon - more on that later).
You can sell as much stock as you want,
paying a 20 NP commission per transaction. (In practice this commission is basically zero
and I'll be treating it as such.)

If stock motion is entirely random, how can you make money? You can think of stock prices
like a random walk. Sometimes they drift up, sometimes they drift down,
but you only realize gains or losses at the time you sell.
So you simply hold all the stocks that go down, and sell the lucky stocks that go up.
Every stock will *eventually* cross into profitable territory, it just might take a while.

The common advice is to set a sell threshold, and sell only when the stock crosses that price.
Conventional wisdom is to sell at 60 NP/share. But how accurate is this wisdom?
A *lot* of analysis has been done by users over the years, including:

* A histogram of price movements from [JellyNeo](https://www.jellyneo.net/?go=neopian_stock_market).
* A [neostocks.info](https://neostocks.info/) site that lets you check historical stock prices
* Corresponding analysis of [neostocks data](https://www.reddit.com/r/neopets/comments/af8p38/comment/edwe8lo/) by u/not-the-artist on Reddit.

This data all suggests the conventional wisdom of selling at 60 NP/share is correct, since price movement
seems dependent on current price, and the 61-100 NP range is where average price movement changes from
0 to slightly negative. The cause of this was eventually revealed by u/neo\_truths's leak of the Stock
Market [pricing algorithm](https://www.reddit.com/r/neopets/comments/xrlfd3/stock_market/).

> Set max move to current price / 20
> Set max move to current price / 50 if current price > 100
> Set max move to current price / 200 if current price > 500
> Set max move to current price / 400 if current price > 1000
> Round up max move
>
> Set variation to random between 1 and max move * 2 - 1. Randomly add +1 to variation with 1/20 chance. Randomly subtract 1 with 1/20 chance.
>
> If current price >= 10 and current price / opening price > 1.15 [subtract] max move / 4 rounded down from variation
> If current price >= 10 and current price / opening price > 1.3 [subtract] max move / 4 rounded down from variation
>
> Set points to variation - max move rounded down
> Set p to min(current price * 10, 100)
> If points + current price > 5, change stock price to current price + points with p% chance

Some re-analysis by u/not-the-artist is [here](https://www.reddit.com/r/neopets/comments/xrlfd3/comment/itjn5de/),
confirming this leak is consistent with what was seen before. The TL;DR is that the only lines that cause net price
drops are

> If current price >= 10 and current price / opening price > 1.15 [substract] max move / 4 rounded down
> If current price >= 10 and current price / opening price > 1.3 [substract] max move / 4 rounded down

Thanks to rounding, these conditions only fire when `max move` is at least 4, and if we look above, this
only starts happening in the 61-100 NP range.

Using a 60 NP sell threshold will lead to an average holding time of 399 days. When bank interest is accounted for,
1000 shares of 15 NP stock is worth around 29.5k NP. (It is lower than 60k NP because you miss on 399 days of bank
interest - full math is done [here](https://www.reddit.com/r/neopets/comments/y8bqig/leaked_code_determining_best_stock_selling_price/) for the curious).
This gives a profit of 14.5k NP per day, assuming you can pay for 1000 shares/day and are patient enough.

Note this is less than Trudy's Surprise. Yeah we're falling into the weeds now.

# Coconut Shy

This is one of many gambling minigames themed around ones you'd see in amusement parks. Like amusement parks, most
of the games are scams. Coconut Shy is one of the few exceptions.

You can throw 20 balls per day for 100 NP each, earning one of five outcomes.

* A miss (0 NP)
* A small hit (50 NP)
* A strong hit that doesn't knock over a coconut (300 NP)
* Knock over a coconut (10,000 NP + a random Evil Coconut)
* The coconut explodes (Jackpot - 500,000 NP)

The two outcomes worth money are the last two. The jackpot is obviously good, but the Evil Coconuts are actually
worth *more*. The Evil Coconuts are stamps, and some Neopets users love collecting stamps. The Coconuts actually
sell for more than the Jackpot right now - current price looks like it is between 750k-1 million per Coconut.

Coconut Shy odds were leaked by u/a\_neopian\_with\_info in this [Reddit post](https://www.reddit.com/r/neopets/comments/wc4nsi/deserted_fairground_games_odds/).
Let's assume you use the Halloween site theme, which slightly improves your odds. The payout table is

| Payout | Probability |
| ------ | ----------- |
| 0 NP   | 20% |
| 50 NP  | 65% |
| 300 NP | 14.9% |
| 10,000 NP + Evil Cocunut (estimated value 750,000 NP) | 0.99% |
| 500,000 NP | 0.01% |

Combined this gives an expected payout of 834.6 NP per throw. Each throw costs 100 NP, so doing 20 throws per day
gives 14,692 NP expected profit per day. Again, this is high variance though, all your payout is on winning a coconut
or hitting the Jackpot, which happens every 50 days on average.

If you decide to go Coconut throwing, you won't be able to throww it by clicking the site, but you can still play
the game by visiting the direct link mentioned on [JellyNeo](https://www.jellyneo.net/?go=coconut_shy). I am honestly
surprised the Evil Coconuts are still so expensive. My guess is that most users don't know Coconut Shy is net profitable,
or the ones that do can't be bothered to do it.

# Faerie Caverns

The Faerie Caverns are a daily where you pay 400 NP to enter the cave, and win a prize if you make it to the
end. You have a 1 in 8 chance of doing so (you have to win three 50-50 coin flips in a row), and can attempt
once per day.

People do this daily because of the Faerie Caverns stamp, which is only available from this daily and sells for
around 50 million NP. However, your odds of winning it are *very* slim. According to a u/neo\_truths [leak](https://www.reddit.com/r/neopets/comments/xwyrf0/faerie_caverns_grave_danger/),
if you win the 1 in 8 and get to the end, your payouts are

| Payout | Probability |
| ------ | ----------- |
| 500 NP to 2,500 NP   | 89.9% |
| 5,000 NP | 4.9% |
| 10,000 NP | 5.1% |
| 25,000 NP + item prize | 0.1% |

Of the item prizes, you have a 10% chance of getting a Faerie Paint Brush, and a 90% chance of winning one of Beautiful Glowing Wings,
Patamoose, Faerie Caverns Background, or Faerie Caverns Stamp. You can see in the odds that Faerie Paint Brush is
considered the best prize, so it's funny that every other prize is worth more.

TABLE HERE

If you do the expected value math, then doing Faerie Caverns is net profitable. However I personally don't do this
daily because of how top-heavy it is. It's only net profitable if you win an item prize, which will happen
1 in 8000 days on average. Someone could legitimately have played Faerie Caverns every day for *the entire lifetime of the site*
and not won an item prize.

Still, if you have the time, go ahead. 400 NP a day is pretty cheap.

# Battleground Boons

The Tyrannian Battleground is an ongoing site-wide event. Every 2 weeks, you can sign up for a team,
and for the week after that each team competes to see who can defeat the most enemies from the other team.
(You fight CPU enemies, not other players.)
If you fought at least 10 battles, and your team wins, then you get to choose a boon that lasts for 1 week.

Some of these boons are important modifiers for earning money.

* The Bank Bribery boon increase bank interest by 3%.
* The Cartogriphication boon guarantees you make it to the end of the Faerie Caverns, which flips it from
"high variance positive EV" to "guaranteed money".
* The Cheaper by the Dozen boon lets you buy stocks at 10 NP instead of 15 NP.

In general, these boons are nice but I don't think they're worth going for. The way the battleground works
is that it picks the team with highest *average* contribution, not highest total contribution. The boons
available to each team are different, and usually the team with the best boons gets the most members that
do the bare minimum and hope to get carried to a win. So there's no guarantee you even get a boon
in the first place. You could try to become a dedicated member to give yourself good odds of winning a boon,
but I think this is more trouble than it's worth.


# The Neopian Lottery

Okay, no you should not do this one, but it's funny so I'll give it a quick shoutout.

In the Neopian lottery, you can buy tickets (up to a limit) with different
numbers, and the jackpot is paid to the user with the most matching numbers (or split among
all such users in the case of a tie). Importantly the lottery jackpot is 100% of all ticket
sales + a 5k starting pot. Since the lottery *always* pays out, it's technically positive
expected value to buy a lottery ticket.

The expected value is like, 1 NP/ticket at best, and you will easily earn more playing a Flash
game. But I think it is just a perfect symbol of Neopets dailies. It's a random slot machine,
but unlike a real casino the odds are very slightly in your favor.
