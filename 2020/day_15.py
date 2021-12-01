from copy import copy

INPUT = [2, 0, 1, 9, 5, 19]


def run_1():
    sequence = copy(INPUT)
    for _ in range(len(sequence), 2020):
        positions = [i for i, v in enumerate(sequence) if v == sequence[-1]]
        sequence.append(0 if len(positions) == 1 else positions[-1] - positions[-2])
    return sequence[-1]


def run_2():
    last_position = {v: i for i, v in enumerate(INPUT)}
    prev_step = 0
    position = len(INPUT)
    while position < 30000000:
        char = prev_step
        prev_step = position - last_position[char] if char in last_position.keys() else 0
        last_position[char] = position
        position += 1
    return char


print(run_1())
print(run_2())
