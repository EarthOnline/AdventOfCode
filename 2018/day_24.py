from operator import attrgetter

INPUT = open("./input_files/input_24", "r").read().strip("\n")


class Group:
    def __init__(self, info: str, army: str):
        self.army = army

        info = info.replace(' units each with ', '|')
        info = info.replace(' hit points ', '|')
        info = info.replace('with an attack that does ', '|')
        info = info.replace(' damage at initiative ', '|')
        infos = info.split('|')
        self.units = int(infos[0])
        self.hit_points = int(infos[1])
        self.initiative = int(infos[4])
        self.weaknesses = list()
        self.immunities = list()

        atk = infos[3].split(' ')
        self.attack_damage = int(atk[0])
        self.attack_type = atk[1]

        sow = infos[2].replace('(', '').replace(') ', '').split('; ')
        sow = [x.split(' to ') for x in sow]
        for s in sow:
            if s[0] == 'weak':
                self.weaknesses.extend(s[1].split(', '))
            if s[0] == 'immune':
                self.immunities.extend(s[1].split(', '))

    @property
    def effective_power(self) -> int:
        return self.units * self.attack_damage

    def __str__(self):
        return f"{self.army}::{self.initiative}"

    def attack(self, opponent):
        if not opponent:
            return
        opponent.take_damage(self.effective_power, self.attack_type)

    def can_attack(self, opponent):
        if not opponent:
            return False

        return opponent.receiving_power(self.effective_power, self.attack_type) >= opponent.hit_points

    def receiving_power(self, effective_power, attack_type):
        if attack_type in self.immunities:
            effective_power = 0
        if attack_type in self.weaknesses:
            effective_power = 2 * effective_power
        return effective_power

    def take_damage(self, effective_power, attack_type):
        effective_power = self.receiving_power(effective_power, attack_type)
        killed_units = effective_power // self.hit_points
        self.units = self.units - killed_units if killed_units < self.units else 0


def get_groups():
    groups = list()
    current_army = ''
    for i in INPUT.split('\n'):
        if not i:
            current_army = ''
            continue
        if not i[0].isnumeric():
            current_army = i[:-1]
            continue
        groups.append(Group(i, current_army))
    return groups


def fight(groups):
    skirmishes = target_selection(groups)
    attack(skirmishes)

    return [g for g in groups if g.units > 0]


def target_selection(groups):
    untargeted = sorted(groups, key=attrgetter('effective_power', 'initiative'), reverse=True)
    selection_que = [dict(attacking=x, defending=None) for x in untargeted]

    for selection in selection_que:
        group = selection['attacking']

        weak_targets = [t for t in untargeted if group.army != t.army and group.attack_type in t.weaknesses]
        if weak_targets:
            selection['defending'] = weak_targets[0]
            untargeted.remove(weak_targets[0])
            continue

        targets = [t for t in untargeted if group.army != t.army and group.attack_type not in t.immunities]
        if targets:
            selection['defending'] = targets[0]
            untargeted.remove(targets[0])
            continue

    return selection_que


def attack(skirmishes):
    if not any([x['attacking'].can_attack(x['defending']) for x in skirmishes]):
        raise DeadlockError()

    skirmishes = sorted(skirmishes, key=lambda x: x['attacking'].initiative, reverse=True)
    for skirmish in skirmishes:
        skirmish['attacking'].attack(skirmish['defending'])


def group_count(groups, army):
    return len([g for g in groups if g.army == army])


class DeadlockError(Exception):
    pass


def battle(boost=0):
    groups = get_groups()
    if boost:
        for group in groups:
            if group.army == 'Immune System':
                group.attack_damage += boost

    while group_count(groups, 'Immune System') and group_count(groups, 'Infection'):
        try:
            groups = fight(groups)
        except DeadlockError:
            return 'Deadlock', 0

    return 'Immune System' if group_count(groups, 'Immune System') else 'Infection', sum([g.units for g in groups])


def run_1():
    winner, units = battle()
    return units


def run_2():
    winner = ''
    units = 0
    boost = 0
    while winner != 'Immune System':
        boost += 1
        winner, units = battle(boost=boost)
        print(boost, winner, units)

    return units


print(run_1())
print(run_2())
