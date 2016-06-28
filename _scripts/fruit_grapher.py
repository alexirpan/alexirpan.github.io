import csv
import os

import numpy as np


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
        for dim in (0, 1):
            fruit_ease = data[:, i, dim]
            n_ease = (~np.isnan(fruit_ease)).sum()
            total = np.nan_to_num(fruit_ease).sum()
            avg = float(total) / n_ease
            averages[categories[dim * num_fruit + i]] = avg
            for j in xrange(num_replies):
                if np.isnan(data[j, i, dim]):
                    data[j, i, dim] = avg
                    replaced += 1
    print 'Replaced %d NaN entries with the corresponding average' % replaced
    return averages

averages = replace_nan_and_get_avg(data, categories)

