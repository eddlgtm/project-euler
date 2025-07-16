# https://projecteuler.net/problem=92


def get_next_square_digit(number: int) -> int:
    return sum([int(x) * int(x) for x in str(number)])


count = 0

for i in range(1, 10000000):
    while True:
        if i == 1:
            break

        if i == 89:
            count += 1
            break

        i = get_next_square_digit(i)

print(count)
