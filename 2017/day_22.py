from collections import defaultdict
from typing import Dict, Tuple

INPUT = open("./input_files/input_22", "r").read().strip("\n")

CLEAN = '.'
INFECTED = "#"

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def load_grid(grid_input: str) -> Tuple[Dict[Tuple[int, int], int], Tuple[int, int]]:
    result = defaultdict(int)
    for row_index, row in enumerate(grid_input.split("\n")):
        for column_index, cell in enumerate(row):
            result[(row_index, column_index)] = 2 if cell == INFECTED else 0
    return result, (row_index // 2, column_index // 2)


def move(direction: int, position: Tuple[int, int]) -> Tuple[int, int]:
    if direction == NORTH:
        return position[0] - 1, position[1]
    if direction == EAST:
        return position[0], position[1] + 1
    if direction == SOUTH:
        return position[0] + 1, position[1]
    if direction == WEST:
        return position[0], position[1] - 1


def run_1():
    grid, position = load_grid(INPUT)
    direction = NORTH
    infections = 0

    for burst in range(10000):
        selected_state = grid[position]
        infections += 0 if selected_state else 1
        direction = (direction + 1 if selected_state else direction - 1) % 4
        grid[position] = not selected_state
        position = move(direction, position)
    return infections


def run_2():
    grid, position = load_grid(INPUT)
    direction = NORTH
    infections = 0

    for burst in range(10000000):
        selected_state = grid[position]
        infections += 1 if selected_state == 1 else 0
        if selected_state == 0:
            direction = (direction - 1) % 4
        if selected_state == 2:
            direction = (direction + 1) % 4
        if selected_state == 3:
            direction = (direction + 2) % 4
        grid[position] = (selected_state + 1) % 4
        position = move(direction, position)
    return infections


print(run_1())
print(run_2())
