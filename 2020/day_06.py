from string import ascii_lowercase

INPUT = open("./input_files/input_06", "r").read().strip("\n")
GROUPS = INPUT.split('\n\n')


def run_1():
    return sum(len(set(g.replace('\n', ''))) for g in GROUPS)


def run_2():
    return sum(len([c for c in ascii_lowercase if g.count(c) == g.count('\n') + 1]) for g in GROUPS)


print(run_1())
print(run_2())
