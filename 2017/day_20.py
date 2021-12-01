from collections import defaultdict
from operator import add
from typing import List, Dict, Tuple

INPUT = open("./input_files/input_20", "r").read().strip("\n")

P = 'p'
V = 'v'
A = 'a'


def run_1():
    slow_particle = None
    slow_particle_acc = None

    for particle, definition in enumerate(INPUT.split("\n")):
        acc = sum([abs(int(x)) for x in definition.split(" ")[2][3:-1].split(",")])
        if slow_particle_acc is None or acc < slow_particle_acc:
            slow_particle_acc = acc
            slow_particle = particle
    return slow_particle


def get_input(input: str) -> List[Dict[str, Tuple[int, int, int]]]:
    result = list()
    for definition in input.split("\n"):
        p, v, a = [[int(x) for x in d[3:-1].split(",")] for d in definition.split(", ")]
        result.append(dict(p=p, v=v, a=a))
    return result


def move(particle: Dict[str, Tuple[int, int, int]]) -> Tuple[int, int, int]:
        particle[V] = tuple(map(add, particle[V], particle[A]))
        particle[P] = tuple(map(add, particle[P], particle[V]))
        return particle[P]


def run_2():
    all_particles = get_input(INPUT)
    for x in range(100):
        locations = defaultdict(list)
        for particle in all_particles:
            locations[move(particle)].append(particle)

        all_particles = list()
        for location, particles in locations.items():
            if len(particles) > 1:
                continue
            all_particles.extend(particles)
    return len(all_particles)


print(run_1())
print(run_2())
