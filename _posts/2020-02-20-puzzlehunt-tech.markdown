---
layout: post
title:  "A Puzzlehunt Tech Checklist"
date:   2020-02-20 03:10:00 -0500
---

I have played my fair share of online puzzlehunts, and now that I've
run a [puzzlehunt](https://www.puzzlesaremagic.com/) myself, I've learned
a lot of things about how to run a successful hunt.

There are several articles about puzzle design on the Internet, but as the
tech person for Puzzles are Magic, I haven't seen any articles about building
a hunt website.

This is a list of things I feel every hunt website should strive to achieve.
Not all of this is necessary, and we certainly didn't do all of this for
Puzzles are Magic, but I feel everything here is a worthy goal to aim for.

If you are reading this, I'm assuming that you know what puzzlehunts are, you've
done a few puzzlehunts yourself, and are either interested in running an online
puzzlehunt, or are interested in what the tech process looks like.


Hunts are Web Apps
------------------------------------------------------------------------------

The most important thing to remember about a puzzlehunt is that a puzzlehunt is
essentially a full web application.
There's a frontend that solvers interact with, there's a backend
that stores submission and solve info, and the two need to send the right
information to each other for your hunt to work.

That means if you want to run an online puzzlehunt with teams, leaderboards,
and so on, you'll either need to know how to set up a website, or be eager to
learn. If you have practice with looking up how to use unfamiliar software
libraries, you should be set.

If you don't know how to program, and can't enlist the help of someone who can,
then your job will get a lot harder, but it won't be impossible. Remember that
if worst comes to worst, you can always just release a batch of PDFs online,
instead of building an entire website.


Using Existing Code
------------------------------------------------------------------------------

Puzzlehunt coding is like video game coding.
It starts sane and well-designed, and becomes increasingly
hacky as you get closer to the hunt deadline. This is especially true if the
hunt has interactive puzzles. In the end, functionality matters
more than code quality, and since hunts are one-time events, there usually
isn't much incentive to invest in clean code.

Expect people to be hesitant about sharing their puzzlehunt code. Or at least,
I'm hesitant to share *my* puzzlehunt code.
I'm happy with the core, but there are a ton of hardcoded puzzle IDs and other
things to make the hunt work as intended. I've considered releasing the code
as-is, warts and all, but even then I'd need to audit the code to verify I'm
not leaking any hardcoded passwords, secret keys, user data, puzzle ideas
I want to use again, and so on.

As far as I know, the only open-source puzzlehunt codebase is
Puzzlehunt CMU's
codebase, which can be found at [this GitHub](https://github.com/dlareau/puzzlehunt_server).
Our hunt code is forked from this code, with several modifications. It's written
in Django
Our hunt was written in Django and served using Apache. Using Django + Apache isn't required,
but both libraries are free, very widely used, and very well tested, so they're
solid picks.

Whether you start from scratch or start from an existing codebase, expect to
make changes to the code to support your needs.


Authentication
------------------------------------------------------------------------------

You will need to decide whether you want logins to be person-based, or team-based.

In a person-based setup, each person makes their own account. People can create
teams, or join existing teams by entering that team's randomly generated hunt code. Puzzlehunt CMU's code does this,
as did Microsoft College Puzzle Challenge. The pro is that you get much
more accurate estimates of how many people have registered. Both Puzzlehunt
CMU and Microsoft CPC are on-campus events where the organizers provide free
food, and they need to know how much food to order. The con is that by requiring
every solver to make an account, you increase friction at registration time.
Everyone on a team must make an account to participate, and anyone the team
wants to recruit during hunt must do the same thing.
Also, some people are generally
wary of entering emails and passwords into an unfamiliar website.

In a team-based setup, each team has a single account. There is a shared username
and password, chosen by the person who creates the team, and their email is the
main point of contact. They share the team's login credentials around, and team
members can optionally add their names and emails on that team's profile page.
This is the setup used by MIT Mystery Hunt, Galactic Puzzle Hunt, and Puzzles
are Magic.

The downside of person-based logins is that they add friction for pick-up
solvers. Every one of those pick-up solvers will need to fill out
your site's registration form before they get to see any puzzles. If you want
as many people as possible to look at your puzzles, this is bad.

For most online hunts, I would recommend team-based logins over person-based
logins. If your goal is to get as many people to look at your puzzles as possible,
you should minimize friction at registration time. I feel this is worth
the trade-off of inaccurate participant counts, but it's up to you. (Based
on survey feedback, only 50-75% of people who played Puzzles are Magic entered
their personal information into the site.)

Whatever login setup you go for, make sure you support the following:

* Unicode in team names and person names. I'd go as far as saying this is
non-negotiable. Several teams have emoji as part of their team culture, and
sometimes you will get teams who use languages besides English.
Puzzles are Magic got a few sign-ups from the Chinese MLP scene (we're
not sure how), and Unicode gave us free Chinese character
support.
* Password resets. People forget their password. It happens. This is especially
important if your site uses a team-based login. Lots of people sign up without
realizing they're creating an account for their entire team.
* HTTPS. There's really no excuse to not use HTTPS.
You may think
that no one will try to hack your puzzlehunt website. You'll be correct.
However, people reuse passwords when they shouldn't, and you don't want
packet sniffers to discover any re-used passwords.
Just use HTTPS. If you don't, people will complain, and I will be one of them.
[Let's Encrypt](https://letsencrypt.org/)
is a free certificate signing authority you can use for this.


Admin Sites
----------------------------------------------------------------------------

Not everyone working on your Hunt will know how to program or interface
with a database, and even those that do may not want to pull out a computer
terminal every time they want to change something.
You'll want admin sites that let you directly modify
your database from a web interface.

Django has a default admin site, and Puzzlehunt CMU's code comes with
custom add-ons to this site. We found they covered 90% of our use cases.

Some things we did through the admin site were: fixing typos in team names,
deleting duplicate teams created by people who registered twice,
and modifying answer checker replies on-the-fly when a 3rd-party site our hunt
relied on went down. We also had live-updating team progress pages and
submission queues, taken from the CMU code, which we used with few changes.


Unlock System
----------------------------------------------------------------------------

In an Australian style hunt, puzzles are unlocked at a fixed time each day,
with hints releasing over time. In a Mystery Hunt style hunt, puzzles are
unlocked based on previoiusly solved puzzles, potentially with time unlocks
as well.

Supporting both time unlocks and unlocks based on solving K out of N
input puzzles is enough to cover both cases. You'll also want the ability to
manually unlock puzzles, to help teams that need more help.


Answer Submission and Replies
----------------------------------------------------------------------------

Unless you expect and want to have someone awake 24/7 during Hunt, you'll
want an automatic answer checking system.

For guess limits, you can either give each team a limited number of guesses
per puzzle, or you can give unlimited guesses with rate limiting. Both are
valid choices. Whatever you do, please, please don't make your answer
checker case-sensitive, and have it strip excess characters before
checking for correctness.

Whether you want to confirm partials or not is up to you, but even
if you don't, it's good to support replies
besides just "correct"
and "incorrect". Supporting custom replies opens up new puzzle design
space.
Example puzzles that rely on custom replies are
[Art of the Dress](https://www.puzzlesaremagic.com/puzzle/art-of-the-dress/)
from Puzzles are Magic, and [The Answer to This Puzzle Is...](https://2018.galacticpuzzlehunt.com/puzzle/the-answer-to-this-puzzle-is.html) from GPH 2018.

Note that if you decide to confirm partials, you'll encourage teams to guess
more, and you should make sure you aren't unduly punishing teams for trying to
check their work.

Submissions should be tagged with the team that submitted them, and what time
they did so, since this will let you reconstruct team progress and
submission statistics after-the-fact.


Errata
----------------------------------------------------------------------------

Everyone tries to make a puzzlehunt without errata, but very few people succeed.
Make sure
you have a page that lists all errata you've issued so far, including
the time that errata came out, and have the errata visible from the puzzle
page as well.

If you are building an MIT Mystery Hunt style puzzlehunt, where different
teams have different puzzles unlocked,
your errata should only be visible to teams that have unlocked the puzzle
it corresponds to.

When you issue errata, you'll want to notify teams, which brings me to...


Email
---------------------------------------------------------------------------

If you have fewer than 100 participants, you can get away with emailing everyone
at once, putting their emails into the BCC field.
Above 100 participants, you'll want an email system.

Puzzles are Magic used Django's built in email system. Whenever we
emailed people, we generated a list of emails, split them into chunks of
80 emails each, then sent emails with a 20 second wait time between each
email send. Without the wait time, we found Gmail refused to send our
emails, likely because of a spam filter.

As of this writing, we had to turn off a few security settings and manually
unlock a CAPTCHA to get Gmail to be okay with Django sending emails from
our hunt Gmail address. None of this was necessary to send emails from the
hunt Gmail to itself, so it took us a long time to discover our email setup
was broken. Make sure you check with an external email!

Because of issues like that, you may want to integrate a dedicated mailing
service, like SendGrid or MailChimp, which will deal with this nonsense
for you. I haven't checked how hard that would be.

You'll want the ability to email everyone (for hunt wide announcements),
everyone on a specific team (if you want to talk to that team), and everyone
who has unlocked but not solved a specific puzzle (to notify for errata).
You may also want the ability to email everyone who hasn't reached a certain
point in the hunt, if you want to talk to less competitive teams.


Puzzle Format
-----------------------------------------------------------------------------

For puzzles, you can either go for a PDF-by-default format, or HTML-by-default
format.

The upside of PDF-by-default is that you can usually assume PDFs will appear
the same to all users. You don't have to worry about different browsers or
operating systems messing up the layout of your puzzle.

Browser compatability is a huge pain, but if you're running an online hunt,
I still advocate for an HTML-by-default puzzlehunt. It requires more work,
but comes with these advantages.

* You can more easily support "online-only" experiences, like music puzzles
and interactive puzzles. In my opinion, if you're making an online hunt,
you should create something that only works online, to differentiate it from
in-person events.
* You reduce the number of clicks between a solver and the puzzle. (Click link,
see puzzle, vs click link, click download, open download, see puzzle.)
* If you have several constructors, it's easier to force consistent fonts and
styles across puzzles, by using a global CSS file.
With PDFs, you need to standardize this yourself.
* HTML pages are inherentently redownloaded whenever a solver refreshes or
reopns the page. That means if you issue errata, solvers will notice your
errata faster than if it's part of a PDF they have to re-download. It's also
possible solvers will accidentally look at their old downloaded PDF, instead of
the new PDF.

In total, I believe these benefits are worth the extra work required.
Of course, you should use PDFs in cases where doing so is easier.
There was no way [A to Zecora](https://www.puzzlesaremagic.com/puzzle/a-to-zecora/) was ever
going to be in an HTML format, and puzzles based on precise alignment of text
are much easier to test in a PDF format.

If you plan to have your puzzles be HTML-by-default, you'll want to have
tools that make HTML conversion easier. It's possible to manually write HTML, but
it's incredibly tedious.
I personally like Markdown, since it's lightweight, builds directly to HTML,
and you can add raw HTML if you need to support something special.

This is off topic, but if you know how, I highly, highly, highly recommend
writing scripts that automate converting puzzle data into HTML
Doing so reduces typo risk, and makes it easier
to update a puzzle based on testsolver feedback. For Puzzles are Magic, when
constructing
[Recommendations](https://www.puzzlesaremagic.com/puzzle/recommendations/),
I wrote
a script that took a target cluephrase, and auto-generated extraction indices
that gave that cluephrase by taking 1 letter from every clue in a list. That
script saved a bunch of time,
since we ended up changing the cluephrase and songs used
3 times, including the night before Hunt.


Access Control
------------------------------------------------------------------------------

Teams should not have access to a puzzle before they have unlocked it.
This is obvious, but what's less obvious is that they also shouldn't
have access to any static resources that puzzle uses. Any puzzle specific
images, Javascript, CSS, PDFs, and so on should be blocked behind a check of
whether the team has unlocked that puzzle yet.

Assume that solvers will find any file that isn't gated behind one of these
unlock checks, and check whether doing so would break anything about your
hunt.

The 100% foolproof way to avoid puzzle leaks is to only put the puzzle into
the website right before it would unlock. This works for Australian-style
hunts, where puzzles are unlocked on a fixed schedule.
However, for testsolving, you'll want to have testsolvers use your hunt
website. So, you'll want the puzzles to be in your website, with access control
to restrict them to playtesters.
And if you're going to support that, then you might
as well put the entire hunt into the website, so that time unlocks run
automatically.


File Metadata
------------------------------------------------------------------------------

There are many ways your puzzle can have side channels that leak information
you may not want to leak. For example, the puzzle
[Wanted: Gangs of Six]( https://pennypark.fun/puzzle/wanted_gangs/) involved
identifying gangs of six characters from several series, extracting
cluephrases using numbers written in fonts matching each series. The solution
mentions that testsolvers were able to extract the font names from the PDF
properties, and many of the font names were named after the series they were
taken from.
The final puzzle uses remastered fonts with less spoiler-y names.
As another example,
for [A Noteworthy Puzzle](https://www.mumspuzzlehunt.com/solution/III/2/)
from the 2019 MUMS Puzzle Hunt, the original sheet music and color names could
be retrieved from inspecting the PDF file.

Audio files come with album and artist metadata. Make sure you clear them.
PDF files can have metadata too. Inspect them and make sure it doesn't leak
anything you don't want to leak.

Note that "side channel" implies you don't want puzzle info to leak this way.
Sometimes, leaking info this way is okay. In
[Tree Ring Circus](http://www.mit.edu/~puzzle/2019/puzzle/tree_ring_circus.html)
from MIT Mystery Hunt 2019, you needed to find the diameters of each circle to
solve the puzzle, based on a given scale. The circles were drawn in SVG, and to aid solving, the
distances used in the SVG file exactly matched the distances needed to solve
the puzzle.


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

Again, like the file metadata mentioned above, sometimes leaking info in
filenames is okay.
An example puzzle that does this is [p1ctures](http://web.mit.edu/puzzle/www/2015/puzzle/p1ctures/)
from MIT Mystery Hunt 2015. Yes, almost anything
can be part of a puzzle if you try hard enough.


Interactive Puzzles
------------------------------------------------------------------------------

Interactive puzzles are usually more work to make, but are also
often the most memorable or popular puzzles. (My
theory is that interactive puzzles naturally lead to emergent complexity,
and emergent complexity is the entire reason that people like solving
puzzles.)

The rule-of-thumb in online video games is
to never, ever trust the client. Puzzlehunts are the same.
In MIT Mystery Hunt 2020, teammate solved 2 or 3 interactive
puzzles by inspecting the client-side Javascript, finding a list of encrypted
strings, searching for the function that decrypted them, and running the
decryption until we found strings that looked like the answer.

Assume that teams will decode any local Javascript, even if you minify and
obfuscate it.
The only guaranteed way to close these shortcuts is to move all
key puzzle functionality to server-side code.
Server-side confirmation has higher latency than client-side confirmation,
so if you're worried about responsiveness,
only confirm the most important
parts of the puzzle on the server. The interactive puzzles for Puzzles are
Magic were essentially turn-based, so latency wasn't an issue, and we could
put everything on the server.

For example,
in [Applejack's Game](https://www.puzzlesaremagic.com/puzzle/applejacks-game/),
all the Javascript does is take the entered message, send it to the server,
and render the server's response. That's it. There's nothing useful to
retrieve from the client-side Javascript, and you need to interact with the
puzzle to discover its rules.

If possible, try to avoid repeating logic across the client and server. The
[GPH 2019 AMA](https://2019.galacticpuzzlehunt.com/wrapup/ama.html) mentions that
Peaches had a bug where client-side logic didn't match the server-side
verification, which caused some correct solutions to get marked as incorrect.

As mentioned in that AMA, if your server side validation fails, make sure to
give teams an obvious error, perhaps one that tells them to contact you so that
you learn about the problem.


Accessibility
-------------------------------------------------------------------------------

You can generally assume that most solvers will be on either Windows or Mac OS X,
they will normally use one of Chrome, Safari, or Firefox, and they'll be solving
from a laptop-sized or monitor-sized screen.

The key word here is *most*. Accessibility issues will always affect a minority
of your users, but there are a lot of minorities.
If you want more people to solve your puzzlehunt, you'll need to be inclusive
when possible.

Some of your solvers will be color blind. Some of your solvers will be *legally*
blind. Some
of your solvers will heavily prefer printing puzzles versus solving them
online. Of those solvers, not all of them will have access to color printers.

You may not be able to please all of these people. If your puzzle is based
on image identification, the legally blind solver is not going to be able to solve
it. You can't even provide alt text that describes the image, because non-blind
solvers will use the alt text as a side channel. But, try to do
the best you can. As mentioned from the 2019 MIT Mystery Hunt AMA,
["Keep in mind what the puzzle actually needs in terms of skills and abilities, and what you’re presuming the solver/s will have. Wherever there’s a mismatch, try to make the puzzle suit the smallest set of abilities without stomping on data the puzzle needs."](https://www.reddit.com/r/mysteryhunt/comments/am5s1d/were_setec_astronomy_and_we_just_ran_a_mystery/efjklm7/).

For color blind solvers, try to avoid colors that are too visually similar to
one another. If you need to use a large number of colors, consider providing
a color blind alternative.

For people who prefer printing puzzles, make sure that your puzzles print well.
By default, printers ignore all CSS, so by default, your puzzles probably
print poorly. You'll need to define [specific print CSS](https://www.smashingmagazine.com/2018/05/print-stylesheets-in-2018/)
files to get your puzzles to print correctly.

Some solvers will be solving from smartphones or tablets, rather
than desktops or laptops. It's okay if your site is worse from mobile, but
make sure your site isn't completely broken on mobile. Even solvers with laptops
will appreciate being able to solve puzzles on the go.

Watch out for slow Internet connections or computers. On
[Number Hunting](https://www.puzzlesaremagic.com/puzzle/number-hunting/),
we found the equations sometimes took a while to render. They also rendered
poorly on mobile, since MathJax doesn't support wrapping equations across lines.
For those reasons, we included a plaintext version as well, since the LaTeX
style rendering was just for flavor reasons.

A puzzle we could have done more on was
[The Key is Going Slow and Steady](https://www.puzzlesaremagic.com/puzzle/the-key-is-going-slow-and-steady/).
One lesson we learned during hunt construction was that puzzle presentation
really matters. If a puzzle looks big, it's intimidating, and solvers are
less likely to start it. So, if you can find a way to make a puzzle look
smaller, you should.
[Recommendations](https://www.puzzlesaremagic.com/puzzle/recommendations/)
testsolved a lot better when I made all the images 4x smaller, even though
this changed nothing about its difficulty.

For The Key is Going Slow and Steady, we used [Prezi](https://prezi.com)
to bundle the flowchart into a smaller space. The problem this
introduced from an accessibility standpoint is that Prezis load really,
really slowly, and they don't work on mobile.
Providing a lightweight alternative to the Prezi would have made the puzzle
cleaner, but we didn't have time.


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
autoscaling your site when you get more users.

Puzzles are Magic was hosted from a raw machine we purchased through Google
Compute Engine. We did this because it required the fewest changes from
the Puzzlehunt CMU code we started from, and we had some GCE free trial credit
to play with. Unfortunately, our free trial expired about
6 weeks before the hunt started.
We spent about $120 in total. Of that total, $80 was spent in the 4 weeks around
hunt, and $40 was spent in the remaining time.
We're currently spending about $16/month to run the hunt in maintenance mode.

Here's a chart for number of users per day, with annotations for key
dates.

![User chart](/public/puzzlehunt-tech/annotated_view_chart.png)
{: .centered }

User counts started increasingly rapidly the week before hunt, peaked the
first weekend, then decayed over time. Make sure you get a large enough
machine a few weeks *before* your hunt starts.

We load tested our website using [Locust](https://locust.io/). Our target was
supporting 750 active users using the site at the same time. We picked that
number based on registration counts leading up to hunt.

Make sure you test from a fast Internet connection, or split your load test
across a few networks! We had trouble getting more than 250 active users to work,
and eventually debugged it to load testing from a slow connection that had
trouble *pretending* to be 250 users. The
site was fine the entire time.

If your server is too busy to respond to solvers, it's also going to be
too busy to respond to your remote login attempts to fix it. Err on the
side of too large. The money is worth your mental health.


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

We're not sure what **AsyncRequestWorkerFactor** is, but all the guides
we found online recommended keeping it at the default of 2.


Caching
-----------------------------------------------------------------------------

Adding caching to your website can heavily speed up its performance. However,
it also opens your site to caching errors, which can be extra dangerous when
you're trying to add errata to a puzzle.

We tried to avoid caching, but part of our Apache config cached static
resources we didn't want to cache, and we were never able to debug how to
turn it off. That caching made one of our erratas take 5 minutes to propagate
to solvers. Luckily, the errata was minor.


Static Conversion
----------------------------------------------------------------------------

As mentioned earlier, running Puzzles are Magic in maintenance mode currently
costs about $16/month. For archiving purposes, sometime after the hunt, you'll
want to convert your website into a fully static site. This brings your maintenance
costs to almost zero. Amazon S3 costs just a few cents per GB of storage and
data transfer, and Github Pages lets you host a static site for free.

Try to have a static answer checker ready to go before hunt ends. Even if all
your solutions are ready the instant hunt ends, you want to give solvers the
ability to check their answers spoiler-free.

As for converting the rest of the site, well, that can take some time.
Remember how I said interactive puzzles should have all their logic be server-side?
Well, making them work client-side basically means rewriting all the code to
run in-browser.

If you'd rather pay the server costs than deal with these headaches, then
sure, leave the site as-is. Personally, I'd rather not pay $16/month for the
rest of my life, and when I find free time I'm going to start converting
everything.

For non-interactive puzzles, the command [mentioned here](https://www.linuxjournal.com/content/downloading-entire-web-site-wget)
seemed to work for me, but you should double check the links yourself, especially
if your paths include Unicode characters.
