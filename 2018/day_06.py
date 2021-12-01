from collections import defaultdict
from typing import Tuple, List, Dict

INPUT = open("./input_files/input_06", "r").read().strip("\n")


LOCATIONS: Dict[int, Tuple[int, int]] = \
    {i: tuple([int(p) for p in l.split(", ")]) for i, l in enumerate(INPUT.split("\n"), start=1)}


def get_distance(location_1: Tuple[int, int], location_2: Tuple[int, int]) -> int:
    x = abs(location_1[0] - location_2[0])
    y = abs(location_1[1] - location_2[1])
    return x + y


def get_grid_size(locations: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    min_x = min([l[0] for l in locations])
    max_x = max([l[0] for l in locations])
    min_y = min([l[1] for l in locations])
    max_y = max([l[1] for l in locations])
    return min_x, min_y, max_x, max_y


def run_1():
    min_x, min_y, max_x, max_y = get_grid_size(list(LOCATIONS.values()))

    region_sizes = defaultdict(int)
    infinite_ids = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = [(get_distance(l, (x, y)), coord_id) for coord_id, l in LOCATIONS.items()]
            min_distance = min([d[0] for d in distances])
            if len([d for d in distances if d[0] == min_distance]) > 1:
                continue

            coord_id = [d[1] for d in distances if d[0] == min_distance][0]
            region_sizes[coord_id] += 1

            if x == min_x or x == max_x or y == min_y or y == max_y:
                infinite_ids.add(coord_id)

    return max(size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids)


def run_2():
    in_range = 0
    min_x, min_y, max_x, max_y = get_grid_size(list(LOCATIONS.values()))
    for x in range(min_x - 100, max_x + 100):
        for y in range(min_y - 100, max_y + 100):
            distance = sum([get_distance(l, (x, y)) for l in LOCATIONS.values()])
            if distance < 10000:
                in_range += 1
    return in_range


print(run_1())
print(run_2())
