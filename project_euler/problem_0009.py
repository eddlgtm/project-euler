# https://projecteuler.net/problem=9

from functools import reduce
from itertools import chain, product
from math import sqrt
from operator import mul


print(
    reduce(
        mul,
        chain.from_iterable(
            [
                [a, b, c]
                for a, b in filter(
                    lambda xy: xy[0] < xy[1], product(range(1, 1000), range(1, 1000))
                )
                if (c := sqrt(a * a + b * b))
                and c % 1 == 0
                and a < b < c
                and a + b + c == 1000
            ]
        ),
    )
)
