# https://projecteuler.net/problem=2


from sequences import fibonacci_sequence


print(
    sum(filter(lambda x: x % 2 == 0, fibonacci_sequence(stop=lambda x: x > 4_000_000)))
)
