from copy import copy
from typing import Tuple, List

INPUT = open("./input_files/input_16", "r").read().strip("\n")


REGISTER_SAMPLE, DEMO_PROGRAM = INPUT.split("\n\n\n\n")

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


OPCODES = [addr, addi,
           mulr, muli,
           banr, bani,
           borr, bori,
           setr, seti,
           gtir, gtri, gtrr,
           eqir, eqri, eqrr]


def get_sample(sample: str) -> Tuple[List[int], List[int], List[int]]:
    before, instruction, after = sample.splitlines()
    return eval(before[8:]), [int(x) for x in instruction.split(' ')], eval(after[8:])


def run_1():
    count = 0
    for sample in REGISTER_SAMPLE.split("\n\n"):
        before, instruction, after = get_sample(sample)
        afters = [x(before, instruction) for x in OPCODES]
        count += 1 if sum([a == after for a in afters]) >= 3 else 0
    return count


def run_2():
    opcodes = copy(OPCODES)
    mapped_opcodes = dict()

    for sample in REGISTER_SAMPLE.split("\n\n"):
        before, instruction, after = get_sample(sample)
        if instruction[0] in mapped_opcodes.keys():
            continue
        afters = [x(before, instruction) for x in opcodes]
        matches = [opcodes[i] for i, a in enumerate(afters) if a == after]
        if len(matches) == 1:
            match = matches[0]
            mapped_opcodes[instruction[0]] = match
            opcodes.remove(match)

    register = [0, 0, 0, 0]
    for instruction in DEMO_PROGRAM.splitlines():
        instruction = [int(i) for i in instruction.split(" ")]
        register = mapped_opcodes[instruction[0]](register, instruction)
    return register[0]


print(run_1())
print(run_2())
