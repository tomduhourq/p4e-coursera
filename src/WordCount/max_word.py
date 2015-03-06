__author__ = 'tomas'

name = raw_input('Enter file: ')
handle = open(name, 'r')
text = handle.read()

invalid_words = {'que', 'de', 'el', 'la', 'los', 'y', 'a', 'en', 'no', 'se'}

words = [elem for elem in text.split() if elem not in invalid_words]
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

max_count = None
max_word = None

for word, count in counts.items():
    if max_count is None or count > max_count:
        max_word = word
        max_count = count

print max_word, max_count
