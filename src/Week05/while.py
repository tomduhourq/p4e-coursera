while True:
	line = raw_input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print 'Your line was', line
print 'Done!'
