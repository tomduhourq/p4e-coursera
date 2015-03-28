__author__ = 'tomas'
from src.FilePractice.file_helper import choose_file

# Exercise 1
def process_line(l):
    for word in l:
        words[word] = words.get(word, 0) + 1

words = dict()
for line in open('../WordCount/quijote.txt'):
    process_line(line.rstrip())

# Exercise 2
def cut_condition_2(l):
    return l == '' or\
           len(l.split()) < 3 or \
           not l.startswith('From')

counts = dict()
for line in choose_file():
    if cut_condition_2(line): continue
    day = line.split()[2]
    counts[day] = counts.get(day, 0) + 1


# Exercise 3
def cut_condition_3(l):
    return l == '' or \
           not l.startswith('From:')

mails = dict()
for line in choose_file():
    if cut_condition_3(line): continue
    mail = line.split()[1]
    mails[mail] = mails.get(mail, 0) + 1

# Exercise 4
max_mail = None
max_count = None
for mail,count in mails.items():
    if max_count is None or count > max_count:
        max_mail = mail
        max_count = count

# Exercise 5
domains = dict()
for line in choose_file():
    if cut_condition_3(line): continue
    mail = line.split()[1]
    domain = mail[mail.find('@') + 1:]
    domains[domain] = domains.get(domain, 0) + 1
