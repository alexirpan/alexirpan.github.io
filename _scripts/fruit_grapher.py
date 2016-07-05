import csv
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def read_data():
    path = os.path.join(os.path.expanduser('~'), 'clean_fruit.csv')
    with open(path) as f:
        reader = csv.reader(f, delimiter=",")
        categories = reader.next()
        rows = []
        for row in reader:
            rows.append(row)
        return categories, rows


def unique_count(rows):
    s = set()
    for row in rows:
        s.add(tuple(row))
    print '%d unique opinions in %d entries' % (len(s), len(rows))


categories, rows = read_data()
unique_count(rows)


def place_into_np(rows):
    num_replies = len(rows)
    num_fruit = len(categories) // 2
    data = np.zeros((num_replies, num_fruit, 2), dtype=np.float32)
    for i, row in enumerate(rows):
        first_half = row[:num_fruit]
        second_half = row[num_fruit:]
        for j, v in enumerate(first_half):
            if v == '':
                value = np.nan
            else:
                value = int(v)
            data[i, j, 0] = value
        for j, v in enumerate(second_half):
            if v == '':
                value = np.nan
            else:
                value = int(v)
            data[i, j, 1] = value
    return data


data = place_into_np(rows)


def replace_nan_and_get_avg(data, categories):
    # Replace every NaN with the average ease of eating or tastiness
    # for that fruit. Modifies original array
    # Returns the mean ease and taste for each fruit
    num_replies = data.shape[0]
    num_fruit = data.shape[1]
    replaced = 0
    averages = dict()

    for i in range(num_fruit):
        fruit_name = categories[i].rsplit(' ', 1)[0][:-1]
        averages[fruit_name] = [0, 0]
        for dim in (0, 1):
            fruit_ease = data[:, i, dim]
            n_ease = (~np.isnan(fruit_ease)).sum()
            total = np.nan_to_num(fruit_ease).sum()
            avg = float(total) / n_ease
            averages[fruit_name][dim] = avg
            for j in xrange(num_replies):
                if np.isnan(data[j, i, dim]):
                    data[j, i, dim] = avg
                    replaced += 1
    print 'Replaced %d NaN entries with the corresponding average' % replaced
    return averages


averages = replace_nan_and_get_avg(data, categories)

# Picture data
LEFT = (19, 288)
CENTER = (339, 288)
RIGHT = (659, 288)
TOP = (339, 18)
BOTTOM = (339, 558)

EASE = (RIGHT[0] - LEFT[0]) / 9.0
TASTE = (TOP[1] - BOTTOM[1]) / 9.0
# This is (0, 0) in fruit space
BOT_LEFT = (LEFT[0] - EASE, BOTTOM[1] - TASTE)


def transform_data(data, averages, categories):
    """Transforms the data into plotted (x, y) coordinates."""
    # Manually strecth the taste scale to make the resulting graph
    # less compact
    min_ease = min(t[0] for t in averages.values())
    max_ease = max(t[0] for t in averages.values())
    min_taste = min(t[1] for t in averages.values())
    max_taste = max(t[1] for t in averages.values())
    taste_scale = (max_ease - min_ease) / (max_taste - min_taste)
    print 'Scaling tastes by %f' % taste_scale

    num_replies = data.shape[0]
    num_fruit = data.shape[1]
    avg_taste = sum(t[1] for t in averages.values()) / len(averages)

    for j in xrange(num_replies):
        for i in xrange(num_fruit):
            data[j, i, 0] = BOT_LEFT[0] + EASE * data[j, i, 0]
            taste = data[j, i, 1]
            taste = (taste - avg_taste) * taste_scale + avg_taste
            data[j, i, 1] = BOT_LEFT[1] + TASTE * taste
    print 'Scaled data to match coordinates.'

    plotted_avgs = dict()
    for i in range(num_fruit):
        fruit_name = categories[i].rsplit(' ', 1)[0][:-1]
        plotted_avgs[fruit_name] = [0, 0]
        for dim in (0, 1):
            fruit_ease = data[:, i, dim]
            n_ease = (~np.isnan(fruit_ease)).sum()
            total = fruit_ease.sum()
            avg = float(total) / n_ease
            plotted_avgs[fruit_name][dim] = avg
    print 'Computed scaled averages'
    return plotted_avgs


plotted_avgs = transform_data(data, averages, categories)


