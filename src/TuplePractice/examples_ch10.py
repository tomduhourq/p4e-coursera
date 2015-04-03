__author__ = 'tomas'
import string

# DSU = Decorate, Sort & Undecorate
txt = 'but soft what light in yonder window breaks'
t = list()
for word in txt.split():
    t.append((len(word), word))

# Compares by first elem for each tuple
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

# Simple word count, getting top 10 words and their apparitions
counts = dict()
for line in open('../DictPractice/romeo-full.txt'):
    for word in line.translate(None, string.punctuation).lower().split():
        counts[word] = counts.get(word, 0) + 1

# Sorting dict by value without recurring to OrderedDict
lst = list()
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print key, val

# Using list comprehension (from having the word count)
print sorted( [ (v, k) for k, v in counts.items() ], reverse=True )[:10]

# Tuples can also be used as composite keys in a dictionary
telephones = {('Duhourq', 'Tom'): 45454545, ('Doe', 'John'): 43434343 }
for last, first in telephones:
    print first, last, telephones[last, first]


