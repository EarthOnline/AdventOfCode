from typing import Dict

INPUT = open("./input_files/input_19", "r").read().strip("\n")


X = 'x'
Y = 'y'
HORIZONTAL = '-'
VERTICAL = '|'
END = '+'


class RoutingDiagram:
    @staticmethod
    def north(position: Dict[str, int]) -> Dict[str, int]:
        return dict(x=position[X], y=position[Y] - 1)

    @staticmethod
    def east(position: Dict[str, int]) -> Dict[str, int]:
        return dict(x=position[X] + 1, y=position[Y])

    @staticmethod
    def south(position: Dict[str, int]) -> Dict[str, int]:
        return dict(x=position[X], y=position[Y] + 1)

    @staticmethod
    def west(position: Dict[str, int]) -> Dict[str, int]:
        return dict(x=position[X] - 1, y=position[Y])

    def new_direction(self):
        if self.direction in [RoutingDiagram.north, RoutingDiagram.south]:
            if self.get_value(RoutingDiagram.east(self.position)) == HORIZONTAL:
                self.direction = RoutingDiagram.east
            else:
                self.direction = RoutingDiagram.west
        elif self.direction in [RoutingDiagram.east, RoutingDiagram.west]:
            if self.get_value(RoutingDiagram.south(self.position)) == VERTICAL:
                self.direction = RoutingDiagram.south
            else:
                self.direction = RoutingDiagram.north
        else:
            self.direction = None

    def __init__(self, input: str):
        self.routing = input.split("\n")
        self.position = dict(x=self.routing[0].index('|'), y=0)
        self.direction = RoutingDiagram.south
        self.text = list()
        self.steps = 0

    def get_value(self, position: Dict[str, int] = None) -> str:
        position = self.position if position is None else position
        return self.routing[position[Y]][position[X]]

    def move(self):
        self.position = self.direction(self.position)
        value = self.get_value()
        self.steps += 1

        if value == END:
            self.new_direction()
        elif value == ' ':
            self.direction = None
        elif value in [HORIZONTAL, VERTICAL]:
            pass
        else:
            self.text.append(value)

    def get_text(self):
        return ''.join(self.text)


def run_1():
    rd = RoutingDiagram(INPUT)

    while rd.direction is not None:
        rd.move()
    return rd.get_text()


def run_2():
    rd = RoutingDiagram(INPUT)

    while rd.direction is not None:
        rd.move()
    return rd.steps


print(run_1())
print(run_2())
