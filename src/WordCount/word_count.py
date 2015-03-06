__author__ = 'tomasduhourq'
import operator

name = raw_input('Enter file: ')
handle = open(name, 'r')
text = handle.read()

wordcount = {}
for word in text.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# Sort the dict by values
s = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
for k, v in s:
    print k, v
