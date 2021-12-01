from collections import defaultdict
from typing import Dict, Tuple, List

INPUT = open("./input_files/input_23", "r").read().strip("\n")


def read_instruction(instruction: str) -> Tuple[str, List[str]]:
    parts = instruction.split(" ")
    return parts[0], parts[1:]


def get_value(registers: Dict[str, int], param: str) -> int:
    if param.isdigit() or param[0] == "-" and param[1:].isdigit():
        return int(param)
    return registers[param]


def interpret(registers: Dict[str, int], instruction: Tuple[str, List[str]], pointer: int) -> Tuple[int, bool]:
    command, params = instruction
    if command == 'jnz':
        param_0 = get_value(registers, params[0])
        param_1 = get_value(registers, params[1])
        return pointer + 1 if param_0 == 0 \
            else pointer + param_1, False
    if command == 'mul':
        registers[params[0]] *= get_value(registers, params[1])
        return pointer + 1, True
    if command == 'set':
        registers[params[0]] = get_value(registers, params[1])
        return pointer + 1, False
    if command == 'sub':
        registers[params[0]] -= get_value(registers, params[1])
        return pointer + 1, False
    return pointer, False


def run_1():
    instructions = [read_instruction(x) for x in INPUT.split("\n")]
    registers = defaultdict(int)
    pointer = 0
    muls = 0

    while pointer < len(instructions):
        pointer, mul = interpret(registers, instructions[pointer], pointer)
        muls += 1 if mul else 0
    return muls


def run_2():
    instructions = [read_instruction(x) for x in INPUT.split("\n")]
    h = 0
    for x in range(int(instructions[0][1][1]) * int(instructions[4][1][1]) - int(instructions[5][1][1]),
                   int(instructions[0][1][1]) * int(instructions[4][1][1]) - int(instructions[5][1][1])
                   - int(instructions[7][1][1]) + 1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h


print(run_1())
print(run_2())
