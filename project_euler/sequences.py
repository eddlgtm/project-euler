from collections.abc import Callable, Generator


def running_total_sequence(
    func: Callable[[int], int],
    starting_number: int = 1,
    stopping_func: Callable[[int], int] = False,
) -> Generator[int, None, bool]:
    running_total = 0
    n = starting_number
    while True:
        running_total = func(n)
        if stopping_func and stopping_func(n):
            return False
        yield running_total
        n += 1


def fibonacci_sequence(
    stop: Callable[[int], bool] = False,
) -> Generator[int, None, bool]:
    a = 0
    b = 1
    sequence = []

    while True:
        if len(sequence) == 0:
            sequence = [0]

        elif len(sequence) == 1:
            sequence.append(1)

        elif a < b:
            a += b
            sequence.append(a)

        else:
            b += a
            sequence.append(b)

        if stop and stop(sequence[-1]):
            return False

        yield sequence[-1]


def triangle_numbers_seq(
    starting_number: int = 1, stopping_func: Callable[[int], int] = False
):
    return running_total_sequence(
        lambda n: n * (n + 1) // 2,
        starting_number=starting_number,
        stopping_func=stopping_func,
    )


def pentagonal_numbers_seq(
    starting_number: int = 1, stopping_func: Callable[[int], int] = False
):
    return running_total_sequence(
        lambda n: n * (3 * n - 1) // 2,
        starting_number=starting_number,
        stopping_func=stopping_func,
    )


def hexagonal_numbers_seq(
    starting_number: int = 1, stopping_func: Callable[[int], int] = False
):
    return running_total_sequence(
        lambda n: n * (2 * n - 1),
        starting_number=starting_number,
        stopping_func=stopping_func,
    )
