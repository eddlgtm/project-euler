# https://projecteuler.net/problem=12


import math


def triangle_numbers():
    triangle = 0
    n = 1
    while True:
        triangle += n
        yield triangle
        n += 1


def num_of_divisors(number: int) -> list[int]:
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
    return len(divs)


for triangle_number in triangle_numbers():
    if num_of_divisors(triangle_number) >= 500:
        print(triangle_number)
        break
