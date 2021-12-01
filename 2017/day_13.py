from collections import defaultdict
from typing import List, Dict, Tuple

INPUT = open("./input_files/input_13", "r").read().strip("\n")


def analyse_layer(layer: str) -> Tuple[int, int]:
    depth, range = [int(x) for x in layer.split(": ")]
    return depth, range


def build_firewall(layers: List[str]) -> Dict[int, int]:
    firewall = defaultdict(int)
    for layer in layers:
        ldepth, lrange = analyse_layer(layer)
        firewall[ldepth] = lrange
    return firewall


def get_scanner_position(lrange: int, picosecond: int) -> int:
    if lrange == 0:
        return -1
    return picosecond % (lrange * 2 - 2)


def pass_firewall(start: int) -> int:
    score = 0
    firewall = build_firewall(INPUT.split("\n"))
    depth = max(firewall.keys())
    for x in range(depth + 1):
        score += x * firewall[x] if get_scanner_position(firewall[x], x + start) == 0 else 0
    return score


def test_firewall(firewall: Dict[int, int], start: int) -> bool:
    depth = max(firewall.keys())
    for x in range(depth + 1):
        if get_scanner_position(firewall[x], x + start) == 0:
            return True
    return False


def run_1():
    return pass_firewall(0)


def run_2():
    delay = 0
    firewall = build_firewall(INPUT.split("\n"))
    while True:
        if test_firewall(firewall, delay) == 0:
            break
        delay += 1
    return delay


print(run_1())
print(run_2())
