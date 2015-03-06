__author__ = 'tomasduhourq'


def get_file():
    name = raw_input('Enter file: ')
    handle = open(name, 'r')
    return handle.read().split()