# https://projecteuler.net/problem=47

from utils import get_prime_factors


def get_distinct_prime_factors(prime_factors: list[int]) -> set[int]:
    return set(get_prime_factors(prime_factors))


consecutive_distinct_primes = set()
consecutive_distinct_primes_count = 0
i = 3

while consecutive_distinct_primes_count < 3:
    i += 1
    distinct_primes = get_distinct_prime_factors(get_prime_factors(i))

    if consecutive_distinct_primes.isdisjoint(distinct_primes):
        consecutive_distinct_primes = consecutive_distinct_primes.union(distinct_primes)
        consecutive_distinct_primes_count += 1

    else:
        consecutive_distinct_primes = set()
        consecutive_distinct_primes_count = 0


print(consecutive_distinct_primes)
print(i - 4)
