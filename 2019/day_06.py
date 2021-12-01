from typing import Tuple

INPUT = open("./input_files/input_06", "r").read().strip("\n")


# INPUT = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""


def get_orbit(orbit: str) -> Tuple[str, str]:
    objects = orbit.split(')')
    return objects[0], objects[1]


ORBITS = [get_orbit(o) for o in INPUT.split('\n')]

ROUTES = {object_2: object_1 for object_1, object_2 in ORBITS}

OBJECTS = [object_2 for object_1, object_2 in ORBITS]


def steps_to_object(object_to, object_from):
    if object_to == object_from:
        return 0
    return 1 + steps_to_object(object_to, ROUTES[object_from])


def run_1():
    return sum([steps_to_object('COM', o) for o in OBJECTS])


def get_orbits(object):
    if object == 'COM':
        return []
    orbits = get_orbits(ROUTES[object])
    orbits.append(object)
    return orbits


def get_route(object_to, object_from):
    route_from = get_orbits(object_from)[::-1]
    route_to = get_orbits(object_to)[::-1]
    print(route_from)
    print(route_to)

    duplicate = [r for r in route_to if r in route_from][0]
    return route_from.index(duplicate) + route_to.index(duplicate) - 2


def run_2():
    return get_route('SAN', 'YOU')


print(run_1())
print(run_2())
