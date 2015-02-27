def create_list(s):
	l = []
	while True:
		e = raw_input('Number for list and -1 to find %s in given set: '% s) 
		try:
			n = int(e)
			if n != -1:
				l.append(n)
			else: break
		except:
			n = -1
			break
	return l
