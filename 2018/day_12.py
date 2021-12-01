from typing import Dict, Tuple

INPUT = open("./input_files/input_12", "r").read().strip("\n")
# INPUT = """initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #"""

PLANT = '#'
EMPTY = '.'


def get_pots() -> Dict[int, bool]:
    pots = dict()
    for number, contents in enumerate(INPUT.splitlines()[0][15:]):
        pots[number] = contents == PLANT
    return pots


POTS = get_pots()


def get_rules() -> Dict[Tuple[bool, bool, bool, bool, bool], bool]:
    rules = dict()
    for rule in INPUT.splitlines()[2:]:
        rules[(rule[0:1] == PLANT,
               rule[1:2] == PLANT,
               rule[2:3] == PLANT,
               rule[3:4] == PLANT,
               rule[4:5] == PLANT)] = rule[-1:] == PLANT
    return rules


RULES = get_rules()


def run_1():
    pots = POTS
    for x in range(20):
        next_gen = dict()
        for number in range(min(pots.keys()) - 2, max(pots.keys()) + 2):
            next_plant = RULES.get((pots.get(number - 2, False),
                                    pots.get(number - 1, False),
                                    pots.get(number, False),
                                    pots.get(number + 1, False),
                                    pots.get(number + 2, False)), False)
            if next_plant:
                next_gen[number] = next_plant
        pots = next_gen
    return sum([k for k, v in pots.items() if v])


def get_configuration(pots: Dict[int, bool]) -> str:
    return ''.join([PLANT if pots.get(x, False) else EMPTY for x in range(min(pots.keys()), max(pots.keys()) + 1)])


def run_2():
    configurations = list()
    pots = POTS
    configurations.append(get_configuration(pots))
    for x in range(50000000000):
        next_gen = dict()
        for number in range(min(pots.keys()) - 2, max(pots.keys()) + 2):
            next_plant = RULES.get((pots.get(number - 2, False),
                                    pots.get(number - 1, False),
                                    pots.get(number, False),
                                    pots.get(number + 1, False),
                                    pots.get(number + 2, False)), False)
            if next_plant:
                next_gen[number] = next_plant
        pots = next_gen
        configuration = get_configuration(pots)
        if configuration in configurations:
            break
        else:
            configurations.append(configuration)

    shift = 50000000000 - len(configurations)
    return sum([k + shift for k, v in pots.items() if v])


print(run_1())
print(run_2())
