INPUT = open("./input_files/input_22", "r").read().strip("\n")

BOSS = tuple([int(x.split(': ')[-1]) for x in INPUT.split('\n')])
PLAYER = (50, 500)


def play_round(player, boss, player_turn, shield=0, poison=0, recharge=0, hard=False):
    # print(player, boss, player_turn, shield, poison, recharge)
    if hard and player_turn:
        player_hp, player_mana = player
        player_hp -= 1
        player = (player_hp, player_mana)

    shield_on = False
    if shield:
        shield_on = True
        shield -= 1

    if poison:
        boss_hp, boss_dmg = boss
        boss_hp -= 3
        boss = (boss_hp, boss_dmg)
        poison -= 1

    if recharge:
        player_hp, player_mana = player
        player_mana += 101
        player = (player_hp, player_mana)
        recharge -= 1

    if player[0] <= 0 or boss[0] <= 0:
        return player[0] > 0, 0

    if not player_turn:
        player_hp, player_mana = player
        boss_hp, boss_dmg = boss
        player_hp -= max(boss_dmg - (7 if shield_on else 0), 1)
        return play_round((player_hp, player_mana), boss, not player_turn, shield, poison, recharge, hard)
    else:
        outcomes = []
        player_hp, player_mana = player
        boss_hp, boss_dmg = boss
        if player_mana >= 53:
            win, mana = play_round((player_hp, player_mana - 53),
                                   (boss_hp - 4, boss_dmg),
                                   not player_turn, shield, poison, recharge, hard)
            outcomes.append((win, mana + 53))
        else:
            return False, 0

        if player_mana >= 73:
            win, mana = play_round((player_hp + 2, player_mana - 73),
                                   (boss_hp - 2, boss_dmg),
                                   not player_turn, shield, poison, recharge, hard)
            outcomes.append((win, mana + 73))

        if player_mana >= 113 and not shield:
            win, mana = play_round((player_hp, player_mana - 113),
                                   (boss_hp, boss_dmg),
                                   not player_turn, 6, poison, recharge, hard)
            outcomes.append((win, mana + 113))

        if player_mana >= 173 and not poison:
            win, mana = play_round((player_hp, player_mana - 173),
                                   (boss_hp, boss_dmg),
                                   not player_turn, shield, 6, recharge, hard)
            outcomes.append((win, mana + 173))

        if player_mana >= 229 and not recharge:
            win, mana = play_round((player_hp, player_mana - 229),
                                   (boss_hp, boss_dmg),
                                   not player_turn, shield, poison, 5, hard)
            outcomes.append((win, mana + 229))

        for win, mana in sorted(outcomes, key=lambda x: x[1]):
            if win:
                return win, mana
        return False, 0


def run_1():
    return play_round(PLAYER, BOSS, True)


def run_2():
    return play_round(PLAYER, BOSS, True, hard=True)


print(run_1())
print(run_2())
