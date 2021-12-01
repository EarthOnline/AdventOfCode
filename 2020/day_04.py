INPUT = open("./input_files/input_04", "r").read().strip("\n")

PASSPORTS = [{kv.split(':')[0]: kv.split(':')[1] for kv in p.replace('\n', ' ').split(' ')}
             for p in INPUT.split("\n\n")]

MANDITORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
CHECKS = dict(byr=lambda x: 1920 <= int(x) <= 2002,
              iyr=lambda x: 2010 <= int(x) <= 2020,
              eyr=lambda x: 2020 <= int(x) <= 2030,
              hgt=lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else
              59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else
              False,
              hcl=lambda x: x[0] == '#' and len(x[1:]) == 6 and all([c in '0123456789abcdef' for c in x[1:]]),
              ecl=lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
              pid=lambda x: len(x) == 9 and x.isnumeric())


def check_wrapper(check, value):
    try:
        return check(value)
    except:
        return False


def run_1():
    return len([p for p in PASSPORTS if all(f in p.keys() for f in MANDITORY_FIELDS)])


def run_2():
    return len([p for p in PASSPORTS if all(check_wrapper(check, p.get(label, '')) for label, check in CHECKS.items())])


print(run_1())
print(run_2())
