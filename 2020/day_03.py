from functools import reduce
from typing import List

INPUT = open("./input_files/input_03", "r").read().strip("\n")


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


def find_path(grid, x_step: int, y_step: int):
    path = list()
    x: int = x_step
    y: int = y_step
    while y < grid.size_y:
        path.append(grid.get((x % grid.size_x, y)))
        x += x_step
        y += y_step
    return ''.join(path)


def run_1():
    grid = Grid(INPUT)
    path = find_path(grid, 3, 1)

    return path.count('#')


def run_2():
    grid = Grid(INPUT)
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    paths = list()
    for x_step, y_step in slopes:
        paths.append(find_path(grid, x_step, y_step))
    return reduce(lambda x, y: x * y, [p.count('#') for p in paths])


print(run_1())
print(run_2())
