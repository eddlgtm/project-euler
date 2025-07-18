# https://projecteuler.net/problem=23

from itertools import product, starmap
from utils import proper_divisors
from operator import add


def is_abundent_number(number: int) -> bool:
    return number < sum(proper_divisors(number))


def get_abundent_numbers(limit: int) -> list[int]:
    abundent_numbers = []

    for number in range(limit):
        if is_abundent_number(number):
            abundent_numbers.append(number)

    return abundent_numbers


abundent_numbers = get_abundent_numbers(28123)
product_of_numbers = product(abundent_numbers, abundent_numbers)

all_numbers = set(range(28123))
abundent_sums = set(filter(lambda x: x <= 28123, starmap(add, product_of_numbers)))

print(sum(all_numbers - abundent_sums))
