# https://projecteuler.net/problem=3

primes = set()


def is_prime(x: int) -> bool:
    if x == 1:
        return False

    if x == 2:
        return True

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


def get_prime_factors(x: int, prime_factors: list[int] = []) -> list[int]:
    for i in range(2, x + 1):
        if x % i == 0 and (i in primes or is_prime(i)):
            prime_factors.append(i)
            primes.add(i)
            return get_prime_factors(x // i, prime_factors)

    return prime_factors


print(max(get_prime_factors(600851475143)))
