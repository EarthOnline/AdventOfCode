from itertools import product

from typing import List, Tuple

INPUT = open("./input_files/input_17", "r").read().strip("\n")
# INPUT = "target area: x=20..30, y=-10..-5"
X, Y = [[int(y) for y in x[2:].split('..')] for x in INPUT[13:].split(', ')]
TARGET_AREA = set(product(range(X[0], X[1] + 1), range(Y[0], Y[1] + 1)))
MAX_X = max(x for x, y in TARGET_AREA)
MIN_Y = min(y for x, y in TARGET_AREA)


def in_target(x: int, y: int) -> bool:
    return (x, y) in TARGET_AREA


def reach_target(route: List[Tuple[int, int]]) -> bool:
    return any(in_target(x, y) for x, y in route)


def new_velosity(x_vel: int, y_vel: int) -> Tuple[int, int]:
    y_vel -= 1
    if x_vel > 0:
        return x_vel - 1, y_vel
    if x_vel < 0:
        return x_vel + 1, y_vel
    return x_vel, y_vel


def prope_trajectory(x_vel: int, y_vel: int) -> List[Tuple[int, int]]:
    x = 0
    y = 0

    while x <= MAX_X and y >= MIN_Y:
        x += x_vel
        y += y_vel
        yield x, y
        x_vel, y_vel = new_velosity(x_vel, y_vel)


def run_1():
    return (MIN_Y + (0 if MIN_Y % 2 else 1)) * (MIN_Y // 2)

    # trials = product(range(MAX_X + 1), range(MIN_Y, abs(MIN_Y) + 1))
    # reached = 0
    # for x_vel, y_vel in trials:
    #     route = list(prope_trajectory(x_vel, y_vel))
    #     if not reach_target(route):
    #         continue
    #
    #     reached = max(reached, max(y for x, y in route))
    # return reached


def run_2():
    trials = product(range(MAX_X + 1), range(MIN_Y, abs(MIN_Y) + 1))
    return sum(reach_target(list(prope_trajectory(x_vel, y_vel))) for x_vel, y_vel in trials)


print(run_1())
print(run_2())
