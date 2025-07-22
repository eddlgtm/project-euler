# https://projecteuler.net/problem=45


from sequences import (
    triangle_numbers_seq,
    pentagonal_numbers_seq,
    hexagonal_numbers_seq,
)

triangle_number = triangle_numbers_seq(285)
pentagonal_number = pentagonal_numbers_seq(165)
hexagonal_number = hexagonal_numbers_seq(143)

triangle_numbers = set()
pentagonal_numbers = set()
hexagonal_numbers = set()

for i in range(100000):
    triangle_numbers.add(next(triangle_number))
    pentagonal_numbers.add(next(pentagonal_number))
    hexagonal_numbers.add(next(hexagonal_number))

print(triangle_numbers.intersection(pentagonal_numbers, hexagonal_numbers))
