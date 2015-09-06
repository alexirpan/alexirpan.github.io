"""
Make plots for p.d.f. or p.m.f. of various distribution. Used for the
envelopes post.

Lots of magic constants here.

Requires NumPy + matplotlib + a LaTeX distribution
"""
import numpy as np
import matplotlib.pyplot as plt

def geometric(p):
    # Instead of computing exactly, take many samples and make histogram
    SAMPLES = 10 ** 5
    z = np.random.geometric(p, size=SAMPLES)
    # From 1 to 10 inclusive
    z = z[ np.logical_and((1 <= z), (z <= 10)) ]
    probs = [(z == i).sum() / float(SAMPLES) for i in xrange(11)]
    width = 1.0

    plt.figure(facecolor='white')
    plt.bar(np.arange(0, 11 * width, width), probs, width, align='center', alpha=0.5)

    plt.title(r"Probability mass function for geometric distribution, $p$ = %.1f" % p)
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$P[X=x]$', fontsize=16)
    plt.xticks(np.arange(11))
    plt.xlim((-width / 2, 10 + width / 2))
    plt.ylim((0, 0.55))
    # Decision boundary
    plt.axvline(x=4-width/2, color='r')
    plt.text(4-width/2+0.1, 0.4, r'$Y \,\geq\, 4$', fontsize=16)
    probs = probs[4:]
    plt.bar(np.arange(4*width, 11 * width, width), probs, width, align='center', alpha=0.3, color='red')

    plt.show()


def std_normal():
    SAMPLES = 10 ** 5
    x = np.linspace(-3, 3, num=1000)
    y = (2 * np.pi) ** -0.5 * np.exp(-x*x/2)

    plt.figure(facecolor='white')
    plt.plot(x, y)

    plt.title("Probability density function for standard normal")
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$p.d.f.(x)$', fontsize=16)
    plt.ylim((0, 0.45))
    ax = plt.gca()
    ax.fill_between(x, y, facecolor='blue', alpha=0.5)
    # Decision boundary
    plt.axvline(x=1, color='r')
    plt.text(1.1, 0.32727, r'$Y \,\geq\, 1$', fontsize=16)
    pairs = zip(x, y)
    pairs = filter(lambda p: p[0] >= 1, pairs)
    x = [p[0] for p in pairs]
    y = [p[1] for p in pairs]
    ax.fill_between(x, y, facecolor='red', alpha=0.3)

    plt.show()


if __name__ == '__main__':
    geometric(0.5)
    std_normal()

