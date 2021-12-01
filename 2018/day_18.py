from typing import Dict, Tuple, List

INPUT = open("./input_files/input_18", "r").read().strip("\n")
# INPUT = """.#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|."""

OPEN = '.'
TREE = '|'
YARD = '#'


def get_state() -> List[List[str]]:
    state = list()
    for line in INPUT.splitlines():
        state.append([acre for acre in line])
    return state


INITIAL_STATE = get_state()


def get_new_acre(x: int, y: int, state: List[List[str]]) -> str:
    max_x = len(state[0]) - 1
    max_y = len(state) - 1
    adjecent = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    adjecent = [(x, y) for x, y in adjecent if 0 <= x <= max_x and 0 <= y <= max_y]
    surrounding_area = list(map(lambda l: state[l[1]][l[0]], adjecent))
    area = state[y][x]
    if area == OPEN:
        return TREE if sum([1 for a in surrounding_area if a == TREE]) >= 3 else OPEN
    if area == TREE:
        return YARD if sum([1 for a in surrounding_area if a == YARD]) >= 3 else TREE
    if area == YARD:
        return YARD if YARD in surrounding_area and TREE in surrounding_area else OPEN
    return ''


def run_1():
    state = INITIAL_STATE
    max_x = len(state[0]) - 1
    max_y = len(state) - 1
    for m in range(10):
        new_state = list()
        for y in range(max_y + 1):
            new_state.append([get_new_acre(x, y, state) for x in range(max_x + 1)])

        state = new_state
    return sum([sum([1 for x in y if x == TREE]) for y in state]) * \
        sum([sum([1 for x in y if x == YARD]) for y in state])


def get_state_signature(state: Dict[Tuple[int, int], str]):
    max_x = max([x for x, y in state.keys()])
    max_y = max([y for x, y in state.keys()])

    lines = list()
    for y in range(max_y + 1):
        lines.append("".join([state[(x, y)] for x in range(max_x + 1)]))
    return "".join(lines)


def run_2():
    states = list()
    state = INITIAL_STATE
    states.append(state)
    max_x = len(state[0]) - 1
    max_y = len(state) - 1
    for m in range(1, 1000000001):
        new_state = list()
        for y in range(max_y + 1):
            new_state.append([get_new_acre(x, y, state) for x in range(max_x + 1)])

        state = new_state
        if state in states:
            break
        states.append(state)
    repeat = states.index(state)
    offset = (1000000000 - repeat + 1) % (m - repeat)
    state = states[repeat + offset - 1]

    return sum([sum([1 for x in y if x == TREE]) for y in state]) * \
        sum([sum([1 for x in y if x == YARD]) for y in state])


print(run_1())
print(run_2())
