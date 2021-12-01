from builtins import sorted

INPUT = '264793-803935'

RANGE = [int(x) for x in INPUT.split('-')]

# RANGE = [137683, 596253]

DOUBLE = [f'{x}{x}' for x in range(10)]




def run_1():
    valid_passwords = 0
    # for x in range(RANGE[0], RANGE[1] + 1):
    #     x = str(x)
    #
    # #     double = False
    # #     for d in DOUBLE:
    # #         double |= d in x
    # #         if double:
    # #             break
    # #     if not double:
    # #         continue
    # #
    # #     increasing = True
    # #     prev = 0
    # #     for c in x:
    # #         c = int(c)
    # #         increasing &= c >= prev
    # #         prev = c
    # #         if not increasing:
    # #             break
    # #     if not increasing:
    # #         continue
    # #
    # #     valid_passwords += 1
    #
    #     valid_passwords += 1 if sorted(x) == list(x) and max([list(x).count(str(n)) for n in range(10)]) > 1 else 0
    # return valid_passwords
    return len([x for x in [str(r) for r in range(RANGE[0], RANGE[1] + 1)] if sorted(x) == list(x) and max([list(x).count(str(n)) for n in range(10)]) > 1])


def run_2():
    valid_passwords = 0
    for x in range(RANGE[0], RANGE[1] + 1):
        x = str(x)

        # double = False
        # current = ''
        # count = 0
        # for c in x:
        #     if current == c:
        #         count += 1
        #     else:
        #         double |= count == 2
        #         current = c
        #         count = 1
        #     if double:
        #         break
        # double |= count == 2
        # if not double:
        #     continue
        #
        # increasing = True
        # prev = 0
        # for c in x:
        #     c = int(c)
        #     increasing &= c >= prev
        #     prev = c
        #     if not increasing:
        #         break
        # if not increasing:
        #     continue
        #
        # valid_passwords += 1

        valid_passwords += 1 if sorted(x) == list(x) and 2 in [list(x).count(str(n)) for n in range(10)] else 0
    return valid_passwords


print(run_1())
print(run_2())
