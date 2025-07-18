# https://projecteuler.net/problem=28
# TODO: Unfinished

from enum import Enum


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


def create_spiral(size: int) -> list[list[int]]:
    spiral = [[]]
    x = 0
    y = 0
    number = 1
    direction = Direction.RIGHT

    spiral[x][y] = number

    number += 1
    direction = Direction.DOWN
    y += 1

    spiral[x][y] = number


print(create_spiral(2))
