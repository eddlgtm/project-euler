import math


def is_prime(x: int) -> bool:
    if x == 1:
        return False

    if x == 2:
        return True

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


def is_pandigital(number: int) -> bool:
    return list(set([int(x) for x in str(number)])) == list(
        range(1, len(str(number)) + 1)
    )


def get_prime_factors(x: int, prime_factors: list[int] = []) -> list[int]:
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            prime_factors.append(i)
            return get_prime_factors(x // i, prime_factors)

    return prime_factors


def divisors(number: int) -> list[int]:
    # Divisors come in pairs
    # 1 and 28
    # 2 and 14
    # 4 and 7

    divs = []
    for x in range(1, int(math.sqrt(number)) + 1):
        if number % x == 0:
            divs.append(x)
            if x != number // x:
                divs.append(number // x)
    return divs


def proper_divisors(number: int) -> list[int]:
    # Divisors come in pairs
    # 1 and 28
    # 2 and 14
    # 4 and
    # Proper divisors do not include itself (so not 28)

    if number == 0 or number == 1:
        return []

    divs = []
    for x in range(1, int(math.sqrt(number)) + 1):
        if number % x == 0:
            divs.append(x)
            if x != number // x:
                divs.append(number // x)

    divs.remove(number)

    return divs
