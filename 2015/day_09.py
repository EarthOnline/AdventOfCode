from itertools import permutations
from typing import List, Dict, Tuple

INPUT = open("./input_files/input_09", "r").read().strip("\n")


def calc_dictances() -> Dict[Tuple[str, str], int]:
    distances = dict()
    for line in INPUT.split("\n"):
        parts = line.split(" ")
        distances[(parts[0], parts[2])] = int(parts[4])
        distances[(parts[2], parts[0])] = int(parts[4])
    return distances


DISTANCES = calc_dictances()


def get_cities():
    cities = set()
    for line in INPUT.split("\n"):
        parts = line.split(" ")
        cities.add(parts[0])
        cities.add(parts[2])
    return list(cities)


def get_dictance(city_1: str, city_2: str) -> int:
    return DISTANCES[(city_1, city_2)]


def get_total_distance(route: List[str]) -> int:
    return sum([get_dictance(route[x], route[x + 1]) for x in range(len(route) - 1)])


def run_1():
    cities = get_cities()
    return min([get_total_distance(x) for x in permutations(cities, len(cities))])


def run_2():
    cities = get_cities()
    return max([get_total_distance(x) for x in permutations(cities, len(cities))])


print(run_1())
print(run_2())
