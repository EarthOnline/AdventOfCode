INPUT = open("./input_files/input_10", "r").read().strip("\n")


class Light:
    def __init__(self, light: str):
        self.position_y = int(light[10:16])
        self.position_x = int(light[18:24])
        self.velocity_y = int(light[36:38])
        self.velocity_x = int(light[40:42])

    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

    def move_back(self):
        self.position_x -= self.velocity_x
        self.position_y -= self.velocity_y


def get_lights():
    return [Light(x) for x in INPUT.split("\n")]


LIGHTS = get_lights()


def run_1():
    second = 0
    width = None

    while True:
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        for light in LIGHTS:
            light.move()
            min_x = min(min_x, light.position_x)
            max_x = max(max_x, light.position_x)
            min_y = min(min_y, light.position_y)
            max_y = max(max_y, light.position_y)
        second += 1
        new_width = max_x - min_x
        if width is None or new_width < width:
            width = new_width
        else:
            for light in LIGHTS:
                light.move_back()
            lights = [(light.position_x, light.position_y) for light in LIGHTS]
            for x in range(min_x, max_x + 1):
                line = list()
                for y in range(min_y, max_y + 1):
                    line.append("#" if (x, y) in lights else ".")
                print("".join(line))
            break
    return second - 1


print(run_1())
