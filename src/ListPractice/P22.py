__author__ = 'tomas'


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2) + 1):
        yield chr(c)

# Generate alphabet with values
alph = {}
value = 0
for c in char_range('A', 'Z'):
    value += 1
    alph[c] = value
# Generate source names list
names = list()
for line in open('names.txt'):
    line = line.split(',')
    names.extend(line)
names.sort()


def get_value(n):
    s = 0
    for c in n[1: len(n) - 1]:
        s += alph[c]
    return s

# Map each names
value = 0
sum = 0
for name in names:
    value += 1
    sum += get_value(name) * value

print sum
