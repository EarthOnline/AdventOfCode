from typing import List, Optional, Dict


class IOPort:
    __instances = dict()

    @staticmethod
    def get_instance(proces_name: str):
        if proces_name in IOPort.__instances.keys():
            return IOPort.__instances[proces_name]
        return IOPort(proces_name)

    @staticmethod
    def clear_instances():
        IOPort.__instances = dict()

    def __init__(self, proces_name: str):
        IOPort.__instances[proces_name] = self

        self.inputs = list()
        self.outputs = list()
        self.wait_pointer = 0
        self.wait = False
        self.finished = False
        self.base = 0

    def get_input(self):
        return self.inputs.pop(0)

    def set_input(self, value):
        self.inputs.append(value)

    def get_output(self):
        if len(self.outputs) > 0:
            return self.outputs[-1]
        return None

    def set_output(self, value):
        self.outputs.append(value)


def add(int_sequence, pointer, param_1: int, param_2: int, output_3: int, **kwargs) -> int:
    int_sequence[output_3] = param_1 + param_2
    return pointer + 4


def multiply(int_sequence, pointer, param_1: int, param_2: int, output_3: int, **kwargs) -> int:
    int_sequence[output_3] = param_1 * param_2
    return pointer + 4


def get_input(int_sequence, pointer, output_1: int, proces_name, **kwargs) -> int:
    io = IOPort.get_instance(proces_name)
    if len(io.inputs) == 0:
        io.wait = True
        io.wait_pointer = pointer
        return
    int_sequence[output_1] = io.get_input()
    return pointer + 2


def set_output(_int_sequence, pointer, param_1: int, proces_name, **kwargs) -> int:
    IOPort.get_instance(proces_name).set_output(param_1)
    return pointer + 2


def jump_if_true(_int_sequence, pointer, param_1: int, param_2: int, **kwargs) -> int:
    if param_1 != 0:
        return param_2
    return pointer + 3


def jump_if_false(_int_sequence, pointer, param_1: int, param_2: int, **kwargs) -> int:
    if param_1 == 0:
        return param_2
    return pointer + 3


def less_than(int_sequence, pointer, param_1: int, param_2: int, output_3: int, **kwargs) -> int:
    int_sequence[output_3] = 1 if param_1 < param_2 else 0
    return pointer + 4


def equals(int_sequence, pointer, param_1: int, param_2: int, output_3: int, **kwargs) -> int:
    int_sequence[output_3] = 1 if param_1 == param_2 else 0
    return pointer + 4


def set_base(_int_sequence, pointer, param_1: int, proces_name, **kwargs) -> int:
    IOPort.get_instance(proces_name).base += param_1
    return pointer + 2


def read_param(process_name: str, int_sequence: List[int], pointer: int, offset, mode: int) -> Optional[int]:
    pointer += offset

    param = int_sequence[pointer]
    if mode == 1:
        return param

    if mode == 2:
        return int_sequence[param + IOPort.get_instance(process_name).base]
    return int_sequence[param]


class Done(EOFError):
    def __init__(self, *args, **kwargs):
        super(Done, self).__init__(*args, **kwargs)


def run_instruction(proces_name: str, int_sequence: Dict[int, int], pointer: int) -> int:
    instruction = f'{int_sequence[pointer]:05d}'
    opcode = int(instruction[-2:])
    param_mode_1 = int(instruction[-3])
    param_mode_2 = int(instruction[-4])
    param_mode_3 = int(instruction[-5])

    param_1 = read_param(proces_name, int_sequence, pointer, 1, param_mode_1)
    param_2 = read_param(proces_name, int_sequence, pointer, 2, param_mode_2)
    param_3 = read_param(proces_name, int_sequence, pointer, 3, param_mode_3)

    base = IOPort.get_instance(proces_name).base

    output_1 = int_sequence[pointer + 1] + base if param_mode_1 == 2 else int_sequence[pointer + 1]
    output_2 = int_sequence[pointer + 2] + base if param_mode_2 == 2 else int_sequence[pointer + 2]
    output_3 = int_sequence[pointer + 3] + base if param_mode_3 == 2 else int_sequence[pointer + 3]

    params = {'param_1': param_1, 'param_2': param_2, 'param_3': param_3,
              'output_1': output_1, 'output_2': output_2, 'output_3': output_3,
              'proces_name': proces_name}

    # print(pointer, opcode, param_mode_1, param_mode_2, param_mode_3, params)
    if opcode == 1:
        pointer = add(int_sequence, pointer, **params)
    if opcode == 2:
        pointer = multiply(int_sequence, pointer, **params)
    if opcode == 3:
        pointer = get_input(int_sequence, pointer, **params)
    if opcode == 4:
        pointer = set_output(int_sequence, pointer, **params)
    if opcode == 5:
        pointer = jump_if_true(int_sequence, pointer, **params)
    if opcode == 6:
        pointer = jump_if_false(int_sequence, pointer, **params)
    if opcode == 7:
        pointer = less_than(int_sequence, pointer, **params)
    if opcode == 8:
        pointer = equals(int_sequence, pointer, **params)
    if opcode == 9:
        pointer = set_base(int_sequence, pointer, **params)
    if opcode == 99:
        IOPort.get_instance(proces_name).finished = True
        return
    if opcode > 9 or opcode == 0:
        raise ValueError('')
    return pointer


def run_program(proces_name: str, int_sequence):
    io = IOPort.get_instance(proces_name)
    pointer = io.wait_pointer
    while io.finished is False and io.wait is False:
        pointer = run_instruction(proces_name, int_sequence, pointer)
