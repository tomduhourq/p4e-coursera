__author__ = 'tomas'

from src.FilePractice.file_helper import choose_file

invalid_words = {'que', 'de', 'el', 'la', 'los', 'y', 'a', 'en', 'no', 'se'}

words = [elem for elem in choose_file().read().split() if elem not in invalid_words]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

max_count = None
max_word = None

for word, count in counts.items():
    if max_count is None or count > max_count:
        max_word = word
        max_count = count

print max_word, max_count
