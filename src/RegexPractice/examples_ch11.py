__author__ = 'tomas'
from src.FilePractice.file_helper import choose_file
import re

# re.search returns a positive number
# if the pattern is found, or -1 otherwise
for line in choose_file():
    if re.search('From:', line):
        print line.rstrip()

# ^  -> match the beginning of the line
# .  -> match any character
# *  -> many times
# +  -> one or more times
# \S -> match any non-whitespace character
# [] -> lists a set of characters to match
for line in choose_file():
    if re.search('^From:', line):
        print line.rstrip()

# Extract a list of matches given a regex
print re.findall('[0-9]+', 'I am 22 years old')
