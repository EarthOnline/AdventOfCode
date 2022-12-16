from copy import copy
from itertools import product, combinations
from time import time

start = time()

INPUT = open("./input_files/input_16", "r").read().strip("\n")


# INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""


def translate(text):
    name = text[6:8]
    rate = int(text.split(';')[0].split('=')[1])
    options = text.replace(', ', ',').split(' ')[-1].split(',')
    return name, (rate, options)


VALVES = dict(translate(x) for x in INPUT.split('\n'))


def shortest_path(s, e):
    visited = set()
    current = (s,)
    steps = 0
    while e not in visited:
        visited.update(current)
        _current = copy(current)
        current = set()
        steps += 1
        for c in _current:
            current.update(x for x in VALVES[c][1] if x not in visited)
    return steps


DISTANCE = {(v, o): shortest_path(v, o) for v, o in product(VALVES.keys(), VALVES.keys()) if v != o}


def potential(s, e, time_left, valves):
    steps = DISTANCE[(s, e)]
    if time_left < steps:
        return 0
    time_left -= steps

    options = [potential(e, o, time_left, set(x for x in valves if x != o)) for o in valves]
    best = max(options) if options else 0

    return best + time_left * VALVES[e][0]


def run_1():
    valves = set(k for k, v in VALVES.items() if v[0] > 0)

    time_left = 30
    location = "AA"
    return max(potential(location, v, time_left, set(x for x in valves if x != v)) for v in valves)


def run_2():
    valves = set(k for k, v in VALVES.items() if v[0] > 0)
    score = 0
    time_left = 26
    location = "AA"
    for player in combinations(valves, len(valves) // 2):
        elephant = valves.difference(player)
        player_score = max(potential(location, v, time_left, set(x for x in player if x != v)) for v in player)
        elephant_score = max(potential(location, v, time_left, set(x for x in elephant if x != v)) for v in elephant)
        score = max(score, player_score + elephant_score)
    return score


print(run_1())
print((time() - start) * 1000)
print(run_2())
print((time() - start) * 1000)
