from collections import deque, defaultdict
from itertools import chain, product
from time import time

start = time()
INPUT = open("./input_files/input_23", "r").read().strip("\n")

ELVES = set(chain.from_iterable([(x, y) for x, v in enumerate(r) if v == '#'] for y, r in enumerate(INPUT.split('\n'))))

POSITIONS = {
    'NW': lambda x, y: (x - 1, y - 1),
    'N': lambda x, y: (x, y - 1),
    'NE': lambda x, y: (x + 1, y - 1),
    'W': lambda x, y: (x - 1, y),
    'E': lambda x, y: (x + 1, y),
    'SW': lambda x, y: (x - 1, y + 1),
    'S': lambda x, y: (x, y + 1),
    'SE': lambda x, y: (x + 1, y + 1),
}

ADJACENT = list(POSITIONS.values())


def is_elf_adjacent(elves, x, y):
    return any(a(x, y) in elves for a in ADJACENT)


def move(elves, x, y, directions):
    for check, _move in directions:
        if all(c(x, y) not in elves for c in check):
            return _move(x, y)
    return x, y


def run_rounds(max_rounds):
    elves = ELVES
    directions = deque([((POSITIONS['NW'], POSITIONS['N'], POSITIONS['NE']), POSITIONS['N']),
                        ((POSITIONS['SW'], POSITIONS['S'], POSITIONS['SE']), POSITIONS['S']),
                        ((POSITIONS['NW'], POSITIONS['W'], POSITIONS['SW']), POSITIONS['W']),
                        ((POSITIONS['NE'], POSITIONS['E'], POSITIONS['SE']), POSITIONS['E'])])

    round = 0
    while True:
        round += 1
        elves_to_move = set(e for e in elves if is_elf_adjacent(elves, *e))
        if len(elves_to_move) == 0:  # Result part 2
            return round

        elves_to_stay = elves.difference(elves_to_move)
        proposed = defaultdict(set)
        for elf in elves_to_move:
            proposed[move(elves, *elf, directions)].add(elf)

        for location, target_elves in proposed.items():
            if len(target_elves) == 1:
                elves_to_stay.add(location)
                continue

            elves_to_stay.update(target_elves)

        elves = elves_to_stay
        directions.append(directions.popleft())

        if round == max_rounds:  # Result part 1
            return elves


def run_1():
    elves = run_rounds(10)

    min_x, max_x = min(x for x, y in elves), max(x for x, y in elves)
    min_y, max_y = min(y for x, y in elves), max(y for x, y in elves)
    return len(set(product(range(min_x, max_x + 1), range(min_y, max_y + 1))).difference(elves))


def run_2():
    return run_rounds(None)


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
