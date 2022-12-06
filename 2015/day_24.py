from itertools import combinations, chain

INPUT = open("./input_files/input_24", "r").read().strip("\n")

PACKAGES = tuple(int(x) for x in INPUT.split('\n'))


def run_1():
    target = sum(PACKAGES) // 3

    groups = list(chain.from_iterable(
        [x for x in combinations(PACKAGES, r) if sum(x) == target] for r in range(1, len(PACKAGES))))
    options = [(x, y, z) for x, y, z in combinations(groups, 3) if tuple(sorted(x + y + z)) == PACKAGES]

    return options


def run_2():
    return


print(run_1())
print(run_2())
