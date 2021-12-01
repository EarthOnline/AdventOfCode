INPUT = open("./input_files/input_09", "r").read().strip("\n")
# INPUT = "9 players; last marble is worth 25 points"
# INPUT = "10 players; last marble is worth 1618 points"
# INPUT = "13 players; last marble is worth 7999 points"
# INPUT = "17 players; last marble is worth 1104 points"
# INPUT = "21 players; last marble is worth 6111 points"
# INPUT = "30 players; last marble is worth 5807 points"


def read_input():
    players, _, _, _, _, _, marbles, _ = INPUT.split("\n")[0].split(" ")
    return int(players), int(marbles)


PLAYERS, MARBLES = read_input()


def get_position(current_position: int, move: int, size: int) -> int:
    return (current_position + move) % size


def run_1():
    marbles = [0]
    current_position = 0
    scores = {x: 0 for x in range(PLAYERS)}

    for x in range(1, MARBLES + 1):
        if x % 23 == 0:
            position = get_position(current_position, -7, len(marbles))
            scores[x % PLAYERS] += marbles[position] + x
            del marbles[position]
            current_position = position
        else:
            position = get_position(current_position, 2, len(marbles))
            marbles.insert(position, x)
            current_position = position
    return max(scores.values())


class Marble:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Marble = None
        self.previous: Marble = None


def run_2():
    marble = Marble(0)
    marble.next = marble
    marble.previous = marble
    scores = {x: 0 for x in range(PLAYERS)}

    for x in range(1, MARBLES * 100 + 1):
        if x % 23 == 0:
            right_marble = marble.previous.previous.previous.previous.previous.previous
            selected_marble = right_marble.previous
            left_marble = selected_marble.previous
            right_marble.previous = left_marble
            left_marble.next = right_marble

            scores[x % PLAYERS] += selected_marble.value + x
            marble = right_marble
        else:
            new_marble = Marble(x)
            left_marble = marble.next
            new_marble.previous = left_marble
            right_marble = left_marble.next
            new_marble.next = right_marble
            left_marble.next = new_marble
            right_marble.previous = new_marble
            marble = new_marble
    return max(scores.values())


print(run_1())
print(run_2())
