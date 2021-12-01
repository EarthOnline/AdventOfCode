INPUT = "074501"


def run_1():
    tries = int(INPUT)
    scores = [3, 7]
    elf_1 = 0
    elf_2 = 1

    while len(scores) < tries + 10:
        score_1 = scores[elf_1]
        score_2 = scores[elf_2]

        for score in str(score_1 + score_2):
            scores.append(int(score))
        elf_1 = (elf_1 + score_1 + 1) % len(scores)
        elf_2 = (elf_2 + score_2 + 1) % len(scores)

    return "".join([str(x) for x in scores[tries:tries + 10]])


def run_2():
    scores = [3, 7]
    elf_1 = 0
    elf_2 = 1

    find_score = [int(x) for x in INPUT]

    while find_score != scores[-6:] and find_score != scores[-7:-1]:
        score_1 = scores[elf_1]
        score_2 = scores[elf_2]

        for score in str(score_1 + score_2):
            scores.append(int(score))
        elf_1 = (elf_1 + score_1 + 1) % len(scores)
        elf_2 = (elf_2 + score_2 + 1) % len(scores)

    return len(scores) - len(find_score) - (0 if find_score == scores[-6:] else 1)


print(run_1())
print(run_2())
