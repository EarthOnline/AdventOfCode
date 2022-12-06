from functools import reduce
from itertools import combinations

INPUT = open("./input_files/input_24", "r").read().strip("\n")

PACKAGES = tuple(int(x) for x in INPUT.split('\n'))


def min_sized_group_for_target(target):
    groups = []
    for r in range(1, len(PACKAGES)):
        options = [set(x) for x in combinations(PACKAGES, r) if sum(x) == target]
        if len(options) > 0:
            groups = options
            break
    return groups


def run_1():
    target = sum(PACKAGES) // 3
    return min(reduce((lambda x, y: x * y), g) for g in min_sized_group_for_target(target))


def run_2():
    target = sum(PACKAGES) // 4
    return min(reduce((lambda x, y: x * y), g) for g in min_sized_group_for_target(target))


print(run_1())
print(run_2())
