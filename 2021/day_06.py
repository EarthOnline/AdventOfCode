INPUT = open("./input_files/input_06", "r").read().strip("\n")
# INPUT = """3,4,3,1,2"""
FISH = [int(x) for x in INPUT.split(',')]


def lantern_simulation(days: int) -> int:
    fishy = [0 for x in range(9)]

    for x in FISH:
        fishy[x] += 1

    for d in range(days):
        # fishy = [
        #     fishy[1],
        #     fishy[2],
        #     fishy[3],
        #     fishy[4],
        #     fishy[5],
        #     fishy[6],
        #     fishy[7] + fishy[0],
        #     fishy[8],
        #     fishy[0]
        # ]

        new_fish = fishy.pop(0)
        fishy[6] += new_fish
        fishy.append(new_fish)

    return sum(fishy)


def run_1():
    return lantern_simulation(80)


def run_2():
    return lantern_simulation(256)


print(run_1())
print(run_2())
