import string
from typing import Set

INPUT = open("./input_files/input_05", "r").read().strip("\n")


ALPHABET_LOWER = string.ascii_lowercase


def get_combinations() -> Set[str]:
    result = set()
    for letter in ALPHABET_LOWER:
        result.add(f'{letter}{letter.upper()}')
        result.add(f'{letter.upper()}{letter}')
    return result


COMBINATIONS = get_combinations()


def reduce_polymer(polymer: str) -> int:
    last_pass_len = None

    while len(polymer) != last_pass_len:
        last_pass_len = len(polymer)

        for x in COMBINATIONS:
            polymer = polymer.replace(x, '')
    return len(polymer)


def run_1():
    return reduce_polymer(INPUT)


def run_2():
    return min([reduce_polymer(INPUT.replace(unit, '').replace(unit.upper(), '')) for unit in ALPHABET_LOWER])


print(run_1())
print(run_2())
