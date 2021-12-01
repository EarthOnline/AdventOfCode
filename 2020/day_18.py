from functools import reduce

INPUT = open("./input_files/input_18", "r").read().strip("\n")


def breakup(string, calculator):
    sequence = list()
    lock = 0
    sub_sequence = list()
    for s in string:
        if s == '(':
            lock += 1
            if lock == 1:
                continue

        if s == ')':
            lock -= 1
            if lock == 0:
                sequence.append(calculator(''.join(sub_sequence)))
                sub_sequence = list()
                continue

        if lock:
            sub_sequence.append(s)
            continue

        if s.isnumeric():
            sequence.append(int(s))
            continue

        sequence.append(s)
    return sequence


def calculate(string):
    sequence = breakup(string, calculate)

    result = 0
    opperator = '+'
    for index, value in enumerate(sequence):
        if index % 2:
            opperator = value
            continue

        if opperator == '+':
            result += value

        if opperator == '*':
            result *= value

    return result


def run_1():
    return sum(calculate(string.replace(' ', '')) for string in INPUT.split('\n'))


def calculate_advanced(string):
    sequence = breakup(string, calculate_advanced)

    result = [0]
    opperator = '+'
    for index, value in enumerate(sequence):
        if index % 2:
            opperator = value
            continue

        if opperator == '+':
            result[-1] += value

        if opperator == '*':
            result.append(value)

    return reduce(lambda x, y: x * y, result)


def run_2():
    return sum(calculate_advanced(string.replace(' ', '')) for string in INPUT.split('\n'))

print(run_1())
print(run_2())
