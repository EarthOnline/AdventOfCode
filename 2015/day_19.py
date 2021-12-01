import string
from collections import defaultdict
from typing import Dict, List, Set

INPUT = open("./input_files/input_19", "r").read().strip("\n")


MOLECULE = INPUT.split("\n")[-1]


def get_replacements() -> Dict[str, List[str]]:
    result = defaultdict(list)
    for line in INPUT.split("\n")[:-2]:
        input, output = line.split(" => ")
        result[input].append(output)
    return dict(result)


REPLACEMENTS = get_replacements()


def run_1():
    results = set()
    for x in range(len(MOLECULE)):
        find = MOLECULE[x]
        if find not in REPLACEMENTS.keys():
            continue
        for hit in REPLACEMENTS[find]:
            results.add(f'{MOLECULE[:x]}{hit}{MOLECULE[x+1:]}')
    for x in range(len(MOLECULE) - 1):
        find = MOLECULE[x:x+2]
        if find not in REPLACEMENTS.keys():
            continue
        for hit in REPLACEMENTS[find]:
            results.add(f'{MOLECULE[:x]}{hit}{MOLECULE[x+2:]}')
    return len(results)


def run_2():
    molecules = len([x for x in MOLECULE if x in string.ascii_uppercase])
    containers = MOLECULE.count('Rn') + MOLECULE.count('Ar')
    seperators = MOLECULE.count('Y') * 2
    return molecules - containers - seperators - 1


print(run_1())
print(run_2())
