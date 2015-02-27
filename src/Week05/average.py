from list_helper import create_list

count = 0
sum = 0
for elem in create_list('max'):
	count += 1
	sum += elem
print 'average is ',sum/count