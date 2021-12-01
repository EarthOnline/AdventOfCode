from functools import reduce
from operator import and_
from typing import Dict, List

INPUT = open("./input_files/input_16", "r").read().strip("\n")


def get_aunts() -> List[Dict[str, int]]:
    result = list()
    for aunt in INPUT.split("\n"):
        parts = aunt.replace(":", "").replace(",", "").split(" ")
        result.append({parts[2]: int(parts[3]), parts[4]: int(parts[5]), parts[6]: int(parts[7])})
    return result


AUNTS = get_aunts()


TICKER_TAPE = dict(
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1)


def match(aunt: Dict[str, int]) -> bool:
    return reduce(and_, [TICKER_TAPE[k] == v for k, v in aunt.items()])


def advanced_match(aunt: Dict[str, int]) -> bool:
    result = True
    for key, value in aunt.items():
        if key in ['cats', 'trees']:
            result &= TICKER_TAPE[key] < value
        elif key in ['pomeranians', 'goldfish']:
            result &= TICKER_TAPE[key] > value
        else:
            result &= TICKER_TAPE[key] == value
    return result


def run_1():
    for index, aunt in enumerate(AUNTS):
        if match(aunt):
            return index + 1


def run_2():
    for index, aunt in enumerate(AUNTS):
        if advanced_match(aunt):
            return index + 1


print(run_1())
print(run_2())
