INPUT = open("./input_files/input_07", "r").read().strip("\n")

TERMINAL = INPUT.split('\n')


class FileSystem:
    def __init__(self):
        self.filesystem = self._read_filesystem()
        self.dir_sizes = []
        self.root_size = self.dir_size(self.filesystem)

    @staticmethod
    def _read_filesystem():
        fileystem = {'/': {}}
        pointer = [fileystem]
        for command in TERMINAL:
            match command[:4]:
                case '$ cd':
                    dir = command[5:]
                    if dir == '..':
                        pointer.pop()
                    else:
                        pointer.append(pointer[-1].get(dir))
                case '$ ls':
                    pass
                case _:
                    size, name = command.split(' ')
                    if size == 'dir':
                        pointer[-1][name] = {}
                    else:
                        size = int(size)
                        pointer[-1][name] = size
        return fileystem

    def dir_size(self, dir):
        size = 0
        for k, v in dir.items():
            if type(v) == dict:
                _size = self.dir_size(v)
                size += _size
                self.dir_sizes.append(_size)
            else:
                size += v
        return size


FILESYSTEM = FileSystem()


def run_1():
    return sum(x for x in FILESYSTEM.dir_sizes if x <= 100000)


def run_2():
    space = 70000000 - FILESYSTEM.root_size
    needed = 30000000 - space
    return sorted(x for x in FILESYSTEM.dir_sizes if x >= needed)[0]


print(run_1())
print(run_2())
