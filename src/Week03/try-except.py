__author__ = 'tomas'

grade = raw_input('Enter a grade:')

try:
    f_grade = float(grade)

except:
    f_grade = -1.0

if f_grade > 1.0 or f_grade < 0.0:
    print 'Grade out of range'
elif f_grade >= 0.9:
    print 'A'
elif f_grade >= 0.8:
    print 'B'
elif f_grade >= 0.7:
    print 'C'
elif f_grade >= 0.6:
    print 'D'
else:
    print 'F'