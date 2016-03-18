---
layout: post
title:  "AlphaGo vs Lee Sedol: Post Match Commentaries"
date:   2016-03-17 17:00:00 -0800
---

*During the [five game match between AlphaGo and Lee Sedol](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol),
I posted my thoughts after each game to Facebook. People seemed to like them, so
I'm collecting them here for posterity.*

*These are mostly unedited, because editing will bring in my unconscious
bias from knowing how the match ended up.*


Game 1
-------------------------

I'm reading reactions to AlphaGo winning the first game, seeing comments like "I missed my chance to bet on a 5-0 result", "Go is dead, RIP", "No wonder Stephen Hawking warned us about artificial intelligence", etc. And my gut reaction is, "Come on, yes it's amazing and historic that AlphaGo won, but it's 1 game, you can't extrapolate it to a 5-0, you can't extrapolate this to expecting AGI in a few years, that's still pretty far away, OMG IT'S NOT THE END TIMES YET STOP SAYING IT IS."

Then, I realized I had become one of THOSE people. Someone who's always exasperated at AI reporting because it's usually overloaded with biological connotations and simplified down to the point of deception. Someone who keeps hyping down AI progress because lots of people react very extremely to headlines when the reality is more nuanced.

In short, I'm matching the AI researcher stereotype. Andrew Ng sums it up best: his extreme optimism about the long term potential of AI is tempered by a relentless short term pessimism about current limitations.

So this time, I'm holding back the pessimism and trying to focus on the long term. I do think about AI displacing jobs, about AGI, about value alignment and AI risk. They're worth thinking about and talking about, even if they can lead to extreme predictions of the future that make me internally facepalm.

A Go robot beat a pro with no handicap for the first time ever. Even if AlphaGo loses the match 1-4, this is still a watershed moment. It's our generation's Kasparov vs Deep Blue, and that deserves all the hype it gets.

I'm rooting for AlphaGo all the way. If it wins, I don't even know what game's next. I was going to say Arimaa, but it turns out bots started beating humans last year, so that's out. Turn based perfect information games could actually be proclaimed dead in a few days, and that's very surprising.

But, they aren't dead yet. Four more games to go.

AlphaGo 1-0 Lee Sedol


Game 2
---------------------------

AlphaGo won again. A 5-0 isn't out of the question, and an overall win is likely - it's hard to see a world where Lee adapts enough to win the next three straight. I don't know anything about Go, but I can argue this for other reasons.

One thing mentioned as strange in the commentary was AlphaGo playing seemingly bad moves that gave up points. This ties back into how both Go and Chess AIs are designed.

A game AI maximizes its chance of victory at all costs. A game AI does not care about margins. It does not care about time used. Its one goal is to win the game. Everything else is meaningless.

When a game AI plays a move that gives up free points, there are two plausible hypotheses.

- The game tree search did not discover the move decreased win percentage, and the AI truly misplayed. Let's call this "I dun goofed".

- The game tree search discovered the move increased win percentage, despite losing some points. For example, playing that move forces a sequence of replies that reduces the overall uncertainty. Let's call this "consolidation".

If the AI wins in the end, you should be suspecting consolidation, especially if it does "mistakes" in the endgame. Game AIs are strongest in the endgame, don't assume they're suddenly messing up.
*(Editor's note: someone later convinced me this isn't true for all game AIs,
but it is true for Monte Carlo Tree Search AIs like AlphaGo.)*

In a comment thread on a Go enthusiast site, someone tried explaining this. "If AlphaGo sees a move that wins by 1 point 90% of the time, and a move that wins by 10 points 80% of the time, it will pick the former."

But that argument misses the point: AlphaGo DOES NOT EVEN KNOW THE POINT MARGIN EXISTS. All it sees is "win, loss, draw". IT ONLY SEES THE RESULT. First, win. There is no second goal.

AlphaGo doesn't see "90% chance win by 1 point, 80% chance win by 10 points". It sees "90% chance win, 80% chance win". When you look at a game that way, of course you'll pick the 90% win.

That's not saying AlphaGo ignores points. AlphaGo cares about them, but only as far as they help for winning. The point margins are already baked into its win percentage estimates. "How can I lose, and what can I do to stop that?" Look for answer, play move, repeat relentlessly. Over and over, until the other player has no hope.

People do this too. We're just a lot worse at it than computers are.

When we predict games, our predictions are fuzzy, and we know they are fuzzy. If our prediction is off by +/- 2, and the prediction is a 1 point victory, we're not going to go for a close game. If a human has a large point lead, they can afford more mistakes. I suspect that's the argument we use to argue for pursuing point leads. We want to give ourselves breathing room.

