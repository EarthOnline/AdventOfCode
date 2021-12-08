from collections import defaultdict
from itertools import chain

from typing import List

INPUT = open("./input_files/input_08", "r").read().strip("\n")
# INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# fgae cfgab fg bagce""".replace("|\n", "|")
NOTES = [[[''.join(sorted(d)) for d in i.strip().split(" ")] for i in x.split("|")] for x in INPUT.split("\n")]


def run_1():
    return sum(len(o) in (2, 4, 3, 7) for o in chain.from_iterable(x[1] for x in NOTES))


def first(_list):
    return _list[0]


def solve_segment(input: List[str], output: List[str]) -> int:
    by_lenght = defaultdict(list)

    for note in input:
        by_lenght[len(note)].append(note)

    digit_1 = first(by_lenght[2])
    digit_4 = first(by_lenght[4])
    digit_7 = first(by_lenght[3])
    digit_8 = first(by_lenght[7])
    digit_6 = first([n for n in by_lenght[6] if not all(x in n for x in digit_1)])
    digit_9 = first([n for n in by_lenght[6] if all(x in n for x in digit_4)])
    digit_0 = first([n for n in by_lenght[6] if n != digit_6 and n != digit_9])
    digit_3 = first([n for n in by_lenght[5] if all(x in n for x in digit_1)])
    f = first([x for x in digit_6 if x in digit_1])
    digit_5 = first([n for n in by_lenght[5] if n != digit_3 and any(x == f for x in n)])
    digit_2 = first([n for n in by_lenght[5] if n != digit_3 and n != digit_5])

    # print(digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9)

    digit_map = {
        digit_0: '0',
        digit_1: '1',
        digit_2: '2',
        digit_3: '3',
        digit_4: '4',
        digit_5: '5',
        digit_6: '6',
        digit_7: '7',
        digit_8: '8',
        digit_9: '9'
    }
    return int(''.join(map(digit_map.get, output)))


def run_2():
    return sum([solve_segment(x[0], x[1]) for x in NOTES])


print(run_1())
print(run_2())
