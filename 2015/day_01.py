INPUT = open("./input_files/input_01", "r").read().strip("\n")


def run_1():
    up = len([x for x in INPUT if x == '('])
    down = len([x for x in INPUT if x == ')'])
    return up - down


def run_2():
    floor = 0
    for index, x in enumerate(INPUT):
        floor += 1 if x == '(' else -1
        if floor == -1:
            return index + 1
    return


print(run_1())
print(run_2())
