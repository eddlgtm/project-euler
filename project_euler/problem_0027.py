# https://projecteuler.net/problem=27

from itertools import product

from utils import is_prime


def quadratic_formula(n, a, b):
    return pow(n, 2) + (a * n) + b


ab_pairs = list(product(range(-1000, 1000), range(-1001, 1001)))

n = 0
consecutive_primes = 0
longest_consecutive_primes = 0
largest_a = 0
largest_b = 0

for a, b in ab_pairs:
    while is_prime(quadratic_formula(n, a, b)):
        n += 1
        consecutive_primes += 1

    if consecutive_primes > longest_consecutive_primes:
        longest_consecutive_primes = consecutive_primes
        largest_a = a
        largest_b = b

    n = 0
    consecutive_primes = 0

print(largest_a * largest_b)
