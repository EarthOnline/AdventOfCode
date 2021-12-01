from typing import Dict, Tuple, Optional

INPUT = open("./input_files/input_15", "r").read().strip("\n")
# INPUT = """#######
# #.G...#
# #...EG#
# #.#.#G#
# #..G#E#
# #.....#
# #######"""
# INPUT = """#######
# #.E...#
# #.#..G#
# #.###.#
# #E#G#G#
# #...#G#
# #######"""

WALL = '#'
EMPTY = '.'

ELF = 'E'
GOBLIN = 'G'


def get_in_range(x, y):
    return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]


class Character:
    def __init__(self, x: int, y: int, ctype: str, cavern: 'Cavern'):
        self.cavern = cavern
        self.x = x
        self.y = y
        self.type = ctype
        self.atack_power = 3
        self.health_points = 200

    def do_turn(self):
        if self.health_points <= 0:
            return
        target = self.can_atack()
        if target:
            target.take_damage(self.atack_power)
            return
        x, y = self.find_step(self.x, self.y)
        del self.cavern.characters[(self.x, self.y)]
        self.x = x
        self.y = y
        self.cavern.characters[(x, y)] = self
        target = self.can_atack()
        if target:
            target.take_damage(self.atack_power)
            return

    def find_step(self, x: int, y: int) -> Tuple[int, int]:
        targets = [x for x in self.cavern.characters.values() if self.is_enemy(x)]
        in_range = list()
        for t in targets:
            for p in [p for p in get_in_range(t.x, t.y) if self.cavern.is_open(*p) and p not in in_range]:
                in_range.append(p)
        in_range.sort(key=lambda k: k[0] + k[1] * 100)
        distances = [self.get_distance(*l) for l in in_range]
        reachable = [d for d in distances if d is not None]
        if len(reachable) == 0:
            return x, y
        distance = min(reachable)
        target = in_range[distances.index(distance)]
        positions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
        enemy_range = [self.get_distance_from_position(*p, *target) for p in positions]
        distances = [x for x in enemy_range if x is not None]
        if len(distances) == 0:
            return x, y
        return positions[enemy_range.index(min(distances))]

    def get_distance(self, find_x: int, find_y: int) -> Optional[int]:
        tried = set()
        step = 0
        step_locations = dict()
        step_locations[step] = [(self.x, self.y)]
        tried.add((self.x, self.y))
        while len(step_locations[step]) > 0:
            step += 1
            step_locations[step] = list()
            for x, y in step_locations[step - 1]:
                positions = [p for p in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)] if p not in tried]
                for p in positions:
                    tried.add(p)
                    if p == (find_x, find_y):
                        return step
                    if self.cavern.is_open(*p):
                        step_locations[step].append(p)
        return None

    def get_distance_from_position(self, x: int, y: int, find_x: int, find_y: int) -> Optional[int]:
        if not self.cavern.is_open(x, y):
            return None
        if (x, y) == (find_x, find_y):
            return 0
        tried = set()
        step = 0
        step_locations = dict()
        step_locations[step] = [(x, y)]
        tried.add((x, y))
        tried.add((self.x, self.y))
        while len(step_locations[step]) > 0:
            step += 1
            step_locations[step] = list()
            for x, y in step_locations[step - 1]:
                positions = [p for p in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)] if p not in tried]
                for p in positions:
                    tried.add(p)
                    if p == (find_x, find_y):
                        return step
                    if self.cavern.is_open(*p):
                        step_locations[step].append(p)
        return None

    def take_damage(self, damage: int):
        self.health_points -= damage
        if self.health_points <= 0:
            del self.cavern.characters[(self.x, self.y)]

    def can_atack(self) -> Optional['Character']:
        characters = [self.cavern.get_character(*p) for p in [(self.x, self.y - 1),
                                                              (self.x - 1, self.y),
                                                              (self.x + 1, self.y),
                                                              (self.x, self.y + 1)]]
        enemies = [c for c in characters if self.is_enemy(c)]
        if len(enemies) == 0:
            return None
        target_hp = min(c.health_points for c in enemies)
        targets = [e for e in enemies if e.health_points == target_hp]
        return targets[0]

    def is_enemy(self, character: Optional['Character']) -> bool:
        return character is not None and character.type != self.type

    def has_enemies(self):
        return len([x for x in self.cavern.characters.values() if self.is_enemy(x)]) > 0


class Cavern:
    def get_cavern_characters(self, layout: str) -> Tuple[Dict[Tuple[int, int], bool],
                                                          Dict[Tuple[int, int], Character]]:
        cavern = dict()
        characters = dict()
        for y, line in enumerate(layout.splitlines()):
            for x, place in enumerate(line):
                cavern[(x, y)] = place == WALL
                if place in [ELF, GOBLIN]:
                    characters[(x, y)] = Character(x, y, place, self)
        return cavern, characters

    def __init__(self, layout: str):
        self.layout, self.characters = self.get_cavern_characters(layout)

    def turn(self) -> bool:
        characters = self.characters
        for (x, y), character in sorted(characters.items(), key=lambda x: x[0][0] + x[0][1] * 100):
            if not character.has_enemies():
                return False
            character.do_turn()
        return True

    def get_character(self, x: int, y: int) -> Optional[Character]:
        return self.characters.get((x, y), None)

    def is_open(self, x: int, y: int) -> bool:
        if self.get_character(x, y):
            return False
        return not self.layout[(x, y)]

    def _print(self, x: int, y: int):
        car = self.get_character(x, y)
        if car:
            return car.type
        return WALL if self.layout[(x, y)] else EMPTY


def run_1():
    turn = 0
    cavern = Cavern(INPUT)
    while True:
        if not cavern.turn():
            break
        # for y, line in enumerate(INPUT.splitlines()):
        #     print("".join([cavern._print(x, y) for x in range(len(line))]))
        turn += 1
        # print(turn, '----------')
    return turn * sum([c.health_points for c in cavern.characters.values()])


def run_2():
    elf_atack = 3
    while True:
        elf_atack += 1
        turn = 0
        cavern = Cavern(INPUT)
        elfs = [x for x in cavern.characters.values() if x.type == ELF]
        for elf in elfs:
            elf.atack_power = elf_atack
        while True:
            if len(elfs) != len([x for x in cavern.characters.values() if x.type == ELF]):
                print('--', elf_atack)
                break
            if not cavern.turn():
                return turn * sum([c.health_points for c in cavern.characters.values()])
            turn += 1


print(run_1())
print(run_2())
