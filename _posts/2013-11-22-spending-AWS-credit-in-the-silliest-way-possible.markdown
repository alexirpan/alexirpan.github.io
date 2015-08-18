---
layout: post
title:  "Spending AWS Credit In the Silliest Way Possible
date:   2013-11-22 03:27:00
categories: jekyll update
---
*This is a post from the old blog, which I have not edited in any way.
Your results may vary - the conclusions here came from prices circa 2013.*


Last year, thanks to various giveaways at events, I got $450 of Amazon Web Service credits. I redeemed them on my account, and left them there.


Fast forward to now. The credits I redeemed last for a year. So, if I don't spend them by mid-February 2014, they'll disappear forever. I don't have anything I need to scale, and I'm certainly not running any data analysis that would help from having lots of EC2 credit. What I can do, however, is mine some Litecoins.


To set up Litecoin mining on Amazon EC2, I mostly followed [this link](https://bitcointalk.org/index.php?topic=169377.0), which is a post about mining with Amazon's GPU instances. It's fairly comprehensive, although somewhat outdated.


First, I downloaded the Litecoin client (off [here](https://litecoin.org/)) to get a Litecoin address, and made an account on a mining pool. I ended up using Coinhuntr, mostly because their interface looked nice, but you can pretty much choose whatever one you want.


Next, I made a Spot Instance request in the N.Virgina region. This is the only region which lets you make spot instance requests for cg1 instances, which are the ones that have 2 Nvidia Tesla M2050s for use. The spot instances are $0.346/hr, versus $2.1/hr for on demand instances, which means the mining is a lot cheaper. I used Ubuntu 12.04 for HVM as my AMI. Ubuntu 12.04 is one of the few supported distributions for Nvidia's CUDA Toolkit, which you need to mine, and GPU instances are only available for HVM.


From there, I followed the EC2 mining link above, with some minor changes.

- I needed to install the libtool package, which for some reason wasn't listed in the packages to download from the script above
- I downloaded the CUDA toolkit that corresponded to Ubuntu 12.04.
- I used cudaminer instead of cgminer. Cudaminer is designed around Nvidia's hardware, whereas cgminer is designed around OpenCL. Both work, but cudaminer gives better performance on Nvidia cards. (If you're planning on using cgminer, watch out that you need version 3.7 or lower, as cgminer stopped support GPU mining on 3.8.)

Because I'm working on spot instances, I made a quick shell script to run through all the required installations and setup, in case the instance goes down. You can look/download them at [http://pastebin.com/k9akQxzX](http://pastebin.com/k9akQxzX) and [http://pastebin.com/1DbyrWr1](http://pastebin.com/1DbyrWr1).


Update: I also downloaded cpuminer, to take advantage of the two Intel X5570s on the cg1 instance. I downloaded from here, it worked out of the box for me. I'm running cpuminer on 8 threads out of 16. Cudaminer needs a CPU as well, so to be safe I'm giving an entire processor to it.


With both cpuminer and cudaminer running, one cg1 instance performs at roughly 340 kH/s. Given the current exchange rate, and assuming spot instances stay at $0.346/hr, the final AWS credit -> LTC exchange rate is

**$3.977 in AWS credit <--> $1 worth of LTC**
{: style="text-align: center;"}


All in all, this is a surprisingly decent exchange rate. It's nowhere near profitable, but suddenly all those AWS credit codes seem a lot better.

