__author__ = 'tomasduhourq'

from src.FilePractice.file_helper import choose_file
import operator

wordcount = {}
for word in choose_file().read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# Sort the dict by values
s = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
for k, v in s:
    print k, v
