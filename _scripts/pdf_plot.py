"""
Make plots for p.d.f. or p.m.f. of various distribution

Requires NumPy + matplotlib + possibly SciPy + a LaTeX distribution
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

    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$P[X=x]$', fontsize=16)
    plt.xticks(np.arange(11))
    plt.xlim((-width / 2, 10 + width / 2))
    plt.ylim((0, 0.55))
    plt.title(r"Probability mass function for geometric distribution, $p$ = %.1f" % p)
    plt.show()

def std_normal():
    SAMPLES = 10 ** 5
    x = np.linspace(-3, 3, num=1000)
    y = (2 * np.pi) ** -0.5 * np.exp(-x*x/2)

    plt.figure(facecolor='white')
    plt.plot(x, y)

    plt.title("Probability density function for standard normal")
    plt.xlabel(r'$x$')
    plt.ylabel(r'$p.d.f.(x)$')
    plt.ylim((0, 0.45))
    ax = plt.gca()
    ax.fill_between(x, y, facecolor='blue', alpha=0.5)
    plt.show()

geometric(0.5)
std_normal()


