from src.Week05.list_helper import create_list

max = None
for elem in create_list('max'):
	if max is None or elem > max:
		max = elem
print 'largest is ',max