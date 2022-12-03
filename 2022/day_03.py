import string

INPUT = open("./input_files/input_03", "r").read().strip("\n")

RUCKSACKS = [(x[:len(x) // 2], x[len(x) // 2:]) for x in INPUT.split('\n')]
PRIORITIES = string.ascii_lowercase + string.ascii_uppercase

GROUPS = list(zip(*[iter(INPUT.split('\n'))] * 3))


def run_1():
    return sum(PRIORITIES.index([x for x in r[0] if x in r[1]][0]) + 1 for r in RUCKSACKS)


def run_2():
    return sum(PRIORITIES.index([x for x in a if x in b and x in c][0]) + 1 for a, b, c in GROUPS)


print(run_1())
print(run_2())
