import string
from itertools import chain

INPUT = open("./input_files/input_12", "r").read().strip("\n")


def create_grid():
    for y, row in enumerate(INPUT.split('\n')):
        for x, value in enumerate(row):
            yield (x, y), string.ascii_lowercase.index(value) + 1 if value in string.ascii_lowercase else value


AREA = dict(create_grid())

MOVES = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def hight_translation(value):
    match value:
        case 'S':
            _value = 1
        case 'E':
            _value = 26
        case _:
            _value = value
    return _value


def solve_path(start_elevation, end_elevation):
    start = tuple(k for k, v in AREA.items() if v == start_elevation)
    end = tuple(k for k, v in AREA.items() if v == end_elevation)

    visited = set(end)
    currents = end
    steps = 0
    while not visited.intersection(start):
        steps += 1

        currents = set(chain.from_iterable(
            [p for p in [m(*c) for m in MOVES] if
             p in AREA and hight_translation(AREA[c]) <= hight_translation(AREA[p]) + 1] for c in currents))
        visited.update(currents)

    return steps


def run_1():
    return solve_path('S', 'E')


def run_2():
    return solve_path(1, 'E')


print(run_1())
print(run_2())
