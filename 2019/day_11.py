import itertools
from collections import defaultdict
from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_11", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

# INT_SEQUENCE = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


def confert_to_dict(int_sequence):
    result = defaultdict(int)

    for i, v in enumerate(int_sequence):
        result[i] = v
    return result


INT_SEQUENCE = confert_to_dict(INT_SEQUENCE)


def make_move(location, direction):
    x, y = location
    if direction == 0:
        return x, y + 1
    if direction == 1:
        return x + 1, y
    if direction == 2:
        return x, y - 1
    if direction == 3:
        return x - 1, y


def run_1():
    grid = defaultdict(int)
    location = (0, 0)
    direction = 0
    painted = set()
    int_sequence = copy(INT_SEQUENCE)
    IOPort.clear_instances()
    name = f'day_11_1'
    io = IOPort.get_instance(name)
    while io.finished is False:
        io.set_input(grid[location])
        run_program(name, int_sequence)
        color, move = io.outputs[-2:]
        grid[location] = color
        painted.add(location)
        direction = ((1 if move == 1 else -1) + direction) % 4
        location = make_move(location, direction)
        io.wait = False
    return len(painted)


def run_2():
    grid = defaultdict(int)
    location = (0, 0)
    grid[location] = 1
    direction = 0
    int_sequence = copy(INT_SEQUENCE)
    IOPort.clear_instances()
    name = f'day_11_2'
    io = IOPort.get_instance(name)
    while io.finished is False:
        io.set_input(grid[location])
        run_program(name, int_sequence)
        color, move = io.outputs[-2:]
        grid[location] = color
        direction = ((1 if move == 1 else -1) + direction) % 4
        location = make_move(location, direction)
        io.wait = False
    locations = grid.keys()
    xs = [x for x, y in locations]
    ys = [y for x, y in locations]
    for y in range(min(ys), max(ys) + 1)[::-1]:
        print(''.join(['X' if grid[x, y] == 1 else ' ' for x in range(min(xs), max(xs) + 1)]))

    return None


print(run_1())
print(run_2())
