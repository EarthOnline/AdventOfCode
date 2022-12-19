from copy import copy
from time import time

start = time()
INPUT = open("./input_files/input_18", "r").read().strip("\n")

DROPLETS = [tuple(int(y) for y in x.split(',')) for x in INPUT.split('\n')]
MIN_X, MAX_X = min(x for x, y, z in DROPLETS) - 1, max(x for x, y, z in DROPLETS) + 1
MIN_Y, MAX_Y = min(y for x, y, z in DROPLETS) - 1, max(y for x, y, z in DROPLETS) + 1
MIN_Z, MAX_Z = min(z for x, y, z in DROPLETS) - 1, max(z for x, y, z in DROPLETS) + 1

ADJACENT = [
    lambda x, y, z: (x - 1, y, z),
    lambda x, y, z: (x + 1, y, z),
    lambda x, y, z: (x, y - 1, z),
    lambda x, y, z: (x, y + 1, z),
    lambda x, y, z: (x, y, z - 1),
    lambda x, y, z: (x, y, z + 1)
]


def adjacent(droplet):
    x, y, z = droplet
    return set(a(x, y, z) for a in ADJACENT)


def run_1():
    return sum(sum(c not in DROPLETS for c in adjacent(d)) for d in DROPLETS)


def run_2():
    steam_area = set()
    current = {(MIN_X, MIN_Y, MIN_Z)}
    steam_area.update(current)
    while current:
        _current = copy(current)
        current = set()
        for x, y, z in _current:
            current.update((x, y, z) for x, y, z in adjacent((x, y, z))
                           if (x, y, z) not in DROPLETS
                           and (x, y, z) not in steam_area
                           and MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y and MIN_Z <= z <= MAX_Z)
        steam_area.update(current)

    return sum(sum(c in steam_area for c in adjacent(d)) for d in DROPLETS)


print(run_1())
print('==> ', (time() - start) * 1000)
print(run_2())
print('==> ', (time() - start) * 1000)
