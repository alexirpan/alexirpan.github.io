---
layout: post
title:  "Perfectly Intelligent Mafia"
date:   2015-08-25 03:43:00 -0800
---

*This is an experiment I set for myself to see how quickly I could summarize the
results of an interesting paper I had read. I had the advantage of knowing the paper
was very approachable. Still, I need to clarify that this was written to optimize
writing time. Not clarity, not length, not style, and certainly not correctness (although
it looks correct when I look at it.)*

*Before writing this entry, I had read the paper and written a few Facebook posts
about the strategy, but nothing formal. This entry, including all code, was written
in 3 hours, 40 minutes.*

Recently, I found a paper by Braverman, Etasami and Mossel ([open access here](http://projecteuclid.org/euclid.aoap/1211819786)) about
strategies in the game of Mafia. As with many other games, assuming perfect
play turns it into a math problem, and acting out the strategy in real life
ruins a lot of the fun,
but at least the math is interesting.

First, let's lay down some ground rules for Mafia, since there are many house
variations.

- There are $$N$$ players, where $$M$$ players are Mafia. Mafia members
know who each other are. Town members do not know who each other are.
    - Some town members are power roles. Common power roles are the cop
    (can investigate people) and the doctor (can save people from the mafia), but
    the paper only analyzes the game with the cop.
- The game starts in day, and alternates between day and night.
    - Each day, all players have a discussion, then choose someone to lynch by a plurality vote. These votes
    are public. A strict majority is required to lynch someone.
    - Each night, mafia chooses someone to kill. The cop can choose to investigate
    a player, and the moderator will tell the cop whether he or she is town
    or mafia. No one else knows who the cop investigated.
- Whenever someone dies in day or night, the moderator announces whether they
were vanilla town, cop, or mafia.
- Town wins if all mafia members get lynched. Mafia wins if mafia are a majority
of the town (since at that point, mafia control the lynch and can kill whomever
they want in the day.)

For the perfectly intelligent version of Mafia, we also assume the following.

- Players get a fixed amount of computation time to choose who to lynch and who
to kill. This ensures the game eventually ends.
- Players are allowed to call for an informal secret vote. Every player makes
a vote in secret. The moderator announces how many votes each player got.
This does not form a binding contract - the lynching is still done through
the open vote, and people can vote differently in the final vote.
    - Presumably all players can hand a note to the trusted moderator, or a cryptographic
    voting scheme is set up beforehand.
- Players can send hidden messages to other players. The only public information
is that a player has sent or received a message from another player, and the message
contents remain hidden.
    - This is done through public key crypto, to allow sending
    messages that only the intended recipient can decrypt.
    - It is assumed the computation time
    to choose who to lynch and kill is not long enough to break the public key.

The paper considers two different games. In the first game, there are no
power roles. In the second game, there is exactly one cop.
In both cases, we are
interested in how many mafia members there need to be for town to win 50% of the time.

No Power Roles
----------------

In real life mafia, the winner comes down to whether mafia can act convincingly like a townie,
and whether town can determine who is lying.

In perfectly intelligent mafia, a mafia member leaks no information and acts exactly
like how a townie would act. So,
it is impossible for town to gain any information on who is mafia and who isn't.
Thus, the best town can do is lynch randomly. Since no town members
are special, the best mafia can do is kill people randomly. (In perfectly
intelligent mafia, there is no leader of discussion, and there is no person
who avoids talking, so no one is more special than any one else. It's all
very egalitarian.)

This is a disappointingly boring optimal strategy, but it still needs to be
implementable despite malicious parties.
This can be done as follows.

1. Assign each player a number from $$0$$ to $$R-1$$, where $$R$$ is the number
of players still alive.
2. Every player generates a random number from $$0$$ to $$R-1$$.
3. Every player announces their number simultaneously. Town unanimously lynches
the sum of numbers mod $$R$$.

This generates a random number as long as one townie is still alive. Even if everyone
else is mafia, no matter what numbers they choose, the resulting sum will be
uniformly distributed. The only people who have incentives to not match the
town vote are
mafia, and anyone who defects is immediately slated for execution the next day.
(Defection also only changes the final vote if a majority of players are mafia, at
which point the game is over anyways.)

Under this scheme, town wins half the time when the number of mafia is
order $$\sqrt{N}$$. There is a decent amount of math to prove this is correct,
but we can easily write some simulations to see if we can trust their result.
Here is a sample script to do this in Python.

{% highlight python %}
import random

Ns = [1000, 4000, 9000]

def simulate_game(n, m):
    # Simulate n players with m mafia, return True on win
    while n > 2 * m:
        # Lynch random player
        if random.randint(0, n-1) < m:
            # Mafia lynched
            m -= 1
        if m == 0:
            return True
        # Mafia lynches random player as well. Two total deaths
        n -= 2

    return False


def get_win_odds(n, m):
    TRIALS = 10000
    return sum(simulate_game(n,m) for _ in xrange(TRIALS)) / float(TRIALS)


def find_5050(n):
    threshold = 0.005
    # Binary search to find m since probability of winning strictly increases with m
    low = 1
    high = n
    while True:
        mid = (low + high) // 2
        per = get_win_odds(n, mid)
        print 'low = %d, high = %d, mid = %d, win chance = %f' % (low, high, mid, per)
        if per < 0.5 - threshold:
            high = mid
        elif per > 0.5 + threshold:
            low = mid
        else:
            return mid


for N in Ns:
    print 'N = %d' % N
    print find_5050(N)

{% endhighlight %}

When $$N = 1000$$, the 50/50 win chance is at 11 mafia. When $$N = 4000$$, the
50/50 win chance is at 21-22 mafia. When $$N = 9000$$, the 50/50 win chance is at
32-34 mafia. This falls in line with growing with $$\sqrt{N}$$.
(If you run the code for yourself, you may want
to increase the threshold, since the variability is more than 0.5%)


One Cop To Rule Them All
------------------------

It turns out the addition of a single cop radically changes the number of
mafia needed to make the game fair. In the one-cop game, the number of mafia
needs to be proportional to $$N$$ instead of $$\sqrt{N}$$

This may be surprising, but remember that a perfectly intelligent player can act exactly like
a vanilla townie. The cop can hide perfectly, and means the mafia's best strategy is still to lynch
randomly. Because the odds of hitting the cop are so small, the cop has several rounds
to collect intel. More interestingly, the power of the cop is not in finding
mafia members. It is in verifying players are town.

The strategy from the paper is not guaranteed to be optimal, but
it is optimal asymptotically - there may be different constant
factors with optimizations. The strategy is split into three phases.

Phase 1
========
Assume there are $$\eta N$$ mafia, where $$0 < \eta < 1$$.
For $$\sqrt{\eta}N$$ rounds, the cop randomly investigates,
town randomly lynches, and mafia randomly kills. If the cop is killed
in phase 1, town immediately forfeits.

Phase 2
========
The cop sends a hidden message to every investigated player that turned up
town, containing an ordered list of all investigation results. In the note passing
implementation of this, the cop also sends a note to every other player,
but that note is blank, to disguise who the investigated players were.
In the public key crypto implementation,
this is not necessary because all messages are sent in public (but only
investigated town can decrypt them.)

The cop then immediately asks to be lynched. This seems unintuitive;
why would the cop want to die? However, once again recall that players
are perfectly intelligent. On this round, another player could claim to
be cop, send the same messages, and it would be impossible to tell who
is genuine. The key is that when a player dies, their role and
alignment is announced. So, the announcement that town has lynched
the cop is the authentication for the list sent. If multiple
people claim cop, they are lynched in order of the claim, since only
mafia has motivation to claim cop.

Phase 3
==========
At this phase, there exists a cabal of townies who knows all members
of the cabal, and knows all those members are town. Additionally, there
are more cabal members than mafia, since $$\sqrt{\eta}N > \eta N$$ for
$$\eta < 1$$.

On each day, players call for a secret vote. The *leader* of the cabal
is defined as the townie highest up the investigation list. (If the leader dies,
the second highest townie is the new leader.) One member of the cabal chooses a person
$$p$$ that is not in the cabal, and sends that message to every other cabal member.
Everyone in the cabal votes $$p$$ in the secret vote, and all town members
abstain. In the open vote, every player votes for the winner of the secret
vote. Since there are more cabal than mafia, it is impossible for mafia to
hijack the secret vote, and thus every lynch avoids the cabal, improving
the successful lynch probability massively.

Overall, the game ends when either
- Cabal size $$\le$$ mafia size, in which case town forfeits immediately because
mafia can hijack the secret vote.
- Every citizen outside the cabal dies, in which case town wins - there
are more cabal members than mafia members, and every lynch made by the cabal
hits mafia.
- All mafia members die, in which case town wins.

For $$\eta < 1/49$$, this strategy works around half the time. Again, there is
quite a bit of math to show the cop lives and the cabal stays large enough,
but we can sidestep all of that by doing more simulations. Again, here is a
Python implementation.

{% highlight python %}
import random

N = 1000

def simulate_game(n, eta):
    # Simulate n players with eta * n mafia, return True on win
    m = int(round(eta * n))
    mafia_left = m
    t = int(round(eta ** 0.5 * n))
    players = set(xrange(n))
    town = set(xrange(m, n))
    mafia = set(xrange(m))
    investigated = set()
    investigated.add(n-1) # Hack to avoid investigating self

    # Phase 1
    for _ in xrange(t):
        if len(mafia) >= len(town):
            return False
        # Lynch random player
        ra = random.choice(tuple(players))
        if ra == n-1:
            # Detective lynched
            return False
        elif ra < m:
            # Mafia lynched
            mafia.remove(ra)
        else:
            town.remove(ra)
        players.remove(ra)
        # Detective investigation
        investigated.add(
            random.choice(tuple(players - investigated))
        )
        # Mafia kill. Must happen after detective investigates
        # since detective can investigated player that gets killed same night.
        ki = random.choice(tuple(town))
        if ki == n-1:
            # Detective killed
            return False
        town.remove(ki)
        players.remove(ki)

    # Phase 2
    investigated.remove(n-1) # Undo investigation hack
    cabal = investigated - mafia
    town.remove(n-1)

    # Phase 3
    while len(cabal) > len(mafia):
        if len(mafia) == 0:
            return True
        if len(town) == 0:
            return True  # Caught by case above but this speeds up the endgame.
        if len(mafia) >= len(town):
            return False
        # Cabal lynch
        lyn = random.choice(tuple(town | mafia - cabal))
        if lyn < m:
            mafia.remove(lyn)
        else:
            town.remove(lyn)
        # Mafia kill
        ki = random.choice(tuple(town))
        town.remove(ki)
        if ki in cabal:
            cabal.remove(ki)
    # Cabal too small while mafia live, failed.
    return False


def get_win_odds(n, eta):
    TRIALS = 10000
    return sum(simulate_game(n,eta) for _ in xrange(TRIALS)) / float(TRIALS)


def find_5050(n):
    threshold = 0.005
    # Binary search to find m since probability of winning strictly increases with m
    low = 0
    high = 0.99
    while True:
        mid = (low + high) / 2.0
        per = get_win_odds(n, mid)
        print 'low = %f, high = %f, mid = %f, win chance = %f' % (low, high, mid, per)
        if per < 0.5 - threshold:
            high = mid
        elif per > 0.5 + threshold:
            low = mid
        else:
            return mid

print find_5050(N)
{% endhighlight %}

This code is much more complicated, because we need to account for the detective
investigating no person twice and the mafia killing a cabal member before the
detective reveals themselves. The output in one run ended up being

    low = 0.000000, high = 0.990000, mid = 0.495000, win chance = 0.000000
    low = 0.000000, high = 0.495000, mid = 0.247500, win chance = 0.000000
    low = 0.000000, high = 0.247500, mid = 0.123750, win chance = 0.000000
    low = 0.000000, high = 0.123750, mid = 0.061875, win chance = 0.024000
    low = 0.000000, high = 0.061875, mid = 0.030937, win chance = 0.253700
    low = 0.000000, high = 0.030937, mid = 0.015469, win chance = 0.587000
    low = 0.015469, high = 0.030937, mid = 0.023203, win chance = 0.398300
    low = 0.015469, high = 0.023203, mid = 0.019336, win chance = 0.497000

giving $$\eta \approx 0.019336$$, which is below the $$1/49 = 0.0204$$ claimed.

Remarks
==========
This strategy can be easily improved. In the implementation above, I did not
let the cabal lynch mafia members investigated by the detective. I also did
not let the game continue when the detective dies or when the cabal becomes
too small, even though it is strictly better for town to keep playing because
there is still a small chance of winning.

All this reasoning relies on the existence of secret message passing.
If that doesn't sit well with you, the cop can also choose to not reveal
themselves until a majority of alive players are verified town. At this point, the
cop reveals themselves and gets lynched. In this case, the cabal is public
knowledge. Each day, the cabal lynches a random person not in the cabal, and mafia
kills a person in the cabal. By
construction, the cabal will always be a majority of living players, so eventually all mafia members
will be killed. This is proved to work for a smaller $$\eta$$, but is still
only fair if the number of mafia is proportional to $$N$$.

Potential Followups
-------------------
The obvious place to go from here is to analyze the doctor, or analyze a multi-cop
game. Some of this is done in the original paper, and I recommend reading it if
you are interested in these results. There are also plenty of other roles to use.
Vigilantes, roleblockers, serial killers...if you try, you might find something
interesting falls out.


Practically Perfect In Every Way...
-----------------------------------

The most important part of this paper is not learning how to play Mafia given perfect
intelligence.

it's the existence of the paper itself.
Much like the paper showing [Nintendo games are NP-hard](http://arxiv.org/abs/1203.1895),
it shows that if you look hard enough, you can find interesting problems everywhere.
