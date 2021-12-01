from copy import copy
from typing import List, Tuple

INPUT = open("./input_files/input_21", "r").read().strip("\n")


INSTRUCTION_POINTER = int(INPUT.splitlines()[0].split(" ")[1])


def get_instructions() -> List[Tuple[str, int, int, int]]:
    instructions = list()
    for i in INPUT.splitlines()[1:]:
        instruction, input_a, input_b, output_c = i.split(" ")
        instructions.append((instruction, int(input_a), int(input_b), int(output_c)))
    return instructions


INSTRUCTIONS = get_instructions()

A = 1
B = 2
C = 3


def addr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] + register[instructions[B]]
    return register


def addi(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] + instructions[B]
    return register


def mulr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] * register[instructions[B]]
    return register


def muli(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] * instructions[B]
    return register


def banr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] & register[instructions[B]]
    return register


def bani(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] & instructions[B]
    return register


def borr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] | register[instructions[B]]
    return register


def bori(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]] | instructions[B]
    return register


def setr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = register[instructions[A]]
    return register


def seti(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = instructions[A]
    return register


def gtir(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if instructions[A] > register[instructions[B]] else 0
    return register


def gtri(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if register[instructions[A]] > instructions[B] else 0
    return register


def gtrr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if register[instructions[A]] > register[instructions[B]] else 0
    return register


def eqir(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if instructions[A] == register[instructions[B]] else 0
    return register


def eqri(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if register[instructions[A]] == instructions[B] else 0
    return register


def eqrr(register: List[int], instructions: List[int]):
    register = copy(register)
    register[instructions[C]] = 1 if register[instructions[A]] == register[instructions[B]] else 0
    return register


INSTRUCTION_MAP = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


def run_1():
    registers = [0 for _ in range(6)]
    while registers[INSTRUCTION_POINTER] < len(INSTRUCTIONS):
        instruction = INSTRUCTIONS[registers[INSTRUCTION_POINTER]]
        registers = INSTRUCTION_MAP[instruction[0]](registers, instruction)
        registers[INSTRUCTION_POINTER] += 1
        if registers[INSTRUCTION_POINTER] == 30:
            break
    return registers[4]


def run_2():
    # Stolen from: https://www.reddit.com/r/adventofcode/comments/a86jgt/2018_day_21_solutions/
    d = 0
    s = set()
    part1 = False
    while True:
        e = d | 65536
        d = 2024736
        while True:
            c = e & 255
            d += c
            d &= 16777215
            d *= 65899
            d &= 16777215
            if (256 > e):
                if part1:
                    print(d)
                    exit(0)
                else:
                    if d not in s:
                        print(d)
                    s.add(d)
                    break
            # the following code was the optimised part
            e = e // 256


print(run_1())
print(run_2())
