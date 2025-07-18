# https://projecteuler.net/problem=29


from itertools import product, starmap


def distinct_powers(bases, exponents) -> set[int]:
    return set(starmap(pow, product(bases, exponents)))


print(len(distinct_powers(range(2, 101), range(2, 101))))
