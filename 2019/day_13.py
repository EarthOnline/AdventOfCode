import itertools
from collections import defaultdict
from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_13", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

# INT_SEQUENCE = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


def confert_to_dict(int_sequence):
    result = defaultdict(int)

    for i, v in enumerate(int_sequence):
        result[i] = v
    return result


INT_SEQUENCE = confert_to_dict(INT_SEQUENCE)


def run_1():
    int_sequence = copy(INT_SEQUENCE)
    IOPort.clear_instances()
    name = f'day_13_1'
    io = IOPort.get_instance(name)
    run_program(name, int_sequence)

    screen_updates = [io.outputs[i * 3: i * 3 + 3] for i in range(len(io.outputs) // 3)]
    screen = dict()
    max_x = max([x for x, y, t in screen_updates])
    max_y = max([y for x, y, t in screen_updates])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            screen[(x, y)] = 0

    for x, y, t in screen_updates:
        screen[(x, y)] = t

    return len([t for t in screen.values() if t == 2])


def run_2():
    int_sequence = copy(INT_SEQUENCE)
    int_sequence[0] = 2
    IOPort.clear_instances()
    name = f'day_13_2'
    io = IOPort.get_instance(name)

    score = 0

    while not io.finished:
        run_program(name, int_sequence)

        screen_updates = [io.outputs[i * 3: i * 3 + 3] for i in range(len(io.outputs) // 3)]

        if io.wait:
            location_paddle = [x for x, y, t in screen_updates[::-1] if t == 3]
            location_paddle = 0 if len(location_paddle) == 0 else location_paddle[0]
            location_ball = [x for x, y, t in screen_updates[::-1] if t == 4]
            location_ball = 0 if len(location_ball) == 0 else location_ball[0]
            io.set_input(0 if location_ball == location_paddle else -1 if location_ball < location_paddle else 1)
            io.outputs = list()
            io.wait = False
        if io.finished:
            score = [t for x, y, t in screen_updates[::-1] if x == -1][0]
    return score


print(run_1())
print(run_2())
