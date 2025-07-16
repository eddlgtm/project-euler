# https://projecteuler.net/problem=14


cache = {}


def get_collatz_sequence(n: int) -> list[int]:
    sequence = []

    while n != 1:
        if n in cache:
            return sequence + cache[n] + [1]
        else:
            cache[n] = sequence

        if n % 2 == 0:
            n = n // 2
            sequence.append(n)
        else:
            n = 3 * n + 1
            sequence.append(n)

    return sequence + [1]


collatz_sequences = []

for i in range(1, 1000000):
    collatz_sequences.append((len(get_collatz_sequence(i)), i))

print(max(collatz_sequences, key=lambda x: x[0]))
