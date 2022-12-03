from functools import reduce
from itertools import chain, combinations, product

INPUT = open("./input_files/input_21", "r").read().strip("\n")

BOSS = tuple([int(x.split(': ')[-1]) for x in INPUT.split('\n')])

WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)]

ARMOR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)]

RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)]


def player_options():
    sets = [list(chain.from_iterable(x)) for x in product(
        [(w,) for w in WEAPONS],
        chain.from_iterable(combinations(ARMOR, r) for r in range(2)),
        chain.from_iterable(combinations(RINGS, r) for r in range(3)))]

    options = [reduce(lambda x, y: tuple([sum(c) for c in zip(x, y)]), s) for s in sets]
    return sorted(options, key=lambda x: x[0])

def play(hitpoints, damage, armor):
    boss_hitpoints, boss_damage, boss_armor = BOSS

    players_turn = True
    while boss_hitpoints > 0 and hitpoints > 0:
        if players_turn:
            boss_hitpoints -= max(damage - boss_armor, 1)
        else:
            hitpoints -= max(boss_damage - armor, 1)

        players_turn = not players_turn

    return hitpoints > 0

def run_1():
    options = player_options()
    for cost, damage, armor in options:
        if play(100, damage, armor):
            return cost
    return None


def run_2():
    options = reversed(player_options())
    for cost, damage, armor in options:
        if not play(100, damage, armor):
            return cost
    return None


print(run_1())
print(run_2())
