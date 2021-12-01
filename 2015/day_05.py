import string

INPUT = open("./input_files/input_05", "r").read().strip("\n")


VOWELS = 'aeiou'
DUBBEL = [f'{x}{x}' for x in string.ascii_lowercase]
BANNED = ['ab', 'cd', 'pq', 'xy']


def is_nice(word: str) -> bool:
    result = len([x for x in word if x in VOWELS]) >= 3
    result &= len([x for x in DUBBEL if x in word]) > 0
    result &= len([x for x in BANNED if x in word]) == 0
    return result


def is_nicer(word: str) -> bool:
    sets = list()
    result_1 = False
    result_2 = False
    prev_set = None
    for x in range(len(word) - 1):
        set = f'{word[x]}{word[x + 1]}'
        if set in sets:
            result_1 = True
            break
        sets.append(prev_set)
        prev_set = set

    for x in range(len(word) - 2):
        if word[x] == word[x + 2]:
            result_2 = True
            break
    return result_1 and result_2


def run_1():
    return len([x for x in INPUT.split("\n") if is_nice(x)])


def run_2():
    return len([x for x in INPUT.split("\n") if is_nicer(x)])


print(run_1())
print(run_2())
