import itertools
import math
from collections import defaultdict
from copy import deepcopy
from functools import reduce

INPUT = open("./input_files/input_14", "r").read().strip("\n")


def get_reactions():
    reactions = [r for r in INPUT.split('\n')]
    results = dict()
    for reaction in reactions:
        ingredients, result = reaction.split(' => ')
        amount, output = result.split(' ')
        results[output] = (int(amount), [(int(i.split(' ')[0]), i.split(' ')[1]) for i in ingredients.split(', ')])

    return results


REACTIONS = get_reactions()


def make(ammount, output, spares):
    if output == 'ORE':
        return ammount

    if output in spares:  # We might have to over produce some stuff. Go PLANET!
        spares_to_use = min(spares[output], ammount)
        ammount -= spares_to_use
        spares[output] -= spares_to_use

    if ammount == 0:  # no ore used, all from stock
        return 0

    reaction = REACTIONS[output]
    full_reactions = ammount // reaction[0]
    short = ammount % reaction[0]
    if short > 0:  # Put away for ReCycling
        full_reactions += 1
        if output not in spares.keys():
            spares[output] = 0
        spares[output] += reaction[0] - short

    ore = [make(a * full_reactions, i, spares) for a, i in reaction[1]]

    return sum(ore)


def run_1():
    spares = dict()
    return make(1, 'FUEL', spares)


def run_2():
    goal = 1000000000000
    # target = goal // 337075
    # target = 5193698
    # target = 5194098
    target = 5194168

    ore = 0
    while ore < goal:
        spares = dict()
        ore = make(target, 'FUEL', spares)
        print(target, ore, ore > goal)
        target += 1
    return target - 2

print(run_1())
print(run_2())
