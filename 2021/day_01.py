INPUT = open("./input_files/input_01", "r").read().strip("\n")
DEPTHS = [int(x) for x in INPUT.split('\n')]


def run_1():
    return sum(x < y for x, y in zip(DEPTHS, DEPTHS[1:]))


def run_2():
    # mesurements = [sum(DEPTHS[x:x+3]) for x in range(len(DEPTHS[:-2]))]
    # return sum(x < y for x, y in zip(mesurements, mesurements[1:]))
    return sum(x < y for x, y in zip(DEPTHS, DEPTHS[3:]))  # Only compare non-overlapping


print(run_1())
print(run_2())
