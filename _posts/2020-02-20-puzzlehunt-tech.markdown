---
layout: post
title:  "A Puzzlehunt Tech Checklist"
date:   2020-02-20 03:10:00 -0500
---

My Little Pony: Puzzles are Magic wrapped up recently. I was the one tech person
for the hunt website, and while working on the hunt website, I learned a
bunch of things about how to run a good hunt website. This is an attempt to
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
and "incorrect", because it can open up new puzzle design space.
Example puzzles that rely on custom replies are
[Art of the Dress](https://www.puzzlesaremagic.com/puzzle/art-of-the-dress/)
from Puzzles are Magic, and [The Answer to This Puzzle Is...](https://2018.galacticpuzzlehunt.com/puzzle/the-answer-to-this-puzzle-is.html) from GPH 2018.

Note that if you decide to confirm partials, you'll encourage teams to guess
more, and you should make sure you aren't unduly punishing teams for trying to
check their work.

At minimum, your submissions should be tagged with the team that submitted them,
and the time they were made, which will be useful when you want to compute
submission statistics after-the-fact.


Errata
----------------------------------------------------------------------------

You will try to make a puzzlehunt without errata. You'll probably fail. Make sure
your puzzlehunt has a page that lists all errata you've issued so far, including
time that errata came out.

If you are building an MIT Mystery Hunt style puzzlehunt, where different
teams have different puzzles unlocked,
your errata should only be visible to teams that have unlocked the puzzle
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

You'll want the ability to email everyone (for hunt wide announcements),
everyone on a specific team (if you want to talk to that team), and everyone
who has unlocked but not solved a specific puzzle (to notify for errata).
You may also want the ability to email everyone who hasn't unlocked a specific
puzzle, if you want to provide extra help to struggling teams.


Puzzle Format
-----------------------------------------------------------------------------

For puzzles, you can either go for a PDF-by-default format, or HTML-by-default
format. I've seen hunts use both. For example, the two Australian hunts I've
done (mezzacotta and MUMS 2019) were both PDF by default.

The upside of PDF by default is that you know your puzzles will appear the
same to all users. You can usually assume PDFs will appear the same to all
users, which means you don't have to worry about how your puzzle will appear
in different browsers or operating systems.

Although it's more work, if you're running an online hunt, I'd advocate for
an HTML-by-default puzzlehunt. An HTML based hunt has the following advantages.

* You can more easily support "online-only" experiences, like music puzzles
and interactive puzzles.
* You reduce the number of clicks between a solver and the puzzle.
* If you have several constructors, it is easier to enforce consistent
fonts and styles across all your puzzles, and it is easier to change what
that consistent styling is (just change the default font in your CSS).
* If you need to issue errata, solvers will notice your errata faster if your
puzzle is HTML-based, because it will be apparent as soon as anyone either
refreshes or reopens the puzzle page. For PDF puzzles, solvers may not notice
the errata until they re-download the puzzle PDF, and it's possible solvers
may accidentally look at their old downloaded PDF instead of the updated PDF.

I believe in total, these benefits are worth the extra work required to support
HTML-by-default puzzles. Of course, you should use PDFs in cases where doing
so is much easier. (There was no way A to Zecora was ever going to be in an
HTML format.)

If you plan to have your puzzles be HTML by default, you'll want to have
tools that make doing so easier. It's not that it's impossible to write
HTML by hand, it's just incredibly tedious to do so. I personally like Markdown
for this. It's a lightweight syntax that builds directly to HTML, and you
can embed HTML inside your Markdown file if you need to.

I highly, highly, highly recommend writing scripts that partially automate
converting puzzles into HTML. Doing so reduces typo risk, and makes it easier
to update a puzzle based on testsolver feedback. For Puzzles are Magic, I had
some scripts that generated HTML for grids, and scripts that auto-generated
indices for puzzles based on taking 1 letter from every clue in a list.
These were very useful for Flying High, Recommendations, and Endgame. Each of
these ended up getting revised about 3 times each, and the scripts saved a
bunch of time and headache.


Access Control
------------------------------------------------------------------------------

Teams should not have access to a puzzle before they have unlocked it.
This is obvious, but what's less obviously true is that they also shouldn't
have access to any static resources that puzzle uses. Any puzzle specific
images, Javascript, CSS, PDFs, and so on should be blocked behind a check of
whether the team unlocked the puzzle in question.

Assume that solvers will find any file that isn't gated behind one of these
unlock checks, and check whether doing so would break anything about your
hunt.


Side Channel Leaks
------------------------------------------------------------------------------

There are many ways your puzzle can have side channels that leak information
you may not want to leak. For exmaple, according to author notes in
Wanted: Gangs of Six from MIT Mystery Hunt 2020, it used to be possible to
extract the names of the fonts used from the puzzle, and several of the font
names were named after the series they were from. To close this side-channel,
the author had to remaster all the fonts themselves to give them non-spoilery
names.

Audio files come with album and artist metadata, unless you clear them. PDF
files come with metadata that can leak info from their construction. For
example, for [A Noteworthy Puzzle](https://www.mumspuzzlehunt.com/solution/III/2/)
from the 2019 MUMS Puzzle Hunt, you could reconstruct the original sheet music
and color names by inspecting the PDF carefully.

This is especially relevant for interactive puzzles, which normally have
a client-side Javascript component. The rule-of-thumb in online video games is
to never, ever trust the client, and the same is true for puzzlehunts. In
MIT Mystery Hunt 2020, teammate was able to solve 2 or 3 puzzles by
inspecting the client-side Javascript, searching for the function that decrypted
hidden text, and decrypting every string until we found one that looked like
the answer. Left OUt is a very competent construction team and I'm not calling
them out, I'm pointing out that this is just fundamentally hard. You will get
solvers that are really good at programming, and they *will* reverse engineer
things faster than you may think.

To avoid this, adhere to the following conventions.

Make your filenames completely non-descriptive. If you have 10 images, name
them "1.png", "2.png", "3.png", and so on, in order of the webpage. The exception
is if doing so would spoil something else about the puzzle. For example, in
Anthropology from Puzzles are Magic, solvers needed to pair emoji hand signs to
numbers. I ended up using images because I didn't want to deal with emojis
looking different across operating systems. However, numbering the images
"1.png", "2.png", and so on would have been misleading, so I generated random
filenames for each image.

If you have hidden content that should only appear after a solver does a certain
step, hide it behind a random filename. If there is a secret 5th image and your
first four images are named "1.png" to "4.png", you don't want solvers to
shortcut the puzzle by trying to load "5.png".

If you are using any file format that comes with metadata, check how to
clear that metadata, and then do so before including it in your hunt.

Some puzzlehunt tech setups go as far as auto-generating random filenames for
every static resource in the hunt. I don't think you need to go that far, but
you can if you want.

For interactive puzzles, have key puzzle functionality hidden on the
server side, and verify the solution server-side before continuing. Continuing
with the Anthropology example, the client-side JS submits the entire grid
state in a POST request, and the server-side Python code verifies the grid
is a valid solution before allowing solvers to continue. For Applejack's Game,
all the client-side code does is repeat whatever the server-side code gives
it. This let me hide the card list and judge logic from the client.

Note that side channel implies that you don't want puzzle info to leak this
way. Sometimes, you do.
Alternatively, you can have filenames be part of your puzzle. A notable puzzle
in this vein I liked is p1cture from MIT Mystery Hunt 2015. Another puzzle like
this is Tree Ring Circus from MIT Mystery Hunt 2019. To solve the puzzle, you
needed to measure the ring sizes (diameters) of the given circles. The easiest
way to do so was to directly inspect the SVG file to see what radius was
used for each circle, and the solution says this was intentional. Another
puzzle that deliberately leaks info through filenames is p1cture from MIT
Mystery Hunt 2015. Your side channel leak is my puzzle idea.


Accessibility
-------------------------------------------------------------------------------

You can generally assume that most solvers will be on either Windows or Mac OS X,
they will normally use one of Chrome, Safari, or Firefox, and they'll be solving
from a laptop-sized or monitor-sized screen.

The key word here is *most*. The thing about accessibility is that it always
affects a minority of your users, but there are a lot of minorities out there.
If you want more people to solve your puzzlehunt, you'll need to be inclusive
when possible.

Some of your solvers will be color blind. Some of your solvers will be *legally*
blind. Some
of your solvers will heavily prefer printing puzzles versus solving them
online, and of those solvers, not all of them will have access to color printers.

You may not be able to please all of these people. If your puzzle is based
on image identification, the legally blind solver is not going to be able to solve
it. You can't even provide alt text that describe the image, because non-blind
solvers will use the alt text as a side channel. But, try to do
the best you can.

It's put best by this reply from the 2019 MIT Mystery Hunt AMA: determine the
minimum amount you are asking solvers to do for your puzzle, and then make sure
as many people who meet that minimum get to solve your puzzle.

For color blind solvers, try to avoid colors that are too visually similar to
one another, and if you need to use a large number of colors, consider providing
a color blind alternative.

For people who prefer printing puzzles, make sure that your puzzles print well.
By default, printers ignore all CSS, so by default, your puzzles probably
print poorly. You'll need to define custom print styling under a
`@media print` section in your CSS file to fix this. Try to avoid having
grids, crosswords, or clues split across page breaks, and double check your
CSS colors show up when you do Print Preview.

Some solvers will solve from smartphones or tablets, rather than desktops or
laptops. Check your site isn't completely broken on mobile.
Even solvers with access to laptops will appreciate being able to solve
puzzles on the go.

For example, in Number Hunting, we rendered all the clues as math equations using
MathJax, because it felt thematic and it was the prettiest way to display
the one clue that needed to use a square root. However, we found that MathJax
doesn't support line wrapping, making the equations render very poorly on mobile,
so we provided an uglier plaintext version as well.

As another example, in The Key is Going Slow and Steady, we used Prezi to build
the Is It A Good Pet flowchart. One thing we learned during hunt construction was
that if a puzzle looks big, it intimidates solvers and they're less likely to
start it. So, if you have a way to make a puzzle look smaller, it encourages
solvers to start work on your puzzle. No testsolver wanted to try solving
Recommendations, until I made all the pictionary images 4x smaller and collapsed
all the audio clips into a single file instead of 14 separate files. Doing so
didn't change the puzzle difficulty. If anything, it made it harder. But, it
made the puzzle take less screen space, and that was enough to get testsolvers to give it a shot.
We expected a similar problem could happen in The Key is Going Slow and Steady,
so we hid the full flowchart behind a dynamic Prezi presentation. The problem
this introduced from an accessibility standpoint is that Prezi doesn't
work on mobile, at all. The presentation was also quite slow and resource-hungry,
which was bad for people using old computers.
Given more time, I would have pushed for a more lightweight alternative.


Hardware
------------------------------------------------------------------------------

Your