Game AIs don't have this problem, because after all their computation they have an exact quantification of their uncertainty, and they will trust that computation, blindly and absolutely.

This all builds to the key reason I think an AlphaGo 5-0 could happen. In the endgame, many moves before the resignation, AlphaGo made a move that many commentators called a mistake. It gave up some free points. **That's not a mistake, it's consolidation.** If AlphaGo needed those points, it wouldn't toss them away. But, it decided that losing those points for sure was better than the chance of losing even more if it fought over them. Here, win the battle! I've still got the war.

If a game AI is fighting tooth-and-nail to the end, that's good news for you. If it starts playing loose? Be afraid. Be very afraid.

AlphaGo 2-0 Lee Sedol


Game 3
-----------------------------------

It's nice to see that instead of falling into despair. Lee Sedol is trying every possible avenue to victory.

After the 2nd game, Lee Sedol reportedly used the 1 day break to pull an all-nighter with several other Go pros, to come up with strategies to use on the 3rd game. At this point, the series isn't about seeing how strong AlphaGo is. It's about fighting for humanity's pride. (Or at least the Go community's pride. I'm sure DeepMind is very proud of what they've accomplished.)

The awesome thing is that these pro players actually have a good understanding of how AlphaGo works. Using that knowledge, they came up with a few key ideas:

- In one game, many pros felt Lee Sedol made a mistake by not pursuing a ko fight. AlphaGo was unproven at this aspect of the game, so they recommended Lee try one to see AlphaGo's response.

- Lee Sedol decided he needed to focus heavily on the early and midgame. As the game progresses, AlphaGo's play gets better, because every MCTS rollout takes less time. If he didn't get a lead early, he wasn't going to win. Lee accordingly spent much more time in the early game to make sure he played it right.

- AlphaGo tends to simplify the board when it has a lead. So, Lee Sedol tried to complicate the game when he could. He didn't know if he had a comparative advantage in complicated board states, but he knew he definitely didn't have one in simple states.

By my understanding, Lee implemented all three. He played aggressively and carefully in the midgame, but was fended off and was down too much time to try a large scale attack again. Many pros felt the game was resignable, but Lee kept going to test AlphaGo. In the endgame, he tried ko fights and complicating moves, but AlphaGo managed both, and he was eventually forced to resign.

**Even though he ultimately failed, it was still a good attempt.** These were all reasonable hypotheses, and although none led to victory, it's still better than not knowing.

It's fascinating to see how quickly the narrative has shifted from "Can AlphaGo win?" to "Can Lee win?" As awesome as AlphaGo is, I'd like to see Lee win at least 1 game, if only for the storyline. Lee Sedol, rising from despair, carrying the hopes of humanity, cheered on by Go pros around the world? That's an anime, and it's happening right now. I guess anime really is real.

