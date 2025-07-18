# https://projecteuler.net/problem=34

from math import factorial


def is_sum_of_digit_factorials(number: int) -> bool:
    numbers = [int(d) for d in str(number)]
    sum_of_factorials = 0

    for d in numbers:
        sum_of_factorials += factorial(d)

    return sum_of_factorials == number


gap = 0
total = 0

# 1 and 2 are not digit factorials as there is no sum
# 1! == 1, 2! == 2
i = 3

# Once we don't see an occurence for 1,000,000 numbers
# we assume no more exist and break the loop
while gap < 1000000:
    if is_sum_of_digit_factorials(i):
        total += i
        gap = 0

    gap += 1
    i += 1

print(total)
