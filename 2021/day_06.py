INPUT = open("./input_files/input_06", "r").read().strip("\n")
# INPUT = """3,4,3,1,2"""
FISH = [int(x) for x in INPUT.split(',')]


def lantern_simulation(days: int) -> int:
    fishy = {x: 0 for x in range(9)}

    for x in FISH:
        fishy[x] += 1

    for d in range(days):
        fishy = {
            0: fishy[1],
            1: fishy[2],
            2: fishy[3],
            3: fishy[4],
            4: fishy[5],
            5: fishy[6],
            6: fishy[7] + fishy[0],
            7: fishy[8],
            8: fishy[0]
        }

    return sum(fishy.values())


def run_1():
    return lantern_simulation(80)


def run_2():
    return lantern_simulation(256)


print(run_1())
print(run_2())
