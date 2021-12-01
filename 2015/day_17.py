from itertools import combinations
from typing import List

INPUT = open("./input_files/input_17", "r").read().strip("\n")


CONTAINERS = [int(x) for x in INPUT.split("\n")]


def get_combinations(requirement: int) -> List[List[int]]:
    result = list()
    for x in range(1, len(CONTAINERS) + 1):
        for c in combinations(CONTAINERS, x):
            if sum(c) == requirement:
                result.append(list(c))
    return result


def run_1():
    return len(get_combinations(150))


def run_2():
    combinations = get_combinations(150)
    min_count = min([len(x) for x in combinations])
    return len([x for x in combinations if len(x) == min_count])


print(run_1())
print(run_2())
