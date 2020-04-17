---
layout: post
title:  "The Argument for Contact Tracing"
date:   2020-04-14 22:05:00 -0700
---

A few days ago, Apple and Google announced a partnership to develop an opt-in
iOS and
Android contact tracing app. Apple's announcement is [here](https://www.apple.com/covid19/contacttracing),
and Google's announcement is [here](https://blog.google/inside-google/company-announcements/apple-and-google-partner-covid-19-contact-tracing-technology).

I felt it was one
of the biggest signs of optimism for both ending stay-at-home orders
and maintaining control over COVID-19, assuming that people opt into it.

I also quickly realized that a bunch of people weren't going to
opt into it. Here's my attempt to fix that.

This post covers what contact tracing is, why I believe it's critical to handling
COVID-19, and how the proposed app implements it with minimal privacy loss,
ensuring that neither people, nor corporations, nor governments learn
personal information they don't need to know.

As a disclaimer, I do currently work at Google, but I have no connection to
the people working on this, I'm speaking in a personal capacity,
and I've deliberately avoided looking
at anything besides the public press releases.


What Is Contact Tracing?
-------------------------------------------------------------------------------

Contact tracing is the way we trace who infected people have been in
contact with. This is something that hospitals already do when a patient gets
a positive test for COVID-19.
The aim of contact tracing is to warn people who may be infected and asymptomatic
to stay home. This cuts lines of disease transmission, slowing down the spread
of the disease.

Much of this is done by hand, and would continue to be done by hand, even if
contact tracing apps become widespread. Contact tracing apps are meant to help
existing efforts, not replace them.


Why Is Contact Tracing So Necessary?
--------------------------------------------------------------------------------

Stay-at-home orders are working. Curves for states that issued stay-at-home orders
earlier are flatter. This is all great news.

