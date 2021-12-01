from collections import defaultdict
from typing import List, Tuple

INPUT = open("./input_files/input_03", "r").read().strip("\n")


def get_claims() -> List[Tuple[int, int, int, int]]:
    claims = list()
    for line in INPUT.split("\n"):
        parts = line.replace(",", " ").replace(": ", " ").replace("x", " ").split(" ")
        claims.append((int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])))
    return claims


CLAIMS = get_claims()


def get_claimed_locations(claim: Tuple[int, int, int, int]) -> List[Tuple[int, int]]:
    locations = list()
    for x in range(claim[0], claim[0] + claim[2]):
        for y in range(claim[1], claim[1] + claim[3]):
            locations.append((x, y))
    return locations


def run_1():
    fabric = defaultdict(int)
    for claim in CLAIMS:
        for location in get_claimed_locations(claim):
            fabric[location] += 1
    return len([x for x in fabric.values() if x > 1])


def run_2():
    fabric = defaultdict(int)
    for claim in CLAIMS:
        for location in get_claimed_locations(claim):
            fabric[location] += 1
    for index, claim in enumerate(CLAIMS):
        overlap = False
        for location in get_claimed_locations(claim):
            overlap |= fabric[location] > 1
        if overlap is False:
            return index + 1
    return


print(run_1())
print(run_2())
