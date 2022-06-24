INPUT = open("./input_files/input_24", "r").read().strip("\n")
MONAD = [x.split() for x in INPUT.splitlines()]


class ALU:
    def __init__(self, serial_number):
        self.memory = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        self.buffer = [int(x) for x in serial_number]

    def _get_or_int(self, value):
        if value in self.memory.keys():
            return self.memory[value]
        return int(value)

    def inp(self, a):
        self.memory[a] = self.buffer.pop(0)

    def add(self, a, b):
        self.memory[a] += self._get_or_int(b)

    def mul(self, a, b):
        self.memory[a] *= self._get_or_int(b)

    def div(self, a, b):
        self.memory[a] //= self._get_or_int(b)

    def mod(self, a, b):
        self.memory[a] = self.memory[a] % self._get_or_int(b)

    def eql(self, a, b):
        self.memory[a] = 1 if self.memory[a] == self._get_or_int(b) else 0

    def run(self):
        for instruction in MONAD:
            getattr(self, instruction[0])(*instruction[1:])
        return self.memory['z']


def solve(maximum=True):
    per_import = [x.splitlines() for x in INPUT.split('inp w\n')[1:]]
    special_lines = [i for i, instruction in enumerate(per_import[0]) if any(pi[i] != instruction for pi in per_import)]
    match_stack = []
    result = ['' for _ in range(14)]
    for position, pi in enumerate(per_import):
        special_values = [int(pi[sl].split()[-1]) for sl in special_lines]
        if special_values[0] == 1:
            match_stack.append((position, special_values[2]))

        if special_values[0] == 26:
            match_position, value = match_stack.pop()
            adjust = value + special_values[1]
            if adjust < 0:
                adjust = abs(adjust)
                position, match_position = match_position, position
            result[position] = '9' if maximum else str(1 + adjust)
            result[match_position] = str(9 - adjust) if maximum else '1'
    return ''.join(result)


def run_1():
    # serial_number = ''.join('9' for _ in range(14))
    # while True:
    #     if '0' not in serial_number:
    #         alu = ALU(serial_number)
    #         if alu.run() == 0:
    #             return serial_number
    #
    #     serial_number = str(int(serial_number) - 1)
    #     continue
    return solve()


def run_2():
    # serial_number = ''.join('1' for _ in range(14))
    # while True:
    #     if '0' not in serial_number:
    #         alu = ALU(serial_number)
    #         if alu.run() == 0:
    #             return serial_number
    #
    #     serial_number = str(int(serial_number) + 1)
    #     continue
    return solve(maximum=False)


print(run_1())
print(run_2())
