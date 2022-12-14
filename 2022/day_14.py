from itertools import product, chain

INPUT = open("./input_files/input_14", "r").read().strip("\n")


def rock_area(construct):
    start = construct[0]
    for end in construct[1:]:
        x = sorted([start[0], end[0]])
        y = sorted([start[1], end[1]])
        for coord in product(range(x[0], x[1] + 1), range(y[0], y[1] + 1)):
            yield coord
        start = end


ROCKS = [set(rock_area([tuple(int(x) for x in y.split(',')) for y in x.split(' -> ')])) for x in INPUT.split('\n')]


class Cave:
    actions = [
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y + 1),
        lambda x, y: (x + 1, y + 1)
    ]

    def __init__(self, with_floor=False):
        self.blocked = set(chain.from_iterable(r for r in ROCKS))
        self.rock_bottom = max(y for x, y in self.blocked)
        self.with_floor = with_floor
        if with_floor:
            self.rock_bottom += 2

        self.source = (500, 0)
        self.rocks = len(self.blocked)

    def allowed(self, x, y):
        if self.with_floor and y == self.rock_bottom:
            return False
        return (x, y) not in self.blocked

    def one_grain(self):
        start = self.source
        while start[1] < self.rock_bottom:
            for test in [a(*start) for a in self.actions]:
                if self.allowed(*test):
                    start = test
                    break
            else:
                break
        return start

    def hour_glass(self):
        while self.source not in self.blocked:
            grain = self.one_grain()
            if grain[1] >= self.rock_bottom:
                break
            self.blocked.add(grain)
        return len(self.blocked) - self.rocks


def run_1():
    return Cave().hour_glass()


def run_2():
    return Cave(with_floor=True).hour_glass()


print(run_1())
print(run_2())
