from collections import defaultdict
from typing import List, Tuple

INPUT = 7511


def get_fuel_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x + 10
    power_level = (rack_id * y + serial_number) * rack_id
    return power_level // 100 % 10 - 5


def counts_for_3_x_3(x: int, y: int) -> List[Tuple[int, int]]:
    square = [(x, y),   (x-1, y),   (x-2, y),
              (x, y-1), (x-1, y-1), (x-2, y-1),
              (x, y-2), (x-1, y-2), (x-2, y-2)]
    return [(x, y) for x, y in square if 0 < x < 299 and 0 < y < 299]


def counts_for(x: int, y: int) -> List[Tuple[int, int, int]]:
    squares = list()
    for size in range(3, 25):
        for offset_y in range(size):
            for offset_x in range(size):
                squares.append((x-offset_x, y-offset_y, size))
    return [(x, y, s) for x, y, s in squares if 0 < x < 299 and 0 < y < 299]


def run_1():
    fuel_levels = defaultdict(int)
    for x in range(1, 301):
        for y in range(1, 301):
            fuel = get_fuel_level(x, y, INPUT)
            for grid in counts_for_3_x_3(x, y):
                fuel_levels[grid] += fuel
    max_fuel = max(fuel_levels.values())

    return [f"{g[0]},{g[1]}" for g, v in fuel_levels.items() if v == max_fuel][0]


def run_2():
    fuel_levels = defaultdict(int)
    for x in range(1, 301):
        for y in range(1, 301):
            fuel = get_fuel_level(x, y, INPUT)
            for grid in counts_for(x, y):
                fuel_levels[grid] += fuel
    max_fuel = max(fuel_levels.values())

    return [f"{g[0]},{g[1]},{g[2]}" for g, v in fuel_levels.items() if v == max_fuel][0]


print(run_1())
print(run_2())
