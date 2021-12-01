from collections import defaultdict
from typing import Dict, Tuple, List

INPUT = open("./input_files/input_18", "r").read().strip("\n")

ON = '#'
OFF = '.'


def get_grid() -> Dict[Tuple[int, int], bool]:
    grid = defaultdict(int)
    for y, line in enumerate(INPUT.split("\n")):
        for x, light in enumerate(line):
            grid[(x, y)] = light == ON
    return grid


GRID = get_grid()


def get_neighbours(light: Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = light
    return [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]


def update(grid: Dict[Tuple[int, int], bool]) -> Dict[Tuple[int, int], bool]:
    new_grid = defaultdict(int)
    for y in range(100):
        for x in range(100):
            light = (x, y)
            state = grid[light]
            neighbours = sum([grid[l] for l in get_neighbours(light)])
            if state:
                new_grid[light] = neighbours in [2, 3]
            else:
                new_grid[light] = neighbours == 3
    return new_grid


def run_1():
    grid = GRID
    for x in range(100):
        grid = update(grid)
    return sum(grid.values())


def run_2():
    grid = GRID
    grid[(0, 0)] = grid[(0, 99)] = grid[(99, 0)] = grid[(99, 99)] = True
    for x in range(100):
        grid = update(grid)
        grid[(0, 0)] = grid[(0, 99)] = grid[(99, 0)] = grid[(99, 99)] = True
    return sum(grid.values())


print(run_1())
print(run_2())
