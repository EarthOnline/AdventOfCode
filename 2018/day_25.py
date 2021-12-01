from copy import copy

INPUT = open("./input_files/input_25", "r").read().strip("\n")
FIXED_POINTS = [list(map(int, fp.split(','))) for fp in INPUT.split('\n')]


def distance(point1, point2) -> int:
    return sum(map(lambda x, y: abs(x - y), point1, point2))


def drop_all_connected(point, points):
    if point in points:
        points.remove(point)

    connected_points = [p for p in points if distance(point, p) <= 3]
    for cp in connected_points:
        drop_all_connected(cp, points)


def run_1():
    unused_points = copy(FIXED_POINTS)
    constelations = 0
    while unused_points:
        constelations += 1
        drop_all_connected(unused_points[0], unused_points)

    return constelations


def run_2():
    return None


print(run_1())
print(run_2())
