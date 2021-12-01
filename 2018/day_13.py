from typing import List, Tuple, Dict

INPUT = open("./input_files/input_13", "r").read().strip("\n")
# INPUT = """/->-\
# |   |  /----\\
# | /-+--+-\  |
# | | |  | v  |
# \-+-/  \-+--/
#   \------/   """
# INPUT = """/>-<\
# |   |
# | /<+-\\
# | | | v
# \>+</ |
#   |   ^
#   \<->/"""


HORIZONTAL = '-'
VERTICAL = '|'
CORNER = ['\\', '/']
INTERSECTION = '+'
CAR_UP = '^'
CAR_DOWN = 'v'
CAR_RIGHT = '>'
CAR_LEFT = '<'

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

LEFT = 0
STRAIGHT = 1
RIGHT = 2


class Car:
    directions = {CAR_UP: NORTH,
                  CAR_RIGHT: EAST,
                  CAR_DOWN: SOUTH,
                  CAR_LEFT: WEST}

    def __init__(self, car: str):
        self.track = HORIZONTAL if car in [CAR_LEFT, CAR_RIGHT] else VERTICAL
        self.direction = Car.directions[car]
        self.turn = LEFT

    def move(self, location: Tuple[int, int], tracks: List[List[str]]) -> Tuple[int, int]:
        x, y = location
        if self.direction == NORTH:
            y -= 1
        elif self.direction == EAST:
            x += 1
        elif self.direction == SOUTH:
            y += 1
        elif self.direction == WEST:
            x -= 1
        self.track = tracks[y][x]

        if self.track in CORNER:
            if self.direction in [EAST, WEST]:
                self.direction = NORTH if y > 0 and tracks[y-1][x] in [VERTICAL, INTERSECTION] else SOUTH
            else:
                self.direction = WEST if x > 0 and tracks[y][x-1] in [HORIZONTAL, INTERSECTION] else EAST

        if self.track == INTERSECTION:
            self.direction = (self.direction - 1 + self.turn) % 4
            self.turn = (self.turn + 1) % 3
        return x, y


def get_track() -> Tuple[List[List[str]], Dict[Tuple[int, int], Car]]:
    tracks = list()
    cars = dict()
    for y, line in enumerate(INPUT.splitlines()):
        row = list()
        for x, track in enumerate(line):
            if track in [CAR_UP, CAR_RIGHT, CAR_DOWN, CAR_LEFT]:
                car = Car(track)
                cars[(x, y)] = car
                row.append(car.track)
            else:
                row.append(track)
        tracks.append(row)
    return tracks, cars


def run_1():
    tracks, cars = get_track()
    tick = 0

    while True:
        tick += 1
        for location in sorted(cars.keys(), key=lambda x: x[1] * 100 + x[0]):
            car = cars.pop(location)
            new_location = car.move(location, tracks)
            if new_location in cars.keys():
                return f"{new_location[0]},{new_location[1]}"
            cars[new_location] = car


def run_2():
    tracks, cars = get_track()
    tick = 0

    while True:
        end = len(cars.keys()) == 1

        tick += 1
        for location in sorted(cars.keys(), key=lambda x: x[1] * 100 + x[0]):
            if location not in cars:
                continue
            car = cars.pop(location)
            new_location = car.move(location, tracks)
            if new_location in cars.keys():
                cars.pop(new_location)
            else:
                cars[new_location] = car
        if end:
            break
    return f"{location[0]},{location[1]}"


print(run_1())
print(run_2())
