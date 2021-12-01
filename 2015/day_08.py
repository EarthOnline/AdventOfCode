INPUT = open("./input_files/input_08", "r").read().strip("\n")


def run_1():
    return sum([len(x) for x in INPUT.split("\n")]) - sum([len(eval(x)) for x in INPUT.split("\n")])


def run_2():
    return sum([len(repr(x).replace('"', '\\"')) for x in INPUT.split("\n")]) - sum([len(x) for x in INPUT.split("\n")])


print(run_1())
print(run_2())
