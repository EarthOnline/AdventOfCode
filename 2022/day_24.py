from itertools import product, chain
from time import time

start = time()
INPUT = open("./input_files/input_24", "r").read().strip("\n")


# INPUT = """#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#"""


class Valley:
    MOVES = {
        '>': lambda x, y: (x + 1, y),
        'v': lambda x, y: (x, y + 1),
        '<': lambda x, y: (x - 1, y),
        '^': lambda x, y: (x, y - 1),
        '.': lambda x, y: (x, y)
    }

    def __init__(self):
        self.wall = set()

        rows = INPUT.split('\n')
        self.start = (rows[0].index('.'), 0)
        self.end = (rows[-1].index('.'), len(rows) - 1)
        self.field = {self.start, self.end}
        self.blizzards = {
            '>': set(),
            'v': set(),
            '<': set(),
            '^': set()}

        for y, row in enumerate(rows):
            for x, tile in enumerate(row):
                if tile == '#' or y == 0 or y == len(rows) - 1:
                    self.wall.add((x, y))
                    continue

                self.field.add((x, y))
                if tile != '.':
                    self.blizzards[tile].add((x, y))

    def wrap_around(self, current_x, current_y, d):
        current_x, current_y = self.MOVES[d](current_x, current_y)
        if (current_x, current_y) not in self.wall:
            return current_x, current_y

        if d == '>':
            return min(x for x, y in self.wall if y == current_y) + 1, current_y
        if d == 'v':
            return current_x, min(y for x, y in self.wall if x == current_x) + 1
        if d == '<':
            return max(x for x, y in self.wall if y == current_y) - 1, current_y
        if d == '^':
            return current_x, max(y for x, y in self.wall if x == current_x) - 1

    def move_blizzards(self):
        for key, values in self.blizzards.items():
            self.blizzards[key] = set(self.wrap_around(*v, key) for v in values)

    def solve(self, reversed=False):
        current = {self.end, } if reversed else {self.start, }
        goal = self.start if reversed else self.end

        rounds = 0
        while goal not in current:
            rounds += 1
            self.move_blizzards()
            danger = set(chain.from_iterable(self.blizzards.values()))
            current = set(m(*p) for m, p in product(self.MOVES.values(), current))
            current = set(l for l in current if l not in danger and l in self.field)

        return rounds


def run_1():
    return Valley().solve()


def run_2():
    valley = Valley()
    return sum([valley.solve(), valley.solve(reversed=True), valley.solve()])


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
