from functools import reduce
from operator import mul
from time import time

start = time()
INPUT = open("./input_files/input_19", "r").read().strip("\n")


class Factory:

    def __init__(self, blueprint):
        _number, _rest = blueprint.split(': ')
        self.number = int(_number.split(' ')[-1])
        self.costs = []
        for _rest in _rest.split('. '):
            _rest = _rest.split(' ')[4:]
            while _rest:
                self.costs.append(int(_rest[0]))
                _rest = _rest[3:]


BLUEPRINTS = [Factory(x) for x in INPUT.split('\n')]


def run(c1, c2, c31, c32, c41, c42, times):
    # (ore_robot, clay_robot, obsidian_robot, geode_robot, ore, clay, obsidian, geode)
    options = [(1, 0, 0, 0, 0, 0, 0, 0)]
    max_geodes = 0
    max_ore = max([c1, c2, c31, c41])

    for t in range(times):
        _options = set(o for o in options if
                       o[7] == max_geodes and o[0] <= max_ore and o[1] <= c32 and o[2] <= c42)
        options = set()
        max_geodes = 0

        for _option in _options:
            r1, r2, r3, r4, o1, o2, o3, o4 = _option
            ore = o1 + r1
            clay = o2 + r2
            obsidian = o3 + r3
            geodes = o4 + r4
            max_geodes = max(max_geodes, geodes)

            options.add((r1, r2, r3, r4, ore, clay, obsidian, geodes))
            if o1 >= c1:
                options.add((r1 + 1, r2, r3, r4, ore - c1, clay, obsidian, geodes))
            if o1 >= c2:
                options.add((r1, r2 + 1, r3, r4, ore - c2, clay, obsidian, geodes))
            if o1 >= c31 and o2 >= c32:
                options.add((r1, r2, r3 + 1, r4, ore - c31, clay - c32, obsidian, geodes))
            if o1 >= c41 and o3 >= c42:
                options.add((r1, r2, r3, r4 + 1, ore - c41, clay, obsidian - c42, geodes))
    return max_geodes


def run_1():
    return sum(b.number * run(*b.costs, 24) for b in BLUEPRINTS)


def run_2():
    return reduce(mul, [run(*b.costs, 32) for b in BLUEPRINTS[:3]])


print(run_1())
print('==> ', (time() - start) * 1000)
print(run_2())
print('==> ', (time() - start) * 1000)
