__author__ = 'tomasduhourq'

# After getting a handler h, h.read() returns
# all the characters in the file in a string.

def choose_file():
    try:
        handler = open(raw_input('Enter file name: '))
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
        if not line.startswith(pattern):
            continue
        print line.rstrip()

def write():
    file_out = open(raw_input('Enter a file name: '), 'w')
    line = raw_input('What to write?\n')
    file_out.write(line)
    file_out.close()

