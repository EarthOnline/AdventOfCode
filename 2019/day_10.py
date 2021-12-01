import math
from collections import defaultdict

INPUT = open("./input_files/input_10", "r").read().strip("\n")


def get_asteroids(map):
    asteriods = set()
    lines = map.split('\n')
    for y, line in enumerate(lines):
        for x, opservation in enumerate(line):
            if opservation == '#':
                asteriods.add((x, y))
    return asteriods


ASTEROIDS = get_asteroids(INPUT)


def distance(location1, location2):
    x1, y1 = location1
    x2, y2 = location2
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return x + y


def angle(location1, location2):
    x1, y1 = location1
    x2, y2 = location2
    x = x2 - x1
    y = y2 - y1

    if y == 0:
        return 90 if x > 0 else 270
    rad = math.atan(x / y)
    deg = math.degrees(rad)
    if y < 0:
        deg = 0 - deg
    if y > 0:
        deg = 180 - deg
    deg = deg % 360
    return deg


def run_1():
    asteroids = list(ASTEROIDS)
    in_sight = dict()
    for asteroid in asteroids:
        others = [a for a in ASTEROIDS if a != asteroid]
        in_sight[asteroid] = len(set([angle(asteroid, o) for o in others]))
    # print([k for k, v in in_sight.items() if v == max(in_sight.values())])
    return max(in_sight.values())


def run_2():
    station = (20, 19)
    others = [a for a in ASTEROIDS if a != station]
    angles = defaultdict(list)
    for other in others:
        angles[angle(station, other)].append(other)
    target_angle = dict()
    for _angle, asteroids in angles.items():
        asteroids.sort(key=lambda x: distance(station, x))
        for i, a in enumerate(asteroids):
            target_angle[a] = i * 360 + _angle
    target_angles = list(target_angle.items())
    target_angles.sort(key=lambda x: x[1])
    targets = [a for a, l in target_angles]
    target_x, target_y = targets[199]
    return target_x * 100 + target_y


print(run_1())
print(run_2())
