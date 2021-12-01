from copy import copy

INPUT = open("./input_files/input_02", "r").read().strip("\n")

INT_SEQUENCE = [int(x) for x in INPUT.split(",")]

GOAL = 19690720


def add(int_sequence, input1: int, input2: int, output: int):
    int_sequence[output] = int_sequence[input1] + int_sequence[input2]


def multiply(int_sequence, input1: int, input2: int, output: int):
    int_sequence[output] = int_sequence[input1] * int_sequence[input2]


def run_program(int_sequence):
    pointer = 0

    while True:
        opcode = int_sequence[pointer]
        if opcode == 1:
            add(int_sequence, int_sequence[pointer + 1], int_sequence[pointer + 2], int_sequence[pointer + 3])

        if opcode == 2:
            multiply(int_sequence, int_sequence[pointer + 1], int_sequence[pointer + 2], int_sequence[pointer + 3])

        if opcode == 99:
            break

        pointer = pointer + 4


def run_1():
    int_sequence = copy(INT_SEQUENCE)
    int_sequence[1] = 12
    int_sequence[2] = 2
    run_program(int_sequence)
    return int_sequence[0]


def run_2():
    for noun in range(100):
        for verb in range(100):
            int_sequence = copy(INT_SEQUENCE)
            int_sequence[1] = noun
            int_sequence[2] = verb
            run_program(int_sequence)
            if int_sequence[0] == 19690720:
                return 100 * noun + verb


print(run_1())
print(run_2())
