---
layout: post
title:  "A Puzzlehunt Tech Checklist"
date:   2020-02-20 03:10:00 -0500
---

My Little Pony: Puzzles are Magic wrapped up recently. I was the one tech person
for the hunt website, and while working on the hunt website, I realized how
many things you needed to know to run a good hunt website. This is an attempt to
list those things.

If you are reading this, I'm assuming that you know what puzzlehunts are, you've
done a few puzzlehunts yourself, and are either interested in running an online
puzzlehunt, or are interested in what the tech process looks like. I'm going to
assume you can program, and have some level of tech literacy. I define tech
literacy as knowing how to use search engines to understand software libraries
you've never used before.

Note: not everything listed here is possible in the Puzzles are Magic code.
Some of this is stuff I wish I had gotten to, and it's okay if your hunt doesn't
support everything here, but you should try to support most of it.


Using Existing Code
------------------------------------------------------------------------------

Generally, expect people to be hesitant to share their puzzlehunt code. This
isn't because they don't want to. It's because puzzlehunt coding is like
video game coding. It starts sane and well-designed, and becomes increasingly
hacky as you get closer to the hunt deadline. This is especially true if
the hunt has interactive puzzles, or does something weird with answer
submission. The codebase for Puzzles are Magic has a core I'm decently happy with, and then
a ton of hardcoded puzzle IDs and functionalities to make the hunt website
work as expected.

As far as I know, the only open-source puzzlehunt codebase is
Puzzlehunt CMU's
codebase, which can be found at [this GitHub](https://github.com/dlareau/puzzlehunt_server).
The Puzzles are Magic code is forked from this code, with several modifications.
This uses Django, served through Apache. Using Django + Apache isn't required,
but both are free, very widely used, and well tested, so they're solid picks.

Whether you start from scratch or start from an existing codebase, expect to
do some programming yourself.


Authentication
------------------------------------------------------------------------------

You will need to decide whether you want logins to be person-based, or team-based.

Person-based logins are good if you need very accurate counts of how many people
are solving your hunt. Puzzlehunt CMU uses person-based logins because it's
a CMU event where they provide free lunch, and they need to know how much food
to order. Microsoft College Puzzle Challenge uses person-based logins for a similar
reason. The upcoming Cryptex Puzzle Hunt uses person-based logins because
the winner is getting mailed a Cryptex, and they need to know who to contact
for shipping details.

If you use person-based logins, the general design pattern is that users can
create a team, receiving a randomly generated team code, and other users can
join a team if they know that team code.

The downside of person-based logins is that they add friction for pick-up
solvers. Every one of those pick-up solvers will need to fill out
your site's registration form before they get to see any puzzles. If you want
as many people as possible to look at your puzzles, this is bad.

If your hunt does not have physical prizes, and does not need very
accurate solver counts, I would recommend team-based logins instead. In
this setup, each team gets a single user account, with a shared username
and password.
This setup is easier for you, and it's easier for them.

If you use team-based logins, the general design pattern is that one person
creates the team, their email is the main point of contact for that team, and
each team gets a profile page where they can add and remove people from their
team.

Whatever login setup you use, make sure your site supports HTTPS and
password resets. Otherwise, you will get people complaining that you aren't
following security best practices, and I will be one of them. You may think
that no one will try to hack your puzzlehunt website. You will mostly be
correct, but people reuse passwords when they shouldn't, and you'll
almost certaintly get someone who reuses a personal password on your
hunt website. Just use HTTPS.
[Let's Encrypt](https://letsencrypt.org/)
is a free certificate signing authority, there's really no excuse at this point.

You should also make sure that team names and person names support Unicode.
Several teams have emoji as part of their team culture, and you need to support
it. I'd go as far as saying this is non-negotiable. Even if you don't care about
emoji, you'll get signups from all over. Puzzles are Magic got a few sign-ups
from Chinese MLP fans, and I'm sure they appreciated that we supported Chinese
characters in team names.


Admin Sites
----------------------------------------------------------------------------

Not everyone working on your Hunt will know how to program or interface
with a database, and those that do may not be interested in learning how
to interace with your code. You'll want admin sites that let you directly modify
your database from a web interface. This will let you modify team names if
teams make a typo, delete duplicate teams if you discover people who
registered twice, modify puzzles that need to be updated, and so on.
Django's default admin site should be good enough for this.

You'll also want pages that let you monitor the progress of the hunt, like
live-updating team progress leaderboards, live-updating submission queues, and
so on. The Puzzlehunt CMU codebase came with these built-in and you can check
their code to see how they work.


Unlock System
----------------------------------------------------------------------------

The following should be enough for the majority of use cases.

* Puzzles that unlock at a certain time.
* Puzzles that unlock if K of N input puzzles are solved.
* The ability to unlock puzzles manually for a specific team, or for all teams.


Answer Submission and Replies
----------------------------------------------------------------------------

Unless you expect to have someone awake 24/7 during Hunt, you'll probably want
an automatic answer checking system.

For guess limits, you can either give each team a limited number of guesses
per puzzle, or you can give unlimited guesses with rate limiting. Both are
valid choices.

Whether you want to confirm partials or not is up to you, but you should
make sure your submission reply system supports replies besides just "correct"
and "incorrect", because it lets you make more interesting puzzles.
An example puzzle that needed this
is [Art of the Dress](https://www.puzzlesaremagic.com/puzzle/art-of-the-dress/)
from Puzzles are Magic.

Note that if you decide to confirm partials, you'll encourage teams to guess
more, and you should make sure you aren't unduly punishing teams for trying to
check their work.

Make sure your code actually saves answer submissions to your database, and that
submissions are tagged with what time they were made. You'll want this to
compute stats after-the-fact.


Errata
----------------------------------------------------------------------------

You will try to make a puzzlehunt without errata. You'll probably fail. Make sure
your puzzlehunt has a page that lets you display issued errata for each puzzle.

If you are building an MIT Mystery Hunt style puzzlehunt, where different
teams have different puzzles unlocked,
make sure your errata is only visible to teams that have unlocked the puzzle
it corresponds to.

When you issue errata, you'll want to notify teams, which brings me to...


Email
---------------------------------------------------------------------------

If you have fewer than 100 participants, you can get away with listing everyone's
email in the BCC field. Above 100 participants, you'll likely get hit by
spam filters that stop emails sent to too many people.

At that point, you'll want an email system. Puzzles are Magic used Django's
built-in system, but we continually had troubles with it and it might be worth
using a dedicated mailing service like SendGrid or MailChimp.

If you do send emails yourself, due to the previously mentioned spam filter,
you'll need to split your list of email addresses into smaller groups of
50 to 80 email addresses each, then send an email to each separately, waiting
some time in between each email send. We never figured out exactly how long we
needed to wait, but 1 second between emails was too short and 20 seconds
between emails was to be fine.

You will want the ability to email everyone (for hunt wide announcements),
everyone on a specific team (if you want to talk to that team), and everyone
who has unlocked but not solved a specific puzzle (to notify for errata).
You may also want the ability to email everyone who hasn't unlocked a specific
puzzle, if you want to provide extra help to struggling teams.
