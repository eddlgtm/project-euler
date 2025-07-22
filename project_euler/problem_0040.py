# https://projecteuler.net/problem=40


def create_champernownes_constant(length: int) -> float:
    constant = ""

    i = 1
    while len(constant) < length:
        constant += str(i)
        i += 1

    return constant


c = create_champernownes_constant(1_000_000)

numbers = list(map(int, [c[0], c[9], c[99], c[999], c[9_999], c[99_999], c[999_999]]))

result = 1
for number in numbers:
    result *= number

print(result)
