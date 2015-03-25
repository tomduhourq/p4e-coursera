__author__ = 'tomasduhourq'
import string
from src.FilePractice.file_helper import choose_file

# Sorting the keys of a dict
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# Create a list of the keys in the dict


def sort_keys(d):
    keys = d.keys()
    keys.sort()
    for key in keys:
        print key, d[key]

sort_keys(counts)

# Using string.translate to get rid of punctuation characters
counts = dict()
for line in open('../ListPractice/romeo.txt'):
    line = line.translate(None, string.punctuation).lower()
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

# Integrating everything
counts = dict()
for line in choose_file():
    for word in line.translate(None, string.punctuation).lower().split():
        counts[word] = counts.get(word, 0) + 1

sort_keys(counts)

