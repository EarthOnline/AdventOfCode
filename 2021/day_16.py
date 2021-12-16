from functools import reduce
from operator import mul

INPUT = open("./input_files/input_16", "r").read().strip("\n")
# INPUT = "D2FE28"
# INPUT = "38006F45291200"
# INPUT = "EE00D40C823060"
# INPUT = "8A004A801A8002F478"
# INPUT = "A0016C880162017C3686B18A3D4780"
# INPUT = "9C0141080250320F1802104A08"
BIN = ''.join(bin(int(i, 16))[2:].zfill(4) for i in INPUT)


ID_FUNCTIONS = {
    0: lambda x: sum(x),
    1: lambda x: reduce(mul, x),
    2: lambda x: min(x),
    3: lambda x: max(x),
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1]
}


class Reader:
    def __init__(self, content: str, pointer=0):
        self.content = content
        self.pointer = pointer

    def update_pointer(self, size: int):
        yield self.pointer
        self.pointer += size
        yield self.pointer

    def read(self, size: int = 1):
        start, end = self.update_pointer(size)
        return self.content[start:end]

    def read_int(self, size: int = 1):
        return int(self.read(size), 2)

    def read_literal(self):
        value = ''
        read_next = True
        while read_next:
            read_next = self.read_int()
            value += self.read(4)
        return int(value, 2)


def read_packet(text: str, start=0):
    reader = Reader(text, start)

    version = reader.read_int(3)
    action_id = reader.read_int(3)
    if action_id == 4:
        return version, reader.read_literal(), reader.pointer

    versions = [version]
    results = []

    def read_sub_packet():
        sub_version, result, reader.pointer = read_packet(text, reader.pointer)
        versions.append(sub_version)
        results.append(result)

    if reader.read() == '0':
        end = reader.read_int(15) + reader.pointer
        while reader.pointer < end:
            read_sub_packet()
    else:
        for _ in range(reader.read_int(11)):
            read_sub_packet()

    return sum(versions), ID_FUNCTIONS.get(action_id, lambda x: 0)(results), reader.pointer


def run_1():
    sum_of_version, result, pointer = read_packet(BIN)
    return sum_of_version


def run_2():
    sum_of_version, result, pointer = read_packet(BIN)
    return result


print(run_1())
print(run_2())
