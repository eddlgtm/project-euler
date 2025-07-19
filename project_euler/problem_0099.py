# https://projecteuler.net/problem=99

import math

data: list[int] = []
with open("data/99.txt", "r") as file:
    for line in file:
        data.append(list(map(int, line.strip().split(","))))

largest_value: int = -1
largest_line: int = -1


def find_larger_exponent(exponent1, exponent2):
    b1, e1 = exponent1
    b2, e2 = exponent2

    log1 = math.log10(b1)
    num1 = log1 * e1

    log2 = math.log10(b2)
    num2 = log2 * e2

    print(log1, num1, log2, num2)

    if num1 > num2:
        return exponent1
    else:
        return exponent2


largest_exponent = data[0]
largest_line = 0

for i, datum in enumerate(data):
    line = i + 1
    b, d = datum

    larger_exponent = find_larger_exponent(largest_exponent, (b, d))

    if largest_exponent == larger_exponent:
        pass
    else:
        largest_exponent = (b, d)
        largest_line = line

print(largest_line)
