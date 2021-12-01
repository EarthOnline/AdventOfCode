from collections import defaultdict

INPUT = open("./input_files/input_03", "r").read().strip("\n")

WIRES = [[x for x in w.split(',')] for w in INPUT.split('\n')]

# WIRES = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
#          ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]

# WIRES = [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
#          ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]

# WIRES = [['R8', 'U5', 'L5', 'D3'],
#          ['U7', 'R6', 'D4', 'L4']]


def r(x, y):
    x += 1
    return x, y


def l(x, y):
    x -= 1
    return x, y


def d(x, y):
    y += 1
    return x, y


def u(x, y):
    y -= 1
    return x, y


DIRECTION_MAP = dict(R=r, L=l, U=u, D=d)


def grid_value(grid, x, y):
    if x == 0 and y == 0:
        return 'O'
    values = grid[x, y]
    if len(values) == 0:
        return '.'
    if 1 in values or 0 in values:
        return '|'
    if 1 in values and 0 in values:
        return 'X'
    print(values)
    return ' '


def run_1():
    grid = defaultdict(list)

    for index, wire in enumerate(WIRES):
        x = 0
        y = 0

        for action in wire:
            direction = action[:1]
            steps = int(action[1:])
            for _ in range(steps):
                x, y = DIRECTION_MAP.get(direction)(x, y)
                grid[x, y].append(index)

    # xs = [x for (x, y) in grid.keys()]
    # ys = [y for (x, y) in grid.keys()]

    # for y in range(min(ys) - 1,  max(ys) + 1):
    #     print(' '.join([grid_value(grid, x, y) for x in range(min(xs) - 1, max(xs) + 1)]))

    # print([(x, y, abs(x) + abs(y)) for (x, y), c in grid.items() if 1 in c and 0 in c])
    return min([abs(x) + abs(y) for (x, y), c in grid.items() if 1 in c and 0 in c])


def run_2():
    grid = defaultdict(list)
    grid_steps = defaultdict(int)

    for index, wire in enumerate(WIRES):
        x = 0
        y = 0
        step = 0

        for action in wire:
            direction = action[:1]
            steps = int(action[1:])
            for _ in range(steps):
                step += 1
                x, y = DIRECTION_MAP.get(direction)(x, y)
                if index not in grid[x, y]:
                    grid_steps[x, y] += step
                grid[x, y].append(index)

    # xs = [x for (x, y) in grid.keys()]
    # ys = [y for (x, y) in grid.keys()]

    # for y in range(min(ys) - 1,  max(ys) + 1):
    #     print(' '.join([grid_value(grid, x, y) for x in range(min(xs) - 1, max(xs) + 1)]))

    # print([(x, y, abs(x) + abs(y)) for (x, y), c in grid.items() if 1 in c and 0 in c])
    return min([grid_steps[x, y] for (x, y), c in grid.items() if 1 in c and 0 in c])


print(run_1())
print(run_2())
