# https://projecteuler.net/problem=43

from itertools import permutations


def all_pandigital_numbers():
    pandigital_numbers = []
    for pandigital_number in list(permutations(range(0, 10), 10)):
        number_as_str = ""
        for digit in pandigital_number:
            number_as_str += str(digit)

            pandigital_numbers.append(int(number_as_str))

    return pandigital_numbers


def is_substring_divisible(number: int) -> bool:
    number = str(number)

    if len(number) != 10:
        return False

    substring_1 = int(number[1] + number[2] + number[3]) % 2 == 0
    substring_2 = int(number[2] + number[3] + number[4]) % 3 == 0
    substring_3 = int(number[3] + number[4] + number[5]) % 5 == 0
    substring_4 = int(number[4] + number[5] + number[6]) % 7 == 0
    substring_5 = int(number[5] + number[6] + number[7]) % 11 == 0
    substring_6 = int(number[6] + number[7] + number[8]) % 13 == 0
    substring_7 = int(number[7] + number[8] + number[9]) % 17 == 0

    return all(
        [
            substring_1,
            substring_2,
            substring_3,
            substring_4,
            substring_5,
            substring_6,
            substring_7,
        ]
    )


total = 0

for pandigital_number in all_pandigital_numbers():
    if is_substring_divisible(pandigital_number):
        total += pandigital_number

print(total)
