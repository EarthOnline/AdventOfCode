from itertools import permutations
from typing import Dict, Tuple

INPUT = open("./input_files/input_13", "r").read().strip("\n")


def calc_happiness() -> Dict[Tuple[str, str], int]:
    return {(p[0], p[10][:-1]): int(p[3]) if p[2] == 'gain' else 0 - int(p[3]) for p in
            [l.split(" ") for l in INPUT.split("\n")]}


HAPPiNESS = calc_happiness()


def get_names():
    names = set()
    for line in INPUT.split("\n"):
        parts = line.split(" ")
        names.add(parts[0])
    return list(names)


def run_1():
    names = get_names()
    all_arangements = [x for x in permutations(names, len(names)) if x[0] == names[0]]
    return max([sum([0 + HAPPiNESS[(a[x - 1], a[x])] +
                     HAPPiNESS[(a[x], a[x - 1])] for x in range(len(a))]) for a in all_arangements])


def run_2():
    names = get_names()
    HAPPiNESS.update({(x, 'Earth'): 0 for x in names})
    HAPPiNESS.update({('Earth', x): 0 for x in names})
    names.append('Earth')
    all_arangements = [x for x in permutations(names, len(names)) if x[0] == names[0]]
    return max([sum([0 + HAPPiNESS[(a[x - 1], a[x])] +
                     HAPPiNESS[(a[x], a[x - 1])] for x in range(len(a))]) for a in all_arangements])


print(run_1())
print(run_2())