(Undertale reference. Don't worry about it.)

AlphaGo 3-0 Lee Sedol

(Also, someone made [this edit](http://imgur.com/a/WefEN) to Hikaru no Go. Never read the source, but I still liked it.)


Game 4
------------------------------------

Holy shit.

Yesterday, I said I'd like for Lee Sedol to win a game for the story.

I DIDN'T THINK IT WOULD ACTUALLY HAPPEN. What in the world? Is anime real after all?

I have to admit that I only caught the end of the game today, so here's my reconstruction from the GoGameGuru comments. Once again, Lee Sedol spent time in the early and midgame for naught, as AlphaGo gained a strong lead. On move 78, Lee Sedol played a very strong move. Michael Redmond (English commentator) praised it. Gu Li (Chinese commentator) called it "God's Move" once he saw it.

AlphaGo replied wrong on move 79, although it wasn't an obvious mistake, and some pro commentators were considering AlphaGo's reply. By move 87, AlphaGo realized its mistake, and that's where things get weird. AlphaGo made a series of surprisingly awful moves, letting Lee take a huge lead. (Even I thought S11 was awful, and I've played ~10 games of Go total in my life.) AlphaGo managed to chip away the lead over the endgame, but Lee replied well (while stuck in overtime from move 90 to boot! Replying with 60s thinking time is very impressive.) Soon, there were no chances left. AlphaGo resigns, room bursts into applause.

Like I said: this is actually an anime. Lee's back is against the wall. He's struggling to stand. "I can't give up! For the world, I must fight!" He sees a move, and stuns the "perfect player", the one who's never lost. Move after move builds into a crescendo, a hurricane force, and AlphaGo doesn't know what to do.

I haven't seen any sports animes, but I'm pretty sure this plot fits just fine.

Naturally, Lee's win led to an interesting press conference. If you missed it, seeing journalists look for a reason Lee won was very amusing.

> Q: "Yesterday, you tweeted that the distributed version of AlphaGo has about a 75% win rate against the single machine version, which was still quite strong. Did you use the single machine version for this match?" (Translation: Did you dumb down the AI to make Lee Sedol feel better after losing 3-0?)

> A: "We used the same distributed version as the previous games."

(Translation: there is no conspiracy.)

> Q: "There's been discussion on an information asymmetry. AlphaGo got to see all of Lee Sedol's past games, and Lee got to see none of AlphaGo's. Having played 3 games against AlphaGo previously, I'd like to hear Lee's thoughts on this." (Translation: Do you think AlphaGo's past 3 wins were only because Lee Sedol was unfamiliar with AlphaGo's play?)

> Lee's A: "I didn't know people were discussing that. I don't see it as important. I did learn about AlphaGo in the past 3 games, but looking back I can only blame myself for my losses."

> Demis's (CEO of DeepMind) A: "AlphaGo was trained on millions of games. We did not specifically train AlphaGo with games against Lee Sedol, and even if it had thousands of his games, it would barely affect the overall algorithm."

(Translation: there is no conspiracy theory, and here's why that conspiracy theory wouldn't even work.)

For his part, Lee has shown very good sportsmanship. He made an interesting comment: "Losing a game after winning three would have been devastating. Winning a game after losing three is exhilarating in its own way." I have to agree. Suddenly, the stakes on game 5 look much higher. There's hope for an almost even 3-2. (4-1 is still more likely.)

So, what went wrong for AlphaGo? I'll explain the leading theories, then explain why they don't actually matter.

The theory is that first, AlphaGo didn't consider the line Lee Sedol played. It was too difficult to derive during the Monte Carlo Tree Search (MCTS), and Lee found a blind spot. Once AlphaGo realized its predicament, the mechanics of Monte Carlo search brought it into a downward spiral.

Recall that AlphaGo's one objective is to maximize win percentage. If AlphaGo evaluates a board as losing, it means that AlphaGo thinks if it had to play itself from that board, it would lose more often. This makes the MCTS biased to extreme outcomes that could lead to a win if the opponent misplays. AlphaGo plays such a move, but the mistake is so obvious that the (human) opponent will never make it. The human replies correctly, and AlphaGo's position deteriorates. "Well, I'm losing. But if I make this crazy move, and the other player messes up, I could still win." Make crazy move, get sane reply. "Well, I'm losing. But if I make this crazy move, and the other player messes up, I could still win." Make crazy move, another sane reply. Keep going, and going...

It's a downward spiral that has claimed weaker MCTS-based Go AIs in the past. AlphaGo somehow got itself out of the spiral, but by then it was too late.

If a human were in AlphaGo's position, they would model Lee Sedol as a strong player who would never make that mistake. They would instead play moves that limit the damage, and wait for an opportunity elsewhere.

But AlphaGo doesn't model its opponent. It's not worth it and it's too difficult, which is why suggesting DeepMind trained AlphaGo specifically as a Lee Sedol killing machine is so laughable. AlphaGo is a human agnostic. The only opponent AlphaGo has for evaluating moves is itself.

Against an opponent of itself (the strongest player it knows), playing safe while losing wouldn't increase win %. If an MCTS AI thinks the odds of opponent misplay are better than the odds of winning with safe play, it will put all the chips on that chance. I've actually seen this happen in my own research. While getting started, I ran MCTS on Tic-Tac-Toe to test my code. If you have two moves that both lead to a 3-in-a-row, MCTS will block neither 3-in-a-row. It'll instead create a 2-in-a-row elsewhere, because its best chance is to hope it gets another turn. What happened today is the same principle, except on a larger timescale with more uncertainty.

Maybe playing safe would be the right play if AlphaGo knew it was playing Lee Sedol, but AlphaGo couldn't know it was playing Lee Sedol.

Based on my experience, and on the testimony of pro players who have tried other Go AIs, and on the anecdotes relayed by people who have toyed with MCTS before, this is by far the explanation I trust the most.

And it's all slightly missing the point.

These are theories, backed up by past experience and evidence, but they'll never progress past guesswork. AlphaGo plays millions of random games **a second**. Its board evaluation is informed by a deep convolutional neural net, which is a legendarily difficult to interpret black box. To pick a move, AlphaGo runs millions of black box computations, averages them all, and gives a response. Why AlphaGo didn't see Lee's "Hand of God" play, why AlphaGo was so sure it needed a mistake to catch up, and whether AlphaGo was correct in that assessment or not is all incredibly difficult to explain, because its behavior is based on so much raw work. If DeepMind finds a concrete explanation for AlphaGo's collapse this game, hats off to them, because I don't think they can do it. I expect reasonable theories at best.

Almost all machine learning used today runs on black boxes. We show this image recognition model does 0.5% better on this dataset than the old one, but it's usually not clear why, and very smart people have to try hard to justify why a machine learning method works over another. (Surprisingly often, the key to good performance is to throw everything at the dart board and see what sticks.)

For now, it's fine. Computers are only good at maximizing exactly defined utility functions, and it's on the human to describe a utility function that makes the AI do what we want. In the future. when computers are good at maximizing ill-defined utilities? Well, that's when you get the paperclip optimizers people like to talk about when advocating for AI safety. I may not agree on the timetable for AGI, but I agree it's worth doing work on now. (For what it's worth: 75% confidence interval on 20-40 years, and I think AI risk research is around as funded as it should be right now. I donated $20 to MIRI last year since it sounded like they could use the help.)
*(Editor's note: after some Facebook discussion, I've since revised this to 50% confidence
for 30-55 years, with more weight towards the end of the range, and believe
AI risk could use more funding.)*

Today showed AIs can exhibit strange emergent behavior in the right circumstances, causing them to jump from "smart" to "insane" in a second. The first question from the press conference hit this nail on the head.

> Q: "Today, we saw AlphaGo make many unfathomable mistakes to experts. They thought these moves made no sense, but were hesitant to question AlphaGo. They weren't sure if AlphaGo's mistakes were actually mistakes. If this happened in real world usage, like something medical, and it recommends what looks like a mistake to experts, and people don't question it because they think there's a bigger picture, it could lead to lots of confusion. So, I'm curious to hear your perspective on that."

It was a great question that cut to the heart of the matter. DeepMind is already eyeing medicine (see DeepMind Health), so this is especially relevant.

> Demis's A: "You have to remember AlphaGo is a prototype. I wouldn't call it a beta, or even an alpha. So of course, part of why we're doing this match is to test our methods against skilled humans. We're also playing a game, a beautiful game. Healthcare would be a different matter, and of course it would require stringent testing like other software. This is a prototype we're testing, so I think it's a different situation."

It's a good point with no easy answers. Trust the AI (who can crunch numbers and read orders of magnitude more data), or trust yourself (and the intuition gained from your comparatively little knowledge)? If something goes wrong, whose fault is it? Yours for trusting the AI too much, or yours for trusting the AI too little?

I'm optimistic we can figure these issues out. We had a small viewing party in the lab for Game 1, and a human-computer interaction professor made an interesting anecdote: humans lose to computers in chess, but a human with a computer partner beats other computers. The human isn't dead meat despite being individually useless. They can still contribute something. It's nice to know we're not obsolete yet.

AlphaGo 3-1 Lee Sedol

(Michael Redmond's reaction to move 78: [YouTube video](https://www.youtube.com/watch?v=yCALyQRN3hw&t=11413).)

[![AlphaGo resigning](/public/ago-lsd/alphagoresign.jpg)](/public/ago-lsd/alphagoresign.jpg)
{: .centered }

AlphaGo resigning. Click for larger version.
{: .centered }



Game 5
-------------------------------------

Final match ends in a win for AlphaGo as expected.

The short summary of the game: in the early game, AlphaGo didn't recognize a known tesuji, letting Lee Sedol gain a sizable lead in the bottom right. However, over the rest of the game AlphaGo was one step ahead of Lee Sedol (commentators said the key point was Lee losing in top-left) It was just enough to let AlphaGo make a comeback, and Lee resigned with the board almost filled to completion. (People say the board ends with AlphaGo winning by 2.5 points)

First off, I want to highlight how much Game 4 dominated the commentary. As soon as AlphaGo made a mistake, people asked if game 4 was going to happen again. Chris Garlock (English co-commentator) kept prompting Michael Redmond to indicate whether he thought AlphaGo's moves were a sign of it blowing up or not. Of course, based on the match result they weren't. In fact, it sounded like AlphaGo played almost every move well, and the only questionable moves were ones that appeared when AlphaGo was leading.

It's really interesting to see how much people tried to read into AlphaGo's evaluation of the board based on the moves it made. An aggressive move must mean it thinks it's losing! A slack move must mean it thinks it's ahead! Well, there's certainly some correlation, but it's definitely not that clear cut.

That's a nice segway for the topic I decided to close on: anthropomorphization of AlphaGo. (Not going to lie, had to Google that to make sure I spelled it right.)

Everyone is very guilty of giving human qualities to AlphaGo, including me. People have described AlphaGo's play as calm or collected or aggressive or smooth, as if AlphaGo is a person. Some commentators call AlphaGo a "she'. The Chinese stream started calling AlphaGo 阿老师, which translates to "Teacher Ah", for "Teacher Alpha Go". AlphaGo has even been given an honorary 9 professional dan rating from the Korean Baduk Association.

This isn't limited to the commentators, the technical side has done this too. One of the onsite DeepMind engineers did an interview during the game about what it's like in AlphaGo's control room. He described it as monitoring the heart of AlphaGo, making sure communication to the datacenter is working, verifying failing machines are automatically rebooted, and so on. (Yes, it is run over the network. I believe it's connected from a datacenter in the central US.) During game 4, Demis made a tweet saying AlphaGo thought it was doing well before realizing its mistake. He then had to clarify that "thought" and "realization" meant "AlphaGo's estimated win % was high, then dropped." In these very writeups, I've said things like "AlphaGo thinks", when the more accurate thing to say is "AlphaGo runs millions of simulations."

On one hand, I don't think anthropomorphizing AI is a bad thing. Many of the algorithms in AI are motivated by real life biology. It's much easier to explain AlphaGo using human analogy. At some point, trying to pedantically explain exactly what AlphaGo is doing every single time is just going to get tiring. There's a concept called the duck test: if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck. If AlphaGo plays like a human, if its algorithms share similarities to a human's, if it can beat a professional player like a human, then maybe it's okay to treat it as a human.

But, the reason it's important to be careful about humanizing AI too much is that many people assign human qualities to AI far more easily than they should, and it makes people both overestimate and misunderstand how AI works. AlphaGo does not think, if by think you mean how a human thinks. It does not have a heart, if by heart you mean something like a human heart. When we say "think" or "heart", we really mean "a very rough approximation to human thought" and "a very rough approximation to a heart". The problem happens when people think "think" actually means "think like a human" when it *doesn't*. It really, really, does not. Is it any wonder that Yann LeCun got pissed off when he [read someone claim that strong AI didn't need any more breakthroughs](https://www.facebook.com/yann.lecun/posts/10153426023477143)?

Anthropomorphizing AI makes it sound like we know a lot more than we actually do, and suggests strong AI will think like humans do, and both are dead wrong. And that's why I get annoyed at it, even as I use human analogies in my own speech.

Looking back, that's why I started doing these write-ups in the first place. It let me explain just how far these analogies apply, meaning not very far at all.

And this is just for a MCTS-based game AI. This is by far the area I'm most qualified to talk about. I know I'm still missing a lot of the bigger picture, and some of the comments made on day 1 were still incredibly exasperating to read.

It's given me some food for thought. If I can tell AI discussion is simplified so often, I should recognize that most of my knowledge must also be founded on very heavy abstraction that hides the underlying complexity, and that if I state it too confidently it'll probably piss off other people as well.

To paraphrase a source I can't remember:

> The thing I hate about those 800-page high school textbooks is that they suggest we've solved biology, chemistry, and physics. We haven't even scratched the surface. I'm worried they'll make students think there's nothing more to discover. That all the answers are written down. One book for Everything About Insects. One for Everything About Light. One for Everything About Algebra. I'm worried students won't understand what it means to be a researcher.

AlphaGo vs Lee Sedol was the highest profile experiment of AI to date, and even if you were supporting Lee Sedol and were crushed when he lost the first 3 games, I think this match is still worthy of applause, if only because it was a real-world test of the capabilities of AI. It's been exciting. Can't wait to see what's next.

AlphaGo 4-1 Lee Sedol

(Oh god, I'm typing this during the final press conference and a reporter just asked how many clones of AlphaGo DeepMind has and how many they were planning to make. I do not have enough hands for the amount of facepalm I want to do.)

(Woops, and another reporter is suggesting DeepMind hosted this contest to see the public's perception towards AI, and wanted to know how DeepMind's ethics board will handle the people's fears about AI. I mean, sure, it could be part of their reasoning, but it's definitely not their main reason for hosting the match.)
*(Editor's note: and connotating that DeepMind has a vaguely sinistor motive
isn't doing me any favors.)*
