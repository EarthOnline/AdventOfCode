import re
from collections import defaultdict

INPUT = open("./input_files/input_23", "r").read().strip("\n")


# INPUT = """pos=<10,12,12>, r=2
# pos=<12,14,12>, r=2
# pos=<16,12,12>, r=4
# pos=<14,14,14>, r=6
# pos=<50,50,50>, r=200
# pos=<10,10,10>, r=5"""


def get_bot(defenition: str):
    position, r = defenition.split(', ')
    position = position[5:-1]
    positions = position.split(',')
    result = (int(positions[0]), int(positions[1]), int(positions[2]), int(r[2:]))
    return result


BOTS = [get_bot(b) for b in INPUT.split('\n')]


def in_range(bot1, bot2):
    x = abs(bot1[0] - bot2[0])
    y = abs(bot1[1] - bot2[1])
    z = abs(bot1[2] - bot2[2])
    return x + y + z <= bot1[3]


def run_1():
    radiuss = [b[3] for b in BOTS]
    bot = BOTS[radiuss.index(max(radiuss))]
    bots = [b for b in BOTS if in_range(bot, b)]
    return len(bots)


def get_distance(bot1, bot2):
    x = abs(bot1[0] - bot2[0])
    y = abs(bot1[1] - bot2[1])
    z = abs(bot1[2] - bot2[2])
    return x + y + z


def run_2():
    bots = BOTS
    # FIX: Adding [0] to each range to make sure it's tested for
    xs = [x[0] for x in bots] + [0]
    ys = [x[1] for x in bots] + [0]
    zs = [x[2] for x in bots] + [0]

    dist = 1
    while dist < max(xs) - min(xs):
        dist *= 2

    while True:
        target_count = 0
        best = None
        best_val = None
        for x in range(min(xs), max(xs) + 1, dist):
            for y in range(min(ys), max(ys) + 1, dist):
                for z in range(min(zs), max(zs) + 1, dist):
                    count = 0
                    for bx, by, bz, bdist in bots:
                        calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                        # FIX: Python 3 changes how div works, we want integer math here
                        if (calc - bdist) // dist <= 0:
                            count += 1
                    if count > target_count:
                        target_count = count
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)
                    elif count == target_count:
                        if best_val is None or abs(x) + abs(y) + abs(z) < best_val:
                            best_val = abs(x) + abs(y) + abs(z)
                            best = (x, y, z)

        if dist == 1:
            print("The max count I found was: " + str(target_count))
            return best_val
        else:
            xs = [best[0] - dist, best[0] + dist]
            ys = [best[1] - dist, best[1] + dist]
            zs = [best[2] - dist, best[2] + dist]
            # FIX: Python 3 changes how div works, we want integer math here
            dist = dist // 2


print(run_1())
print(run_2())
