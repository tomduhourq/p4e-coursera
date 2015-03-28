__author__ = 'tomas'
import collections, string
from src.FilePractice.file_helper import choose_file
# Exercise 1
mails = dict()
for line in choose_file():
    if line == '' or not line.startswith('From:'): continue
    mail = line.split()[1]
    mails[mail] = mails.get(mail, 0) + 1

lst = list()
for mail, count in mails.items():
    lst.append((count, mail))

lst.sort(reverse=True)

count, mail = lst[0]
print mail, count

# Exercise 2
HOUR_POSITION = 5
hours = dict()
for line in choose_file():
    words = line.split()
    if len(words) < HOUR_POSITION or\
       line == '' or\
       not line.startswith('From'): continue
    hour = words[HOUR_POSITION].split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

# Sort by hour
hours = collections.OrderedDict(sorted(hours.items()))

for hour, count in hours.items():
    print hour, count

# Exercise 3
letters = dict()


def chars():
    return line.lower().translate(None, string.punctuation + string.digits).split()


for line in choose_file():
    for word in chars():
        for char in word:
            letters[char] = letters.get(char, 0) + 1

letters = collections.OrderedDict(sorted(letters.items(), key=lambda x: x[1], reverse=True))

for char, count in letters.items():
    print char, count




