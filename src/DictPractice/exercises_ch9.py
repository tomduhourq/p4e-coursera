__author__ = 'tomas'


# Exercise 1
def process_line(l):
    for word in l:
        if word not in words:
            words[word] = 1

words = dict()
for line in open('../WordCount/quijote.txt'):
    process_line(line.split())


