from functools import reduce

INPUT = open("./input_files/input_10", "r").read().strip("\n")


def get_value(hash, index, lenght):
    hash_length = len(hash)

    result = list()
    ranges = list()

    end = index + lenght
    if end >= hash_length:
        ranges.append((index, None))
        ranges.append((None, end - hash_length))
    else:
        ranges.append((index, end))

    for r in ranges:
        result.extend(hash[r[0]:r[1]])
    return result


def set_value(hash, index, value):
    hash_lenght = len(hash)
    value_lenght = len(value)

    end = index + value_lenght
    overrun = end - hash_lenght
    if end > hash_lenght:
        hash[index:] = value[: 0 - overrun]
        hash[:overrun] = value[0 - overrun:]
    else:
        hash[index:end] = value
    return hash


def run_1():
    lenghts = [int(x) for x in INPUT.split(",")]
    hash = list(range(256))
    skip_size = 0
    index = 0

    for length in lenghts:
        value = (get_value(hash, index, length))
        value.reverse()
        set_value(hash, index, value)

        index = (index + length + skip_size) % len(hash)
        skip_size += 1
    return hash[0] * hash[1]


def knot_hash(input: str) -> str:
    lenghts = [ord(x) for x in input] + [17, 31, 73, 47, 23]

    hash = list(range(256))
    skip_size = 0
    index = 0

    for _x in range(64):
        for length in lenghts:
            value = (get_value(hash, index, length))
            value.reverse()
            set_value(hash, index, value)

            index = (index + length + skip_size) % len(hash)
            skip_size += 1

    condensed_hash = list()
    for index in range(len(hash) // 16):
        condensed_hash.append(reduce(lambda x, y: x ^ y, hash[index * 16:(index + 1) * 16]))

    return "".join([hex(x)[2:].zfill(2) for x in condensed_hash])


def run_2():
    return knot_hash(INPUT)


if __name__ == '__main__':
    print(run_1())
    print(run_2())
