from multiprocessing.sharedctypes import copy

INPUT = open("./input_files/input_13", "r").read().strip("\n")
# INPUT = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5"""


def translate(text: str):
    text = text.split('\n\n')
    dots = [(int(x), int(y)) for x, y in [d.split(',') for d in text[0].split('\n')]]
    intructions = [(k, int(v)) for k, v in [x.split(' ')[-1].split('=') for x in text[1].split('\n')]]

    return dots, intructions


DOTS, INSTRUCTIONS = translate(INPUT)


def fold(paper, instruction):
    fold_type, position = instruction

    if fold_type == 'y':
        return set([(x, y) for x, y in paper if y < position] +
                   [(x, position - (y - position)) for x, y in paper if y > position])
    if fold_type == 'x':
        return set([(x, y) for x, y in paper if x < position] +
                   [(position - (x - position), y) for x, y in paper if x > position])


def print_paper(paper):
    min_x = min(x for x, y in paper)
    max_x = max(x for x, y in paper)
    min_y = min(y for x, y in paper)
    max_y = max(y for x, y in paper)

    for y in range(min_y, max_y + 1):
        print(''.join('#' if (x, y) in paper else ' ' for x in range(min_x, max_x + 1)))
    print()


def run_1():
    return len(fold(DOTS, INSTRUCTIONS[0]))


def run_2():
    paper = DOTS
    for instruction in INSTRUCTIONS:
        paper = fold(paper, instruction)
    print_paper(paper)
    return None


print(run_1())
print(run_2())