def fit_gaussian(data, averages, categories):
    """ Fits a Gaussian distribution to the data through MLE. """
    num_replies = data.shape[0]
    num_fruit = data.shape[1]
    covariances = dict()

    for i in range(num_fruit):
        fruit_name = categories[i].rsplit(' ', 1)[0][:-1]
        covariances[fruit_name] = np.cov(data[:, i, :], rowvar=False)
        assert covariances[fruit_name].shape == (2, 2)

    return covariances


covariances = fit_gaussian(data, plotted_avgs, categories)

fruits = list(averages.keys())
hardest = sorted(fruits, key=lambda f: averages[f][0])
easiest = sorted(fruits, key=lambda f: -averages[f][0])
worst = sorted(fruits, key=lambda f: averages[f][1])
tastiest = sorted(fruits, key=lambda f: -averages[f][1])
# Area of ellipse = pi * a * b where a,b are lengths of major and minor
# axes.
# For covariance matrices, a and b are the sqrt of the eigenvalues
# The determinant is the product of the eigenvalues
# So, the determinant corresponds exactly to the area of the ellipse for
# 1 stddev away.
agreed_on = sorted(fruits, key=lambda f: np.linalg.det(covariances[f]))
controversial = sorted(fruits, key=lambda f: -np.linalg.det(covariances[f]))

print 'Hardest', hardest
print 'Easiest', easiest
print 'Worst', worst
print 'Tastiest', tastiest
print 'Controversial', controversial
print 'Agreed On', agreed_on


# Copied from StackOverflow
def plot_point_cov(points, nstd=2, ax=None, **kwargs):
    """
    Plots an `nstd` sigma ellipse based on the mean and covariance of a point
    "cloud" (points, an Nx2 array).

    Parameters
    ----------
        points : An Nx2 array of the data points.
        nstd : The radius of the ellipse in numbers of standard deviations.
            Defaults to 2 standard deviations.
        ax : The axis that the ellipse will be plotted on. Defaults to the 
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.

    Returns
    -------
        A matplotlib ellipse artist
    """
    pos = points.mean(axis=0)
    cov = np.cov(points, rowvar=False)
    return plot_cov_ellipse(cov, pos, nstd, ax, **kwargs)

def plot_cov_ellipse(cov, pos, nstd=2, ax=None, **kwargs):
    """
    Plots an `nstd` sigma error ellipse based on the specified covariance
    matrix (`cov`). Additional keyword arguments are passed on to the 
    ellipse patch artist.

    Parameters
    ----------
        cov : The 2x2 covariance matrix to base the ellipse on
        pos : The location of the center of the ellipse. Expects a 2-element
            sequence of [x0, y0].
        nstd : The radius of the ellipse in numbers of standard deviations.
            Defaults to 2 standard deviations.
        ax : The axis that the ellipse will be plotted on. Defaults to the 
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.

    Returns
    -------
        A matplotlib ellipse artist
    """
    def eigsorted(cov):
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        return vals[order], vecs[:,order]

    if ax is None:
        ax = plt.gca()

    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))

    # Width and height are "full" widths, not radius
    width, height = 2 * nstd * np.sqrt(vals)
    ellip = patches.Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)

    ax.add_artist(ellip)
    return ellip


def show_plot(data, averages, covariances, ellipse=True, orig_fruit=True):
    fig = plt.figure()

    if orig_fruit:
        img = plt.imread('xkcdfruit.png')
    else:
        img = plt.imread('xkcdemptyfruit.png')
    plt.imshow(img)

    # Location of averages
    fruits = []
    ease_coor = []
    taste_coor = []
    for fruit in averages.keys():
        fruits.append(fruit)
        ease_coor.append(averages[fruit][0])
        taste_coor.append(averages[fruit][1])

    # Adds text labels
    plt.scatter(ease_coor, taste_coor)
    for i, fruit in enumerate(fruits):
        x_off = 3 * len(fruit)
        xy = [ease_coor[i] - x_off, taste_coor[i] - 5]
        plt.annotate(s=fruit, xy=xy)

    if ellipse:
        # Adds confidence ellipse
        nstd = 0.25
        # Area within nstd of mean
        p = 1 - np.exp(-0.5 * nstd ** 2)
        print 'Drawing ellipses within %f of mean' % p

        for i, fruit in enumerate(fruits):
            cov = covariances[fruit]
            ave = averages[fruit]
            # Draw the 2-sigma ellipse.
            plot_point_cov(data[:, i, :], nstd=nstd, facecolor='none')
            #plot_cov_ellipse(cov, ave, nstd=0.25, facecolor='none')
            print 'Added ellipse for %s' % fruit

    plt.show()


show_plot(data, plotted_avgs, covariances, ellipse=False, orig_fruit=True)
