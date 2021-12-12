from collections import defaultdict
from typing import Dict, List, Set

from copy import copy

INPUT = open("./input_files/input_12", "r").read().strip("\n")
# INPUT = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""


def get_connections(paths: List[str]) -> Dict[str, Set[str]]:
    connections = defaultdict(set)
    for path in paths:
        s, e = path.split('-')
        if e != 'start':
            connections[s].add(e)
        if s != 'start':
            connections[e].add(s)
    return connections


PATHS = get_connections(INPUT.split('\n'))
ONLY_ONCE = [x for x in PATHS.keys() if x.lower() == x]


def find_paths(start: str, end: str, current_path: List[str], can_cheat: bool = False) -> List[List[str]]:
    if start == end:
        return [current_path]

    paths = []
    for option in PATHS.get(start, []):
        if can_cheat is False and option in ONLY_ONCE and option in current_path:
            continue
        _can_cheat = can_cheat ^ (option in ONLY_ONCE and option in current_path)
        _cp = copy(current_path)
        _cp.append(option)
        paths.extend(find_paths(option, end, _cp, _can_cheat))
    return paths


def run_1():
    return len(find_paths('start', 'end', ['start']))


def run_2():
    return len(find_paths('start', 'end', ['start'], can_cheat=True))


print(run_1())
print(run_2())
