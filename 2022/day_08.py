INPUT = open("./input_files/input_08", "r").read().strip("\n")


class Forest:
    def __init__(self):
        self.grid = self.create_grid()
        self.max_x = max(x for x, y in self.grid.keys())
        self.max_y = max(y for x, y in self.grid.keys())

    @staticmethod
    def create_grid():
        grid = {}
        for y, row in enumerate(INPUT.split('\n')):
            for x, value in enumerate(row):
                grid[(x, y)] = int(value)
        return grid

    def is_visible(self, x, y):
        size = self.grid[(x, y)]
        others = [
            max(self.grid[(r, y)] for r in range(x)) if x > 0 else -1,
            max(self.grid[(r, y)] for r in range(x + 1, self.max_x + 1)) if x < self.max_x else -1,
            max(self.grid[(x, r)] for r in range(y)) if y > 0 else -1,
            max(self.grid[(x, r)] for r in range(y + 1, self.max_y + 1)) if y < self.max_y else -1]
        return min(others) < size

    def senic_score(self, x, y):
        size = self.grid[(x, y)]
        others = [
            [self.grid[(r, y)] for r in range(x)][::-1],
            [self.grid[(r, y)] for r in range(x + 1, self.max_x + 1)],
            [self.grid[(x, r)] for r in range(y)][::-1],
            [self.grid[(x, r)] for r in range(y + 1, self.max_y + 1)]]
        score = 1
        for other in others:
            blocking = [i for i, t in enumerate(other, start=1) if t >= size]
            score *= blocking[0] if blocking else len(other)
        return score

    def get_visible_trees(self):
        return sum(self.is_visible(x, y) for x, y in self.grid.keys())

    def get_highest_score(self):
        return max(self.senic_score(x, y) for x, y in self.grid.keys())


FOREST = Forest()


def run_1():
    return FOREST.get_visible_trees()


def run_2():
    return FOREST.get_highest_score()


print(run_1())
print(run_2())
