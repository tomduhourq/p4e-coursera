__author__ = 'tomasduhourq'

def choose_file():
    try:
        handler = open(raw_input('Enter a file name: '))
    except:
        print 'Invalid file'
        exit()
    return handler

def count():
    count = 0
    for line in choose_file():
        count += 1
    print 'File has: %d lines' % count

def search_for(pattern):
    for line in choose_file():
        if line.find(pattern) == -1:
            continue
        print line.rstrip()

def write():
    file_out = open(raw_input('Enter a file name: '), 'w')
    line = raw_input('What to write?\n')
    file_out.write(line)
    file_out.close()

