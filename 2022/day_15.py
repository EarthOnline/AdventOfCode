import string
from functools import reduce
from time import time

start = time()

INPUT = open("./input_files/input_15", "r").read().strip("\n")


class Pair:
    DIGITS = string.digits + '-'

    def __init__(self, contruct):
        _s, _b = contruct.split(': ')
        self.sensor = tuple(int(''.join(y for y in x if y in self.DIGITS)) for x in _s.split(', '))
        self.beacon = tuple(int(''.join(y for y in x if y in self.DIGITS)) for x in _b.split(', '))
        self.distance = self.get_distance(self.sensor, self.beacon)

    def blocked_at_y(self, y):
        range_distance = self.distance - abs(self.sensor[1] - y)
        if range_distance < 0:
            return None
        return self.sensor[0] - range_distance, self.sensor[0] + range_distance

    @staticmethod
    def get_distance(sensor, beacon):
        s_x, s_y = sensor
        b_x, b_y = beacon
        return abs(s_x - b_x) + abs(s_y - b_y)


PAIRS = [Pair(x) for x in INPUT.split('\n')]


def join(ranges, range_x):
    if range_x is None:
        return ranges

    untouched = set(r for r in ranges if r[0] > range_x[1] or r[1] < range_x[0])

    if len(untouched) == len(ranges):
        untouched.add(range_x)
        return untouched

    touched = set(r for r in ranges if r not in untouched)
    touched.add(range_x)
    untouched.add((min(s for s, e in touched), max(e for s, e in touched)))
    return untouched


def run_1():
    y = 2000000
    blocked_space = sum(e - s + 1 for s, e in reduce(join, map(lambda p: p.blocked_at_y(y), PAIRS), set()))
    beacon_space = len(set(p.beacon[0] for p in PAIRS if p.beacon[1] == y))
    return blocked_space - beacon_space


def run_2():
    for y in range(0, 4000001):
        blocked = reduce(join, map(lambda p: p.blocked_at_y(y), PAIRS), set())
        if len(blocked) > 1:
            return (sorted(blocked, key=lambda i: i[0])[0][1] + 1) * 4000000 + y


print(run_1())
print((time() - start) * 10 ** 3)
print(run_2())
print((time() - start) * 10 ** 3)
