---
layout: post
title:  "\"How Do You Feel About Grad School?\""
date:   2015-09-28 23:14:00 -0800
---

Foreword
------------------------------------------------------------------
As of the time I'm writing this, I've never been a full time software developer
and I've never been a full time researcher. It's possible my perspective is
warped. If you feel parts of this are inaccurate or exaggerated, it's a feature,
not a bug.

This is how I feel about things as a graduating senior. The beauty of opinions
is that I make no claim to be right, and you're under no obligation to agree with me.

How I Got To Where I Am Now
-----------------------------------------------------------------

**December 2015**

*I see you shiver with anticipation.*

It's not a good shiver. I need to send an email to the professor I'm doing
research with. You would think that after doing it so many times, it
wouldn't be so intimidating, but you would be wrong.


![PhD Comics Email](/public/grad-school-thoughts/phdcomicsemail.gif)
{: .centered }

From [PhD Comics](http://www.phdcomics.com/comics/archive.php?comicid=1047)
{: .centered }

Still, there's a reason this email is harder to write than most.
I take a deep breath, and start composing my thoughts.

> Subject: Not applying this year
>
> After thinking about things more, I'm not planning to apply to grad school
> this year. I'm going to try to explain my reasons...

\*\*\*
{: .centered }

Most friends at Berkeley were surprised I didn't apply to graduate school.
To many of them, it seemed patently obvious I was going to apply. I want to
explain why it wasn't so clear cut. Over the past few years, I've both been
100% sure I was going to apply and 100% sure I wasn't. Graph my motivation for
graduate school and you'll get out a sine wave.

First, I should explain why it looked like I was headed for grad school.
I don't like to brag about my academic accomplishments. It's both
pointless and not actually indicative of your social worth, intelligence, or
research ability.

Still, in this case it's relevant.
So, (breathes in), my transcript has more As than Bs. Some of those As are A+s.
I've taken four technicals every semester, which is more than the average (but
I know people who take more.)
I started taking graduate level courses in junior year, because the remaining
upper divisions didn't interest me enough. Meanwhile, I've also been doing
research since junior year, in the Robot Learning Lab at UC Berkeley.

Given just that information, it really, *really* looks like I'm an academic,
through and through.

That's what it looks like.

In reality, I'm not sure I am on. I never have been sure.

Getting good grades and taking challenging courses shows you have good work
ethic or good talent. They are signs you have the potential to be a
good researcher. They don't automatically make you one.

\*\*\*
{: .centered }

*Let's do the Time Warp again.*

**September 2014**

It's my first day in the lab, and I already feel like I don't belong.

I have no idea what I want to research. I
only asked for a research position because it's The Thing Students With
High GPA are supposed to do. At least I know why I'm here - I got the top score
on the AI final last semester. (Turns out when you have no research,
no relationships,
almost no extracurriculars, a barely functioning social life, and no side
projects, you can devote a lot of time to schoolwork. In retrospect, spending
15 hours optimizing a Pacman bot was a big waste of time.)

To help give me direction, I meet with a graduate student who will be my main
mentor from here on out. We introduce ourselves, and he starts proposing a few
topics that could be interesting.

At one point, he asks, "Have you heard of neural nets?"

"Nope," I reply. Interally, I think, *Remember to admit what you don't know.
That should be easy, you don't know anything yet.*

"Okay. The basic idea is to take your input features, apply a linear
transformation represented by a matrix, then apply a nonlinear function to that.
It turns out if you repeat this process several times, you can solve a wide
range of problems."

I follow this explanation (hooray!), but I have no idea why
this should even work. He admits the theory behind neural nets is a bit shaky,
but he points towards an execptionally cool result: [learning to play Atari
games purely from visual input](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf).

We talk a bit more, and although I don't make a decision on
what problem to research, I get a better idea of the available options.

I talk with another student to get an account on a lab machine.
Yay, I'm on the team!
I'm not sure where to start, but I know that when people do research, they write
papers, and other people read them. So I start there. For the next few days,
Google Scholar is my best friend.

As I read the literature and work through neural net tutorials, I overhear
some discussion.

"Hey, do you understand RNNs?"

"Kind of? I implemented one a while back for a NIPS paper."

"Okay, that's more than I've done. Mind helping me understand LSTMs?"

I don't understand a word of it, but I try not to let it discourage me.
It's my first week. There's no way I should know what they're talking about.

