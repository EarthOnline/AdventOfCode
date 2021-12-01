from copy import copy
from typing import List

INPUT = open("./input_files/input_11", "r").read().strip("\n")


ADJECENT = [lambda x, y: (x-1, y-1), lambda x, y: (x, y-1), lambda x, y: (x+1, y-1),
            lambda x, y: (x-1, y),                          lambda x, y: (x+1, y),
            lambda x, y: (x-1, y+1), lambda x, y: (x, y+1), lambda x, y: (x+1, y+1)]


class Grid(dict):
    def __init__(self, map):
        super().__init__()

        for y, line in enumerate(map.split('\n')):
            for x, location in enumerate(line):
                self[(x, y)] = location

    @property
    def _xs(self) -> List:
        return [x for x, y in self.keys()]

    @property
    def min_x(self) -> int:
        return min(self._xs)

    @property
    def max_x(self) -> int:
        return max(self._xs)

    @property
    def size_x(self) -> int:
        return self.max_x + 1

    @property
    def _ys(self) -> List:
        return [y for x, y in self.keys()]

    @property
    def min_y(self) -> int:
        return min(self._ys)

    @property
    def max_y(self) -> int:
        return max(self._ys)

    @property
    def size_y(self) -> int:
        return self.max_y + 1

    def __str__(self):
        result = list()
        for y in range(self.min_y, self.size_y):
            result.append(' '.join([self.get((x, y), ' ') for x in range(self.min_x, self.size_x)]))
        return '\n'.join(result)


def check_adjecent(grid, x, y):
    return ''.join([grid.get(a(x, y), '') for a in ADJECENT])


def change_seats(grid):
    new_grid = copy(grid)
    for k, v in grid.items():
        if v == 'L' and check_adjecent(grid, *k).count('#') == 0:
            new_grid[k] = '#'
            continue

        if v == '#' and check_adjecent(grid, *k).count('#') >= 4:
            new_grid[k] = 'L'
            continue
    return new_grid


def run_1():
    old_grid = Grid(INPUT)
    while True:
        new_grid = change_seats(old_grid)
        if old_grid == new_grid:
            break
        old_grid = new_grid

    return str(new_grid).count('#')


def check_in_sight(grid, x, y):
    result = list()
    for direction in ADJECENT:
        _x, _y = direction(x, y)
        seat = grid.get((_x, _y), '')
        while seat == '.':
            _x, _y = direction(_x, _y)
            seat = grid.get((_x, _y), '')
        result.append(seat)

    return ''.join(result)


def change_seats_2(grid):
    new_grid = copy(grid)
    for k, v in grid.items():
        if v == 'L' and check_in_sight(grid, *k).count('#') == 0:
            new_grid[k] = '#'
            continue

        if v == '#' and check_in_sight(grid, *k).count('#') >= 5:
            new_grid[k] = 'L'
            continue
    return new_grid


def run_2():
    old_grid = Grid(INPUT)
    while True:
        new_grid = change_seats_2(old_grid)
        if old_grid == new_grid:
            break
        old_grid = new_grid

    return str(new_grid).count('#')


print(run_1())
print(run_2())
