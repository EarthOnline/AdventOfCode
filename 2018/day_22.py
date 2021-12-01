from typing import Dict, Tuple, List

INPUT = open("./input_files/input_22", "r").read().strip("\n")


DEPTH = int(INPUT.splitlines()[0].split(" ")[1])
TARGET = tuple([int(v) for v in INPUT.splitlines()[1].split(" ")[1].split(",")])

# DEPTH = 510
# TARGET = (10, 10)

X = 0
Y = 1

ROCKY = "."
WET = "="
NARROW = "|"


RISK_LEVEL = {
    ROCKY: 0,
    WET: 1,
    NARROW: 2
}


REGION_TYPE = [ROCKY, WET, NARROW]


def geologic_index(x: int, y: int, area_gi: List[List[int]]) -> int:
    if x == 0 and y == 0:
        return 0
    if x == TARGET[X] and y == TARGET[Y]:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_level(x - 1, y, area_gi) * erosion_level(x, y - 1, area_gi)


def erosion_level(x: int, y: int, area_gi: List[List[int]]) -> int:
    return (area_gi[y][x] + DEPTH) % 20183


def region_type(x: int, y: int, area_gi: List[List[int]]) -> str:
    return REGION_TYPE[erosion_level(x, y, area_gi) % 3]


def get_area() -> Dict[Tuple[int, int], str]:
    area = dict()
    area_gi = list()
    for y in range(TARGET[Y] + 1):
        area_gi.append(list())
        for x in range(TARGET[X] + 1):
            area_gi[y].append(geologic_index(x, y, area_gi))
            area[(x, y)] = region_type(x, y, area_gi)
    return area


AREA = get_area()


def run_1():
    return sum([RISK_LEVEL[t] for t in AREA.values()])


TORCH = 'T'
GEAR = 'G'
NEITHER = 'N'

ALLOWED = {ROCKY: [GEAR, TORCH],
           WET: [GEAR, NEITHER],
           NARROW: [TORCH, NEITHER]}


def get_extended_area() -> Dict[Tuple[int, int], str]:
    area = dict()
    area_gi = list()
    for y in range(TARGET[Y] * 10 + 1):
        area_gi.append(list())
        for x in range(TARGET[X] * 10 + 1):
            area_gi[y].append(geologic_index(x, y, area_gi))
            area[(x, y)] = region_type(x, y, area_gi)
    return area


AREA2 = get_extended_area()


def up(x, y):
    return x, y - 1


def down(x, y):
    return x, y + 1


def right(x, y):
    return x + 1, y


def left(x, y):
    return x - 1, y


def moves(x, y):
    result = [up(x, y), right(x, y), down(x, y), left(x, y)]
    return [(x, y) for (x, y) in result if 0 <= x <= 50 and 0 <= y <= 1000]


def run_2():
    minutes = 0
    visited_tool = {TORCH: [(0, 0)],
                    GEAR: [],
                    NEITHER: []}

    current = [((0, 0), TORCH, 0)]
    while TARGET not in visited_tool[TORCH]:
        print(minutes, current)
        step = []
        for (location, tool, timeout) in current:

            if timeout != 0:
                # we have to wait
                if location not in visited_tool[tool]:
                    step.append((location, tool, timeout - 1))
                    if timeout == 1:
                        visited_tool[tool].append(location)
                continue

            # we can go up, down, left, right or switch
            for move in moves(*location):
                # moving
                if move not in visited_tool[tool] and tool in ALLOWED[AREA2[move]]:
                    step.append((move, tool, 0))
                    visited_tool[tool].append(move)

            # switching
            new_tool = [t for t in ALLOWED[AREA2[location]] if t != tool][0]
            if location not in visited_tool[new_tool]:
                step.append((location, new_tool, 6))

        current = step
        minutes += 1
    return minutes


print(run_1())
print(run_2())
