__author__ = 'tomasduhourq'
from src.FilePractice.file_helper import choose_file

# Exercise 4
words = list()
for line in choose_file():
    for w in line.split():
        if not words.__contains__(w):
            words += w

print words

