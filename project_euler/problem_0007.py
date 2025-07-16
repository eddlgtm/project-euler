# https://projecteuler.net/problem=7

import itertools

from utils import is_prime

primes = []
numbers = itertools.count(0)

while len(primes) <= 10001:
    primes.append(next(filter(is_prime, numbers)))

print(max(primes))
