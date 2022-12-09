from functools import reduce

INPUT = open("./input_files/input_02", "r").read().strip("\n")

KEYPAD = {(r % 3, r // 3): str(r + 1) for r in range(9)}

OTHER_KEYPAD = {
    (2, 0): "1",
    (1, 1): "2",
    (2, 1): "3",
    (3, 1): "4",
    (0, 2): "5",
    (1, 2): "6",
    (2, 2): "7",
    (3, 2): "8",
    (4, 2): "9",
    (1, 3): "A",
    (2, 3): "B",
    (3, 3): "C",
    (2, 4): "D"}

MOVES = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
}


def make_move(keypad, pointer, move):
    result = MOVES[move](*pointer)
    return result if result in keypad else pointer


def follow_instructions(keypad):
    code = []
    pointer = [k for k, v in keypad.items() if v == "5"][0]

    for sequence in INPUT.split('\n'):
        pointer = reduce(lambda p, m: make_move(keypad, p, m), sequence, pointer)
        code.append(keypad[pointer])
    return ''.join(code)


def run_1():
    return follow_instructions(KEYPAD)


def run_2():
    return follow_instructions(OTHER_KEYPAD)


print(run_1())
print(run_2())
