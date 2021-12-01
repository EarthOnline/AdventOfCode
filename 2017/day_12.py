from typing import Set, List, Tuple

INPUT = open("./input_files/input_12", "r").read().strip("\n")


def analyze_connection(connection: str) -> Tuple[int, List[int]]:
    address = [int(x.strip(",")) for x in connection.split(" ") if x != "<->"]
    return address[0], address[1:]


def build_group(connections: List[str], start: int) -> Set[int]:
    group_list = set()
    group_list.add(start)
    result = 0

    while result != len(group_list):
        result = len(group_list)

        for connection in connections:
            address, pipes = analyze_connection(connection)
            if address not in group_list:
                continue
            group_list |= set(pipes)
    return group_list


def run_1():
    return len(build_group(INPUT.split("\n"), 0))


def run_2():
    connections = INPUT.split("\n")
    used = set()
    groups = 0

    for connection in connections:
        address, _pipes = analyze_connection(connection)
        if address in used:
            continue
        used |= build_group(connections, address)
        groups += 1

    return groups


print(run_1())
print(run_2())
