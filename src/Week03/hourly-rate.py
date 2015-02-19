__author__ = 'tomas'

hrs = raw_input('Enter Hours: ')
h = float(hrs)
rate = raw_input('Enter rate: ')
r = float(rate)

if h > 40:
    print 40*r + 1.5*r*(h-40)
else:
    print h*r