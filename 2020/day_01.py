from functools import reduce
from itertools import combinations

INPUT = open("./input_files/input_01", "r").read().strip("\n")
BALANCE = [int(b) for b in INPUT.split('\n')]


def run_1():
    selected = [x for x in BALANCE if 2020 - x in BALANCE]
    return reduce(lambda x, y: x * y, selected)  # python < 3.8
    # return math.prod(selected)  # python >= 3.8


def run_2():
    selected = [x for x in combinations(BALANCE, 3) if sum(x) == 2020][0]
    return reduce(lambda x, y: x * y, selected)


print(run_1())
print(run_2())