The same song and dance continues for the next two weeks. Eventually, I hit on
investigating Monte Carlo Tree Search.
My lectures are separated by 1-2 hour gaps, and I spend them doing research.
By which I mean reading
the simplest reference I can find, in a desperate bid to find something I
can even comprehend. I also go to weekly group meetings. Every presentation
loses me on literally the first slide, but there's free lunch, so I can't complain.

![PhD Comics Presentation](/public/grad-school-thoughts/phdcomicspresentation.gif)
{: .centered }

I'm the guy with the brown afro, except I'm not even a first year which makes it worse.
Source: [PhD Comics](http://www.phdcomics.com/comics/archive.php?comicid=719)
{: .centered }

In my first one-on-one meeting, I mention that my problem feels well-solved,
and my mentor has to gently
remind me that a paper doesn't make an idea valid. A paper means
exactly what it says; the method used works on exactly the experiments mentioned.
It may or may not work anywhere else. My faith in scientific studies
drops sharply. (It bottoms out a few weeks later, after reading
[The Control Group Is Out Of Control](http://slatestarcodex.com/2014/04/28/the-control-group-is-out-of-control/).)

Once I see papers as promising ideas instead of ground
truth, prior work doesn't intimidate me as much.
At the same time, there's still a vast ocean of prior work, and I can barely
keep myself afloat.

It takes me two weeks to write my first line of code.
Reading papers isn't enough. I need to implement something to actually understand
what it does.

It takes me another week to get my code to work.

Then, one more week to understand why it works at all.

\*\*\*
{: .centered }

No one, not even the most brilliantly arrogant people I know, has ever said
research is easy. Professors talk about the long hours, 60 to 80 hour work weeks,
and for most of the time you're stuck on a problem. Of course, you're
not really stuck, because by failing so many times, you learn when an approach
doesn't work. Still, it can be hard to see the upside when you have no positive
results.

This makes scientific research a fundamentally different problem from homework.
The nicest quote explaining this is from the book "Countdown", describing
a speech Andrew Wiles gave at the International Math Olympiad.

> Solving Olympiad problems is not like doing mathematical research and is not
> necessarily the best training for research. Working at the mathematical
> frontiers is more like a marathon than a sprint. Problems can take many years to solve,
> and you never know for sure whether you're going to make the finish line. "The
> transition from a sprint to a marathon requires a new kind of stamina and a
> profoundly different test of character," he said. "We admire someone who can win
> a gold medla in four successive Olympic Games, not so much for the raw talent
> as for the strength of will and determinatino to purse a goal over such a
> sustained period of time. [...] You can forget the idea, if you ever had it,
> that all you require is a bit of natural genius and that then you can wait for
> inspiration to strike."

I read "Countdown" in high school, but the sheer difficulty of research
still blindsided me. It led to me not doing as much research as I should have.
Given a choice between a two hour homework problem and a two month
research problem, it was a lot easier for me to choose the former.

\*\*\*
{: .centered }

**October 2014**

An interesting idea pops into my head. I do a literature check, and find
my exact idea in a paper from seven years ago.

It's a bittersweet finding, but I'm still proud of myself.
Another researcher had the same idea, and they got a paper out of it!
Maybe I'm not a fraud after all. And, I see some interesting extensions that
aren't mentioned in the literature.

For the next week, I'm riding a high of accomplishment, making steady progress
on an implementation.
Then, it all goes wrong. My classes all ramp up at the same time.
I spend my days in lecture and my nights doing homework and projects. Resarch
goes on the back burner. I'm sorry! I don't have time for you! I need to learn
about thread schedulers, about clopen sets and Jacobians, and you need to wait.
You have to wait for me. Please.

No amount of pleading can change the facts: by my next one-on-one, I've done
literally no research. I sheepishly try to cobble something together in time
for my meeting, but I can't do much with no new ideas and no new code. (Besides,
grad students are the sharpest bullshit detectors I know. It comes with the
territory.)

In my meeting, I hear disappointment in his words, but I can't
tell if he's actually disappointed or if I'm reading self-loathing
because that's what I want to hear. I finally have free time that afternoon,
but I go home instead. I'm in too bad a mood to do any work.

Instead of meeting up with friends, I lie on my bed
and stare at the ceiling, thoughts swirling in my head.

*You're pushing yourself too hard. You need to slow down.*

*Or maybe*, says another voice, *maybe you weren't pushing yourself enough,
and now you are. Do you believe in growth through adversity or not?*

*I do. I really do. That doesn't mean I can't push myself too much.*

\*\*\*
{: .centered }

Graduate school demands you to be excellent.

Although anybody can apply for graduate school, not everybody can get in.
As I understand it, these are the implicit requirements for top
CS graduate schools.

- A high GPA. It doesn't have to be perfect, a 3.5 GPA won't raise any
questions and anything above it is at best a small bonus.
- Prior research with a professor. If you do not have this, you will 100% not
get in. In the best case, your research leads to
a publication, but depending on the subfield this is not required.
If you're applying for AI or machine learning, the standards are much higher
because so many (almost 50%) of applicants try for these fields.
One publication or one paper under review is almost expected.
- Three letters of recommendation.
A common mix is a strong letter from your PI, an okay letter from the course
you TAed, and a weak letter from the course you did well in. Again, stronger
applicants will have two research letters, or maybe even three.

(Based on [these two](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf)
[sources](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf).)

This is an incredibly demanding funnel. First, only the strong CS students
will even meet these qualifications. They apply,
the truly excellent ones (or the lucky ones) (or actually, both) get accepted,
and they start a PhD. About 14% of Berkeley CS undergrads go to graduate school,
including masters programs, and I'd say it's reasonable to say that is actually
the top 14% of the major.

A quarter of incoming PhD students will drop out of the program. (This is the
estimated CMU drop out rate, circa 2014.)

You need incredible talent and dedication to even get into a program as good
as CMU, to make it through the application filter, and a quarter of them
won't finish.

People call academia an ivory tower, but if anything it's an ivory spire.
The top high schoolers are average undergrads.
The top undergrads are average graduate students.
The top graduate students are average professors, and getting a tenure-track
position in the first place is hard. Then you need to lobby for tenure,
then you need to compete for grant money, and it keeps going. There is no top
to the spire, because the people who make it high enough have become so
enlightened that they recognize the top *doesn't actually exist.* It's an
illusion that distracts you from actually doing research.

It takes a very confident person to believe they can make it all the way
up the spire. It takes a very dedicated person to actually do so.

These are both awful realizations if you have imposter syndrome like I do.

Off the top of my head, I can name several people smarter than me. (I met
them in high school, and they've been better han me since.) I can name
a few undergrads with first author publications. (They work in the same
lab I do, but they've worked longer and harder than I have.) It's to the point
where I base my self worth not on where I am in relation to others, but on where
I am in relation to my own standards, because relative ranking will only leave
you disappointed. Not everybody can be Elon Musk. That's not saying I do this
successfully, but I try.

The point is that when I surround myself with people better than me, I lose the
ability to rank myself. Am I doing well in the Berkeley CS program? Yes.
Objectively, I'm doing very well. Subjectively, I still feel like an idiot who
spends way too much time doing who knows what.

\*\*\*
{: .centered }

**January 2015**

New semester, same problems. Four more technical classes to juggle, and more
deadlock in my research. Four classes is pushing it if I want to do good
research, but I love my classes too much to drop any of them.
Does learning Kolmogorov complexity help my research? No. Absolutely not.
Proving the existence of incompressible strings is still super awesome.

I put in hours where I can, but my schedule is busy, and once again I can't
put in as many as I'd like. Still, I have some interesting results, showing
that with enough training time (on the order of running it overnight)
I can get a program to self-learn heuristics for playing Connect Four.
It's not amazing, but I have trouble beating it, so it's at least okay.

However, the approach I'm trying fundamentally requires lots of computation
time, and running experiments is becoming infeasible. I can't make more progress
until I find a way to make my experiments run faster.

These are the thoughts in the back of my head, while I wait in line for free
food. At Berkeley, the demand for CS internships is so high that companies
give free dinner, T-shirts, stickers, and other free stuff at their info sessions.
It's pocket change for them, and hungry CS students are totally okay with the
bait. I'm waiting with a few other people from the CS honor societies. Some
are 100% doing grad school, some are 100% not doing grad school. A few are on
the fence, like me.

"What are we even doing with our lives? Is waiting in line for 20 minutes really
worth it for free food?"

"Well, I'm here to get used to the grad student life. Why are you here, Mister
I Already Accepted A Full Time Offer In Industry?"

"You know, I don't really know. Force of habit, I guess."

We laugh, and no one acknowledges the financial commentary. We all
already know it's true, and it doesn't need repeating.

\*\*\*
{: .centered }

Let's talk about the elephant in the room: the money.

The software industry pays stupidly well. Based on Berkeley Career Center
surveys, the average salary for an EECS student in 2014 was $108,000.
For a company in Silicon Valley, this actually is not that surprising, but if
that salary for new grads doesn't seem slightly insane, you need to recalibrate
what you know about money.

That's not even getting into the perks. Companies like Google, Facebook, and
LinkedIn sell themselves by offering insane perks.
Free lunch, free dinner, we have a ball pit on campus, we have massagers on campus.
We built a slide from the 2nd floor of the building to the ground floor, because
it helps express our inner child. You'll never go hungry, you'll never go
thirsty, and by the way we have some interesting problems that need solving,
so why don't you join us?

Alternatively, new grads can work at a startup. Come here, and you can change
the world! Or, you can exploit a temporary inefficiency of the market and be the
first one to solve it. We're changing how people connect with each other.
We're changing transportation. Join now, and if we make it big you'll make it
out like a king.

How does a computer science PhD program compete with that? It sells itself
with research. In a PhD program, you will tackle the hardest problems,
the ones where no one knows the answer. You will devote the next few years
towards learning as much as you want in your quest to solve one of those problems.
It will be hard, difficult, and poorly paid, but in the end you will learn
what it feels like to truly know something.

If you're looking for money, grad school isn't for you. As said by (CITE),
getting a PhD will cost you about a house.

If you want to coast through life with a reasonable living salary, grad school
isn't for you. You'll live, but you'll live cheaply, and it certainly won't be
easy.

The only valid reason to go to CS grad school is because you want to do research.
You need a fiery passion for your subject, a deep-seated curiousity that will
keep you motivated and up at night. AS (CITE) puts it, a PhD is designed to
break your will and test your faith.

Money isn't my biggest decision factor. Of course, I'll gladly negotiate for
more money if I can, but in the end I care more about self-satisfication
and impact.

In many respects, going for a PhD is like starting a startup. Both demand
dedication. Both end up becoming your life. It takes around 5 years to get a
PhD, and it can take 5 years for people to even learn about your startup. They
demand a similar skillset, and I suspect there's a big overlap between
people with or considering PhDs and startup founders.

If a startup is a bet against the world that you can build something useful,
then a PhD is a bet against the world that you can discover something that
no one has ever seen before.

However, there definitely are differences.
Paul Graham says everybody should try founding a startup.
No one says everybody should try getting a PhD.

\*\*\*
{: .centered }

**September 2015**

I chose to do an internship instead of research the summer before senior year.
I was a bit disillusioned with research after running into so many road blocks,
and didn't feel like I was self-motivated enough to try for a PhD program.

It was [a good experience]({% post_url 2015-08-20-things-i-did-in-my-khan-academy-internship %}),
and overall I'm very glad I decided to take the offer.
At the same time, as the semester started, I found myself enjoying research
a lot more. Maybe it was the light course load in the first few weeks, or maybe
it was the realization that I actually knew something, and could hold a
conversation with the grad student mentoring me. At least, for a while.

Riding the peak of research motivation, I set up meetings with my PI to find
a way to get a reasonable application in time for deadlines. I get started on
a new project, one that could lead to a paper faster than my old one.
(Later, I read a paper where the authors independently discovered the same
ideas I did, released just last year.
They ran into the same computational barrier, and got over it by throwing
more computing power at the problem instead of thinking of algorithmic
improvements. I feel a bit cheated, but at least it means I was on the right
track.)

There's an undercurrent of satisfaction to my life, but it's buried beneath
the weariness of living a life between problem sets. I get more research done
than last semester, but it still doesn't feel like enough.

It's Friday.

Friday, Friday, gotta get down on Friday.

Oh wait, no I can't. This needs to be done *now*. In fact, it needed to be done
two days ago.

So begins the story of how I spent a Friday night in the lab. Could have been
playing board games with friends. Could have been relaxing at home. Nope, lab.
Lab lab lab.

The lab is understandably quiet. No one wants to work on Friday night. I'm not
here by choice, and neither are they.

I finish dinner and start working by 8 PM. Five hours later, it's done. Not well,
not prettily, but good enough, and it's not worth staying later.

As I walk out, I think, *Wow, done by 1 AM. That's actually not so bad.* It's a
bit depressing that I'm serious about this.

Out of curiosity, I do one circuit of the lab, and one other person is still
spending their Friday night (now Saturday morning) doing work.

\*\*\*
{: .centered }

By this semester, I know what research is like. I have full-time job offers
that I can take if I want. If I wanted to relax and do nothing this semester,
I could.

So of course, I signed up for three grad classes, TAed for the first time, and
did a research appointment on top of it. At some point in high school, I gained
a deep unease with myself that pushes me to do more. Appeasing that part of
myself while making sure I don't overload has been one of the harder parts of
my life.

I definitely have a big self-deprecation complex. On one hand, it's probably
a net positive for success, especially success in research. Without natural
curiosity, there's no way I could deal with academia, because the only reason
anyone would choose the academia life is because they wanted it. (There are
exceptions, like international students who need to keep student status for
their visas, but often they like research as well.)

To say there's angst in academia is an understatement. For graduate school,
you don't need to look very hard to find black humor and horror stories.
I've already linked lots of PhD Comics. All the things you see in PhD Comics?
It's real. A bit exaggerated, and different people run into different troubles,
but it happens.

Not a fan of comics? Okay, why don't you read
[The Ph.D. Grind](http://pgbovine.net/PhD-memoir.htm) by Philip Guo? It's a
detailed account of the author's experience getting a PhD at Stanford, and I
consider it required reading if you're considering a PhD. More than
anything else, it conveys how soul-crushing academia can be. (That's not to say
his experience was common. In retrospect, [he says he was a 30th percentile
in happiness at Stanford](http://pgbovine.net/PhD-interview-eugene-wu-keith-winstein.htm),
but also said it could have been even harder if he was at a weaker school.)

Stories about the malaise in academia are all over the place. There is sampling
bias, where only the more extreme opinions get told, but it's a bit worrying
when finding doom and gloom stories is so much easier than finding the
sunshine and rainbows stories.

> "You make time for hobbies," she told me. "This isn't undergrad anymore.
> This is the rest of your life."

[Source (need Quora account)](http://qr.ae/RgsIFA)

> Look, I am in fact a career academic. I know exactly what's attractive about it, I've made considerable financial and personal sacrifices to get myself to a position where I can work in a university environment and spend my time doing groundbreaking research. And yet. The gateway into this life is a PhD, and the PhD system is deeply, deeply fucked up when it isn't actively abusive. **Doing a PhD will break you.** It's pretty much designed to break you. Yes, even you, you who are brilliant (that almost goes without saying; it's because you're brilliant that you're contemplating doing a PhD in the first place). You who are resilient and have survived several kinds of shit that life has thrown at you just to get to the point where you're about to graduate with a brilliant degree. You who have the unconditional support of your family and friends and partners. If you have every admirable personal quality you can think of, if you have every advantage in life, still, getting through a PhD will grind you down, will come terrifyingly close to killing your soul and might well succeed. It will do horrible things to your mental and physical health and test to breaking point every significant relationship in your life. 

[Source](https://liv.dreamwidth.org/389934.html)

![PhD Comics Cancer](/public/grad-school-thoughts/phdcancer.gif)
{: .centered }

[Excerpt of this comic](http://www.phdcomics.com/comics/archive.php/archive.php?comicid=1162)
{: .centered }

> A 2015 study at the University of California Berkeley found that 47% of graduate students suffer from depression, following a previous 2005 study that showed 10% had contemplated suicide. A 2003 Australian study found that that the rate of mental illness in academic staff was three to four times higher than in the general population, according to a New Scientist article.

[Source](http://qz.com/547641/theres-an-awful-cost-to-getting-a-phd-that-no-one-talks-about/)

So, if it's so bad, why is choosing not to go to grad school such a hard decision?

It's because some people care deeply about research. they care about it enough
to accept the hardships that comes with the PhD. There's an old saying: if you
could be happy anywhere else, don't go into academia. Some people can't be happy
anywhere else. It is what it is.

(Philip Guo calls this [a unicorn job](http://pgbovine.net/unicorn-jobs.htm). It's
a job where you put up with lots of stress for that 10% or 20% of the job you
actually want to do, because you enjoy it that much.)

It feels like I fall right on the boundary between the two.
A lot of sections from The PhD Grind resonated with me, but my favorite was
this one.

> I discovered over the past 5 years that I love being a spectator of
> research, but the burden of being a continual producer of new research is
> just too great for me.

When I don't do research for a while, I miss the feeling that I'm in touch with
the cutting-edge and directly playing a hand in shaping the future. (In AI too!
Holy shit, I get to experiment with algorithms for computer learning, how awesome
is that opportunity?) When I do research for longer, I realize how much of a
novice I am and how ridiculous it is to believe I can personally make a key
contribution to the field. (Oh jeez, so many subfields, so many subsubfields,
papers and papers and papers and which ones are even worth reading?)

One time, [Andrew Ng](http://www.andrewng.org/), one of the biggest names
in machine learning, came to give a talk on the deep learning work he did at
Baidu. Every talk on deep learning gets a packed auditorium. A talk on deep
learning by Andrew Ng? It was packed 15 minutes before it started.

He gave a broad overview of the current research trend towards bigger models
and bigger datasets, then talked about his work developing smart assistants
like the Baidu Eye. The way he talked about it, you could tell this wasn't
just something he worked on, it was something he *believed* in. They were
his vision of the future, and he was there to play a part in making it real.

Another day, I was in the lab, and overheard a conversation between a visiting
postdoc and a graduate student. They started talking about PhD Comics, and
the postdoc said she could never relate to the comic. She was always a happy
grad student.

Passion and faith in your work is what will carry you through a PhD.
Nothing else will.

It was a high bar, and I wasn't sure enough in myself to say I crossed it.
As the months passed by, I realized I had made my decision a long time
ago. I was just too worried to say it out loud.

\*\*\*
{: .centered }

*I've given a lot of thought to how I wanted to express how I feel about
grad school, but in the end I decided it would be simpler to include my
email in full.*

**December 2015**

I take a deep breath, and start composing my thoughts.

> After thinking about things more, I'm not planning to apply to grad school this year. I'm going to try to explain my reasons.
> 
> - I haven't been researching faculty at any schools I might be applying to. Given that some of the deadlines are Dec 8th, that means I won't have a very polished application. But more importantly, I haven't had the motivation to work on applications. Of course, very few people look forward to writing applications, but people interested in grad school will usually have the motivation to trudge through it because they see it as necessary to get to where they want to go.
> 
> - I haven't notified people writing my letters of recommendation. Again, this isn't a deal breaker by itself, but it's certainly somewhat bad etiquette, and it goes back towards the idea of motivation. If I believed I wanted to apply this year I certainly would have notified faculty sooner.
> 
> - I talked with some other seniors/grad students, and the general consensus was that you should only go to grad school if you are very sure you want to go. If you're only somewhat interested, you should internally downgrade interest by a lot.
> 
> - Assuming I magically finished my application and got into a top graduate program, I'd still lean towards not going. After a PhD, I don't think I'd want to stay in academia, and would likely try to get into an industry lab. At that point, the PhD essentially becomes a 5-6 year long process of improving research skills enough to apply for those positions, which doesn't sound worth it to me.
> 
> To me, there are many reasons to go for a PhD, but I'm not completely sold on any of them:
> 
> - To prove to yourself / the world that you can get through a PhD program, because only a small percentage of people can do so. I don't a strong need to prove myself to be better than other people, and care more about my personal standards for how much I can push myself. (I suppose that could also be seen as an argument for why I should do a PhD, which is all about pushing boundaries.)
> 
> - A very strong belief that what you're doing your research in is important. Strong enough to deal with the stresses of academia, and solid enough to keep going even after realizing just how big your field is. I believe that AI research is very important and impactful, and enjoy reading about new advances, but the costs of creating new research are too high for me.
> 
> - A personal fulfillment achieved by understanding something very deeply. For theory-leaning people (which I'd classify myself as), this may also be the joy from finding an especially elegant proof or neat connection between different topics. This is definitely hard to find outside academia, but aspects of this still show up in industry, and being an expert on X is common advice for standing out among your peers.
> 
> - A love for teaching with the plan to go for a lecturer position after a PhD. I've liked TAing this semester and approve of education in general, but again this isn't a strong enough interest to make me want to teach full time.
> 
> The summary ends up being: I wasn't motivated to work on my applications. I took that as a sign that I wasn't as interested in a PhD as I was before. After asking myself a few things, I realized it was unlikely I would start a PhD even given a free entrance into a top program. None of these decisions depend on whether I'd be a good researcher or not, they all depend on whether I'm motivated to do research or not,
> 
> Maybe this is already clear, but *I'm not saying any of these beliefs are set in stone.* It is entirely possible that I'll change my mind about many of these things, However, my expectation is that my beliefs aren't going to change significantly by next year to make applying worth it. I still plan to do more research this week + finals week to set up opportunities for myself to gain motivation for research, but if they change enough to make me want to go to grad school I'll just have to wait a year on applications.
> 
> Alex
