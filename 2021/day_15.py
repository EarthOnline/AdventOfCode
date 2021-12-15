from itertools import product, chain

from typing import List, Tuple

INPUT = open("./input_files/input_15", "r").read().strip("\n")
# INPUT = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""


def map_cave(cave: List[List[int]]) -> List[Tuple[Tuple[int, int], int]]:
    for x, y in product(range(len(cave[0])), range(len(cave))):
        yield (x, y), int(cave[y][x])


CAVE = dict(map_cave([[int(x) for x in l] for l in INPUT.split('\n')]))


def adjecent(x, y, max_x, max_y):
    if x > 0:
        yield x - 1, y
    if x < max_x:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < max_y:
        yield x, y + 1


def lowest_route(cave):
    max_x = max(x for x, y in cave.keys())
    max_y = max(y for x, y in cave.keys())

    current_positions = {k: set() for k in range(10)}
    current_positions[0].add((0, 0))
    been_there = set()
    step = 0
    while (max_x, max_y) not in current_positions[0]:
        step += 1
        new_positions = [p for p in current_positions.pop(0) if p not in been_there]

        for p in new_positions:
            been_there.add(p)

            for posibility in [c for c in adjecent(*p, max_x, max_y) if c not in been_there]:
                current_positions[cave[posibility]].add(posibility)

        current_positions = {k - 1: v for k, v in current_positions.items()}
        current_positions[9] = set()

    return step


def run_1():
    return lowest_route(CAVE)


def expand_cave(cave, size):
    max_x = max(x for x, y in cave.keys()) + 1
    max_y = max(y for x, y in cave.keys()) + 1
    first_cave = [list(chain.from_iterable([(cave[(x, y)] + r - 1) % 9 + 1 for x in range(max_x)]
                                           for r in range(size))) for y in range(max_y)]

    for r in range(size):
        for line in first_cave:
            yield [(x + r - 1) % 9 + 1 for x in line]


def run_2():
    return lowest_route(dict(map_cave(list(expand_cave(CAVE, 5)))))


print(run_1())
print(run_2())
