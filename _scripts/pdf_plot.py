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

    plt.bar(np.arange(0, 11 * width, width), probs, width, align='center')
    plt.xlabel('x')
    plt.ylabel('P[X=x]')
    plt.xticks(np.arange(11))
    plt.xlim((-width / 2, 10 + width / 2))
    plt.ylim((0, 0.6))
    plt.title("Probability mass function for geometric distribution, p = %.2f" % p)
    plt.tight_layout()
    plt.show()

geometric(0.5)
