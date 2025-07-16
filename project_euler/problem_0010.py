# https://projecteuler.net/problem=10

from utils import is_prime

print(sum([x for x in range(2000000) if is_prime(x)]))