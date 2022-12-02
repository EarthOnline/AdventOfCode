INPUT = open("./input_files/input_02", "r").read().strip("\n")

ROUNDS = [tuple(x.split(' ')) for x in INPUT.split('\n')]

ROCK = 0
PAPER = 1
SCISSORS = 2

TRANSLATE = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

def play_1(turn):
    other, you = [TRANSLATE[x] for x in turn]
    return score(other, you)

def score(other, you):
    shift = 1 - other
    result = (you + shift) % 3 - 1
    return 3 + result * 3 + you + 1

def run_1():
    scores = [play_1(x) for x in ROUNDS]
    return sum(scores)

def play_2(turn):
    other, outcome = [TRANSLATE[x] for x in turn]
    you = (other + (outcome - 1)) % 3
    return score(other, you)

def run_2():
    scores = [play_2(x) for x in ROUNDS]
    return sum(scores)


print(run_1())
print(run_2())
