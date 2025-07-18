# https://projecteuler.net/problem=31
# TODO: Unfinished

from itertools import combinations_with_replacement


coins = [1, 2, 5, 10, 20, 50, 100]


print(
    len(
        [
            combination
            for combination in combinations_with_replacement(coins, 200)
            if sum(combination) == 200
        ]
    )
    + 1
)
