# https://projecteuler.net/problem=36


def is_double_palindrome(number: int) -> bool:
    base_2_palindrome = str(bin(number)[2:]) == str(bin(number)[2:])[::-1]
    base_10_palindrome = str(number) == str(number)[::-1]
    return base_2_palindrome and base_10_palindrome


total = 0
for number in range(1000000):
    if is_double_palindrome(number):
        total += number

print(total)
