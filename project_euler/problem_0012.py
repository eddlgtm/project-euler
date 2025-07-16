# https://projecteuler.net/problem=12


import math


def triangle_numbers():
    triangle = 0
    n = 1
    while True:
        triangle += n
        yield triangle
        n += 1

def divisors(number: int) -> list[int]:
    divs = []
    for x in range(1, int(math.sqrt(number)) + 1):
        if number % x == 0:
            divs.append(x)
            if x != number // x:
                divs.append(number // x)
    return divs

for triangle_number in triangle_numbers():
    d = divisors(triangle_number)
    print(f"{triangle_number} has {len(d)} divisors")
    if len(d) >= 500:
        print(d)
        print(triangle_number)
        break
