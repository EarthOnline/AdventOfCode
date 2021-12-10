from functools import reduce

INPUT = open("./input_files/input_10", "r").read().strip("\n")
# INPUT = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""
LINES = INPUT.split('\n')


OPENED_BY = {
    ')': '(',
    ']': '[' ,
    '}': '{',
    '>': '<'
}


POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

MORE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def debugger(line: str, debug_type: str):
    open = []
    start_points = OPENED_BY.values()
    end_points = OPENED_BY.keys()

    for l in line:
        if l in start_points:
            open.append(l)
            continue

        if l in end_points and OPENED_BY[l] == open[-1]:
            open.pop()
            continue

        if debug_type == 'first_illegal':
            return l

    if debug_type == 'first_illegal':
        return ''
    if debug_type == 'repair':
        closed_by = {v: k for k, v in OPENED_BY.items()}
        return ''.join(closed_by[o] for o in open[::-1])


def first_illegal(line: str):
    return debugger(line, 'first_illegal')


def repair(line: str):
    return debugger(line, 'repair')


def score(sequence: str):
    # score = 0
    # for s in sequence:
    #     score *= 5
    #     score += MORE_POINTS[s]
    #
    # return score
    return reduce(lambda x, y: x * 5 + MORE_POINTS[y], sequence, 0)  # initial 0


def run_1():
    return sum(POINTS.get(first_illegal(l), 0) for l in LINES)


def run_2():
    scores = sorted(score(repair(l)) for l in LINES if first_illegal(l) == '')
    return scores[len(scores) // 2]


print(run_1())
print(run_2())
