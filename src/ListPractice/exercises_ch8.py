__author__ = 'tomasduhourq'
from src.FilePractice.file_helper import choose_file

# Exercise 4
words = list()
for line in choose_file():
    for w in line.split():
        if not words.__contains__(w):
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
    e = raw_input('Enter number or "done":')
    if e == 'done' : break
    try:
        n = float(e)
    except:
        print 'You entered an invalid number'
        exit()
    nums = nums + [n]

print 'Maximum: ', max(nums)
print 'Minimum: ', min(nums)
