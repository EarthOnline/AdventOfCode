INPUT = open("./input_files/input_02", "r").read().strip("\n")


def run_1():
    total = 0
    packages = [sorted([int(y) for y in x.split("x")]) for x in INPUT.split("\n")]
    for package in packages:
        total += 3 * package[0] * package[1] + 2 * package[0] * package[2] + 2 * package[1] * package[2]
    return total


def run_2():
    total = 0
    packages = [sorted([int(y) for y in x.split("x")]) for x in INPUT.split("\n")]
    for package in packages:
        total += 2 * package[0] + 2 * package[1] + package[0] * package[1] * package[2]
    return total


print(run_1())
print(run_2())
