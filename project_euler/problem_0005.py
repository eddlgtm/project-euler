# https://projecteuler.net/problem=5

import itertools


def is_divisible_up_to_20(x: int) -> bool:
    for i in range(2, 20):
        if x % i != 0:
            return False

    return True


print(next(filter(is_divisible_up_to_20, itertools.count(start=20, step=20)), None))
