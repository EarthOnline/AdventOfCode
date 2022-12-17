from collections import deque
from time import time

start = time()

INPUT = open("./input_files/input_17", "r").read().strip("\n")
# INPUT = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

ROCKS = [
    {(2, 0), (3, 0), (4, 0), (5, 0)},
    {(3, 2), (2, 1), (3, 1), (4, 1), (3, 0)},
    {(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)},
    {(2, 0), (2, 1), (2, 2), (2, 3)},
    {(2, 0), (3, 0), (2, 1), (3, 1)},
]


class Wind:
    def __init__(self):
        self.directions = deque(INPUT)
        self.index = 0

    @property
    def direction(self):
        direction = self.directions.popleft()
        self.directions.append(direction)
        self.index = (self.index + 1) % len(self.directions)
        return direction


class Chamber:
    MOVES = {
        '>': lambda x, y: (x + 1, y),
        '<': lambda x, y: (x - 1, y),
        'v': lambda x, y: (x, y - 1),
    }

    def __init__(self):
        self.wind = Wind()
        self.blocked = set()
        self.max_y = 0
        self.removed = 0

    @property
    def starting_point(self):
        return self.max_y + 4

    def crash_rock(self, rock):
        moved_x, moved_y = 0, 0
        while True:
            direction = self.wind.direction
            change = self.MOVES[direction]
            _rock = set(change(*r) for r in rock)
            if all(0 <= x < 7 and (x, y) not in self.blocked for x, y in _rock):
                moved_x += 1 if direction == '>' else -1
                rock = _rock

            change = self.MOVES['v']
            _rock = set(change(*r) for r in rock)
            if all(0 < y and (x, y) not in self.blocked for x, y in _rock):
                moved_y += 1
                rock = _rock
            else:
                self.blocked.update(rock)
                self.max_y = max(self.max_y, max(y for x, y in rock))
                break
        return moved_x, moved_y


def generate_rock(number, start):
    rock = ROCKS[number % 5]
    return set((x, y + start) for x, y in rock)


def run_1():
    chamber = Chamber()

    for number in range(2022):
        rock = generate_rock(number, chamber.starting_point)
        chamber.crash_rock(rock)

    return chamber.max_y


def run_2():
    chamber = Chamber()
    old_moves_dict = {}
    rocks = 1000000000000
    extra_height = 0

    pointer = 0
    while pointer < rocks:
        number = pointer
        pointer += 1
        wind_index = chamber.wind.index
        rock = generate_rock(number, chamber.starting_point)
        moved = chamber.crash_rock(rock)

        key = (wind_index, number % len(ROCKS), moved)
        if key not in old_moves_dict:
            old_moves_dict[key] = []
        old_moves = old_moves_dict[key]
        old_moves.append((chamber.max_y, number))

        if len(old_moves) <= 2:
            continue

        last_height, last_number = old_moves[-2]
        next_last_height, next_last_number = old_moves[-3]

        if chamber.max_y - last_height != last_height - next_last_height:
            continue

        if number - last_number != last_number - next_last_number:
            continue

        skip_size = number - last_number
        skips = (rocks - number - 1) // skip_size
        pointer += skips * skip_size
        extra_height = (chamber.max_y - last_height) * skips

    return chamber.max_y + extra_height


print(run_1())
print('==> ', (time() - start) * 1000)
print(run_2())
print('==> ', (time() - start) * 1000)
