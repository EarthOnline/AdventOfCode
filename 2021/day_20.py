from itertools import product

from typing import Set, Tuple

INPUT = open("./input_files/input_20", "r").read().strip("\n")
# INPUT = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###"""
ALGORITHM = INPUT.split('\n\n')[0]
IMAGE = INPUT.split('\n\n')[1].split('\n')
IMAGE = set((x, y) for x, y in product(range(len(IMAGE)), range(len(IMAGE))) if IMAGE[y][x] == '#')

PIXELS = [
    lambda x, y: (x - 1, y - 1),
    lambda x, y: (x, y - 1),
    lambda x, y: (x + 1, y - 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y + 1),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y + 1),
]


def image_borders(image: Set[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    min_x = min(x for x, y in image) - 1
    max_x = max(x for x, y in image) + 2
    min_y = min(y for x, y in image) - 1
    max_y = max(y for x, y in image) + 2
    return min_x, max_x, min_y, max_y


def algorithm(x, y, image, negative=False):
    if negative:
        return ALGORITHM[int(''.join('0' if p(x, y) in image else '1' for p in PIXELS), 2)]
    return ALGORITHM[int(''.join('1' if p(x, y) in image else '0' for p in PIXELS), 2)]


def print_image(image):
    min_x, max_x, min_y, max_y = image_borders(image)

    print('---')
    for y in range(min_y, max_y):
        print(''.join('#' if (x, y) in image else '.' for x in range(min_x, max_x)))
    print('---')


def enhancement_pass(image, even_pass):
    compensate_infinity = ALGORITHM[0] == '#'
    min_x, max_x, min_y, max_y = image_borders(image)

    output = set()
    for x, y in product(range(min_x, max_x), range(min_y, max_y)):
        if even_pass and compensate_infinity:
            if algorithm(x, y, image) == '.':
                output.add((x, y))
        else:
            if algorithm(x, y, image, compensate_infinity) == '#':
                output.add((x, y))

    return output


def run_1():
    image = IMAGE

    for _ in range(2):
        image = enhancement_pass(image, _ % 2 == 0)
    return len(image)


def run_2():
    image = IMAGE

    for _ in range(50):
        image = enhancement_pass(image, _ % 2 == 0)
    return len(image)


print(run_1())
print(run_2())
