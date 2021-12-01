import random
from collections import defaultdict
from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_15", "r").read().strip("\n")
INPUT_2 = open("input_files/input_15_2", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]


# INT_SEQUENCE = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


def confert_to_dict(int_sequence):
    result = defaultdict(int)

    for i, v in enumerate(int_sequence):
        result[i] = v
    return result


INT_SEQUENCE = confert_to_dict(INT_SEQUENCE)

MOVES = {1: lambda l: (l[0], l[1] - 1),
         2: lambda l: (l[0], l[1] + 1),
         3: lambda l: (l[0] - 1, l[1]),
         4: lambda l: (l[0] + 1, l[1])}


def print_grid(grid):
    xs = [x for x, y in grid.keys()]
    ys = [y for x, y in grid.keys()]

    for y in range(min(ys), max(ys) + 1):
        print(' '.join([grid.get((x, y), ' ') for x in range(min(xs), max(xs) + 1)]))


def make_grid():
    grid = dict()
    location = (0, 0)
    grid[location] = '+'

    int_sequence = copy(INT_SEQUENCE)
    IOPort.clear_instances()
    name = f'day_15_1'
    io = IOPort.get_instance(name)
    run_program(name, int_sequence)
    while not io.get_output() == 2:
        direction, step = random.choice(list(MOVES.items()))
        io.set_input(direction)
        io.wait = False
        run_program(name, int_sequence)
        result = io.get_output()
        if result == 0:
            grid[step(location)] = '#'
            continue
        location = step(location)
        if result == 1:
            continue
        if result == 2:
            grid[location] = 'X'
            break
    print_grid(grid)





def get_grid(map):
    grid = dict()
    for y, line in enumerate(map.split('\n')):
        for x, location in enumerate(line):
            if x % 2 == 0:
                grid[(x // 2, y)] = location

    return grid


def neigbour_has_step(grid, x, y):
    if grid[(x, y - 1)] in ['.', '+']:
        return True
    if grid[(x, y + 1)] in ['.', '+']:
        return True
    if grid[(x - 1, y)] in ['.', '+']:
        return True
    if grid[(x + 1, y)] in ['.', '+']:
        return True
    return False


def neigbour_has_oxy(grid, x, y):
    if grid[(x, y - 1)] in ['O', 'X']:
        return True
    if grid[(x, y + 1)] in ['O', 'X']:
        return True
    if grid[(x - 1, y)] in ['O', 'X']:
        return True
    if grid[(x + 1, y)] in ['O', 'X']:
        return True
    return False


def run_1():
    grid = get_grid(INPUT_2)
    steps = 0

    while len([v for v in grid.values() if v == 'X']):
        new_grid = {k: v for k, v in grid.items() if v not in [' ', 'X']}
        for location, value in [(l, v) for l, v in grid.items() if v in [' ', 'X']]:
            new_grid[location] = '.' if neigbour_has_step(grid, location[0], location[1]) else grid[location]
        grid = new_grid
        steps += 1
        # print_grid(grid)

    return steps


def run_2():
    grid = get_grid(INPUT_2)
    minutes = 0

    while len([v for v in grid.values() if v in [' ', '+']]):
        new_grid = {k: v for k, v in grid.items() if v not in [' ', '+']}
        for location, value in [(l, v) for l, v in grid.items() if v in [' ', '+']]:
            new_grid[location] = 'O' if neigbour_has_oxy(grid, location[0], location[1]) else ' '
        grid = new_grid
        minutes += 1
        # print_grid(grid)

    return minutes


print(run_1())
print(run_2())
