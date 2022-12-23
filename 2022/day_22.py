import string
from time import time

start = time()
INPUT = open("./input_files/input_22", "r").read().strip("\n")


class Board:
    MOVES = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
    ]

    def __init__(self):
        self.open = set()
        self.wall = set()
        self.field = set()

        for y, row in enumerate(INPUT.split('\n\n')[0].split('\n'), start=1):
            for x, tile in enumerate(row, start=1):
                if tile == '.':
                    self.open.add((x, y))
                    self.field.add((x, y))
                if tile == '#':
                    self.wall.add((x, y))
                    self.field.add((x, y))

    def wrap_around(self, current_x, current_y, d):
        if d == 0:
            return min(x for x, y in self.field if y == current_y), current_y
        if d == 1:
            return current_x, min(y for x, y in self.field if x == current_x)
        if d == 2:
            return max(x for x, y in self.field if y == current_y), current_y
        if d == 3:
            return current_x, max(y for x, y in self.field if x == current_x)
        return current_x, current_y

    def wrap_cube(self, current_x, current_y, direction):
        if direction == 0:
            if 1 <= current_y <= 50:
                return (100, 151 - current_y), 2
            if current_y <= 100:
                return (current_y + 50, 50), 3
            if current_y <= 150:
                return (150, 151 - current_y), 2
            return (current_y - 100, 150), 3

        if direction == 2:
            if 1 <= current_y <= 50:
                return (1, 151 - current_y), 0
            if current_y <= 100:
                return (current_y - 50, 101), 1
            if current_y <= 150:
                return (51, 151 - current_y), 0
            return (current_y - 100, 1), 1

        if direction == 3:
            if current_y == 100:
                return (51, 50 + current_x), 0
            if 51 <= current_x <= 100:
                return (1, current_x + 100), 0
            return (current_x - 100, 200), 3

        if direction == 1:
            if current_y == 51:
                return (100, current_x - 50), 2
            if current_y == 151:
                return (50, current_x + 100), 2
            return (current_x + 100, 1), 1

    def get_password(self, moves, cube=False):
        direction = 0
        position = self.wrap_around(1, 1, 0)

        for move in moves:
            if move == 'L':
                direction = (direction - 1) % 4
                continue

            if move == 'R':
                direction = (direction + 1) % 4
                continue

            for _ in range(move):
                new_position = self.MOVES[direction](*position)
                new_direction = direction
                if new_position not in self.field:
                    if cube:
                        new_position, new_direction = self.wrap_cube(*new_position, direction)
                    else:
                        new_position = self.wrap_around(*new_position, direction)
                if new_position in self.wall:
                    break
                position = new_position
                direction = new_direction

        x, y = position
        return 1000 * y + 4 * x + direction


def translate_moves(input):
    buffer = ''
    for i in input:
        if i in string.digits:
            buffer += i
            continue

        yield int(buffer)
        yield i
        buffer = ''

    if buffer != '':
        yield int(buffer)


MOVES = list(translate_moves(INPUT.split('\n\n')[1]))


def run_1():
    board = Board()
    return board.get_password(MOVES)


def run_2():
    board = Board()
    return board.get_password(MOVES, cube=True)


print('\n', 'Part 1 ==> ', run_1())
print(f'in {int((time() - start) * 1000)} ms')
print('\n', 'Part 2 ==> ', run_2())
print(f'in {int((time() - start) * 1000)} ms')
