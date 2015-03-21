__author__ = 'tomas'

# Using list comprehensions to generate math sets.
squares = [x**2 for x in range(10)]
powers_2 = [2**i for i in range(13)]
filter_even = [x for x in powers_2 if x % 2 == 0]

# Generating primes negating the ones which aren't prime.
noprimes = set([j for i in range(2, 8) for j in range(i*2, 10000, i)])
primes = [x for x in range(2, 10000) if x not in noprimes]

print primes