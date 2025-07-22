# https://projecteuler.net/problem=25

from sequences import fibonacci_sequence
from utils import last

print(
    last(
        [
            i
            for i, _ in enumerate(
                fibonacci_sequence(stop=lambda x: len(str(x)) == 1000)
            )
        ]
    )
)
