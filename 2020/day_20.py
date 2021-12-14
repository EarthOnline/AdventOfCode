from copy import copy, deepcopy
from itertools import chain, product
from math import sqrt

INPUT = open("./input_files/input_20", "r").read().strip("\n")
# INPUT = """Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###..."""


class Tile:
    def __init__(self, image: str = None):
        if image is None:
            self.sequence = 0
            self.image = None
        else:
            text = image.split("\n")
            self.sequence = int(text[0][-5:-1])
            self.image = text[1:]

    def flip(self):
        self.image = [x[::-1] for x in self.image]

    def rotate(self):
        self.image = ["".join(x[r] for x in self.image[::-1]) for r in range(len(self.image))]

    @property
    def real_image(self):
        return ["".join(y[1:-1]) for y in self.image[1:-1]]

    def __str__(self):
        return "\n".join(self.image)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return str(self.sequence)

    @property
    def borders(self):
        return dict(
            n=self.image[0],
            e="".join([y[-1] for y in self.image]),
            s=self.image[-1],
            w="".join([y[0] for y in self.image])
        )

    # def match(self, image):
    #     my_borders = self.borders
    #     other_borders = image.borders
    #
    #     return {
    #         'n': my_borders['n'] == other_borders['s'],
    #         's': my_borders['s'] == other_borders['n'],
    #         'e': my_borders['e'] == other_borders['w'],
    #         'w': my_borders['w'] == other_borders['e']
    #     }


ACTIONS = [lambda x: x.rotate(),
           lambda x: x.rotate(),
           lambda x: x.rotate(),
           lambda x: x.rotate(),
           lambda x: x.flip(),
           lambda x: x.rotate(),
           lambda x: x.rotate(),
           lambda x: x.rotate()]

TILES = [Tile(t) for t in INPUT.split("\n\n")]

MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """


def build_check(image):
    checks = []

    for y, row in enumerate(image.split('\n')):
        for x, mark in enumerate(row):
            if mark == '#':
                checks.append((x, y))

    return checks


CHECK = build_check(MONSTER)


def solver(arangement, tiles):
    grid = deepcopy(arangement)
    tiles = copy(tiles)
    for y, row in enumerate(grid):
        for x, image in enumerate(row):
            if image is not None:
                continue

            for tile in tiles:
                for action in ACTIONS:
                    action(tile)
                    borders = tile.borders
                    if (y == 0 or borders['n'] == grid[y-1][x].borders['s']) \
                            and (x == 0 or borders['w'] == grid[y][x-1].borders['e']):
                        grid[y][x] = tile
                        solve = solver(grid, [t for t in tiles if t.sequence != tile.sequence])

                        if solve:
                            return solve
            return False
    return grid


def solve_grid():
    size = int(sqrt(len(TILES)))
    grid = [[None for _ in range(size)] for _ in range(size)]
    return solver(grid, TILES)


def image_builder(grid):
    image_grid = [[x.real_image for x in y] for y in grid]

    image = []
    for i in image_grid:
        for r in range(len(image_grid[0][0])):
            image.append("".join([x[r] for x in i]))

    return image


def hunt_monster(tile):
    trials = list(product(range(len(tile.image[0]) - 20 + 1), range(len(tile.image) - 3 + 1)))
    main_check = build_check(MONSTER)

    for action in ACTIONS:
        action(tile)
        found = False

        for x, y in trials:
            check = [tile.image[y + _y][x + _x] in ['#', '0'] for _x, _y in main_check]

            if len(check) == sum(check):
                found = True
                for _x, _y in main_check:
                    tile.image[y + _y] = tile.image[y + _y][:x + _x] + '0' + tile.image[y + _y][x + _x + 1:]

        if found:
            return tile


def run_1():
    solve = solve_grid()
    return solve[0][0].sequence * solve[0][-1].sequence * solve[-1][0].sequence * solve[-1][-1].sequence


def run_2():
    tile = Tile()
    tile.image = image_builder(solve_grid())
    tile = hunt_monster(tile)
    return sum(x == '#' for x in chain.from_iterable(tile.image))


print(run_1())
print(run_2())
