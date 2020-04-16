---
layout: post
title:  "The Argument for Contact Tracing"
date:   2020-04-14 22:05:00 -0700
---

A few days ago, Apple and Google announced a partnership to develop an iOS and
Android contact tracing app. I believed that if it went properly, it was one
of the biggest signs of optimism for both ending
stay-at-home orders and maintaining control over COVID-19. However, I also quickly
realized it would be a hard sell to get people to opt-in. Many people are wary
about governments extending their authority and power during the crisis, like
what happened with the Patriot Act.

This post covers what contact tracing is, why I believe it's critical to handling
COVID-19, and how it can be implemented with minimal privacy loss that is
clearly worth giving up for public health.

Before I get into things, I want to emphasize that many of the technical problems
are essentially *solved*. The difficulty is entirely about convincing people
to opt-in, once the app is released.

As a disclaimer, I currently work at Google. I'm speaking in a personal
capacity, and have deliberately avoided looking at anything besides public
press releases.

https://www.apple.com/covid19/contacttracing

https://blog.google/…/apple-and-google-partner-covid-19-con…


What Is Contact Tracing?
-------------------------------------------------------------------------------

Contact tracing is, very broadly, tracing who infected people have been in
contact with. This is something that hospitals already do when a patient gets
a positive test for COVID-19.

The aim of contact tracing is to warn people who may be infected and asymptomatic
to stay home, to cut lines of disease transmission.

Much of this is done by hand, and would continue to be done by hand, even if
contact tracing apps become widespread. Contact tracing apps are meant to help
existing efforts, not replace them.


Why Is Contact Tracing So Necessary?
--------------------------------------------------------------------------------

Stay-at-home orders are working. Curves for states that issued stay-at-home orders
earlier are flatter, and the number of new cases per day is slowing down.

This is all great news, but the stay-at-home orders have also caused tons of
economic damage. Now, to be clear, the economic damage without stay-at-home
orders would likely have been worse. Corporation leaders may have been pushing
to ease stay-at-home orders sooner, but if you actually ask economists,
(FIND LINK) 100% of them agreed that it was better for the economy to keep
non-essential businesses closed until the public health threat went away.
(The difference here is that corporate leaders care about their company, while
economists care about the *economy*. Most of the economy is workers, not CEOs.)

The aim, then, is to reach the point where businesses can reopen while keeping
the disease under control (link Hammer and Dance?)
As summarized by this Vox article, there are about 4 endgames for this.

I see approximately 3 endgames for that. They are summarized by this Vox article: https://www.vox.com/…/coronavirus-plans-social-distancing-e…

1. Social distancing continues until cases literally go to 0, and the disease
is eradicated.
2. Social distancing continues until a vaccine is developed, widely distributed,
and enough of the population gets it to give herd immunity.
3. Social distancing continues until cases drop to a small number, and
massive testing infrastructure is in place. Think millions of tests per day. If you have enough tests to literally test the entire country, repeatedly,
then you need less contact tracing, because you have enough ground truth (COVID-19 tests) to figure out who is and isn't infected.
4. Social distancing continues until cases go to a low number, and widespread contact tracing, plus a large, less massive number of tests are in place.

Of these scenarios. 1) isn't happening, 2) will take the longest,
3) will be medium length, and 4) is the fastest.

Eradication is incredibly unlikely, since the disease broke containment.
The vaccine development timeline is long, and it will be about a year before
it is declared safe. For testing, scaling up production and logistics is
underway right now, but reaching the scale of millions of tests per day sounds
hard enough that I don't think the US can do it.

That's where contact tracing comes in. Technical solutions can exploit what
made software take over the world: a team of programmers can make an app that
easily distributes to millions of people in very little time. With good contact
tracing, we will need fewer tests to track the spread of COVID-19.

Vaccine development, test production, and contact tracing apps will all be done in parallel, but I expect contact tracing to finish first,
and to be the best hope of letting people get back to work the fastest.


