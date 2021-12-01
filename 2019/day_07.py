import itertools
from copy import copy

from helpers.intcode_computer import run_program, IOPort

INPUT = open("./input_files/input_07", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

# INT_SEQUENCE = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]


def run_1():
    inputs = [0, 1, 2, 3, 4]

    results = dict()

    for perm in itertools.permutations(inputs, 5):
        IOPort.clear_instances()
        IOPort.get_instance(f'day_07_1_0').set_input(perm[0])
        IOPort.get_instance(f'day_07_1_1').set_input(perm[1])
        IOPort.get_instance(f'day_07_1_2').set_input(perm[2])
        IOPort.get_instance(f'day_07_1_3').set_input(perm[3])
        IOPort.get_instance(f'day_07_1_4').set_input(perm[4])

        output = 0

        for t in range(5):
            name = f'day_07_1_{t}'
            io = IOPort.get_instance(name)
            io.set_input(output)
            run_program(name, copy(INT_SEQUENCE))
            output = io.get_output()
        results[''.join([str(x) for x in perm])] = output

    max_result = max(results.values())
    return max_result


def run_2():
    inputs = [5, 6, 7, 8, 9]

    results = dict()

    for perm in itertools.permutations(inputs, 5):
        seqs = [copy(INT_SEQUENCE) for _ in range(5)]
        IOPort.clear_instances()

        IOPort.get_instance('day_07_2_0').set_input(perm[0])
        IOPort.get_instance('day_07_2_1').set_input(perm[1])
        IOPort.get_instance('day_07_2_2').set_input(perm[2])
        IOPort.get_instance('day_07_2_3').set_input(perm[3])
        IOPort.get_instance('day_07_2_4').set_input(perm[4])

        output = 0

        while not IOPort.get_instance('day_07_2_4').finished:
            for t in range(5):
                name = f'day_07_2_{t}'
                io = IOPort.get_instance(name)
                io.set_input(output)
                run_program(name, seqs[t])
                output = io.get_output()
        results[''.join([str(x) for x in perm])] = output
        # print(perm, output)

    max_result = max(results.values())
    return max_result


print(run_1())
print(run_2())
