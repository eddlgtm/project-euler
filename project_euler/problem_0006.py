# https://projecteuler.net/problem=6

sum_of_the_squares = sum([x * x for x in range(1, 101)])
square_of_the_sums = sum(range(1, 101)) ** 2


print(square_of_the_sums - sum_of_the_squares)
