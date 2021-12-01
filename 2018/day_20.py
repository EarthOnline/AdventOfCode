from itertools import permutations
from typing import List

INPUT = open("./input_files/input_20", "r").read().strip("\n")
# INPUT = """^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""
# INPUT = """^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""


CIRCLE = 'NESW'

CIRCLES = permutations(CIRCLE)

HORIZONTAL = ['EW', 'WE']

VERTICAL = ['NS', 'SN']


def split_string(regex: str) -> List[str]:
    bracket = 0
    regexes = list()
    regexes.append('')

    for x in regex:
        if x == "|" and bracket == 0:
            regexes.append('')
            continue
        if x == "(":
            bracket += 1
        if x == ")":
            bracket -= 1
        regexes[-1] += x
    return regexes


def split_substring(regex: str) -> List[str]:
    bracket = 0
    regexes = list()
    regexes.append('')

    for x in regex:
        if x == "(":
            bracket += 1
            if bracket == 1:
                regexes.append('')
                continue
        if x == ")":
            bracket -= 1
            if bracket == 0:
                regexes.append('')
                continue
        regexes[-1] += x
    return regexes


def count_max_length(regex: str) -> int:
    count = list()

    for i, r in enumerate(split_string(regex)):
        count.append(0)
        substrings = split_substring(r)
        # print(r, substrings)

        if len(substrings) == 1:
            count[i] += len(substrings[0])
            continue
        for x in split_substring(r):
            count[i] += count_max_length(x)
    return max(count)


def get_paths(regex: str) -> List[str]:
    paths = list()

    active_paths = list()
    active_depth = 0
    active_paths.append('')

    for x in regex:
        if x == '(':
            active_depth += 1
            if active_depth >= len(active_paths):
                active_paths.append('')
            continue
        if x == ')':
            active_paths[active_depth] = ''
            active_depth -= 1
            continue
        if x == '|':
            active_paths[active_depth] = ''
            continue
        active_paths[active_depth] += x
        paths.append(''.join(active_paths[:active_depth + 1]))
    return paths


def clean_regex(regex: str) -> str:
    prev_regex = ''
    while prev_regex != regex:
        prev_regex = regex
        for x in CIRCLES:
            regex = regex.replace("".join(x), "")
        for x in HORIZONTAL:
            regex = regex.replace(x, '')
        for x in VERTICAL:
            regex = regex.replace(x, '')
    return regex


def run_1():
    regex = clean_regex(INPUT.replace("^", "").replace("$", ""))
    return count_max_length(regex)


def run_2():
    regex = INPUT.replace("^", "").replace("$", "")
    paths = get_paths(regex)

    clean_paths = set()
    for path in paths:
        clean_paths.add(clean_regex(path))
    return len([x for x in clean_paths if len(x) >= 1000])


print(run_1())
print(run_2())
