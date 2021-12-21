from collections import defaultdict

INPUT = open("./input_files/input_21", "r").read().strip("\n")
# INPUT = """Player 1 starting position: 4
# Player 2 starting position: 8"""


class DeterministicDie:
    def __init__(self):
        self.rolls = 0
        self.position = 0

    def roll(self):
        self.rolls += 1
        self.position = self.position % 100 + 1
        return self.position


class Player:
    def __init__(self, description: str):
        self.number = int(description[7])
        self.position = int(description[-2:])
        self.score = 0

    def turn(self, die):
        steps = die.roll()
        steps += die.roll()
        steps += die.roll()

        self.position = (self.position + steps - 1) % 10 + 1
        self.score += self.position


PLAYER_1, PLAYER_2 = [Player(x) for x in INPUT.split('\n')]


def run_1():
    die = DeterministicDie()

    while PLAYER_1.score < 1000 and PLAYER_2.score < 1000:
        PLAYER_1.turn(die)
        if PLAYER_1.score >= 1000:
            break
        PLAYER_2.turn(die)

    return min(PLAYER_1.score, PLAYER_2.score) * die.rolls


def run_2():
    possible_rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    wins = [0, 0]
    p1_start, p2_start = [int(x[-2:]) for x in INPUT.split('\n')]
    possible_universes = {((p1_start, 0), (p2_start, 0)): 1}

    turn = 1
    while possible_universes:
        turn = (turn + 1) % 2
        newly_possible = defaultdict(int)

        for players, observed in possible_universes.items():
            for steps, times in possible_rolls.items():
                player_position, player_score = players[turn]

                player_position = (player_position + steps - 1) % 10 + 1
                player_score += player_position
                new_observations = observed * times
                if player_score >= 21:
                    wins[turn] += new_observations
                    continue

                universe_key = ((player_position, player_score), players[1]) if turn == 0 else (players[0], (player_position, player_score))
                newly_possible[universe_key] += new_observations
        possible_universes = newly_possible

    return max(wins)


print(run_1())
print(run_2())