However, the stay-at-home orders have also caused tons of
economic damage. Now, to be clear, the economic damage without stay-at-home
orders would have been worse. Corporate leaders and Republicans may have talked
about lifting stay-at-home orders,
but as relayed by [Justin Wolfers,
UMich Economics professor](https://twitter.com/JustinWolfers/status/1244294419492343808),
a survey of over 40 leading economists found 0% of them agreed that lifting
severe lockdowns early would decrease total economic damage.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Survey of leading economists:<br><br>&quot;Abandoning severe lockdowns at a time when the likelihood of a resurgence in infections remains high will lead to greater total economic damage than sustaining the lockdowns to eliminate the resurgence risk.&quot;<br><br>0% disagree.<a href="https://t.co/6NNAaLlSjq">https://t.co/6NNAaLlSjq</a> <a href="https://t.co/7kcnVVPw2N">pic.twitter.com/7kcnVVPw2N</a></p>&mdash; Justin Wolfers (@JustinWolfers) <a href="https://twitter.com/JustinWolfers/status/1244294419492343808?ref_src=twsrc%5Etfw">March 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Understand the incentives: CEO&#39;s and bankers are calling for workers to be recalled. Economists—whose models also account for what&#39;s in the workers&#39; best interests—disagree. Epidemiologists—who understand how pandemics spread—also disagree.</p>&mdash; Justin Wolfers (@JustinWolfers) <a href="https://twitter.com/JustinWolfers/status/1244298426759680004?ref_src=twsrc%5Etfw">March 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

So, lockdowns are going to continue until there's low risk of the disease
resurging.
As summarized by this [Vox article](https://www.vox.com/2020/4/10/21215494/coronavirus-plans-social-distancing-economy-recession-depression-unemployment),
there are about 4 endgames for this.

1. Social distancing continues until cases literally go to 0, and the disease
is eradicated.
2. Social distancing continues until a vaccine is developed, widely distributed,
and enough of the population gets it to give herd immunity.
3. Social distancing continues until cases drop to a small number, and
massive testing infrastructure is in place. Think millions of tests per day,
enough to test literally the entire country, repeatedly, to track the
course of the disease.
4. Social distancing continues until cases go to a low number, and widespread contact tracing, plus a large, less massive number of tests are in place.

Eradication is incredibly unlikely, since the disease broke containment.
Vaccines aren't going to be widely available for about a year, because safety
studies will need a year to finish.
For testing, scaling up production and logistics is
underway right now, but reaching millions of tests per day sounds
hard enough that I don't think the US can do it.

That's where contact tracing comes in. With good contact tracing, you need
fewer tests to get a good picture of where the disease is. Additionally,
digital
solutions can exploit what made software take over the world: once it's ready,
an app can be easily distributed to millions of people in very little time.

Vaccine development, test production, and contact tracing apps will all be done in parallel,
but given the United States already has testing shortfalls, I expect contact
tracing to finish first, and to be the
best hope for letting people get back to work the fastest.


What About Privacy?
-------------------------------------------------------------------------------

Ever since the Patriot Act, people have been wary of governments using crises
as an excuse to extend their powers, and ever since 2016, people have been
wary of trusting Big Tech. So it's understandable that they're sounding alarm
bells over a collaboration between
Apple, Google, and the government.

However, if you actually read the proposal for the contact tracing app, you find that

1. The privacy loss is fairly minimal.
2. The attacks on privacy you can execute are potentially annoying, but not catastrophic.

When you contrast this with people *literally* dying, the privacy loss is
negligible in comparison.

Let's start with a privacy loss that isn't okay, to clarify the line.
In South Korea, the government published personal information for COVID-19
patients.
This included where they traveled, their gender, and their rough age. All
this information is broadcasted to everyone in the area. See this piece
from [The Atlantic](https://www.theatlantic.com/ideas/archive/2020/04/contact-tracing-could-free-america-from-its-quarantine-nightmare/609577/), or this article from [Nature](https://www.nature.com/articles/d41586-020-00740-y), for more information.

Exposing this level of personal detail is entirely unnecessary. There are ways
without
publicizing people's activities to this level of detail. There is no change in
health outcome between knowing you were near an infected person, and knowing
you were near an infected person of a certain age and gender. In either case,
you should self-quarantine. The South Korea model makes people lose privacy
for zero gain.

How does the Apple and Google collaboration differ? Here is the diagram from Google's announcement.

![Page 1 of Google diagram](/public/contact-tracing/google1.png)
{: .centered }

![Page 2 of Google diagram](/public/contact-tracing/google2.png)
{: .centered }

This is similar to the [DP-3T protocol](https://github.com/DP-3T/documents), which is briefly explained in this
comic by [Nicky Case](https://ncase.me/contact-tracing/).

<p class="centered">
    <img style="max-width:80%;" src="/public/contact-tracing/ncase.png" alt="DP-3T tracing comic">
</p>

1. Each phone continually generates random keys, that are broadcasted by Bluetooth
to all nearby devices. These keys change every 5-15 minutes.
2. Each device records the random messages it has heard from nearby devices.
3. Whenever someone tests positive, they can elect to upload all their messages to a database. This upload requires the consent of both the user and a public health official.
4. Apple's and Google's servers store a list of all messages sent by COVID-19 patients. They will be stored for 14 days, the incubation period of the virus.
5. Periodically, every device will download the entire list of messages that COVID-19 cases have sent. It will then, on-device, compare that list to a locally saved list of messages received from nearby phones.
6. If there is enough overlap, the user gets a message saying they were recently in contact with a COVID-19 case.

What makes this secure? Since each phone's message is random, and changes
frequently, the list of messages for nearby phones
doesn't indicate anything about who those messages correspond to. Since
the database is a pile of random messages, there's no way to extract further
information from the stored database, like age, gender, or street address.
That protects the privacy from both the user and the database's owner.

The protocol minimizes privacy loss, but it does still exposes some information.
Exposing some information is required for contact tracing to work. Suppose Alice only meets with
Bob in a 14 day period. She later gets a notification that someone she interacted
with tested positive for COVID-19. It's rather obvious that Alice can conclude
Bob has COVID-19. However, in this scenario, Alice would be
able to conclude this no matter how contact tracing is implemented. In the proposed
app, it leaks this required information, and no more. If Alice meets 10 people,
then gets a notification, all she learns is that one of the 10 people
she met is COVID-19 positive - which, again, is something that she could have
concluded anyways.

If implemented as stated, neither the hospital, nor Apple, nor Google should learn
who's been meeting who, and the users getting the notification shouldn't learn
who transmitted the disease to them.


What If Apple and Google Do Something Sketchy?
-------------------------------------------------------------------------------

First, the simpler, less technical answer. So far, Apple and Google have
publicized and announced their protocol ahead of time. Their press releases
include a Bluetooth specification, a cryptography specification, and the API
that both iOS and Android will support. This is standard practice
if you want to do security right, because it lets external people audit the
security. It also acts as an implicit contract - if they deviate from the spec,
the Internet will bring down a firestorm of angry messages and broken trust.
If you can count on anyone to do due diligence, it's the cryptography nerds.

In short, if this was a sneaky power grab, they're sure making it hard to
be sneaky by readily giving out so much information.

*Maybe* there's a hole in the protocol. I think that's very unlikely. Remember,
it's basically the [DP-3T protocol](https://github.com/DP-3T/documents), which was
designed entirely by academic security professors, not big tech companies.
I haven't had the time to verify they're exactly identical, but on a skim they
had the same security guarantees.

When people explain what could go wrong, they point out that although the
app is opt-in, governments could say people aren't allowed to leave lockdown
unless they opt-in, effectively making it mandatory. Do we really want
big tech companies building a system like this?

My answer is yes, absolutely, and if governments push for mandatory installs,
then that's fine too, as long as the app's security isn't compromised.

Look, you may be philosophically against large corporations accumulating power.
I get it. Corporations have screwed over a *lot* of people. However, I don't
think contact tracing gives them much more power, and
right now
the coronavirus is also screwing over a lot of people. It's correct
to temporarily suspend your principles. Not permanently, temporarily. Just until
the public health emergency is over. Contact tracing only works if it's
widespread. To make it widespread, you *want* the large reach of tech companies,
because you need as many users as possible.
(Similarly, you may hate Big Pharma, but Big
Pharma is partnering with the CDC for COVID-19 test production, and at this time
they're best equipped to produce the massive numbers of tests
needed to detect COVID-19.)

[NOVID](https://www.novid.org/#top) is an existing contact tracing app, with
similar privacy goals. It got a lot of traction in the math contest
community, because it's led by Po-Shen Loh. I thought NOVID was a great effort
that got the ball rolling, but I never expected it to have any shot of
reaching outside the math contest community. Its footprint is too small.
Meanwhile, everyone knows who Apple and Google are. It's much more likely
they'll get the adoption needed to make contact tracing effective. Both companies
also have Health divisions, meaning they should have the knowledge to
satisfy health regulations, and the connections to train public health
authorities on how to use the app. These are all fixed costs, and the central
lesson of fixed costs is that they're easier to absorb when you have a large
[war chest](https://www.cnbc.com/2020/01/28/apple-q1-2019-cash-hoard-heres-how-much-cash-apple-has-on-hand.html).

Basically, if you want contact tracing to exist, but don't want Apple or Google making it, then who do you want?
The network effects and political leverage they have makes them most able to
rapidly spread contact tracing. I'm not very optimistic about a decentralized
solution, because (spoiler for next section) that opens you up to several
other issues. If you want a centralized solution, the only larger actor is
the government, and if you don't trust Apple or Google, you shouldn't trust
the government either.

Frankly, if you were worried about privacy, both companies
have plenty of easier avenues to get personal information, and based on the
Snowden leaks, the US government knows this too.
I do think
there's some risk that governments will pressure Apple and Google to compromise
the security for surveillance reasons, but I believe big tech companies have
enough sway to avoid compromising to governmental pressure, and will choose
to do so if pushed.


What If Other Actors Do Something Sketchy on Top of Apple and Google's Platform?
-------------------------------------------------------------------------------

From a privacy standpoint, these are the most serious criticisms, and I'll defer
to [Moxie Marlinspike's first reaction](https://twitter.com/moxie/status/1248707315626201088),
because he created [Signal](https://en.wikipedia.org/wiki/Signal_(software)) and
has way more experience on how to break things.

These contact tracing apps all use Bluetooth, to enable nearby
communication. A bunch of people who wouldn't normally use Bluetooth are going
to have it on. This opens them up to attacks that use Bluetooth. For example, a tracking
company can place a Bluetooth beacon in a hotspot of human activity. One beacon
by itself only registers nearby devices, and doesn't give much, but if you place enough of these
beacons and aggregate their pings, you can start triangulating movements.
In fact, if you do a search for "Bluetooth beacon", one of the first results
is [a page from a marketing company explaining why advertisers should use
Bluetooth beacons to run location-based ad campaigns](https://www.beaconstac.com/what-is-a-bluetooth-beacon).
Meaning, these campaigns are happening already, and now those ads will work
for a bunch more people.

Furthermore, it's a pretty small leap to assume that advertisers will also
install the contact tracing app to their devices. They'll place them in a
similar way to existing Bluetooth beacons, and bam, now they also know the
rough frequency of COVID-19 contacts in a given area.

My feeling is that like before, these attacks could be executed on
any contact tracing app. For contact tracing to be widespread, it needs to be
silent, automatic, and work on existing hardware. That pretty much leaves Bluetooth,
as far as I know. Coordinated attacks on Bluetooth are possible, but they're more
expensive to execute in a privacy-first protocol. Compared to stopping the
start of another exponential growth in loss of life, I think this is acceptable.

Moxie notes that he expects location data to be incorporated at some point.
If the app works as described, each day, the device needs to download
data for every new case that day. At large scale, this could become 100s
of MBs of downloads each day. To decrease
download size, you'd want each phone to only download messages uploaded from
a limited set of devices that includes all nearby devices...which is basically
just location data, with extra steps.

I disagree that you'd need to do that. People already download MBs worth of
data for YouTube, Netflix, and updates for their existing apps. If each device
only downloads data when it's on Wi-Fi and plugged in, then it should be okay.
I'd also think that people would be highly motivated to allow those downloads
to finish - if they don't finish the download, they don't learn if they were
close to anyone with COVID-19!

If users upload massive amounts of keys, they could trigger DDOS attacks by
forcing gigabytes of downloads to all users. If users declare they are COVID-19
positive when they aren't, they could spread fake information through the contact
tracing app. However, the risk of both of these should be small, because in
theory all uploads will require the sign-off of a doctor or public health
authority. DDOS attacks and pranks are only problems in a decentralized, minimal verification
system. If hospitals have the final say, that acts as the centralized source
of trust that reduces the potential for abuse.


Summary
-------------------------------------------------------------------------------

Here are the takeaways.

Contact tracing is a key part to bringing things back to normal as fast as
is safe, which is important for restarting the economy.

Of the existing contact tracing solutions, the collaboration between Apple
and Google is currently the one I expect to get the largest adoption. They
have the leverage, they have the network effects, and they have the
brand name recognition to make it work.

For that solution, I expect that, while there will be some privacy loss,
it'll be close to the minimum amount of privacy loss required to make
widespread contact tracing work - and that privacy loss is small, compared
to what it prevents. And so far, they seem to be operating in good faith,
with a public specification of what they plan to implement, which closely matches
the academic consensus.

If this *doesn't* happen - if it doesn't get enough adoption, if people are too
scared to use it, or something else, then given the current US response,
I could see the pessimistic forecasts of the UCL report coming true: cycles
of lockdown on, lockdown off, until a vaccine is ready. And I will be
really, really, really mad if that happens, because to me, it would have
been entirely preventable.
