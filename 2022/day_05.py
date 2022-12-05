from copy import deepcopy
from itertools import zip_longest

INPUT = open("./input_files/input_05", "r").read().strip("\n")

MOVES = [tuple(int(y) for i, y in enumerate(x.split(' ')) if i % 2 == 1) for x in INPUT.split('\n\n')[1].split('\n')]


def read_crates(input_string):
    stacks = {}
    lines = [list(zip_longest(*[iter(x)] * 4)) for x in reversed(input_string.split('\n'))]

    for _, stack, _, _ in lines[0]:
        stacks[int(stack)] = []

    for line in lines[1:]:
        for i, (_, crate, _, _) in enumerate(line, start=1):
            if crate != ' ':
                stacks[i].append(crate)
    return stacks


CRATES = read_crates(INPUT.split('\n\n')[0])


def move_crates_9000(stacks, move):
    times, p1, p2 = move
    for _ in range(times):
        stacks[p2].append(stacks[p1].pop())
    return stacks


def move_crates_9001(stacks, move):
    times, p1, p2 = move
    stacks[p2].extend(stacks[p1][0 - times:])
    stacks[p1] = stacks[p1][:0 - times]
    return stacks


def run_1():
    stacks = deepcopy(CRATES)
    list(map(lambda x: move_crates_9000(stacks, x), MOVES))
    return ''.join(x[-1] for x in stacks.values())


def run_2():
    stacks = deepcopy(CRATES)
    list(map(lambda x: move_crates_9001(stacks, x), MOVES))
    return ''.join(x[-1] for x in stacks.values())


print(run_1())
print(run_2())
