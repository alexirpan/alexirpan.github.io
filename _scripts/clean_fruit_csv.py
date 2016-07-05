"""Loads fruit.csv, removes duplicate entries, and outputs an anonymized clean_fruit.csv file"""

import csv
import os

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


categories, rows = read_data()
write_path = os.path.join(os.path.expanduser('~'), 'clean_fruit.csv')

with open(write_path, 'w') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(categories)
    for row in rows:
        writer.writerow(row)

