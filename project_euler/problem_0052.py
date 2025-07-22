# https://projecteuler.net/problem=52

from itertools import count


def numbers_contain_same_digits(numbers: list[int]) -> bool:
    sorted_numbers_as_strings = set()

    for number in numbers:
        number_as_list = str(sorted([d for d in str(number)]))
        sorted_numbers_as_strings.add(number_as_list)

    return len(sorted_numbers_as_strings) == 1


assert numbers_contain_same_digits([123, 321, 213]) == True
assert numbers_contain_same_digits([124, 321, 213]) == False

for n in count(1):
    numbers = [2 * n, 3 * n, 4 * n, 5 * n, 6 * n]
    if numbers_contain_same_digits(numbers):
        print(n)
        break
