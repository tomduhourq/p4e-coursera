from src.Week05.list_helper import create_list

e = raw_input('Elem to search: ')
try:
    n = int(e)
except:
    n = -1
if n != -1:
    found = False
    for elem in create_list('elem'):
        if elem == n:
            found = True
            break
    print 'found is ', found