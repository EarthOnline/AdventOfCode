from functools import reduce
from itertools import chain, product

INPUT = open("./input_files/input_09", "r").read().strip("\n")
# INPUT = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
HMAP = [[int(x) for x in y] for y in INPUT.split("\n")]


ADJECENT = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def get_adjecent(grid, x, y):
    for d in ADJECENT:
        _x, _y = d(x, y)
        if _y < 0 or _y >= len(grid):
            continue
        if _x < 0 or _x >= len(grid[_y]):
            continue
        yield _x, _y


def is_lowest(grid, x, y) -> bool:
    current = grid[y][x]
    others = [grid[_y][_x] for _x, _y in get_adjecent(grid, x, y)]

    return current < min(others)


def run_1():
    lowests = [HMAP[y][x] for x, y in product(range(len(HMAP[0])), range(len(HMAP))) if is_lowest(HMAP, x, y)]

    return sum(map(lambda x: x + 1, lowests))


def create_basin(grid, x, y):
    if grid[y][x] == 9:
        return []
    coords = [(x, y)]
    grid[y][x] = 9
    coords.extend(chain.from_iterable(create_basin(grid, _x, _y) for _x, _y in get_adjecent(grid, x, y)))
    return coords


def run_2():
    lowests = [(x, y) for x, y in product(range(len(HMAP[0])), range(len(HMAP))) if is_lowest(HMAP, x, y)]
    basins = [create_basin(HMAP, l[0], l[1]) for l in lowests]
    sizes = [len(b) for b in basins]

    return reduce(lambda x, y: x * y, sorted(sizes)[-3:])


print(run_1())
print(run_2())
