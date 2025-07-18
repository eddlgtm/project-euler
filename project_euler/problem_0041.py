# https://projecteuler.net/problem=41

from utils import is_pandigital, is_prime

largest_pandigital_prime = -1

for i in range(1_000_000_000):
    if is_pandigital(i) and is_prime(i):
        largest_pandigital_prime = i

print(largest_pandigital_prime)
