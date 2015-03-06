from src.Week05.list_helper import create_list

min = None
for elem in create_list('min'):
	if min is None or elem < min:
		min = elem
print 'smallest is ',min