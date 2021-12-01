from typing import Dict

INPUT = open("./input_files/input_07", "r").read().strip("\n")


def build_instructions(input: str) -> Dict[str, str]:
    result = dict()
    for instruction in [x.split(" -> ") for x in input.split("\n")]:
        result[instruction[1]] = instruction[0]
    return result


def get_value(instructions: Dict[str, str], value: str, cache: Dict[str, int]) -> int:
    if value.isdigit():
        return int(value)
    if value not in cache:
        cache[value] = calc_wire(instructions, value, cache)
    return cache[value]


def calc_wire(instructions: Dict[str, str], wire: str, cache: Dict[str, int]) -> int:
    instruction = instructions[wire]
    if 'AND' in instruction:
        inst = instruction.split(' AND ')
        return get_value(instructions, inst[0], cache) & get_value(instructions, inst[1], cache)
    if 'NOT' in instruction:
        return (~ get_value(instructions, instruction[4:], cache)) % 65536
    if 'OR' in instruction:
        inst = instruction.split(' OR ')
        return get_value(instructions, inst[0], cache) | get_value(instructions, inst[1], cache)
    if 'LSHIFT' in instruction:
        inst = instruction.split(' LSHIFT ')
        return get_value(instructions, inst[0], cache) << int(inst[1])
    if 'RSHIFT' in instruction:
        inst = instruction.split(' RSHIFT ')
        return get_value(instructions, inst[0], cache) >> int(inst[1])
    return get_value(instructions, instruction, cache)


def run_1():
    cache: Dict[str, int] = dict()
    instructions = build_instructions(INPUT)
    return calc_wire(instructions, 'a', cache)


def run_2():
    cache: Dict[str, int] = dict()
    cache['b'] = 16076
    instructions = build_instructions(INPUT)
    return calc_wire(instructions, 'a', cache)


print(run_1())
print(run_2())
