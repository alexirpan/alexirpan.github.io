import csv
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.offsetbox as ob
from matplotlib._png import read_png


def read_data():
    path = os.path.join(os.path.expanduser('~'), 'fruit.csv')
    with open(path) as f:
        reader = csv.reader(f, delimiter=",")
        categories = reader.next()
        categories = categories[1:-2]
        rows = []
        for row in reader:
            rows.append(row)
        rows = clean_data(rows)
        return categories, rows


def clean_data(rows):
    # Removes duplicate entries. An entry is for sure a duplicate if it uses
    # the same email. This won't get rid of all entries but I'm assuming
    # no one tried to seriously attack a survey about fruit
    dedup_rows = []
    seen_emails = set()
    for row in rows:
        email = row[-1]
        # First item = timestamp. Last two items = whether to be notified and
        # email. Don't want either of these anymore, remove before doing
        # further analysis
        anon_row = row[1:-2]
        if email == '':
            dedup_rows.append(anon_row)
        elif email not in seen_emails:
            seen_emails.add(email)
            dedup_rows.append(anon_row)
    print 'Removed %d duplicate entries, leaving %d replies' % (
        len(rows) - len(dedup_rows), len(dedup_rows))
    # Remove entries with no opinion
    cleaned_rows = [row for row in dedup_rows if row.count('') < len(row)]
    print 'Removed %d empty entries, leaving %d replies' % (
        len(dedup_rows) - len(cleaned_rows), len(cleaned_rows))
    return cleaned_rows


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


def show_plot(averages, stretch=True):
    fig = plt.figure()

    img = plt.imread('xkcdemptyfruit.png')
    plt.imshow(img)
    # Coordinates of key locations in image
    LEFT = (19, 288)
    CENTER = (339, 288)
    RIGHT = (659, 288)
    TOP = (339, 18)
    BOTTOM = (339, 558)

    EASE = (RIGHT[0] - LEFT[0]) / 9.0
    TASTE = (TOP[1] - BOTTOM[1]) / 9.0
    # This is (0, 0) in fruit space
    BOT_LEFT = (LEFT[0] - EASE, BOTTOM[1] - TASTE)

    if stretch:
        min_ease = min(t[0] for t in averages.values())
        max_ease = max(t[0] for t in averages.values())
        min_taste = min(t[1] for t in averages.values())
        max_taste = max(t[1] for t in averages.values())
        taste_scale = (max_ease - min_ease) / (max_taste - min_taste)
    else:
        taste_scale = 1
    print 'Scaling tastes by %f' % taste_scale
    avg_ease = sum(t[0] for t in averages.values()) / len(averages)
    avg_taste = sum(t[1] for t in averages.values()) / len(averages)
    print 'Average of data is (%f, %f)' % (avg_ease, avg_taste)

    fruits = []
    ease_coor = []
    taste_coor = []
    for fruit in averages.keys():
        fruits.append(fruit)
        ease = averages[fruit][0]
        ease_coor.append(BOT_LEFT[0] + ease * EASE)
        taste = averages[fruit][1]
        taste = (taste - avg_taste) * taste_scale + avg_taste
        taste_coor.append(BOT_LEFT[1] + taste * TASTE)

    plt.scatter(ease_coor, taste_coor)
    for i, fruit in enumerate(fruits):
        xy = [ease_coor[i] - 10, taste_coor[i] - 5]
        plt.annotate(s=fruit, xy=xy)
        add_image(fig, 'fruit-pics/%s.png' % fruit.lower(), xy[0], xy[1])
    plt.savefig('foo.png')


def add_image(fig, filename, x, y):
    # Adds image to (x, y) in the plot
    if not os.path.isfile(filename):
        print '%s could not be found' % filename
        return
    img = plt.imread(filename)
    width = img.shape[1]
    height = img.shape[0]
    ax_img = fig.add_axes([x, y, width, height])
    ax_img.imshow(img)
    print 'Added %s' % filename


show_plot(averages, stretch=True)
