INPUT = open("./input_files/input_04", "r").read().strip("\n")
# INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""


class BingoNumber:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.drawn = False

    def striketrough(self, number: int):
        if self.number == number:
            self.drawn = True
        return self.number == number


class BingoCard:
    def __init__(self, card_init: str):
        self.card_init = card_init
        self.bingo_numbers = []

        card_init = card_init.replace('  ', ' ')
        for y, row in enumerate(card_init.split("\n")):
            row = row.strip()
            for x, number in enumerate(row.split(" ")):
                self.bingo_numbers.append(BingoNumber(x, y, int(number)))

    def strike_number(self, number: int):
        list(map(lambda x: x.striketrough(number), self.bingo_numbers))
        return self.has_bingo

    @property
    def has_bingo(self):
        for xy in range(5):
            if sum(True for n in self.bingo_numbers if n.x == xy and n.drawn) == 5 \
                    or sum(True for n in self.bingo_numbers if n.y == xy and n.drawn) == 5:
                return True
        return False

    def __str__(self):
        return self.card_init

    def __repr__(self):
        return self.__str__()


RANDOM_ORDER = [int(x) for x in INPUT.split("\n\n")[0].split(",")]
CARDS = [BingoCard(x) for x in INPUT.split("\n\n")[1:]]


def run_1():
    for number in RANDOM_ORDER:
        if sum(map(lambda x: x.strike_number(number), CARDS)) > 0:
            break

    card = [c for c in CARDS if c.has_bingo][0]
    unmarked = sum(n.number for n in card.bingo_numbers if n.drawn is False)

    return unmarked * number


def run_2():
    have_bingo = set()
    for number in RANDOM_ORDER:
        if sum(map(lambda x: x.strike_number(number), CARDS)) == len(CARDS):
            break

        have_bingo.update([c for c in CARDS if c.has_bingo])

    card = [c for c in CARDS if c not in have_bingo][0]
    unmarked = sum(n.number for n in card.bingo_numbers if n.drawn is False)

    return unmarked * number


print(run_1())
print(run_2())
