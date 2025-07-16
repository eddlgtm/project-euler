# https://projecteuler.net/problem=4


from itertools import product, starmap
from operator import mul


def is_pallindrone(number: int) -> bool:
    return str(number) == str(number)[::-1]


print(
    max(
        filter(
            is_pallindrone, (starmap(mul, product(range(100, 999), range(100, 999))))
        )
    )
)
