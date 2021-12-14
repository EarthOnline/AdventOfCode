from copy import copy

INPUT = open("./input_files/input_22", "r").read().strip("\n")
# INPUT = """Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10"""
PLAYER_1, PLAYER_2 = [[int(c) for c in x.split('\n')[1:]] for x in INPUT.split('\n\n')]


def combat(player_1, player_2):
    while len(player_1) != 0 and len(player_2) != 0:
        c1 = player_1.pop(0)
        c2 = player_2.pop(0)

        if c1 > c2:
            player_1 += [c1, c2]
        else:
            player_2 += [c2, c1]

    return max(player_1, player_2, key=lambda x: len(x))


def run_1():
    winner = combat(copy(PLAYER_1), copy(PLAYER_2))
    return sum(i * v for i, v in enumerate(winner[::-1], 1))


def game_key(player_1, player_2):
    return ','.join(str(x) for x in player_1) + '::' + ','.join(str(x) for x in player_2)


def recursive_combat(player_1, player_2, return_type='score'):
    games = []
    while len(player_1) != 0 and len(player_2) != 0:
        key = game_key(player_1, player_2)
        if key in games:
            return player_1 if return_type == 'score' else 'player_1'
        games.append(key)

        c1 = player_1.pop(0)
        c2 = player_2.pop(0)

        winner = 'player_1' if c1 > c2 else 'player_2'
        if len(player_1) >= c1 and len(player_2) >= c2:
            winner = recursive_combat(player_1[:c1], player_2[:c2], 'player')

        if winner == 'player_1':
            player_1 += [c1, c2]
        else:
            player_2 += [c2, c1]

    if return_type == 'score':
        return max(player_1, player_2, key=lambda x: len(x))
    return 'player_1' if len(player_2) == 0 else 'player_2'


def run_2():
    winner = recursive_combat(copy(PLAYER_1), copy(PLAYER_2))
    return sum(i * v for i, v in enumerate(winner[::-1], 1))


print(run_1())
print(run_2())
