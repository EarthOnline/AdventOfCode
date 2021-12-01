from typing import Tuple

INPUT = open("./input_files/input_03", "r").read().strip("\n")


def go_north(location: Tuple[int, int]) -> Tuple[int, int]:
    return location[0], location[1] + 1


def go_east(location: Tuple[int, int]) -> Tuple[int, int]:
    return location[0] + 1, location[1]


def go_south(location: Tuple[int, int]) -> Tuple[int, int]:
    return location[0], location[1] - 1


def go_west(location: Tuple[int, int]) -> Tuple[int, int]:
    return location[0] - 1, location[1]


MOVES = {'^': go_north,
         '>': go_east,
         'v': go_south,
         '<': go_west}


def run_1():
    location = (0, 0)
    visited = set()
    visited.add(location)

    for x in INPUT:
        location = MOVES[x](location)
        visited.add(location)
    return len(visited)


def run_2():
    location = [(0, 0), (0, 0)]
    visited = set()
    visited.add(location[0])

    for index, x in enumerate(INPUT):
        deliverer = index % 2
        location[deliverer] = MOVES[x](location[deliverer])
        visited.add(location[deliverer])
    return len(visited)


print(run_1())
print(run_2())