What About Privacy?
-------------------------------------------------------------------------------

Ever since the Patriot Act, people have been wary of governments using crises
as an excuse to extend their powers, and ever sinze 2016, people have been
wary of trusting Big Tech. So it's understandable that a collaboration between
Apple, Google, and governmental health authorities is triggering alarm bells.

However, if you read the proposal for the contact tracing app, you find that

1. The privacy loss is fairly minimal.
2. The attacks on privacy you can execute are potentially annoying, but not catastrophic.

And, when you contrast this with people *literally* dying, the privacy loss is
negligible in comparison.

Let's start with a privacy loss that *isn't* okay, to clarify the line.
In South Korea, the government published personal information for patients
confirmed COVID-19 positive.
This included where they traveled, their gender, and their rough age. All
of this infromation is broadcasted to everyone in the area.

's approach. I need to track down the source for this, but in South Korea, the government published a full list of details for all patients confirmed as COVID-19 positive. (https://www.nature.com/articles/d41586-020-00740-y)

Exposing this level of personal detail is just entirely unnecessary. Yes, it
slows down infection, but there are ways to report this information *without*
publicizing people's activities to this level of detail. There is no change in
health outcome between knowing you were near an infected person, and knowing
you were near an infected person of a certain age and gender. In either case,
you're self-quarantining. This is privacy loss for no gain.

How does the Apple and Google collaboration differ? Here is the diagram from Google's announcement.

DIAGRAM

This is similar to the DP-3T protocol, which is briefly explained by this
comic

COMIC

1. Each phone continually generates a random string of gibberish, broadcasting it on Bluetooth to all nearby devices. This changes every 5-15 minutes.
2. Each device records all random message it has heard, from other nearby devices that have the app installed.
3. Whenever someone tests positive, they can elect to upload all their messages to a database. This upload would require both a public health official and the infected's consent to sign off on it.
4. Apple's and Google's servers will store a giant list of all messages sent by a COVID-19 patient. They will be stored for 14 days.
5. Periodically, every device will download the entire list of messages that COVID-19 cases have sent. It will then, on-device, compare that list to a locally saved list of messages that device has received from nearby phones.
6. If there is enough overlap, the user gets a message saying they were recently in contact with a COVID-19 case.

Something like this is already implemented in the existing NOVID contact
tracing app, which also uses Bluetooth and a self-reporting function to securely
trace contacts.

What the proposed protocol does is attempt to minimize the privacy loss, while maintaining enough information to make contact tracing possible.
Crucially, as stated, Apple's and Google's servers do not directly store any interactions between phones. It stores only the messages that COVID-19 cases have sent out - but it does not store the receivers of those messages, assuming it's implemented according to spec.

That last part is a sticking point.


What If Sketchy Stuff Happens?
-------------------------------------------------------------------------------

First, the simpler, less technical answer. So far, Apple and Google have
publicized and announced their protocol ahead of time. This is standard practice
if you want to do security right, because it lets external people audit the
security, including people who aren't fans of either company.

In short, they are so far doing things properly, and acting in a way that would
make it much harder for them to sneak backdoors or privacy breaks into their
protocol.

Additionally, for the protocol itself, remember that it's basically the DP-3T
protocol, a protocl that was designed entirely by academic security
researchers, not big tech companies. I have not had the time to verify the details,
but the high level spec sounds essentially identical.

If you are on board with all of that, but do have the technical expertise to evaluate crypto, then I'd encourage you to compare it with the DP-3T protocol (https://github.com/DP-3T/documents), a contact tracing protocol designed entirely by academics. I have not had the time to check the details, but believe the public spec is basically the DP-3T protocol. I am a crypto passerby, not a crypto nut, but to my eyes I don't see any way to break the protocol. The only reason I say the privacy loss is minimal, instead of privacy loss 0, is because it's very hard to claim zero privacy loss. If it breaks, it should break minimally.

