from itertools import product

from copy import deepcopy

from typing import List, Tuple

INPUT = open("./input_files/input_11", "r").read().strip("\n")
# INPUT = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""
OCTOPUSES = [[int(x) for x in r] for r in INPUT.split('\n')]


def get_adjecent(x: int, y: int) -> List[Tuple[int, int]]:
    adjecent = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]
    return [(x, y) for x, y in adjecent if 0 <= x < 10 and 0 <= y < 10]


def run_flashy_round(grid):
    to_increase = [(x, y) for x, y in product(range(10), range(10))]
    has_flashed = set()

    while len(to_increase) > 0:
        x, y = to_increase.pop()
        grid[y][x] += 1
        if grid[y][x] > 9 and (x, y) not in has_flashed:
            has_flashed.add((x, y))
            to_increase.extend(get_adjecent(x, y))

    for x, y in has_flashed:
        grid[y][x] = 0

    return len(has_flashed)


def run_1():
    grid = deepcopy(OCTOPUSES)
    return sum(map(lambda x: run_flashy_round(grid), range(100)))


def run_2():
    grid = deepcopy(OCTOPUSES)
    step = 0

    while True:
        step += 1

        if run_flashy_round(grid) == 100:
            break

    return step


print(run_1())
print(run_2())
