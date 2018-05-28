---
layout: post
title:  "Pokemon Red/Blue as an AI Testbed"
date:   2018-05-27 02:31:00 -0700
---

This started as a joke. Something that was fun to think about, but was never
meant to be serious.

But then I thought about it more, and started seeing the potential. It's still
a bit ridiculous, but it's more plausible than I thought.

Here's the proposal: **the next grand challenge for AI should be to train an
agent to beat Pokemon Red, Blue, or Yellow.**


Arguments in Favor
======================================================

Popularity
------------------------------------------------------

The first grand challenge was Chess. Then it was Go. But in between Chess and
Go, there was a game called Arimaa.

PICTURE?

Arimaa is game that can be played with a chessboard and chess pieces. It was
designed to both be a fun game, and to be harder for computers to solve than
Chess, thanks to a larger branching factor.

As part of this, the creator of Arimaa announced a computer Arimaa challenge.
Every year, the best human Arimaa player would play the best computer Arimaa
player. The Arimaa agent had to run on hardware that cost no more than $1000.
The creator of the first superhuman Arimaa bot would win a cash prize.

This prize was won in 2007 (CHECK). Was it a big deal? Well, maybe, if you were into
the Arimaa or game AI community. I didn't hear about it until a few years after
it happened, when I was bored and visited the Arimaa Wikipedia page out of
curiosity.

In part, this was because the winning bot was made by a hobbyist, and there was
no accompanying PR blitz. But I feel a bigger part is that not many people
cared about the *game* of Arimaa. A ton of people have heard of Chess, or Go,
and played them without a care in the world about when AI would beat humans.
It's hard to build buzz around something with a small target audience, even if
the solution has inspiring ideas.

This is where the Gen 1 Pokemon games shine. They were not just a thing, they
were *the* thing. In the general zeitgeist, they're easily the most famous
generation of Pokemon games. It's not that Pokemon has ever stopped being a
thing, it's just that Gen 1 was massively big in popular culture. Pokemon Go
has taught us that nostalgia for Gen 1 is still alive.

If a serious project got started, I'm sure there would be lots of interest.
I know this because I proposed a Pokemon AI at a hackathon and got three
different people to signal interest. (We didn't work on it because all the
emulators I could find were best supported on Windows, no one had a Windows
laptop, and spending a hackathon debugging emulators didn't sound like a
great time.)


Turn-Based Gameplay
--------------------------------------------------------

Nothing in Pokemon requires reaction time. All movement is tile-based.
All time limits (Repels, Safari Zone, poison damage) are based on the number
of tiles you move, meaning that staying still never advances the game
state. All battles are turn-based, and have no real-time elements.
At best, the only real-time tricks are things based around manipulating
the RNG, or for glitches like save corruption or the Fly glitch.

In principle, you could have the game run in real time, and completely
ignore inference speed. In practice, this probably isn't that important,
because you'd likely be running the game on an emulator that supports
frame-by-frame advancing, but it's a nice bonus.


Natural Goals With Different Time Horizons
------------------------------------------------------------


