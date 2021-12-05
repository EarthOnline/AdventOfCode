from collections import defaultdict
from itertools import chain
from typing import Dict, List

INPUT = open("./input_files/input_05", "r").read().strip("\n")
# INPUT = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""


HORIZONTAL = 1 
VERTICAL = 2
DIAGONAL = 3

X, Y = 0, 1


class Line:
    def __init__(self, line_input: str):
        start, end = line_input.split(' -> ')
        self.start = tuple(int(x) for x in start.split(','))
        self.end = tuple(int(x) for x in end.split(','))
        
        self.type = self._get_line_type()
        self.direction = self._get_direction()
    
    def _get_line_type(self):
        if self.start[X] == self.end[X]:
            return VERTICAL
        if self.start[Y] == self.end[Y]:
            return HORIZONTAL
        return DIAGONAL
    
    def _get_direction(self):
        direction = [0, 0]
        if self.start[X] < self.end[X]:
            direction[X] = 1
        elif self.start[X] > self.end[X]:
            direction[X] = -1
        if self.start[Y] < self.end[Y]:
            direction[Y] = 1
        elif self.start[Y] > self.end[Y]:
            direction[Y] = -1
        return tuple(direction)

    @property
    def path(self):
        path = [self.start]
        while path[-1] != self.end:
            path.append((path[-1][X] + self.direction[X], path[-1][Y] + self.direction[Y]))

        return path


LINES = [Line(x) for x in INPUT.split('\n')]


def number_of_occurences(points: List):
    counts = defaultdict(int)
    for point in points:
        counts[point] += 1
    return counts


def run_1():
    points = chain.from_iterable([l.path for l in LINES if l.type in [HORIZONTAL, VERTICAL]])
    return sum(c >= 2 for c in number_of_occurences(points).values())


def run_2():
    points = chain.from_iterable([l.path for l in LINES])
    return sum(c >= 2 for c in number_of_occurences(points).values())


print(run_1())
print(run_2())
