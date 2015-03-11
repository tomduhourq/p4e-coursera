__author__ = 'tomasduhourq'

from file_helper import choose_file

# 7.1 : print the contents of a file all to uppercase
for line in choose_file():
    print line.rstrip().upper()

# 7.2 : average of the line starting with a pattern
count = 0
total = 0.0
for line in choose_file():
    if line.find('X-DSPAM-Confidence:') == -1:
        continue
    count += 1
    total += float(line[line.find(':') + 1:].lstrip())
print 'Average spam confidence ', total/count