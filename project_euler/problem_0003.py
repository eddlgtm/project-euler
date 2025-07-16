# https://projecteuler.net/problem=3

from utils import is_prime


def get_prime_factors(x: int, prime_factors: list[int] = []) -> list[int]:
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            prime_factors.append(i)
            return get_prime_factors(x // i, prime_factors)

    return prime_factors


print(max(get_prime_factors(600851475143)))
