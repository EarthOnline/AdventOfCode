from typing import Dict

INPUT = open("./input_files/input_02", "r").read().strip("\n")
_PASSWORDS = [x.split(' ') for x in INPUT.split('\n')]
PASSWORDS = [dict(policy=[int(r) for r in x[0].split('-')], char=x[1][:-1], password=x[2]) for x in _PASSWORDS]


def policy_check_1(password: Dict) -> bool:
    return password['password'].count(password['char']) in range(password['policy'][0], password['policy'][1] + 1)


def run_1():
    return len([x['password'] for x in PASSWORDS if policy_check_1(x)])


def policy_check_2(password: Dict) -> bool:
    chars_to_check = password['password'][password['policy'][0] - 1] + password['password'][password['policy'][1] - 1]
    return chars_to_check.count(password['char']) == 1


def run_2():
    return len([x['password'] for x in PASSWORDS if policy_check_2(x)])


print(run_1())
print(run_2())
