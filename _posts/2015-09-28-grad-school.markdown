---
layout: post
title:  "\"How Do You Feel About Grad School?\""
date:   2015-09-28 23:14:00 -0800
---

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
> After giving it some thought, I'm not applying to graduate school this year.
> I want to explain why I made this choice...

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

I 
The blessing and curse of the Information Age is that if you want to
learn something, you can. Ever wondered what gerrymandering was? Here, go
to Wikipedia. What about World War II? Well, that's covered too, in volumes and
volumes of books, and also in a few comics, and also in an anime.

One day, I find out Orson Scott Card's political views clash with your own.
The work is divided from the author, but it slightly colors how you perceive
any novels he writes. The next, I read that if the US had invaded Cuba during the Cuban
Missile Crisis, Fidel Castro would have ordered a nuclear attack, even knowing
he would have died to the reply.

One day I binge read PhD Comics and The PhD Grind, and the bleak picture of
academia is exposed to my eyes for the first time.

When it comes to graduate school, you don't have to look very hard to find the
black humor. You also don't have to look very hard to find stories that are
dark with no laughs. Similar refrains come up.

> "I'm doing research in something that I can't even explain to people I know"
>
> "Here I am, stuck with no progress after five months,
> while my friends have jobs, families, and money."
>
> "Pulled an all-nighter for that paper deadline. Can't even crash the next day,
> too many other things to finish."

The PhD grind is especially effective in portraying the grinding conditions
the author went through. PhD Comics is hyperbolic for the sake of comedy,
but The PhD Grind is real. I consider it required material if you want to
learn what a PhD can really mean.

Together, they paint a gloomy picture of academia. In academia, you voluntarily
are taking low pay and long hours in the name of research. Or as said by
(CITE), "A PhD costs you around a house."

So, if it sounds so bad, why was choosing not to go to graduate school such a
hard decision?

Research can be depressing and relentless, but it's still science.


A lot of sections resonated with me, but my favorite was this one.

> I discovered over the past 5 years that I love being a spectator of
> research, but the burden of being a continual producer of new research is
> just too great for me.



That's the problem. That's the root cause of all my indecision. People take
a lot of technology for granted, but when I step back and take a look, **really**
take a look, it is completely baffling that we can do the things we can today.
Speech recognition went from garbage to in every smartphone. Image classification
went from a pipe dream to a reality that companies are fighting tooth and nail
over. The rate of progress is unbelieveable, and it seems like every 2-3 months
there's a new breakthrough that pushes the scope of human knowledge every
so slightly outward.

Then I sit down and try to do research, and make only incremental progress after
several months of work.

The machine of research is a beautiful piece of work, and it can be gratifying to
know you are literally building the future, but in the end you're still just
one cog in a mass of gears and wires.

\*\*\*
{: .centered }



