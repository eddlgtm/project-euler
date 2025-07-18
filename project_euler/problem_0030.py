# https://projecteuler.net/problem=30


def is_sum_of_power_of_digits(number: int, exponent: int = 5) -> bool:
    return number == sum([pow(int(d), exponent) for d in str(number)])


assert is_sum_of_power_of_digits(9474, 4) == True

print(sum([x for x in range(10000000) if is_sum_of_power_of_digits(x) is True]))
