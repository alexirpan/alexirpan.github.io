---
layout: post
title:  "Mining on AWS: A small update"
date:   2013-11-27 00:05:00
---
*This is a post from the old blog, which I have not edited in any way.
Your results may vary - the conclusions here came from prices circa 2013.*

In light of the recent massive jump in Litecoin prices, I'd like to share some amusing facts.


Thanks to Facebook friends, it turns out that the g2 instances are more efficient at mining Litecoins. Running both cudaminer and 4-threaded cpuminer gives a total of around 170 kH/s, which is around half the hashing power of the cg1 instance for a quarter the cost. Additionally, spot instance prices for g2 are currently very stable at $0.075/hr, and are available in both N.Virginia and Oregon, instead of just N.Virginia.


Given this more efficient mining, and the current Litecoin price of roughly $20/LTC, and assuming a 1% pool fee, the estimated AWS -> LTC exchange rate is


**$0.815 in AWS costs <-> $1 in LTC**
{: style="text-align: center;"}



That's right, mining on AWS is currently profitable!


Some caveats:

1. The price of LTC is very volatile. That it doubled in price in a single day should be proof of that. There is no guarantee it will stay profitable for very long. Litecoin prices could crash the next day and it wouldn't even be that surprising.


2. You are at the mercy of how lucky your mining pool is at getting a block. The pool I'm using has averaged around 110-120% of expected time per block, which brings me to almost dead even. Additionally, the high prices are bringing in more miners, so the difficulty is going to rise, which will also bring expected profit down.


3. The fees for exchanging LTC to USD are 2% at BTC-e, the most popular Litecoin exchange. Overall this doesn't mean much, but if you need to continually convert LTC to USD to feed back into AWS, it's 2% less money going through the loop.


4. For g2 instances, you are limited to 10 spot instances per region, giving a maximum of 20 instances. So unfortunately, you can't abuse EC2's ridiculous scalability, because Litecoin mining is only profitable at the spot instance price. Assuming you max out on instances, the mining calculator gives 2.28 LTC/day, which works out to expected $10/day in profit.


5. If more people start asking for spot instances, the price will rise and profitability will go away. Given the current situation, this might happen very soon.


Personally, I'm planning to run as many instances as I can manage to get. No matter how fleeting this might be, it's hilarious that AWS mining is currently profitable, and I intend to abuse the situation while it lasts.
