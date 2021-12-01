from collections import defaultdict
from typing import Tuple, Dict

INPUT = open("./input_files/input_06", "r").read().strip("\n")

ON = 'turn on'
OFF = 'turn off'
TOGGLE = 'toggle'


def run_instructions(grid: Dict[Tuple[int, int], bool], input: str):
    for line in input.split("\n"):
        if ON in line:
            _range = [int(x) for x in line[len(ON) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] = True
        if OFF in line:
            _range = [int(x) for x in line[len(OFF) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] = False
        if TOGGLE in line:
            _range = [int(x) for x in line[len(TOGGLE) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] = not grid[(x, y)]


def run_instructions_again(grid: Dict[Tuple[int, int], int], input: str):
    for line in input.split("\n"):
        if ON in line:
            _range = [int(x) for x in line[len(ON) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] += 1
        if OFF in line:
            _range = [int(x) for x in line[len(OFF) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] -= 1 if grid[(x, y)] > 0 else 0
        if TOGGLE in line:
            _range = [int(x) for x in line[len(TOGGLE) + 1:].replace(' through ', ',').split(",")]
            for y in range(_range[1], _range[3] + 1, 1):
                for x in range(_range[0], _range[2] + 1, 1):
                    grid[(x, y)] += 2


def run_1():
    grid = defaultdict(bool)
    run_instructions(grid, INPUT)
    return len([x for x in grid.values() if x])


def run_2():
    grid = defaultdict(int)
    run_instructions_again(grid, INPUT)
    return sum(grid.values())


print(run_1())
print(run_2())
