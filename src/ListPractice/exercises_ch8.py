__author__ = 'tomasduhourq'
from src.FilePractice.file_helper import choose_file

# Exercise 4
words = list()
for line in choose_file():
    for w in line.split():
        if not w in words:
            words.append(w)

words.sort()
print words

# Exercise 5
count = 0
for line in choose_file():
    if not line.startswith('From '): continue
    count += 1
    print line.split()[1]

print 'There were %d lines in the file with From as the first word' % count

# Exercise 6
nums = list()
while(True):
    e = raw_input('Enter a number or "done":')
    if e == 'done' : break
    try:
        n = float(e)
    except:
        print 'Invalid input'
        exit()
    nums = nums + [n]

print 'Maximum: ', max(nums)
print 'Minimum: ', min(nums)

len = len(nums)
if len > 0:
    print 'Average: ', sum(nums)/len
