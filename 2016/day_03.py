from itertools import chain

INPUT = open("./input_files/input_03", "r").read().strip("\n")

TRIANGLES = [tuple(sorted((int(t[:5].strip()), int(t[5:10].strip()), int(t[10:].strip())))) for t in INPUT.split('\n')]


def restructure_input():
    all_items = list(chain.from_iterable(
        (int(t[:5].strip()), int(t[5:10].strip()), int(t[10:].strip())) for t in INPUT.split('\n')))

    return chain.from_iterable([y for i, y in enumerate(all_items) if i % 3 == x] for x in range(3))


ACTUAL_TRIANGLES = [sorted(x) for x in list(zip(*[iter(restructure_input())] * 3))]


def run_1():
    return sum(t1 + t2 > t3 for t1, t2, t3 in TRIANGLES)


def run_2():
    return sum(t1 + t2 > t3 for t1, t2, t3 in ACTUAL_TRIANGLES)


print(run_1())
print(run_2())
