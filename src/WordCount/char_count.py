__author__ = 'tomas'
import collections

# Three approaches to make a char count with a given string.
def map_char(char):
    return ord(char) - ord('a')


def char_count_file(file):
    for line in open(file):
        solver(line)


def solver(input):
    for word in input.lower().split():
        for char in list(word):
            # Special characters are not supported
            if map_char(char) not in range(0, 27): continue
            list_count[map_char(char)] += 1
            dict_count[char] = dict_count.get(char, 0) + 1


list_count = [0] * 26
dict_count = dict()
# Determine if the user wants to perform the count on file or string.
words = raw_input('Enter some words or a file: ')
if words.endswith('.txt'):
    # 1) Create 26 counters, traverse the string and
    # count the char occurrences and print' em all. Simple but long.
    char_count_file(words)
else:
    # 2) Create a list with 26 elements as counters, and
    # work it out with `ord`. When we print it, we won't see any keys,
    # just numbers with the totals.
    # 3) Create a dictionary with chars as keys,
    # really simple.
    solver(words)

ordered = collections.OrderedDict(sorted(dict_count.items()))

print list_count
print ordered