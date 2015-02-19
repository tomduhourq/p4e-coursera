__author__ = 'tomas'


def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + 1.5 * (h - 40) * r


hrs = raw_input("Enter Hours:")
hours = float(hrs)
rt = raw_input("Enter Rate per hour:")
rate = float(rt)
print computepay(hours, rate)