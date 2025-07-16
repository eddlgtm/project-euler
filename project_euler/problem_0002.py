# https://projecteuler.net/problem=2


def fib(limit: int) -> list[int]:
    a = 1
    b = 1
    sequence = [a, b]

    while sequence[-1] <= limit:
        if a < b:
            a += b
            sequence.append(a)
        else:
            b += a
            sequence.append(b)

    return sequence


print(sum(filter(lambda x: x % 2 == 0, fib(4000000))))
