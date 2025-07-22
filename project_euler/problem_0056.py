# https://projecteuler.net/problem=56

from itertools import product


def sum_digits_in_number(number: int) -> int:
    return sum([int(d) for d in str(number)])


assert sum_digits_in_number(371) == 11

combinations = list(product(range(100), range(100)))

assert combinations[0] == (0, 0)
assert combinations[-1] == (99, 99)

print(max(map(sum_digits_in_number, [pow(a, b) for a, b in combinations])))