Things I have seen:

a. This is described as an opt-in app, but governments will step in and tell people that they can't leave the house unless they opt-in, making it essentially required.
b. Do we really want big tech companies building a system like this?

For these two, my feelings are

a. Good
b. Yes

At this point, I believe that yes, it would be good for an app like this to be widespread. I believe that big tech companies have enough sway to avoid compromising security of the protocol, even under governmental pressure. Apple's reputation is built in part on privacy, both companies have lots of security expertise, and, look, if you were worried about privacy, both companies have plenty of easier avenues to get personal information.

For the protocol to work, as many users as possible have to contribute to the same database of "messages sent by COVID-19 patients". Efforts like NOVID are a good step, and will likely adapt to use the APIs Apple and Google promise to release, but their reach will be small. This is a case where you *want* big tech to have lots of reach, to get people to use the service. (Similarly, you may have ill will towards Big Pharma, but Big Pharma is partnering with the CDC for COVID-19 test production. I'm not saying you should forever suspend your principles, if you are philosophically against accumulation of power into large corporations, but at this time it's correct to temporarily suspend your principles.)

As for potential attack vectors, I am mostly following the impressions of Moxie Marlinspike, the creator of Signal, because he has thought a lot more about how to break things than I have.

https://twitter.com/moxie/status/1248707315626201088

His conclusions are that tracking companies would download the app onto their own devices. They could place them in hotspots of human activity, and could use them to get COVID-19 within local areas, and potentially makes it linkable. (I admit that I don't understand how it becomes linkable if only the messages are shared. I don't think the MAC addresses are shared?)

He also concludes that it's likely (but not guaranteed yet) that location data will be incorporated in some way. If the app works as described, each device needs to download 16 bytes of data times number of devices infected. If the app is widespread, this could become 100s of MBs of downloads each day.

He says this is untenable. I'm not sure that's true. Regardless, if we assume that's true, then to limit download size, you'd want each phone to only download messages from a targeted set of devices that includes all nearby devices...which probably reduces to location data in some way. Here I disagree and think the solution will look more like "the phone only downloads data when you are on Wi-Fi, and it is plugged in".

For attack vectors, he says that it's possible for contact tracing to get used as a DDOS attack, or a prank, if users either upload massive amounts of keys (forcing gigabytes of downloads to all users), or users declare they are COVID-19 positive when they aren't, just to scare people.

I think the risk of both of these should be small, because in theory all uploads require the sign-off of a public health authority. This should already force centralized access for database uploads and reduce how much people can attack the protocol.

4. Jesus This is Long Would You Wrap This Up Already

Okay. Here are the takeaways.

If you were not on-board with contact tracing as a method, I think it is the leading candidate for fastest way to bring things closer to normal.

If you were on board with contact tracing, but not on board with it being done by Apple or Google, then who do you want? The combination of network effects and political leverage they have makes them most able to rapidly spread the word for contact tracing. The only larger actor is the government, and if you don't trust Apple or Google, then you shouldn't trust the government either.

If you were on board with contact tracing, and accept that Apple and Google are in good position to make it a reality, are unsure about whether this will become a long-lasting surveillance tool, and don't have the technical expertise to evaluate it yourself, then so far, it appears that both companies are doing things properly. They have a public spec of what they say they will implement. People are free to audit it and comment on it.

If you are on board with all of that, but do have the technical expertise to evaluate crypto, then I'd encourage you to compare it with the DP-3T protocol (https://github.com/DP-3T/documents), a contact tracing protocol designed entirely by academics. I have not had the time to check the details, but believe the public spec is basically the DP-3T protocol. I am a crypto passerby, not a crypto nut, but to my eyes I don't see any way to break the protocol. The only reason I say the privacy loss is minimal, instead of privacy loss 0, is because it's very hard to claim zero privacy loss. If it breaks, it should break minimally.
