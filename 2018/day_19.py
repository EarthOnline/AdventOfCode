import math
from copy import copy
from typing import List, Tuple

INPUT = open("./input_files/input_19", "r").read().strip("\n")

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


def get_divisors(number: int) -> List[int]:
    large_divisors = []
    for x in range(1, int(math.sqrt(number) + 1)):
        if number % x == 0:
            yield x
            if x*x != number:
                large_divisors.append(number // x)
    for divisor in reversed(large_divisors):
        yield divisor


def run_1():
    registers = [0 for _ in range(6)]

    while registers[INSTRUCTION_POINTER] < len(INSTRUCTIONS):
        instruction = INSTRUCTIONS[registers[INSTRUCTION_POINTER]]
        registers = INSTRUCTION_MAP[instruction[0]](registers, instruction)
        registers[INSTRUCTION_POINTER] += 1
    return registers[0]


def run_2():
    registers = [0 for _ in range(6)]
    registers[0] = 1
    count = 0
    while registers[INSTRUCTION_POINTER] < len(INSTRUCTIONS):
        instruction = INSTRUCTIONS[registers[INSTRUCTION_POINTER]]
        registers = INSTRUCTION_MAP[instruction[0]](registers, instruction)
        registers[INSTRUCTION_POINTER] += 1
        if registers[0] != 1:
            break
    return sum(get_divisors(registers[2]))


print(run_1())
print(run_2())
