from typing import Tuple, Set

from day_10 import knot_hash

INPUT = "xlqgujun"


def run_1():
    used = 0
    for index in range(128):
        row_input = f'{INPUT}-{index}'
        row_hash = knot_hash(row_input)
        row = "".join([bin(int(x, 16))[2:].zfill(4) for x in row_hash])
        used += len([x for x in row if x == "1"])
    return used


def build_drive(drive_hash: str) -> Set[Tuple[int, int]]:
    drive = set()
    for index in range(128):
        row_input = f'{drive_hash}-{index}'
        row_hash = knot_hash(row_input)
        row = "".join([bin(int(x, 16))[2:].zfill(4) for x in row_hash])
        for i, sector in enumerate(row):
            if sector == "1":
                drive.add((index, i))
    return drive


def is_adjacent(row: int, column: int) -> Set[Tuple[int, int]]:
    return {(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)}


def clear_neighbours(drive, row: int, column: int):
    for neighbour in is_adjacent(row, column):
        if neighbour not in drive:
            continue
        drive.remove(neighbour)
        clear_neighbours(drive, *neighbour)


def run_2():
    drive = build_drive(INPUT)

    groups = 0
    while len(drive) > 0:
        groups += 1
        clear_neighbours(drive, *drive.pop())

    return groups


print(run_1())
print(run_2())
