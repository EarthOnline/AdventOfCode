from copy import copy, deepcopy
from math import sqrt

INPUT = open("./input_files/input_20", "r").read().strip("\n")
INPUT = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


class Tile:
    def __init__(self, image: str):
        self.sequence = int(image.split("\n")[0][-5:-1])
        self.image = image.split("\n")[1:]

    def flip(self):
        self.image = [x[::-1] for x in self.image]

    def rotate(self):
        self.image = ["".join(x[r] for x in self.image[::-1]) for r in range(len(self.image))]

    @property
    def real_image(self):
        return ["".join([y for y in x[1:-1]]) for x in self.image[1:-1]]

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
            e="".join([x[0] for x in self.image]),
            s=self.image[-1],
            w="".join([x[-1] for x in self.image])
        )

    def match(self, image):
        my_borders = self.borders
        other_borders = image.borders

        return {
            'n': my_borders['n'] == other_borders['s'],
            's': my_borders['s'] == other_borders['s'],
            'e': my_borders['e'] == other_borders['w'],
            'w': my_borders['w'] == other_borders['e']
        }


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

    for x, row in enumerate(image.split('\n')):
        for y, mark in enumerate(row):
            if mark == '#':
                checks.append((x,y))

    return checks


CHECK = build_check(MONSTER)


def solver(arangement, tiles):
    # print(arangement, tiles)
    grid = deepcopy(arangement)
    tiles = copy(tiles)
    for x, row in enumerate(grid):
        for y, image in enumerate(row):
            if image is not None:
                continue

            for tile in tiles:
                for action in ACTIONS:
                    action(tile)
                    borders = tile.borders
                    if (x == 0 or borders['n'] == grid[x-1][y].borders['s']) \
                            and (y == 0 or borders['w'] == grid[x][y-1].borders['e']):
                        grid[x][y] = tile
                        solve = solver(grid, [t for t in tiles if t.sequence != tile.sequence])

                        if solve:
                            return solve
            return False
    return grid


def image_builder(grid):
    image_grid = [[y.real_image for y in x] for x in grid]

    image = []
    for i in image_grid:
        for r in range(len(image_grid[0][0])):
            image.append("".join([x[r] for x in i]))

    return image


def hunt_monster(image):
    pass


size = int(sqrt(len(TILES)))
grid = [[None for y in range(size)] for x in range(size)]
solve = solver(grid, TILES)


def run_1():
    return solve[0][0].sequence * solve[0][-1].sequence * solve[-1][0].sequence * solve[-1][-1].sequence


def run_2():
    print(MONSTER)
    print(CHECK)
    image = image_builder(solve)
    return image



print(run_1())
print(run_2())