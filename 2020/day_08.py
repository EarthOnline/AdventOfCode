from copy import copy

INPUT = open("./input_files/input_08", "r").read().strip("\n")
INSTRUCTIONS = [(o, int(a)) for o, a in [instruction.replace('+', '').split(' ') for instruction in INPUT.split('\n')]]


PROCESSOR = dict(
    nop=lambda pointer, accumulator, argument: (pointer + 1, accumulator),
    acc=lambda pointer, accumulator, argument: (pointer + 1, accumulator + argument),
    jmp=lambda pointer, accumulator, argument: (pointer + argument, accumulator)
)


def run(instructions) -> int:
    has_seen = set()

    pointer = 0
    accumulator = 0
    while 0 <= pointer < len(instructions):
        if pointer in has_seen:
            raise Exception(f'Loop: {accumulator}')
        has_seen.add(pointer)

        operation, argument = instructions[pointer]
        pointer, accumulator = PROCESSOR.get(operation)(pointer, accumulator, argument)

    return accumulator


def run_1():
    result = 0
    try:
        run(INSTRUCTIONS)
    except Exception as e:
        result = e

    return result


def run_2():
    change_pointer = 0
    accumulator = 0
    while True:
        instructions = copy(INSTRUCTIONS)
        operation, argument = instructions[change_pointer]

        if operation == 'acc':
            change_pointer += 1
            continue
        operation = 'nop' if operation == 'jmp' else 'jmp'
        instructions[change_pointer] = (operation, argument)
        try:
            accumulator = run(instructions)
            break
        except Exception as e:
            change_pointer += 1
            pass
    return accumulator


print(run_1())
print(run_2())
