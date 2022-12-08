INPUT = open("./input_files/input_04", "r").read().strip("\n")

GROUPS = [tuple(tuple(int(z) for z in y.split('-')) for y in x.split(',')) for x in INPUT.split('\n')]


def run_1():
    return sum((x[0] >= y[0] and x[1] <= y[1]) or (y[0] >= x[0] and y[1] <= x[1]) for x, y in GROUPS)


def run_2():
    return sum((x[0] <= y[1] and x[1] >= y[0]) for x, y in GROUPS)


print(run_1())
print(run_2())
