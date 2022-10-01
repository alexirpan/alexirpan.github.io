---
layout: post
title:  "Generative Modelling is Still Accelerating"
date:   2022-08-18 02:57:00 -0700
---

DALL·E 2 was announced in April of this year. As a rule, by the time the paper
is public, the model probably existed a month ago, often more.

It's been swiftly followed by Midjourney, Stable Diffusion, and Imagen, all
developed simultaneously as far as I can tell. If you are new to ML, this
is pretty common. Although you may not be aware of the good ideas, people
who are paying attention will notice and develop the same good ideas within a
few months of each other. My understanding is that diffusion was building
up steam, then [classifier-free guidance](https://openreview.net/forum?id=qw8AKxfYbI)
was developed, and that was the key piece that unlocked the improved generations
we're seeing today. (I highly recommend [Sander Dieleman's post](https://benanne.github.io/2022/05/26/guidance.html)
if you want to learn more of the math.)

In the months since, image generation has gone from a thing some people talked
about, to something *everyone* was talking about. The copyright discussion used
to only be about people who know the details of open source licenses, a pretty
small fraction of people (no matter how different it might appear on the Internet).
Now it's something generic artists immediately have an opinion on.

I've seen people say "this is a DALL-E ass looking movie poster", in a bad way.
I've seen artists preach AI asceticism, meaning "do not use image generation
tools, opt out of letting your art get used in these tools if they give you
the choice". I read a post from someone who discussed AI asceticism, and then
acknowledged that they could not do it, the image generation was too fun to play
with.

This still feels crazy to me? People have normalized that it is possible
to get high quality language-guided image generation *really, really* quickly.
In another world, perhaps it would end there. A lot of wild stuff has been happening.
But if I had to estimate where we
were on the technology development curve, I'd say we're about here:

[!Image of technology S-curve, with a red dot about 1/3rd of the way up the curve, before the inflection point](/public/generative-models/technology-s-curve.png)
{: .centered }

I believe this for two big reasons.

Generative modeling in the past few years were primarily ruled by GANs. The developments
in image generation are baesd not on a better GAN, but on diffusion methods,
an entirely different paradigm for viewing ML problems. Anytime you have a new paradigm,
you should expect a lot of people to try it on their problem, and then watch some of
those people succeed and breakthrough on problems that used to be hard.

I'd say the bigger reason I believe we're just getting started is that diffusion is a very
general idea. The current AI news has been powered by images, but nothing about diffusion
is image centric. There's more to life than just images.

When AlphaGo first beat Lee Sedol, I [said]({% post_url 2016-03-17-alphago-lsd %}) that
it might be the end of turn-based perfect information games - all of them. Go was mountain top,
and although AIs wouldn't exist for other games, no one would doubt that it was possible if
someone put a team on solving it.

Something similar is starting to feel true for problem domains where there is enough human data
on the Internet. Before people yell at me: I said **starting**! I think there's only a few
domains where we actually have enough human data at the moment. If pure data quantity
was the only factor that mattered, RL agents playing Atari games should have taken over the
world by now.

What matters right now is how much human output you can get for your problem domain.
When I read through the [Whisper](https://cdn.openai.com/papers/whisper.pdf) paper for
better speech recognition, I found this section especially interesting.

> Many transcripts on the internet are not actually human-
> generated but the output of existing ASR systems. Recent
> research has shown that training on datasets of mixed human
> and machine-generated data can significantly impair the per-
> formance of translation systems (Ghorbani et al., 2021). In
> order to avoid learning “transcript-ese”, we developed many
> heuristics to detect and remove machine-generated tran-
> scripts from the training dataset. Many existing ASR sys-
> tems output only a limited subset of written language which
> removes or normalizes away aspects that are difficult to pre-
> dict from only audio signals such as complex punctuation
> (exclamation points, commas, and question marks), format-
> ting whitespace such as paragraphs, or stylistic aspects such
> as capitalization. An all-uppercase or all-lowercase tran-
> script is very unlikely to be human generated. While many
> ASR systems include some level of inverse text normaliza-
> tion, it is often simple or rule-based and still detectable from
> other unhandled aspects such as never including commas.

As data-hungry as the Whisper model is, it is still better to exclude certain kinds of
data from its training set. It is not just enough to have a massive pool of data, you
still need some management to make sure it is of the right form. (Kind of like how
swimming pools are not just piles of water, they get chlorinated and processed to remove
germs.)

For text, we wrote a bunch of stuff on the Internet, so it was all there. For
images, we took a bunch of photos and drew a bunch of art, so it was all there.
What else? Well, there's a bunch of audio files on Bandcamp and Soundcloud and Spotify,
I assume people are trying stuff there. There are a gajillion videos on Youtube,
and by now I've heard 3 different ML research labs talk about "learning from YouTube".
It's not a secret, it's just hard.

Aside from those, I actually don't know of much else that fits my mental model
of "literally billions of people have put this content online for free". There are lots
of *effort-heavy* datasets for different problem domains (protein folding, theorem proving, [GoPro datasets](https://ego4d-data.org/), etc.). These were created with purpose and intention, and that intention limits how
big the datasets can be. Some of those will lead to cool things! I don't think they'll lead to
fundamental floor raising of what we believe ML models are capable of. The problem with Whisper
is that you don't want to learn "transcript-ese" instead of Japanese, and I'm not yet convinced
that current models are good enough to cross the transcript-ese barrier.

Even so, if you assume the improvements stop there, and you just have better image generation, audio generation, and
video generation, that still covers...like, a really heavy fraction of the human experience?
The submission deadline for ICLR just passed, meaning all the ML researchers are putting their
conference submissions on arXiv, and there is some wild, **wild** stuff branching off from diffusion
models as-is.

There's an [audio diffusion](https://felixkreuk.github.io/text2audio_arxiv_samples/)
paper, for text-to-audio.

<div class="centered">
<video width="100%" height="auto" max-width="100%" controls>
    <source type="video/mp4" src="/public/generative-models/audiogen-teaser.mp4">
</video>
</div>

There is a [3D asset generator](https://dreamfusion3d.github.io/) based on NeRF + using
Imagen as a loss function, letting you bootstrap from 2D text-to-image into 3D data.

<div class="centered">
<video width="100%" height="auto" max-width="100%" autoplay loop playsinline muted poster="https://dreamfusion-cdn.ajayj.com/sept28/wipe_opposite_6x4_smoothstep.jpg" class="video d-none d-xs-none d-sm-block">
    <source type="video/mp4" src="https://dreamfusion-cdn.ajayj.com/sept28/wipe_opposite_6x4_smoothstep.mp4">
</video>
</div>

There is a [video generator](https://makeavideo.studio/) that's also bootstrapping from a 2D image model
to build up to video generation, since this seems to work better than [doing video diffusion straight](https://video-diffusion.github.io/).

![Animation of asteroids](asteroids.webp)
{: .centered }

This may be early, but diffusion looks like it's going to go down as a ResNet-level idea
in how it generally impacts the development of machine learning models. The jump seems pretty discontinous to me!
I know this stuff is hard, and there are cavaets to what works and what doesn't, and you just see
the successes, and so on. Still, I don't think there is a reasonable way you can say,
"ah, yeah, but this is all a dead-end, it's going to hit a wall soon". Right now the runway seems at least
2 years long to me, and that's a lot of time for model improvements. As a comparison, 2 years ago is
about when GPT-3 came out.

This stuff is going to hit the wider public consciousness in about a year or two, and people are not
going to be ready for it.
