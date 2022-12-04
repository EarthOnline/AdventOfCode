INPUT = open("./input_files/input_23", "r").read().strip("\n")


def jmp_cln(value):
    return int(value.replace('+', '')) if '+' in value or '-' in value else value


INSTRUCTIONS = [tuple(jmp_cln(y) for y in x.replace(',', '').split(' ')) for x in INPUT.split('\n')]


def run_program(start_a=0, start_b=0):
    register = {'a': start_a, 'b': start_b}
    pointer = 0
    while pointer < len(INSTRUCTIONS):
        instuction = INSTRUCTIONS[pointer]
        match instuction[0]:
            case 'hlf':
                register[instuction[1]] //= 2
                pointer += 1
            case 'tpl':
                register[instuction[1]] *= 3
                pointer += 1
            case 'inc':
                register[instuction[1]] += 1
                pointer += 1
            case 'jmp':
                pointer += instuction[1]
            case 'jie':
                pointer += instuction[2] if register[instuction[1]] % 2 == 0 else 1
            case 'jio':
                pointer += instuction[2] if register[instuction[1]] == 1 else 1
    return register


def run_1():
    return run_program()['b']


def run_2():
    return run_program(start_a=1)['b']


print(run_1())
print(run_2())
