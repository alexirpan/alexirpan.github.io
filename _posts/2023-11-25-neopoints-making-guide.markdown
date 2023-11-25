---
layout: post
title:  "Far More Research Into Making Neopoints Than Anyone Needs to Know"
date:   2023-11-25 00:33:00 -0800
---

The new management of Neopets is trying to start a Neopets Renaissance. They've brought back Flash games, thanks to the
Rust-based flash emulator [Ruffle](https://ruffle.rs/).
New content is coming out, with an acknowledgement that the player base is mostly nostalgic adults rather than new kids.
Although the site aims to maintain its kid-friendly exterior, the inside has changed.
These days, the typical Neopets user is a mid 20s woman that's more likely to be LGBT than straight. (See
this [unofficial demographics survey](https://www.reddit.com/r/neopets/comments/zft93c/neopets_user_base_demographics_survey_results/).)
The most recent Faerie Festival was incredibly queer coded, to the point I'd be shocked if it weren't intended.

I have slightly mixed feelings about all the changes.
I like Neopets as a time capsule of the early 2000s Internet, and every change erodes that image. Still, expecting the site to stay the
same forever was never a realistic assumption to have.

It's too early to tell if the Neopets Renaissance is real, but a decent number of people are coming back,
many with the same question: how do I afford anything?

**Buddy do I have the post for you!**

You know how much time I have spent studying how to squeeze Neopoints water out of the Neopets stone? WAY TOO MUCH TIME. Like really I've spent too much. I should stop.

Part of your duty to humanity is that if you spend a bunch of time learning something, you should teach what you've learned so that other people
don't have to go through the same struggle. Yes, even if it's about Neopets.

Most mega-rich Neopians made money from playing the item market. Figure out the cost of items, buy low sell high,
read trends based on upcoming site events, and so forth.
When done properly, this makes you more Neopoints than anything else. It's similar to real-world finance, where
there can be very short feedback loops between having the right idea and executing on that idea for profit.

Also like real finance, doing so requires a baseline level of dedication and activity to keep up-to-date
on item prices, haggle for good deals, and get a sense for when a price spike is real or when it's someone trying
to manipulate the market. There is no regulation, with all the upsides and downsides that implies.

This post is *not* about playing the market, because any such advice would be very ephemeral, and also,

![Ain't nobody got time for that](/public/np-guide/notime.gif)
{: .centered }

Instead, this is about ways to extract value from the built-in site features of Neopets.
We are going to do *honest work* and fail to ever reach the market-moving elite
class and we are going to be *fine with that*.
Everything here is doable without direct interaction with any other Neopets user,
aside from putting items in your shop to turn them into pure Neopoints.

I've tried to limit this to just things that I think are worth your time.
There are *tons* of site actions that give you free stuff, except the stuff is all
junk.


# Daily Quests

These are super new, just a few weeks old, and are the reason I started writing this post at all.

Each day, you get five daily quests. These are small, tiny tasks, like "play a game" or "feed a pet".
Each quest gives a reward, either Neopoints or an item from the daily quest pool.
Doing all 5 dailies gives a 20k NP bonus. I'd say you can expect to get about 25k NP a day, depending
on how many NP rewards you get.

The weekly reward is the thing that's special. If you do all daily quests 7 days in a row, you get a
weekly reward, and the weekly rewards are *insane*. The prices are still adjusting rapidly, but when they
first launched, my weekly reward was a book valued at 40 million NP. By the time I got it, the price had
dropped like a rock, and I sold it for 450k NP. That book now sits at 200k NP.

The prices of weekly rewards will likely keep dropping, and my guess is that the weekly prize will end up around
150k NP on average. If we assume the daily quests give 25k NP per day, and do them every day for week, we get an
average of (25,000 + 150,000/7) = **46,400 NP/day**.


## Aside: Item Inflation

For various reasons, money doesn't leave the Neopets ecosystem as fast as it should, and some items are rarer
than they should be.
It's not a total disaster, but
it is bad. There are some nice plots made by [u/UniquePaleontologist on Reddit](https://www.reddit.com/r/neopets/comments/16madug/lets_talk_about_inflation/) charting
item prices going back to 2008, showing trends over 15 years of data! To quote the post,

> my background is in biology and data science not economics but I do love my broken html pet simulator

![Chart of prices](/public/np-guide/inflation.webp)
{: .centered }

This chart is inspired by the [consumer price index](https://en.wikipedia.org/wiki/Consumer_price_index), and plots
paintbrush prices over time.
Paintbrush prices are the red curve, and a random basket of 1000 items is the gray curve.
This is in log scale, so increasing the y-axis by 1 means multiplying the price by 2.7x.

We see that random items have trended down over time, but
paintbrushes have gone crazy. Looking from 2014 to 2023, paintbrush prices have increased by around
7.4x. This is almost a 25% year-over-year increase. A similar trend appears in stamps and
other rare collectibles.

The common interpretation of the weekly quests is that TNT is directly fighting item inflation,
by picking rare items and drastically increasing their supply.
You could interpret this as TNT listening to their userbase and making
items more accessible, or you could view it as TNT desperately trying to get users
interested in playing again. The two are not mutually exclusive!

My interpretation is closer to the latter. The way weekly quests are implemented
feels straight out of a gacha game. You have to play every day, you do minor tasks
that each feel like they don't take time but add up to real time in total, and
the quests direct you to interact with parts of the site that could either keep you
around (Flash games) or encourage you to spend money (pet customization).
I've already been tricked into playing a Flash game to clear a daily quest, then playing
it again just for a high score.

Still, if they are going to pander to me with good items, I will take the good
items. I never said these gacha-style techniques didn't work.

![A weekly reward tracker with 1 of 7 books filled](/public/np-guide/dailyquest.png)
{: .centered }

Just six more days...
{: .centered }

# Food Club

We now move to the exact opposite of Daily Quests. Daily Quests were created
incredibly recently, with a partial goal of fighting item inflation, and intelligently
use techniques from a mobile gaming playbook.

Food Club is a dumb system, made 20 years ago without any conception towards the long-term
health of the site, and is a major reason the economy has so much inflation.

Think of Food Club as like betting on horse racing. No, scratch that, it's literally
betting on horse racing. Except the horses are pirates and the race is competitive
eating. There are 5 arenas, each with 4 pirates that compete for who can eat the
most food. You can make 10 bets a day, and earn Neopoints if your bets are correct.

There is some hidden formula defining win rate that I'm sure someone has derived
from data, but, in general, Neopets displays the odds for each pirate and you
can assume the odds for a pirate match its win probability.
A 4:1 pirate will have a win rate of about 25%, and betting on them is zero
expected value.

(Normally, gambling odds account for returning your wager, and 5:1 odds pays out 5+1=6 on a win and 0 on a loss,
corresponding to a 1/6 win probability. Food Club never returns your wager, so 4:1 pays out 4 and means a 1/4
win probability.)

Neopets always rounds pirate odds to the nearest integer, and never lets them go lower than 2:1 or higher than 13:1. We
can use this to our advantage.

Suppose we have an arena like this:

Pirate 1 - 2:1  
Pirate 2 - 6:1  
Pirate 3 - 13:1  
Pirate 4 - 13:1  

This is a real arena from today's Food Club, at time of writing. Let's figure
out the 2:1 pirate's win probability. We know the 6:1 pirate wins around 1/6 of the
time, and the two 13:1 pirates win around 1/13 of the time. (Possibly less, but
let's be generous.) The 2:1 pirate wins the rest of the time, so their win
probability should be around

$$
1 - \frac{1}{6} - \frac{1}{13} - \frac{1}{13} \approx 67.9\%
$$

If Neopets didn't round, the true payout for this pirate should be around 1.47:1. But thanks to
rounding, the payout is 2:1 and betting on this pirate is positive expected value.
We'd get an expected profit of 35.8%.

Food Club strategy is based on identifying the positive expected value pirates
and exploiting them as much as possible. Finding them is easy (you do the math
above for each arena), but deciding how risky you want to play it is where strategy
comes in. If you don't want to learn strategy,
there are plenty of "Food Club influencers" who publicly post their bets each
day on Reddit or Discord, and you can just copy one of them. Generally you can expect
an average profit of 70%-90% of what you bet each day, although you should only
start doing Food Club when you have enough of a bankroll to absorb losses. Around 50x your
max bet size should be good enough (covers up to 5 straight days of total busts).

The maximum bet size you can make is 50 plus 2 times your account age, in days.
Let's suppose you successfully recover your account that's 15 years old. You'd
be able to bet 11,000 NP per bet. With 10 bets per day and an 80% expected profit, that's
(10 * 11,000 * 0.8) = **88,000 NP/day**.

This is a *lot*. Who knows why TNT decided to make max bet size dependent on account age,
but it creates a real divide between users who recover their old account and
users who give up and start fresh. It's also incredibly easy to automate.
u/neo_truths is a grey hat hacker who has access to Neopets source code and database
logs, and occasionally discloses deep dives into Neopets data on Reddit. They've revealed
that based on request logs, it's very likely there is a Food Club botnet.
Thanks to the (many) Neopets data breaches, and lax Neopets security standards, there
are a lot of vulnerable accounts out there. The botter has presumably broken into
many old, abandoned accounts, took everything they had, and converted them
into Food Club players.

> 1. They have stolen over 40k accounts already (started late 2021) and keep stealing hundreds every week
>
> 2. Sum of historic food club profit having profit > 100k: 224b with 14.5k accounts
>
> 3. Sum of bank balance having balance > 100k: 51b with 14.5k accounts
>
> 4. Sum of on hand balance having balance > 100k: 2b with 1.5k accounts
>
> 5. Sum of shop balance having balance > 100k: 4b with 125 accounts

From [here](https://www.reddit.com/r/neopets/comments/138swva/richest_neopian/)
{: .centered }

This botnet is creating literally billions of NP each day, selling it for real money
on black market sites, and pumping NP into the economy.
It's pretty likely this is why item inflation has took off.
It's a real problem, but I'm not sure TNT has an easy way out. Food Club is
*the* recommended NP making tool for anyone who comes back to the site. Taking away free money is hard,
and it's a site feature that's stayed the same for so long that it has its own
inertia. They might revamp Food Club, but for now, go bet on those pirates.

![Food Club image](/public/np-guide/foodclub.png)
{: .centered }

# Trudy's Surprise

This is a daily they added in 2015, and just gives away more Neopoints.

Each day, you spin the slot machine and get NP based on how many icons you match.
Matching 0 icons vs all 4 icons is only a difference of 2k to 3k NP - the main trick
is that the base Neopoints value quickly rises with the length of your streak, reaching
18.5k NP/day starting at day 10 and a guaranteed payout of 100k on day 25. The streak then
resets. Trudy's Surprise also gives items for 7 day streaks, but these items are usually junk and
not worth anything.

<p class="centered"><img src="/public/np-guide/trudys.png" alt="Trudy's Surprise" style="width: 66%;"></p>

The payout table is listed on [JellyNeo](https://www.jellyneo.net/?go=trudys_surprise). We'll
assume that you make 0 matches every day and get to day 25 of the streak. This will include
one Bad Luck Bonus, an extra 2.5k paid the first time you get 0 matches during a streak.

Averaging over the payout table, we get to **17,915 NP/day**. Most of the money is made
between Day 10 and Day 25.

# Battledome

Ah, the Battledome. You play long enough, you end up with one high-end outlet. For me that was the Battledome. Top tier items can literally extend up to over a billion Neopoints.

The Battledome went through a revamp in 2013. Diehard fans usually don't like this revamp. It removed
HP increase from 1-player (which destroyed most single-player competition), removed complexity
that the 2-player community liked, and introduced Faerie abilities so broken that the majority
are banned in what little exists of the PvP scene.

The one good thing it brought was fight rewards. When you win against CPU opponents, you earn a small
amount of Neopoints and an item drop. The item drops can include codestones, which you can use to train
your pet. Or, you could just sell them directly. You get 15 item drops per day.

For a long time, the exact mechanics of drop rates was not fully known, aside from users quickly finding
that the Koi Warrior dropped codestones way more often. Over time, people found that there are arena-wide drops, which come from every challenger in that arena,
and challenger-specific drops, which depends on which challenger you fight.

There are a few sources of Battledome drop data:

* A list of Battledome prizes run by [JellyNeo's Battlepedia](https://battlepedia.jellyneo.net/?go=battle_prizes),
which lists all arena-specific and challenger-specific prizes, but without their drop rates.
* A crowdsourced dataset of Battledome drops summarized [here](https://www.reddit.com/r/neopets/comments/5alvls/battledome_loot_breakdown/).
This gives exact rates for codestone drops, but only aggregates the data into "codestone" versus "not-codestone".
Through this, we know find the arena of the opponent is the most important factor for codestone drops, and
there's little variation in drop rate for different challengers in that arena. The Koi Warrior is in
the Dome of the Deep, the arena with highest codestone drop rate, proving the conventional wisdom
is good.
* Much later, u/neo\_truths posted a leak on the [drop rates and drop algorithm](https://www.reddit.com/r/neopets/comments/yc488a/battledome_dome_loot/).
This gives exact rates for the arena-wide drops, but has no data on challenger specific drops.

First let's check the validity of this leak. Using data from that post, I coded a Battledome
drop simulator, and ran it to sample 100k items from each arena. You can download the Python
script [here](/public/np-guide/battledome_sim.py).
Let's compare this to the crowdsourced codestone drop rates.

<table style="margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th>Arena</th>
      <th>Codestones (crowdsourced)</th>
      <th>Codestones (simulator)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Frost Arena</td>
      <td>17%</td>
      <td>19.9%</td>
    </tr>
    <tr>
      <td>Cosmic Dome</td>
      <td>15%</td>
      <td>17.1%</td>
    </tr>
    <tr>
      <td>Pango Palladium</td>
      <td>14%</td>
      <td>16.6%</td>
    </tr>
    <tr>
      <td>Rattling Cauldron</td>
      <td>24%</td>
      <td>25.0%</td>
    </tr>
    <tr>
      <td>Central Arena</td>
      <td>11%</td>
      <td>12.0%</td>
    </tr>
    <tr>
      <td>Neocola Centre</td>
      <td>18%</td>
      <td>20.3%</td>
    </tr>
    <tr>
      <td>Dome of the Deep</td>
      <td>30%</td>
      <td>34.1%</td>
    </tr>
    <tr>
      <td>Ugga Dome</td>
      <td>14%</td>
      <td>15.3%</td>
    </tr>
  </tbody>
</table>

Overall the leak looks pretty legitimate! The simulator consistently overestimates the rate of codestone
drops, but this makes sense because it pretends challenger-specific drops don't exist. Every
time you get a challenger-specific drop, you miss out on an arena-wide drop, and codestones only appear
in the arena-wide item pool.

The reason I care about verifying this leak is that the Battledome drops more than just codestones, and I wwant
a more exact estimate of expected value from Battledoming.
Before going forward, we'll need to make some adjustments.
On average, the simulator codestone drop rate is around 89% of the true crowdsourced
drop rate. So for upcoming analysis, I'll multiply all drop rates from my simulator by 89%. (One way to
view this is that it assumes challenger drops are 11% of all item drops, and all such drops are worth 0 NP.)
To further simplify things, I'll only count a few major items.

* Codestones dropped by every arena. Training school currency.
* Dubloon coins dropped in Dome of the Deep. Training school currency.
* Armoured Neggs dropped in Neocola Centre. Can be fed to a Neopet for +1 Defense.
* Neocola tokens dropped in Neocola Centre and the Cosmic Dome. Can be gambled at the Neocola Machine, which has a chance of giving a Transmogrification Potion.
* Nerkmids from the Neocola Centre and Cosmic Dome. Can be gambled at the Alien Aisha Vending Machine, where has a chance of giving a Paint Brush.
* Cooling Ointments from the Frost Arena. Can cure any disease from your Neopet.

Using JellyNeo's estimated item prices at time of writing, we can find which arena gives the most profit, assuming
you play until you get 15 items.

<table style="margin-left:auto; margin-right:auto;">
  <thead>
    <tr>
      <th>Arena</th>
      <th>Expected Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Central Arena</td>
      <td>26,813 NP/day</td>
    </tr>
    <tr>
      <td>Ugga Dome</td>
      <td>27,349 NP/day</td>
    </tr>
    <tr>
      <td>Frost Arena</td>
      <td>35,428 NP/day</td>
    </tr>
    <tr>
      <td>Pango Palladium</td>
      <td>38,904 NP/day</td>
    </tr>
    <tr>
      <td>Rattling Cauldron</td>
      <td>48,521 NP/day</td>
    </tr>
    <tr>
      <td>Neocola Centre</td>
      <td>57,408 NP/day</td>
    </tr>
    <tr>
      <td>Dome of the Deep</td>
      <td><strong>69,046 NP/day</strong></td>
    </tr>
    <tr>
      <td>Cosmic Dome</td>
      <td><strong>135,557 NP/day</strong></td>
    </tr>
  </tbody>
</table>

I should warn you that getting to 15 items a day requires a *lot* of clicks, but the profit
available is very real. The Cosmic Dome is clearly best, but you can only fight those challengers if
you have Neopets Premium. Assuming you don't, you'll want to fight the Koi Warrior in the Dome of
the Deep instead.

A default untrained pet won't be able to defeat the Koi Warrior. If you are just getting started, my recommendation is to start with the
S750 Kreludan Defender Robot. It's in the Neocola Centre, and at just 14 HP it's an easy fight
that still gives 57.4k NP/day.
Then, you can
train your way up to fighting the Koi Warrior if you're so inclined. There are a bunch of guides
for how to train and what weapons are good to use. I recommend the weapon sets hosted by the Battlepedia,
[which are already updated](https://battlepedia.jellyneo.net/?go=weapon_recommendations) to account for daily quests making some items much cheaper.

One last thing. All analysis earlier assumes challenger-specific items are worthless.
There are two major exceptions.
First is the Giant Space Fungus.
The Giant Space Fungus is in the Cosmic Dome, and when fought on Hard it will sometimes drop
Bubbling Fungus, which can be consumed to increase Strength.
They sell for 136k NP each. The crowdsourced post from earlier found that Bubbling Fungus
was 1% of the item drops. Fighting it gives 0.15 Bubbling Fungus per day, or 20,400 NP/day extra.

![Bubbling Fungus](/public/np-guide/fungus.gif)
{: .centered }

The second is the Snowager. It's in the Frost Arena, and
can drop Frozen Neggs. These can be traded directly for Negg points, meaning they can get
traded for Sneggs which boost HP. Of all stat boosters, HP increasers are the most expensive,
since it's the only stat that can be increased without limit, and some high-end users like to
compete on having the strongest pet. Each Frozen Negg sells for 450k NP at time of writing.

![Frozen Negg](/public/np-guide/frozennegg.gif)
{: .centered }

Unfortunately there is not much data around on Frozen Negg drop rates. The best I found is
[this Reddit post](https://www.reddit.com/r/neopets/comments/13xq7qu/snowager_battledome_results_when_it_dropped/)
where they fought the Snowager every day between March 30th and June 1st. They got 24
Frozen Neggs in that time, which is an average of 0.375 Frozen Neggs per day. Assuming that
rate holds, the Snowager gives an extra 168,750 NP/day.
On top of the other Frost Arena items, you're looking at 200k NP/day!

The one snag is that both of these enemies are among the hardest challengers in the game. The
Giant Space Fungus on Hard has 632 HP. The Snowager on Easy has 650 HP.
If you are new to pet training, it could literally take you a year and millions of NP to get your
pet strong enough beat the Snowager. If your only goal is to earn money, it will pay off
eventually, but you'll need to be patient.
If you're willing to start that journey, I recommend following the route in the Battlepedia guide
(train all stats evenly up to level 100 / strength 200 / defense 200, then train only level to 250
to unlock the Secret Ninja Training School, then catch up the other stats). It'll save you both
time and money.

In summary,

* The Battledome can give you a lot of Neopoints per day if you fight until you get 15 items and
sell them each day.
* The profit order is Snowager > Giant Space Fungus (Hard) > any Cosmic Dome enemy > any Dome of the Deep enemy > S750 Kreludan Defender Robot
* Most players who don't have premium will stop at Dome of the Deep and reach 69k NP/day, but if you
are willing to commit to training up to Snowager levels you can earn 200k NP/day instead.

## Aside: The Eo Codestone Conspiracy

Eo Codestones have consistently been more expensive than other codestones. When asked why, the very common
reply is that Eo Codestones drop more rarely.

This has always felt off to me. An Eo Codestone sells for 33,500 NP. A Main Codestone sells for 3,000 NP.
You're telling me an Eo Codestone is over 10 times rarer than a Main Codestone? That seems crazy.

I ran my Battledome sim, and in both the Cosmic Dome and Dome of the Deep, I found that Eo Codestones
dropped at a similar rate to every other tan codestone.
I then checked my Safety Deposit Box, and saw the same thing - I have
about the same number of every kind of tan codestone. And I have a few hundred of each, so
I'm pretty sure the sample size is big enough.

The "drops more rarely" argument seems bogus. I have three remaining theories.

1. Codestones given out through other means (i.e. random events) are heavily biased towards Eo Codestones.
This seems unlikely to me. Most codestones should come from Battledome events these days, so even if random
events were biased, they shouldn't affect the distribution by enough to explain a 10x price difference.
2. The Mystery Island Training School asks for Eo Codestones more frequently than other ones. This could
explain the difference - similar supply, higher demand. I don't know of any stats for this, but this also
seems unlikely to me. At most I could see a codestone getting asked for 2x as often as another one, not 10x as often.
3. The Eo Codestone price is heavily manipulated to keep an artificially high price. This seems like the
most likely theory to me.

Unfortunately, knowing the price is likely manipulated doesn't mean I can do anything about it. The free
market's a scam, but it's the only game in town.

# Wishing Well

The Wishing Well is a place where you toss in Neopoints to make wishes. If you're lucky, your wish will be granted!

Each wish costs 21 NP, and you can make up to 14 wishes a day (7 in the morning and 7 at night).
You may wish for any item rarity 89 and below.

What makes the Wishing Well profitable is that the most expensive rarity 89 or below item is usually way, way more expensive than the wishing cost.
When I started doing the Wishing Well, the price of such items was around 300k, but now it's regularly over 1 million.
You can usually find what to wish for by seeing what's most common in the winner list from yesterday.

As for why it's so high? The Wishing Well only gives out 20 items a day, and this isn't enough to
make a dent in demand, especially when Neopets keeps releasing new items. Case in point - for
Neopets's 24th birthday, shops started stocking a Neopets 24th Birthday Goodie Bag. It was pretty
hard to obtain one thanks to restock botters, but people figured out they were a r79 item and just
started wishing for them.

![Wishing well wishes](/public/np-guide/wishing.png)
{: .centered }

People are asking for 7 million NP on the Trading Post for these bags. I don't think that will last.
For the purposes of estimating value, let's assuming a Wishing
Well item is worth 1 million NP. I'd say I win an item from the Wishing Well about 3 times a year.
Then the expected earnings are 3 million NP per year, or 8,219 NP/day. It costs 294 NP to make the wishes,
so this is **7,925 NP/day**.

The more people who make wishes, the less frequently anyone's wishes will be granted. I did consider not
mentioning the Wishing Well to preserve profit for myself, but I figure the effect isn't that big, and
it's not that much of a secret anyways.


# Bank Interest

In real life, the interest rate you get in a savings account is driven by the Treasury's
interest rate, which is based on a bunch of complicated factors over what they want the
economy to look like.

In Neopets it's driven by how many Neopoints you deposit. The more you store, the more interest
you get. At the top-most bracket (10 million Neopoints), you earn 12.5% interest per year.
You may be thinking "doesn't this promote rich-get-richer?" and yep you're entirely right. You
may also be thinking "isn't 12.5% interest per year a lot?" and yep, you're also right.

![Different kings of bank accounts](/public/np-guide/bank.png)
{: .centered }

This is never going to be a big part of your daily income unless you have a ton of money already,
and if you already have a ton of money I don't know why you're reading this guide. I mention it because
it's the floor for any money making method that doesn't convert into cash on hand. Such as...

# The Stock Market

Ahh, the stock market. According to legend, stock prices used to be driven by user behavior.
Then some users coordinated a stock pump, and it got changed to be entirely random.
This doesn't stop people from posting "to the mooooon" on the message boards, especially
during the Gamestop craze of 2021.

Each day, you can buy up to 1,000 shares of stock. You're only allowed to buy stock that's
at least 15 NP/share (or 10 NP/share if you have the Battleground boon - more on that later).
You can sell as much stock as you want,
paying a 20 NP commission per transaction. (In practice this commission is basically zero
and I'll be treating it as such.)

If stock motion is entirely random, how can you make money? You can think of stock prices
like a random walk. Sometimes they drift up, sometimes they drift down,
but you only realize gains or losses at the time you sell.
So you simply hold all the unlucky stocks that go down, and sell the lucky stocks that go up.

The common advice is to set a sell threshold, and sell only when the stock crosses that price.
The higher your threshold, the more money you'll make, but the longer you'll have to wait.
Conventional wisdom is to sell at 60 NP/share. But how accurate is this wisdom?
A *lot* of analysis has been done by users over the years, including:

* A histogram of price movements from [JellyNeo](https://www.jellyneo.net/?go=neopian_stock_market).
* A [neostocks.info](https://neostocks.info/) site that lets you check historical stock prices
* Corresponding analysis of [neostocks data](https://www.reddit.com/r/neopets/comments/af8p38/comment/edwe8lo/) by u/not-the-artist on Reddit.

This data all suggests the conventional wisdom of selling at 60 NP/share is correct, since price movement
is dependent on current price, and the 61-100 NP range is where average price movement changes from net
0 to slightly negative. That threshold is the point where you start losing money due to missing out on
bank interest.

The cause of this was eventually revealed by u/neo\_truths's leak of the Stock
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
confirming this leak is consistent with what was seen before. The TL;DR for why 60 NP is the magic number comes from
these two lines.

> If current price >= 10 and current price / opening price > 1.15 [subtract] max move / 4 rounded down  
> If current price >= 10 and current price / opening price > 1.3 [subtract] max move / 4 rounded down

These are the only sections of the pricing algorithm that are negative on average.
Thanks to rounding, these conditions only fire when `max move` is at least 4, and if we look above, this
only starts happening in the 61-100 NP range.

Using a 60 NP sell threshold will lead to an average holding time of 399 days. When bank interest is accounted for,
1,000 shares of 15 NP stock is worth around 29,550k NP. (It is lower than 60k NP because you miss on 399 days of bank
interest - full math is done [here](https://www.reddit.com/r/neopets/comments/y8bqig/leaked_code_determining_best_stock_selling_price/) for the curious).
This gives a profit of **14,550 NP/day**, although you will have to wait over a year per buy to convert it back to cash-on-hand.

Look at it this way - you're making your money work for you. Also there's a free avatar for getting to 1 million NP
in the stock market, which you'll easily hit if you wait until 60 NP to sell. I've got about 6 million NP tied up in
the market right now.

![Stock Market avatar GIF](/public/np-guide/stockavatar.gif)
{: .centered }

# Coconut Shy

This is one of many gambling minigames themed around ones you'd see in amusement parks. Like amusement parks, most
of the games are scams. Coconut Shy is one of the few exceptions.

You can throw 20 balls per day for 100 NP each, earning one of five outcomes.

* A miss (0 NP)
* A small hit (50 NP)
* A strong hit that doesn't knock over a coconut (300 NP)
* Knock over a coconut (10,000 NP + a random Evil Coconut)
* The coconut explodes (Jackpot! 500,000 NP)

The two outcomes worth money are the last two. The jackpot is obviously good, but the Evil Coconuts are actually
worth *more*. Every Evil Coconut is a stamp, and some Neopets users love collecting stamps. Right now, a given Evil
Coconut sells for between 750,000 NP and 1,000,000 NP.

Coconut Shy odds were leaked by u/a\_neopian\_with\_info in this [Reddit post](https://www.reddit.com/r/neopets/comments/wc4nsi/deserted_fairground_games_odds/).
Let's assume you use the Halloween site theme, which slightly improves your odds. The payout table is

<table style="margin-left:auto; margin-right:auto;">
  <thead>
    <tr>
      <th>Payout</th>
      <th>Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0 NP</td>
      <td>20%</td>
    </tr>
    <tr>
      <td>50 NP</td>
      <td>65%</td>
    </tr>
    <tr>
      <td>300 NP</td>
      <td>14.9%</td>
    </tr>
    <tr>
      <td>10,000 NP + Evil Cocunut</td>
      <td>0.99%</td>
    </tr>
    <tr>
      <td>500,000 NP</td>
      <td>0.01%</td>
    </tr>
  </tbody>
</table>

If we value evil coconuts at 750k NP, this is an expected payout of 834.6 NP per throw. Each throw costs 100 NP, so it's
734.6 NP profit per throw, and doing 20 throws gives **14,692 NP/day**.
This has pretty high variance. On average, you'll only win a worthwhile prize every 50 days.

If you decide to go Coconut throwing, you'll need to use the direct link from
[JellyNeo](https://www.jellyneo.net/?go=coconut_shy). The original game used Flash, and it was never converted
after the death of Flash, but you can still directly hit the backend URL that the Flash game would have
hit.

I am honestly surprised the Evil Coconuts are still so expensive. My guess is that most users don't know
Coconut Shy is net profitable, or the ones that do can't be bothered to do it.

# Faerie Caverns

Spoiler alert: Faerie Caverns are just a more extreme version of Coconut Shy.

Each day, you can pay 400 NP for the right to enter the caverns.
You'll face
three "left or right?" choices in the cave, with a 50% chance of either being right.
If you guess right all three times, you win a prize!

![A treasure chest in the cave](/public/np-guide/faerie_cave_success.gif)
{: .centered }

If you don't, you get nothing and have to try again tomorrow.

People do this daily because of the Faerie Caverns stamp, which is only available from this daily and sells for
around 50 million NP. However, your odds of winning it are *very* slim. You have a 1 in 8 chance of winning
treasure, and according to a u/neo\_truths [leak](https://www.reddit.com/r/neopets/comments/xwyrf0/faerie_caverns_grave_danger/),
the payouts for doing so are as follows.

<table style="margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th>Payout</th>
      <th>Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>500 NP to 2,500 NP</td>
      <td>89.9%</td>
    </tr>
    <tr>
      <td>5,000 NP</td>
      <td>4.9%</td>
    </tr>
    <tr>
      <td>10,000 NP</td>
      <td>5.1%</td>
    </tr>
    <tr>
      <td>25,000 NP + item prize</td>
      <td>0.1%</td>
    </tr>
  </tbody>
</table>

Of the item prizes, you have a 10% chance of getting a Faerie Paint Brush, and a 90% chance of winning one of Beautiful Glowing Wings,
Patamoose, Faerie Caverns Background, or Faerie Caverns Stamp. You can see in the odds that Faerie Paint Brush is
considered the best prize, so it's funny that every other prize is worth more.

<table style="margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th>Prize</th>
      <th>Estimated Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Faerie Paint Brush</td>
      <td>1,200,000 NP</td>
    </tr>
    <tr>
      <td>Beautiful Glowing Wings</td>
      <td>2,000,000 NP</td>
    </tr>
    <tr>
      <td>Patamoose</td>
      <td>3,000,000 NP</td>
    </tr>
    <tr>
      <td>Faerie Caverns Background</td>
      <td>2,000,000 NP</td>
    </tr>
    <tr>
      <td>Faerie Caverns Stamp</td>
      <td>50,000,000 NP</td>
    </tr>
  </tbody>
</table>

If you do the expected value math, then doing Faerie Caverns is net profitable. The expected earnings work
out to 1,772 NP/day. After accounting for the 400 NP cost, the Faerie Caverns are worth **1,372 NP/day**.

This really isn't that much, it's the same as playing some Flash games but with more gambling involved.
The positive expected value is entirely dependent on winning an item prize, which is a 1 in 1000 chance
after passing a 1 in 8 chance of reaching the treasure. Neopets is about 8700 days old.
You could have played Faerie Caverns every day for Neopets's *entire existence*, and it would not be surprising
if you never won an item prize.

For that reason, I don't do the Faerie Caverns daily.
Still, it is technically worth it if you have higher risk tolerance. 400 NP a day is pretty cheap.

# Battleground Boons

The Tyrannian Battleground is an ongoing site-wide event. Every 2 weeks, team signups are open for 1 week,
then you fight the 2nd week.
If you fought at least 10 battles, and your team wins, everyone on your team can choose a boon that lasts
during the next cycle's signup period (lasts for 1 week).

![Tyrannian Battleground](/public/np-guide/battleground.jpg)
{: .centered }

Some of these boons are important modifiers to previous money-earning methods.

* The Bank Bribery boon increase bank interest by 3%.
* The Cartogriphication boon tells you which direction to go in the Faerie Caverns, making your odds of
treasure 100% instead of 12.5%.
* The Cheaper by the Dozen boon lets you buy stocks at 10 NP instead of 15 NP.

In general, these boons are nice but I don't think they're worth going for. We can math them out as follows.

* Ignoring compound interest effects, Bank Bribery is worth (3% / 365) * (net worth) per day.
* For Cartogriphication, your expected payout gets multiplied by 8. This makes the Faerie Caverns worth
14,174 NP/day. Subtracting the default 1,772 NP/day value, we get an increase of 12,402 NP/day.
* The Cheaper by the Dozen boon will save 5,000 NP/day when buying stock.

We see that Cartogriphication is the best boon if you are risky, Cheaper by the Dozen
is the best boon if you aren't, and Bank Bribery is the best boon if you are rich. For the last one,
you'll need to have over
60.8 million for an interest increase larger than Cheaper by the Dozen, or 150.9 million to see an interest
increase larger than Cartogriphication's value.

At best, you'll only have a battleground boon every other week, and it's not even guaranteed
you win a boon. The winning team in the battleground is the team with highest *average* contribution, not highest
total contribution. Very often, the team with the best boons has the most freeloaders that do the bare
minimum and hope to get carried to a win. Every freeloader makes it harder to win. At this point I've mostly
stopped trying to go for boons.

There is one very narrow use case where I'd say the Battleground boons are worth it. The Reddit user
u/throwawayneopoints did a [detailed analysis](https://www.reddit.com/r/neopets/comments/lah877/toil_and_trouble_testing_out_the_orders_double/)
of the Double Bubble boon. This boon will randomly let you get a 2nd use out of a single use consumable potion.
People assumed this only applied to healing potions, which would be worthless, but that analysis showed it also applies to stat-boosting
potions and morphing potions. The refill rate is 25%, and stat boosters can be pretty expensive, so
it's pretty easy to make Double Bubble worth it. (For example, if you use 10 Bubbling Funguses for
pet training, Double Bubble will save you around 340,000 NP on average.)


# The Neopian Lottery

Okay, no you should not do this one, but it's funny so I'll give it a quick shoutout.

The Neopian lottery is a very classic lottery where you buy tickets to contribute to a common
jackpot paid to the winners. You pick six numbers between 1 to 30, then hope. What makes
the Neopian lottery special is that it **always** pays out, splitting the jackpot evenly
among winners in the case of a tie in number of matching numbers.

The jackpot has a 5k starting pot, so, *very technically*, this is a positive expected value
lottery. A lottery these days will have around 4000-5000 tickets sold, so your expected value
is like, 1 NP/ticket, which is really not worth your time. But I think it is just a perfect
symbol of Neopets dailies. It's a random slot machine, that is slightly rigged in your favor.

Amusingly, the JellyNeo guide features this joke.

![An image that says "Me, I never play the lotto. Have you taken a statistics class?"](/public/np-guide/lottery.png)
{: .centered }

Normally this would be good advice, but in this *specific instance*, if you crunch the numbers,
the statistics say the lotto is worth it. Have *you* taken a statistics class?

# If You Do Everything...

<table style="margin-left: auto; margin-right: auto;">
<tr><td>Daily Quests</td><td>46,400 NP/day</td></tr>
<tr><td>Food Club (assuming 15 year old account)</td><td>88,000 NP/day</td></tr>
<tr><td>Trudy's Surprise</td><td>17,915 NP/day</td></tr>
<tr><td>Battledome (Dome of the Deep)</td><td>69,046 NP/day</td></tr>
<tr><td>Wishing Well</td><td>7,925 NP/day</td></tr>
<tr><td>Stock Market</td><td>14,550 NP/day</td></tr>
<tr><td>Coconut Shy</td><td>14,692 NP/day</td></tr>
<tr><td>Faerie Caverns</td><td>1,372 NP/day</td></tr>
<tr><td><strong>Total</strong></td><td><strong>259,900 NP/day</strong></td></tr>
</table>

In total, we are looking at **7.797 million NP/month** if you commit to doing everything.
That's a good deal better than just playing Flash games.

Given the amount of time I've already spent researching NP making methods, I
believe I've covered everything important, but if you think I missed something, feel free to
comment. I'm hoping this post was a helpful resource for your Neopets needs. Or your needs
to...see someone do a lot of research into things that don't matter? I've watched
[Unraveled](https://www.youtube.com/playlist?list=PLaDrN74SfdT7Ueqtwn_bXo1MuSWT0ji2w), I
understand the appeal. Whichever need it was, I wish you luck on your wealth
accumulating journey.
