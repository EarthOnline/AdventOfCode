from collections import defaultdict

INPUT = open("./input_files/input_14", "r").read().strip("\n")


class Reindeer:
    def __init__(self, reindeer: str):
        specs = reindeer.split(" ")
        self.name = specs[0]
        self.speed = int(specs[3])
        self.endurance = int(specs[6])
        self.rest = int(specs[13])

    def distance(self, seconds: int):
        cycle = self.endurance + self.rest
        moved = (seconds // cycle) * self.endurance + min((seconds % cycle, self.endurance))
        return moved * self.speed


def get_specs():
    return [Reindeer(x) for x in INPUT.split('\n')]


SPECS = get_specs()


def run_1():
    return max([x.distance(2503) for x in SPECS])


def run_2():
    scores = {x.name: 0 for x in SPECS}
    for x in range(2503):
        round_scores = defaultdict(list)
        for y in SPECS:
            round_scores[y.distance(x + 1)].append(y.name)
        for y in round_scores[max(round_scores.keys())]:
            scores[y] += 1
    return max(scores.values())


print(run_1())
print(run_2())
