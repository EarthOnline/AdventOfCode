from itertools import product
from math import floor, ceil
from re import findall

INPUT = open("./input_files/input_18", "r").read().strip("\n")
# INPUT = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
# INPUT = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]"""
NUMBERS = INPUT.split('\n')


def explode(number):
    depth = 0
    pair_to_reduce = 0
    for i, c in enumerate(number):
        if c == '[':
            depth += 1

        if c == ']':
            depth -= 1

        if depth == 5:
            pair_to_reduce = i
            break

    if pair_to_reduce == 0:
        return number

    part_1 = number[:pair_to_reduce]
    end = number.index(']', pair_to_reduce)
    x, y = [int(x) for x in number[pair_to_reduce + 1:end].split(',')]
    part_2 = number[end + 1:]
    left_numbers = findall(r'\d+', part_1)
    if len(left_numbers) > 0:
        old_number = left_numbers[-1]
        new_number = str(int(old_number) + x)
        replaces = len([x for x in left_numbers if old_number in x])
        part_1 = part_1.replace(old_number, 'X')
        part_1 = part_1.replace('X', old_number, replaces - 1)
        part_1 = part_1.replace('X', new_number)
    right_numbers = findall(r'\d+', part_2)
    if len(right_numbers) > 0:
        old_number = right_numbers[0]
        new_number = str(int(old_number) + y)
        part_2 = part_2.replace(old_number, new_number, 1)
    return part_1 + '0' + part_2


def split(number):
    numbers = [x for x in findall(r'\d+', number) if int(x) > 9]
    if len(numbers) == 0:
        return number

    replace = int(numbers[0])
    number = number.replace(str(replace), f'[{floor(replace / 2)},{ceil(replace / 2)}]', 1)
    return number


def reduce(number):
    while True:
        new_number = explode(number)
        if number != new_number:
            number = new_number
            continue

        new_number = split(number)
        if number != new_number:
            number = new_number
            continue

        break

    return new_number


def add(number_1, number_2):
    return reduce(f'[{number_1},{number_2}]')


def magnitude(number):
    replaceable = findall(r'\[\d+,\d+\]', number)
    while len(replaceable) > 0:
        for r in replaceable:
            x, y = [int(x) for x in r[1:-1].split(',')]
            number = number.replace(r, str(3*x + 2*y))
        replaceable = findall(r'\[\d+,\d+\]', number)
    return int(number)


def run_1():
    pref_number = None
    for number in NUMBERS:
        if pref_number:
            # print(pref_number, number)
            number = add(pref_number, number)
            # print('=', number)

        pref_number = number
    return magnitude(pref_number)


def run_2():
    return max(magnitude(add(x, y)) for x, y in product(NUMBERS, NUMBERS) if x != y)


print(run_1())
print(run_2())
