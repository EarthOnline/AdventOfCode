INPUT = open("./input_files/input_07", "r").read().strip("\n")
INPUT = """16,1,2,0,4,2,7,1,2,14"""
SUBMARINES = [int(x) for x in INPUT.split(',')]

SUB_MIN = min(SUBMARINES)
SUB_MAX = max(SUBMARINES)


def run_1():
    return min(sum(map(lambda x: abs(x - p), SUBMARINES)) for p in range(SUB_MIN, SUB_MAX))


def run_2():  # aantal_integers * (start_positie + eind_positie) / 2 == n * (n + 1) // 2
    return min(sum(d * (d+1) // 2 for d in map(lambda x: abs(x - p), SUBMARINES)) for p in range(SUB_MIN, SUB_MAX))


print(run_1())
print(run_2())
