from hashlib import md5

INPUT = "bgvyzdsv"


def run_1():
    index = 0

    while True:
        hasher = md5()
        hasher.update(f'{INPUT}{index}'.encode('UTF-8'))
        if hasher.hexdigest()[:5] == '00000':
            break
        index += 1
    return index


def run_2():
    index = 0

    while True:
        hasher = md5()
        hasher.update(f'{INPUT}{index}'.encode('UTF-8'))
        if hasher.hexdigest()[:6] == '000000':
            break
        index += 1
    return index


print(run_1())
print(run_2())
