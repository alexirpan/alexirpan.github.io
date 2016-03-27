---
layout: post
title:  "The Surprisingly Dramatic History of Online Dominion"
date:   2016-02-08 10:00:00 -0800
---

------------------------------------------------------------------

DECIDE HOW TO HANDLE ABOVE

The story that's actually interesting here isn't the history of Dominion.
It's my impression of Dominion's history and my experiences with the game.
The history will arise naturally, but my experience won't.

ALSO, MAY STILL NEED AN INTRO

It's a long story. To do it right, we need to head back to the very beginning.


TIMELINE:
    Before my time:
        Dominion's original release and reception
        Original online implementation on BSW
        BGGDL

    My time:
        The rise of Isotropic
        Geronimoo Simulator
        Talk about Council Room too!
        And the fan card contest getting onto the site during April Fool's
        Announcement of an official client by Goko
        Closed Beta
            With security concerns
        Disastrous Launch and bring back into closed beta
        Long span before Isotropic goes down

    My semi-hiatus:

    Goko era:
        Rise of Goko Salvager
        Dominion streams over Dominion videos
        Transition to Making Fun
        Long stall before new version
        Repeated disappointment

    Present day:
        Making More Fun (dll hacking oh my)

    Future:
        The next implementation


--------------------------------------------------------------------------

My competitive Dominion career (or hobby, to be more precise) started
the summer before 11th grade. I was at a summer math program, and during
free time one of the mentors proposed we played Dominion.
He described it as "*Magic: the Gathering*, except you don't have to
buy new cards every time, which is nice when you start doing adult
things like pay rent."

Over that summer, I got hooked. I was playing at least 2 hours a day for
five weeks straight, and that much play time adds up. It was fun to
play around with cards, trying to figure out what cards I wanted and how
different cards interacted with each other. Militia was great, but it was
bad against Library, and meanwhile Ironworks was amazing with Gardens.
None of this was spelled out by the game, but it was implicit in its
design. That sense of discovery when someone figured out something new
and won was both incredible and infectious.

In the months after that summer, someone discovered a free online
client called Isotropic. I signed up for an account, and that's when
this story really starts.

--------------------------------------------------------------------------

By the time I started really getting into Dominion, the online community
had been around for a few years. Dominion came out in 2008, and I didn't
start playing until 2010.

Now, first I do want to briefly explain how the game works. I can't write
a huge post about Dominion without explaining what Dominion *is*.

Dominion is a deckbuilding game. Like other Eurogames, the goal is to end
the game with the most victory points.

The high level overview is that every player starts with an identical deck.
Each turn, players play cards to generate money, and use that money
to buy better cards. Players can then use their new cards to generate more
money, which lets them buy even better cards, and so on.

Cards in Dominion are split into three broad types.

* Victory cards give victory points, but do nothing during the game,
which forces players to balance between getting points and improving their deck.
* Treasure cards produce money. They're weak for their cost, but you can play
as many Treasures as you want. These often form the backbone of your deck.
* Action cards have a variety of powerful effects. To balance this, each player
is limited to 1 Action per turn. However, some Actions (like Cellar and Village,
displayed below) give you more actions.

IMAGE

What makes Dominion so replayable is that every set comes with around 25
Action cards. Before the game starts, players randomly pick 10 Action cards to
use that game. Those Action cards make up the supply, a shared pool of cards
that everyone buys from. The randomization makes every game of Dominion a
different experience, and when you consider there are 8 (CHECK) sets so far,
you're looking at an insane amount of replay value. There was also a certain
elegance to the rules. Everyone started with the same cards, everyone had
access to the same cards, and everyone had the same goal: build the best deck
you can as fast as you can. There's definitely luck in Dominion, but all the
symmetry makes it a very skill-testing game.

All these qualities made Dominion a commercial success. It was beloved on
BoardGameGeek, and in fact that's where strategy discussion started.
By the time I entered the scene, I was playing catch-up. The community had
already developed its own internal jargon. I read about the Silver Test (is
that card you want better than Silver?). I learned the difference between
terminals, cantrips, and +Actions. (Terminal actions give no actions. Cantrips
give +1 Card, +1 Action, and a minor effect, meaning they replace themselves.
+Actions give +2 Actions or more.) Debates over the strength of Chapel and Witch,
over the power of the Big Money strategy, rules of thumb for the opening - there
was a ton of existing content, and I read as much of it as I could.


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
Isotropic on a laptop with 5 minutes of battery life, and it
worked fine.
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
