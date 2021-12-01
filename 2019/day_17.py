import random
from collections import defaultdict
from copy import copy
from functools import reduce

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_17", "r").read().strip("\n")
# INPUT_2 = open("input_files/input_15_2", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]


# INT_SEQUENCE = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


def confert_to_dict(int_sequence):
    result = defaultdict(int)

    for i, v in enumerate(int_sequence):
        result[i] = v
    return result


INT_SEQUENCE = confert_to_dict(INT_SEQUENCE)


def make_grid():
    int_sequence = copy(INT_SEQUENCE)
    IOPort.clear_instances()
    name = f'day_17_1'
    io = IOPort.get_instance(name)
    run_program(name, int_sequence)
    return ''.join([chr(o) for o in io.outputs])


SCAFOLDING_INPUT = make_grid()
print(SCAFOLDING_INPUT)


def get_scafolding(input):
    result = dict()
    for y, row in enumerate(input.split('\n')):
        for x, value in enumerate(row):
            result[(x, y)] = value
    return result


SCAFOLDING = get_scafolding(SCAFOLDING_INPUT)


def is_crossing(x, y):
    tries = [(x, y), (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    return reduce(lambda a, b: a & b, [SCAFOLDING.get(l, ' ') == '#' for l in tries])


def run_1():
    return sum([l[0] * l[1] for l in SCAFOLDING.keys() if is_crossing(l[0], l[1])])


def run_2():
    int_sequence = copy(INT_SEQUENCE)
    int_sequence[0] = 2

    inst = 'R,10,L,8,R,10,R,4,' \
           'L,6,L,6,R,10,' \
           'R,10,L,8,R,10,R,4,' \
           'L,6,R,12,R,12,R,10,' \
           'L,6,L,6,R,10,' \
           'L,6,R,12,R,12,R,10,' \
           'R,10,L,8,R,10,R,4,' \
           'L,6,L,6,R,10,' \
           'R,10,L,8,R,10,R,4,' \
           'L,6,R,12,R,12,R,10'

    main = 'A,B,A,C,B,C,A,B,A,C\n'
    func_a = 'R,10,L,8,R,10,R,4\n'
    func_b = 'L,6,L,6,R,10\n'
    func_c = 'L,6,R,12,R,12,R,10\n'
    video = 'n\n'

    input = main + func_a + func_b + func_c + video
    input = [ord(c) for c in input]

    IOPort.clear_instances()
    name = f'day_17_2'
    io = IOPort.get_instance(name)
    io.inputs = input
    run_program(name, int_sequence)
    return io.get_output()


make_grid()
print(run_1())
print(run_2())
