# https://projecteuler.net/problem=21

from utils import proper_divisors


def d(n: int) -> int:
    return sum(proper_divisors(n))


print(sum([a + b for a in range(10000) if (b := d(a)) and a > b and d(b) == a]))
