from copy import copy
from itertools import permutations, chain

INPUT = open("./input_files/input_17", "r").read().strip("\n")
# INPUT = """.#.
# ..#
# ###"""
NEIGHBORS_3D = set(permutations([-1, -1, -1, 0, 0, 1, 1, 1], 3))


def get_neighbors_3d(x, y, z):
    return [(x + _x, y + _y, z + _z) for _x, _y, _z in NEIGHBORS_3D]


class Grid3D(set):
    def set_from_map(self, map):
        for y, line in enumerate(map.split('\n')):
            for x, location in enumerate(line):
                if location == '#':
                    self.add((x, y, 0))

    @property
    def items_to_inspect(self):
        return set(chain.from_iterable([get_neighbors_3d(x, y, z) for x, y, z in self])).union(self)

    def is_active(self, x, y, z):
        return (x, y, z) in self

    def new_value(self, x, y, z):
        active = self.is_active(x, y, z)
        neighbors = [self.is_active(*n) for n in get_neighbors_3d(x, y, z)].count(True)
        return neighbors in [2, 3] if active else neighbors == 3

    def next_round(self):
        new_grid = copy(self)
        new_grid.clear()
        [new_grid.add(c) for c in self.items_to_inspect if self.new_value(*c)]
        return new_grid


def run_1():
    grid = Grid3D()
    grid.set_from_map(INPUT)
    for _ in range(6):
        grid = grid.next_round()
    return len(grid)


NEIGHBORS_4D = set(permutations([-1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1], 4))


def get_neighbors_4d(x, y, z, w):
    return [(x + _x, y + _y, z + _z, w + _w) for _x, _y, _z, _w in NEIGHBORS_4D]


class Grid4D(set):
    def set_from_map(self, map):
        for y, line in enumerate(map.split('\n')):
            for x, location in enumerate(line):
                if location == '#':
                    self.add((x, y, 0, 0))

    @property
    def items_to_inspect(self):
        return set(chain.from_iterable([get_neighbors_4d(x, y, z, w) for x, y, z, w in self])).union(self)

    def is_active(self, x, y, z, w):
        return (x, y, z, w) in self

    def new_value(self, x, y, z, w):
        active = self.is_active(x, y, z, w)
        neighbors = [self.is_active(*n) for n in get_neighbors_4d(x, y, z, w)].count(True)
        return neighbors in [2, 3] if active else neighbors == 3

    def next_round(self):
        new_grid = copy(self)
        new_grid.clear()
        [new_grid.add(c) for c in self.items_to_inspect if self.new_value(*c)]
        return new_grid


def run_2():
    grid = Grid4D()
    grid.set_from_map(INPUT)
    for _ in range(6):
        grid = grid.next_round()
    return len(grid)


print(run_1())
print(run_2())
