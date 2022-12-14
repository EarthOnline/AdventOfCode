INPUT = open("./input_files/input_10", "r").read().strip("\n")

INSTRUCTIONS = [(y[0], int(y[1]) if len(y) > 1 else None) for y in [x.split(' ') for x in INPUT.split('\n')]]


class Screen:
    def __init__(self):
        self.cycles = 1
        self.register = 1

        self.signal_strength = 0

        self.screen_buffer = []

    def _add_cycle(self):
        self.signal_strength += self.cycles * self.register if self.cycles % 40 - 20 == 0 else 0

        self.screen_buffer.append('#' if (self.cycles - 1) % 40 in [self.register + x for x in (-1, 0, 1)] else ' ')

        self.cycles += 1

    def _action(self, instruction):
        command, value = instruction
        match command:
            case 'noop':
                self._add_cycle()
            case 'addx':
                self._add_cycle()
                self._add_cycle()
                self.register += value

    def run(self, instructions):
        for instruction in instructions:
            self._action(instruction)

    def draw_screen(self):
        buffer = self.screen_buffer
        print(''.join('-' for _ in range(80)))
        while buffer:
            print(' '.join(buffer[:40]))
            buffer = buffer[40:]
        print(''.join('-' for _ in range(80)))


def run_1_2():
    screen = Screen()
    screen.run(INSTRUCTIONS)
    print(screen.signal_strength)
    screen.draw_screen()


run_1_2()
