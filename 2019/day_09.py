import itertools
from collections import defaultdict
from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_09", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

# INT_SEQUENCE = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


def confert_to_dict(int_sequence):
    result = defaultdict(int)

    for i, v in enumerate(int_sequence):
        result[i] = v
    return result


INT_SEQUENCE = confert_to_dict(INT_SEQUENCE)


def run_1():
    IOPort.clear_instances()
    name = f'day_09_1'
    io = IOPort.get_instance(name)
    io.set_input(1)
    run_program(name, copy(INT_SEQUENCE))
    return io.outputs


def run_2():
    IOPort.clear_instances()
    name = f'day_09_2'
    io = IOPort.get_instance(name)
    io.set_input(2)
    run_program(name, copy(INT_SEQUENCE))
    return io.outputs


print(run_1())
print(run_2())
