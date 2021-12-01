from collections import defaultdict
from functools import reduce
from itertools import chain

INPUT = open("./input_files/input_16", "r").read().strip("\n").split('\n')


def run_1():
    line = 0
    valid_numbers = set()
    while True:
        input = INPUT[line]
        line += 1
        if input == '':
            break

        ranges = input[input.find(':') + 2:].split(' or ')
        for r in ranges:
            start, end = [int(x) for x in r.split('-')]
            valid_numbers = valid_numbers.union(range(start, end + 1))

    line += 4
    invalid_numbers = list()
    for input in INPUT[line:]:
        invalid_numbers.extend([int(x) for x in input.split(',') if int(x) not in valid_numbers])

    return sum(invalid_numbers)


def get_valid_numbers(ranges: str):
    valid_numbers = set()
    ranges = ranges.split(' or ')
    for r in ranges:
        start, end = [int(x) for x in r.split('-')]
        valid_numbers = valid_numbers.union(range(start, end + 1))
    return valid_numbers


def run_2():
    fields = list()
    for field in INPUT[:INPUT.index('')]:
        fields.append(dict(label=field[:field.index(':')],
                           valid_numbers=get_valid_numbers(field[field.index(':') + 2:])))
    valid_numers = set(chain.from_iterable(f['valid_numbers'] for f in fields))

    tickets = [[int(x) for x in i.split(',')] for i in INPUT[INPUT.index('nearby tickets:') + 1:]]
    valid_tickets = [t for t in tickets if all([x in valid_numers for x in t])]
    field_values = defaultdict(set)
    for ticket in valid_tickets:
        for index, value in enumerate(ticket):
            field_values[index].add(value)

    valid_fields = defaultdict(list)
    for index, values in field_values.items():
        for field in fields:
            if all(v in field['valid_numbers'] for v in values):
                valid_fields[index].append(field['label'])

    while max(len(l) for l in valid_fields.values()) > 1:
        solved = [l[0] for l in valid_fields.values() if len(l) == 1]
        valid_fields = {k: [x for x in v if x not in solved] if len(v) > 1 else v for k, v in valid_fields.items()}

    my_ticket = [int(x) for x in INPUT[INPUT.index('your ticket:') + 1].split(',')]
    return reduce(lambda x, y: x * y,
                  [x for i, x in enumerate(my_ticket) if valid_fields[i][0].startswith('departure')])


print(run_1())
print(run_2())
