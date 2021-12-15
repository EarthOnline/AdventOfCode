from itertools import product, chain

INPUT = open("./input_files/input_15", "r").read().strip("\n")
# INPUT = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""


def map_cave(text):
    lines = text.split('\n')
    for x, y in product(range(len(lines[0])), range(len(lines))):
        yield (x, y), int(lines[y][x])


CAVE = dict(map_cave(INPUT))


def adjecent(x, y, max_x, max_y):
    if x > 0:
        yield x -1, y
    if x < max_x:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < max_y:
        yield x, y + 1


def lowest_route(cave):
    max_x = max(x for x, y in cave.keys())
    max_y = max(y for x, y in cave.keys())

    been_there = set()
    step = 0

    current_positions = {k: set() for k in range(10)}
    current_positions[0].add((0, 0))
    while (max_x, max_y) not in current_positions[0]:
        step += 1
        new_positions = current_positions.pop(0)

        for p in new_positions:
            if p in been_there:
                continue
            been_there.add(p)

            posibilities = [c for c in adjecent(*p, max_x, max_y) if c not in been_there]
            for pos in posibilities:
                current_positions[cave[pos]].add(pos)

        current_positions = {k - 1: v for k, v in current_positions.items()}
        current_positions[9] = set()

    return step


def run_1():
    return lowest_route(CAVE)


def run_2():
    first_cave = [list(chain.from_iterable(map(lambda x: (int(x) + r - 1) % 9 + 1
                                               , c) for r in range(5))) for c in INPUT.split('\n')]

    large_cave = []
    for r in range(5):
        for line in first_cave:
            large_cave.append(list(map(lambda x: (int(x) + r - 1) % 9 + 1, line)))

    cave = {(x, y): large_cave[y][x] for x, y in product(range(len(first_cave[0])), range(len(first_cave[0])))}
    return lowest_route(cave)


print(run_1())
print(run_2())
