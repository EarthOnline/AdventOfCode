from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_05", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

# INT_SEQUENCE = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#                 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#                 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
#
# INT_SEQUENCE = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]


def run_1():
    name = 'day_05_1'
    io = IOPort.get_instance(name)
    io.set_input(1)
    run_program(name, copy(INT_SEQUENCE))
    return io.get_output()


def run_2():
    name = 'day_05_2'
    io = IOPort.get_instance(name)
    io.set_input(5)
    run_program(name, copy(INT_SEQUENCE))
    return io.get_output()


print(run_1())
print(run_2())
