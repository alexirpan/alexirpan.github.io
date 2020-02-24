---
layout: post
title:  "A Puzzlehunt Tech Checklist"
date:   2020-02-20 03:10:00 -0500
---

[My Little Pony: Puzzles are Magic](https://www.puzzlesaremagic.com/) wrapped up recently. I was the tech person
for the hunt. While setting up the hunt website, I learned a bunch of things
about how to run an online puzzlehunt. This is an attempt to list those things.

If you are reading this, I'm assuming that you know what puzzlehunts are, you've
done a few puzzlehunts yourself, and are either interested in running an online
puzzlehunt, or are interested in what the tech process looks like.

Not everything mentioned here is something we got to for Puzzles are Magic. This
list is a mix of things we did, and things we wish we did.
It's okay if your hunt doesn't support everything here, but you
should aim to support a lot of it.


Using Existing Code
------------------------------------------------------------------------------

Generally, expect people to be hesitant to share their puzzlehunt code. This
isn't because they don't want to. It's because puzzlehunt coding is like
video game coding. It starts sane and well-designed, and becomes increasingly
hacky as you get closer to the hunt deadline. This is especially true if
the hunt is heavy on interactive puzzles.
The codebase for Puzzles are Magic has a core I'm decently happy with, and then
a ton of hardcoded puzzle IDs and functionalities to make the hunt website
work the way it was supposed to.

As far as I know, the only open-source puzzlehunt codebase is
Puzzlehunt CMU's
codebase, which can be found at [this GitHub](https://github.com/dlareau/puzzlehunt_server).
The Puzzles are Magic code is forked from this code, with several modifications.
Our hunt was written in Django and served using Apache. Using Django + Apache isn't required,
but both are free, very widely used, and well tested, so they're solid picks.

Whether you start from scratch or start from an existing codebase, expect to
do some programming yourself.


Authentication
------------------------------------------------------------------------------

You will need to decide whether you want logins to be person-based, or team-based.

Person-based logins are good if you need very accurate counts of how many people
are solving your hunt. Puzzlehunt CMU uses person-based logins because it's
a CMU event where they provide free lunch, and they need to know how much food
to order. Microsoft College Puzzle Challenge used person-based logins for a similar
reason. The upcoming Cryptex Puzzle Hunt uses person-based logins because
the winner is getting mailed a Cryptex, and they need to know who to contact
for shipping details.

If you use person-based logins, the general design pattern is that every
person creates an account, and each user can join a team if they enter some
team code or password that links a team to their account.

The downside of person-based logins is that they add friction for pick-up
solvers. Every one of those pick-up solvers will need to fill out
your site's registration form before they get to see any puzzles. If you want
as many people as possible to look at your puzzles, this is bad.

If your hunt does not have physical prizes, and does not need very
accurate solver counts, I would recommend team-based logins instead. In
this setup, each team gets a single user account, with a shared username
and password. One person creates the team, and their email is the main
point of contact for that team. They can then optionally add other team members
and emails from that team's profile page.

Whatever login setup you use, make sure your site supports HTTPS and
password resets. Otherwise, you will get people complaining that you aren't
following security best practices. I'll be one of those people.

You may think
that no one will try to hack your puzzlehunt website. You'll be correct.
However, people reuse passwords when they shouldn't, and you don't want
packet sniffers to figure out any re-used passwords.
Just use HTTPS.
[Let's Encrypt](https://letsencrypt.org/)
is a free certificate signing authority you can use for this.

Make sure that team names and person names support Unicode.
Several teams have emoji as part of their team culture, and you need to support
it. I'd go as far as saying this is non-negotiable. Even if you don't care about
emoji, Unicode comes with other benefits too. Puzzles are Magic got a few
sign-ups from Chinese MLP fans. We're not sure how that happened, but I'm sure
they appreciated Chinese character support.


Admin Sites
----------------------------------------------------------------------------

Not everyone working on your Hunt will know how to program or interface
with a database, and even those that do may not want to pull out a computer
terminal every time they want to change something.
You'll want admin sites that let you directly modify
your database from a web interface.
Django has a default admin site, and we found that was good enough.

Some things we used this for were: fixing typos in team names,
deleting duplicate teams created by people who registered twice,
and modifying answer replies when a 3rd-party site our hunt relied on went
down.

You'll also want pages that let you monitor the progress of the hunt.
The Puzzlehunt CMU codebase had some custom admin sites for live-updating
team progress and submissions queues, and we basically used those with
a few minor changes.


Unlock System
----------------------------------------------------------------------------

Supporting the following should be good enough for a majority of use cases.

* Puzzles that unlock at a certain time.
* Puzzles that unlock if K of N input puzzles are solved.
* The ability to unlock puzzles manually for a specific team, or for all teams.


Answer Submission and Replies
----------------------------------------------------------------------------

Unless you expect and want to have someone awake 24/7 during Hunt, you'll
want an automatic answer checking system.

For guess limits, you can either give each team a limited number of guesses
per puzzle, or you can give unlimited guesses with rate limiting. Both are
valid choices. Whatever you do, please, please don't make your answer
checker case-sensitive.

Whether you want to confirm partials or not is up to you, but
make sure your submission reply system supports replies besides just "correct"
and "incorrect". Having this can open up new puzzle design space.
Example puzzles that rely on custom replies are
[Art of the Dress](https://www.puzzlesaremagic.com/puzzle/art-of-the-dress/)
from Puzzles are Magic, and [The Answer to This Puzzle Is...](https://2018.galacticpuzzlehunt.com/puzzle/the-answer-to-this-puzzle-is.html) from GPH 2018.

Note that if you decide to confirm partials, you'll encourage teams to guess
more, and you should make sure you aren't unduly punishing teams for trying to
check their work.

At minimum, your submissions should be tagged with the team that submitted them,
and the time they were made, since this will let you compute submissions
statistics after-the-fact.


Errata
----------------------------------------------------------------------------

You will try to make a puzzlehunt without errata. You'll probably fail. Make sure
your puzzlehunt has a page that lists all errata you've issued so far, including
the time that errata came out.

If you are building an MIT Mystery Hunt style puzzlehunt, where different
teams have different puzzles unlocked,
your errata should only be visible to teams that have unlocked the puzzle
it corresponds to.

When you issue errata, you'll want to notify teams, which brings me to...


Email
---------------------------------------------------------------------------

If you have fewer than 100 participants, you can get away with emailing everyone
at once, putting their emails into the BCC field.
Above 100 participants, you'll likely get hit by spam filters.

At that point, you'll want an email system. Puzzles are Magic sent
email directly through Django, but we continually had trouble with it,
and it might be worth
using a dedicated mailing service like SendGrid or MailChimp.

You'll want the ability to email everyone (for hunt wide announcements),
everyone on a specific team (if you want to talk to that team), and everyone
who has unlocked but not solved a specific puzzle (to notify for errata).
You may also want the ability to email everyone who hasn't unlocked a specific
puzzle, if you want to provide extra help to struggling teams.

In our email setup, we split our list of emails into chunks of 80
emails each, then added a 20 second wait time between each email send. Without
this wait time, we found Gmail refused to send our emails (likely because
of a spam filter of some sort).


Puzzle Format
-----------------------------------------------------------------------------

For puzzles, you can either go for a PDF-by-default format, or HTML-by-default
format. I've seen hunts use both.

The upside of PDF-by-default is that you know your puzzles will appear the
same to all users. You can usually assume PDFs will appear the same to all
users, which means you don't have to worry about how your puzzle will appear
in different browsers or operating systems.

Despite this, if you're running an online hunt, I'd advocate for
an HTML-by-default puzzlehunt. An HTML based hunt has the following advantages.

* You can more easily support "online-only" experiences, like music puzzles
and interactive puzzles.
* You reduce the number of clicks between a solver and the puzzle.
* If you have several constructors, you can have a global CSS file that
standardizes consistent fonts and styles across all your puzzles. With PDFs,
you would need to do this standardization yourself.
* If you need to issue errata, solvers will notice your errata faster if your
puzzle is HTML-based, because it will be apparent as soon as anyone either
refreshes or reopens the puzzle page. For PDF puzzles, solvers may not notice
the errata until they re-download the puzzle PDF, and it's possible solvers
may accidentally look at their old download instead of the new one.

In total, these benefits are worth the extra work required to support
HTML-by-default puzzles. Of course, you should use PDFs in cases where doing
so is much easier. (There was no way [A to Zecora](https://www.puzzlesaremagic.com/puzzle/a-to-zecora/) was ever going to be in an
HTML format.)

If you plan to have your puzzles be HTML-by-default, you'll want to have
tools that make writing HTML easier.
It's not that it's impossible to write
HTML by hand, it's just incredibly tedious to do so. I personally like Markdown,
it's a lightweight syntax that builds directly to HTML.

I highly, highly, highly recommend writing scripts that partially automate
converting puzzles into HTML. Doing so reduces typo risk, and makes it easier
to update a puzzle based on testsolver feedback. For Puzzles are Magic, I wrote
scripts that generated HTML for grids, and auto-generated extraction indices
for puzzles
based on taking 1 letter from every clue in a list.
These were very useful for Flying High, Recommendations, and Endgame. Each of
those puzzles were revised about 3 times, and the scripts made it much
easier to build the required edits.


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


File Metadata
------------------------------------------------------------------------------

There are many ways your puzzle can have side channels that leak information
you may not want to leak. For example, the puzzle
[Wanted: Gangs of Six]( https://pennypark.fun/puzzle/wanted_gangs/) involves
identifying gangs of six characters from several series, extracting
cluephrases using numbers written in fonts matching each series. The solution
mentions that testsolvers were able to extract the font names from the PDF
properties, and many of the font names were named after the series in question.
The final puzzle uses remastered fonts with less spoiler-y names.
As another example,
for [A Noteworthy Puzzle](https://www.mumspuzzlehunt.com/solution/III/2/)
from the 2019 MUMS Puzzle Hunt, the original sheet music and color names could
be retrieved from inspecting the PDF file.

Audio files come with album and artist metadata, unless you clear them. PDF
files come with metadata, unless you clear them. Make sure you do so.

Note that "side channel" implies you don't want puzzle info to leak this way.
Sometimes, leaking info this way is okay, and even encouraged. In
[Tree Ring Circus](http://www.mit.edu/~puzzle/2019/puzzle/tree_ring_circus.html)
from MIT Mystery Hunt 2019, you needed to find the diameters of each circle to
solve the puzzle. The circles were drawn in SVG, and to aid solving, the
radii used exactly matched the radii needed to extract the solution.


Filenames
------------------------------------------------------------------------------

Make your filenames completely non-descriptive. If you have 10 images, name
them "1.png", "2.png", "3.png", and so on, in order of the webpage. The exception
is if doing so would spoil something else about the puzzle. For example, in
[Anthropology](https://www.puzzlesaremagic.com/puzzle/anthropology/) from Puzzles are Magic, solvers needed to pair emoji hand signs to
numbers. I ended up using images because I didn't want to deal with emojis
looking different across operating systems. However, naming the images
"1.png", "2.png", and so on could have been misleading. I didn't want solvers
pairing the emoji in "1.png" to the number 1, so I used random filenames for
each image.

If you have an interactive puzzle where hidden content only appears after the
solvers finish part of the puzzle, hide that content behind a random filename.
For example, if you have a secret 5th image, and you name your first four
images "1.png" to "4.png", you don't want solvers to shortcut the puzzle by
trying to load "5.png".

Again, like the file metadata mentioned above, sometimes leaking info this way
is okay. An example puzzle that does this is [p1ctures](http://web.mit.edu/puzzle/www/2015/puzzle/p1ctures/)
from MIT Mystery Hunt 2015. Yes, almost anything
can be part of a puzzle if you try hard enough.


Interactive Puzzles
------------------------------------------------------------------------------

Interactive puzzles are usually more work to make than other puzzles, but
often they're the most memorable or popular puzzles. (My
theory is that interactive puzzles naturally lead to emergent complexity,
and emergent complexity is the entire reason that people like solving
puzzlehunt-style puzzles.)

The rule-of-thumb in online video games is
to never, ever trust the client. Puzzlehunts are the same.
In MIT Mystery Hunt 2020, teammate was able to solve 2 or 3 interactive
puzzles by inspecting the client-side Javascript, finding a list of encrypted
strings, searching for the function that decrypted then, and ran the
descryption until we found ones that looked like the answer.

The only 100% safe way to prevent these kinds of shortcuts is to move all
key puzzle functionality to server-side code. For
[Anthropology](https://www.puzzlesaremagic.com/puzzle/anthropology/),
the client sends the entire grid state to the server, the server verifies
it, and the client processes the given response. This let me hide all the grid
logic.
For
[Applejack's Game](https://www.puzzlesaremagic.com/puzzle/applejacks-game/),
the client sends the entered message, the server cleans it into only letters
and commas, and the client forwards the response. This let me hide the card
list and the judging logic.

Server-side confirmation has higher latency than client-side confirmation,
so if you are worried about responsiveness, only confirm the most important
parts of the puzzle on the server-side. For Puzzles are Magic, our logic
was very simple, and we figured it would be responsive enough if everything
was server side.

If possible, try to avoid repeating logic across the client and server. The
[GPH 2019 AMA](https://2019.galacticpuzzlehunt.com/wrapup/ama.html) mentions that
Peaches had a bug where the client-side logic didn't match the server-side
verification, which caused some valid solutions to get marked as incorrect.
As mentioned in that AMA, if your server side validation fails, make sure to
give teams an obvious error, perhaps one that tells them to contact you and
explain what they were doing beforehand.


Accessibility
-------------------------------------------------------------------------------

You can generally assume that most solvers will be on either Windows or Mac OS X,
they will normally use one of Chrome, Safari, or Firefox, and they'll be solving
from a laptop-sized or monitor-sized screen.

The key word here is *most*. Each accessiblity issue will always affect a minority
of your users, but there are a lot of different minorities.
If you want more people to solve your puzzlehunt, you'll need to be inclusive
when possible.

Some of your solvers will be color blind. Some of your solvers will be *legally*
blind. Some
of your solvers will heavily prefer printing puzzles versus solving them
online. Of those solvers, not all of them will have access to color printers.

You may not be able to please all of these people. If your puzzle is based
on image identification, the legally blind solver is not going to be able to solve
it. You can't even provide alt text that describe the image, because non-blind
solvers will use the alt text as a side channel. But, try to do
the best you can. As mentioned from the 2019 MIT Mystery Hunt AMA,
["Keep in mind what the puzzle actually needs in terms of skills and abilities, and what you’re presuming the solver/s will have. Wherever there’s a mismatch, try to make the puzzle suit the smallest set of abilities without stomping on data the puzzle needs."](https://www.reddit.com/r/mysteryhunt/comments/am5s1d/were_setec_astronomy_and_we_just_ran_a_mystery/efjklm7/).

For color blind solvers, try to avoid colors that are too visually similar to
one another. If you need to use a large number of colors, consider providing
a color blind alternative.

For people who prefer printing puzzles, make sure that your puzzles print well.
By default, printers ignore all CSS, so by default, your puzzles probably
print poorly. You'll need to define [specific print CSS](https://www.smashingmagazine.com/2018/05/print-stylesheets-in-2018/)
files to get your puzzles to print correctly. Some specific issues we hit
in Puzzles are Magic were grids getting split across page breaks, CSS colors
not appearing on print, and hints appearing on print because our
black background hiding the hints wasn't included.

In addition to those concerns, some solvers will be solving from smartphones or tablets, rather
than desktops or laptops. It's okay if your site works worse from mobile, but
make sure your site isn't completely broken on mobile. Even solvers with laptops
will appreciate being able to solve puzzles on the go.

A place I felt we did this well was [Number Hunting](https://www.puzzlesaremagic.com/puzzle/number-hunting/).
We rendered the clues as math equations for flavor reasons and style reasons,
but we included an uglier plaintext version as well, in case MathJax rendering
failed or was slow for certain users.

A place we could have done more was
[The Key is Going Slow and Steady](https://www.puzzlesaremagic.com/puzzle/the-key-is-going-slow-and-steady/).
One lesson we learned during hunt construction was that puzzle presentation
really matters. If a puzzle looks big, it intimidates solvers, and they're
less likely to start it. So, if you can find a way to make a puzzle look
smaller, you can make the puzzle look more inviting. No testsolver wanted to
solve [Recommendations](https://www.puzzlesaremagic.com/puzzle/recommendations/),
so I made all the images 4x smaller and collapsed the 14 audio clips into one.
This didn't change the core puzzle content. If anything, it made it harder.
But, it made the puzzle *look* smaller, and that was enough to get testsolvers
to give it a shot.

For The Key is Going Slow and Steady, we used [Prezi](https://prezi.com)
to make the flowchart look smaller than it really was. The problem this
introduced from an accessibility standpoint was that Prezi loaded slowly,
was pretty resource-hungry, and didn't work on mobile devices.
Providing a lightweight alternative to the Prezi would have made the puzzle
cleaner.


Hardware and Load Testing
------------------------------------------------------------------------------

To run your hunt, you're going to need a server. If you work at a university,
check if your university provides free computing services. If you don't have
a server on hand, or you don't want to trust your personal Internet, you'll
probably use a cloud computing service.

For cloud services, you can either go for a raw machine, or you can use app
creation services like Google App Engine or AWS Elastic Beanstalk. App services
will give you less flexibility, will require writing code to fit their API,
and are more expensive. However, they'll handle more things for you, like
autoscaling.

Puzzles are Magic was hosted from a raw machine we purchased through Google
Compute Engine. We did this because it required the fewest changes from
the Puzzlehunt CMU code we started from. Most cloud services offer free
cloud credit to new accounts. Unfortunately, our free trial expired about
6 weeks before the hunt started.
We ended up spending about $120 in total. Of that total, $80 was spent
in the month of hunt, and $0 was spent in the remaining time. We're currently
spending about $16/month to run the hunt in maintenance mode.

Website load will start slow, and will rapidly increase in the days before
hunt. Most teams won't sign up until a few days before your hunt starts, so
keep this in mind when load testing. Below is a chart for number of
active users each day for Puzzles are Magic.

![User chart](/public/puzzlehunt-tech/annotated_view_chart.png)
{: .centered }

We load tested our website using [Locust](https://locust.io/). Our target was
supporting 750 active users at once. We picked that number based on registration
counts and the desired margin of error. Early on, we had trouble getting more
than 250 active users to work, but we eventually debugged it to testing from
a slow Internet connection that had trouble pretending to be 250 users at once,
so make sure you test from a fast connection, or you split your load test
across a few networks.

If your server is too busy to respond to solvers, it's also going to be
too busy to respond to your remote login attempts to fix it, so you want to err on the
side of too large.


More Exact Hardware Details
-------------------------------------------------------------------------

We used a `n1-standard-4` machine.
Based on [GCE specs](https://cloud.google.com/compute/docs/cpu-platforms),
this corresponds to 4 hardware hyper-threads on a Skylake-based Intel Xeon Processor.
The machine had 15 GB of RAM, and used the following Apache config (added to
`/etc/apache2/apache2.conf`).

```
<IfModule mpm_event_module>
    StartServers 10
    ServerLimit 110
    MinSpareThreads 25
    MaxSpareThreads 75
    MaxRequestWorkers 1000
    ThreadsPerChild 5
    AsyncRequestWorkerFactor 2
</IfModule>
```

**StartServers** is the number of processes to start. It should satisfy
`MinSpareThreads < StartServers * ThreadsPerChild < MaxSpareThreads`.

**ServerLimit** is the maximum number of processes to start. It should satisfy
`ServerLimit * ThreadsPerChild > MaxRequestWorkers`. (This isn't true for
our config because of a config error.)

**MinSpareThreads** and **MaxSpareThreads** and the number of spare threads
to prepare for new incoming connections. We didn't change this.

**MaxRequestWorkers** is the maximum number of threads (requests) you want your server
to support. Any requests over this limit will be blocked, until existing
requests are fulfilled.

**ThreadsPerChild** is the number of threads to spawn per process. Most
configurations online use `ThreadsPerChild 25`. We found using more processes
and fewer threads per process made our site load a bit faster, at the
cost of more CPU usage and RAM usage. Using `ThreadsPerChild 25` is probably
good enough for you.

We're not sure what **AsyncRequestWorkerFactor** is, but all the recommendations
we found online recommended keeping it at the default of 2.


Caching
-----------------------------------------------------------------------------

Adding caching to your website can heavily speed up its performance. However,
it also opens your site to caching errors, which can be extra dangerous when
you're trying to add errata to a puzzle. We decided not to use any caching.


Static Conversion
----------------------------------------------------------------------------

As mentioned earlier, running Puzzles are Magic in maintenance mode currently
costs about $16/month. For archiving purposes, sometime after the hunt, you'll
want to convert your website into a static resource. This brings your maintenance
costs to almost zero. Amazon S3 costs just a few cents per GB of storage and
data transfer, and Github Pages lets you host a static site for free.

We're in the middle of converting Puzzles are Magic into a static website. The
main blocker is the interactive puzzles. All the core logic for these puzzles
is server side, and we need to port all the server-side logic into client-side
Javascript before we can flip the switch.

If you have a lot of interactive puzzles, or you are hosting from a personal
server, or you'd rather pay the server costs instead of spending time doing the
static conversion, you can skip this step.
