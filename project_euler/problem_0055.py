# https://projecteuler.net/problem=55

from utils import is_palindrome


def rotate_number(number: int) -> int:
    return int(str(number)[::-1])


def is_lychrel_number(number: int) -> bool:
    i = 0
    while i < 50:
        number += rotate_number(number)
        if is_palindrome(number):
            return True

        i += 1

    return False


assert is_palindrome(121) == True
assert rotate_number(123) == 321
assert is_lychrel_number(349) == True
assert is_lychrel_number(196) == False

print(sum([1 for number in range(10_001) if not is_lychrel_number(number)]))
