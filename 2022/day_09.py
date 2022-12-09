from itertools import product

INPUT = open("./input_files/input_09", "r").read().strip("\n")

MOVES = [(y, int(z)) for y, z in [x.split(' ') for x in INPUT.split('\n')]]


class Rope:
    STEPS = {
        'U': lambda x, y: (x, y + 1),
        'D': lambda x, y: (x, y - 1),
        'L': lambda x, y: (x - 1, y),
        'R': lambda x, y: (x + 1, y)
    }

    def __init__(self, size=2):
        self.knots = [(0, 0) for _ in range(size)]
        self.tail_possitions = {self.knots[-1]}

    @staticmethod
    def one_closer(p, _p):
        if _p < p:
            return _p + 1
        if _p > p:
            return _p - 1
        return _p

    def moves(self, direction, times):
        for _ in range(times):
            self.move(direction)

    def move(self, direction):
        x, y = self.knots[0] = self.STEPS[direction](*self.knots[0])

        for _i, node in enumerate(self.knots[1:], start=1):
            x, y = self.knots[_i] = self.move_next(x, y, node)

        self.tail_possitions.add(self.knots[-1])

    def move_next(self, x, y, node):
        if node in product((x - 1, x, x + 1), (y - 1, y, y + 1)):  # acceptable positions
            return node

        _x, _y = node
        return self.one_closer(x, _x), self.one_closer(y, _y)


def run_1():
    rope = Rope()
    for command, times in MOVES:
        rope.moves(command, times)
    return len(rope.tail_possitions)


def run_2():
    rope = Rope(10)
    for command, times in MOVES:
        rope.moves(command, times)
    return len(rope.tail_possitions)


print(run_1())
print(run_2())
