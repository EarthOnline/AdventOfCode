import string
from itertools import groupby
from typing import List

INPUT = "hepxcrrq"

ALPHABET = string.ascii_lowercase
BANNED = 'iol'


def increment_password(password: List[int]) -> List[int]:
    for index, char in enumerate(password):
        char = (char + 1) % 26
        password[index] = char
        if char != 0:
            break
    return password


def meet_requirements(password: List[int]) -> bool:
    if len([x for x in password if ALPHABET[x] in BANNED]):
        return False
    if len([x for x, y in groupby(password) if len(list(y)) > 1]) <= 1:
        return False
    if len([x for x in range(len(password) - 2) if password[x + 2] + 2 == password[x + 1] + 1 == password[x]]) == 0:
        return False
    return True


def generate_password(password: str) -> str:
    password_list = list(reversed([ALPHABET.index(x) for x in password]))

    while True:
        password_list = increment_password(password_list)
        if meet_requirements(password_list):
            break
    return ''.join([ALPHABET[x] for x in reversed(password_list)])


def run_1():
    return generate_password(INPUT)


def run_2():
    return generate_password(generate_password(INPUT))


print(run_1())
print(run_2())
