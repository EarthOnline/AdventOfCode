from collections import defaultdict
from typing import Dict, Tuple, List

INPUT = open("./input_files/input_18", "r").read().strip("\n")


def read_instruction(instruction: str) -> Tuple[str, List[str]]:
    parts = instruction.split(" ")
    return parts[0], parts[1:]


def get_value(registers: Dict[str, int], param: str) -> int:
    if param.isdigit() or param[0] == "-" and param[1:].isdigit():
        return int(param)
    return registers[param]


def run_1():
    instructions = INPUT.split("\n")
    registers = defaultdict(int)
    pointer = 0
    sound_freq = 0

    while pointer < len(instructions):
        while True:
            command, params = read_instruction(instructions[pointer])
            # print(command, params)
            if command == 'add':
                registers[params[0]] += get_value(registers, params[1])
                pointer += 1
                break
            if command == 'jgz':
                pointer += get_value(registers, params[1]) if get_value(registers, params[0]) > 0 else 1
                break
            if command == 'mod':
                registers[params[0]] %= get_value(registers, params[1])
                pointer += 1
                break
            if command == 'mul':
                registers[params[0]] *= get_value(registers, params[1])
                pointer += 1
                break
            if command == 'rcv':
                if get_value(registers, params[0]) > 0:
                    return sound_freq
                pointer += 1
            if command == 'set':
                registers[params[0]] = get_value(registers, params[1])
                pointer += 1
                break
            if command == 'snd':
                sound_freq = get_value(registers, params[0])
                pointer += 1
                break

            print(command, params)
            pointer += 1
            break
    return


def interpret(registers: Dict[str, int], instructions: List[str], pointer: int, msg_que: List[int]
              ) -> Tuple[int, List[int], bool]:
    command, params = read_instruction(instructions[pointer])
    # print(command, params)
    if command == 'add':
        registers[params[0]] += get_value(registers, params[1])
        return pointer + 1, list(), False
    if command == 'jgz':
        return pointer + get_value(registers, params[1]) if get_value(registers, params[0]) > 0 \
            else pointer + 1, list(), False
    if command == 'mod':
        registers[params[0]] %= get_value(registers, params[1])
        return pointer + 1, list(), False
    if command == 'mul':
        registers[params[0]] *= get_value(registers, params[1])
        return pointer + 1, list(), False
    if command == 'rcv':
        if len(msg_que) == 0:
            return pointer, [], True
        registers[params[0]] = msg_que[0]
        del msg_que[0]
        return pointer + 1, [], False
    if command == 'set':
        registers[params[0]] = get_value(registers, params[1])
        return pointer + 1, [], False
    if command == 'snd':
        return pointer + 1, [get_value(registers, params[0])], False
    return pointer, [], False


def run_2():
    instructions = INPUT.split("\n")

    registers_a = defaultdict(int)
    registers_a['p'] = 0
    pointer_a = 0
    msg_que_a = list()

    registers_b = defaultdict(int)
    registers_b['p'] = 1
    pointer_b = 0
    msg_que_b = list()

    count = 0

    while pointer_a < len(instructions) and pointer_b < len(instructions):
        pointer_a, msg_b, waiting_a = interpret(registers_a, instructions, pointer_a, msg_que_a)
        msg_que_b.extend(msg_b)

        pointer_b, msg_a, waiting_b = interpret(registers_b, instructions, pointer_b, msg_que_b)
        msg_que_a.extend(msg_a)
        count += len(msg_a)

        if waiting_a and waiting_b:
            break
    return count


print(run_1())
print(run_2())
