INPUT = open("./input_files/input_23", "r").read().strip("\n")

lines = (*((*line,) for line in INPUT.splitlines()),)
COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOM_LOCATION = {'A': 3, 'B': 5, 'C': 7, 'D': 9}


def extend(data):
    return (*data[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *data[3:],)


def roomSize(data):
    return len(data) - 3


def field(data, x, y):
    return data[y][x]


def stoppable(data):
    return tuple(i for i in range(1, len(data[0]) - 1) if i not in ROOM_LOCATION.values())


def isInOwnRoom(data, x, y):
    if not isAmphipod(data, x, y):
        return False
    if x == ROOM_LOCATION[field(data, x, y)]:
        return True
    return False


def isInAnyRoom(data, x, y):
    return y > 1








def isAmphipod(data, x, y):
    val = field(data, x, y)
    return val if val in ROOM_LOCATION.keys() else False


def isEmpty(data, x, y):
    return field(data, x, y) == '.'


def isRoomEmpty(data, x):
    for y in range(2, 2 + roomSize(data)):
        if not isEmpty(data, x, y):
            return False
    return True


def isBlockingRoom(data, x, y):
    for j in range(y + 1, 2 + roomSize(data)):
        if isAmphipod(data, x, j) and not isInOwnRoom(data, x, j):
            return True
    return False


def hasRoomAvailable(data, x, y):
    amphipod = field(data, x, y)
    room = ROOM_LOCATION[amphipod]
    if isRoomEmpty(data, room): return True
    for y in range(2, 2 + roomSize(data)):
        if not isEmpty(data, room, y) and not isInOwnRoom(data, room, y):
            return False
    return True


def isPathEmpty(data, x, targetX):
    while x != targetX:
        if x > targetX:
            x -= 1
        if x < targetX:
            x += 1
        if not isEmpty(data, x, 1):
            return False
    return True


def isBlockedInRoom(data, x, y):
    if y < 3: return False
    return not isEmpty(data, x, y - 1)


def moveinPos(data, room):
    for y in range(1 + roomSize(data), 1, -1):
        if isEmpty(data, room, y):
            return y


def canMove(data, x, y):
    return (not isInOwnRoom(data, x, y) or isBlockingRoom(data, x, y)) and not isBlockedInRoom(data, x, y)


def moveCost(data, x, y, i, j):
    return ((y - 1) + abs(x - i) + (j - 1)) * COST[field(data, x, y)]


def move(d, x, y, i, j):
    newData = (*((*(((field(d, a, b), field(d, x, y))[a == i and b == j], field(d, i, j))[a == x and b == y] for a in
                    range(len(d[b]))),) for b in range(len(d))),)
    return (newData, moveCost(d, x, y, i, j))



class Hallway:
    def __init__(self, layout):
        self.layout = layout

    def room_done(self, room):
        x = ROOM_LOCATION[room]
        for y in range(2, 2 + roomSize(self.layout)):
            if not isInOwnRoom(self.layout, x, y):
                return False
        return True

    @property
    def all_done(self):
        return any(self.room_done(r) for r in ROOM_LOCATION.keys())


TRIED = {}


def solve(data):
    if data in TRIED:
        return TRIED[data]

    hall = Hallway(data)
    if hall.all_done:
        return 0

    costs = []
    for y in range(1, len(data)):
        for x in range(1, len(data[y])):
            amphipod = isAmphipod(data, x, y)
            if not amphipod:
                continue
            if canMove(data, x, y):
                room = ROOM_LOCATION[amphipod]
                if hasRoomAvailable(data, x, y) and isPathEmpty(data, x, room):
                    d, c = move(data, x, y, room, moveinPos(data, room))
                    cost = solve(d)
                    if cost >= 0:
                        costs.append(c + cost)
                elif isInAnyRoom(data, x, y):
                    for i in stoppable(data):
                        if not isPathEmpty(data, x, i):
                            continue
                        d, c = move(data, x, y, i, 1)
                        cost = solve(d)
                        if cost >= 0:
                            costs.append(c + cost)
    result = -1
    if costs:
        result = min(costs)
    TRIED[data] = result
    return result


def run_1():
    return solve(lines)


def run_2():
    return solve(extend(lines))


print(run_1())
print(run_2())
