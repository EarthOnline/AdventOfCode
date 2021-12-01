import itertools
import math
from collections import defaultdict
from copy import deepcopy
from functools import reduce

INPUT = open("./input_files/input_12", "r").read().strip("\n")


# INPUT = """<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>"""


MOONS = [tuple([int(c[2:]) for c in m[1:-1].split(', ')]) for m in INPUT.split('\n')]


def move(moons):
    combinations = itertools.combinations(moons, 2)
    for moon1, moon2 in combinations:
        x1, y1, z1 = moon1['pos']
        x2, y2, z2 = moon2['pos']
        x_change = 1 if x1 < x2 else -1 if x1 > x2 else 0
        y_change = 1 if y1 < y2 else -1 if y1 > y2 else 0
        z_change = 1 if z1 < z2 else -1 if z1 > z2 else 0

        x, y, z = moon1['vel']
        moon1['vel'] = (x + x_change, y + y_change, z + z_change)
        x, y, z = moon2['vel']
        moon2['vel'] = (x - x_change, y - y_change, z - z_change)
    for moon in moons:
        pos_x, pos_y, pos_z = moon['pos']
        vel_x, vel_y, vel_z = moon['vel']
        moon['pos'] = (pos_x + vel_x, pos_y + vel_y, pos_z + vel_z)


def run_1():
    moons = [dict(pos=m, vel=(0, 0, 0)) for m in MOONS]

    for _ in range(1000):
        move(moons)
        # print(moons)
    energy = [(abs(m['pos'][0]) + abs(m['pos'][1]) + abs(m['pos'][2]))
              * (abs(m['vel'][0]) + abs(m['vel'][1]) + abs(m['vel'][2])) for m in moons]
    return sum(energy)


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def run_2():
    moons = [dict(pos=m, vel=(0, 0, 0)) for m in MOONS]
    moves = 0
    period = dict()
    start = [[(m['pos'][axis], m['vel'][axis]) for m in moons] for axis in range(3)]

    while len(period) < 3:
        moves += 1
        move(moons)
        for axis in range(3):
            if axis not in period and start[axis] == [(m['pos'][axis], m['vel'][axis]) for m in moons]:
                period[axis] = moves

    return reduce(lcm, period.values())


print(run_1())
print(run_2())
