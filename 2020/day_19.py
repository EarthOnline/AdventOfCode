from itertools import product

INPUT = open("./input_files/input_19", "r").read().strip("\n").split('\n')
RULES = {k: v for k, v in [r.split(': ') for r in INPUT[:INPUT.index('')]]}
MESSAGES = INPUT[INPUT.index('') + 1:]


def valid_messages(key):
    if key == '':
        return {''}

    if not key.isnumeric():
        return {key[1]}

    rules = RULES[key].split(' | ')
    results = set()
    for rule in rules:
        sets = list(product(*[valid_messages(k) for k in rule.split(' ')]))
        results = results.union([''.join(s) for s in sets])
    return results


def run_1():
    valids = valid_messages('0')
    return len([m for m in MESSAGES if m in valids])


def run_2():
    r42 = valid_messages('42')
    r31 = valid_messages('31')

    valid = 0
    for message in MESSAGES:
        count_31 = 0
        count_42 = 0

        if len(message) % 8 != 0:
            continue

        pieces = [message[i:i+8] for i in range(0, len(message), 8)]
        stop = False
        for piece in pieces[::-1]:
            if count_42 == 0 and piece in r31:
                count_31 += 1
            elif piece in r42:
                count_42 += 1
            else:
                stop = True
                break
        if stop:
            continue

        if count_31 > 0 and (count_42 - count_31) > 0:
            valid += 1
            print(message, count_42, count_31)

    return valid


print(run_1())
print(run_2())
