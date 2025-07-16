# https://projecteuler.net/problem=25


def fibonacci_sequence():
    a = 1
    b = 1
    sequence = [a, b]

    while True:
        if a < b:
            a += b
            sequence.append(a)
        else:
            b += a
            sequence.append(b)

        yield sequence[-1]


for i, number in enumerate(fibonacci_sequence(), 3):
    if len(str(number)) == 1000:
        print(i)
        break
