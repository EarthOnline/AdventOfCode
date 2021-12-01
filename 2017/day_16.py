from copy import copy
from typing import List

INPUT = open("./input_files/input_16", "r").read().strip("\n")


def dance(line: List[str], step: str) -> List[str]:
    if step[0] == 'x':
        position1, position2 = [int(x) for x in step[1:].split("/")]
        x = line[position1]
        line[position1] = line[position2]
        line[position2] = x
    elif step[0] == 'p':
        position1, position2 = [line.index(x) for x in step[1:].split("/")]
        x = line[position1]
        line[position1] = line[position2]
        line[position2] = x
    elif step[0] == 's':
        size = int(step[1:])
        x = line[0 - size:]
        x.extend(line[:len(line) - size])
        line = x
    else:
        print(step)
    return line


def run_1():
    line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    steps = INPUT.split(",")
    for step in steps:
        line = dance(line, step)
    return "".join(line)


def run_2():
    line = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    org_line = copy(line)

    repeat = None
    length = 1000000000

    steps = INPUT.split(",")
    for _x in range(length):
        if _x > 0 and line == org_line:
            repeat = _x
            break

        for step in steps:
            # if repeat is None or
            line = dance(line, step)

    for _x in range(length % repeat):
        for step in steps:
            line = dance(line, step)
    return "".join(line)


print(run_1())
print(run_2())
