import copy

from copy import copy

INPUT = open("./input_files/input_25", "r").read().strip("\n")
# INPUT = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>"""


def read_herds(text):
    cucumbers = {}
    for y, line in enumerate(text.splitlines()):
        for x, cucumber in enumerate(line):
            if cucumber in ['>', 'v']:
                cucumbers[(x, y)] = cucumber
    return cucumbers, x + 1, y + 1


CUCUMBERS, MAX_X, MAX_Y = read_herds(INPUT)


def print_floor(cucumbers):
    for y in range(MAX_Y):
        print(''.join(cucumbers.get((x, y), '.') for x in range(MAX_X)))
    print('---')


def run_1():
    before = {}
    after = copy(CUCUMBERS)

    def move(floor, x, y, direction, turn):
        if direction != turn:
            return x, y
        if direction == '>':
            new = (x + 1) % MAX_X, y
        if direction == 'v':
            new = x, (y + 1) % MAX_Y
        if new in floor.keys():
            return x, y
        return new

    moves = 0
    while before != after:
        # print('--', moves, '--')
        # print_floor(after)
        moves += 1
        before = after
        between = {move(before, x, y, c, '>'): c for (x, y), c in before.items()}
        after = {move(between, x, y, c, 'v'): c for (x, y), c in between.items()}

    return moves


def run_2():
    return


print(run_1())
print(run_2())
