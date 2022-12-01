INPUT = open("./input_files/input_01", "r").read().strip("\n")

ELFS = [sum(int(x) for x in y.split("\n")) for y in INPUT.split("\n\n")]


def run_1():
    return max(ELFS)


def run_2():
    return sum(sorted(ELFS, reverse=True)[:3])


print(run_1())
print(run_2())
