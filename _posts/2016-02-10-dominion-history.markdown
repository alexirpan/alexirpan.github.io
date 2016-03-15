---
layout: post
title:  "The Surprisingly Dramatic History of Online Dominion"
date:   2016-02-08 10:00:00 -0800
---

MAKE UP AN INTRO HERE

As someone who's played Dominion competitively on and off for the last
five years, it's hard for me to detach my impression of events from the facts.
So, I'm not going to. I'm going to play the opinionated historian, not
the interested outsider and not the invested fanboy.

It's a long story. To do it right, we need to head back to the very beginning.


    TIMELINE:
    Dominion's original release and reception
    Original online implementation on BSW
    BGGDL
    The rise of Isotropic
        Talk about Council Room too!
        And the fan card contest getting onto the site during April Fool's
    Announcement of an official client by Goko
    Closed Beta
        With security concerns
    Disastrous Launch and bring back into closed beta
    Long span before Isotropic goes down
    Rise of Goko Salvager
    Transition to Making Fun
    Long stall before new version
    Repeated disappointment
    Making More Fun (dll hacking oh my)
    The next new implementation

In 2008, Donald X. Vaccarino (known as DXV or Donald X in the community)
published Dominion. It quickly shot to the top 10 board games on BoardGameGeek.
It's fallen since then, but much like Setters of Catan it's a historically
important board game that sparked many changes.

Now, I'm not going to explain the rules in depth. This post is about
the Dominion community, not the game. However, I do need to briefly explain how
the game works.

Dominion is called a deckbuilding game. In fact, it's usually credited as the
first deckbuilder, inspiring games like Ascension, Puzzle Strike, Star Realms,
and, uh, Deck Builder.

IMAGE

The core idea is that everyone starts with the same deck of cards. On each turn,
people play cards, generate resources, and buy new cards for their deck. As

In Dominion, everyone starts with the same deck of cards. Over the course of the
game, people play cards from their hand to generate money. They use that money
to buy more cards from the supply, making their deck better. (EXPLAIN SUPPLY)

What makes Dominion so replayable is that each set comes with around 25
different Action cards. Each game only uses 10, which makes every game a different
experience. With expansions, the depth becomes ridiculous. But we'll get to
how ridiculous competitive Dominion gets later.

Anyways, Dominion released, and it was a huge hit. It soon grew its own pocket
of fandom in the BoardGameGeek forums. Nascent strategy discussions came and went.
Is Chapel too strong? Does it pass the Silver Test? Over time, people started
coming up with special terms. Big Money, the opening, greening, terminals, Village
Idiot. Over time, strategy discussion started crystallizing around the important
concepts. Engines, rushes, cycling, Cursing. There's a cornucopia of terms (and
the expansion *Cornucopia* brought its own set as well.)

All of this discussion couldn't exist without Dominion Online. In the beginning,
there was Dominion on BrettspielWhet (BSW). I wasn't around for BSW, but by
my understanding, it was clunky and heavyweight. Nevertheless, it worked and it was
free. TALK ABOUT EXPANSIONS HERE.

EMPHASIzE POWER OF ONLINE PLAY?

BSW picture

Sometime around 2010, one user, DougZ, posted an innocent reply to a thread asking
when BSW would have the newest expansion.

> I've implemented a server where you can play Dominion against other players online. There's no AI, and the interface is pretty bare-bones, but it does include all the published cards including Prosperity (except for a couple of the promo cards).
>
> You can find instructions and a link to the server at http://dominion.isotropic.org/faq.
>
> Posted Sun Aug 8, 2010 10:57 pm

[Source](https://boardgamegeek.com/article/5373751#5373751)
{: .centered }

It was just another post in just another thread. But in time, Isotropic would
usher in a golden age.

\*\*\*
{: .centered }

There's a scene from CHECK THE MOVIE. "You weren't there, man! You had to be there!"
Isotropic was a similar - if you weren't there for Iso, it can be hard to see why
the community holds it in such high regard.

Isotropic was not professional by any stretch of the information. It was the
side project of one Google engineer, most famous for his presentation
["Chicken chicken chicken: chicken chicken"](https://www.youtube.com/watch?v=yL_-1d9OSdk).
It quite literally ran out of DougZ's basement - an AMA about Isotropic revealed
that "server maintenance" was code for "turn the machine off and on again."

At a first glance, Isotropic doesn't look like anything special. It didn't have
the graphics of BSW. It didn't even have the official card art.

ADD A PICTURE OF ISO HERE.

Still, it was the best platform Online Dominion has ever had. It may have been
plain, but it did the key things right.

* The gameplay engine was rock solid. Rules were always implemented correctly.
Matching was reliable, the server almost never dropped games, and players
could reconnect to games if they lost their internet connection. At worst,
there would be some brief lag.
* The interface was designed well. It never felt like the client got in the way
of what you wanted to do. When it comes to controls, the goal of any game client
is to feel like an extension of your thoughts.
* The minimalist graphics made it runnable on basically every computer. I played
Isotropic on a Windows Vista laptop that had 5 minutes of battery life, and it
worked fine. All you needed was an internet connection - in principle you could
play on your phone and it would work.
* If you needed to do something for a bit, the game displayed a text log of the
past few turns, which let you catch up on what happened while you looked away.

Those were all the main essentials, but Isotropic had a few features that
made it the focal point of the fan community

* There was a competitive ladder based on TrueSkill (LINK), a variant of
Elo that generalizes to multiplayer games. The FAQ linked directly to
Microsoft's documentation, and described exactly how new players got ranked.
The leaderboard was exceptionally transparent - you always knew exactly
how good the system thought you were.
* Expansions were released promptly. DougZ was a friend of Donald X's (CHECK),
and a private version of Isotropic was actually used for playtesting. That meant
expansions were available for free on Isotropic the day they were in stores.
* Although it wasn't there from the start, automatch quickly let players
get matched with people of their skill level. Players could also directly
challenge players in the lobby, since every player's skill level was displayed
next to them.
* At the end of each game, you were given a link to the text log for each game.
This made it easy to share games you thought were cool, ask for help, review
what you did wrong, and so on.

Essentially, Isotropic implemented everything the competitive community
wanted, and a few things it didn't know it wanted. People quickly evolved
the metagame, using Isotropic as their platform to test new ideas.

Around tNear this time, one player called

Around this time, theory and rrenaud, started a blog for
Dominion. They called it Dominion Strategy, and posted their first
article in [November 2010](http://dominionstrategy.com/2010/11/12/combo-of-the-day-1-quarrytalisman/).
(CHECK IF THIS WAS FIRST INSTANCE OF IT)

As theory posted more content, Dominion Strategy became the hub of
competitive Dominion. Theory posted startegy articles, and people debated them
in the comments section. Analysis slowly shifted from BGG to the new site.

Meanwhile, rrenaud was working on a different problem: Dominion analytics.
Every day, Isotropic uploaded an archive of all games played that day. It was
ripe for analysis, but needed text log parsing, some daily scripts to
download the logs each day, a database to store logs for each player, and so
on. With a few others (CREDIT), he built [CouncilRoom](http://www.councilroom.com).
With CouncilRoom, people could cite statistics for their arguments, pushing
strategy discussion in a more mechanical direction.

Soon, DominionStrategy was *the* place to go for Dominion. Theory's articles
on the best cards per cost point were huge debating grounds. In (CHECK) 2011,
he started the DominionStrategy Forum, commonly abbreviated f.DS, and that
was where things really kicked off.

